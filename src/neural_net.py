from . import genome

class NeuralNet:
  inputs = []
  outputs = []
  genomes = []

  def __init__(self) -> None:
    for i in range(10):
      new_g = genome.Genome()
      new_g.mutate()
      self.genomes.append(new_g)

    for g in self.genomes:
      g.print_genome()
    pass


  