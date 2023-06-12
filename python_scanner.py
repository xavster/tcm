#!/bin/python

import sys
import socket
from datetime import datetime

try:

    #Here we define the hostname/IP to scan
    if len(sys.argv) == 2:
            target = socket.gethostbyname(sys.argv[1]) #just in case it is a hostname
    else:
            print("Invalid")


    #some banners
    print ("-" * 20)
    print ("Scanning - " + target)
    print (str(datetime.now()))
    print ("-" * 20)
    

    for port in range(20,200):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error, if 0, no error, port open. If 1, there is an error, port closed
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except socket.gaierror:#dns resolution does not work
     print("Hostname not resolved.")
     sys.exit()

except KeyboardInterrupt: #ctrl+c
    print("Program exit!")
    sys.exit()
except socket.error:#no connection/inet
    print("Could not connect to target")
    sys.exit()

