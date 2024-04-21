import os

def get_all_files(root_folder: str, file_list: list, ext: str=None):
    """
    Find all files in folder and it's subfolders.

    Parameters:
        root_folder (str): Start folder
        file_list (list): Empty list where we collect the files
        ext (str) optional: Extension filter    
    """
    
    # Check if root_folder is valid
    assert os.path.isdir(root_folder), f"root_folder is not valid: {root_folder}"

    # Check if file_list is a list
    assert isinstance(file_list, list), f"file_list must be of type list and not {type(file_list)}"

    # get all content from root_folder
    folder_content = os.listdir(root_folder)

    subfolders = []

    for i in folder_content:
        full_path = os.path.join(root_folder, i)

        if os.path.isfile(full_path):
            file_list.append(full_path)
        else:
            subfolders.append(full_path)
    
    for folder in subfolders:
        get_all_files(folder, file_list, ext)