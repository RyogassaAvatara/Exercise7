def findvalue(mydict, val):
    key = []
    for i in mydict:
        if val in mydict[i]:
            key.append(i)
    return key


if __name__ == "__main__":
    dict = {"John": "Good", "Bruno": "Bad", "idk": "Neutral"}
    userInput = input("Pick a value of key: ")
    print(findvalue(dict, userInput))
