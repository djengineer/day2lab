import threading
import http.server
import socket 
from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler, ThreadingHTTPServer
import http.server
import multiprocessing
import ssl
import os

fullpath = os.path.realpath(__file__)
base_dir, fname = os.path.split(fullpath)
application_path= base_dir + '/webroot'

global http_server_process
http_server_process = None

class MyHttpHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=application_path, **kwargs)

def httpsd(server_class=ThreadingHTTPServer, handler_class=MyHttpHandler):
	global certdir
	server_address = ('', 8000)
	httpd = server_class(server_address, handler_class)
	httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile=base_dir + "/certificates/key.pem", 
        certfile=base_dir + '/certificates/cert.pem', server_side=True)
	httpd.serve_forever()

def start_https_button():
	global http_server_process
	global http_status
	if http_server_process != None:
		print("HTTP/HTTPS server already started.")
		pass
	elif http_server_process == None:
		# Name error means not defined. start a new server.
		http_server_process = multiprocessing.Process(target=httpsd,name='HTTPSprocess')
		http_server_process.start()
		http_status = "STARTED"
		print("HTTPS server process started")

if __name__ == "__main__":
	start_https_button()
