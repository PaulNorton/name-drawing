import random


welcome_message = """Welcome to the NameDrawer!\n
For each family, type names in this format: Tom, Dick, Harry
When you're finished, just hit return.\n"""


class Person:
    def __init__(self, name, family):
        self.name = name
        self.family = set(family)

    def is_valid_giftee(self, possible_gifter):
        return self.name not in possible_gifter.family


class NameDrawing:
    def __init__(self, family_units):
        self.people = self.convert_family_units(family_units)

    @staticmethod
    def convert_family_units(family_units):
        return [Person(name, family) for family in family_units for name in family]

    def draw(self):
        if len(self.people) < 2:
            raise Exception('Not enough people in the list!')

        while True:
            results = self.attempt_draw()
            if results is not None:
                return results

    def attempt_draw(self):
        results = {}
        giftees = set(self.people)
        for gifter in self.people:
            valid_giftees = [person for person in giftees if person.is_valid_giftee(gifter)]
            if not valid_giftees:
                return None
            giftee = random.choice(valid_giftees)
            results[gifter.name] = giftee.name
            giftees.remove(giftee)
        return results


def get_input():
    family_units = []
    family_count = 1
    print(welcome_message)
    while True:
        people = input(f'Family #{family_count}: ')
        if people == "":
            break
        family = people.split(", ")
        family_units.append(family)
        family_count += 1
    return family_units


if __name__ == '__main__':
    family_units = get_input()
    drawing = NameDrawing(family_units)
    results = drawing.draw()

    print('\n(Gifter : Giftee)')
    for gifter, giftee in results.items():
        print(f'{gifter} : {giftee}')
