#!/usr/bin/env python3

import tkinter
import random
import math

import time

Shapes = []




class Shape:
	def __init__(self, x, y, colour):
		self.x = x
		self.y = y
		self.colour = colour
		
		self.angle_y = 0
		self.angle_x = 0
		self.angle_z = 0


		self.points_3D = []
		self.points_3D_transposed = []
		self.points_2D = []

	def Matrix_3D_to_2D_1(self):
		for i in range(len(self.points_3D)):
			row = []
			for j in range(len(self.points_3D[0])-1):
				row.append(self.points_3D[i][j])
			self.points_2D.append(row)

		#print(self.points_2D)
		
	def Rotate_x(self, dir):
		self.angle_x +=  dir
		
	def Rotate_y(self, dir):
		self.angle_y += dir
		
	def Rotate_z(self, dir):
		self.angle_z += dir
		
	def Matrix_Multiplication(self, matrix1, matrix2):
		# Construct a result matrix
		pmatrix = []
		for i in range(len(matrix1)):
			row = []
			for j in range(len(matrix2[0])):
				row.append(0)
			pmatrix.append(row)
				
		# Populate the results matrix
		for i in range(len(matrix1)):
			for j in range(len(matrix2[0])):
				for k in range(len(matrix2)):
					temp = matrix1[i][k] * matrix2[k][j]
					pmatrix[i][j] += temp
		return pmatrix
		
	def Matrix_Transpose_3D_to_3D(self):
	# Python Program - Matrix Multiplication

		matrix1 = self.points_3D
				   
		angle = self.angle_y * math.pi / 10
		s = math.sin(angle)
		c = math.cos(angle)
		
		#rotate in the Y axiz
		matrix2 = [[1, 0, 0],
				   [0, c, s],
				   [0, -s, c]]		
				   
		pmatrix = self.Matrix_Multiplication(matrix1,matrix2)
		
		angle = self.angle_z * math.pi / 10
		s = math.sin(angle)
		c = math.cos(angle)
		
		#rotate in the Z axiz
		matrix2 = [[c, s, 0],
				   [-s, c, 0],
				   [0, 0, 1]]
				   
		pmatrix = self.Matrix_Multiplication(pmatrix,matrix2)
		
		angle = self.angle_x * math.pi / 10
		s = math.sin(angle)
		c = math.cos(angle)
		
		#rotate in the X axiz
		matrix2 = [[c, 0, s],
				   [0, 1, 0],
				   [-s, 0, c]]
		
		pmatrix = self.Matrix_Multiplication(pmatrix,matrix2)
		

		
		self.points_3D_transposed = pmatrix


	def Matrix_3D_to_2D(self):
	# Python Program - Matrix Multiplication
	
	# (X,3)      (3,2)     = (X,2)
	# points_3D  Matrix2     points_2D	
		
		matrix1 = self.points_3D_transposed
		matrix2 = [[1, 0], #x
				   [0, 1], #y
				   [0.3, 0.6]] #z
		
		# Construct a result matrix
		pmatrix = []
		for i in range(len(matrix1)):
			row = []
			for j in range(len(matrix2[0])):
				row.append(0)
			pmatrix.append(row)
				
		# Populate the results matrix
		for i in range(len(matrix1)):
			for j in range(len(matrix2[0])):
				for k in range(len(matrix2)):
					temp = matrix1[i][k] * matrix2[k][j]
					pmatrix[i][j] += temp
		
		self.points_2D = pmatrix


def Mark_Point(x,y):
	w.create_line(x - 5, y - 5, x+5, y+5, fill="red")
	w.create_line(x + 5, y - 5, x-5, y+5, fill="red")

def draw_shape(critter):

	Mark_Point(critter.x,critter.y)

	points_2D = critter.points_2D
	s = points_2D[0]
	for point in points_2D:
		e = point
		w.create_line(critter.x + s[0], critter.y + s[1], critter.x + e[0], critter.y + e[1], fill=critter.colour)
		s = e
		
