from . import genome

class NeuralNet:
  inputs = []
  outputs = []
  genomes = []

  def __init__(self) -> None:
    self.genomes = [genome.Genome() for i in range(10)]
    for g in self.genomes:
      g.mutate
      g.print_genome()
    pass


  