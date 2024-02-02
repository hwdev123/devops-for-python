import os
from common.functions import get_user_input

def change_directory(path):
    """
    Change the current working directory to the given path.   

    Parameters:
    - path (str): The path to change to.

    Raises:
    - OSError: If an error occurs during directory change.
    """
    if not os.path.isdir(path):
        print(f"The entered path '{path}' is not a valid directory.")
        return
    try:
        os.chdir(path)
        print(f"Changed into the directory: {os.getcwd()}")
    except OSError as e:
        if isinstance(e, PermissionError):
            print(f"The path {path} does not exit.")
        elif isinstance(e, FileNotFoundError):
            print(f"You do not have the permissions to access the path: {path}")
        else:
            print("Error while changing into directory: {e}")


if __name__ == '__main__':
    try:
        path = get_user_input()
        change_directory(path)
    except KeyboardInterrupt:
        print("\nProgram interupted. Exiting...")
