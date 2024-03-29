from turtle import speed
from natural_selection.base import base_creature
from natural_selection.base import base_display

import pygame

# TODO:
# I want the ability to do the following:
# - be able to inherit from base_creature to create your own creatures
# -- set attributes and input output functions
# - be able to initialize different types of worlds: graphics or no
# -- Graphics doesn't need much
# -- No-Graphics needs a creature killer
# - be able to make my own creature killer


# create a new type of creature and add a bunch to the display
class MyCreature(base_creature.BaseCreature):
  def __init__(self):
    super().__init__()

    self.start_time = 0.
    self.time_interval = self.rand.uniform(100, 500)

    self.pos = pygame.Vector2(self.rand.uniform(100, 500), self.rand.uniform(100, 500))
    self.size= pygame.Vector2(10, 10)

    self.speed = 100

    self.add_input_funcs([self.my_input_func])
    self.add_output_funcs([self.move_left, self.move_right, self.move_down, self.move_up])

    # for staying on the screen
    self.left_bound = 0
    self.top_bound = 0
    self.right_bound = 500
    self.bottom_bound = 500


  def draw(self, screen):
    pygame.draw.rect(screen, (255, 255, 255), (self.pos.x, self.pos.y, self.size.x, self.size.y))
    
  def update(self, dt):
    super().update(dt)

    self.stay_on_screen()


  def stay_on_screen(self):
    if self.pos.x > self.right_bound:
      self.pos.x = self.right_bound
    if self.pos.x < self.left_bound:
      self.pos.x = self.left_bound
    if self.pos.y > self.bottom_bound:
      self.pos.y = self.bottom_bound
    if self.pos.y < self.top_bound:
      self.pos.y = self.top_bound

  def set_bounds(self, screen_width, screen_height):
    self.right_bound = screen_width
    self.bottom_bound = screen_height

  def my_input_func(self) -> bool:
    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - self.start_time

    # Check if time interval has passed
    if elapsed_time >= self.time_interval:
      self.start_time = current_time
      return True
    else:
      return False

  def move_left(self):
    self.pos.x -= self.speed

  def move_right(self):
    self.pos.x += self.speed

  def move_up(self):
    self.pos.y -= self.speed
  
  def move_down(self):
    self.pos.y += self.speed


  
# main
  
def main():
  display = base_display.BaseDisplay()

  c_list = []

  screen_width, screen_height = display.get_screen_bounds()

  for _ in range(10):
    c = MyCreature()
    c.set_bounds(screen_width, screen_height)
    c_list.append(c)
    

  display.add_creatures(c_list)

  display.main()


if __name__ == "__main__":
  main()