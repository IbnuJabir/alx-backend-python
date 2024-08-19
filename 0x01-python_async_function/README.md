# 0x01. Python - Async

This directory contains a series of Python scripts focused on understanding and implementing asynchronous programming using the `asyncio` module. The tasks within this project will guide you through the basics of asynchronous functions, coroutines, and tasks in Python.

## Learning Objectives

By the end of this project, you should be able to:

- Understand and explain the `async` and `await` syntax in Python.
- Execute an async program using the `asyncio` module.
- Run multiple coroutines concurrently.
- Create and manage `asyncio` tasks.
- Utilize the `random` module in conjunction with async programming.

## Project Structure

### Task 0: The Basics of Async
- **File:** `0-basic_async_syntax.py`
- **Description:** Implements an asynchronous coroutine `wait_random` that takes an integer `max_delay` (default 10) and waits for a random delay between 0 and `max_delay` seconds, eventually returning the delay.

### Task 1: Let's Execute Multiple Coroutines at the Same Time with Async
- **File:** `1-concurrent_coroutines.py`
- **Description:** Defines an async routine `wait_n` that spawns `wait_random` `n` times with a specified `max_delay`. It returns a list of all the delays in ascending order without using the `sort()` function.

### Task 2: Measure the Runtime
- **File:** `2-measure_runtime.py`
- **Description:** Implements a `measure_time` function that measures the total execution time for `wait_n(n, max_delay)` and returns the average time per coroutine.

### Task 3: Tasks
- **File:** `3-tasks.py`
- **Description:** Defines a regular function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task` for `wait_random`.

### Task 4: More Tasks
- **File:** `4-tasks.py`
- **Description:** Modifies `wait_n` into a new function `task_wait_n`, where `task_wait_random` is called instead of `wait_random`.

## Requirements

- All scripts are executed using Python 3.7 on Ubuntu 18.04 LTS.
- Each script includes a `README.md` at the root of the folder.
- Scripts follow `pycodestyle` guidelines (version 2.5.x).
- All functions and coroutines are type-annotated and properly documented.
- The first line of all your files is exactly `#!/usr/bin/env python3`.
- All files must be executable.

## Author

This project is done by **Kedir Jabir**.  
Email: [kedirjabir12@gmail.com](mailto:kedirjabir12@gmail.com)


