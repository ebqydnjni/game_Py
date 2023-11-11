##################
#   Ball.py       #
#  Aldiouma Mbaye # 
#    13/06/2023   #
##################

import sys
import tty
import time
import termios
import select

#mes modules
import Arriere
import Ball

def init(data):
	
	#initialisation de la partie	
	data['timeStep']=0.015
	
	#creation des elements du jeu
	data['arriere'] = Arriere.create('laby.txt')
	data['arriere1'] = Arriere.create('laby1.txt')
	data['ball']=Ball.create(0,9,8,8)
	data['ball1']=Ball.create(27,10,8,8)
	data['ball2']=Ball.create(50,10,8,-6)
	data['ball3']=Ball.create(73,10,8,10)
	data['ball4']=Ball.create(94,10,8,-4)
	data['ball5']=Ball.create(115,10,8,13)
	data['ball6']=Ball.create(136,10,8,-12)
	# interaction clavier
	data['old_settings']=termios.tcgetattr(sys.stdin)
	tty.setcbreak(sys.stdin.fileno())

def live(data):
	Ball.live(data['ball'],data['timeStep'])	
	x=Ball.get_x(data['ball'])
	y=Ball.get_y(data['ball'])
	i=int(x)
	j=int(y)
	c=Arriere.get_char(data['arriere'],j,i)
	
	if c=='#':	
		txt="\033["+'18'+";"+'18'+"H"
		sys.stdout.write(txt)
		sys.stdout.write("\033[40m")
		sys.stdout.write("YOU WIN!!!\n")
		quitGame(data)

	Ball.rebound(data['ball1'],data['timeStep'],data['arriere'])
	Ball.rebound(data['ball2'],data['timeStep'],data['arriere'])
	Ball.rebound(data['ball3'],data['timeStep'],data['arriere'])
	Ball.rebound(data['ball4'],data['timeStep'],data['arriere'])
	Ball.rebound(data['ball5'],data['timeStep'],data['arriere'])
	Ball.rebound(data['ball6'],data['timeStep'],data['arriere'])

	c1=Ball.position(data['ball1'],data['arriere'])
	c2=Ball.position(data['ball2'],data['arriere'])
	c3=Ball.position(data['ball3'],data['arriere'])
	c4=Ball.position(data['ball4'],data['arriere'])
	c5=Ball.position(data['ball5'],data['arriere'])
	c6=Ball.position(data['ball6'],data['arriere'])


	if c=="l" or c=="-":
		txt="\033["+'18'+";"+'18'+"H"
		sys.stdout.write(txt)
		sys.stdout.write("\033[40m")
		sys.stdout.write("PERDU!!!\n")
		quitGame(data)


def interact(data):
	if isData():
		c = sys.stdin.read(1)
		if c == '\x1b':         # x1b is ESC
			quitGame(data)
		elif c=='z' :
			Ball.move_up(data['ball'])	
		elif c=='n' :
			Ball.move_down(data['ball'])

def isData():
	return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

def show(data):
	sys.stdout.write("\033[2J")
	sys.stdout.write("\033[10;20H")
	Arriere.show(data['arriere'])
	Ball.show(data['ball'])
	Ball.show1(data['ball1'])
	Ball.show1(data['ball2'])
	Ball.show1(data['ball3'])
	Ball.show1(data['ball4'])
	Ball.show1(data['ball5'])
	Ball.show1(data['ball6'])
	sys.stdout.write("\n")

def run(data):
	#Boucle de simulation	
	while 1:
		interact(data)		
		live(data)
		show(data)
		time.sleep(data['timeStep'])

def quitGame(data):	
	#couleur white
	sys.stdout.write("\033[37m")
	sys.stdout.write("\033[40m")
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN, data['old_settings'])
	sys.exit()


def main():
	data={}
	init(data)
	run(data)

if __name__ == '__main__':
	main()

