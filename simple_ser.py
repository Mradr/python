#!/usr/bin/python
#coding=utf-8

import socket
import os
import sys
import thread
import time

def ser_recv(connfd, cliaddr):
	while True:
		buf = connfd.recv(4096)
		print buf


	thread.exit_thread() 


def ser_send(connfd, cliaddr):
	print cliaddr
	connfd.sendall('welcome to my server\n')
	
	t = thread.start_new_thread(ser_recv, (connfd, cliaddr))

	while True:
		print '#',
		buf = sys.stdin.readline()
		connfd.sendall(buf)

	thread.exit_thread() 


def server(host, port):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	s.listen(3)

	while True:
		time.sleep(1)
		connfd, cliaddr = s.accept()
		t = thread.start_new_thread(ser_send, (connfd, cliaddr))



if __name__ == '__main__':
#	port = 1235
#	host = '192.168.0.112'
	host = sys.argv[1]
	port = int(sys.argv[2])
	
	server(host, port)


