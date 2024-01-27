def encode(data):
    #importing the primary dictionary
    import random as ran
    from data.basic import hex as dic2
    from data.basic import words_lol as dic
    import extra.dectrypt as dec
    #data
    reprint = ""
    num = dec.incrypt()
    key1 = dec.incrypt2()
    keydata = ran.randint(1,9)
    keydata2 = keydata
    key1 = str(key1[0])
    for item in key1:
        keydata = keydata * int(dic2[str(item)])
    for item in data:
        key = next(key for key, value in dic.items() if value == item)
        key = key - int(num[0])
        key = key + int(keydata)
        reprint =  reprint + str(key)
        key = ""
    print("key",num[0],key1,keydata2)
    return [reprint]

def decode(data):
    from data.basic import words_lol as dic
    import extra.dectrypt as dec
    reprint = ""
    count = 0
    comp = ""
    ans = dec.decrypt()
    for item in data:
        if count != 8:
            comp = comp + item
            count = count + 1
        if count == 8:
            ans2 = ans[0]
            comp = int(comp) + int(ans2[0])
            comp = int(comp) - int(ans2[1])
            reprint = reprint + str(dic[int(comp)])
            count = 0
            comp = ""
    return [reprint]

def incrypt():
    key1 = ""
    key3 = ""
    import random as ran
    from data.basic import hex as dic
    ans = ran.randint(1,3)
    while ans != 0:
        item = ran.randint(0,15)
        item = str(item)
        key = next(key for key, value in dic.items() if value == item)
        key1 = key1 + str(key)
        ans = ans - 1
    key2 = ran.randint(1,9)
    a = 8
    while a != 0:
        key3 = key3 + str(ran.randint(0,2))
        a = a - 1
    keydata = key2
    for item in key1:
        keydata = keydata * int(dic[str(item)])
    return[key3]

def incrypt2():
    key1 = ""
    key3 = 0
    import random as ran
    from data.basic import hex as dic
    ans = ran.randint(1,3)
    while ans != 0:
        item = ran.randint(0,15)
        item = str(item)
        key = next(key for key, value in dic.items() if value == item)
        key1 = key1 + str(key)
        ans = ans - 1
    key2 = ran.randint(1,9)
    a = 8
    while a != 0:
        key3 = key3 + ran.randint(1,3)
        a = a - 1
    keydata = key2
    for item in key1:
        keydata = keydata * int(dic[str(item)])
    return[key1]

def decrypt():
    from data.basic import hex as dic2
    ci = input("please input your key in the format (n n n): ")
    ci = ci.split(" ")
    keydata = ci[2]
    for item in ci[1]:
        keydata = int(keydata) * int(dic2[str(item)])
    ci[0] = ci[0]
    ci[1] = keydata
    return[ci]
