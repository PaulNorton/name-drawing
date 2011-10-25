import random

class NameDrawing:
    @staticmethod
    def convertFamilyUnits(familyUnits):
        people = []
        for unit in familyUnits:
            for person in unit:
                exclude = list(unit)
                exclude.remove(person)
                people.append({'name': person, 'exclude': exclude})
        return people
        
    def __init__(self, list):
        self.names = list

    def draw(self):
        if len(self.names) < 2:
            return 'Not enough people in the list!'
        while True:
            restart = False
            results = {}
            giftees = list(self.names)
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
                return results
                
