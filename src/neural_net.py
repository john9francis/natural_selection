from . import genome
import pygame
import random
from . import class_finder

class NeuralNet:
  creature = None

  genomes = []

  input_output_dict = {}

  input_filepath = 'src/inputs.py'
  output_filepath = 'src/outputs.py'

  # instructions dict format:
  # input_function: [output_function, weight]
  instructions = {}

  start_time = pygame.time.get_ticks()
  time_interval = 200

  def __init__(self) -> None:
    pass


  def add_genome(self, genome):
    self.genomes.append(genome)

  def get_genome_list(self):
    return self.genomes
  
  def set_genome_list(self, genome_list):
    self.genomes = genome_list

  def update(self, dt):

    rand_val = random.random()
    

    # get a random genome
    genome_object = random.choice(self.genomes)
    g = genome_object.get_genome()

    # only continue if the weight is bigger than our random val
    if g[2] > rand_val:

      # do the input and it's output function
      input_indx = round(g[0] * (len(self.inputs) - 1))
      output_indx = round(g[1] * (len(self.outputs) - 1))


      if (self.inputs[input_indx](self)):
        self.outputs[output_indx](self)


    

    '''
    for key in self.input_output_dict:

      # check if one is true, and if so, do what it's connected to.
      if key.check_input():

        # check if a random float is less than weight
        weight = self.input_output_dict[key][1]
        if random.random() < weight:
          self.input_output_dict[key][0].trigger_output()
    '''



  def create_neural_net(self, creature):
    ''' initializer for this neural net.'''
    self.creature = creature

    # first, get all our maps populated
    #self.populate_maps()

    # then, initialize every class with the creature
    #self.initialize_inputs_outputs(creature)
    pass

    

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

      # get the weight
      weight = g.get_genome()[2]

      # Now add these to the dict
      self.input_output_dict[self.inputs[input_indx]] = [self.outputs[output_indx], weight]
    pass



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