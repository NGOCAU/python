#!/usr/bin/python
import socket
def remotehostinfo():
	rhost = raw_input("Nhap remote hostname: ")
	rip = socket.gethostbyname(rhost)
	try: 
		print "IP add of remote host is: ",rip
	except socket.error,err_msg:
		print "ERROR"
remotehostinfo()
