import pygame
import random

class Creature:

  pos = pygame.Vector2(500, 50)
  size = pygame.Vector2(5, 5)
  speed = 100

  start_time = pygame.time.get_ticks()
  time_interval = 200

  instructions = ["LEFT", "PAUSE", "RIGHT"]
  instr_i = 0

  def __init__(self, start_pos, instruction_list=None):
    self.pos = start_pos
    if instruction_list != None:
      self.instructions = instruction_list
    

  def update(self, dt):
    if self.instructions[self.instr_i] == "LEFT":
      self.pos.x -= self.speed * dt
      # move left
      pass
    if self.instructions[self.instr_i] == "RIGHT":
      self.pos.x += self.speed * dt
      # move right
      pass
    if self.instructions[self.instr_i] == "PAUSE":
      # pause
      pass

    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - self.start_time

    # Check if 2 seconds have passed
    if elapsed_time >= self.time_interval:
      self.start_time = current_time

      self.instr_i = random.randint(0, len(self.instructions) - 1)


  def draw(self, screen):
    # draw basic white rect
    pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))


  def get_instructions(self):
    return self.instructions

  def set_instructions(self, ins):
    self.instructions = ins

  def mutate(self):
    choice = random.random()
    if choice > .3:
      # duplicate a random instruction
      self.instructions.append(random.choice(self.instructions))
    elif .3 >= choice > .7:
      # remove a random instruction
      self.instructions.pop(random.randint(0, len(self.instruction_list) - 1))