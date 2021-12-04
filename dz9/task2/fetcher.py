import argparse
import asyncio
import json
import os

import aiohttp

SOURCE_FILE_NAME = 'data.txt'
WORKER_COUNT = 10
SAVE_PATH = './result'


async def worker(url_tasks, resp_tasks):
    while True:
        if url_tasks.empty():
            break
        url = url_tasks.get_nowait()
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, ssl=False) as resp:
                    await resp_tasks.put(await resp.text())
            except Exception as Argument:
                msg = {"error": str(Argument)}
                print(msg)
                await resp_tasks.put(json.dumps(msg))


async def saver(resp_tasks, num):
    for i in range(num):
        resp = await resp_tasks.get()
        with open(os.path.join(SAVE_PATH, f"response_{i}.html"), "w") as file:
            file.write(resp)


def load_urls():
    with open(SOURCE_FILE_NAME, 'r') as file:
        data = file.read().split('\n')
        return data


async def entry():
    urls = load_urls()
    url_tasks = asyncio.Queue(maxsize=len(urls))
    for url in urls:
        await url_tasks.put(url)
    resp_tasks = asyncio.Queue(maxsize=len(urls))
    workers = [asyncio.create_task(worker(url_tasks, resp_tasks)) for _ in range(WORKER_COUNT)]
    resp_saver = asyncio.create_task(saver(resp_tasks, len(urls)))
    await asyncio.gather(resp_saver, *workers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="URL Fetcher")
    parser.add_argument("thread_count", type=int)
    parser.add_argument("file")
    parser.add_argument("-d", "--destination", dest="destination", default='./result')
    args = parser.parse_args()

    WORKER_COUNT = args.thread_count
    SOURCE_FILE_NAME = args.file
    SAVE_PATH = args.destination

    asyncio.run(entry())
