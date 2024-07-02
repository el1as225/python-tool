import requests
import threading
import time
import sys


def flood(url, num_requests, num_threads=1, delay_between_requests=100, rate_limit_timeout=5000):
    # Konfiguration
    # url                       =   URL deiner Website
    # num_requests              =   Anzahl der Anfragen
    # num_threads               =   Anzahl der Threads
    # delay_between_requests    =   Wartezeit zwischen den Anfragen in Millisekunden
    # rate_limit_timeout        =   Wartezeit bei Überschreitung des Rate-Limits in Millisekunden

    # DEBUG
    print(f"URL: {url}")
    print(f"Anzahl der Anfragen: {num_requests}")

    # Funktion zur Verarbeitung der Statuscodes
    def handle_status_code(status_code):
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

    # Funktion zum Senden der Anfragen
    def send_requests(request_counter, status_message):
        for _ in range(num_requests // num_threads):
            try:
                response = requests.get(url)
                message = handle_status_code(response.status_code)
                with request_counter.get_lock():
                    request_counter.value += 1
                with status_message.get_lock():
                    status_message.value = message.encode('utf-8')
                # Lösche die aktuellen Zeilen und überschreibe sie
                # Lösche die vorherige Zeile (counter line)
                sys.stdout.write("\033[F\033[K")
                # Lösche die vorherige Zeile (status line)
                sys.stdout.write("\033[F\033[K")
                sys.stdout.write(f"Anfragen gesendet: {
                                 request_counter.value}\nStatus: {message}\n")
                sys.stdout.flush()
                if response.status_code == 429:
                    # Wartezeit bei Überschreitung des Rate-Limits in Sekunden
                    time.sleep(rate_limit_timeout / 1000)
                else:
                    # Reguläre Wartezeit zwischen Anfragen in Sekunden
                    time.sleep(delay_between_requests / 1000)
            except requests.exceptions.RequestException as e:
                print(f"Anfrage fehlgeschlagen: {e}")

    def __init__():
        from multiprocessing import Value, Array

        # Gemeinsamer Zähler für die Anzahl der gesendeten Anfragen und Statusnachricht
        request_counter = Value('i', 0)
        # Platz für die Statusnachricht
        status_message = Array('c', b' ' * 100)

        threads = []

        # Erstelle und starte die Threads
        start_time = time.time()
        for _ in range(num_threads):
            thread = threading.Thread(target=send_requests, args=(
                request_counter, status_message))
            thread.start()
            threads.append(thread)

        # Warte, bis alle Threads abgeschlossen sind
        for thread in threads:
            thread.join()

        end_time = time.time()

        print(f"\nAlle Anfragen abgeschlossen in {
              end_time - start_time} Sekunden")
