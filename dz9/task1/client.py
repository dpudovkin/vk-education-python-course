import argparse
import json
import threading
import socket

THREAD_COUNT = 10
FILE_NAME = ''
PORT = 10000


def init_worker(url_list, lock):
    def worker_loop():
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('localhost', PORT)
            sock.connect(server_address)
        except Exception as Argument:
            print({"error": str(Argument)})
            return

        while True:
            with lock:
                if len(url_list) == 0:
                    sock.close()
                    break
                url = url_list.pop()

            sock.sendall(url.encode('utf8'))
            data = sock.recv(1000)
            print(f"{url}: {json.loads(data.decode())}")

    return threading.Thread(target=worker_loop)


def get_urls():
    with open(FILE_NAME, 'r') as file:
        data = file.read().split('\n')
        return data


def run():
    urls = get_urls()
    lock = threading.Lock()

    workers = []
    for i in range(THREAD_COUNT):
        worker = init_worker(urls, lock)
        worker.start()
        workers.append(worker)

    for worker in workers:
        worker.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Client for URL server")
    parser.add_argument("file")
    parser.add_argument("-c", "--concurrency", dest="thread_count", default=10, type=int)
    parser.add_argument("-p", "--port", dest="port", default=10000, type=int)
    args = parser.parse_args()
    FILE_NAME = args.file
    THREAD_COUNT = args.thread_count
    PORT=args.port
    run()
