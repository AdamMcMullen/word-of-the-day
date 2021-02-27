# Word of the Day Program
# 2020 Adam McMullen
# Author: Adam McMullen <adammcmullen.com>
# URL: <https://github.com/adammcmullen/Word-of-the-Day/>

from PyDictionary import PyDictionary

# This is a word of the day program, that uses SMTP email sending to send text and email notifications

##//////////////////////////////////////////////////////
##  Word of the Day
##//////////////////////////////////////////////////////

dictionary=PyDictionary()
f = open("words.txt", "r")
words=f.read()
wordlist=words.split('\n')
defns=''
#len(wordlist)
for i in range(len(wordlist)):
    defns+=wordlist[i]+':'+str(dictionary.meaning(wordlist[i])).replace('\'','').replace('{','').replace('}','').replace('[','').replace(']','')+'\n\n'
print(defns)

# words=words.replace('ï‚§', '').replace('\n', '').split('\t')
#
with open('definitions.txt', 'w') as f:
    for item in defns:
        f.write("%s\n" % item)
f.close()

print()

recieve= 'amcmullen@rocketmail.com' # Create a list of all emails which will recieve an alert.
import smtplib, ssl

port = 465
sender='WordOfTheDay68@gmail.com'
password = 'WordOfTheDay68!@#$%^&*()'
sender = 'WordOfTheDay68@gmail.com' # Email account for the sender's email.
subject = "Subject: Word of the Day!"
text = " It is currently working"
message = subject +"\n\n"+defns
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)
print("Sent.")
exit() # Ending loop once the alert is sent. This stops numerous alerts.
main()
exit()