import unittest
import random

class TestNameDrawing(unittest.TestCase):
	def setUp(self):
		self.drawing = ''

	def test_choice(self):
		choices = ['a', 'b', 'c']
		self.assertTrue(random.choice(choices) in choices)

if __name__ == '__main__':
	unittest.main()
