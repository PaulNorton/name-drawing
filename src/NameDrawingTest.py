import unittest
from NameDrawing import NameDrawing

class TestNameDrawing(unittest.TestCase):
	def setUp(self):
		self.familyUnits = [
			['Tom'], 
			['Richard', 'Susan'], 
			['Harry', 'Ginny', 'Albus'],
		]
		people = []
		self.list_of_names = []
		for unit in self.familyUnits:
			for person in unit:
				self.list_of_names.append(person)
				exclude = list(unit)
				exclude.remove(person)
				people.append({'name': person, 'exclude': exclude})
				
		self.drawing = NameDrawing(people)

	def test_drawing__everybodyIsGettingSomebodyAGift(self):
		results = self.drawing.draw()
		for person in self.drawing.names:
			self.assertTrue(person['name'] in results.keys(), person['name']+" was in the list, but is not getting anybody a gift")

	def test_drawing__everybodyIsGettingAGift(self):
		results = self.drawing.draw()
		for person in self.drawing.names:
			self.assertTrue(person['name'] in results.values(), person['name']+" was in the list, but is not receiving a gift")

	def test_drawing__noRandomPeopleInDrawing(self):
		results = self.drawing.draw()
		for gifter, giftee in results.items():
			self.assertTrue(gifter in self.list_of_names, gifter+" was not in the list, but is getting "+giftee+" a gift!")
			self.assertTrue(giftee in self.list_of_names, giftee+" was not in the list, but is getting a gift from "+gifter)

	def test_drawing__nobodyGetsThemselfAGiftLikeKevinFromTheOffice(self):
		results = self.drawing.draw()
		for gifter, giftee in results.items():
			self.assertNotEqual(gifter, giftee, gifter+" is getting themself a gift!")
			
	def test_drawing__nobodyGetsFamilyUnitMemberAGift(self):
		results = self.drawing.draw()
		for unit in self.familyUnits:
			for gifter in unit:
				giftee = results[gifter]
				self.assertFalse(giftee in unit, gifter+" is getting their family unit member, "+giftee+", a gift")
    
	def test_drawing__oneThousandTimes(self):
		#run one thousand times to see if we get stuck...
		for i in range(1000):
			self.drawing.draw()			

if __name__ == '__main__':
	unittest.main()
	
