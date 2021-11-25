import asyncio
import aiohttp

SOURCE_FILE_NAME = 'data.txt'
WORKER_COUNT = 10
SAVE_PATH = './result'


async def worker(url_tasks, resp_tasks):
    while True:
        if url_tasks.empty():
            break
        url = await url_tasks.get()
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as resp:
                resp_text = await resp.text()  # TODO delete
                await resp_tasks.put(resp_text)


async def saver(resp_tasks, iter):
    for i in range(iter):
        resp = await resp_tasks.get()
        with open(f"{SAVE_PATH}/response_{i}.html", "w") as file:  # TODO os join path
            file.write(resp)
        print(len(resp))


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
    asyncio.run(entry())
