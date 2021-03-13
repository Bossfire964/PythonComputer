


class display():
	widthScreen = []
	lengthNum = 10
	image = []

def startScreen(width, length):
	table = []
	for number in range(width):
		table.append("~")
	display.widthScreen = table
	display.default = table
	display.lengthNum = length
	for number in range(length):
		print(''.join(table))



def UpdateScreen():
	for item in range(display.lengthNum):
		newDisplay = []
		for num in range(len(display.widthScreen)):
			newDisplay.append("~")
		for image in display.image:
			if image.split(':')[0] == str(item):
				newDisplay[int(image.split(':')[1])] = image.split(':')[2]
		print(''.join(newDisplay))