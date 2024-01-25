# NOTE: Everything in this file should be a child class of Output.

from src import base_input_output

class MoveLeft(base_input_output.Output):
  def trigger_output(self):
    self.creature.pos.x -= 10

class MoveRight(base_input_output.Output):
  def trigger_output(self):
    self.creature.pos.x += 10

class MoveUp(base_input_output.Output):
  def trigger_output(self):
    self.creature.pos.y -= 10

class MoveDown(base_input_output.Output):
  def trigger_output(self):
    self.creature.pos.y += 10
