import pygame
import random

from . import genome

from . import neural_net

class Creature:
  _screen = None

  pos = pygame.Vector2(500, 50)
  size = pygame.Vector2(5, 5)
  speed = 100

  genome_amount = 10

  nn = None

  def __init__(self, start_pos):
    self.pos = start_pos
  
    self.nn = neural_net.NeuralNet()
    self.nn.create_neural_net(self)
    print("creature initialized")
    

  def update(self, dt):
    self.nn.update(dt)
    self.stay_on_screen()


  def draw(self, screen):
    # draw basic white rect
    pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))

  def mutate(self):
    pass


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
    for i in range(self.genome_amount):
      g = genome.Genome()
      g.set_random_genome()
      self.nn.add_genome(g)
    pass

  def set_genomes(self, genome_list):
    self.nn.set_genome_list(genome_list)

  def get_genomes(self):
    return self.nn.get_genome_list()