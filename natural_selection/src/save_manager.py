import json

class SaveManager:

  def __init__(self):
    self.creature_dict = {}
    self.path = "runs/"
    self.filename = self.path + "run1.json"
    pass


  def save_creatures(self, creature_list):
    self.populate_creature_dict(creature_list)
    self.clear_file()
    self.save()


  def populate_creature_dict(self, creature_list):
    # first, clear out creature dict
    self.creature_dict.clear()

    # then populate with new data
    for counter, c in enumerate(creature_list):
      self.creature_dict[counter] = c.get_genomes()


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

  def clear_file(self):
    with open(self.filename, 'w') as json_file:
      json.dump({}, json_file)
    pass

  def convert_string_keys_to_int(self, input_dict):
    # Create a new dictionary with integer keys
    result_dict = {int(key): value for key, value in input_dict.items()}
    return result_dict




# test
if __name__ == "__main__":
  with open("runs/run1.json", 'w') as json_file:
    json.dump({}, json_file)