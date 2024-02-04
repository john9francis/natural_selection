import pygame
import random
import math

class NeuralNet:
  creature = None
  genomes = []

  
  # =======================================================================
  # Inputs functions
  # =======================================================================

  start_time = 0
  start_time = pygame.time.get_ticks()
  time_interval = 200

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
    
  
  inputs = []

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


  outputs = []


  # =================================================================


  def __init__(self, creature) -> None:
    self.creature = creature

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
    
    # randomize the list to remove bias
    # NOTE: This is actually wrong... because it would ruin the genome
    #random.shuffle(self.inputs)
    #random.shuffle(self.outputs)
    # There needs to be a different way to remove the bias

    pass



  def update(self, dt):
    # get a random genome
    g = random.choice(self.creature.get_genomes())

    # only continue if the weight is bigger than our random val
    if g[2] > random.uniform(0,1):

      # get the indices by turning the floats into ints.
      input_indx = round(g[0] * len(self.inputs) - 1)
      output_indx = round(g[1] * len(self.outputs) - 1)


      # if the input func returns true, do the output
      if (self.inputs[input_indx]()):
        self.outputs[output_indx]()

