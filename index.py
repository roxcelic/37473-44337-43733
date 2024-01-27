#impots extra/test.py to get access to its functions
import extra.test as enc
import extra.dectrypt as dec
#imports the primary dictionary
from data.basic import words_lol as dic

data = ""
running = True
file_data = False
task_data = ""
output =  ""

enc.data_check()
#enc.list_dict()

while running is True:
    ci = input("what would you like to do, encode(e), decode(d), access file(af) or stop(stop): ")
    ci = ci.lower()

    if ci == "af":
        ci = input("would you like to open a file(o) or write to one?(w)")
        ci = ci.lower()
        if ci == "o":
            #opening a file
            answer2 = input("please input the name of your file including the file extension")
            answer2 = "data/input/" + str(answer2)
            taskfile = open(answer2,"r")
            task_data = taskfile.read()
            taskfile.close()
            output = task_data

        #writing to a file
        if ci == "w":
            if file_data is True:
                answer2 = input("what would you like to name your file including file extenstion? ")
                answer2 = "data/output/" + str(answer2)
                taskfile = open(answer2,"w")
                taskfile.write(str(output[0]))
                taskfile.close()
            if file_data is not True: print("you do not have any data to write to a file")

    if ci == "e":
        if file_data is True:
            ci = input("there is previous data in this script, would you like to use that? (y/n): ")
            ci = ci.lower()
            if ci == "y": data = output
            if ci == "n": data = input("what would you like to encode?")
        else: data = input("what would you like to encode?")
        output = dec.encode(data)
        print(output[0])
    if ci == "d":
        if file_data is True:
            ci = input("there is previous data in this script, would you like to use that? (y/n): ")
            ci = ci.lower()
            if ci == "y": data = output
            if ci == "n": data = input("what would you like to decode?")
        else: data = input("what would you like to decode?")
        output = dec.decode(str(data[0]))
        print(output[0])

    if output != "":
        file_data = True
        
    if ci == "stop":
        running = False
