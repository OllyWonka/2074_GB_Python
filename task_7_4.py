import os
import sys

size = {}


def test_folder(my_directory):
    if not os.path.exists(my_directory):
        return
    with os.scandir(my_directory) as my_files:
        for file in my_files:
            if os.path.isfile(file):
                my_file = 10 ** len(str(os.stat(file).st_sizet))
                size[my_file] = size.get(my_file, 0) + 1
            elif os.path.isdir(file):
                test_folder(os.path.join(my_directory, file))


if __name__ == '__main__':
    my_directory = 'my_doc'
    print(test_folder(my_directory=my_directory))
