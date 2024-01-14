import pygame

class Creature:

  pos = pygame.Vector2(500, 50)
  size = pygame.Vector2(5, 5)
  speed = 100

  start_time = pygame.time.get_ticks()
  time_interval = 200

  instructions = ["LEFT", "PAUSE", "RIGHT", "PAUSE"]
  instr_i = 0

  def __init__(self):
    pass

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

      self.instr_i += 1
      if self.instr_i > len(self.instructions) - 1:
        self.instr_i = 0


  def draw(self, screen):
    # draw basic white rect
    pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))



