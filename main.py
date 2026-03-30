import sys
import importlib

def main(args):
    """
    Args example: ["module","submodule","upsert"]
    - folder_name = "module"
    - sub_folder  = "submodule"
    - operation   = "upsert"
    """
    folder_name, sub_folder, operation = args

    # Build the module path dynamically
    module_path = f"{folder_name}.{sub_folder}.{operation}"

    try:
        # Dynamically import the module
        mod = importlib.import_module(module_path)

        # Call a function inside upsert.py, e.g. first_query()
        if hasattr(mod, "first_query"):
            query = mod.first_query()
            print("Generated SQL:")
            print(query)
        else:
            print(f"No function 'first_query' found in {module_path}")

    except ModuleNotFoundError as e:
        print(f"Could not import {module_path}: {e}")

if __name__ == "__main__":
    # Databricks passes job parameters as sys.argv[1:]
    main(sys.argv[1:])
