'''
This program splits creates dictionary entries for each black listed word. each
entry is assigned a word, and the 2 corresponding probabilities.
'''
# Split the blacklist into lines.
blacklist = open("Blacklist.txt").read().splitlines()
# for counting how many times a word appears in a given message
# importing libraries
import string
import collections




def splitInWords(message):
    global arrayOfCount
    arrayOfCount = []
    global arrayOfWords
    arrayOfWords = []
    global keeepingTrackOfWords
    keeepingTrackOfWords = []
    global arrayOfChars
    arrayOfChars = []
    global index
    global isTheWordFound
    global b
    global a
    a = []
    isTheWordFound = False
    index = 0

    # initialise arrays so that i first get the words letter by letter
    # when i find a space, I stop and add the full word to the array of
    # words. In the end, I call a method that counts how many times a word
    # appears and counts them individualy

    for word in message:
        if word != ' ':
            arrayOfChars.append(word)
            isTheWordFound = False
        elif word == ' ':
            b = string.join(arrayOfChars, '')
            keeepingTrackOfWords.append(b)
            for i in range(index):
                if arrayOfWords[i] == b:
                    isTheWordFound= True

                    arrayOfChars = []
                    break

            if isTheWordFound == False:
                arrayOfWords.append(b)
                index += 1
                arrayOfCount.append(1)
                arrayOfChars = []

    # I also clear the array of chars, for being able to create a new word


    a = string.join(a, ' ')
    a = collections.Counter(keeepingTrackOfWords)
    # print a, which represents the array where it says how many times
    # each word appears

# the only issue with the message is that for taking the final word, it needs
# a space after it



# documentation: https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list

# An empty list to store each dictionaries of blacklisted words.
dictlist = []

# Split each lines by tabs.
for element in blacklist:
    key = element.split('\t')
    #dict = {'Word':key(0),'Proba1':key(1),'Proba2':key(2)}
    dictlist.append({'Word':key[0],'Proba1':key[1],'Proba2':key[2]})
    print key      #Remove the comment to see each individual lines.

print dictlist     #Remove the comment to see the array nof dictionaries

# Test with user input.
message = raw_input('Enter message here: ')
message = message + ' '
splitInWords(message)
for word in a.keys():
    for entry in dictlist:
        if word == entry['Word']:
            print entry['Word'], entry['Proba1']
