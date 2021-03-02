# Word of the Day Program
# 2020 Adam McMullen
# Author: Adam McMullen <adammcmullen.com>
# URL: <https://github.com/adammcmullen/Word-of-the-Day/>

from Dictionary import get_definition

# This script sends an email containing html data

# this could be improved by using Beautiful soup or the re modules

def clean_html(html):
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Word Of The Day"
    msg['From'] = sender
    msg['To'] = recieve

    # Create the body of the message (a plain-text and an HTML version).
    text = "Good Morning!\nHere is your word of the day"

    html=html.replace(html[html.find('<footer'):html.find('</footer>')+len('</footer>')],'')
    html=html.replace(html[html.find('<header'):html.find('</header>')+len('</header>')],'')
    html=html.replace(html[html.find('<section class="serp-nav-button'):html.find('</section>')+len('</section>')],'')
    html=html.replace(html[html.find('<div class="css-1jfqmi-SourceCitation ejtq9h60"'):html.find('</div>')+len('</div>')],'')
    start=html.find('<aside class="css-2mugq2 e1bbcgok4"')
    html=html.replace(html[start:html.find('</aside>',start)+len('</aside>')],'')
    start=html.find('<aside class="css-1bq7a5h-SupplementalEditorialContainer e13sij4y2"')
    html=html.replace(html[start:html.find('</aside>',start)+len('</aside>')],'')


    def find_inner_start(html,start):
        loc=html.find('<',start)
        next_tag=html.find('<',loc+1)
        if html[next_tag+1] !='/':
            return find_inner_start(html,loc+1)
        else:
            return loc

    def remove_inner(html,key):
        block_start=html.find(key)
        
        if block_start != -1:
            start=find_inner_start(html,block_start)
            if len(html[start+1:html.find(' ',start+1)]) < len(html[start+1:html.find('>',start+1)]):
                item=html[start+1:html.find(' ',start)]
            else:
                item=html[start+1:html.find('>',start)]
            
            end=html.find('/'+item+'>',start)

            if html[start+1]=='!':
                item = html[start+2:html.find(' ',start)]
                end=html.find(item+'>',start)  

            html=html.replace(html[start:end+len('/'+item+'>')],'')
            
            
            return remove_inner(html,key)
        else:
            return html


    html=remove_inner(html,'<div class="css-1ynqlq-RightMarketingSlot e4zjj2w0"')
    html=remove_inner(html,'<div id="quizzes"')



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

    return message










