import asyncio
import queue
import random

async def worker(worker_id: int, queue: asyncio.Queue):
 while True:
    job_id = await queue.get()

    #Simulating processing work
    print(f"Worker {worker_id} started processing {job_id}")
    await asyncio.sleep(random.uniform(0.5, 1.5))  # Simulate variable processing time
    print(f"Worker {worker_id} finished processing {job_id}")

    queue.task_done()

async def main():
    queue  = asyncio.Queue()
    # Create worker tasks to run concurrently in the background

    workers = [ asyncio.create_task(worker(i, queue))
               for i in range(3)
    ]

    # Enqueue 10 job items
    for job in range(1, 11):
        await queue.put(job)

    # Wait until all jobs are processed
    await queue.join()

    for w in workers:
        w.cancel()  # Cancel the worker tasks after all jobs are done

asyncio.run(main())        
            

