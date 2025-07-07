import sys
try:
    if len(sys.argv) != 2:
        raise Exception("python3 main.py <path_to_book>")
except Exception as e:
    print(f"program is used as follows: {e}")
    sys.exit(1)

