# A base creature that the user derives from 

import pygame
import random
import copy

from . import base_neural_net

class BaseCreature:

  def __init__(self, genome_amount=2):
    '''
    Genome amount is how many neural connections
    the creature has. The more genomes the more "smart" 
    the creature is (theoretically)
    '''
    self.genome_amount = genome_amount

    self.genome = []
    self.nn = base_neural_net.BaseNeuralNet(self)

    self.rand = random.Random()

    # this line can possibly be replaced by 
    # "self.set_random_genomes()"
    for _ in range(self.genome_amount):
      g1 = []
      g1.append(self.rand.random())
      g1.append(self.rand.random())
      g1.append(self.rand.random())
      self.genome.append(g1)

    
  def add_input_funcs(self, func_list:list):
    '''
    Takes in references to functions that recieve
    Input, and adds them to the neural net

    NOTE: INPUT FUNCS MUST RETURN A BOOL
    '''
    self.nn.add_input_functions(func_list)

  def add_output_funcs(self, func_list:list):
    '''
    Takes in references to functions that make
    the creature do things, and adds them to the
    neural net.
    '''
    self.nn.add_output_functions(func_list)

  def update(self, dt):
    self.nn.update(dt)


  def draw(self, screen):
    raise NotImplementedError



  def mutate(self):
    # change one random value in the genome
    indx1 = self.rand.randint(0, len(self.genome)-1)
    indx2 = self.rand.randint(0,2)
    self.genome[indx1][indx2] = self.rand.uniform(0,1)
    pass


  def remove_self_from_list(self, list_to_leave: list):
    if self in list_to_leave:
      list_to_leave.remove(self)
    pass



  def set_random_genomes(self):
    # Create a new random list for each creature
    self.genome = [[self.rand.uniform(0, 1) for _ in range(3)] for _ in range(self.genome_amount)]



  def set_genomes(self, genome_list):
    if len(genome_list) == self.genome_amount:
      self.genome = genome_list
    else:
      print("Set genomes error in creature.py. wrong length of genome list.")
      print(f"tried to set {len(genome_list)} into a {self.genome_amount} size list.")


  def get_genomes(self):
    genome_copy = copy.deepcopy(self.genome)
    return genome_copy
  