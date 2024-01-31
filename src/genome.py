import random

class Genome:
  # The genome is the following format:
  # 0: input address
  # 1: output address
  # 2: strength of connection between them 
  genome = None


  def __init__(self) -> None:
    self.genome = [0., 0., 1.]
    pass

  def get_genome(self):
    return self.genome

  def set_genome(self, new_genome):
    self.genome = new_genome
    pass

  def set_random_genome(self):
    self.genome = [random.random(), random.random(), random.random()]

  def print_genome(self):
    print(self.genome)

  def mutate(self):
    # randomly changes one of the floats
    indx = random.randint(0, len(self.genome)-1)
    self.genome[indx] = random.random()
    pass

  @staticmethod
  def get_random_genome():
    '''Gets a random genome without having to initialize the class'''
    return [random.uniform(0.0, 1.0) for _ in range(3)]