import asyncio
from random import random

# Пишем небольшую показательную программу передачи эстафетной палочки с asyncio


async def pass_baton(team_name):
    speed = random()
    print(f'{team_name}: Passing the baton... {speed:.2f}')
    await asyncio.sleep(speed)
    return speed


async def team_run(team_name):
    total_time = 0
    for _ in range(5):
        time = await pass_baton(team_name)
        total_time += time
        print(f'\t{team_name}: {total_time:.2f}')


async def main():
    await asyncio.gather(team_run('Team_1'), team_run('Team_2'))


if __name__ == '__main__':
    asyncio.run(main())

