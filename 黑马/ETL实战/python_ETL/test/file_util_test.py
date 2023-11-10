
import os

print(os.listdir('./test_dir'))

path_list = []

for file_name in os.listdir('./test_dir'):
    file_path = os.path.join('./test_dir', file_name)
    abs_path = os.path.abspath(file_path)
    
    if os.path.isfile(file_path):
        path_list.append(abs_path)

print(path_list)
