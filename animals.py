#Critters and Croquettes

from datetime import date

class Donkey():
    def __init__(self, name, species, shift, chip_num):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.area = 'petting area'
        self.walking = True
        self.shift = shift
        self.__chip_number = chip_num

    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self, number):
        pass

    def __repr__(self):
        return f"{self.name} is a {self.species}"

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

