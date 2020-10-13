from datetime import date

class Donkey():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'petting area'
        self.walking = True
        self.shift = shift


class Llama():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'petting area'
        self.walking = True
        self.shift = shift

class Goat():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'petting area'
        self.walking = True
        self.shift = shift

class Chicken():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'petting area'
        self.walking = True
        self.shift = shift

class Ostrich():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'petting area'
        self.walking = True
        self.shift = shift

class Copperhead():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'glass tank'
        self.slithering = True
        self.shift = shift
        

class RatSnake():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'glass tank'
        self.slithering = True
        self.shift = shift


class SnappingTurtle():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'glass tank'
        self.walking = True
        self.shift = shift

class Mouse():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'glass tank'
        self.walking = True
        self.shift = shift

class Armadillo():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'glass tank'
        self.walking = True
        self.shift = shift


class Mallard():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'pond'
        self.swimming = True
        self.walking = True
        self.shift = shift

class Goldfish():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'pond'
        self.swimming = True
        self.shift = shift


class Frog():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'pond'
        self.swimming = True
        self.shift = shift


class Trout():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'pond'
        self.swimming = True
        self.shift = shift


class Crawfish():
    def __init__(self, name, species, shift):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'pond'
        self.swimming = True
        self.shift = shift

roberto = Llama("Roberto", "alpaca", "midday")
print(f'{roberto.name} the {roberto.species} is available to pet during the {roberto.shift} shift.')
# prints Roberto the alpaca is available to pet during the midday shift.