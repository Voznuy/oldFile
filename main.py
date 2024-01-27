import os
import time


def delete_old_files_and_empty_dirs(directory, days=15):
    current_time = time.time()

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if os.path.isfile(item_path):
            file_mtime = os.path.getmtime(item_path)
            time_difference = current_time - file_mtime
            if time_difference > days * 24 * 3600:
                os.remove(item_path)
                print(f"Видалено файл: {item_path}")
        elif os.path.isdir(item_path):
            delete_old_files_and_empty_dirs(item_path, days)

    if not os.listdir(directory):
        os.rmdir(directory)
        print(f"Видалено порожню папку: {directory}")


delete_old_files_and_empty_dirs('/home/admin228a/Videos', days=15)
