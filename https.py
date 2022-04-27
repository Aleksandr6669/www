import http.server
import socketserver
from threading import Thread
import os
import ssl



script_dir = os.path.dirname(os.path.realpath(__file__))
keypath = os.path.join(script_dir, 'private.key')
certpath = os.path.join(script_dir, 'certificate.crt')

def server_thread(port):
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.socket = ssl.wrap_socket(
        httpd.socket, keyfile=keypath, certfile=certpath, server_side=True)
        httpd.serve_forever()
if __name__ == '__main__':

    port = 443
    print("Starting server at port %d" % port)
    #os.chdir("/home/www/www")
    os.chdir("www")
    Thread(target=server_thread, args=(port,)).start()
