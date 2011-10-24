import unittest
import random
from NameDrawing import NameDrawing

class TestNameDrawing(unittest.TestCase):
	def setUp(self):
		self.drawing = NameDrawing(['Tom', 'Richard', 'Harry'])

	def test_drawing__everybodyIsGettingSomebodyAGift(self):
		results = self.drawing.draw()
		for key in self.drawing.names:
			self.assertTrue(key in results.keys())

        def test_drawing__everybodyIsGettingAGift(self):
                results = self.drawing.draw()
                for key in self.drawing.names:
                        self.assertTrue(key in results.values())

        def test_drawing__noRandomPeopleInDrawing(self):
                results = self.drawing.draw()
                for key in results:
                        self.assertTrue(key in self.drawing.names)

        def test_drawing__nobodyGetsThemselfAGiftLikeKevinFromTheOffice(self):
                results = self.drawing.draw()
                for gifter, giftee in results.items():
                        self.assertNotEqual(gifter, giftee)

	def test_choice(self):
		choices = ['a', 'b', 'c']
		self.assertTrue(random.choice(choices) in choices)

if __name__ == '__main__':
	unittest.main()
