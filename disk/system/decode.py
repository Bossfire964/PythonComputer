
import os
import sys
import time
sys.path.insert(1, '/'.join(os.path.realpath(__file__).split('/')[:-3]))
from modules import ram


def is_int(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def spliter(word):
    return [char for char in word]


def Lex(code):
	overallLines = []
	for line in code:
		line = line.strip('\n')
		letters = []
		words = []
		for i, char in enumerate(spliter(line)):
			if char == "=":
				words.append(''.join(letters))
				words.append("=")
				letters = []
			else:
				letters.append(char)
		if len(letters) > 0:
			words.append(''.join(letters))
		words.append("END")
		for word in words:
			overallLines.append(word)
	return overallLines

def Parse(tokens):
	tokenTree = []
	currentTree = []
	for i, token in enumerate(tokens):
		if token == "=":
			currentTree.append(tokens[i-1] + ":EQL:" + tokens[i + 1])
		if token == "END":
			for command in currentTree:
				tokenTree.append(command)
				currentTree = []
	return tokenTree

def Interpreter(commands):
	var = ["OSType, OSParam, null, boot"]
	varVal = ["null, null, null, loader"]
	
	for command in commands:
		if command.split(':')[1] == "EQL":
			if command.split(':')[0] == "OSType" or command.split(':')[0] = "OSParam":
				pass
			else:
				if command.split(':')[0] == "displaybg":
					pass
				if command.split(':')[0] in var:
				varVal[var.index(command.split(':')[0])] = command.split(':')[2]
				else:
					var.append(command.split(':')[0])
					varVal[var.index(command.split(':')[0])] = command.split(':')[2]




dir_list = os.listdir('/'.join(os.path.realpath(__file__).split('/')[:-1]))
for file in dir_list:
	if str(file).split('.')[1] == "os":
		code = []
		with open(file, "r") as f:
			code = f.readlines()
		print(code)
		print(Lex(code))
		print(Parse(Lex(code)))






