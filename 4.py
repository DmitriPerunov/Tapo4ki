import os

current_path = os.path.abspath(__file__)

parent_path = os.path.join(current_path, '..')

print(current_path)
print(parent_path)

def get_all_files(path):
    for i_name in os.listdir(path):
        new_path = os.path.join(path, i_name)
        if os.path.isdir(new_path):
            print('Папка', i_name)
            get_all_files(new_path)
        №else:
            print('-', i_name)

get_all_files(parent_path)
