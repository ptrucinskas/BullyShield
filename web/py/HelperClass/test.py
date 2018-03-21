import ProcessMessage
list_of_profanityWords = []
list_of_selected_profanities = []
notPrfanityWordsInSentence = []

# getting all the profanity words and put all them in a tuple
# the elements of the tuple are word, T, F
def tuple_of_profanity():
	blacklist = open("../Data/Blacklist.txt").read().splitlines()
	for line in blacklist:
		tuples = tuple(line.split("\t"))
		list_of_profanityWords.append(tuples)
	

# see whether the current message has 
# any kind of blacklisted words or not return 

def searchForProfanity(listOfWords):
	del list_of_selected_profanities[:] 
	for word in listOfWords:
		for tupleGroup in list_of_profanityWords:
			bullyWord, trueP, falseP = tupleGroup
			if(bullyWord == word):
				list_of_selected_profanities.append(tupleGroup)
				break
  
def listOfNotBullyWordsInTheSentece():
	del notPrfanityWordsInSentence[:]
	for tupleGroup in list_of_profanityWords:
		for profanityTuple in list_of_selected_profanities:
			if not tupleGroup == profanityTuple:
		           notPrfanityWordsInSentence.append(tupleGroup) 

#*********** Bays probability **************


finalProbability = 0.0

def bays():
	print list_of_selected_profanities
	interLevelProbabilityTrue = 1.0
	interLevelProbabilityFalse= 1.0

	# probability of true
	for tuples in list_of_selected_profanities:
		word, true1, false1 = tuples
		interLevelProbabilityTrue *= float(true1)

	for tuples in notPrfanityWordsInSentence:  	
		word, true1, false1 = tuples
		interLevelProbabilityTrue *= 1- float(true1)

	# probability of false
	for tuples in list_of_selected_profanities:
		word, true2, false2 = tuples
		interLevelProbabilityFalse *= 1 -float(false2)

	for tuples in notPrfanityWordsInSentence:  	
		word, true2, false2 = tuples
		interLevelProbabilityFalse *= float(false2)
	
	print interLevelProbabilityTrue
 	print interLevelProbabilityFalse	
	print (interLevelProbabilityTrue > interLevelProbabilityFalse)
	
	if interLevelProbabilityTrue > interLevelProbabilityFalse:
		finalProbability = interLevelProbabilityTrue * 0.5 
		finalProbability /= denominator() 
 
	#return finalProbability

def denominator():
	probability = 0.0
	for tuples in list_of_selected_profanities:
		probability += float(1/171476)
	for tuples in notPrfanityWordsInSentence:  	
		probability += float(1 - 1/171476)
	return probability
	
#*********** End bays probability **************
def startPoint(message):
	tuple_of_profanity()
        message = ProcessMessage.tokenise_message(message)
	searchForProfanity(message)
	del list_of_selected_profanities[:] 
        listOfNotBullyWordsInTheSentece()
        print notPrfanityWordsInSentence
	bays()



startPoint("This is a fuck shit cunt fuck you all")
startPoint("You are fucking beautiful")
print float (finalProbability)
print notPrfanityWordsInSentence
