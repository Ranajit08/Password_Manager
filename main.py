import csv
import sys
from parser import parser


def main():
    if len(sys.argv) == 2:
        mainloop(sys.argv[1])
    else:
        sys.exit("Error: no commands.")

def mainloop(file: str) -> None:
    try:
        with open(f"{file}.csv", 'w') as f:
            writer = csv.DictWriter(f, fieldnames=["site", "username", "password"])
            writer.writeheader()
    except FileNotFoundError:
        sys.exit(":( Some problems occurs.")
    parser(file)

if __name__ == "__main__":
    main()