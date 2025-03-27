
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
<!doctype html>
<html>
    <head>
        <title>TCP/IP</title>
    </head>
    <body bgcolor="pink">
        <center><HI>TCP/IP PROTOCOLS<br></center>
            <br>
            1.Application Layer Protocols - HTTP,FTP,SSH,Telnet & DNS <br>
            2.Transport Layer Protocols - TCP/UDP <br>
            3.Network Layer Protocols - IPV4/IPV6 <br>
            4.Link Layer Protocols -  MAC <br>
            <br>
            <br>
            Name: Kirutika KR<br>
            Reg no: 212224230128<br>
            
    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()