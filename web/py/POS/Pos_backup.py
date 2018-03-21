'''
This program reads through the message to see if it follows a certain sentence
structure: Subject, connectors and blacklisted word. Before doing this it compares the message with a list of previously flagged messages to see if they match. Each message that is processed is either flagged and added to the flagged
list or safe. If a message is classified as safe the user has the option to
manually flag it for the next time. This message will only be added after the
program is closed (If you flag a message and try the same one straight after it
will not recognise it). The program is terminated once the conversation reaches
5 flags.
- Steeve.
'''
# Create all the lists to use.
connectors = ['is', 'are', 'r', 'a', 'an']
subjectList = open("POS/Subjects.txt").read().splitlines()
blacklist = open("POS/TestBlacklist.txt").read().splitlines()
file = open("POS/FlaggedMessages.txt", "a")
flaggedMessages = open("POS/FlaggedMessages.txt").read().splitlines()
nice = open("POS/NiceWords.txt").read().splitlines()

#Flags = 0
flag = False

def main1(message):
    if message.lower() in flaggedMessages:
        return True

    word = message.split()

    for i in range(len(word)):
        if word[i].lower() in subjectList:
            if i + 1 != len(word) and word[i + 1].lower() in connectors:
                if i + 2 != len(word) and word[i + 2].lower() in connectors:
                    if i + 3 != len(word) and word[i + 3].lower() in blacklist:
                        if i + 4 != len(word) and word[i + 4].lower() in nice:
			    return False	
                        elif message in flaggedMessages:
                            return True
                        else:
<<<<<<< HEAD
                            return True
                            flag = True
                            if message.lower() in flaggedMessages:
                               return True
                            else:
                                file.write(message.lower() + '\n')
                                Flags += 1
                        break
=======
                            file.write(message + '\n')
			    return True	
>>>>>>> final
                elif i + 2 != len(word) and word[i + 2].lower() in blacklist:
                    return True
                    if i + 3 != len(word) and word[i + 3].lower() in nice:
                        return False
                    else:
<<<<<<< HEAD
                        print 'Flagged!!'
                        flag = True
                        if message.lower() in flaggedMessages:
                            print 'This message has been flagged by another user!'
                        else:
                            file.write(message.lower() + '\n')
                        Flags += 1
                    break
=======
                        return True
                        if message in flaggedMessages:
                            return True
                        else:
                            file.write(message + '\n')
			    return True	
>>>>>>> final
            elif i + 1 != len(word) and word[i + 1].lower() in blacklist:
                return True
                if i + 2 != len(word) and word[i + 2].lower() in nice:
                    return False
                else:
<<<<<<< HEAD
                    print 'Flagged!'
                    flag = True
                    if message.lower() in flaggedMessages:
                        print 'This message has been flagged by another user!'
                    else:
                        file.write(message.lower() + '\n')
                    Flags += 1
                break
=======
                    return True
                    if message in flaggedMessages:
                        return True
                    else:
                        file.write(message + '\n')
		        return True
>>>>>>> final
        elif word[i].lower() in blacklist:
            #print 'Warning!\t' + word[i]
            continue
        else:
            continue
    return False    	
   # suggestFlag(message)

'''
def suggestFlag(message):
    global Flags
    if not flag: #== False:
        flagMessage = raw_input('Flag?(Y/N): ')
        if flagMessage.lower() == 'y':
            file.write(message + '\n')
            Flags += 1
            print 'Added to the flagged messages list.'
        elif flagMessage.lower() == 'n':
            print 'Not added'
        else:
            print 'Invalid input try again.'
            suggestFlag(message)
'''

#print Pos("Hello")
