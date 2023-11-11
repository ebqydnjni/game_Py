##################
#   Ball.py       #
#  Aldiouma Mbaye # 
#    13/06/2023   #
##################
import sys

def create(file):
	img={'width':None,'height':None,'grid':[]}
	
	myfile=open(file, "r")	
	s=myfile.read()
	myfile.close()

	lines=s.splitlines()
	for line in lines:
		img['grid'].append(list(line))

		img['height']=len(lines)
		img['width']=len(lines[0])

	return img

def show(img):
	print(img)

def get_width(img):
	return img['width']

def get_height(img):
	return img['height']

def set_height(img,b):
	img['height']=b

def get_grid(img):
	return img['grid']

def set_grid(img,b):
	img['grid']=b
	img['height']=len(b)
	img['width']=len(b[0])

def get_char(img,line_index,column_index):
	return img['grid'][line_index][column_index]

def set_char(img,line_index,column_index,c):
	img['grid'][line_index][column_index]=c

def show(img):
	for j in range(img['height']):
		sys.stdout.write("\033["
		+str(j+1)
		+";"
		+str(1)
		+"H")
		for k in range(img['width']):
			sys.stdout.write(get_char(img,j,k))
	sys.stdout.write("\n")
