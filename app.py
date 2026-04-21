from http.server import BaseHTTPRequestHandler, HTTPServer
import os, shutil

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        load = os.getloadavg()
        total, used, free = shutil.disk_usage("/")

        output = f"""
        <h1>System Health Check 🚀</h1>
        <p>CPU Load: {load}</p>
        <p>Disk Total: {total // (2**30)} GB</p>
        <p>Disk Used: {used // (2**30)} GB</p>
        <p>Disk Free: {free // (2**30)} GB</p>
        """

        self.wfile.write(output.encode())

def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Server running on port 8000...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()