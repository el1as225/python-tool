import os
import importlib.util
import sys

MODULES_DIR = 'modules'
loaded_modules = {}

def load_modules(modules_dir):
    global loaded_modules
    for module_name in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, module_name)
        if os.path.isdir(module_path) and '__init__.py' in os.listdir(module_path):
            try:
                # Dynamisch den Modulpfad erstellen
                spec = importlib.util.spec_from_file_location(module_name, os.path.join(module_path, '__init__.py'))
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                loaded_modules[module_name] = module
                print(f'Module {module_name} loaded successfully.')
            except Exception as e:
                print(f'Failed to load module {module_name}: {e}')
    return loaded_modules

def get_module(module_name):
    return loaded_modules.get(module_name, None)

def list_modules():
    return list(loaded_modules.keys())

def load_main_function(module_name):
    module_dir = os.path.join(MODULES_DIR, module_name)
    main_path = os.path.join(module_dir, '__main__.py')
    if os.path.isfile(main_path):
        try:
            spec = importlib.util.spec_from_file_location(f"{module_name}.__main__", main_path)
            main_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(main_module)
            return getattr(main_module, 'main', None)
        except Exception as e:
            print(f"Error loading main function for module {module_name}: {e}")
            return None
    return None