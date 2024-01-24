# The base classes for inputs and outputs

class Input:
  creature = None

  # gets connected to an output function
  def __init__(self, creature) -> None:
    self.creature = creature
    pass

  def check_input(self) -> bool:
    # this is a virtual function.
    # all children need to make this function return a bool.
    raise NotImplementedError("Input child class must impliment 'check_input' method.")


class Output:
  # makes the creature do something
  creature = None

  def __init__(self, creature) -> None:
    self.creature = creature
    pass

  def trigger_output(self):
    raise NotImplementedError("Output children class must implement 'trigger_output' method.")
