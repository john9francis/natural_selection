import enum
import json

class SaveManager:
  creature_dict = {}
  path = "runs/"
  filename = path + "run1.json"

  def __init__(self):
    self.creature_dict = {}
    pass

  def populate_creature_dict(self, creature_list):
    for counter, c in enumerate(creature_list):
      self.creature_dict[counter] = c.get_raw_genome_list()


  def get_creature_dict(self):
    return self.creature_dict


  def save(self):
    with open(self.filename, 'w') as json_file:
      json.dump(self.creature_dict, json_file)
    pass

  def load(self):
    with open(self.filename, 'r') as json_file:
      self.creature_dict = json.load(json_file)

    # now we just need to convert all the string keys to int keys
    self.creature_dict = self.convert_string_keys_to_int(self.creature_dict)
    pass

  def convert_string_keys_to_int(self, input_dict):
    # Create a new dictionary with integer keys
    result_dict = {int(key): value for key, value in input_dict.items()}
    return result_dict

