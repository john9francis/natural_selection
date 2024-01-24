import inspect
import importlib.util

def get_functions_from_file(file_path):
    functions = []

    # Load the module from the file
    spec = importlib.util.spec_from_file_location("module_from_file", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Iterate through members of the module
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            functions.append(obj)

    return functions


def execute_functions_from_file(file_path):
    # Load the module from the file
    spec = importlib.util.spec_from_file_location("module_from_file", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Iterate through members of the module
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            print(f"Executing function: {name}")
            obj()  # Call the function

# Example usage
file_path = "src/test_classes_functions.py"
function_list = get_functions_from_file(file_path)

# Now function_list contains all the functions defined in the specified file
print(function_list)

execute_functions_from_file(file_path)