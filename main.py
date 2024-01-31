import pygame
import random

from src import genome
from src import creature
from src import save_manager



def main():
  # initialization settings:
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()

  dt = 0
  running = True

  creature_amount = 5

  # init save manager
  sm = save_manager.SaveManager()
  genome_dict = {}
  try:
    sm.load()
    genome_dict = sm.get_creature_dict()
  except FileNotFoundError:
    # create new creatures 
    for i in range(creature_amount):
      genome_dict[i] = genome.Genome.get_random_genome()



  # initialize our creatures
  creature_list = []
  for i in range(creature_amount):
    c = creature.Creature(
      pygame.Vector2(
        random.random() * screen.get_width(), 
        random.random() * screen.get_height()),
      )

    # set the screen so they don't fall off of it
    c.set_screen(screen)

    # add them to creature list
    creature_list.append(c)

    # set their genome to the genome dict unless
    # their isn't any more, in which case they
    # inherit from one of the surviving creatures
    try:
      new_genome = genome_dict[i]
    except KeyError:
      new_genome = random.choice(creature_list).get_raw_genome_list()

    c.set_raw_genome_list(new_genome)


  while running:
    # allow to quit
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    # re-draw the background each frame so we don't get previous frames showing up
    screen.fill("black")


    # update our creatures
    for thing in creature_list:
      thing.update(dt)
      thing.draw(screen)


    # update the screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000


  # kill all creatures to the left of the screen
  index = 0
  while index < len(creature_list):
    if creature_list[index].pos.x > screen.get_width() / 2:
      # creature on the right, kill them
      creature_list.pop(index)
    else:
      index += 1


  # save the all the creature's genomes to save file
  sm.populate_creature_dict(creature_list)
  sm.save()
  print(f"{len(creature_list)} creatures survived this run, a {len(creature_list) / creature_amount * 100} % survival rate.")


  print("Quitting...")
  pygame.quit()




if __name__ == "__main__":
  main()