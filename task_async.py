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


async def main():
    requests = [f'Request {i}' for i in range(1000)]

    parsed_results = await asyncio.gather(*(parse_request(req) for req in requests))

    processed_results = await asyncio.gather(*(process_data(data) for data in parsed_results))

    for r, d in zip(parsed_results, processed_results):
        print(f'parse_request: {r}, process_data: {d}')


if __name__ == '__main__':
    start = monotonic()

    asyncio.run(main())

    duration = monotonic() - start
    print(f'It took {duration:0.2f} secs')