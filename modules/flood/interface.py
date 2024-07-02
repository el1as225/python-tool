import os

# Clears the console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

class FloodSettings:
    def __init__(self):
        self.url = ""                      # URL deiner Website
        self.num_requests = 0              # Anzahl der Anfragen
        self.num_threads = 1               # Anzahl der Threads
        self.delay_between_requests = 100  # Wartezeit zwischen den Anfragen in Millisekunden
        self.rate_limit_timeout = 5000     # Wartezeit bei Überschreitung des Rate-Limits in Millisekunden
        self.attacking = False             # Angriff aktiv

    # Flood settings interface
    def settings_flood(self):
        cls()  # clear the console

        # Available commands: target, requests, threads, delay, ratelimitdelay, run, exit
        print("  target \033[93m[Target url]\033[0m\n  requests \033[93m[1-1000]\033[0m\n  threads \033[93m[1-100]\033[0m\n  delay \033[93m[1-10000]\033[0m\n  ratelimitdelay \033[93m[1-10000]\033[0m\n\n  run\n  exit\n")

        while not self.attacking:
            userInput = input("(alpha-v1.1) \033[92mguest\033[0m:\033[91m~/dos/flood\033[0m$ ")
            command = userInput.split(" ")[0]
            value = userInput[len(command):].strip()

            match command:
                case "target":
                    self.url = value
                    dashes = "-" * len(self.url)
                    print(f"\033[93m\n  |--------------{dashes}|\n  | Target URL: {self.url} |\n  |{dashes}--------------|\n\033[0m")  # Bestätigung der URL
                case "requests":
                    try:
                        self.num_requests = int(value)
                        dashes = "-" * len(str(self.num_requests))
                        print(f"\033[93m\n  |------------{dashes}|\n  | Requests: {self.num_requests} |\n  |{dashes}------------|\n\033[0m")
                    except ValueError:
                        self.print_error()
                case "threads":
                    try:
                        self.num_threads = int(value)
                        dashes = "-" * len(str(self.num_threads))
                        print(f"\033[93m\n  |-----------{dashes}|\n  | Threads: {self.num_threads} |\n  |{dashes}-----------|\n\033[0m")
                    except ValueError:
                        self.print_error()
                case "delay":
                    try:
                        self.delay_between_requests = int(value)
                        dashes = "-" * len(str(self.delay_between_requests))
                        print(f"\033[93m\n  |---------{dashes}|\n  | Delay: {self.delay_between_requests} |\n  |{dashes}---------|\n\033[0m")
                    except ValueError:
                        self.print_error()
                case "ratelimitdelay":
                    try:
                        self.rate_limit_timeout = int(value)
                        dashes = "-" * len(str(self.rate_limit_timeout))
                        print(f"\033[93m\n  |---------------------{dashes}|\n  | Ratelimit Delay: {self.rate_limit_timeout} |\n  |{dashes}---------------------|\n\033[0m")
                    except ValueError:
                        self.print_error()
                case "run":
                    cls()  # clear the console
                    print("\033[91m\n  |--------------------|\n  | Starting attack... |\n  |--------------------|\n\033[0m")
                    if self.url == "" or self.num_requests == 0:
                        print("\033[91m\n  |--------------------------------------------|\n  | ERROR: Please fill in all the information. |\n  |--------------------------------------------|\n\033[0m")
                        self.attacking = False
                        continue
                    else:
                        self.attacking = True
                        break
                case "exit":
                    print("\033[91m\n  |-----------------|\n  | Exiting program |\n  |-----------------|\n\033[0m")
                    break

        if self.attacking:
            self.print_summary()
            return self.url, self.num_requests, self.num_threads, self.delay_between_requests, self.rate_limit_timeout, self.attacking

    def print_error(self):
        print("\033[91m\n  |---------------------------------|\n  | ERROR: Please enter a valid number. |\n  |---------------------------------|\n\033[0m")

    def print_summary(self):
        dashes = "-" * (len(self.url) + 21)  # Adjusted length for the border
        print(f"  \033[93m|{dashes}|\033[0m")
        print(f"  \033[93m|  \033[1mURL:\033[0m \033[93m{self.url}{' ' * (len(self.url) + 14 - len(str(self.url)))}|\033[0m")
        print(f"  \033[93m|  \033[1mRequests:\033[0m \033[93m{self.num_requests}{' ' * (len(self.url) + 9 - len(str(self.num_requests)))}|\033[0m")
        print(f"  \033[93m|  \033[1mThreads:\033[0m \033[93m{self.num_threads}{' ' * (len(self.url) + 10 - len(str(self.num_threads)))}|\033[0m")
        print(f"  \033[93m|  \033[1mDelay:\033[0m \033[93m{self.delay_between_requests}{' ' * (len(self.url) + 12 - len(str(self.delay_between_requests)))}|\033[0m")
        print(f"  \033[93m|  \033[1mRate Limit Delay:\033[0m \033[93m{self.rate_limit_timeout}{' ' * (len(self.url) + 1 - len(str(self.rate_limit_timeout)))}|\033[0m")
        print(f"  \033[93m|{dashes}|\033[0m\n\n\n")

def test():
    # Beispielverwendung
    flood_settings = FloodSettings()
    flood_settings.settings_flood()

if __name__ == "__main__":
    test()