def fill_shape(shape):

	Mark_Point(shape.x,shape.y)


	points_2D = shape.points_2D
	for p in points_2D:
		p[0] += shape.x
		p[1] += shape.y
	
	if(len(points_2D) == 1):
		Mark_Point(points_2D[0][0], points_2D[0][1])
	elif(len(points_2D) == 2):
		w.create_line(points_2D[0][0], points_2D[0][1], points_2D[1][0], points_2D[1][1], fill=shape.colour)
	else:
		w.create_polygon(points_2D, outline='black', fill=shape.colour, width=1)

def Create_Rubix():
	for x in range(-1,2):
		for y in range(-1,2):
			for z in range(-1,2):
				if (x == 0 and y == 0 and z == 0):
					#nothing
					temp = "naa"
				else:
					#print(str(x) + ", " + str(y) + ", " +str(z))
					Create_Cube(x*50,y*50,z*50)
	Create_Axis(0,0,0)
	#Create_Cube(0,-50,-50)
	#Create_Arrow(50,0,0)
	
	
def Create_Axis(x, y, z):
	c = Shape(150,150,"blue")
	p1 = [0, 0, 70]
	p2 = [0, 0, 300]

	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	Shapes.append(c)
	
	c = Shape(150,150,"blue")
	p1 = [0, 0, -70]
	p2 = [0, 0, -300]

	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	Shapes.append(c)
	
	c = Shape(150,150,"red")
	p1 = [0, 70, 0]
	p2 = [0, 300, 0]

	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	Shapes.append(c)
	
	c = Shape(150,150,"red")
	p1 = [0, -70, 0]
	p2 = [0, -300, 0]

	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	Shapes.append(c)
	
	c = Shape(150,150,"green")
	p1 = [70, 0, 0]
	p2 = [300, 0, 0]

	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	Shapes.append(c)
	
	c = Shape(150,150,"green")
	p1 = [-70, 0, 0]
	p2 = [-300, 0, 0]

	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	Shapes.append(c)
	
def Create_Arrow(x, y, z):
	c = Shape(150,150,"blue")
	p1 = [x - 40, y + 0, z]
	p2 = [x + 40, y + 0, z]
	p3 = [x + 40, y + 5,  z]
	p4 = [x - 35, y + 5,  z]
	p5 = [x + 0, y + 20,  z]
	p6 = [x + -5, y + 20,  z]
	
	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.points_3D.append(p3)
	c.points_3D.append(p4)
	c.points_3D.append(p5)
	c.points_3D.append(p6)
	
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	
	Shapes.append(c)
	draw_shape(c)
	fill_shape(c)

def Create_Cube(x, y, z):

	

	c = Shape(150,150,"lightblue")
	p1 = [x + 20, y + -20, z + 20]
	p2 = [x + -20,y + -20, z + 20]
	p3 = [x + -20,y + 20,  z + 20]
	p4 = [x + 20, y + 20,  z + 20]
	
	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.points_3D.append(p3)
	c.points_3D.append(p4)
	
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	
	Shapes.append(c)
	draw_shape(c)
	fill_shape(c)
	
	c = Shape(150,150,"lightgreen")
	p1 = [x + 20, y + -20, z - 20]
	p2 = [x + -20,y + -20, z - 20]
	p3 = [x + -20,y + 20,  z - 20]
	p4 = [x + 20, y + 20,  z - 20]
	
	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.points_3D.append(p3)
	c.points_3D.append(p4)
	
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	
	Shapes.append(c)
	draw_shape(c)
	fill_shape(c)
	
	c = Shape(150,150,"red")
	p1 = [x + 20, y + -20, z + -20]
	p2 = [x + 20, y + -20, z + 20]
	p3 = [x + 20, y + 20,  z + 20]
	p4 = [x + 20, y + 20,  z + -20]
	
	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.points_3D.append(p3)
	c.points_3D.append(p4)
	
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	
	Shapes.append(c)
	draw_shape(c)
	fill_shape(c)
	
	c = Shape(150,150,"orange")
	p1 = [x - 20, y + -20, z + -20]
	p2 = [x - 20, y + -20, z + 20]
	p3 = [x - 20, y + 20,  z + 20]
	p4 = [x - 20, y + 20,  z + -20]
	
	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.points_3D.append(p3)
	c.points_3D.append(p4)
	
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	
	Shapes.append(c)
	draw_shape(c)
	fill_shape(c)
	
	c = Shape(150,150,"purple")
	p1 = [x - 20, y + 20, z + -20]
	p2 = [x - 20, y + 20, z + 20]
	p3 = [x + 20, y + 20,  z + 20]
	p4 = [x + 20, y + 20,  z + -20]
	
	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.points_3D.append(p3)
	c.points_3D.append(p4)
	
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	
	Shapes.append(c)
	draw_shape(c)
	fill_shape(c)
	
	c = Shape(150,150,"pink")
	p1 = [x - 20, y - 20, z + -20]
	p2 = [x - 20, y - 20, z + 20]
	p3 = [x + 20, y - 20,  z + 20]
	p4 = [x + 20, y - 20,  z + -20]
	
	c.points_3D.append(p1)
	c.points_3D.append(p2)
	c.points_3D.append(p3)
	c.points_3D.append(p4)
	
	c.Matrix_Transpose_3D_to_3D()
	c.Matrix_3D_to_2D()
	
	Shapes.append(c)
	draw_shape(c)
	fill_shape(c)
	
