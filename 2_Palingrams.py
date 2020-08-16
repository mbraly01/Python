import string

#returns whether or not a string is a palingram
def is_palingram(palingram):
    #removes spacing, punctuation, and lowercases everything
    palingram = palingram.replace(' ','')
    palingram = palingram.lower()
    palingram = palingram.translate(palingram.maketrans("","", string.punctuation))
    #runs through the word until it gets to the middle
    #checks letters for palingram
    for i in range(len(palingram)):
        if i <= len(palingram)-1-i:
            if palingram[i] == palingram[len(palingram)-1-i]:
                if i == len(palingram) - 1 - i:
                    break
            else:
                return False
        else:
            break
    return True

word = '1hello ol Le.h1'
print(is_palingram(word))