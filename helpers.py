#!/usr/bin/python3

# The MIT License (MIT)
# Copyright (c) 2016 Stephan Kristyn (meshfields.de) 
# http://meshfields.de/mit-license/
#
# Console Drawing Tool Helpers

import unittest

class Expect(unittest.TestCase):

   def length_of_list_to_be_equal(self,length,inputs):
      self.assertEqual(len(inputs), length)

   def values_to_be_equal(self,a,b):
      self.assertEqual(a, b)

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class VT100:
	CLS = '\x1b[2J' # Clear Screen