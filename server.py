"""Implement the microservice server"""
import json
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer
from controllers.get_estate import GetEstateController
from connections.db import DBConnection
import settings


class BaseServer(BaseHTTPRequestHandler):
    """Class with basic server capabilities.
    Inherits from BaseHTTPRequestHandler 
    """
    def _set_headers(self, status_code: int):
        """establishes response data headers
        """
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_GET(self):
        """Implements GET method on server
        """
        if self.path == "/status":
            response = {
                "APP_NAME": settings.APP_NAME,
                "VERSION": settings.VERSION,
                "status": "up and running!",
            }
            self._set_headers(200)
            self.wfile.write(bytes(json.dumps(response).encode("utf-8")))

    def do_POST(self):
        """Implements POST method on server
        """
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(content_length)
            if self.path == "/estate":
                db = DBConnection(settings.CONN_NAME)
                params = json.loads(post_data.decode("utf-8"))
                response = GetEstateController.get_estate(db, params)
                self._set_headers(200)
                self.wfile.write(bytes(json.dumps(response).encode("utf-8")))
        except Exception as e:
            self._set_headers(500)
            logging.error(f"error: {e}")


def run(server_class=HTTPServer, handler_class=BaseServer, port=8000):
    """Run an HTTP server

    Parameters
    ----------
    server_class : Server, optional
        The type of server to run, by default HTTPServer
    handler_class : Handler, optional
        Instance of the class that handles requests, by default BaseServer
    port : int, optional
        The port by which communication runs through, by default 8000
    """
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("HTTP server running on port %s" % port)
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
