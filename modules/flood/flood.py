import requests
import threading
import time
import sys
from multiprocessing import Value, Array


class Flood:
    def __init__(self, url, num_requests, num_threads=1, delay_between_requests=100, rate_limit_timeout=5000):
        self.url = url
        self.num_requests = num_requests
        self.num_threads = num_threads
        self.delay_between_requests = delay_between_requests
        self.rate_limit_timeout = rate_limit_timeout
        self.request_counter = Value('i', 0)
        self.status_message = Array('c', b' ' * 100)

    def handle_status_code(self, status_code):
        status_messages = {
            200: "OK: Die Anfrage war erfolgreich.",
            301: "Moved Permanently: Die Ressource wurde dauerhaft verschoben.",
            302: "Found: Die Ressource wurde temporär verschoben.",
            400: "Bad Request: Die Anfrage war ungültig.",
            401: "Unauthorized: Authentifizierung erforderlich.",
            403: "Forbidden: Zugriff verweigert.",
            404: "Not Found: Die Ressource wurde nicht gefunden.",
            429: "Too Many Requests: Zu viele Anfragen. Rate limit exceeded.",
            500: "Internal Server Error: Ein Serverfehler ist aufgetreten.",
            502: "Bad Gateway: Ungültige Antwort vom Gateway.",
            503: "Service Unavailable: Der Dienst ist vorübergehend nicht verfügbar.",
            504: "Gateway Timeout: Zeitüberschreitung des Gateways."
        }
        return status_messages.get(status_code, f"Unknown Status Code: {status_code}")

    def send_requests(self):
        for _ in range(self.num_requests // self.num_threads):
            try:
                response = requests.get(self.url)
                message = self.handle_status_code(response.status_code)
                with self.request_counter.get_lock():
                    self.request_counter.value += 1
                with self.status_message.get_lock():
                    self.status_message.value = message.encode('utf-8')
                # Lösche die aktuellen Zeilen und überschreibe sie
                # Lösche die vorherige Zeile (counter line)
                sys.stdout.write("\033[F\033[K")
                # Lösche die vorherige Zeile (status line)
                sys.stdout.write("\033[F\033[K")
                sys.stdout.write(f"Anfragen gesendet: {
                                 self.request_counter.value}\nStatus: {message}\n")
                sys.stdout.flush()
                if response.status_code == 429:
                    # Wartezeit bei Überschreitung des Rate-Limits in Sekunden
                    time.sleep(self.rate_limit_timeout / 1000)
                else:
                    # Reguläre Wartezeit zwischen Anfragen in Sekunden
                    time.sleep(self.delay_between_requests / 1000)
            except requests.exceptions.RequestException as e:
                print(f"Anfrage fehlgeschlagen: {e}")

    def start(self):
        threads = []
        start_time = time.time()
        for _ in range(self.num_threads):
            thread = threading.Thread(target=self.send_requests)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        end_time = time.time()
        print(f"\nAlle Anfragen abgeschlossen in {
              end_time - start_time} Sekunden")
