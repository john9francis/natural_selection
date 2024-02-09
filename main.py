import pygame
import random

from src import creature
from src import save_manager
from src import creature_killer





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
        screen,
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
        screen,
      )

      c.set_genomes([
        [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)], 
        [random.uniform(0,1), random.uniform(0,1), random.uniform(0,1)], 
        ])

      new_creature_list.append(c)

    return new_creature_list
  

  def repopulate_creatures(_creature_amount) -> list:

    new_creatures = []

    for _ in range(_creature_amount):
      c = creature.Creature(
        pygame.Vector2(
          random.uniform(0,1) * screen.get_width(),
          random.uniform(0,1) * screen.get_height()
        ),
        screen,
      )

      parent = random.choice(creature_list)
      c.set_genomes(parent.get_genomes())

      new_creatures.append(c)

    return new_creatures
  

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

  # initialize creature list
  creature_list = []

  try:
    sm.load()

    creature_dict = sm.get_creature_dict()

    if len(creature_dict) > 0:
      print("loading from file")
      creature_list = create_creatures_from_dict(creature_dict)
    else:
      raise FileNotFoundError

  except FileNotFoundError:
    print("Creating random creatures")
    creature_list = create_random_creatures(creature_amount)
    pass


  if len(creature_list) < creature_amount:
    print("Repopulating from survivors")
    repopulated_creatures = repopulate_creatures(creature_amount - len(creature_list))
    creature_list.extend(repopulated_creatures)



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


  # kill the weak creatures
  killer = creature_killer.CreatureKiller(screen)
  creature_list = killer.kill_creatures_on_right(creature_list)

  
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