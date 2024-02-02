import pygame
import random

from src import creature
from src import save_manager



def main():
  # initialization settings:
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()

  # init save manager
  sm = save_manager.SaveManager()

  dt = 0
  running = True

  # set how many creatures we want to test
  creature_amount = 10

  """
  TO DO: OPTIMIZE MAIN FILE
  
  --start--
  1. set creature amount
  2. check if json exists and is not empty
    a. if json is empty, create creature amount creatures with random genomes
    b. if json is not empty, create creatures based on the genomes in the json
      i. if there are more creatures than json, generate the remaining ones random
      ii. if there are less creatures than json, just do the first json ones 
  3. mutate some creatures
  
  --end--
  1. kill some creatures based on a condition
  2. delete json file or clear it
  3. put genomes of surviving creatures in the json
  """



  # init a genome dict to load our json data to
  genome_dict = {}


  try:
    # load from json file
    sm.load()

    # extract the data
    genome_dict = sm.get_creature_dict()
    
    # of the file was empty, throw the error so we can move on
    if len(genome_dict) == 0:
      raise FileNotFoundError

  except FileNotFoundError:

    # If file was empty, fill the genome dict with random data
    for i in range(creature_amount):

      # genome list to hold the genome
      genome_list = []

      # append as many instructions as the creatures take
      for j in range(creature.Creature.static_get_genome_amount()):
        genome_list.append([random.uniform(0,1) for _ in range(3)])

      # set it to the creature dict
      genome_dict[i] = genome_list




  # initialize our creatures
  creature_list = []

  for i in range(creature_amount):

    # give creature a random position
    c = creature.Creature(
      pygame.Vector2(
        random.random() * screen.get_width(), 
        random.random() * screen.get_height()),
      )

    # set the screen so they don't fall off of it
    # NOTE: add to constructor
    c.set_screen(screen)

    # add them to creature list
    creature_list.append(c)

    # set their genome to the genome dict unless
    # their isn't any more, in which case they
    # inherit from one of the surviving creatures
    try:
      new_genome = genome_dict[i]
    except KeyError:
      new_genome = random.choice(creature_list).get_genomes()

    # set the genome to the creature
    c.set_genomes(new_genome)

    # finally, finalize the genome to send it to the nn
    c.finalize_genome()


    # lastly, mutate at random
    #if random.random() < .05:
    #  c.mutate()




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


  # kill all creatures to the right of the screen
  """
  index = 0
  while index < len(creature_list):
    if creature_list[index].pos.x > screen.get_width() / 2:
      # creature on the right, kill them
      creature_list.pop(index)
    else:
      index += 1

  """


  # save the all the creature's genomes to save file
  sm.populate_creature_dict(creature_list)
  print(creature_list)
  print(sm.get_creature_dict())

  # make sure to clear out old info before saving
  sm.clear_file()
  sm.save()

  # print survival rate
  print(f"{len(creature_list)} creatures survived this run, a {len(creature_list) / creature_amount * 100} % survival rate.")


  print("Quitting...")
  pygame.quit()




if __name__ == "__main__":
  main()