# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os

def split_file_path(file_path):
    dir_path, file_name = os.path.split(file_path)
    file_name_without_ext, file_extension = os.path.splitext(file_name)
    return dir_path, file_name_without_ext, file_extension

file_path = "/Path/tomy/files/test.sln"
path, name, extension = split_file_path(file_path)
print("Путь:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)