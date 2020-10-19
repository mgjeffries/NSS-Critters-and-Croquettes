from animals import *
from attractions import Attraction

fred = Donkey( 'fred', 'Donkey', 'Morning')
george = Donkey( 'george', 'Donkey', 'Morning')
varmint_village = Attraction("Varmint Village", "cute and fuzzy critters to cuddle")
aviary = Attraction("The Roost", "winged and clawed critters")
varmint_village.animals.append( fred )
varmint_village.animals.append( george )

print(varmint_village)