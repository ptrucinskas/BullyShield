'''
NB classifier by Kane & Hossein
'''

import ProcessMessage
list_of_profanityWords = []
list_of_selected_profanities = []
notPrfanityWordsInSentence = []

# getting all the profanity words and put all them in a tuple
# the elements of the tuple are word, T, F
def tuple_of_profanity():
	del list_of_profanityWords[:]
        import os
        script_dir = os.path.dirname(__file__)
        rel_path = "../Data/Blacklist.txt"
        abs_file_path = os.path.join(script_dir, rel_path)
        blacklist = open(abs_file_path).read().splitlines()
	#blacklist = open("Data/Blacklist.txt").read().splitlines()
	for line in blacklist:
		tuples = tuple(line.split("\t"))
		list_of_profanityWords.append(tuples)

# see whether the current message has 
# any kind of blacklisted words or not return 

def searchForProfanity(listOfWords):
	#list_of_selected_profanities = []
	del list_of_selected_profanities[:]
	for word in listOfWords:
		for tupleGroup in list_of_profanityWords:
			bullyWord, trueP, falseP = tupleGroup
			if(bullyWord == word):
				list_of_selected_profanities.append(tupleGroup)
				break
  
def listOfNotBullyWordsInTheSentece():
	#notPrfanityWordsInSentence = []
	del notPrfanityWordsInSentence[:] 
	for tupleGroup in list_of_profanityWords:
		for profanityTuple in list_of_selected_profanities:
			if tupleGroup == profanityTuple:
				break
		else:
			notPrfanityWordsInSentence.append(tupleGroup) 
#*********** Bays probability **************




def bays():
#	print list_of_selected_profanities 
#	print notPrfanityWordsInSentence
	finalProbability = 0.0
	interLevelProbabilityTrue = 1.0
	interLevelProbabilityFalse= 1.0
	# probability of true
	for tuples in list_of_selected_profanities:
		word, true, false = tuples
		interLevelProbabilityTrue *= float(true)
	
	#print "***" + str(interLevelProbabilityTrue) 
	#for tuples in notPrfanityWordsInSentence:  	
	#	word, true, false = tuples
		
		#print tuples 
		#print interLevelProbabilityTrue
	#	interLevelProbabilityTrue *= float(false) 

	#print "***" + str(interLevelProbabilityTrue) 
	# probability of false
	for tuples in list_of_selected_profanities:
		word, true, false = tuples
		interLevelProbabilityFalse *= float(false) 
	
	#print "***" + str(interLevelProbabilityFalse) 
	#for tuples in notPrfanityWordsInSentence:  	
	#	word, true, false = tuples
	#	interLevelProbabilityFalse *= 1-float(false)
	
	#print "***" + str(interLevelProbabilityFalse) 
	#print interLevelProbabilityTrue
 	#print interLevelProbabilityFalse	
	#print (interLevelProbabilityTrue > interLevelProbabilityFalse)

	if interLevelProbabilityTrue > interLevelProbabilityFalse:
		#print "final " + str(finalProbability)
		finalProbability = interLevelProbabilityTrue * 0.5 
  		#print "final " + str(finalProbability)
		finalProbability /=  denominator()
		#print "final " + str(finalProbability) 
 	#print finalProbability
        #print "final " + str(finalProbability)
	return finalProbability

def denominator():
	probability = 0.0
        #print list_of_selected_profanities
	for tuples in list_of_selected_profanities:
		probability += float(1/171476)
	for tuples in notPrfanityWordsInSentence:  	
		probability += float(1 - 1/171476)
	return probability
	
#*********** End bays probability **************
def startPoint(message):
	tuple_of_profanity()
        message = ProcessMessage.tokenise_message(message.lower())
	searchForProfanity(message)
        listOfNotBullyWordsInTheSentece()
	return bays()
startPoint("You are a fucking CUNT,Im going to STAB you with a rusty spoon. I hope you DIE, you fucking fuckWIT. Bastard dickHead.")
#startPoint("You are a bitch")
#startPoint("it was fucking annoying")

listOfNotBullyWordsInTheSentece()
print bays()

