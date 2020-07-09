
from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 

    now = datetime.now()

    #### Date Formatting ####

    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month

    # print(now.strftime("The current year is: %Y"))  # output: The current year is: 2020
    # print(now.strftime("%a, %d %B, %y"))      # output: Wed, 08 July, 20
    # print(now.strftime("%a, %d %b, %y"))      # output: Wed, 08 Jul, 20
    # print(now.strftime("%A, %d %B, %Y"))      # output: Wednesday, 08 July, 2020
    # print(now.strftime("%D"))      # output: 07/08/20


    # %c - locale's date and time, %x - locale's date, %X - locale's time

    # print(now.strftime("Local date and time: %c"))
    # print(now.strftime("Local date: %x"))
    # print(now.strftime("Local time: %X"))


    #### Time Formatting ####

    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM

    print(now.strftime("Current time: %I:%M:%S %p"))  # 12 hour format
    print(now.strftime("24-hour time: %H:%M:%S"))     # 24 hour format



if __name__ == "__main__":
  main()
