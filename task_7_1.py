import os

my_directory = os.path.dirname(os.path.abspath(__file__))


def my_dir(my_directory, firstly):
    for key, val in firstly.items():
        main_folder = os.path.join(my_directory, key)
        if not os.path.exists(main_folder):
            os.mkdir(main_folder)
        for i in val:
            main_folder = os.path.join(my_directory, key, i)
            if not os.path.exists(main_folder):
                os.makedir(main_folder)


firstly = {'my_project': ['settings', 'main', 'admin',
                          'auth']}
if __name__ == '__main__':
    my_dir(my_directory, firstly)
