

'''Allows a user to flag each message one by one
'''

file = open("MessagesToProcess.txt", "r")
file.read().splitlines()
messageList = []
for message in file:
  print 1
  messageList.append(message)
  
print messageList
file.close()
