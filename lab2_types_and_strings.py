#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence
        print("first letter is {0} and last is {1}".format(message[0], message[-1]))

        # use slice notation
        print(message[:4])

        # escaping a character
        print("""He said “that’s fantastic”!""")

        # find all a's in the input word and count how many there are
        message = str(message)
        print ("the first occurrence of a is {0}th character and there are {1} total a's".format(message.find("a"),
                                                                                                 message.lower().
                                                                                                 count("a")))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        newMessage = message.replace("a", "-")
        print (newMessage)

        # printing only characters at even index positions
        for i in range(0, len(message), 2):
            print ("Index {0} is {1}".format(i, message[i]))

    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: " + message)

        # hand the input string to a list and print it out
        list = str(message).split()
        print (list)

        # append a new element to the list and print
        list.append("apple")
        print (list)
        # remove from the list in 3 ways
        list.remove("apple")
        print (list)

        print ("The popped value is {0}".format(list.pop()))
        print (list)

        del list[0]
        print (list)
        # check if the word cake is in your input list
        print ("cake" in list)

        # reverse the items in the list and print
        list.reverse()
        print (list)

        # reverse the list with the slicing trick
        list = list[::-1]
        print (list)

        # print the list 3 times by using multiplication
        print (list * 3)


tas = Types_and_Strings()
#tas.play_with_strings()
tas.play_with_lists()