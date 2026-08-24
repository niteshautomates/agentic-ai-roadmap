# 7 Async Patterns for Running AI Agents Concurrently in Python

A concise summary guide for interview preparation covering the core concept, implementation primitive, and primary use case for each asynchronous pattern in Python multi-agent systems.

---

### 1. Fire and Forget (`asyncio.create_task`)
* **Summary:** Spawns a background task asynchronously and immediately continues execution without waiting for the task's output.
* **Primitive:** `asyncio.create_task(agent_task())`
* **Use Case:** Non-blocking background side tasks like saving chat history to a database, updating vector indices, or firing logging/telemetry events.

---

### 2. Scatter-Gather (`asyncio.gather`)
* **Summary:** Runs multiple sub-agents simultaneously in parallel and waits for all of them to return their completed results before proceeding.
* **Primitive:** `await asyncio.gather(*agent_tasks)`
* **Use Case:** Concurrent research and retrieval tasks, such as querying Web Search, Wikipedia, and internal document DBs at the same time to build context.

---

### 3. Supervised Task Groups (`asyncio.TaskGroup`)
* **Summary:** Manages parallel agents within a structured concurrency scope, automatically canceling all remaining active agents if any single worker crashes.
* **Primitive:** `async with asyncio.TaskGroup() as tg:`
* **Use Case:** Critical multi-step workflows (e.g., payment validation + seat reservation) where failure in one sub-agent requires aborting all active sub-tasks.

---

### 4. Producer-Consumer (`asyncio.Queue`)
* **Summary:** Decouples task generation from task execution using an async queue, where dynamic producer agents push tasks and worker pools process them asynchronously.
* **Primitive:** `queue = asyncio.Queue(maxsize=100)`
* **Use Case:** Processing unpredictable or dynamic workloads, such as continuous user request streams or dynamic multi-agent task delegation.

---

### 5. Backpressure Rate-Limiting (`asyncio.Semaphore`)
* **Summary:** Enforces a strict ceiling on the maximum number of agents allowed to execute concurrently using a shared counter guard.
* **Primitive:** `async with asyncio.Semaphore(10):`
* **Use Case:** Protecting external APIs from HTTP 429 rate limits and preventing agent pools from exhausting limited database connection pools or system memory.

---

### 6. Speculative Execution (`asyncio.wait` + `FIRST_COMPLETED`)
* **Summary:** Launches redundant agents to attempt the same goal concurrently, taking the output of whichever finishes first and canceling the rest.
* **Primitive:** `asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)`
* **Use Case:** Ultra-low latency user-facing applications, such as racing a fast local 8B model against a cloud API to return the fastest response.

---

### 7. Asynchronous Streaming Pipelines (Async Generators)
* **Summary:** Connects specialized agents sequentially via continuous streams, allowing downstream agents to process chunks immediately before upstream agents finish.
* **Primitive:** `async def agent(): yield data` / `async for chunk in agent():`
* **Use Case:** Real-time multi-agent processing chains, like streaming raw LLM tokens into a real-time markdown formatter, which streams into a moderation parser.

---

### Quick Interview Cheat Sheet

| Requirement | Preferred Pattern | Primary Python Primitive |
| :--- | :--- | :--- |
| **All parallel tasks must return** | Scatter-Gather or Task Groups | `asyncio.gather()`, `asyncio.TaskGroup()` |
| **Protect API rate limits / DB pools** | Backpressure | `asyncio.Semaphore()` |
| **Variable work rate / decoupled workers** | Producer-Consumer | `asyncio.Queue(maxsize=N)` |
| **Lowest latency possible** | Speculative Execution | `asyncio.wait(..., FIRST_COMPLETED)` |
| **Background execution without blocking** | Fire and Forget | `asyncio.create_task()` |
| **Real-time pipeline processing** | Streaming Pipeline | Async generators (`yield` / `async for`) |