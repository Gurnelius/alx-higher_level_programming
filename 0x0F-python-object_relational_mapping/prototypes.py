#!/usr/bin/env python3

import sys
import re

# Check if file name is provided as argument
if len(sys.argv) != 2:
    print("Usage: {} <filename>".format(sys.argv[0]))
    sys.exit(1)

# Get the file name from command line argument
filename = sys.argv[1]

try:
    # Open the file
    with open(filename, 'r') as file:
        # Read the content of the file
        content = file.read()

        # Find function prototypes using regular expression
        prototypes = re.findall(r'(?<=Prototype:\s).*', content)

        if prototypes:
            # Append prototypes to binary_trees.h
            with open("binary_trees.h", 'a') as output_file:
                for prototype in prototypes:
                    output_file.write(prototype + '\n')
        else:
            print("No function prototypes found in the file.")

except FileNotFoundError:
    print("File not found:", filename)
    sys.exit(1)

