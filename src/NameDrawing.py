class NameDrawing:
	def __init__(self, people):
		self.people = people
		self.names = [ person['name'] for person in people ]

	def draw(self):
		return { 'Tom':'Ginny', 'Richard':'Harry', 'Susan': 'Albus', 'Harry':'Tom', 'Ginny':'Richard', 'Albus':'Susan' }
