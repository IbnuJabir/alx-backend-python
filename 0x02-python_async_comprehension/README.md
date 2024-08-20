# 0x02. Python - Async Comprehension

## Description
This project is part of the ALX Software Engineering program and focuses on asynchronous programming in Python. It covers the use of asynchronous generators, async comprehensions, and how to type-annotate generators.

## Learning Objectives
By the end of this project, you should be able to:
- Write an asynchronous generator.
- Use async comprehensions.
- Type-annotate generators in Python.

## Requirements
- Python 3.7
- All files should adhere to the `pycodestyle` (version 2.5.x) coding style.
- All code should be type-annotated.
- Files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3`.

## Project Structure
The project contains the following tasks:

### Task 0: Async Generator
- **File:** `0-async_generator.py`
- **Description:** Write a coroutine called `async_generator` that loops 10 times, each time asynchronously waits 1 second, and then yields a random float number between 0 and 10.

### Task 1: Async Comprehension
- **File:** `1-async_comprehension.py`
- **Description:** Write a coroutine called `async_comprehension` that collects 10 random numbers using an async comprehension over `async_generator`, then returns the 10 numbers.

### Task 2: Run Time for Four Parallel Comprehensions
- **File:** `2-measure_runtime.py`
- **Description:** Write a coroutine called `measure_runtime` that executes `async_comprehension` four times in parallel using `asyncio.gather`, measures the total runtime, and returns it.

## How to Run
Each task file can be run independently. For example, to run the first task:
```bash
python3 0-main.py
```

## Example Usage
Example output for `0-async_generator.py`:
```bash
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418, ...]
```

Example output for `1-async_comprehension.py`:
```bash
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575, ...]
```

Example output for `2-measure_runtime.py`:
```bash
10.021936893463135
```

## Author
- Kedir Jabir - [kedirjabir12@gmail.com](mailto:kedirjabir12@gmail.com)
```

This template gives a clear overview of the project, tasks, and how to run and use the provided files.