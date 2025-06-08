import os

def directory_watcher():
    for folder_name, sub_folder_names, file_names in os.walk("marvellous"):
        print("Folder name is ", folder_name)
        for sub_folder in sub_folder_names:
            print("Sub-folder name is ", sub_folder)
        for file_name in file_names:
            print("File name is ", file_name)


def main():
    directory_watcher()


if __name__ == "__main__":
    main()
