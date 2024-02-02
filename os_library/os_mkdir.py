import os

def create_directory(path):
        os.makedirs(path, mode=0o644)
        print(f"Directory created: {path}")
        
def get_user_input():
    return input("Enter the name of your path: ")


if __name__ == '__main__':
    path = get_user_input()
    create_directory(path)

    