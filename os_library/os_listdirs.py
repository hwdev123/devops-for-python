import os
from os_library.functions import get_user_input

def change_directory(path):
    """
    Lists the working directory to the given path.   

    Parameters:
    - path (str): The path to change to.

    Raises:
    - OSError: If an error occurs during directory change.
    """
    
    os.listdir(path)

