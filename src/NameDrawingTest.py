import unittest
from NameDrawing import NameDrawing

class TestNameDrawing(unittest.TestCase):
	def setUp(self):
		self.drawing = NameDrawing(['Tom', 'Richard', 'Harry'])

	def test_drawing__everybodyIsGettingSomebodyAGift(self):
		results = self.drawing.draw()
		for person in self.drawing.names:
			self.assertTrue(person in results.keys(), person+" was in the list, but is not getting anybody a gift")

	def test_drawing__everybodyIsGettingAGift(self):
		results = self.drawing.draw()
		for person in self.drawing.names:
			self.assertTrue(person in results.values(), person+" was in the list, but is not receiving a gift")

	def test_drawing__noRandomPeopleInDrawing(self):
		results = self.drawing.draw()
		for gifter, giftee in results.items():
			self.assertTrue(gifter in self.drawing.names, gifter+" was not in the list, but is getting "+giftee+" a gift!")
			self.assertTrue(giftee in self.drawing.names, giftee+" was not in the list, but is getting a gift from "+gifter)

	def test_drawing__nobodyGetsThemselfAGiftLikeKevinFromTheOffice(self):
		results = self.drawing.draw()
		for gifter, giftee in results.items():
			self.assertNotEqual(gifter, giftee, gifter+" is getting themself a gift!")
			
	def test_drawing__oneThousandTimes(self):
		#run one thousand times to see if we get stuck...
		for i in range(1000):
			self.drawing.draw()

if __name__ == '__main__':
	unittest.main()
