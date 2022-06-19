import time
import os
import shutil

def main():
    deleted_folders = 0
    deleted_files = 0
    path = "path_to_delete"
    days = 30
    seconds = time.time() - (days * 24 * 60 * 60)


    if os.path.exists(path):
        for root_folder, files, folders in os.walk(path):
            if seconds >= age_of_file_or_folder(root_folder):
                remove_folder(root_folder)
                deleted_folders += 1
                break

            else:
                for folder in folders:
                    folder_path = os.path.join(root_folder, folder)
                    if seconds >= age_of_file_or_folder(folder_path):
                        remove_folder(folder_path)
                        deleted_folders += 1

                for file in files:
                    file_path = os.path.join(root_folder, file)
                    if seconds >= age_of_file_or_folder(file_path):
                        remove_file(file_path)
                        deleted_files += 1
        else:
            if seconds >= age_of_file_or_folder(path):
                remove_file(path)
                deleted_files += 1
    
    else:
        print(f'"{path}" is not found')
        deleted_files += 1

    print(f"Folders Deleted: {deleted_folders}")
    print(f"Files Deleted: {deleted_files}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} has been removed")
    else:
        print("Cannot delete the path: " + path)
    
def remove_file(path):
    if not os.remove(path):
        print(f"{path} has been removed")
    else:
        print("Cannot delete the path: " + path)

def age_of_file_or_folder(path):
    ctime = os.stat(path).st_ctime
    return ctime

if __name__ == '__main__':
    main()
        

