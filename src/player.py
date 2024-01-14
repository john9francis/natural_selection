import pygame

class Player:

  pos = pygame.Vector2()
  size = pygame.Vector2(50, 50)
  speed = 300
  screen = None

  def __init__(self, _screen):
    self.screen = _screen
    self.pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 2)
    pass

  def update(self, dt):

    # make the players move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
      self.pos.y -= 300 * dt
    if keys[pygame.K_s]:
      self.pos.y += 300 * dt
    if keys[pygame.K_a]:
      self.pos.x -= 300 * dt
    if keys[pygame.K_d]:
      self.pos.x += 300 * dt

    # keep player on the screen
    if self.pos.x > self.screen.get_width() - self.size.x:
      self.pos.x = self.screen.get_width() - self.size.x
    if self.pos.x < 0:
      self.pos.x = 0
    if self.pos.y > self.screen.get_height() - self.size.y:
      self.pos.y = self.screen.get_height() - self.size.y
    if self.pos.y < 0:
      self.pos.y = 0


  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))


