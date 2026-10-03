"""Servidor local da vitrine da Delícias da JU.

Execute `python main.py` e abra http://localhost:8000 no navegador.
"""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


def create_server(host: str = "", port: int = 8000) -> ThreadingHTTPServer:
    """Create the local static-file server without starting its event loop."""
    return ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler)


if __name__ == "__main__":
    server = create_server()
    print("Delícias da JU em http://localhost:8000")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nAté logo!")
        server.server_close()
