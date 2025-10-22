import asyncio
from tabnanny import process_tokens


async def process_numbers(a: int, b: int, duration: int):
    print(f"Adding numbers {a} + {b}")

    await asyncio.sleep(duration)

    return a + b

async def main():

    tasks = [process_numbers(3, 4, 5),
             process_numbers(5, 8, 3),
             process_numbers(6, 5, 2)] #corutine objects

    results = await asyncio.gather(*tasks)

    print(results)

async def main_background():

    task1 = asyncio.create_task(process_numbers(3, 3, 3))
    task2 = asyncio.create_task(process_numbers(4, 3, 4))

    results1 = await task1
    results2 = await task2

    print(results1, results2)


asyncio.run(main_background())