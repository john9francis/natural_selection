import pygame
from base_input_output import Input

class Periodic_Activation(Input):
  start_time = None
  time_interval = None

  def __init__(self, creature) -> None:
    super().__init__(creature)

    self.start_time = pygame.time.get_ticks()
    self.time_interval = 200

  def check_input(self) -> bool:
    # Calculate elapsed time
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - self.start_time

    # Check if 2 seconds have passed
    if elapsed_time >= self.time_interval:
      self.start_time = current_time
      return True
    else:
      return False