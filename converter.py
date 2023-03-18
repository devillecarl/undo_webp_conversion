import os
import shutil

def remove_extra_extensions(file_name):
    extensions = ['.jpg', '.jpeg', '.png', '.svg']
    for ext in extensions:
        if ext in file_name:
            return file_name.split(ext, 1)[0] + ext
    return file_name

def rename_files_in_folder(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for file_name in filenames:
            original_file_path = os.path.join(dirpath, file_name)
            new_file_name = remove_extra_extensions(file_name)
            new_file_path = os.path.join(dirpath, new_file_name)
            
            if original_file_path != new_file_path:
                shutil.move(original_file_path, new_file_path)
                print(f"Renamed {original_file_path} to {new_file_path}")

if __name__ == "__main__":
    root_folder = os.path.dirname(os.path.abspath(__file__))
    print(f"Using root folder: {root_folder}")
    rename_files_in_folder(root_folder)
