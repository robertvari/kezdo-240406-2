from my_functions.file_utils import get_all_files

folder_path = r"D:\Work\PythonSuli\kezdo-240406\alapok_2\test_folder"
my_files = []
get_all_files(folder_path, my_files, ext="jpg")