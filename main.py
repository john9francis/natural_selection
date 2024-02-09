import pygame
from src import creature_list
from src import player as p


def main():

  # initialization settings:
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()

  dt = 0
  running = True

  # init creature list
  c_list = creature_list.CreatureList(10, screen)
  c_list.initialize_creature_list()


  # initialize a player
  player = p.Player(screen)


  while running:
    # allow to quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # re-draw the background each frame so we don't get previous frames showing up
    screen.fill("black")


    # update our creatures
    c_list.update(dt)

    # update player
    player.update(dt)
    player.draw()


    # kill any creatures the player is touching
    # NOTE: this is not good to affect the creature list
    # directly, but it was an easy way to do it

    repopulate = False

    #for c in c_list._creature_list:
    #  if player.check_if_in_hitbox(c.pos):
    #    c.remove_self_from_list(c_list._creature_list)
    #    repopulate = True

    # repopulate any creatures that may have died
    if repopulate:
      c_list.runtime_repopulate_creatures()

    # update the screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

    # end game loop


  # debug print
  #for c in c_list._creature_list:
  #  print(c.get_genomes())

  # kill weak creatures and reset
  c_list.kill_some_creatures()
  #c_list.save_and_reset()
  

  print("Quitting...")
  pygame.quit()



if __name__ == "__main__":
  main()