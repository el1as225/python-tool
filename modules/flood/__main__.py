import sys
from .flood import Flood
from .interface import FloodSettings, cls


def main():
    settings_flood = FloodSettings()
    try:
        url, num_requests, num_threads, delay_between_requests, rate_limit_timeout, attacking = settings_flood.settings_flood()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    flood = Flood(url, num_requests, num_threads,
                  delay_between_requests, rate_limit_timeout)
    if attacking:
        flood.start()
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
