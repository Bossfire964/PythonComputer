from modules import cpu

commandslist = [
	"0000000000000000000000000000000100000000000000000000000000000111",
	"0000000000000000000000000000001000000000000000000000000000000000"
]


currentOn = 0


def spliter(word):
    return [char for char in word]

    
def clock():
	global currentOn
	cpu.runCommand(spliter(commandslist[currentOn]))
	currentOn += 1
	if currentOn == len(commandslist):
		currentOn = 0