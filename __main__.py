from modules.flood.flood import flood
from modules.flood.interface import settings_flood, cls


def main():
    # Clear the console
    cls()

    # Welcome message
    print("\033[1m\033[95mWelcome to Eli's DoS Tool!\033[0m\033[0m\n")

    # Available commands: target, requests, threads, delay, ratelimitdelay, run, exit
    print("  flood \033[93m[simple http/s dos attack]\033[0m\n")

    # Start Flood module
    match input("(alpha-v1.1) \033[92mguest\033[0m:\033[91m~/eli's_dos_kit\033[0m$ "):
        case "flood":
            url, num_requests, num_threads, delay_between_requests, rate_limit_timeout, attacking = settings_flood()
            if attacking:
                flood(url, num_requests, num_threads,
                      delay_between_requests, rate_limit_timeout)
            else:
                exit(1)
        case "exit":
            exit()


if __name__ == "__main__":
    main()
