"""Serve the portfolio locally, without serving engineering source materials."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class PortfolioHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = unquote(urlsplit(self.path).path)
        relative = path.lstrip('/')
        resolved = (ROOT / relative).resolve()
        allowed = (
            resolved == ROOT / 'index.html'
            or (relative == '' and resolved == ROOT)
            or any(resolved.is_relative_to(ROOT / folder) for folder in ('assets', 'projects'))
        )
        if not allowed or (resolved.is_dir() and resolved != ROOT):
            self.send_error(404)
            return None
        return super().send_head()


if __name__ == '__main__':
    handler = partial(PortfolioHandler, directory=str(ROOT))
    with ThreadingHTTPServer(('127.0.0.1', 8000), handler) as server:
        print('Portfolio preview on port 8000. Press Ctrl+C to stop.', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
