import os

def directory_watcher(dir_name = "marvellous"):
    flag = os.path.isabs(dir_name)

    if not flag:
        dir_name = os.path.abspath(dir_name)
    
    flag = os.path.exists(dir_name)
    if not flag:
        print("The path is invalid.")
        exit()

    flag = os.path.isdir(dir_name)
    if not flag:
        print("The is valid, but the target is not directory.")
        exit()

    print("Absolute path is ", dir_name)
    deleted_files = 0
    total_files = 0
    for folder_name, sub_folder_names, file_names in os.walk(dir_name):
        for file_name in file_names:
            total_files += 1
            if (os.path.getsize(os.path.join(folder_name, file_name) == 0)):
                print(f"File size of {file_name} is zero.")
                os.remove(os.path.join(folder_name, file_name))
                deleted_files += 1
    print(f"Deleted files({deleted_files})/Total files({total_files})")


def main():
    print("Enter the name of the directory that you want to traverse : ")
    dir_name = input()
    directory_watcher(dir_name)


if __name__ == "__main__":
    main()
