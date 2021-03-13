import sys
from modules import cpu
from modules import register
commandslist = [
	"0000000000000000000000000000000100000000000000000000000000000011",
	"0000000000000000000000000000110100000001000000100000000000000001"
	
]


currentOn = 0


def spliter(word):
    return [char for char in word]


def clock():
	global currentOn
	if currentOn == len(commandslist):
		sys.exit()
	cpu.runCommand(spliter(commandslist[currentOn]))
	currentOn += 1