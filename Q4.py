def word_frequencies(mylist):
    dict = {}
    for i in mylist:
        if i not in dict.keys():
            dict[i] = 1
        elif i in dict.keys():
            dict[i] = dict[i] + 1
    return dict


if __name__ == "__main__":
    words = ["happy", "sad", "ok", "sad", "ok", "meh", "ok", "happy"]
    print(word_frequencies(words))