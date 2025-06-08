import sys
import time

def create_log():
    timestamp = time.ctime()
    
    file_name = "MarvellousLog%s.log"%(timestamp)
    file_name = file_name.replace(" ", "_")
    file_name = file_name.replace(":", "_")

    folder_name = "marvellous_logs"
    os.

    fobj = open(file_name, "w")

    border = "-"*80
    fobj.write(border+"\n")
    fobj.write("This is a log file of Marvellous Automation script.\n")
    fobj.write(border+"\n")

    fobj.write("\n\n\n\n\n")
    fobj.write(border+"\n")
    fobj.write("This file was created at : \n" + timestamp + "\n")
    fobj.write(border)
    fobj.close()

def main():
    create_log()

if __name__ == "__main__":
    main()
