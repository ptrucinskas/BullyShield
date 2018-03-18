import string
import collections
import os

'''
For now this program reads through the user terminal input and compares it with
a random blacklist that I made. The probabilities would need to be altered once
we determine the correct probabilities for each word (Google?).
The main problem for now is that it cannot detect the same word twice in a
message and counts it as 1 occurence and only conducts the bayes fonction for
that word once.
The required fixes would therefore be to impliment it with our blacklist, to
connect it with the chat, to fix the word frequency problem and
to determine the probabilities.
- Steeve & Teodor.
'''


dictList = []

def bayes_main(chat_message):
  split_to_lines()
  splitInWords(chat_message)
  return main(chat_message)



def split_to_lines():
  script_dir = os.path.dirname(__file__)
  rel_path = "../Data/Blacklist.txt"
  abs_file_path = os.path.join(script_dir, rel_path)
  blacklist = open(abs_file_path).read().splitlines()
# An empty list to store each dictionaries of blacklisted words.
  
# Split each lines by tabs.
  for element in blacklist:
      key = element.split('\t')
      #dict = {'Word':key(0),'Proba1':key(1),'Proba2':key(2)}
      dictList.append({'Word':key[0],'Proba1':key[1],'Proba2':key[2]})
      #print key  
  return dictList
   


def splitInWords(message):
    arrayOfCount = []
    arrayOfWords = []
    keeepingTrackOfWords = []
    arrayOfChars = []
    index = 0
    isTheWordFound = False
    b = ""
    global a 
    a= {}

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

'''
Calculate the probability of a message being a bully message using bayes.
The probabilities aren't final as we would have to assign as probability to each
word but for now I have:
P(BullyMessage) = 0.5
P(Word) = 0.6
P(Word|BullyMessage) = 0.7
'''
PBully = 0.5
# This is the main score counter that goes up everytime a message is flagged.
score = 0
def bayes(word, probability):
    # These will later get the probability of the given word from a text file
    # or the database
    PWord = 0.4
    PWordBully = probability

    global PBully
    PBully = (PWordBully * PBully) / PWord
    return PBully



# Read the message and compare it with the blacklist.
def message(chat_message):
    global PBully
    global score
    global Message
    global position
    Message = chat_message
    splitInWords(Message)
    # Goes through the blacklist and checks if the word is in the message.
    for word in a.keys():
        position = a.keys().index(word)
        for entry in dictList:
            if word == entry['Word']:
                index = a.values()[position]
                for i in range(index):
                    bayes(word, float(entry['Proba1']))

                if PBully > 0.3:
                    print "This is message has been flagged!"
                    score = score + 1

    # Prints out the probability after each message to demonstrate the bayes
    # function on every message even the non flagged messages.
    print PBully
    # Reset the probability fo the next message.
    PBully = 0.5
# This will keep accepting messages until the main score count surpasses 5.
def main(chat_message):
   # while score < 5:
        message(chat_message)
        print score
        return score
        


