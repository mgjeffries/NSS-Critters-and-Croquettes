class Attraction:
  def __init__(self, name, description):
      self.attraction_name = name
      self.description = description
      self.animals = list()

  def __repr__(self):
    output = self.description + "\n"
    for animal in self.animals:
      output += f"{animal.name} is a {animal.species} that can be found in the {self.attraction_name} \n"
    return output

