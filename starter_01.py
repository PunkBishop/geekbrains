import os


def create_parent(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        print(f'Родительская папка уже существует: {FileExistsError.filename}')
    return 0


def create_child(parent, *dirs):
    for el in dirs:
        try:
            directory = os.path.join(parent, el)
            os.mkdir(directory)
        except FileExistsError:
            print(f'Родительская папка уже существует: {FileExistsError.filename}')
    return 0


def starter(main):
    create_parent(main)
    create_child(main, 'settings', 'mainapp', 'adminapp', 'authapp')


parent_dir = 'Starter_dir'
if __name__ == '__main__':
    starter(parent_dir)