def draw():
	w.create_rectangle(0, 0, 300, 300, fill="white")

	for shape in Shapes:
		shape.Matrix_Transpose_3D_to_3D()
		shape.Matrix_3D_to_2D()
		
	#Order the shapes by the three dimentions by the sum of their points.
	Shapes.sort(key=lambda x: sum(c[0] for c in x.points_3D_transposed), reverse=False)
	Shapes.sort(key=lambda x: sum(c[1] for c in x.points_3D_transposed), reverse=True)
	Shapes.sort(key=lambda x: sum(c[2] for c in x.points_3D_transposed), reverse=False)
	for shape in Shapes:
		fill_shape(shape)
		
	#reset position
	for shape in Shapes:
		if (shape.angle_x % 5) == 0 and (shape.angle_y % 5) == 0 and (shape.angle_z % 5) == 0:
			shape.points_3D = shape.points_3D_transposed
			shape.angle_y = 0
			shape.angle_x = 0
			shape.angle_z = 0
	

def callback(source):
	#print ("called the callback from: " + source)
	if source == 'b':
		root.title("b")
		for i in range(1,10):
			time.sleep(1)
			for shape in Shapes:
				shape.Rotate_y(1)
			draw()
	if source == 'reset':
		root.title("reset")
		for shape in Shapes:
			shape.points_3D = shape.points_3D_transposed
			shape.angle_y = 0
			shape.angle_x = 0
			shape.angle_z = 0
	if source == 'a':
		root.title("a")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][0] > 25):
				shape.Rotate_y(1)
		draw()
		
	if source == 'k':
		root.title("k")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][0] > 25):
				shape.Rotate_y(-1)
		draw()
		
	if source == 'x_up':
		root.title("x_up")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][0] < -25):
				shape.Rotate_y(1)
		draw()
	if source == 'x_down':
		root.title("x_down")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][0] < -25):
				shape.Rotate_y(-1)
		draw()
		
	if source == 'y_down':
		root.title("y_down")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][1] < -25):
				shape.Rotate_x(-1)
		draw()
		
	if source == 'y_up':
		root.title("y_up")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][1] < -25):
				shape.Rotate_x(1)
		draw()
		
	if source == 'y_down2':
		root.title("y_down2")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][1] >25):
				shape.Rotate_x(-1)
		draw()
		
	if source == 'y_up2':
		root.title("y_up2")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][1] >25):
				shape.Rotate_x(1)
		draw()
		
	if source == 'z_down':
		root.title("z_down")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][2] < -25):
				shape.Rotate_z(-1)
		draw()
		
	if source == 'z_up':
		root.title("z_down")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][2] < -25):
				shape.Rotate_z(1)
		draw()
		
	if source == 'z_down2':
		root.title("z_down")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][2] > 25):
				shape.Rotate_z(-1)
		draw()
		
	if source == 'z_up2':
		root.title("z_down")
		for shape in Shapes:
			if(shape.points_3D_transposed[0][2] > 25):
				shape.Rotate_z(1)
		draw()
	
	#rotation of whole cube
	if source == 'z_R':
		root.title("z_R")
		for shape in Shapes:
			shape.Rotate_z(1)
		draw()
		
	if source == 'z_L':
		root.title("z_L")
		for shape in Shapes:
			shape.Rotate_z(-1)
		draw()
		
	if source == 'y_R':
		root.title("y_R")
		for shape in Shapes:
			shape.Rotate_y(1)
		draw()
		
	if source == 'y_L':
		root.title("y_L")
		for shape in Shapes:
			shape.Rotate_y(-1)
		draw()
		
	if source == 'x_R':
		root.title("x_R")
		for shape in Shapes:
			shape.Rotate_x(1)
		draw()
		
	if source == 'x_L':
		root.title("x_L")
		for shape in Shapes:
			shape.Rotate_x(-1)
		draw()
		
	if source == 'c':
		root.title("c")

		
# Initialise Window
root  = tkinter.Tk()
root.geometry("300x600")

root.title("TEST")

# create a menu
menu = tkinter.Menu(root)
root.config(menu=menu)

filemenu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command= lambda: callback('reset'))
filemenu.add_command(label="Open...", command= lambda: callback('b'))
filemenu.add_separator()
filemenu.add_command(label="Exit", command= lambda: callback('c'))

helpmenu = tkinter.Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command= lambda: callback('d'))

# Add buttons
b = tkinter.Button(root, text="Bottom (left)", command= lambda: callback('a'))
b.place(height=20, width=80, x=0, y=0)

c = tkinter.Button(root, text="Bottom (right)", command= lambda: callback('k'))
c.place(height=20, width=80, x=0, y=20)

x_up = tkinter.Button(root, text="Top (left)", command= lambda: callback('x_up'))
x_up.place(height=20, width=80, x=80, y=0)

x_down = tkinter.Button(root, text="Top (right)", command= lambda: callback('x_down'))
x_down.place(height=20, width=80, x=80, y=20)

y_up = tkinter.Button(root, text="Top (left)", command= lambda: callback('y_up'))
y_up.place(height=20, width=80, x=0, y=100)

y_down = tkinter.Button(root, text="Top (right)", command= lambda: callback('y_down'))
y_down.place(height=20, width=80, x=80, y=100)

y_up2 = tkinter.Button(root, text="Top (left)", command= lambda: callback('y_up2'))
y_up2.place(height=20, width=80, x=0, y=120)

y_down2 = tkinter.Button(root, text="Top (right)", command= lambda: callback('y_down2'))
y_down2.place(height=20, width=80, x=80, y=120)

z_up = tkinter.Button(root, text="Top (left)", command= lambda: callback('z_up'))
z_up.place(height=20, width=80, x=0, y=200)

z_down = tkinter.Button(root, text="Top (right)", command= lambda: callback('z_down'))
z_down.place(height=20, width=80, x=80, y=200)

z_up2 = tkinter.Button(root, text="Top (left)", command= lambda: callback('z_up2'))
z_up2.place(height=20, width=80, x=0, y=220)

z_down2 = tkinter.Button(root, text="Top (right)", command= lambda: callback('z_down2'))
z_down2.place(height=20, width=80, x=80, y=220)

#rotation of whole cube
z_L = tkinter.Button(root, text="Z Left", command= lambda: callback('z_L'))
z_L.place(height=20, width=80, x=0, y=240)

z_R = tkinter.Button(root, text="Z Right", command= lambda: callback('z_R'))
z_R.place(height=20, width=80, x=80, y=240)

y_L = tkinter.Button(root, text="Y Left", command= lambda: callback('y_L'))
y_L.place(height=20, width=80, x=0, y=260)

y_R = tkinter.Button(root, text="Y Right", command= lambda: callback('y_R'))
y_R.place(height=20, width=80, x=80, y=260)

x_L = tkinter.Button(root, text="X Left", command= lambda: callback('x_L'))
x_L.place(height=20, width=80, x=0, y=280)

x_R = tkinter.Button(root, text="X Right", command= lambda: callback('x_R'))
x_R.place(height=20, width=80, x=80, y=280)


w = tkinter.Canvas(root, width=300, height=300)
w.place(x=0, y=300)

w.create_line(2, 2, 2, 300, fill="red")
w.create_line(2, 300,300,300, fill="blue")
w.create_line(300, 300, 300, 2, fill="yellow")
w.create_line(300, 2, 2, 2, fill="green")

#initialise cube
Create_Rubix()

tkinter.mainloop()
