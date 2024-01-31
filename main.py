import main as main
import random

def inc(num,count2,key):
    count = [3,3,3,3,3,3,3,3,3]
    item = 7
    passing = 0
    end = False

    while end is False:
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
        passing = passing + 1
        
        if key == "1":
            if count == count2:
                end = True
                return[chr(passing)]
            if count == [7,7,7,7,7,7,7,7,3]:
                raise TypeError("sorry but there was no room for characters past:", chr(passing))
                end = True
                
        if key == "2":
            if passing == num:
                number = ''.join(str(e) for e in count)
                number = int(number)
                return[number]
                end = True

def enc(number):
    boop = 1
    key1 = ""
    key2 = ""
    out = ""
    key3 = ""
    passing = 0
    count = 0
    number2 = ""
    num = ""
    while passing != 8:
        key1 = key1 + str(random.randint(0,2))
        passing = passing + 1
    key2 = random.randint(1,9)
    passing = 0
    while passing != 5:
        keydata = random.randint(0,15)
        key3 = key3 + str(main.hexs[keydata])
        boop = boop * keydata
        passing = passing + 1
    boop = boop * key2
    for item in number:
        if count != 8:
            count = count + 1
            num = str(num) + str(item)
        if count == 8:
            num = int(num) - int(key1)
            num = num + boop
            number2 = number2 + str(num)
            count = 0
            num = ""
    keys = str(key1) + " " + str(key2) + " " + str(key3)
    out = list(out)
    out.append(keys)
    out.append(number2)
    return[out]

def decrypt(keys, number):
    key5 = 1
    keys = keys.split(" ")
    key1 = keys[0]
    key2 = keys[1]
    key3 = keys[2]
    count = 0
    number2 = ""
    num = ""
    for item in key3:
        key4 = next(key4 for key4, value in main.hexs.items() if value == item)
        key5 = key5 * key4
    key2 = int(key5) * int(key2)
    for item in str(number):
        if count != 8:
            count = count + 1
            num = str(num) + str(item)
        if count == 8:
            count = 0
            num = int(num) - int(key2)
            num = num + int(key1)
            number2 = str(number2) + str(num)
            num = ""
    return[number2]

hexs = {
    0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "a",
    11 : "b",
    12 : "c",
    13 : "d",
    14 : "e",
    15 : "f"
    }
