import MySQLdb
import random
import re
import sys

messageID = int(sys.argv[1])

DB_HOST = "52.23.237.31"
DB_USER = "bullyshieldadmin"
DB_PSWD = "csx7"
DB_NAME = "bullyshield_website"

db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
cursor = db.cursor()
sqlPull = "SELECT * FROM `message` WHERE id='%d'" % messageID

try:
  cursor.execute(sqlPull)
  message = cursor.fetchone()
  #column_description = []
  #column_description.append(cursor.description)
  #column_names = column_description[:][0]
  #row = dict(zip(column_names, message))

  x = random.randint(0,1)

  query = "UPDATE `message` SET `flag` = '%d' WHERE `id` = '%d'" % (x, messageID)
  cursor.execute(query)

  db.commit()


  print(str(x))
except Exception, e:
  print("Something went wrong!" + str(e))
  db.rollback()

finally:
  if db:
      db.close()
