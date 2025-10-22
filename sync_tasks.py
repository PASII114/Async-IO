import time
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread


def execute_sync_task(task_name: str, duration: int):
    print(f"Starting task - {task_name}")
    time.sleep(duration)
    print(f"Ending task - {task_name}")


def main():
    thread1 = Thread(target=execute_sync_task, args=("Task 1", 5))
    thread2 = Thread(target=execute_sync_task, args=("Task 2", 2))
    thread3 = Thread(target=execute_sync_task, args=("Task 3", 3))

    thread1.start()
    thread2.start()
    thread3.start()


def main_threadpool():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.submit(execute_sync_task, "Task 1", 5)
        executor.submit(execute_sync_task, "Task 2", 2)
        executor.submit(execute_sync_task, "Task 3", 3)

# main_threadpool()

import asyncio

async def execute_async_task(task_name: str, duration: int): #coroutine function
    print(f"Starting task - {task_name}")
    # time.sleep(duration)
    print(f"Ending task - {task_name}")


async def async_main():
    await asyncio.gather(
        execute_async_task("Task 1", 5),
        execute_async_task("Task 2", 3),
        execute_async_task("Task 3", 5)
    )

asyncio.run(async_main()) #initiating our event loop