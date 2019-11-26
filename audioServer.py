# Group members: Aaron, Camaal, Kelly, Max
# version 1.0 9-21-2019
# CS 457 Data Communications
#Prof. Bhuse
#Files: ftp_server
# Purpose: to have a multi-threaded server receive and process commands from clients with further details below.
# On receiving a command, the server should parse the command and perform the appropriate action. The format of the commands is such as follows:

# 1.	CONNECT <server name/IP address> <server port>: This command allows a client to connect to a server.
# The arguments are the IP address of the server and the port number on which the server is listening for connections.

# 2.	LIST: When this command is sent to the server, the server returns a list of the files in the current directory on which it is executing.
# The client should get the list and display it on the screen.

# 3.	RETRIEVE <filename>: This command allows a client to get a file specified by its filename from the server.

# 4.	STORE <filename>: This command allows a client to send a file specified by its filename to the server.

# 5.	QUIT: This command allows a client to terminate the control connection.
# On receiving this command, the client should send it to the server and terminate the connection.
# When the ftp_server receives the quit command it should close its end of the connection.


import socket
import time
import os
import sys
import select
from _thread import *

import pyaudio
import wave
import numpy as np

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

# intialize and run everything


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
        
    port = 9000
    print("Socket Created")  # Status update

    # Attempt to bind socket to IP and port, error otherwise.
    try:
        s.bind(('localhost', int(port)))
    except socket.error:
        print("Binding failed")
        sys.exit()
    print("socket bound")  # Status update

    s.listen()
    print("listening")  # Status update

    # driver loop
    while 1:
        try:
            conn, addr = s.accept()  # continuously accept client connections
            # Print IP address and port# of connected client
            print("Connected with " + addr[0] + ":" + str(addr[1]))
            # Start new thread for client each connection
            start_new_thread(clientthread, (conn, addr,)) #,s
        except socket.error:
            continue
        except KeyboardInterrupt:
            print("\nQuiting server...")
            break
    s.close()  # Close socket


def send_audio(conn):
	# continuously accept audio input and send it over the socket 
	

	stream = p.open(format=sample_format,
					channels=channels,
					rate=fs,
					frames_per_buffer=chunk,
					input=True)


	x = 0
	while True:
		data = stream.read(chunk)
		#send data, then frames.append on the client side
		conn.send(data)
		print('sending audio ', x)
		x+=1

	# Stop and close the stream 
	stream.stop_stream()
	stream.close()
	# Terminate the PortAudio interface
	p.terminate()

	print('Finished recording')	
	
	conn.send(frames.tobytes())
	

# Function to handle all client connections and their respective commands
def clientthread(conn, addr):
    send_audio(conn)


main()