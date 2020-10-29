def removeKeys(mydict, keylist):
    for i in keylist:
        if i in mydict:
            mydict.pop(i)
    return mydict


if __name__ == "__main__":
    dict = {"car": "civic", "year": "2020", "color": "white"}
    print(dict)
    remove_keys = input("Input the keys to remove: ").split(" ")
    print(removeKeys(dict, remove_keys))


