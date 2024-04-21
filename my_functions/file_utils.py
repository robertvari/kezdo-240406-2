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

    pass