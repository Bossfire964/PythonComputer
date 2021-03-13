from modules import bus
from modules import register
from modules import alu
from modules import ram



commandLib = {
	"00000000000000000000000000000001" : "Put on bus",
	"00000000000000000000000000000010" : "Load 0"
}

def spliter(word):
    return [char for char in word]


def runCommand(command):
	struct = ''.join(command)[:32]
	print("Data: " + struct)

	if struct == "00000000000000000000000000000001":
		bus.data = spliter('00000000000000000000000000000000' + ''.join(command[33:]))
		print(bus.data)
	if struct == "00000000000000000000000000000010":
		register.registers[0].writing = False
		register.registers[0].loading = True