#!/usr/bin/python3
import os

if __name__ == "__main__":
    stdout_fd = 1
    text = "#pythoniscool\n"

    stdout_file = os.fdopen(stdout_fd, 'w')

    stdout_file.write(text)

    stdout_file.close()
