import MySQLdb
import re
import sys
import time
from HelperClass import MySQLConnect
from HelperClass import Bays_accurate
from HelperClass import ProcessMessage
from HelperClass import Email
from POS import Pos


SCORE_TO_TRIGGER_FLAG = 8

userID = int(sys.argv[1])
messageID = int(sys.argv[2])

#main program. Given a userId and messageId, this retrives the message
#calls the Bayes algorithm, and calls methods to set flags accordingly

def bully_shield(userID, messageID):
  isSuspect = False 

  #wait for 0.2s to ensure message is in db. Then get message.
  time.sleep(0.2)
  message = MySQLConnect.get_message(messageID)
  isSuspect = ProcessMessage.scan_message(message)

  #place message into MessagesToProcess.txt
  #file = open("POS/MessagesToProcess.txt", 'a')
  #file.write(message + "\n")
  #file.close()

  #check if there is a blacklisted word in message, pass to Bayes if true
  #decrease score of user if false
  if isSuspect == True:
      score = float(Bays_accurate.startPoint(message))
      if score > 0.0:
        MySQLConnect.increase_score(userID, 1)
      else:
        MySQLConnect.increase_score(userID, -1)
  else:
       MySQLConnect.increase_score(userID, -1)

  if Pos.main1(message) == True:
    MySQLConnect.increase_score(userID, 1)

  time.sleep(0.2)
  #Check if user score has reached a certain limit. Set Flag if so
  current_score = MySQLConnect.get_score(userID)
  if current_score > SCORE_TO_TRIGGER_FLAG:
    MySQLConnect.set_flag(userID, 'flag')
    log_flag(userID, messageID)
    Email.sendEmail(userID, messageID)



#Prints to log.txt. Should be called everytime a message is flagged
def log_flag(userID, messageID):
  try:
     file = open('log.txt', 'a')
     file.write("UserID: " + str(userID) + " was flagged by messageID: "
                + str(messageID) + "\n")
     file.close()
     has_Flagged = False

  except:
     print "Something went wrong in writing to the file"
     file.close()


bully_shield(userID, messageID)
