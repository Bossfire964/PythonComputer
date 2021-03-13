from modules import bus
from modules import register

add = True
on = False
reg1 = 0
reg2 = 1

def spliter(word):
    return [char for char in word]

def check():
	global add
	global on
	global reg1
	global reg2
	if on == True:
		if add == True:
			new_data = bin(int(''.join(register.registers[reg1].data), 2) + int(''.join(register.registers[reg2].data), 2)).split()
			new_data = spliter(new_data)
			while len(new_data) > 64:
				new_data.pop(0)
			bus.data = new_data
		elif add == False:
			new_data = bin(int(''.join(register.registers[reg1].data), 2) - int(''.join(register.registers[reg2].data), 2)).split()
			new_data = spliter(new_data)
			while len(new_data) > 64:
				new_data.pop(0)
			bus.data = new_data
		on = False