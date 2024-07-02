import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls() # clear the console

# Welcome message
print("\033[1m\033[95mWelcome to Eli's DoS Tool!\033[0m\033[0m\n")

# Available commands: target, requests, threads, delay, ratelimitdelay, run, exit
print("  target \033[93m[Target url]\033[0m\n  requests \033[93m[1-1000]\033[0m\n  threads \033[93m[1-100]\033[0m\n  delay \033[93m[1-10000]\033[0m\n  ratelimitdelay \033[93m[1-10000]\033[0m\n\n  run\n  exit\n")

userInput = ""                # Benutzereingabe

url = ""                      # URL deiner Website
num_requests = 0              # Anzahl der Anfragen

num_threads = 1               # Anzahl der Threads
delay_between_requests = 100  # Wartezeit zwischen den Anfragen in Millisekunden
rate_limit_timeout = 5000     # Wartezeit bei Überschreitung des Rate-Limits in Millisekunden

attacking = False             # Angriff aktiv

while not attacking:
  userInput = input("(v0.1) \033[92mguest\033[0m:\033[91m~/eli's_dos_tool\033[0m$ ")  # Eingabeaufforderung
  
  command = userInput.split(" ")[0]
  value = userInput[len(command):].strip()
  
  match command:
    case "target":
      url = userInput.strip("target ")            # URL deiner Website
      dashes = "-" * len(url)
      print(f"\033[93m\n  |--------------{dashes}|\n  | Target URL: {url} |\n  |{dashes}--------------|\n\033[0m")  # Bestätigung der URL
    case "requests":
      try:
        num_requests = int(value)                 # Anzahl der Anfragen
        dashes = "-" * len(str(num_requests))
        print(f"\033[93m\n  |------------{dashes}|\n  | Requests: {num_requests} |\n  |{dashes}------------|\n\033[0m")
      except ValueError:
        print("\033[91m\n  |---------------------------------|\n  | ERROR: Please enter a valid number. |\n  |---------------------------------|\n\033[0m") # Fehlermeldung
    case "threads":
      try:
        num_threads = int(value)                  # Anzahl der Threads
        dashes = "-" * len(str(num_threads))
        print(f"\033[93m\n  |-----------{dashes}|\n  | Threads: {num_threads} |\n  |{dashes}-----------|\n\033[0m") # Bestätigung der Threads
      except ValueError:
        print("\033[91m\n  |---------------------------------|\n  | ERROR: Please enter a valid number. |\n  |---------------------------------|\n\033[0m") # Fehlermeldung
    case "delay":
      try:
        delay_between_requests = int(value)       # Wartezeit zwischen den Anfragen in Millisekunden
        dashes = "-" * len(str(delay_between_requests))
        print(f"\033[93m\n  |---------{dashes}|\n  | Delay: {delay_between_requests} |\n  |{dashes}---------|\n\033[0m")  # Bestätigung der Wartezeit
      except ValueError:
        print("\033[91m\n  |---------------------------------|\n  | ERROR: Please enter a valid number. |\n  |---------------------------------|\n\033[0m") # Fehlermeldung
    case "ratelimitdelay":
      try:
        rate_limit_timeout = int(value)             # Wartezeit bei Überschreitung des Rate-Limits in Millisekunden
        dashes = "-" * len(str(rate_limit_timeout))
        print(f"\033[93m\n  |---------------------{dashes}|\n  | Ratelimit Delay: {rate_limit_timeout} |\n  |{dashes}---------------------|\n\033[0m")  # Bestätigung der Wartezeit
      except ValueError:
        print("\033[91m\n  |---------------------------------|\n  | ERROR: Please enter a valid number. |\n  |---------------------------------|\n\033[0m") # Fehlermeldung
    case "run":
      cls() # clear the console
      print("\033[91m\n  |--------------------|\n  | Starting attack... |\n  |--------------------|\n\033[0m")
      if url == "" or num_requests == 0:
        print("\033[91m\n  |--------------------------------------------|\n  | ERROR: Please fill in all the information. |\n  |--------------------------------------------|\n\033[0m")  # Fehlermeldung
        attacking = False
        continue
      else:
        attacking = True
        break
    case "exit":
      print("\033[91m\n  |-----------------|\n  | Exiting program |\n  |-----------------|\n\033[0m") # Programm beenden
      break

if attacking:
  dashes = "-" * (len(url) + 21)  # Adjusted length for the border
  print(f"  \033[93m|{dashes}|\033[0m")
  print(f"  \033[93m|  \033[1mURL:\033[0m \033[93m{url}{' ' * (len(url) + 14 - len(str(url)))}|\033[0m")
  print(f"  \033[93m|  \033[1mRequests:\033[0m \033[93m{num_requests}{' ' * (len(url) + 9 - len(str(num_requests)))}|\033[0m")
  print(f"  \033[93m|  \033[1mThreads:\033[0m \033[93m{num_threads}{' ' * (len(url) + 10 - len(str(num_threads)))}|\033[0m")
  print(f"  \033[93m|  \033[1mDelay:\033[0m \033[93m{delay_between_requests}{' ' * (len(url) + 12 - len(str(delay_between_requests)))}|\033[0m")
  print(f"  \033[93m|  \033[1mRate Limit Delay:\033[0m \033[93m{rate_limit_timeout}{' ' * (len(url) + 1 - len(str(rate_limit_timeout)))}|\033[0m")
  print(f"  \033[93m|{dashes}|\033[0m\n")
