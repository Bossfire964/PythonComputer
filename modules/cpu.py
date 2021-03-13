from modules import bus
from modules import register
from modules import alu
from modules import ram
from modules import clock
from modules import display



commandLib = {
	"00000000000000000000000000000001" : "Put on bus [value=32]",
	"00000000000000000000000000000010" : "Load 0 [no value]",
	"00000000000000000000000000000011" : "Display Bus [bin(1)=bin, bin(2)=int]",
	"00000000000000000000000000000100" : "Load 1 [no value]",
	"00000000000000000000000000000101" : "Load 2 [no value]",
	"00000000000000000000000000000110" : "Write 0 [no value]",
	"00000000000000000000000000000111" : "Write 1 [no value]",
	"00000000000000000000000000001000" : "Write 2 [no value]",
	"00000000000000000000000000001001" : "Add",
	"00000000000000000000000000001010" : "Subtract"
}

def spliter(word):
    return [char for char in word]


def runCommand(command):
	struct = ''.join(command)[:32]
	if clock.mode == "debug":
		print("Data: " + struct)

	if struct == "00000000000000000000000000000001":
		bus.data = spliter('00000000000000000000000000000000' + ''.join(command[33:]))
	if struct == "00000000000000000000000000000010":
		register.registers[0].writing = False
		register.registers[0].loading = True
	if struct == "00000000000000000000000000000100":
		register.registers[1].writing = False
		register.registers[1].loading = True
	if struct == "00000000000000000000000000000101":
		register.registers[2].writing = False
		register.registers[2].loading = True
	if struct == "00000000000000000000000000000110":
		register.registers[0].writing = True
		register.registers[0].loading = False
	if struct == "00000000000000000000000000000111":
		register.registers[1].writing = True
		register.registers[1].loading = False
	if struct == "00000000000000000000000000001000":
		register.registers[2].writing = True
		register.registers[2].loading = False
	if struct == "00000000000000000000000000000011":
		if int(''.join(command[33:]), 2) == 1:
			print(''.join(bus.data))
		elif int(''.join(command[33:]), 2) == 2:
			print(int(''.join(bus.data), 2))
	if struct == "00000000000000000000000000001001":
		alu.on = True
		alu.add = True
	if struct == "00000000000000000000000000001010":
		alu.on = True
		alu.add = False