import main as main
import random

output = ""
prev_data = False
key = 0
count = 0

running = True
while running is True:
    ci = input("what would you like to do, encrypt(e), decrypt(d), encode(ec), decode(dc), access file(af) or stop(stop)")
    ci = ci.lower()

    #enc
    if ci == "e":
        key = "2"
        hi2 = ""
        if prev_data is True:
            ci = input("previous data has been found, would you like to use that? (y/n) ")
            ci = ci.lower()
        if ci == "y": hi = output
        if ci != "y": hi = input("please type in what you wish to encode-")
        for item in hi:
            hi4 = ""
            hi3 = main.inc(ord(item),count,key)
            hi3 = str(hi3[0])
            passes = 0
            while passes != 8:
                hi4 = hi4 + hi3[passes]
                passes = passes + 1
            hi2 = str(hi2) + str(hi4)
        print(hi2)
        output = hi2

    #denc
    if ci == "d":
        key = "1"
        if prev_data is True:
            ci = input("previous data has been found, would you like to use that? (y/n) ")
            ci = ci.lower()
        if ci == "y": hii = output
        if ci != "y": hii = input("please type in what you wish to decode-")
        hii3 = ""
        hii2 = ""
        count = 0
        for item in str(hii):
            if count != 8:
                hii2 = hii2 + item
                count = count + 1
            if count == 8:
                count = 0
                hii2 = [*hii2]
                hii2.append(3)
                hii2 = [int(i) for i in hii2]
                counts = ''.join(str(e) for e in hii2)  
                hii3 = hii3 + (main.inc(counts,hii2,key)[0])
                hii2 = ""
        print(hii3)
        output = hii3

    if ci == "ec":
        if prev_data is True:
            ci = input("previous data has been found, would you like to use that? (y/n) ")
            ci = ci.lower()
        if ci == "y": number = output
        if ci != "y": number = input("please type in what you wish to encrypt- ")
        number = main.enc(number)
        number = number[0]
        print ("key- ",number[0])
        print ("output- ",number[1])
        output = number[1]

    if ci == "dc":
        if prev_data is True:
            ci = input("previous data has been found, would you like to use that? (y/n) ")
            ci = ci.lower()
        if ci == "y": number = output
        if ci != "y": number = input("please type in what you wish to decrypt- ")
        key = input("please input your key in the form (n n n)- ")
        out = main.decrypt(key, number)
        print(out[0])
        output = out[0]

    if ci == "af":
        ci = input("would you like to open a file(o) or write to one?(w)")
        ci = ci.lower()
        
        if ci == "o":
            #opening a file
            answer2 = input("please input the name of your file including the file extension")
            answer2 = "input/" + str(answer2)
            taskfile = open(answer2,"r")
            task_data = taskfile.read()
            taskfile.close()
            output = task_data

        #writing to a file
        if ci == "w":
            if prev_data is True:
                answer2 = input("what would you like to name your file including file extenstion? ")
                answer2 = "output/" + str(answer2)
                taskfile = open(answer2,"w")
                taskfile.write(str(output))
                taskfile.close()
            if prev_data is not True: print("you do not have any data to write to a file")

        

    if ci == "stop":
        running = False
        print("byeeeeeee")

    if output != "":
        prev_data = True
    else: prev_data = False
