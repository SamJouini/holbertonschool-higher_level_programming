#!/usr/bin/python3
"""
Develop a simple API using Python with the `http.server` module.
"""

import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    This class inherits from the BaseHTTPRequestHandler class and overrides
    the do_GET method to handle GET requests.
    """

    def do_GET(self):
        """
        This method is called whenever a GET request is received by the server.
        It checks the requested path and sends the appropriate response.
        """
        if self.path == '/data':
            # If the requested path is '/data', send a JSON response
            self.send_response(200)  # Set the response status code to 200 (OK)
            self.send_header('Content-type', 'application/json')
            # Set the response content type to JSON
            self.end_headers()  # End the response headers

            # Create a sample data dictionary
            data = {"name": "John", "age": 30, "city": "New York"}

            # Convert the data dictionary to JSON
            # Send it as the response body
            self.wfile.write(json.dumps(data).encode())

        else:
            # For any other path, send a plain text response
            self.send_response(200)  # Set the response status code to 200 (OK)
            self.send_header('Content-type', 'text/plain')
            # Set the response content type to plain text
            self.end_headers()  # End the response headers

            # Send a simple message as the response body
            self.wfile.write(b"Hello, this is a simple API!")

if __name__ == '__main__':
    """
    This block is executed when the script
    is run directly (not imported as a module).
    It starts the HTTP server and listens for incoming requests.
    """
    server_address = ('', 8000)
    # Set the server address to listen on all available interfaces
    httpd = http.server.\
        HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server on http://localhost:8000')
    httpd.serve_forever()
    # Start the server and listen for incoming requests indefinitely
