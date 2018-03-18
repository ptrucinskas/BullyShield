import MySQLdb
import re

"""
 Connects to the MySQL database. Various functions to retrieve and update data.
 Each function a forms new connection with the server, for ease of access
 in project development.

 Functions:

 add_to_blacklist(word)        - Inserts word into blacklist, if word already exists
                                 will replace the row.
                               - Requires word argument as String. DOES NOT CHECK IF IS
                                 SINGLE WORD - YET.

 check_connection()            - Checks that a connection can be established.

 get_flags(userID, flagToGet)  - Returns a boolean depending on value of specified
                                 flag for that user

 get_score(userID)             - Returns the current score for a given userID

 get_message                   - Returns the body of the message from the messageID

 increase_score(userID, score) - Sets the score of a userID
                               - Requires UserID as int, score as int

 mass_add_to_BL(fileToPush)    - Mass inserts words from a text file
                               - Requires a path to text file given as String
                               - file must contain words to insert on separate lines

 pull_blacklist()              - Takes all word entries from black_list, ensures all
                                 are lower case, and adds to blackList[]

 set_flag(userID, flagToSet)   - Sets the specified flag of a given user to 1
                               - Requires user ID as int or string, flagToSet as string
                                 atm 'flag'

 unset_flag(userID, flagToSet) - Sets the specified flag of a given user to 0
                               - Requires user ID as int or string, flagToSet as string
                                 ie 'flag'
                                 
 get_guardian_email(userID)    - Returns guardian email string of given user
                               - Requires user ID as int or string
                                 
  
  
 get_other(userId, messageId) - Returns user ID of other user that received the message
                              - Requires sender and message IDs as ints or strings

"""

#Connection Settings
DB_HOST = "localhost"
DB_USER = "root"
DB_PSWD = "22224568"
DB_NAME = "bullyshield_website"

#global list of black-listed words
blackList = []


def add_to_blacklist(word):
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()

  wordToInsert = word.lower()

  sqlPull = "SELECT word FROM `black_list`"
  sqlPush = "REPLACE INTO `black_list` (`word`) VALUES ('" \
            + wordToInsert + "');"

  try:
      cursor.execute(sqlPush)
      db.commit()

  except:
    print("Something went wrong!")
    db.rollback()

  finally:
    if db:
     db.close()



def check_connection():
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)  #connect to database
  cursor = db.cursor()                                      #create cursor object
  sql = "SELECT VERSION()"                                  #SQL string to query db

  try:
    cursor.execute(sql)                                     #attempt to query db
    result = cursor.fetchone()                              #fetch value of one row
    print "version: %s" % result

  except:
    print("Connection cannot be established")

  finally:
    if db:
      db.close()                                            #always close connecton



def get_flags(userID, flagToGet):
  userId = str(userID)
  is_flagged = False

  sql = "SELECT `" + flagToGet + "` FROM `fos_user` WHERE id ='" + userId + "'"
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()

  try:
    cursor.execute(sql)
    result = cursor.fetchone()
    if(result[0] == 1):
      is_flagged = True;

  except:
    print("Something went wrong!")

  finally:
    if db:
      db.close()
      return is_flagged



def get_score(userID):
  userId = str(userID)
  sql = "SELECT `score` FROM `fos_user` WHERE id ='" + userId + "'"
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()

  try:
    cursor.execute(sql)
    result = cursor.fetchone()

  except:
    print("Something went wrong!")

  finally:
    if db:
      db.close()
      return int(result[0])



def get_message(messageID):
  messageId = str(messageID)
  sql = "SELECT `body` FROM `message` WHERE id ='" + messageId + "'"
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()

  try:
    cursor.execute(sql)
    result = cursor.fetchone()

  except:
    print("Something went wrong!")

  finally:
    if db:
      db.close()
      return result[0]




def increase_score(userID, score):
  userId = str(userID)
  score = str(score)
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()
  sql =  "UPDATE `fos_user` SET `score` = `score` + '" + score \
      + "' WHERE `fos_user`.`id` = '" + userId + "'"

  try:
    cursor.execute(sql)
    db.commit()

  except:
    print("Something went wrong!")
    db.rollback()

  finally:
    if db:
      db.close()



def mass_add_to_BL(fileToPush):
  wordArray = []

  wordFile = open(fileToPush, "r")
  for word in wordFile:
      newWord = str(word)
      newWord = newWord.lower()
      newWord = newWord.strip()
      newWord = re.sub('[)`,(\'"]', '', newWord)
      wordArray.append(newWord)

  for word in wordArray:
   try:
    add_to_blacklist(word)
   except:
      print("Something went wrong in mass add")

   finally:
       wordFile.close()



def pull_blacklist():
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()
  sql = "SELECT word FROM `black_list`"
  tempList = []

  try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
      tempList.append(row)

    for i in tempList:
      i = str(i)
      i = i.lower()
      j = re.sub('[),(\'"]', '', i)
      blackList.append(j)

  except:
    print("Something went wrong!")

  finally:
    return blackList
    if db:
      db.close()



def set_flag(userId, flagToSet):
  userId = str(userId)

  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()
  sql = "UPDATE `fos_user` SET `" + flagToSet \
         + "` = '1' WHERE `fos_user`.`id` = '" + userId + "'"

  try:
    cursor.execute(sql)
    db.commit()

  except:
    print("Something went wrong!")
    db.rollback()

  finally:
    if db:
      db.close()



def unset_flag(userId, flagToSet):
  userId = str(userId)
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()
  sql = "UPDATE `fos_user` SET `" + flagToSet \
         + "` = '0' WHERE `fos_user`.`id` = '" + userId + "'"

  try:
    cursor.execute(sql)
    db.commit()

  except:
    print("Something went wrong!")
    db.rollback()

  finally:
    if db:
      db.close()



def get_guardian_email(userId):
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()
  query = "SELECT guardian FROM `fos_user` WHERE id='" + str(userId) + "'"

  try:
    cursor.execute(query)
    return cursor.fetchone()[0]

  except:
    print("Something went wrong!")
    db.rollback()

  finally:
    if db:
      db.close()



def get_other(userId, messageId):
  db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
  cursor = db.cursor()
  query = "SELECT participant_id FROM thread_metadata " \
          "WHERE thread_id IN (SELECT thread_id FROM message WHERE id='"+str(messageId)+"') " \
          "AND participant_id !=" + str(userId)

  try:
    cursor.execute(query)
    other_participant_id = cursor.fetchone()[0]

    return other_participant_id

  except:
    print("Something went wrong!")
    db.rollback()

  finally:
    if db:
      db.close()
