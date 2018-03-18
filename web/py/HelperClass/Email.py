import smtplib
import MySQLConnect

"""
    Sends Email messages to the bully and bullied.
    
    Usage:
    
    - sendEmail(bullyId, messageId) 
    
        First argument is user ID of who sent the flagged message.
        Second argument is ID of the flagged message.
        
        Sends two emails, one to bully, other one to the bullied user.
        Bully is the one whose user ID is give, other is retrieved from the 
        database using the message ID.
        
    - getEmailTextBully(recipient)
        
        Contains template for email that is received by the bully user.
    
    - getEmailTextBullied(recipient)
    
        Contains template for email that is received by the bullied user.
        
    - SMTP_SERVER_ADDRESS, SMTP_SERVER_PORT, EMAIL_USER, EMAIL_PASSWORD
    
        Adjust these variables to change the SMTP server configuration.
        
"""


SMTP_SERVER_ADDRESS = 'smtp.gmail.com'
SMTP_SERVER_PORT = 587
EMAIL_USER = "bully.shield.csx7@gmail.com"
EMAIL_PASSWORD = "csx7csx7"


# Returns email template (send to bully)
def getEmailTextBully(recipient):
    return "\r\n".join([
        "From: " + EMAIL_USER,
        "To: " + recipient,
        "Subject: One of your messages was inappropriate",
        "",
        "Hello guardian of child,",
        "",
        "A conversation your child is having, has been brought",
        "to the program's attention. The conversation contains",
        "several harmful words and phrases that show that",
        "your child may be a bully. "
        "We want to take this opportunity to encourage you to act. ",
        "",
        "Thanks",
        "BullyShield Dev Team"
    ])

# Returns email template (send to bullied)
def getEmailTextBullied(recipient):
    return "\r\n".join([
        "From: " + EMAIL_USER,
        "To: " + recipient,
        "Subject: One of your messages was inappropriate",
        "",
        "Hello guardian of child,",
        "",
        "A conversation your child is having, has been brought",
        "to the program's attention. The conversation contains",
        "several harmful words and phrases that show that",
        "your child may be being bullied. "
        "We want to take this opportunity to encourage you to act.",
        "",
        "Thanks",
        "BullyShield Dev Team"
    ])



# Sends emails to both bully and bullied.
# Requires Id of user that was determined to be the bully and message Id
# that was flagged
def sendEmail(bullyId, messageId):
    try:
        guardian_email_bully = MySQLConnect.get_guardian_email(bullyId)

        bulliedId = MySQLConnect.get_other(bullyId, messageId)

        guardian_email_bullied = MySQLConnect.get_guardian_email(bulliedId)

        server = smtplib.SMTP(SMTP_SERVER_ADDRESS, SMTP_SERVER_PORT)
        server.ehlo()
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, guardian_email_bully, getEmailTextBully(guardian_email_bully))
        server.sendmail(EMAIL_USER, guardian_email_bullied, getEmailTextBullied(guardian_email_bullied))
        server.quit()
    except:
        print "Something went wrong while sending emails"
