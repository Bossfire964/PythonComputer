from modules import bus

class register():
	def __init__(self, idname):
		self.idname = idname
		self.writing = False
		self.loading = False
		self.data = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


registers = []
def setUp():
	global registers
	register0 = register(1)
	registers.append(register0)
	register1 = register(2)
	registers.append(register1)
	register2 = register(3)
	registers.append(register2)


def check():	
	for register in registers:
		if register.writing == True:
			bus.data = register.data
		if register.loading == True:
			register.data = bus.data
		register.writing = False
		register.loading = False





