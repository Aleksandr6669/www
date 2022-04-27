import http.server
import socketserver
from threading import Thread
import os



def server_thread(port):
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()
if __name__ == '__main__':

    port = 80
    print("Starting server at port %d" % port)
    #os.chdir("/home/www/www")
    os.chdir("www")
    Thread(target=server_thread, args=(port,)).start()
