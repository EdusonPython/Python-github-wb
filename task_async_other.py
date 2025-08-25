import asyncio
from time import monotonic
import random


async def parse_request(request):
    await asyncio.sleep(random.random())
    data = random.randint(1, 100)
    print(f'{request} done')
    return data


async def process_data(data):
    await asyncio.sleep(random.random())
    print('x')
    return data * 2


async def handle_request(request):
    data = await parse_request(request)
    process = await process_data(data)
    return f'parse_request: {data}, process_data: {process}'


async def main():
    requests = [f'Request {i}' for i in range(1000)]

    tasks = [asyncio.create_task(handle_request(req)) for req in requests]

    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == '__main__':
    start = monotonic()

    asyncio.run(main())

    duration = monotonic() - start
    print(f'It took {duration:0.2f} secs')