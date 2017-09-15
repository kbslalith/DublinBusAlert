import urllib.request
import re, sys
import smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


x=0
# Read the API using urlib function, 3188 [Leopardstown Bus stop]


class Getime:
    url = 'https://data.dublinked.ie/cgi-bin/rtpi/realtimebusinformation?stopid=3188&format=xml'
    read = urllib.request.urlopen(url).read()

    # Since everthing is read in bytes, convert them into strings
    new_read = read.decode("utf-8")
    test = str(new_read.split())
    testword = "<duetime>"

    #print (test)
    #Index the string and print the 10th element from '<' which is the number we care of.
    #next_word = new_read[new_read.index('duetime') + 8]

    duetime = re.findall(r'<duetime>(.*?)</duetime>',new_read)
    route = re.findall(r'<route>(.*?)</route>',new_read)
    sch_dep_time = re.findall(r'<scheduleddeparturedatetime>(.*?)</scheduleddeparturedatetime>',new_read)
    #For now print it.
    #print ("This bus to smurfit is in \n")
    mailmsg = str((str(duetime)+" min;"+" Bus No -> "+str(route)+" dep by -> "+str(sch_dep_time)))

    # Time to send mail

    fromaddr = "bustime1102@gmail.com"
    toaddr = "kbslalith@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "BUS TIMING OF 114 BUS FROM Leopardstown"

    body = mailmsg
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "bustime@1102")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()




#sys.exit(0)
