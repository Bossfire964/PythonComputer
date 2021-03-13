import time
import sys
from modules import register
from modules import alu
from modules import ram
from modules import cpu

register.setUp()


time_data = 1
mode = "play"


def start():
	global time_data
	global mode
	def clock():
		ram.clock()
		register.check()
		alu.check()



	if mode == "play":
		while True:
			time.sleep(time_data)
			clock()
	elif mode == "debug":
		while True:
			we = input(">> ")
			if we == "exit":
				sys.exit()
			clock()