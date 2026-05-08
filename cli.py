import sys

from fibonacci import generate_fibonacci


def main():
    if len(sys.argv) != 2:
        print("Usage: python cli.py <limit>", file=sys.stderr)
        sys.exit(1)

    try:
        limit = int(sys.argv[1])
    except ValueError:
        print("Error: limit must be an integer", file=sys.stderr)
        sys.exit(1)

    sequence = generate_fibonacci(limit)
    print(",".join(map(str, sequence)))


if __name__ == "__main__":
    main()
