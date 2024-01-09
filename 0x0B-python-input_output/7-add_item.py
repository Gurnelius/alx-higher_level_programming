#!/usr/bin/python3
'''
    Add all arguments to a python list
    and save them to file.
'''


import os
save = __import__("5-save_to_json_file").save_to_json_file
load = __import__("6-load_from_json_file").load_from_json_file


def save_args(filename, argv=[]):
    """
    Appends command-line arguments to a list
    and saves it to a file.

    Parameters:
        filename (str): The name or path of the
            file to save the list.
        argv (list, optional): A list of command-line arguments.
        Default is an empty list.

    Returns:
        list: The combined list of existing content and new arguments.

    Raises:
        None
    """
    _list = []
    if not os.path.isfile(filename):
        save(_list, filename)
    if argv:
        _list = load(filename)

        [_list.append(x) for x in argv]

        save(_list, filename)
    return _list


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        save_args("add_item.json", sys.argv[1:])
    else:
        save_args("add_item.json")
