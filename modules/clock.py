import time
import sys
from modules import register
from modules import alu
from modules import ram
from modules import cpu
from modules import display

register.setUp()
display.startScreen(10, 10)


time_data = 1
mode = "debug"


def start():
	global time_data
	global mode
	def clock():
		ram.clock()
		register.check()
		alu.check()
		display.UpdateScreen()



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