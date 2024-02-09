import pygame
from src import creature_list


def main():

  # initialization settings:
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()

  dt = 0
  running = True

  # init creature list
  c_list = creature_list.CreatureList(100, screen)
  c_list.initialize_creature_list()


  while running:
    # allow to quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # re-draw the background each frame so we don't get previous frames showing up
    screen.fill("black")


    # update our creatures
    c_list.update(dt)


    # update the screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

    # end game loop


  # kill weak creatures and reset
  c_list.kill_some_creatures()
  c_list.save_and_reset()
  

  print("Quitting...")
  pygame.quit()



if __name__ == "__main__":
  main()