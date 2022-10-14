from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            path, params = self.path.split('?')
            paramapmpam = {i.split('=')[0]: i.split('=')[1] for i in params.split('&')}
        except ValueError:
            path = self.path
        content_type = self.headers['Content-Type']

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        self.send_response(200)

        self.end_headers()

        if path == '/text' and content_type == 'text/plain':
            response = b'hui\n'
        elif path == '/image' and content_type == 'application/octet-stream':
            response = b'<===3\n'
        else:
            response = body

        self.wfile.write(response)


httpd = HTTPServer(('localhost', 8000), Server)
httpd.serve_forever()
