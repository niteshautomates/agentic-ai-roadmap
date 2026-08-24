import asyncio

async def fetch_slow_db_record(record_id: int):
    # Simulate a slow database query
    await asyncio.sleep(3)
    return {"id": record_id, "name": "User Data"}

async def main():
    try:
        # Enforce a 1.5-second timeout budget on the query
        result = await asyncio.wait_for(fetch_slow_db_record(42), timeout=1.5)
        print("Received:", result)
    except asyncio.TimeoutError:
        print("Operation timed out! Falling back to cached response.")

asyncio.run(main())