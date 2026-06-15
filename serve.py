import http.server
import socketserver
import os

os.chdir('/Users/olesiabeno/Desktop/6 кроків/landing')
PORT = 8083
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
