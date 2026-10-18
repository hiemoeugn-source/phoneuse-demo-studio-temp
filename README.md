# phoneuse Demo Studio

可交给 Codex 继续制作的独立演示项目。包含 Dashboard、模拟 iPhone、逐步操作动画和高清录制脚本。

**这是预设场景的界面模拟，不是真机控制或通用 AI agent。输入不同文字不会自动生成新任务。** 当前示例：航班延误通知 → 解锁 → 查看日历接机安排 → 给 Alex 发消息 → 向用户报告。新场景由 Codex 修改并验证。

## 直接预览（只需 Python 3.10+）

```sh
python3 serve.py
```

Windows 使用 `py serve.py`。打开 http://127.0.0.1:8775/ 。端口占用时使用 `python3 serve.py --port 8776`。

页面 5 秒后自动开始；`/?autoplay=0` 可关闭自动开始，输入文字后点 Send 启动固定示例。`R` 重置。`/?preview=homescreen`、`/?preview=inbox`、`/?preview=messages` 用于静态检查。

不需要 API key、手机、SSH、WDA 或数据库。首次启动不需要联网安装依赖。

## 交给 Codex

在 Codex 中打开这个项目文件夹，粘贴 [CODEX-PROMPT.md](CODEX-PROMPT.md) 全文。项目约束在 [AGENTS.md](AGENTS.md)。

- `scene.js`：通知、步骤、消息、报告、自动开始延迟。
- `index.html`：页面样式、手机各屏、日历内容和动画时间线。修改联系人、日期、时间时必须同步所有屏幕，不能只改 scene.js。
- `assets/`：仅本场景使用的壁纸和 UI 图标素材。
- `scripts/capture.mjs`：本地 Chromium 连续视频帧采集。
- `scripts/render.py`：4:3、1920×1440、60 fps H.264，完整双栏、小幅整体缩放。

## 导出视频（可选）

需要 Node.js 20+ 和 Python 3.10+。在项目目录运行：

```sh
npm install
npx playwright install chromium
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-recording.txt
```

Windows 安装依赖时使用 `.venv\Scripts\python.exe`。保持 `python3 serve.py` 在一个终端运行，在另一个终端运行：

```sh
npm run capture
.venv/bin/python scripts/render.py
```

如果用了 8776：`npm run capture -- http://127.0.0.1:8776/`。输出在 `exports/phoneuse-proactive-studio-hq.mp4`。

录制固定为 46 秒。改时间线后同步修改 capture.mjs 的等待时长、render.py 的 duration 和镜头关键帧。录制使用变化帧事件，静态画面不重复采集；输出 60 fps 不等于设备永远不会掉帧，应检查解锁、切换 App、输入和结尾过渡。

预览已在原机器验证；独立录制脚本提供标准 Playwright 流程，首次在新电脑使用时须按上述流程实际录制检查。Codex 内置浏览器也可按 AGENTS.md 使用 CUA 采集，不应绕过其工具规则。

## 素材与分享

不包含密钥、私人配置、配对资料、完整手机截图、原始手机视频或聊天记录。图标精灵仅保留本场景需要的图标区域。示例行程、联系人和消息用于演示。

Apple/iOS 和 United 图标属于对应权利方，未授予额外商标或素材授权。默认建议私有仓库，邀请协作者；发布视频时应清楚说明这是模拟/概念演示。不要把模拟发送称为真实发送。
