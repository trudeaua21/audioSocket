#Group members: Aaron, Camaal, Kelly, Max
#version 1.0 9-21-2019
#CS 457 Data Communications
#Prof. Bhuse
#Files: ftp_client
#Purpose: to have a client issue commands to a server until client terminates connection by sending 'QUIT'
#Tested with socket.txt file 7kb and file needs to be in the same directory as the server

import socket
import sys
import time
import os
from pathlib import Path
import pyaudio
import wave
import numpy as np


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "output.wav"

def main():
	host = 'localhost'
	port = 9000
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try: 
		sock.connect((host, int(port)))
		print ("connected")
	except:
		print("error")
		sys.exit()
		
	handle_retrieve(sock)


def handle_retrieve(sock):
	pya = pyaudio.PyAudio()
	stream2 = pya.open(format=pya.get_format_from_width(width=2), channels=channels, rate=fs, output=True)
	x = 1 
	while True:
		data = sock.recv(1024)
		print('Playing audio ', x)
		stream2.write(data)
		x+=1
		
	stream2.stop_stream()
	stream2.close()
	pya.terminate()
	 
	print('Finished playback')



if __name__ == "__main__":
    main()