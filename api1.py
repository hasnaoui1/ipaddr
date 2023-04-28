
from flask import Flask
import ipaddress 
from ipaddress import IPv4Address , IPv4Network


app = Flask(__name__)

classA = range (0,127)  
classB = range (128,191)
classC = range (192,223)
classD = range (239,240)


@app.route("/")
def home():
    return ("THIS IS MY FIRST API ")


@app.route("/class/<ip1>")
def classx(ip1):
    x = ip1.split('.')
    address = int(x[0])
    if address in classA:
            return ("class a")
    elif address in classB:
            return ("class b")
    elif address in classC:
            return ("class c")
    elif address in classD:
            return ("class d")
        

   
    

@app.route("/broadcast/<ip>/<mask>")
def broadcast (ip ,mask ):
    
    network1 = ipaddress.IPv4Network(ip + '/' + mask , False) 
    broadcastip = network1.broadcast_address
    
    return  (str(broadcastip))

@app.route("/network/<ip>/<mask>")
def network(ip,mask):
    
    network1 = ipaddress.IPv4Network(ip + '/' + mask , False) 
    return (str(network1))
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2000)














