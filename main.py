import pygame

from src import creature
from src import player

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

dt = 0
running = True


# initialize a creature
creature_list = []

c = creature.Creature()
creature_list.append(c)

p = player.Player(screen)
creature_list.append(p)


while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # re-draw the background each frame so we don't get previous frames showing up
  screen.fill("black")

     
  # update our creatures
  for thing in creature_list:
    thing.update(dt)
    thing.draw(screen)


  pygame.display.flip()
  dt = clock.tick(60) / 1000


print("Quitting...")
pygame.quit()