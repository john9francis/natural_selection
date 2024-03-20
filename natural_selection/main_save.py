import pygame
from src import creature_list as cl
from src import player as p

from src import save_manager as sm
from src import creature_killer as ck


def main():

  # initialization settings:
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()

  dt = 0.
  running = True

  # init creature list
  c_list = cl.CreatureList(500, screen)

  # init other things
  saver = sm.SaveManager()
  killer = ck.CreatureKiller(screen)

  while running:
    # allow to quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # re-draw the background each frame so we don't get previous frames showing up
    screen.fill("black")

    dt = clock.tick(60) / 1000.0

    # update our creatures
    c_list.update(dt)

    # update the screen
    pygame.display.flip()

    # end game loop

  # Kill some creatures
  c_list._creature_list = killer.kill_creatures_on_left(c_list._creature_list)

  # save the surviving ones to a json
  saver.save_creatures(c_list._creature_list)


  print("Quitting...")
  pygame.quit()



if __name__ == "__main__":
  main()