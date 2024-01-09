import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_size = pygame.Vector2(50, 50)

running = True

screen.fill("black")

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  
  # draw the player on the screen
  pygame.draw.rect(screen, (255, 255, 255), (player_pos.x, player_pos.y, player_size.x, player_size.y))


  # this line draws to the window
  pygame.display.flip()


print("Quitting...")
pygame.quit()