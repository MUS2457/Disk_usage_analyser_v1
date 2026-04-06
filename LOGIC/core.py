import os

def scan_folder_subfolder(folder_path):
    files_paths = []

    for item in os.listdir(folder_path):

        current_path = os.path.join(folder_path, item)

        if os.path.isfile(current_path):
            files_paths.append(current_path)

        elif os.path.isdir(current_path):
            sub_files = scan_folder_subfolder(current_path)  # call fc instead of writing same code, the fc only equal above so it returns a list
            files_paths.extend(sub_files)

    return files_paths


