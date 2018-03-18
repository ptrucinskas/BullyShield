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
subjectList = open("Subjects.txt").read().splitlines()
blacklist = open("TestBlacklist.txt").read().splitlines()
file = open("FlaggedMessages.txt", "a")
flaggedMessages = open("FlaggedMessages.txt").read().splitlines()

Flags = 0
flag = False

def Pos(message):
    global Flags
    global flag
    if message.lower() in flaggedMessages:
        print 'This message has been flagged by another user!'
        flag = True
        Flags += 1
        return

    word = message.split()

    for i in range(len(word)):
        if word[i].lower() in subjectList:
            print 'Subject\t' + word[i]
            if i + 1 != len(word) and word[i + 1].lower() in connectors:
                print 'Connector\t' + word[i + 1]
                if i + 2 != len(word) and word[i + 2].lower() in connectors:
                    print 'Connector\t' + word[i + 2]
                    if i + 3 != len(word) and word[i + 3].lower() in blacklist:
                        print 'Blacklist!!!\t' + word[i + 3]
                        print 'Flagged!!!'
                        flag = True
                        if message in flaggedMessages:
                            print 'This message has been flagged by another user!'
                        else:
                            file.write(message + '\n')
                        Flags += 1
                        break
                elif i + 2 != len(word) and word[i + 2].lower() in blacklist:
                    print 'Blacklist!!\t' + word[i + 2]
                    print 'Flagged!!'
                    flag = True
                    if message in flaggedMessages:
                        print 'This message has been flagged by another user!'
                    else:
                        file.write(message + '\n')
                    Flags += 1
                    break
            elif i + 1 != len(word) and word[i + 1].lower() in blacklist:
                print 'Blacklist!\t' + word[i + 1]
                print 'Flagged!'
                flag = True
                if message in flaggedMessages:
                    print 'This message has been flagged by another user!'
                else:
                    file.write(message + '\n')
                Flags += 1
                break
        elif word[i].lower() in blacklist:
            print 'Warning!\t' + word[i]
        else:
            print 'Safe\t' + word[i]

    suggestFlag(message)

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

def main():
    global flag
    while Flags < 5:
        flag = False
        message = raw_input('Message: ')
        Pos(message)
    print 'This conversation has been flagged!'
    file.close()

main()
