import sys
from modules import cpu
from modules import register
commandslist = [
	"0000000000000000000000000000000100000000000000000000000000000011",
	"0000000000000000000000000000001000000000000000000000000000000000",
	"0000000000000000000000000000000100000000000000000000000000000001",
	"0000000000000000000000000000010000000000000000000000000000000000",
	"0000000000000000000000000000100100000000000000000000000000000000",
	"0000000000000000000000000000001100000000000000000000000000000010"
	
]


currentOn = 0


def spliter(word):
    return [char for char in word]


def clock():
	global currentOn
	cpu.runCommand(spliter(commandslist[currentOn]))
	currentOn += 1
	if currentOn == len(commandslist):
		sys.exit()