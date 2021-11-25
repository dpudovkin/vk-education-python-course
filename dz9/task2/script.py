import asyncio

import aiohttp

#
# async def run():
#     urls=['https://www.google.com/']*10
#     for url in urls:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url, ssl=False) as resp:
#                 resp_len = len(await resp.text())
#                 print(f'Status: {resp.status}, Response length: {resp_len}')

async def seq_start(urls):
    index =0
    for url in urls:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, ssl=False) as resp:
                print(f"Start {index}")
                resp_len = len(await resp.text())
                print(f'Status: {resp.status}, Response length: {resp_len}')
                index = index + 1
                print(f"Stop {index}")



async def run(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as resp:
            resp_len = len(await resp.text())
            print(f'Status: {resp.status}, Response length: {resp_len}')


async def entry():
    urls = ['https://www.google.com/'] * 10

    await seq_start(urls)

    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(run(url)))
    await asyncio.gather(*tasks)



if __name__ == '__main__':
    asyncio.run(entry())





