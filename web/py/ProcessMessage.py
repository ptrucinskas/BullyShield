import MySQLdb
import random
import re
import sys


messageID = int(sys.argv[1])
userID = int(sys.argv[2])

DB_HOST = "52.23.237.31"
DB_USER = "bullyshieldadmin"
DB_PSWD = "csx7"
DB_NAME = "bullyshield_website"

db = MySQLdb.connect(DB_HOST, DB_USER, DB_PSWD, DB_NAME)
cursor = db.cursor()


# Returns a single row from DB as a dictionary, keys represent column names
def getSingleRowDict(query):
    cursor.execute(query)
    result = cursor.fetchone()

    column_names = []
    for i in range(len(cursor.description)):
        column_names.append(cursor.description[i][0])
    row = dict(zip(column_names, result))

    return row
def getEmailText(message):
    return "\r\n".join([
        "From: user_me@gmail.com",
        "To: user_you@gmail.com",
        "Subject: Just a message",
        "",
        "Your message has been flagged",
        message
    ])

try:
    message = getSingleRowDict("SELECT * FROM `message` WHERE id='%d'" % messageID)
    # Example of this dictionary
    # {'body': 'tes', 'created_at': datetime.datetime(2018, 3, 8, 18, 16, 15),
    # 'sender_id': 7L, 'thread_id': 25L, 'flag': 1, 'id': 160L}


    flag = 1#random.randint(0,1)

    query = "UPDATE `message` SET `flag` = '%d' WHERE `id` = '%d'" % (flag, messageID)
    cursor.execute(query)

    db.commit()

    if flag == 1:
        user = getSingleRowDict("SELECT * FROM `fos_user` WHERE id='%d'" % userID)
        # Example of this dictionary
        # {'username': 'taiptaip', 'confirmation_token': None,
        # 'username_canonical': 'taiptaip', 'roles': 'a:0:{}',
        # 'password_requested_at': None, 'email_canonical': 'ptrucinskas@gmail.com',
        # 'guardian': 'tavotevas@gmail.com', 'enabled': 1,
        # 'id': 7L, 'flag': 0,
        # 'score': 0L, 'last_login': datetime.datetime(2018, 3, 8, 16, 22, 31),
        # 'password': '$2y$13$nf33XCvpTANqj/JFJvMdcO/QfCrgLillxYOmBUUEcbR0Jt2w9RYye',
        # 'salt': None, 'email': 'ptrucinskas@gmail.com'}

        guardian_email = user["guardian"]

        import smtplib
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("bully.shield.csx7@gmail.com", "csx7csx7")
        msg = getEmailText("There was malicious content")
        server.sendmail("bully.shield.csx7@gmail.com", guardian_email, msg)
        server.quit()

except Exception, e:
    print("Something went wrong!" + str(e))
    db.rollback()

finally:
    if db:
        db.close()
