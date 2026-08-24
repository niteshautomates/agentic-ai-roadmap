import asyncio

async def fetch_url(url: str, semaphore: asyncio.Semaphore):
    # Enforce concurrency limit (max concurrent locks)
    async with semaphore:
        print(f"Fetching: {url}")
        # Simulate an asynchronous HTTP network call
        await asyncio.sleep(1) 
        print(f"Completed: {url}")
        return f"Data from {url}"

async def main():
    # Allow a maximum of 3 concurrent network connections
    semaphore = asyncio.Semaphore(3)
    urls = [f"https://api.example.com/item/{i}" for i in range(10)]
    
    # Schedule all fetches concurrently while respecting the semaphore limit
    tasks = [fetch_url(url, semaphore) for url in urls]
    results = await asyncio.gather(*tasks)
    
    print(f"Successfully processed {len(results)} items.")

asyncio.run(main())