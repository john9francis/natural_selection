import pygame
from src import creature_list as cl
from src import player as p


def main():

  # initialization settings:
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()

  dt = 0.
  running = True

  # init creature list
  c_list = cl.CreatureList(500, screen)


  # initialize a player
  player = p.Player(screen)

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

    # update player
    player.update(dt)
    player.draw()


    # kill any creatures the player is touching
    # NOTE: this is not good to affect the creature list
    # directly, but it was an easy way to do it

    for c in c_list._creature_list:
      if player.check_if_in_hitbox(c.pos):
        c.remove_self_from_list(c_list._creature_list)

    # repopulate for all the creatures that were eaten
    c_list.runtime_repopulate_creatures()

    # update the screen
    pygame.display.flip()

    # end game loop


  print("Quitting...")
  pygame.quit()



if __name__ == "__main__":
  main()