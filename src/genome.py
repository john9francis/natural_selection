class Genome:
  # The genome is the following format:
  # 0: input address
  # 1: output address
  # 2: strength of connection between them 
  genome = [0., 0., 0.]


  def __init__(self) -> None:
    pass

  def get_genome(self):
    return self.genome

  def set_genome(self, new_genome):
    genome = new_genome
    pass

  def print_genome(self):
    print(self.genome)

  def mutate(self):
    pass