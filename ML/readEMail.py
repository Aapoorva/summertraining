#!/usr/bin/env python3

import smtplib
import time
import imaplib
import email

# server and port to read email
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


def read_email_from_gmail(FROM_EMAIL,FROM_PWD):
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        #logining into gmail acount
        mail.login(FROM_EMAIL,FROM_PWD)
        #selecting inbox label
        mail.select('inbox')

        #searching ids for each email
        type, data = mail.search(None, 'ALL')
        # storing ids to new variable
        mail_ids = data[0]

        id_list = mail_ids.split()
        #storing  1 nd last id to decide range 
        first_email_id = int((id_list[0]).decode())
        latest_email_id = int((id_list[-1]).decode())


        for i in range(latest_email_id,first_email_id, -1):
            i=str(i)
            #                         
            typ,data = mail.fetch(i, '(RFC822)' )       


            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_string(response_part[1].decode())
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

    except Exception as e:
        print(str(e))


# FROM_EMAIL = input('FROM_EMAIL : ')
# FROM_PWD = input('FROM_PWD : ')
# read_email_from_gmail(FROM_EMAIL,FROM_PWD)
read_email_from_gmail('aapoorva15@gmail.com','A@1099441 1514219')
