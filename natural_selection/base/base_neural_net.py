# A base neural network to be used for the base creature.
# Has no default input or output functions.

import pygame
import random


class BaseNeuralNet:

  def __init__(self, creature) -> None:
    self.rand = random.Random()

    self.creature = creature
    self.genomes = []

    # init our inputs and outputs lists
    self.inputs = []
    self.outputs = []



  def add_input_functions(self, func_list:list):
    self.inputs.extend(func_list)


  def add_output_functions(self, func_list:list):
    self.outputs.extend(func_list)


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

