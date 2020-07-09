
from datetime import date
from datetime import time
from datetime import datetime

def main():
    # date

    # today = date.today()
    # print("Today's date is ", today)

    # print("Date components: ", today.day, today.month, today.year)

    # print("Today's week is:", today.weekday())

    # day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # print("Today's week is:", day[today.weekday()])

    # datetime

    today = datetime.now()
    print("The current date and time is: ", today)


    # time

    t= datetime.time(datetime.now())
    print("The current time is: ", t)


if __name__ == '__main__':
    main()