import modules  # Ensure modules are loaded
import os

def main():
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Welcome message
    print("\033[1m\033[95mWelcome to Eli's DoS Tool!\033[0m\033[0m\n")

    # Available commands: target, requests, threads, delay, ratelimitdelay, run, exit
    print("  -1. \033[93m[Exit Program]\033[0m\n")
    
    # List all available modules
    available_modules = modules.list_modules()
    if not available_modules:
        print("No modules available.")
        return
    
    print("\033[93mAvailable modules:\033[0m")
    for idx, module_name in enumerate(available_modules):
        print(f"  {idx + 1}. {module_name}")
    print("\n")
    # Prompt user to select a module
    selected_index = int(input("Select a module to load (number): ")) - 1
    if selected_index < 0 or selected_index >= len(available_modules):
        print("Invalid selection. Quitting...")
        return
    
    selected_module_name = available_modules[selected_index]
    
    # Load and execute the main function of the selected module
    main_func = modules.load_main_function(selected_module_name)
    if main_func and callable(main_func):
        main_func()
    else:
        print(f"No main function found in module {selected_module_name}.")

if __name__ == "__main__":
    modules.load_modules(modules.MODULES_DIR)
    main()
