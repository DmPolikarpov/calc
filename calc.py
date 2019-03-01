from tkinter import *
from decimal import *
from pygame import *
window = Tk()
#какой-то комментарий
img = PhotoImage(file = 'calc.gif')
imgLb = Label(window, image = img).grid(row = 1, columnspan = 6)
scrLb = Label(window, relief = 'sunken', bd = 10,\
font = ('Times New Roman', 30), width = 16, justify = RIGHT)
scrLb.grid(row = 2, columnspan = 6)
btn0 = Button(window, relief = 'raised',\
 font = ('Times New Roman', 18), width = 4, text = '0', command = lambda text = '0': click(text)).grid(row = 18, column = 1)
btn1 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '1', command = lambda text = '1': click(text)).grid(row = 16, column = 1)
btn2 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '2', command = lambda text = '2': click(text)).grid(row = 16, column = 2)
btn3 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '3', command = lambda text = '3': click(text)).grid(row = 16, column = 3)
btn4 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '4', command = lambda text = '4': click(text)).grid(row = 14, column = 1)
btn5 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '5', command = lambda text = '5': click(text)).grid(row = 14, column = 2)
btn6 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '6', command = lambda text = '6': click(text)).grid(row = 14, column = 3)
btn7 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '7', command = lambda text = '7': click(text)).grid(row = 12, column = 1)
btn8 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '8', command = lambda text = '8': click(text)).grid(row = 12, column = 2)
btn9 = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '9', command = lambda text = '9': click(text)).grid(row = 12, column = 3)
PntBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '.', command = lambda text = '.': click(text)).grid(row = 18, column = 2)
ACBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = 'AC', command = lambda text = 'AC': click(text)).grid(row = 10, column = 1)
DelBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = 'Del', command = lambda text = 'Del': click(text)).grid(row = 18, column = 3)
plsBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '+', command = lambda text = '+': click(text)).grid(row = 16, column = 4)
mnsBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '-', command = lambda text = '-': click(text)).grid(row = 14, column = 4)
ymnBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '*', command = lambda text = '*': click(text)).grid(row = 12, column = 4)
rdlBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '/', command = lambda text = '/': click(text)).grid(row = 10, column = 4)
plmBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '+/-', command = lambda text = '+/-': click(text)).grid(row = 10, column = 3)
prcBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '%', command = lambda text = '%': click(text)).grid(row = 10, column = 2)
rezBtn = Button(window, relief = 'raised',  bd = 5,\
 font = ('Times New Roman', 18), width = 4, text = '=', command = lambda text = '=': click(text)).grid(row = 18, column = 4)



window.title('privet')
window.resizable(0, 0)


indata = []
actStr = ''
operation = ''


def click(text):
	global indata
	global actStr
	global scrLb
	global operation
	prc = []
	svar = []
	if '0' <= text <= '9' or text == '.':
		if len(actStr)<=5:
			actStr += text
			scrLb.configure(text = actStr)
	elif text == '+':
		if len(indata) >= 1:
			indata.append(scrLb['text'])
			calculate()
		operation = '+'
		indata.append(scrLb['text'])
		actStr = ''
	elif text == '-':
		if len(indata) >= 1:
			indata.append(scrLb['text'])
			calculate()
		operation = '-'
		indata.append(scrLb['text'])
		actStr = ''
	elif text == '*':
		if len(indata) >= 1:
			indata.append(scrLb['text'])
			calculate()
		operation = '*'
		indata.append(scrLb['text'])
		actStr = ''
	elif text == '/':
		if len(indata) >= 1:
			indata.append(scrLb['text'])
			calculate()
		operation = '/'
		indata.append(scrLb['text'])
		actStr = ''
	elif text == '=':
		indata.append(scrLb['text'])
		calculate()
	elif text =='AC':
		actStr = ''
		indata = []
		scrLb.configure(text = '')
	elif text == 'Del':
		svar = actStr[::-1]
		svar = svar[1:]
		actStr = svar[::-1]
		scrLb.configure(text = actStr)
	elif text == '%':
		prc.append(scrLb['text'])
		prc = Decimal(prc.pop())
		prc = prc / 100
		scrLb.configure(text = prc)
	elif text == '+/-':
		prc.append(scrLb['text'])
		prc = Decimal(prc.pop())
		prc = - prc
		scrLb.configure(text = prc)


def calculate():
	global indata
	global actStr
	global scrLb
	global operation
	result = 0
	operand2 = Decimal(indata.pop())
	operand1 = Decimal(indata.pop())
	if operation =='+':
		result = operand1 + operand2
	if operation =='-':
		result = operand1 - operand2
	if operation =='*':
		result = operand1 * operand2
	if operation =='/':
		result = operand1 / operand2
		result = round(result, 3)
	scrLb.configure(text = str(result))






window.mainloop()