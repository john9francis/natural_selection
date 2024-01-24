from . import genome
import pygame

class NeuralNet:
  inputs = []
  outputs = []
  genomes = []

  instructions = {}

  start_time = pygame.time.get_ticks()
  time_interval = 200

  def __init__(self) -> None:
    for i in range(10):
      new_g = genome.Genome()
      new_g.mutate()
      self.genomes.append(new_g)

      self.populate_maps()

      # now link up each input to each output based on genomes



  def update(self, dt):
    for i in self.inputs:
      # check if one is true, and if so, do what it's connected to.
      pass
    pass


  # INPUTS AND OUTPUTS ================================================ 

  def move_right(self, creature):
    creature.pos.x += 100

  def move_left(self, creature):
    creature.pos.x -= 100

  def periodic_activation(self, creature) -> bool:
    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - self.start_time

    # Check if 2 seconds have passed
    if elapsed_time >= self.time_interval:
      self.start_time = current_time
      return True
    else:
      return False


  def populate_maps(self):
    # populate input map
    self.inputs.append(self.periodic_activation)
    # populate output map
    self.outputs.append(self.move_right)
    self.outputs.append(self.move_left)
  