class Attraction:
  def __init__(self, name, description):
      self.attraction_name = name
      self.description = description
      self.animals = list()
  
  @property
  def last_animal_added(self):
    return self.animals[-1]

  def __repr__(self):
    output = self.description + "\n"
    for animal in self.animals:
      output += f"{animal.name} is a {animal.species} that can be found in the {self.attraction_name} \n"
    return output

