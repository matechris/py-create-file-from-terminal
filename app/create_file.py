import os
import sys
from datetime import datetime


def create_file() -> None:
    command = sys.argv

    if "-f" not in command:
        path = os.path.join(*command[2:])

        if not os.path.exists(path):
            os.makedirs(path)

        return

    path = ""

    if "-d" in command:
        path = os.path.join(*command[2:-2])

        if not os.path.exists(path):
            os.makedirs(path)

    file_name = os.path.join(path, command[-1])

    with open(file_name, "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_count = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                break

            file.write(f"{line_count} {content_line}\n")
            line_count += 1


if __name__ == "__main__":
    create_file()
