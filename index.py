from animals import *
from attractions import Attraction

fred = Donkey( 'fred', 'Donkey', 'Morning', 1234)
george = Donkey( 'george', 'Donkey', 'Morning', 1235)
varmint_village = Attraction("Varmint Village", "cute and fuzzy critters to cuddle")
aviary = Attraction("The Roost", "winged and clawed critters")
varmint_village.animals.append( fred )
varmint_village.animals.append( george )

print(george.chip_number)
george.chip_number = 5678
print(george.chip_number)
