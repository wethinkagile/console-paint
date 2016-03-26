#!/usr/bin/python3

# The MIT License (MIT)
# Copyright (c) 2016 Stephan Kristyn (meshfields.de) 
# http://meshfields.de/mit-license/
#
# Console Drawing Tool Methods

import sys 		# essential
import re 		# regex
from helpers import *

# Globals

color  = Color()
vt100  = VT100()
pixels = []
b_canvas = 0
d_canvas = 0

# Methods

def colorise(listOfTuples, color):
	
	# Method: <colorise>
	#
	# Wants: List of Tuples [(x1,y1), (xn,yn)] and color as a String
	# Gives: Line of n-Tuples [(x1,y1,color), (xn,yn,color)]

	newLine = []
	for item in listOfTuples:
		newLine.append( (item[0], item[1], color) )
	return newLine

def getLine(x1,y1,x2,y2):
    
    # Method: <getLine>
	#
	# Wants: 2-Tuple [(x1,y1), (x2,y2)]
	# Gives: Line of n-Tuples [(x1,y1), (xn,yn)] between two Input Coordinates
   
    # Setup initial conditions
    dx = x2 - x1
    dy = y2 - y1
 
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
 
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
 
    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True
 
    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
 
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
 
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx
 
    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


def getCanvasTuples(x,y):	

	# Method: <getCanvasTuples>
	#
	# Wants: 1-Tuple (w,h)
	# Gives: Lines of colored n-Tuples of Canvas a,b,c,d [(x1,y1,color1),(xn,yn,colorn)]

	xa = 0
	ya = 0

	xb = x
	yb = 0

	xc = x
	yc = y

	xd = 0
	yd = y

	canvasLine1 = getLine (xa,ya,xb,yb)
	canvasLine2 = getLine (xb,yb,xc,yc)
	canvasLine3 = getLine (xc,yc,xd,yd)
	canvasLine4 = getLine (xa,ya,xd,yd)

	coloredCanvasLine1 = colorise(canvasLine1,'.')
	coloredCanvasLine2 = colorise(canvasLine2,'.')
	coloredCanvasLine3 = colorise(canvasLine3,'.')
	coloredCanvasLine4 = colorise(canvasLine4,'.')

	# Return one List of Colored Tuples
	return coloredCanvasLine1 + coloredCanvasLine2 + coloredCanvasLine3 + coloredCanvasLine4

def getRectangleTuples(x1,y1,x2,y2):	

	# Method: <getRectangleTuples>
	#
	# Wants: 1-Tuple (w,h)
	# Gives: Lines of n-Tuples of Rectangle a,b,c,d

	xa = x1
	ya = y1

	xb = x2
	yb = y1

	xc = x2
	yc = y2

	xd = x1
	yd = y2

	rectangleLine1 = getLine (xa,ya,xb,yb)
	rectangleLine2 = getLine (xb,yb,xc,yc)
	rectangleLine3 = getLine (xc,yc,xd,yd)
	rectangleLine4 = getLine (xa,ya,xd,yd)

	coloredRectangleLine1 = colorise(rectangleLine1,'x')
	coloredRectangleLine2 = colorise(rectangleLine2,'x')
	coloredRectangleLine3 = colorise(rectangleLine3,'x')
	coloredRectangleLine4 = colorise(rectangleLine4,'x')

	# Return one List of Colored Tuples
	return coloredRectangleLine1 + coloredRectangleLine2 + coloredRectangleLine3 + coloredRectangleLine4

def drawLine(lineInput):

	# Method: <drawLine>
	#
	# Wants: 4-Tuple (x1,y1,x2,y2)
	# Gives: Line of colored n-Tuples
	
	lineInput = lineInput.split() # L x1 y1 x2 y2
	
	# Production
	lineTuples        = getLine(int(lineInput[1]),int(lineInput[2]),int(lineInput[3]),int(lineInput[4]))
	coloredLineTuples = colorise(lineTuples,'x')

	substitutePixels(coloredLineTuples)
	restart(True)


def drawCanvas(canvasInput):

	# Method: <drawCanvas>
	#
	# Wants: 3-Tuple (Command, width, height)
	# Gives: Calculates and Adds Coordinates to global Pixel Array

	canvasInput = canvasInput.split() # C w h
	
	# Calculate Area Pixels
	global b_canvas
	global d_canvas
	b_canvas = int(canvasInput[1])
	d_canvas = int(canvasInput[2])
	canvasAreaTuples = initCanvasArea(b_canvas,d_canvas)
	addPixels(canvasAreaTuples)
	
	# Calculate Border Pixels
	canvasTuples = getCanvasTuples(int(canvasInput[1]),int(canvasInput[2]))	
	addPixels(canvasTuples) 
	restart(True)

def initCanvasArea(b, d):

	# Method: <initCanvasArea>
	#
	# Wants: Tuple (b_point, d_point) of "abcd" of a rectangle
	# Gives: Calculates Coordinates Area and colors them ' '.
	
	canvasAreaTuples = []
	for x in range(b-1,0,-1):
		for y in range (d-1,0,-1):
			canvasAreaTuples += [(x,y,' ')]
	return canvasAreaTuples

def drawRectangle(rectangleInput):

	rectangleInput = rectangleInput.split() # R x1 y1 x2 y2

	# Production
	rectangleTuples = getRectangleTuples(int(rectangleInput[1]),int(rectangleInput[2]),int(rectangleInput[3]),int(rectangleInput[4]))
	substitutePixels(rectangleTuples)
	restart(True)


