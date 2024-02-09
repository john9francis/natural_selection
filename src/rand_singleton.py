# a singleton that keeps track of
# random variables so they are unique
# during runtime

import random

class RandSingleton:
  _instance = None
  _random = None


  def __new__(cls):
    if cls._instance is None:
      cls._instance = super(RandSingleton, cls).__new__(cls)
      cls._instance._random = random.Random()
    return cls._instance
  