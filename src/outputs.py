from base_input_output import Output

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