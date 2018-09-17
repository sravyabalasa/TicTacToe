#Sravya Balasa
#Lab 4

from tkinter import *
root=Tk()
root.title("Sravya's Tic Tac Toe Game")
import time

x= PhotoImage(file="x.gif")
circle= PhotoImage(file="o.gif")

#Quit Button
quitButton=Button(root, text='Quit Game', command=root.destroy,pady=10).grid(row=4, column=1) 

ButtonSpaces=[False,False,False,False,False,False,False,False,False] #set up a dictionary maybe instead?
turn="Player"

def close_window(thing):
	thing.destroy()

def isWinner():
	if (ButtonSpaces[0]=="TrueCircle" and ButtonSpaces[1]=="TrueCircle" and ButtonSpaces[2]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[3]=="TrueCircle" and ButtonSpaces[4]=="TrueCircle" and ButtonSpaces[5]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[6]=="TrueCircle" and ButtonSpaces[7]=="TrueCircle" and ButtonSpaces[8]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[0]=="TrueCircle" and ButtonSpaces[3]=="TrueCircle" and ButtonSpaces[6]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[1]=="TrueCircle" and ButtonSpaces[4]=="TrueCircle" and ButtonSpaces[7]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[2]=="TrueCircle" and ButtonSpaces[5]=="TrueCircle" and ButtonSpaces[8]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[0]=="TrueCircle" and ButtonSpaces[4]=="TrueCircle" and ButtonSpaces[8]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[2]=="TrueCircle" and ButtonSpaces[4]=="TrueCircle" and ButtonSpaces[6]=="TrueCircle"):
		print("You've won the game!")
		close_window(root)
	elif (ButtonSpaces[0]=="Truex" and ButtonSpaces[3]=="Truex" and ButtonSpaces[6]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif (ButtonSpaces[0]=="Truex" and ButtonSpaces[4]=="Truex" and ButtonSpaces[7]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif (ButtonSpaces[1]=="Truex" and ButtonSpaces[4]=="Truex" and ButtonSpaces[7]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif (ButtonSpaces[0]=="Truex" and ButtonSpaces[1]=="Truex" and ButtonSpaces[2]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif (ButtonSpaces[3]=="Truex" and ButtonSpaces[4]=="Truex" and ButtonSpaces[5]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif (ButtonSpaces[6]=="Truex" and ButtonSpaces[7]=="Truex" and ButtonSpaces[8]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif (ButtonSpaces[0]=="Truex" and ButtonSpaces[4]=="Truex" and ButtonSpaces[8]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif (ButtonSpaces[2]=="Truex" and ButtonSpaces[4]=="Truex" and ButtonSpaces[6]=="Truex"):
		print("Sorry, the computer beat you!")
		close_window(root)
	elif False not in ButtonSpaces:
		print("This game was a draw!")
		close_window(root)
	else:
		msg="It's your turn!"
		userMessage=Message(root, text=msg)
		userMessage.config(bg='white',font=('times',16,'italic'))
		userMessage.grid(row=6,column=1)


def randomsquare(theturn): 
	#BETTER ALGORITHM
	from random import randint
	i=(randint(0,8))
	while ButtonSpaces[i]!=False:
		i=(randint(0,8))

	count=0
	number=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
			number=ButtonSpaces.index(z)

	#NEED DELAY HERE
	if theturn=="Computer" and ButtonSpaces[i]==False:
		Buttons[i].config(image=x,width=150,height=150, relief=SUNKEN, state=DISABLED) #use a dictionary??
		ButtonSpaces[i]="Truex"

	isWinner()
		

#Grid Setup	

#BUTTON SIZES? Okay on WINDOWS/Not on MAC	
def inaction1():
	if ButtonSpaces[0]==False:
		button1.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[0]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button1=Button(root,width=20,height=9,command=inaction1)
button1.grid(row=0,column=0)

def inaction2():
	if ButtonSpaces[1]==False:
		button2.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[1]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button2=Button(root,width=20,height=9,command=inaction2)
button2.grid(row=0,column=1)

def inaction3():
	if ButtonSpaces[2]==False:
		button3.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[2]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button3=Button(root,width=20,height=9,command=inaction3)
button3.grid(row=0,column=2)

def inaction4():
	if ButtonSpaces[3]==False:
		button4.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[3]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner() #if count !=0 AND iswinner
	else:
		randomsquare(turn)
button4=Button(root,width=20,height=9,command=inaction4)
button4.grid(row=1,column=0)

def inaction5():
	if ButtonSpaces[4]==False:
		button5.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[4]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button5=Button(root,width=20,height=9,command=inaction5)
button5.grid(row=1,column=1)

def inaction6():
	if ButtonSpaces[5]==False:
		button6.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[5]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button6=Button(root,width=20,height=9,command=inaction6)
button6.grid(row=1,column=2)

def inaction7():
	if ButtonSpaces[6]==False:
		button7.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[6]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button7=Button(root,width=20,height=9,command=inaction7)
button7.grid(row=2,column=0)

def inaction8():
	if ButtonSpaces[7]==False:
		button8.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[7]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button8=Button(root,width=20,height=9,command=inaction8)
button8.grid(row=2,column=1)

def inaction9():
	if ButtonSpaces[8]==False:
		button9.config(image=circle,width=150,height=150, relief=SUNKEN, state=DISABLED)
		ButtonSpaces[8]="TrueCircle"
	turn="Computer"
	count=0
	for z in ButtonSpaces:
		if z==False:
			count+=1
	if count==0:
		isWinner()
	else:
		randomsquare(turn)
button9=Button(root,width=20,height=9,command=inaction9)
button9.grid(row=2,column=2)

Buttons=[button1,button2,button3,button4,button5,button6,button7,button8,button9] 

root.mainloop()
