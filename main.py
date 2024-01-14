import pygame

from src import creature

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_size = pygame.Vector2(50, 50)

running = True


# initialize a creature
c = creature.Creature()

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # re-draw the background each frame so we don't get previous frames showing up
  screen.fill("black")
  
  # draw the player on the screen
  pygame.draw.rect(screen, (255, 255, 255), (player_pos.x, player_pos.y, player_size.x, player_size.y))

  # make the player move:
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
    player_pos.y -= 300 * dt
  if keys[pygame.K_s]:
    player_pos.y += 300 * dt
  if keys[pygame.K_a]:
    player_pos.x -= 300 * dt
  if keys[pygame.K_d]:
    player_pos.x += 300 * dt


  # keep player on the screen
  if player_pos.x > screen.get_width() - player_size.x:
    player_pos.x = screen.get_width() - player_size.x
  if player_pos.x < 0:
    player_pos.x = 0
  if player_pos.y > screen.get_height() - player_size.y:
    player_pos.y = screen.get_height() - player_size.y
  if player_pos.y < 0:
    player_pos.y = 0
     
  # update our creatures
  c.update(dt)
  c.draw(screen)

  # this line draws to the window
  pygame.display.flip()

  # limits FPS to 60
  # dt is delta time in seconds since last frame, used for framerate-
  # independent physics.
  dt = clock.tick(60) / 1000


print("Quitting...")
pygame.quit()