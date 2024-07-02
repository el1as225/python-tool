import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls() # clear the screen
print("\033[1m\033[95mWelcome to Eli's DoS Tool!\033[0m\033[0m\n")

# Selecting targen URL
print("  target \033[93m[Target url]\033[0m\n  requests \033[93m[1-1000]\033[0m\n  threads \033[93m[1-100]\033[0m\n  delay \033[93m[1-10000]\033[0m\n  ratelimitdelay \033[93m[1-10000]\033[0m\n\n  run\n  exit\n")

userInput = ""
url = ""
num_requests = ""
num_threads = ""
delay_between_requests = ""
rate_limit_timeout = ""
attacking = True

while attacking:
  userInput = input("(v0.1) \033[92mguest\033[0m:\033[91m~/eli's_dos_tool\033[0m$ ")
  
  match userInput.split(" ")[0]:
    case "target":
      url = userInput.strip("target ")                            # URL deiner Website
      
      dashes = "-" * len(url)
      print(f"\033[93m\n  |--------------{dashes}|\n  | Target URL: {url} |\n  |{dashes}--------------|\n\033[0m")
    case "requests":
      num_requests = userInput.strip("requests ")                 # Anzahl der Anfragen
      
      dashes = "-" * len(num_requests)
      print(f"\033[93m\n  |------------{dashes}|\n  | Requests: {num_requests} |\n  |{dashes}------------|\n\033[0m")
    case "threads":
      num_threads = userInput.strip("threads ")                   # Anzahl der Threads
      
      dashes = "-" * len(num_threads)
      print(f"\033[93m\n  |-----------{dashes}|\n  | Threads: {num_threads} |\n  |{dashes}-----------|\n\033[0m")
    case "delay":
      delay_between_requests = userInput.strip("delay ")          # Wartezeit zwischen den Anfragen in Millisekunden
      
      dashes = "-" * len(delay_between_requests)
      print(f"\033[93m\n  |--------{dashes}|\n  | Delay: {delay_between_requests} |\n  |{dashes}--------|\n\033[0m")
    case "ratelimitdelay":
      rate_limit_timeout = userInput.strip("ratelimitdelay ")     # Wartezeit bei Überschreitung des Rate-Limits in Millisekunden
      
      dashes = "-" * len(rate_limit_timeout)
      print(f"\033[93m\n  |---------------------{dashes}|\n  | Ratelimit Delay: {rate_limit_timeout} |\n  |{dashes}---------------------|\n\033[0m")
    case "run":
      print("\033[91m\n  |--------------------|\n  | Starting attack... |\n  |--------------------|\n\033[0m")
      if url == "" or num_requests == "" or num_threads == "" or delay_between_requests == "" or rate_limit_timeout == "":
        print("\033[91m\n  |--------------------------------------------|\n  | ERROR: Please fill in all the information. |\n  |--------------------------------------------|\n\033[0m")
        attacking = True
        continue
      else:
        attacking = False
        break
    case "exit":
      print("\033[91m\n  |-----------------|\n  | Exiting program |\n  |-----------------|\n\033[0m")
      break

if not attacking:
  print("\nURL: " + url + "\nRequests: " + num_requests + "\nThreads: " + num_threads + "\nDelay: " + delay_between_requests + "\nRate Limit Delay: " + rate_limit_timeout + "\n")