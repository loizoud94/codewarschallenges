def spin_words(sentence):
    list1 = sentence.split()
    list2 = []
    for word in list1:
        if len(word) > 4:
            word = word[::-1]
        list2.append(word)
    sentence2 = " ".join(list2)
    
    return sentence2
