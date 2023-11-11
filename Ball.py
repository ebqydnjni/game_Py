##################
#   Ball.py       #
#  Aldiouma Mbaye # 
#    13/06/2023   #
##################
import sys
import Arriere

#creation de la balle
def create(x,y,vx,vy):
	ball=dict()
	ball["x"]=x
	ball["y"]=y
	ball["vx"]=vx
	ball["vy"]=vy
	return ball

#assensor/mutator
def get_x(ball):
	return ball["x"]

def set_x(ball,x):
	ball["x"]=x

def get_y(ball):
	return ball["y"]

def set_y(ball,y):
	ball["y"]=y

def get_vx(ball):
	return ball["vx"]

def set_vx(ball,b):
	ball["vx"]=b

def get_vy(ball):
	return ball["vy"]

def set_vy(ball,b):
	ball["vy"]=b

def move_up(a):
	a['y']-=1

def move_down(a):
	a['y']+=1	

def show(a) : 
	x=str(int(a["x"])+1)
	y=str(int(a["y"])+1)
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)
	sys.stdout.write("\033[45m")
	sys.stdout.write("O\n")
	sys.stdout.write("\033[40m")

def show1(a) : 
	x=str(int(a["x"])+1)
	y=str(int(a["y"])+1)
	txt="\033["+y+";"+x+"H"
	sys.stdout.write(txt)
	sys.stdout.write("\033[44m")
	sys.stdout.write("<>0\n")
	sys.stdout.write("\033[40m")

def rebound(a,dt,grid):
	i0=int(get_x(a))
	j0=int(get_y(a))
	x0=get_x(a)
	y0=get_y(a)
	a['y']+=dt*a['vy']
	x=get_x(a)
	y=get_y(a)
	i=int(x)
	j=int(y)	
	c=Arriere.get_char(grid,j,i)
	if c == '-':
		if not j==j0:
			vy=get_vy(a)
			set_vy(a,-vy)
			set_y(a,y0)	

def position(a,grid):
	x=get_x(a)
	y=get_y(a)
	i=int(x)
	j=int(y)
	c=Arriere.get_char(grid,j,i)	
	return c

def live(a,dt):
	a['x']+=dt*a['vx']