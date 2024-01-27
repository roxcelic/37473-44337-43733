#the goal of this function is to check if the primary dictionary has been eddited
def data_check():
    #imports the primary dictionary as 'dic'
    from data.basic import words_lol as dic
    #imports a pre saved clone of the primary dictionary as 'dic_check'
    from data.backup.basic import words_lol as dic_check

    #count is a list composed of 9 intigers as all of the character codes for this are 8 digits long and for some reason i was too tired to figure out it never added to the 9th
    count = [3,3,3,3,3,3,3,3,3]
    #item counts which one of the items in the 'count' list is being focused on
    item = 7
    #passing is a simple intiger made to count how many times it passes through (mostly for debug purposes)
    passing = 0
    #eddit is a boolean value which tells the code weather of not the dictionary has been eddited
    eddit = False

    #a simple for loop
    for row in dic:
        #this is so that on pass 0 it can start at 33333333 so that 0 is reigsetered as an item in the list and it keeps track with the for loop
        if passing != 0:
            #counting is another boolean value used to tell the code if its already changed a digit on this pass
            counting = True
            #a while loop that makes sure that it has not changed a digit yet
            while counting is True:
                #this is an if statment to check if the item in the list is equal to 3
                if count[item] == 3:
                    #this will turn the 3 into a 4 (the bits used in my encryption are [3,4,7]
                    count[item] = count[item] + 1
                    #checks if the item value isnt 8
                    if item != 8:
                        #sets it to 8
                        item = 8
                        #tells the script a list item has been changed
                        counting = False
                #does the same thing but for the number 4
                elif count[item] == 4:
                    count[item] = count[item] + 3
                    if item != 8:
                        item = 8
                        counting = False
                #does a similar thing for the number 7
                elif count[item] == 7:
                    count[item] = 3
                    if item != 0:
                        item = item - 1
                        #it never sets 'counting' to False so it will continue onto the next place down
                        
        #turns the list into a singular intiger
        number = str(count[0]) + str(count[1])+str(count[2])+str(count[3])+str(count[4])+str(count[5])+str(count[6])+str(count[7])
        number = int(number)

        #compares the two each pass
        if passing != 255:
            passing = passing + 1
            if dic[number] != dic_check[number]:
                eddit = True

    #gives you, your answer
    if eddit is True:
        print("the contense of the primary dictionary has been eddited, you may not get the desired results")
    if eddit is False:
        print("the primary dictionary is working as intended")

#this function just lists the items, it does all the same thing so will not need much annotation
def list_dict():
    from data.basic import words_lol as dic

    count = [3,3,3,3,3,3,3,3,3]
    item = 7
    passing = 0
    eddit = False

    for row in dic:
        if passing != 0:
            counting = True
            while counting is True:
                if count[item] == 3:    
                    count[item] = count[item] + 1
                    if item != 8:
                        item = 8
                        counting = False
                elif count[item] == 4:
                    count[item] = count[item] + 3
                    if item != 8:
                        item = 8
                        counting = False
                elif count[item] == 7:
                    count[item] = 3
                    if item != 0:
                        item = item - 1
            
        number = str(count[0]) + str(count[1])+str(count[2])+str(count[3])+str(count[4])+str(count[5])+str(count[6])+str(count[7])
        number = int(number)
        #prints the values that where given and recorded throughout its run time on every pass
        if passing != 255:
            print(passing,",",number,"=",dic[number])
            passing = passing + 1
