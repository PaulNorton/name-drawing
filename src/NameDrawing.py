import random

class NameDrawing:
    def __init__(self, names):
        self.names = []
        for name in names:
            while name in self.names:
                name += '*'
            self.names.append(name)
        

    def draw(self):
        if len(self.names) < 2:
            return 'Not enough people in the list!'
        while True:
            restart = False
            results = {}
            giftees = list(self.names)
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