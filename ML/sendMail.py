#!/usr/bin/env python3

import smtplib

try :
	# creates SMTP session
	#				server location , port no
	s = smtplib.SMTP('smtp.gmail.com', 587)

	# start TLS for security
	s.starttls()

	sender_mail=input("Sender Mail : ")
	sender_passwd=input("Sender Password : ")

	# Authentication
	s.login(sender_mail,sender_passwd)
	print("Successfull Log In")

	receiver_email=input("Receiver Mail : ")
	msg=input("Message : ")

	# sending the mail
	s.sendmail(sender_mail,receiver_email, msg)
	print("Mail Sent")

except Exception as e:
	print("ERROR : ",e)
# terminating the session
s.quit()