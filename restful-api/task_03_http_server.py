#!/usr/bin/python3
"""
Develop a simple API using Python with the `http.server` module.
"""

import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        if __name__ == '__main__':
            server_address = ('', 8000)
            httpd = http.server.\
                HTTPServer(server_address, SimpleHTTPRequestHandler)
            print('Starting server on http://localhost:8000')
            httpd.serve_forever()
