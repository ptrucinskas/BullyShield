#nltk.download()
from nltk.tokenize import sent_tokenize
from nltk.tokenize import wordpunct_tokenize
#from HelperClass  import MySQLConnect
import MySQLConnect

import AlasdairBinarySearch

#list of black listed words pulled from a sentence.
listOfProfanitiesinSentence = []
blackList = MySQLConnect.pull_blacklist()


def tokenise_message(message):
  tokens = sent_tokenize(message)
  string = ""
  tokenstring = string.join(tokens)
  tok = wordpunct_tokenize(tokenstring)
  return tok


def scan_message(sentence):
  isContainingBlackListedWord = False         
  tokenList = tokenise_message(sentence) #tokenise the message
  
  for index in tokenList:
    if(AlasdairBinarySearch.binary_search_in_list(index, blackList)):
      isContainingBlackListedWord = True
      listOfProfanitiesinSentence.append(index)

  if (isContainingBlackListedWord):
    return True
  else:
     return False

#Nb will retrun probab of bullying. update db with score.
