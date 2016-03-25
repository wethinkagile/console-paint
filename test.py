#!/usr/bin/python3

# The MIT License (MIT)
# Copyright (c) 2016 Stephan Kristyn (meshfields.de) 
# http://meshfields.de/mit-license/
#
# Console Drawing Tool Tests

from methods import *

class Expect(unittest.TestCase):

	def length_of_list_to_be_equal(self,length,inputs):
		self.assertEqual(len(inputs), length)

	def values_to_be_equal(self,a,b):
		self.assertEqual(a, b)

expect = Expect()


print("\nUnit Tests\n")

def testGetLine():

	print(color.BOLD+"> Should get Coordinates of Line"+color.END)

	mockLine = getLine(1,2,6,2) # Mock
	expect.values_to_be_equal(mockLine,[(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2)])

def testColoriseLine():

	print(color.BOLD+"> Should colorise the Coordinates"+color.END)

	mockLine = getLine(1,2,6,2) # Mock
	coloredMockLine = colorise(mockLine,'x')
	expect.values_to_be_equal(coloredMockLine,[(1, 2, 'x'), (2, 2, 'x'), (3, 2, 'x'), (4, 2, 'x'), (5, 2, 'x'), (6, 2, 'x')])


def testSetPixel():
	
	print(color.BOLD+"> Should Set Color for a specific Coordinate"+color.END)

	pixels = []  # Cleans global pixels
	testPixels() 
	testColor  = setPixel(1,3,'o')
	testColor2 = setPixel(22,22,'-')

	expect.values_to_be_equal(testColor,True)
	expect.values_to_be_equal(testColor2,False)


def testGetCanvasTuples():

	print(color.BOLD+"> Should get colored Canvas"+color.END)
	
	mockCanvas = getCanvasTuples(20,4) # Mock
	expect.values_to_be_equal(mockCanvas,([(0, 0, '-'), (1, 0, '-'), (2, 0, '-'), (3, 0, '-'), (4, 0, '-'), (5, 0, '-'), (6, 0, '-'), (7, 0, '-'), (8, 0, '-'), (9, 0, '-'), (10, 0, '-'), (11, 0, '-'), (12, 0, '-'), (13, 0, '-'), (14, 0, '-'), (15, 0, '-'), (16, 0, '-'), (17, 0, '-'), (18, 0, '-'), (19, 0, '-'), (20, 0, '-'), (20, 0, '|'), (20, 1, '|'), (20, 2, '|'), (20, 3, '|'), (20, 4, '|'), (20, 4, '-'), (19, 4, '-'), (18, 4, '-'), (17, 4, '-'), (16, 4, '-'), (15, 4, '-'), (14, 4, '-'), (13, 4, '-'), (12, 4, '-'), (11, 4, '-'), (10, 4, '-'), (9, 4, '-'), (8, 4, '-'), (7, 4, '-'), (6, 4, '-'), (5, 4, '-'), (4, 4, '-'), (3, 4, '-'), (2, 4, '-'), (1, 4, '-'), (0, 4, '-'), (0, 0, '|'), (0, 1, '|'), (0, 2, '|'), (0, 3, '|'), (0, 4, '|')]))

def testGetRectangleTuples():

	print(color.BOLD+"> Should get colored Rectangle"+color.END)
	
	mockRectangle = getRectangleTuples(16,1,20,3)
	expect.values_to_be_equal(mockRectangle,([(16, 1, 'x'), (17, 1, 'x'), (18, 1, 'x'), (19, 1, 'x'), (20, 1, 'x'), (20, 1, 'x'), (20, 2, 'x'), (20, 3, 'x'), (20, 3, 'x'), (19, 3, 'x'), (18, 3, 'x'), (17, 3, 'x'), (16, 3, 'x'), (16, 1, 'x'), (16, 2, 'x'), (16, 3, 'x')]))

def testPixels():
	
	print(color.BOLD+"> Should add reduntant Items to pixels and uniquify"+color.END)

	mockTuples = [(1,2,'x'),(1,2,'x'),(1,3,'-')]
	localPixels = addPixels(mockTuples)
	
	expect.values_to_be_equal(len(localPixels)+1,len(mockTuples))
	

def testGetPixel():
	
	print(color.BOLD+"> Should Get Color Of Coordinates"+color.END)

	testPixels() 
	testPixel       = getPixel(1,2)
	testPixelNone   = getPixel(0,0)
	testPixelCanvas = getPixel(1,3)

	expect.values_to_be_equal(testPixel,'x')
	expect.values_to_be_equal(testPixelNone,False)
	expect.values_to_be_equal(testPixelCanvas,'-')

def testInitCanvasArea():

	b = 20
	d = 4
	canvasAreaTuples = initCanvasArea(b,d)
	expect.values_to_be_equal(canvasAreaTuples,[(19, 3, ' '), (19, 2, ' '), (19, 1, ' '), (18, 3, ' '), (18, 2, ' '), (18, 1, ' '), (17, 3, ' '), (17, 2, ' '), (17, 1, ' '), (16, 3, ' '), (16, 2, ' '), (16, 1, ' '), (15, 3, ' '), (15, 2, ' '), (15, 1, ' '), (14, 3, ' '), (14, 2, ' '), (14, 1, ' '), (13, 3, ' '), (13, 2, ' '), (13, 1, ' '), (12, 3, ' '), (12, 2, ' '), (12, 1, ' '), (11, 3, ' '), (11, 2, ' '), (11, 1, ' '), (10, 3, ' '), (10, 2, ' '), (10, 1, ' '), (9, 3, ' '), (9, 2, ' '), (9, 1, ' '), (8, 3, ' '), (8, 2, ' '), (8, 1, ' '), (7, 3, ' '), (7, 2, ' '), (7, 1, ' '), (6, 3, ' '), (6, 2, ' '), (6, 1, ' '), (5, 3, ' '), (5, 2, ' '), (5, 1, ' '), (4, 3, ' '), (4, 2, ' '), (4, 1, ' '), (3, 3, ' '), (3, 2, ' '), (3, 1, ' '), (2, 3, ' '), (2, 2, ' '), (2, 1, ' '), (1, 3, ' '), (1, 2, ' '), (1, 1, ' ')])


testGetPixel()
testSetPixel()
testInitCanvasArea()
testGetCanvasTuples()
testGetRectangleTuples()
testColoriseLine()
testGetLine()

print("\n"+color.GREEN+"8 Tests passed."+color.END+"\n")