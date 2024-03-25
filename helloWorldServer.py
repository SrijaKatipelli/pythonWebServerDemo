from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, world!')

httpd = HTTPServer(('localhost', 8000), MyHTTPRequestHandler)
print('Server running on localhost:8000...')
httpd.serve_forever()