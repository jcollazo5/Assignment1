# Jennifer Collazo-Assignment 7B

#loop
def getValues(word):
    while word != '':
        word = word.replace(',', '') #remove commas
        word = word.replace(' ', '') #remove spaces
        word = word.lower() #turn string into all lower cases
        for i in range(len(word)):
            if word[i] == word[len(word)-1-i]:
                continue
            else:
                print("That's not a palindrome")
                break
        else:
            print("That's a palindrome")
        word =input(str('Please enter a word or phase, or <return> to quit: '))
        
#get inputs
word = input(str('Please enter a word or phase, or <return> to quit: '))
word = getValues(word)

