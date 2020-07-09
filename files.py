
def main():  
    # Open a file for writing and create it if it doesn't exist

    # file = open("textfile.txt", "w+")  # w gives write access. + creates new file if it doesn't exist. 


    # Open the file for appending text to the end

    # file = open("textfile.txt", "a")     # a means append data to end of the file instead of overwriting the existing content.
    file = open("textfile.txt", "r")     # r gives read access.


    # write some lines of data to the file

    # for i in range(10):
    #     file.write("This is line " + str(i) + "\r\n" )


    # close the file when done

    # file.close()


    # Open the file back up and read the contents

    if file.mode == 'r':
        # contents = file.read()  # reads the entire file and prints it
        # print(contents)

        fl = file.readlines()  # reads the file line by line
        for x in fl:
            print(x)

if __name__ == "__main__":
  main()