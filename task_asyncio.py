import asyncio
from time import monotonic, sleep
import random
from concurrent.futures import ProcessPoolExecutor

async def parse_request(request):
    await asyncio.sleep(random.random())
    data = random.randint(1, 100)
    print(f'{request} done')
    return data

def process_data(data):
    sleep(random.random())
    print('x')
    return data * 2


async def main():
    requests = [f'Request {i}' for i in range(50)]  # список "запросов"

    start = monotonic()

    # асинхронная загрузка
    tasks = [parse_request(req) for req in requests]
    results = await asyncio.gather(*tasks)

    # CPU-обработка в процессах
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as executor:
        processed = await asyncio.gather(
            *[loop.run_in_executor(executor, process_data, r) for r in results]
        )

    print("Processed:", processed)

    duration = monotonic() - start
    print(f'It took {duration:0.2f} secs')

if __name__ == '__main__':
    asyncio.run(main())