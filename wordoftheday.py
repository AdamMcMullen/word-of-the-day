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

# To make it nicer in future I could use beautiful soup for webscraping, but I am happy with the style from dictionary.com and don't need to extract the text

##//////////////////////////////////////////////////////
##  Word of the Day
##//////////////////////////////////////////////////////


def send_email():

    f = open("words_test.txt", "r") # open the txt file that contains all the words
    words=f.read()
    wordlist=words.split('\n')

    word=wordlist[0]
    print(word)

    with open('old_words.txt', 'a') as file:
        file.write(word+'\n')

    with open("words_test.txt", "w") as f:
        for w in wordlist:
            if w != word:
                f.write(w+'\n')

    #Define who sends the email
    port = 465
    sender = 'WordOfTheDay68@gmail.com' # Email account for the sender's email.
    password = 'WordOfTheDay68!@#$%^&*()'
    recieve= 'amcmullen@rocketmail.com' # Create a list of all emails which will recieve an alert


    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Word Of The Day"
    msg['From'] = sender
    msg['To'] = recieve
    text = "Good Morning!\nHere is your word of the day"

    html=clean_html(get_definition(word))

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

    # Create the body of the message (a plain-text and an HTML version).

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

def send_email_at(send_time):
    time.sleep(send_time.timestamp() - time.time())
    send_email()
    print('email sent')

first_email_time = dt.datetime(2021,3,2,10,58,20)#11,30,0) # set your sending time in UTC (mar 2, 6:30 am EST)
interval = dt.timedelta(minutes=1)#24*60) # set the interval for sending the email

send_time = first_email_time
while True:
    send_email_at(send_time)
    send_time = send_time + interval