def addPixels(listOfTuples):

	# Method: <addPixels>
	# Wants: listOfTuples [(x1,y1,color1),(xn,yn,colorn)]
	# Returns: Changes global pixels and also return local copy for tests

	global pixels 

	for k,v in enumerate(listOfTuples):
		setPixel(v[0], v[1], v[2])

	pixels += listOfTuples
	pixels = list(set(pixels)) # Uniquify
	return pixels

def substitutePixels(listOfTuples):

	# Method: <addPixels>
	# Wants: listOfTuples [(x1,y1,color1),(xn,yn,colorn)]
	# Returns: Changes global pixels and also return local copy for tests

	global pixels 

	for k,v in enumerate(listOfTuples):
		setPixel(v[0], v[1], v[2])
	pixels = list(set(pixels)) # Uniquify
	return pixels


def getPixel(x,y):
	
	# Method: <getPixel>
	# Wants: Single Tuple (x1,y1)
	# Returns: Checks if Tuple is in global pixels and returns color, Returns False if empty or Canvas Colors: '-' and '|''

	for k,v in enumerate(pixels):
		if x == v[0] and y == v[1]:
			return v[2]
	return False


def setPixel(x,y, newColor):

	# Method: <setPixel>
	# Wants: Single Tuple (x1,y1)
	# Returns: Checks if Tuple is in pixels and changes color

	global pixels

	for k,v in enumerate(pixels):
		if (x,y) == (v[0],v[1]):
			del pixels[k]  			
			pixels += [(x,y,newColor)]
			return True
	return False

def drawFourNeighbour(x, y, oldColor, newColor):

	# Method: <drawFourNeighbour>
	# Wants: Set of 1-Tuple Coordinates, old and new color
	# Returns: Nothing. Fills pixels with newColor by using getPixel and setPixel

	if (getPixel(x,y) == oldColor):
		setPixel(x, y, newColor)
		drawFourNeighbour(x, y + 1, oldColor, newColor); # below
		drawFourNeighbour(x, y - 1, oldColor, newColor); # above
		drawFourNeighbour(x - 1, y, oldColor, newColor); # left
		drawFourNeighbour(x + 1, y, oldColor, newColor); # right
	return

def drawBucketFill(bucketFillInput):

	# Method: <drawBucketFill>
	# Wants: Raw User Input "B x y". Wrapper for drawFourNeighbour Algorithm
	# Returns: Nothing. Calls restart() with plot=True.

	bucketFillInput = bucketFillInput.split() # B x y color
	drawFourNeighbour(int(bucketFillInput[1]),int(bucketFillInput[2]),' ',bucketFillInput[3])
	restart(True)

# One Test in here because of the global. ToDo: OOP-ify everything
expect = Expect()
def testDrawFourNeighbour():

	print(color.BOLD+"> Should bucket fill a 20,4 Canvas with o"+color.END)

	global pixels
	pixels = []

	canvasAreaTuples = initCanvasArea(20,4)
	addPixels(canvasAreaTuples)
	
	# Calculate Border Pixels
	canvasTuples = getCanvasTuples(20,4)	
	addPixels(canvasTuples) 

	# print(pixels)

	# Bucket Fill
	drawFourNeighbour(15, 3, ' ', 'o')

	# Test Bucket Fill
	expect.values_to_be_equal(len(pixels),105)


def plotPixels():

	# Method: <plotPixels>
	# Wants: nothing
	# Returns: nothing. Creates a console output for user to see.

	pixels.sort()
	print(vt100.CLS)
	
	for k,v in enumerate(pixels):

		x     = v[0]
		y 	  = v[1]
		color = v[2]

		if k > 0 and x != pixels[k-1][0]:
			print("")
		print(color,end="")
	print("")


def handleUserInputError():
	print(vt100.CLS)
	print('Wrong Input Format! Use [C w h], [L x1 x2 y1 y2], [R x1 x2 y1 y2], [B x y] or [Q]')
	restart(False)

def handleNoCanvasError():
	print(vt100.CLS)
	print('Draw a Canvas First!')
	restart(False)

def inputHandling(userInput):

	userInputType = userInput.split()[0]

	# User Experience

	r = re.compile('[^LCRBQ]')
	if r.search(userInputType) is not None:
		handleUserInputError()

	if userInputType == 'C':
		if len(userInput.split()) != 3:
			handleUserInputError()
		else:
			drawCanvas(userInput)

	if userInputType == 'L':

		if len(userInput.split()) != 5:
			handleUserInputError()
		if len(pixels) == 0:
			handleNoCanvasError()
		else:
			drawLine(userInput)
		
	if userInputType == 'R':
		
		if len(userInput.split()) != 5:
			handleUserInputError()
		if len(pixels) == 0:
			handleNoCanvasError()
		else:
			drawRectangle(userInput)
		
			
	if userInputType == 'B':
		
		if len(userInput.split()) != 4:
			handleUserInputError()
		if len(pixels) == 0:
			handleNoCanvasError()
		else:
			drawBucketFill(userInput)

	if userInputType == 'Q':

		if len(userInput.split()) != 1:
			handleUserInputError()
		else:
			sys.exit(0)

def restart(plot):
	if len(pixels) != 0 and plot is True:
		plotPixels()
	userInput = input('['+color.BOLD+'L'+color.END+'ine] ['+color.BOLD+'C'+color.END+'anvas] ['+color.BOLD+'R'+color.END+'ectangle] ['+color.BOLD+'B'+color.END+'ucketfill] ['+color.BOLD+'Q'+color.END+'uit]')
	inputHandling(userInput)

