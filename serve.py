"""Local-only, dependency-free preview server."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
p = argparse.ArgumentParser()
p.add_argument('--port', type=int, default=8775)
a = p.parse_args()
root = Path(__file__).resolve().parent
print(f'Open http://127.0.0.1:{a.port}/ (Ctrl+C to stop)', flush=True)
ThreadingHTTPServer(('127.0.0.1', a.port), partial(SimpleHTTPRequestHandler, directory=str(root))).serve_forever()
