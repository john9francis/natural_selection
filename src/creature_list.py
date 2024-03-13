# Class that contains the creature list as well as initialization
# settings and repopulating functions

import pygame
import random

from src import creature
from src import save_manager
from src import creature_killer

class CreatureList:

  def __init__(self, creature_amount, screen) -> None:
    self._save_manager = save_manager.SaveManager()
    self._creature_amount = creature_amount
    self._screen = screen

    self._creature_list = []
    self.dt = 0

    self.rand = random.Random()
    pass


  def initialize_creature_list(self):
    '''
    First, tries to load creatures from file
    and loads any remaining creatures by duplicating
    the genomes of creatures that survived last run.
    If no files found, creates creatures randomly.
    '''
    try:
      self._save_manager.load()

      creature_dict = self._save_manager.get_creature_dict()

      if len(creature_dict) > 0:
        print("loading from file")
        self._creature_list = self.create_creatures_from_dict(creature_dict)
      else:
        raise FileNotFoundError

    except FileNotFoundError:
      print("Creating random creatures")
      self._creature_list = self.create_random_creatures(self._creature_amount)
      pass


    if len(self._creature_list) < self._creature_amount:
      print("Repopulating from survivors")
      repopulated_creatures = self.repopulate_creatures()
      self._creature_list.extend(repopulated_creatures)
      pass


    # mutate some
    self.mutate_creatures()


  def update(self, dt):
    '''
    Updates and draws all the creatures
    '''
    for c in self._creature_list:
      c.update(self.dt)
      c.draw(self._screen)



  def save_and_reset(self):
    '''
    Saves all creatures to a file
    '''
    # save the all the creature's genomes to save file
    self._save_manager.populate_creature_dict(self._creature_list)

    # make sure to clear out old info before saving
    self._save_manager.clear_file()
    self._save_manager.populate_creature_dict(self._creature_list)
    self._save_manager.save()

    # print survival rate
    print(
      f"{len(self._creature_list)} creatures survived this run, a {len(self._creature_list) / self._creature_amount * 100} % survival rate.")




  # Specific creature generation functions
  # ________________________________________________

  def mutate_creatures(self, how_many=5):
    # Mutate a few
    for _ in range(how_many):
      self.rand.choice(self._creature_list).mutate()


  def kill_some_creatures(self):
    '''
    Temporary function to kill some creatures off
    '''
    # kill the weak creatures
    killer = creature_killer.CreatureKiller(self._screen)
    self._creature_list = killer.kill_creatures_on_right(self._creature_list)


  
  def create_creatures_from_dict(self, _creature_dict) -> list:
    new_creature_list = []

    for key in _creature_dict:
      c = creature.Creature(
        pygame.Vector2(
          self.rand.uniform(0,1) * self._screen.get_width(),
          self.rand.uniform(0,1) * self._screen.get_height()
        ),
        self._screen,
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


  def create_random_creatures(self, _creature_amount) -> list:
    new_creature_list = []

    for _ in range(_creature_amount):
      c = creature.Creature(
        pygame.Vector2(
          self.rand.uniform(0,1) * self._screen.get_width(),
          self.rand.uniform(0,1) * self._screen.get_height()
        ),
        self._screen,
      )

      c.set_random_genomes()

      new_creature_list.append(c)

    return new_creature_list
  

  def runtime_repopulate_creatures(self):
    new_creatures = self.repopulate_creatures()

    # very small chance to mutate a creature
    for i in range(len(new_creatures)):
      value = self.rand.random()
      if value > .7:
        new_creatures[i].mutate()

    # add the new ones onto the total creatures
    self._creature_list.extend(new_creatures)
  

  def repopulate_creatures(self, creature_amount=0) -> list:
    '''
    Repopulates creatures by duplicating genomes from the
    already existing creatures. default behavior is to 
    repopulate the set creature amount - the length of the creature list
    thus making the creature list's new length be the set creature amount. 
    '''
    if creature_amount == 0:
      creature_amount = self._creature_amount - len(self._creature_list)


    new_creatures = []

    for _ in range(creature_amount):
      c = creature.Creature(
        pygame.Vector2(
          self.rand.uniform(0,1) * self._screen.get_width(),
          self.rand.uniform(0,1) * self._screen.get_height()
        ),
        self._screen,
      )

      parent = self.rand.choice(self._creature_list)
      c.set_genomes(parent.get_genomes())

      new_creatures.append(c)

    return new_creatures