import pygame
import random

from src import creature
from src import save_manager





def main():

  # FUNCTIONS
  def create_creatures_from_dict(_creature_dict) -> list:
    new_creature_list = []

    for key in _creature_dict:
      c = creature.Creature(
        pygame.Vector2(
          random.uniform(0,1) * screen.get_width(),
          random.uniform(0,1) * screen.get_height()
        ),
        screen
      )

      # now set the genome to the value of the dict
      genome = _creature_dict[key]
      if len(genome) == c.get_genome_amount():
        c.set_genomes(genome)
      else:
        c.set_random_genomes()
        print("Setting from the save file didn't work")

      new_creature_list.append(c)
    

    return new_creature_list


  def create_random_creatures(_creature_amount) -> list:
    new_creature_list = []

    for _ in range(_creature_amount):
      c = creature.Creature(
        pygame.Vector2(
          random.uniform(0,1) * screen.get_width(),
          random.uniform(0,1) * screen.get_height()
        ),
        screen
      )

      c.set_random_genomes() 

      new_creature_list.append(c)


    # mutate all creatures a bunch of times
    for c in new_creature_list:
      c.mutate()
      c.mutate()
      c.mutate()
    return new_creature_list
  

  # initialization settings:
  pygame.init()
  screen = pygame.display.set_mode((1280, 720))
  clock = pygame.time.Clock()

  # init save manager
  sm = save_manager.SaveManager()

  dt = 0
  running = True

  # set how many creatures we want to test
  creature_amount = 100

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

  creature_list = list()

  try:
    sm.load()

    creature_dict = sm.get_creature_dict()

    if len(creature_dict) > 0:
      creature_list = create_creatures_from_dict(creature_dict)
    else:
      raise FileNotFoundError

  except FileNotFoundError:
    creature_list = create_random_creatures(creature_amount)
    pass


  if len(creature_list) < creature_amount:

    # finish it off by repopulating from the surviving creatures
    left_over = creature_amount - len(creature_list)
    for _ in range(left_over):
      c = creature.Creature(
        pygame.Vector2(
          random.uniform(0,1) * screen.get_width(),
          random.uniform(0,1) * screen.get_height()
        ),
        screen
      )

      parent = random.choice(creature_list)
      c.set_genomes(parent.get_genomes())

      creature_list.append(c)


  # DEBUGGING
  for i in range(min(5, len(creature_list))):
      print(f"Creature {i + 1} Genome: {creature_list[i].get_genomes()}")


  # Mutate a few
  for _ in range(5):
    random.choice(creature_list).mutate()



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
    if creature_list[index].pos.x < screen.get_width() / 2:
      # creature on the right, kill them
      creature_list.pop(index)
    else:
      index += 1

  


  # save the all the creature's genomes to save file
  sm.populate_creature_dict(creature_list)

  # make sure to clear out old info before saving
  sm.clear_file()
  sm.populate_creature_dict(creature_list)
  sm.save()

  # print survival rate
  print(f"{len(creature_list)} creatures survived this run, a {len(creature_list) / creature_amount * 100} % survival rate.")


  print("Quitting...")
  pygame.quit()




if __name__ == "__main__":
  main()