import threading
import time
import os


def create_folders():
    folders = ["data", "logs", "output"]
    for folder in folders:
        root = os.path.join(os.getcwd(), '..',folder)
        os.makedirs(root, exist_ok=True)


def create_files():
    files = ["data/input.txt", "logs/log.txt", "output/result.txt"]
    for file in files:
        root = os.path.join(os.getcwd(), '..', file)
        with open(root, 'w') as f:
            f.write(f"This is the {file} file.\n")

if __name__ == "__main__":
    make_folders = threading.Thread(target=create_folders)
    make_files = threading.Thread(target=create_files)
    make_folders.start()
    make_folders.join()
    make_files.start()
    make_files.join()
    print("Folders and files created successfully.")

