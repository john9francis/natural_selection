# This will find classes and add them to a list. 

import inspect
import importlib.util

def get_classes_from_file(file_path):
    classes = []

    # Load the module from the file
    spec = importlib.util.spec_from_file_location("module_from_file", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Iterate through members of the module
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            classes.append(obj)

    return classes

# Example usage
file_path = "src/test_classes_functions.py"
class_list = get_classes_from_file(file_path)

# Now class_list contains all the classes defined in the specified file
print(class_list)
for i in class_list:
  i.print_stuff()


