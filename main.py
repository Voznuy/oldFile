import os
import datetime


def remove_old_files_and_empty_folders(directory_path, days_threshold=10):
    current_time = datetime.datetime.now()
    threshold = current_time - datetime.timedelta(days=days_threshold)


    def remove_empty_folders(folder):
        try:
            for item in os.listdir(folder):
                item_path = os.path.join(folder, item)
                if os.path.isdir(item_path):
                    remove_empty_folders(item_path)
            if not os.listdir(folder):
                os.rmdir(folder)
                print(f"Folder {folder} deleted")
        except Exception as e:
            print(f"Error delete folder {folder}: {e}")
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if os.path.isfile(file_path):
            last_modified_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
            if last_modified_time < threshold:
                try:
                    os.remove(file_path)
                    print(f"File {filename}deleted")
                except Exception as e:
                    print(f"Error deleted file {filename}: {e}")
    remove_empty_folders(directory_path)


directory_path = "/home/admin228a/Videos"
remove_old_files_and_empty_folders(directory_path)
