import os
import hashlib

def main():
    print("Entr file name")
    file_name = input()

    fobj = open(file_name, 'rb')
    hobj = hashlib.md5()

    buffer = fobj.read(1024)
    while(len(buffer)>0):
        hobj.update(buffer)
        buffer = fobj.read(1024)

    fobj.close()
    print("Checksum of file is ", hobj.hexdigest())

if __name__ == "__main__":
    main()