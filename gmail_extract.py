from bs4 import BeautifulSoup
import requests, openpyxl
import csv
import email, getpass, imaplib, os, re
import matplotlib.pyplot as plt


#This directory is where you will save attachments
detach_dir = "F:\OTHERS\CS\PYTHONPROJECTS"
#Enter your GMail username -->
user = raw_input("gmircous@gmail.com")
#Enter your password -->
pwd = getpass.getpass("Pinkrato3")

m = imaplib.IMAP4_SSL("imap.gmail.com")
m.login(user, pwd)

#Select one folder, you could use the whole INBOX instead

m.select("BUSINESS/PETROLEUM")


#One should use m.list() to get all the mailboxes. \
#Search for all emails coming from specified sender and select the mail ids:

resp, items = m.search(None, '(FROM "EIA_eLists@eia.gov")')
items = items[0].split()

my_msg = [] # store relevant msgs here in please
msg_cnt = 0
break_ = False
#
#I want the last emails, so that I am using items[::-1]

for emailid in items[::-1]:

    resp, data = m.fetch(emailid, "(RFC822)")

    if ( break_ ):
        break

    for response_part in data:

      if isinstance(response_part, tuple):
          msg = email.message_from_string(str(response_part[1]))
          varSubject = msg['subject']
          varDate = msg['date']
#
#I want only the ones beginning with $

          if varSubject[0] == '$':
              r, d = m.fetch(emailid, "(UID BODY[TEXT])")

              ymd = email.utils.parsedate(varDate)[0:3]
              my_msg.append([ email.message_from_string(d[0][1]) , ymd ])

              msg_cnt += 1
#
#I want only the N=100 last messages

              if ( msg_cnt == 100 ):
                  break_ = True

l = len(my_msg)
US, EastCst, NewEng, CenAtl, LwrAtl, Midwst, GulfCst, RkyMt, WCst, CA = [0]*l, [0]*l, [0]*l, [0]*l, [0]*l, [0]*l, [0]*l, [0]*l, [0]*l, [0]*l
absc = [k for k in range(len(my_msg))]
dates = [str(msg[1][2])+'-'+str(msg[1][3])+'-'+str(msg[1][0]) for msg in my_msg]
cnt = -1

for msg in my_msg:

    data = str(msg[0]).split("\n")
    cnt+=1
    for c in [k.split("\r")[0] for k in data[2:-2]]:
#
#Use regular expressions to fetch relevant information

        m = re.match( r"(.+)(=3D\$)(.+)" , c )
        if( m == None ):
            continue

        country, na, price = m.groups()

        if ( country == "US" or country == "USA" ) :
            US[cnt] = float(price)
        elif( country == "NewEng" ) :
            EastCst[cnt] = float(price)
        elif( country == "EastCst" ) :
            NewEng[cnt] = float(price)
        elif( country == "EastCst" ) :
            CenAtl[cnt] = float(price)
        elif( country == "EastCst" ) :
            LwrAtl[cnt] = float(price)
        elif( country == "EastCst" ) :
            Midwst[cnt] = float(price)
        elif( country == "EastCst" ) :
            GulfCst[cnt] = float(price)
        elif( country == "EastCst" ) :
            RkyMt[cnt] = float(price)
        elif( country == "EastCst" ) :
            WCst[cnt] = float(price)
        elif( country == "EastCst" ) :
            CA[cnt] = float(price)
#Plot all these curves with US prices

plt.plot( absc, US )

plt.plot( absc, EastCst )
plt.plot( absc, NewEng, '#251BE0' )
plt.plot( absc, EastCst, '#1BE0BF' )
plt.plot( absc, CenAtl, '#E0771B' )
plt.plot( absc, LwrAtl, '#CC1BE0' )
plt.plot( absc, Midwst, '#E01B8B' )
plt.plot( absc, GulfCst, '#E01B3F' )
plt.plot( absc, RkyMt )
plt.plot( absc, WCst )
plt.plot( absc, CA )

plt.legend( ('US', 'EastCst', 'NewEng' , 'EastCst', 'CenAtl', 'LwrAtl', 'Midwst', 'GulfCst', 'RkyMt', 'WCst', 'CA')  )
plt.title('Diesel price')
locs,labels = plt.xticks(absc, dates)
plt.show()


#
source = requests.get('')
soup = BeautifulSoup(source.text, 'html.parser')
