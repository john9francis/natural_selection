from . import genome
import pygame
from . import class_finder

class NeuralNet:
  inputs = []
  outputs = []
  genomes = []

  input_output_dict = {}

  input_filepath = 'src/inputs.py'
  output_filepath = 'src/outputs.py'

  instructions = {}

  start_time = pygame.time.get_ticks()
  time_interval = 200

  def __init__(self) -> None:
    for i in range(10):

      # get some random genomes
      # NOTE: Later these will be loaded from a JSON
      new_g = genome.Genome()
      new_g.mutate()
      self.genomes.append(new_g)



  def update(self, dt):
    for key in self.input_output_dict:
      # check if one is true, and if so, do what it's connected to.
      if key.check_input():
        self.input_output_dict[key].trigger_output()



  def create_neural_net(self, creature):
    ''' initializer for this neural net.'''
    # first, get all our maps populated
    self.populate_maps()

    # then, initialize every input
    self.initialize_inputs_outputs(creature)

    # finially, populate the dict.
    self.populate_input_output_dict()
    

  def initialize_inputs_outputs(self, creature):
    new_input_list = []
    for input in self.inputs:
      new_input_list.append(input(creature))

    new_output_list = []
    for output in self.outputs:
      new_output_list.append(output(creature))

    self.inputs = new_input_list
    self.outputs = new_output_list


  def populate_maps(self):
    # put the corresponding classes in their maps.
    self.inputs = class_finder.get_classes_from_file(self.input_filepath)
    self.outputs = class_finder.get_classes_from_file(self.output_filepath)
    pass

  def populate_input_output_dict(self):
    # based on the genomes, link up inputs to outputs. 
    # NOTE: For now I am neglecting the strength factor, I will code it in later.
    for g in self.genomes:

      # get the input relative to the input list
      input = len(self.inputs) * g.get_genome()[0]

      # turn input into an int, it is now an index in the input list
      input_indx = int(round(input)) - 1

      # same with output
      output = len(self.outputs) * g.get_genome()[1]
      output_indx = int(round(output)) - 1

      # Now add these to the dict
      for i in range(len(self.inputs)):
        print(i)
      self.input_output_dict[self.inputs[input_indx]] = self.outputs[output_indx]
    pass