

def main():
    x = 0

    # while loop

    # while (x < 5):
    #     print(x)
    #     x = x + 1

    # for loop

    # for x in range(5, 10):
    #     print(x)

    # for loop over a collection

    # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # for d in days:
    #     print(d)

    # break statement

    # for x in range(5, 10):
    #     if (x == 7): break
    #     print(x)

    # continue statement

    # for x in range(5, 10):
    #     if (x == 7): continue
    #     print(x)

    # using enumerate() function to get index
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i,d in enumerate(days):      
        print(i, d)

    # The enumerate() iterate over the collection like loop normally but in addition to returning 
    # the value of the item , it also returns the index of the item.


main()
