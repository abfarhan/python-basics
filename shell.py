
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    # src = path.realpath("textfile.txt")
    
    # let's make a backup copy by appending "bak" to the name
    # dst = src + ".bak"

    # copy over the permissions, modification times, and other info
    # shutil.copy(src, dst)    # copy fn copies only the content of the file
    # shutil.copystat(src, dst)    # copystat fn copies the metadata of the file

    # rename the original file
    # os.rename("textfile.txt","newfile.txt")

    # now put things into a ZIP archive
    # root_dir, tail = path.split(src) 
    # print(root_dir)
    # print(tail)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")

      
if __name__ == "__main__":
  main()
