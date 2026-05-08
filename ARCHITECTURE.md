# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- `fibonacci.py`: Core Fibonacci generation logic with a function `generate_fibonacci(limit: int) -> list[int]`
- `cli.py`: Command-line interface that accepts a limit argument and prints the Fibonacci sequence
- `tests/test_fibonacci.py`: Unit tests for the Fibonacci generation function

## Interfaces

- `fibonacci.py` exposes:
  - `generate_fibonacci(limit: int) -> list[int]`: Returns a list of Fibonacci numbers up to the given limit
  - `fibonacci(n: int) -> int`: Returns the nth Fibonacci number (optional helper)

- `cli.py` depends on `fibonacci.py`:
  - Parses command-line arguments to get the limit
  - Calls `generate_fibonacci(limit)` and prints the result

## Shared Data Structures

- `limit`: Integer representing the upper bound (inclusive or exclusive as specified)
- Return type: `list[int]` containing Fibonacci numbers in ascending order

## External Dependencies

- No external dependencies required. Standard Python only.
