// Optional standalone recorder. Run the local preview server first.
import { chromium } from 'playwright';
import fs from 'node:fs/promises';
import path from 'node:path';
const url = process.argv[2] || 'http://127.0.0.1:8775/';
if (!['127.0.0.1', 'localhost'].includes(new URL(url).hostname)) throw new Error('Use a local demo URL');
const dir = path.resolve('work/capture');
await fs.mkdir(dir, { recursive: true });
const browser = await chromium.launch({headless:true});
try {
  const page = await browser.newPage({viewport:{width:1200,height:900},deviceScaleFactor:2});
  await page.goto(`${url}${url.includes('?')?'&':'?'}autoplay=0`);
  await page.evaluate(async()=>{await document.fonts.ready; await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
  const cdp = await page.context().newCDPSession(page);
  const frames = [], writes = [];
  cdp.on('Page.screencastFrame', event => {
    const file = `${String(frames.length).padStart(5,'0')}.jpg`;
    frames.push({file,timestamp:event.metadata.timestamp});
    writes.push(fs.writeFile(path.join(dir,file), Buffer.from(event.data,'base64')));
    void cdp.send('Page.screencastFrameAck',{sessionId:event.sessionId});
  });
  await cdp.send('Page.startScreencast',{format:'jpeg',quality:98,maxWidth:2400,maxHeight:1800,everyNthFrame:1});
  await page.waitForTimeout(5000);
  await page.evaluate(()=>begin());
  await page.waitForTimeout(41000);
  await cdp.send('Page.stopScreencast');
  await Promise.all(writes);
  if(frames.length<100) throw new Error(`Too few frames: ${frames.length}`);
  await fs.writeFile(path.join(dir,'manifest.json'),JSON.stringify({frames},null,2));
  console.log(`Saved ${frames.length} changed frames. Static screens naturally emit fewer frames.`);
} finally {await browser.close();}
