class Output:
  # makes the creature do something
  creature = None

  def __init__(self, creature) -> None:
    self.creature = creature
    pass

  def trigger_output(self):
    raise NotImplementedError("Output children class must implement 'trigger_output' method.")



class MoveLeft(Output):
  def trigger_output(self):
    self.move_left()

  def move_left(self):
    self.creature.pos -= 10



class MoveRight(Output):
  def trigger_output(self):
    self.move_right()
  
  def move_right(self):
    self.creature.pos += 10