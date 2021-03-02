# Word of the Day Program
# 2020 Adam McMullen
# Author: Adam McMullen <adammcmullen.com>
# URL: <https://github.com/adammcmullen/Word-of-the-Day/>

#https://stackoverflow.com/questions/52022134/how-do-i-schedule-an-email-to-send-at-a-certain-time-using-cron-and-smtp-in-pyt
#https://stackoverflow.com/questions/882712/sending-html-email-using-python

from Dictionary import get_definition
from html_email import clean_html

import datetime as dt
import time

import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# This is a word of the day program, that uses SMTP email sending to send text and email notifications. I webscrape deictionary.com for the word defition in the Dictionary module and clean-up the html to give me what I want in html_email

# To make it nicer in future I could use beautiful soup for webscraping, but I am happy with the style from dictionary.com and presently don't need to extract the text
# I could also consider doing a google search if dictionary.com cannot find the word.

##//////////////////////////////////////////////////////
##  Word of the Day
##//////////////////////////////////////////////////////

# This is the function to actually send the email
def send_email():

    # Open the txt file that contains all the words and put into a list
    # The txt file has a different word on each line
    f = open("words_test.txt", "r")
    words=f.read()
    wordlist=words.split('\n')

    # The word to be defined and emailed is the first in the txt file/list
    word=wordlist[0]
    print(word)

    # Add the word you are defining to old_words file to keep as a record
    with open('old_words.txt', 'a') as file:
        file.write(word+'\n')

    # Rewrite to the words.txt file everything except the word to be defined
    with open("words_test.txt", "w") as f:
        for w in wordlist:
            if w != word:
                f.write(w+'\n')

    #Define email parameters
    port = 465
    sender = 'WordOfTheDay68@gmail.com' # Email account for the sender's email.
    password = 'kjhdsfjhiu^&*(h982%^34y8yibhds5678$%'
    recieve= 'amcmullen@rocketmail.com' # Create a list of all emails which will recieve the email


    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Word Of The Day"
    msg['From'] = sender
    msg['To'] = recieve
    text = "Good Morning!\nHere is your word of the day"

    # Try to scrape dictionary.com  or merriam webster for the word's definition
    pythonAnywhere =True
    try:
        defn=get_definition(word,pythonAnywhere)
        print("got the definition")
    except:
        message="Subject: Word of the Day!"+"\n\nCouldn't find "+word+" in its database. There might be a typo.\n\nAdam"
        html="""<!DOCTYPE html><html><body><h2>Couldn't find """+word+""" in its database. There might be a typo.</h2><p><a href="https://www.merriam-webster.com/dictionary/"""+word+"""">https://www.merriam-webster.com/dictionary/"""+word+"""</a></p><p><a href="https://www.dictionary.com/browse/"""+word+"""">https://www.dictionary.com/browse/"""+word+"""</a></p></body></html>"""


    # Try to clean up the html with definition then add it to the message
    try:
        html=clean_html(defn,pythonAnywhere)
        print("cleaned up the html")

    except:
        message="Subject: Word of the Day!"+"\n\nThere were problems cleaning up the html, maybe you should use beautiful soup.\n\nAdam"
        html="""<!DOCTYPE html><html><body><h2>There were problems cleaning up the html, maybe you should use beautiful soup.</h2><p><a href="https://www.merriam-webster.com/dictionary/"""+word+"""">https://www.merriam-webster.com/dictionary/"""+word+"""</a></p><p><a href="https://www.dictionary.com/browse/"""+word+"""">https://www.dictionary.com/browse/"""+word+"""</a></p></body></html>"""


    #Save the email content to a .html file
    f = open("email.html", "a")
    f.write(html)
    f.close()

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    message = msg.as_string()


    # Create the body of the message (a plain-text and an HTML version) and send
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

# This function sleeps until 7 am each morning to send the email
def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')


first_email_time = dt.datetime(2021,3,3,11,30,0) # set your sending time in EST (mar 3, 6:30 am EST)
interval = dt.timedelta(minutes=24*60) # set the interval for sending the email

# Continuously run this script to send a new email each day
send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval

