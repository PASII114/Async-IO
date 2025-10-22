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


asyncio.run(main())