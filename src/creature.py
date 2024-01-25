import pygame
import random

from . import neural_net

class Creature:

  pos = pygame.Vector2(500, 50)
  size = pygame.Vector2(5, 5)
  speed = 100

  nn = None

  def __init__(self, start_pos):
    self.pos = start_pos
  
    self.nn = neural_net.NeuralNet()
    self.nn.create_neural_net(self)
    

  def update(self, dt):
    self.nn.update(dt)


  def draw(self, screen):
    # draw basic white rect
    pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))

  def mutate(self):
    pass