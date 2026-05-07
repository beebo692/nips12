#!/usr/bin/env python3
"""Simple HTTP server for previewing the project page."""
import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 9999
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("0.0.0.0", PORT), handler) as httpd:
    print(f"Serving vla-interp-page at http://localhost:{PORT}")
    httpd.serve_forever()
