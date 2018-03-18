
def binary_search_in_list(intendedWord, listOfCurse):

        listSize = len(listOfCurse)
  	firstListIndex = 0
	lastListIndex = len(listOfCurse)-1
	wordIsFound = False
	
    	while firstListIndex<=lastListIndex and not wordIsFound:
		midpoint = (firstListIndex + lastListIndex)/2
		if listOfCurse[midpoint].lower() == intendedWord:
			wordIsFound = True
		else:
			if intendedWord < listOfCurse[midpoint]:
				lastListIndex = midpoint-1
			else:
 				firstListIndex = midpoint+1
	return wordIsFound


'''
STUCK IN INFINTE LOOP
def BinarySearch(wordToSearch, arrayOfWords):
	isWordFound = False
	array = arrayOfWords
	#Initilises variables that are used in the searching of the array
	lowerLimit = 0
	upperLimit = len(array) - 1
	middlePoint = 0
	
	#A while loop is used to loop until we find the element
	#Note: We do not know how many times we need to loop. Hence, we need to use
	#a while loop. It's condition is that isWordFound = false
	while isWordFound == False:
		#update the middle point every iteration, this allows us to ignore
		#parts of the array
		middlePoint = (lowerLimit + upperLimit) / 2
		if wordToSearch == array[middlePoint]:
			#Is the word we need at the middle point of the array
			#If yes, set the boolean variable to true and jump out
			isWordFound = True
			continue
		else:
			#Otherwise, is the word greater than or less than the middle 
			#point of the array. Act accordingly i.e. reduce the limits
			#with which we operate on.
			if wordToSearch > array[middlePoint]:
				lowerLimit = middlePoint + 1
			elif wordToSearch < array[middlePoint]:
				upperLimit = middlePoint - 1
	
	return isWordFound

'''
