


class display():
	widthScreen = []
	lengthNum = 10

def startScreen(width, length):
	table = []
	for number in range(width):
		table.append("~")
	display.widthScreen = table
	display.lengthNum = length
	for number in range(length):
		print(''.join(table))



def UpdateScreen():
	for item in range(display.lengthNum):
		print(''.join(display.widthScreen))