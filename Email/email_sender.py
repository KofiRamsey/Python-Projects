import smtplib

sender_email = "your@gmail.com" # your email here
receiver_email = "other@gmail.com" # receiver email here

with open("password.txt", "r") as file: # create a passwords.txt file with your gmail password
    password = file.read().strip()

message = """
Subject: Test Email

This is a test email.
Sent by python
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

