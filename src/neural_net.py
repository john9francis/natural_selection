import pygame
import random
import math

class NeuralNet:
  creature = None
  genomes = []

  start_time = pygame.time.get_ticks()
  time_interval = 200


  def __init__(self, creature) -> None:
    self.creature = creature
    pass


  def add_genome(self, genome):
    self.genomes.append(genome)


  def get_genome_list(self):
    return self.genomes
  

  def set_genome_list(self, genome_list):
    self.genomes = genome_list


  def update(self, dt):
    # get a random genome
    genome_object = random.choice(self.genomes)
    g = genome_object.get_genome()

    # only continue if the weight is bigger than our random val
    if g[2] > random.random():

      # get the indices by turning the floats into ints.
      # note: we will randomly go floor or ceil to not be biased
      if random.random() > .5:
        input_indx = math.floor(g[0] * (len(self.inputs) - 1))
      else:
        input_indx = math.ceil(g[0] * (len(self.inputs) - 1))
      if random.random() > .5:
        output_indx = math.floor(g[0] * (len(self.outputs) - 1))
      else:
        output_indx = math.ceil(g[0] * (len(self.outputs) - 1))


      # do the input and it's output function
      if (self.inputs[input_indx](self)):
        self.outputs[output_indx](self)


  # =======================================================================
  # Inputs functions
  # =======================================================================

  start_time = 0

  def periodic_activation(self) -> bool:
    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - self.start_time

    # Check if 2 seconds have passed
    if elapsed_time >= self.time_interval:
      self.start_time = current_time
      return True
    else:
      return False
    
  
  inputs = [periodic_activation]

  # =======================================================================
  # Outputs functions
  # =======================================================================

  def move_left(self):
    self.creature.pos.x -= 10

  def move_right(self):
    self.creature.pos.x += 10

  def move_up(self):
    self.creature.pos.y -= 10

  def move_down(self):
    self.creature.pos.y += 10


  outputs = [move_left, move_right, move_up, move_down]