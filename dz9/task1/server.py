import argparse
import json
import sys
import threading
import socket
from queue import Queue
import time
import requests
from parser import frequent_word

CONNECTION_KEY = 'CONNECTION'
CLIENT_ADDRESS_KEY = 'CLIENT_ADDRESS'
EXPIRED_TIMEOUT_KEY = 'EXPIRED_TIMEOUT'
URL_KEY = 'URL'
CALLBACK_KEY = 'CALLBACK'

EXPIRED_TIMEOUT = 10_000  # timeout millis

WORD_COUNT = 5
WORKER_COUNT = 10
CONNECTION_COUNT = 10


def current_millis_time():
    return round(time.time() * 1000)


def handle_url(url):
    try:
        receive = requests.get(url)
        words = frequent_word(receive.text, WORD_COUNT)
        return words
    except Exception as Argument:
        return {"sent_data": str(url.decode()), "error": str(Argument)}


def init_url_worker(url_queue):
    def worker_loop():
        while True:
            data = url_queue.get()
            url = data[URL_KEY]
            data[CALLBACK_KEY](data=handle_url(url))

    return threading.Thread(target=worker_loop)


def init_worker(queue, url_queue):
    def init_callback(connection):
        def callback(data):
            try:
                json_data = json.dumps(data, indent=4, ensure_ascii=False).encode('utf8')
                connection.sendall(json_data)
                print(data)
            except Exception as Argument:
                print({"response_data": data, "error": str(Argument)})

        return callback

    def worker_loop():
        while True:

            client = queue.get()

            valid = True

            expired_time = client[EXPIRED_TIMEOUT_KEY]
            connection = client[CONNECTION_KEY]
            client_address = client[CLIENT_ADDRESS_KEY]

            if current_millis_time() > expired_time:
                valid = False
                print(f'Client {client_address} was expired.')
            try:
                while valid:
                    data = connection.recv(200)
                    if data:
                        url_queue.put({URL_KEY: data, CALLBACK_KEY: init_callback(connection)})
                    else:
                        break
            except:
                print('Socket closed by peer', file=sys.stderr)
            finally:
                connection.close()

    return threading.Thread(target=worker_loop)


def event_loop(queue, port):
    server_address = ('localhost', port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen()
    print(f'Listen clients on localhost:{port}...')
    while True:
        connection, client_address = sock.accept()
        queue.put({CONNECTION_KEY: connection,
                   CLIENT_ADDRESS_KEY: client_address,
                   EXPIRED_TIMEOUT_KEY: current_millis_time() + EXPIRED_TIMEOUT})


def run(port):
    url_workers = []
    url_queue = Queue()

    for i in range(WORKER_COUNT):
        worker = init_url_worker(url_queue)
        worker.start()
        url_workers.append(worker)

    workers = []
    queue = Queue()

    for i in range(CONNECTION_COUNT):
        worker = init_worker(queue, url_queue)
        worker.start()
        workers.append(worker)

    master_thread = threading.Thread(target=event_loop, args=(queue, port))
    master_thread.start()
    master_thread.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Master work server")
    parser.add_argument("-w", "--worker_count", dest="worker_count", required=True, type=int)
    parser.add_argument("-k", "--word_count", dest="word_count", required=True, type=int)
    parser.add_argument("-c", "--concurrency", dest="concurrency", type=int, default=10)
    parser.add_argument("-p", "--port", dest="port", type=int, default=10000)

    args = parser.parse_args()

    WORKER_COUNT = args.worker_count
    WORD_COUNT = args.word_count

    run(args.port)
