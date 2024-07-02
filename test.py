import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls() # clear the screen
print("\033[1m\033[95mWelcome to Eli's DoS Tool!\033[0m\033[0m\n")

# Selecting targen URL
print("  target [Target url]\n  requests [1-1000]\n  threads [1-100]\n  delay [1-10000]\n  ratelimitdelay [1-10000]\n\n  run\n")
userInput = ""

while userInput != "run":
  userInput = input("(v0.1) \033[92mguest\033[0m:\033[91m~/eli's_dos_tool\033[0m$ ")
  
  match userInput.split(" ")[0]:
    case "run":
      print("\033[91m\n  |--------------------|\n  | Starting attack... |\n  |--------------------|\n\033[0m")
      break
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
      print(f"\033[93m\n  |--------{dashes}|\n  | Delay: {url} |\n  |{dashes}--------|\n\033[0m")
    case "ratelimitdelay":
      rate_limit_timeout = userInput.strip("ratelimitdelay ")     # Wartezeit bei Überschreitung des Rate-Limits in Millisekunden
      
      dashes = "-" * len(rate_limit_timeout)
      print(f"\033[93m\n  |---------------------{dashes}|\n  | Ratelimit Delay: {url} |\n  |{dashes}---------------------|\n\033[0m")

#print("\n" + url + "\n" + num_requests + "\n" + num_threads + "\n" + delay_between_requests + "\n" + rate_limit_timeout + "\n")