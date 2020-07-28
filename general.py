import os;


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Directory Created')
        os.makedirs(directory)


create_project_dir("the_new_crawler")