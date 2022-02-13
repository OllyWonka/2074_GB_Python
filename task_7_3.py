import sys
import os
import shutil

main_path = sys.argv[1]
my_files = [os.path.relpath(os.path.join(root, file), main_path) for
root, _, my_files in os.walk(main_path) for file in my_files if
file.endswith('.html')]
for my_path in my_files:
    path, file = os.path.split(my_path)
    test_path = os.path.join(main_path, 'templates', path)
    if not os.path.exists(test_path):
        os.makedirs(test_path)
    shutil.copyfile(os.path.join(main_path, my_path),
os.path.join(test_path, file))

