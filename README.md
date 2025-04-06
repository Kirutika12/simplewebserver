# EX01 Developing a Simple Webserver
## Date: 27.03.2025
## Name: Kirutika KR
## Reg no: 212224230128

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.


## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
```
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
```
```
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
```

## OUTPUT:
![alt text](<Screenshot 2025-03-27 112705.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.
