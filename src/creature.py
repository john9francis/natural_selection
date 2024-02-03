import pygame
import random

from . import neural_net

class Creature:
  _screen = None

  pos = pygame.Vector2(500, 50)
  size = pygame.Vector2(5, 5)
  speed = 100

  genome_amount = 2
  genome = []

  nn = None

  def __init__(self, start_pos, screen):
    self.pos = start_pos
    self.nn = neural_net.NeuralNet(self)

    for _ in range(self.genome_amount):
      self.genome.append([0, 0, 0])

    self.set_screen(screen)
    

  def update(self, dt):
    self.nn.update(dt)
    self.stay_on_screen()


  def draw(self, screen):
    # draw basic white rect
    pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))

  def get_genome_amount(self):
    return self.genome_amount


  @staticmethod
  def static_get_genome_amount():
    return Creature.genome_amount


  def mutate(self):
    pass

  def finalize_genome(self):
    self.nn.set_genome_list(self.genome)


  def stay_on_screen(self):
    if self._screen != None:
      if self.pos.x < 0:
        self.pos.x = 0
      if self.pos.x > self._screen.get_width() - self.size.x:
        self.pos.x = self._screen.get_width() - self.size.x
      if self.pos.y < 0:
        self.pos.y = 0
      if self.pos.y > self._screen.get_height() - self.size.y:
        self.pos.y = self._screen.get_height() - self.size.y
    pass


  def set_screen(self, screen):
    self._screen = screen
    pass


  def set_random_genomes(self):
    self.genome.clear()
    for _ in range(self.genome_amount):
      self.genome.append([random.uniform(0,1) for _ in range(3)])

    self.finalize_genome()
    pass


  def set_genomes(self, genome_list):
    if len(genome_list) == self.genome_amount:
      self.genome = genome_list
    else:
      print("Set genomes error in creature.py. wrong length of genome list.")
      print(f"tried to set {len(genome_list)} into a {self.genome_amount} size list.")

    self.finalize_genome()


  def get_genomes(self):
    return self.genome
  
  """
  def get_raw_genome_list(self):
    '''returns just a list of lists so it can be json serializable'''
    raw_list = []
    # get the genome data list
    for g in self.nn.get_genome_list():
      raw_list.append(g.get_genome())

    return raw_list
  

  def set_raw_genome_list(self, raw_g_list):
    ''' populates the genomes off of a plain list of lists'''
    for i in raw_g_list:
      g = genome.Genome()
      g.set_genome(i)

      self.nn.add_genome(g)
  """