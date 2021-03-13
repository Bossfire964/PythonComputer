import time
import sys
from modules import register
from modules import alu
from modules import ram
from modules import cpu

register.setUp()


time_data = 1000
mode = "debug"


def start():
	def clock():
		ram.clock()
		register.check()
		alu.check()
		print(register.registers[0].data)



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