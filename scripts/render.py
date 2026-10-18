from pathlib import Path
import json,math,bisect
import av
from PIL import Image,ImageDraw,ImageFilter,ImageFont
root=Path(__file__).resolve().parents[1]
cap=root/'work/capture';out=root/'exports';out.mkdir(exist_ok=True);m=json.loads((cap/'manifest.json').read_text());frames=m['frames'];t0=frames[0]['timestamp'];times=[f['timestamp']-t0 for f in frames]
fps=60;duration=46
# Zoom, source center, and timing. Every transition uses a smooth ease.
# Keep the complete dashboard visible; move the entire frame instead of cropping either column.
keys=[(0,.965,600,450),(5.5,.965,600,450),(8,1,600,450),(12,1,600,450),
(14,.98,600,450),(18,1,600,450),(25,1,600,450),(28,.98,600,450),
(32,1,600,450),(39,1,600,450),(42,1,600,450),(46,.98,600,450)]

def camera(t):
 for a,b in zip(keys,keys[1:]):
  if a[0]<=t<=b[0]:
   q=(t-a[0])/(b[0]-a[0]);q=q*q*q*(q*(q*6-15)+10)
   return tuple(a[i]+(b[i]-a[i])*q for i in range(1,4))
 return keys[-1][1:]
def make_stream(path,w,h):
 c=av.open(str(path),'w',options={'movflags':'+faststart'});s=c.add_stream('libx264',rate=fps);s.width=w;s.height=h;s.pix_fmt='yuv420p';s.options={'crf':'16','preset':'fast'};return c,s
def emit(c,s,img,i):
 f=av.VideoFrame.from_image(img);f.pts=i
 for p in s.encode(f):c.mux(p)
def close(c,s):
 for p in s.encode():c.mux(p)
 c.close()
c1,s1=make_stream(out/'phoneuse-proactive-studio-hq.mp4',1920,1440)
mask=Image.new('L',(1840,1380));ImageDraw.Draw(mask).rounded_rectangle((0,0,1839,1379),radius=24,fill=255)
shadow=Image.new('RGBA',(1920,1440));ImageDraw.Draw(shadow).rounded_rectangle((40,40,1880,1420),radius=24,fill=(18,19,20,45));shadow=shadow.filter(ImageFilter.GaussianBlur(14))
base=Image.new('RGB',(1920,1440),'#E9E7E0');base.paste(shadow,(0,0),shadow)
last=-1;still=None;cached_key=None;cached_canvas=None
for i in range(math.ceil(duration*fps)):
 t=i/fps;j=max(0,bisect.bisect_right(times,t)-1)
 if j!=last:still=Image.open(cap/frames[j]['file']).convert('RGB');last=j
 im=still
 z,cx,cy=camera(t)
 cache_key=(j,round(z,4))
 if cache_key!=cached_key:
  sw=round(1840*z);sh=round(1380*z);ox=(1920-sw)//2;oy=(1440-sh)//2
  shot=im.resize((sw,sh),Image.Resampling.BICUBIC)
  frame_mask=Image.new('L',(sw,sh));ImageDraw.Draw(frame_mask).rounded_rectangle((0,0,sw-1,sh-1),radius=24,fill=255)
  frame_shadow=Image.new('RGBA',(1920,1440));ImageDraw.Draw(frame_shadow).rounded_rectangle((ox,oy+8,ox+sw,oy+sh+8),radius=24,fill=(18,19,20,40));frame_shadow=frame_shadow.filter(ImageFilter.GaussianBlur(14))
  canvas=Image.new('RGB',(1920,1440),'#E9E7E0');canvas.paste(frame_shadow,(0,0),frame_shadow);canvas.paste(shot,(ox,oy),frame_mask)
  cached_key=cache_key;cached_canvas=canvas
 else:canvas=cached_canvas
 emit(c1,s1,canvas,i)
 if i in [int(5*fps),int(9*fps),int(16*fps),int(30*fps),int(44.5*fps)]:canvas.save(out/f'preview-{i}.jpg')
 if i%300==0:print(f'{i}/{math.ceil(duration*fps)} frames',flush=True)
close(c1,s1)
print('Completed phoneuse-proactive-studio-hq.mp4',flush=True)
