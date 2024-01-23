import random

class Genome:
  # The genome is the following format:
  # 0: input address
  # 1: output address
  # 2: strength of connection between them 
  genome = None


  def __init__(self) -> None:
    self.genome = [0., 0., 0.]
    pass

  def get_genome(self):
    return self.genome

  def set_genome(self, new_genome):
    genome = new_genome
    pass

  def print_genome(self):
    print(self.genome)

  def mutate(self):
    # simply adds a random float to our genome
    indx = random.randint(0, len(self.genome)-1)
    self.genome[indx] += random.random()
    pass