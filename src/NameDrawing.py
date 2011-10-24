import random

class NameDrawing:
<<<<<<< HEAD
    def __init__(self, list):
        self.names = list
            
=======
    def __init__(self, people):
        self.people = people
        self.names = [ person['name'] for person in people ]
>>>>>>> a6fecdc8e8b166c9e707c1dc7688c5dfa574980f

    def draw(self):
        if len(self.names) < 2:
            return 'Not enough people in the list!'
        while True:
            restart = False
            results = {}
            giftees = list(self.names)
<<<<<<< HEAD
            for gifter in self.names:
                while True:
                    random_index = random.randint(0, (len(giftees) - 1))
                    possible_giftee = giftees[random_index]
                    if possible_giftee['name'] not in gifter['exclude'] and possible_giftee != gifter:
                        break
                    else:
                        restart = True
                        for remaining_giftee in giftees:
                            if remaining_giftee['name'] not in gifter['exclude'] and remaining_giftee != gifter:
                                restart = False
                        if restart == True:
                            break
                results[gifter['name']] = giftees.pop(random_index)['name']
            if restart == False:
                print results
                #return results
                break
                
people = [{'exclude': [], 'name': 'Tom'}, {'exclude': ['Susan'], 'name': 'Richard'}, {'exclude': ['Richard'], 'name': 'Susan'}, {'exclude': ['Ginny', 'Albus'], 'name': 'Harry'}, {'exclude': ['Harry', 'Albus'], 'name': 'Ginny'}, {'exclude': ['Harry', 'Ginny'], 'name': 'Albus'}]
test = NameDrawing(people)
print test.draw()
=======
            for a in self.names:
                while True:
                    c = random.randint(0, (len(giftees) - 1))
                    b = giftees[c]
                    if b != a:
                        break
                    elif len(giftees) == 1 and a == giftees[0]:
                        restart = True
                        break
                results[a] = giftees.pop(c)
            if restart == False:
                return results
                break
>>>>>>> a6fecdc8e8b166c9e707c1dc7688c5dfa574980f
