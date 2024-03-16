# Creates a base display that takes in creatures and runs.

import pygame

class BaseDisplay():
  def __init__(self) -> None:
    self.c_list = []
    pass


  def add_creatures(self, new_creatures:list):
    '''Adds creatures to the scene'''
    self.c_list.extend(new_creatures)



  def main(self):

    # initialization settings:
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    dt = 0.
    running = True


    while running:
      # allow to quit
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

      # re-draw the background each frame so we don't get previous frames showing up
      screen.fill("black")

      dt = clock.tick(60) / 1000.0

      # update our creatures
      for c in self.c_list:
        c.update(dt)
        c.draw(screen)

      # update the screen
      pygame.display.flip()

      # end game loop


    print("Quitting...")
    pygame.quit()

