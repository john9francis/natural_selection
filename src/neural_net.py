import pygame
import random


class NeuralNet:

  def __init__(self, creature) -> None:
    self.rand = random.Random()

    self.creature = creature
    self.genomes = []

    # init our inputs and outputs lists
    self.inputs = [
      self.periodic_activation
      ]
    
    self.outputs = [
      self.move_down,
      self.move_up,
      self.move_left,
      self.move_right
      ]
    
    self.start_time = 0
    self.time_interval = 200
  
  # =======================================================================
  # Inputs functions
  # =======================================================================

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

  # =================================================================







  def update(self, dt):
    # get a random genome
    g = self.rand.choice(self.creature.get_genomes())

    # only continue if the weight is bigger than our random val
    if g[2] > self.rand.uniform(0,1):

      # get the indices by turning the floats into ints.
      input_indx = round(g[0] * len(self.inputs) - 1)
      output_indx = round(g[1] * len(self.outputs) - 1)


      # if the input func returns true, do the output
      if (self.inputs[input_indx]()):
        self.outputs[output_indx]()

