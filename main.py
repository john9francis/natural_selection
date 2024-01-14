import pygame
import random

from src import creature
from src import player
from src import save_manager


# initialization settings:
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

dt = 0
running = True

creature_amount = 1000


# initialize our save manager to load from file
sm = save_manager.SaveManager()
creature_instruction_dict = {}
try:
  sm.load()
  creature_instruction_dict = sm.get_creature_dict()
except FileNotFoundError:
  # create new creatures 
  for i in range(creature_amount):
    creature_instruction_dict[i] = ["RIGHT", "LEFT", "PAUSE"]

# initialize our creatures
creature_list = []
for i in range(len(creature_instruction_dict)):
  c = creature.Creature(
    pygame.Vector2(
      random.random() * screen.get_width(), 
      random.random() * screen.get_height()),
      creature_instruction_dict[i]
    )
  # mutate them
  c.mutate()
  creature_list.append(c)


# repopulate using the creatures that survived last time!
remaining = creature_amount - len(creature_list)
for i in range(remaining):
  instructions = random.choice(creature_list).get_instructions()

  c = creature.Creature(
    pygame.Vector2(
      random.random() * screen.get_width(),
      random.random() * screen.get_height()),
  instructions
  )

  c.mutate()
  creature_list.append(c)



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
    # creature on the left, kill them
    creature_list.pop(index)
  else:
    index += 1

# save the creature info
sm.populate_creature_dict(creature_list)
sm.save()
print(f"{len(creature_list)} creatures survived this run.")

print("Quitting...")
pygame.quit()