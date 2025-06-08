import os

def directory_watcher(dir_name):
    for folder_name, sub_folder_names, file_names in os.walk(dir_name):
        print("Folder name is ", folder_name)
        for sub_folder in sub_folder_names:
            print("Sub-folder name is ", sub_folder)
        for file_name in file_names:
            print("File name is ", file_name)


def main():
    print("Enter the name of the directory that you want to traverse : ")
    dir_name = input()
    directory_watcher(dir_name)


if __name__ == "__main__":
    main()
