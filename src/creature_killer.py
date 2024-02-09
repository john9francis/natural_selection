class CreatureKiller:
  screen = None

  def __init__(self, screen) -> None:
    self.screen = screen
    pass


  def kill_creatures_on_left(self, creature_list):
    '''
    Takes in a creature list, pops the ones on the left of the 
    screen, and returns the updated list
    '''
    index = 0
    while index < len(creature_list):
      if creature_list[index].pos.x < self.screen.get_width() / 2:
        creature_list.pop(index)
      else:
        index += 1

    return creature_list
  

  def kill_creatures_on_right(self, creature_list):
    '''
    Takes in a creature list, pops the ones on the right of the 
    screen, and returns the updated list
    '''
    index = 0
    while index < len(creature_list):
      if creature_list[index].pos.x > self.screen.get_width() / 2:
        creature_list.pop(index)
      else:
        index += 1

    return creature_list
  

  def kill_creatures_on_top(self, creature_list):
    '''
    Takes in a creature list, pops the ones on the upper half of the 
    screen, and returns the updated list
    '''
    index = 0
    while index < len(creature_list):
      if creature_list[index].pos.y < self.screen.get_height() / 2:
        creature_list.pop(index)
      else:
        index += 1

    return creature_list
  

  def kill_creatures_on_bottom(self, creature_list):
    '''
    Takes in a creature list, pops the ones on the bottom half of the 
    screen, and returns the updated list
    '''
    index = 0
    while index < len(creature_list):
      if creature_list[index].pos.y > self.screen.get_height() / 2:
        creature_list.pop(index)
      else:
        index += 1

    return creature_list
