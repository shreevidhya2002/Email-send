import cv2
import smtplib
import imghdr
from email.message import EmailMessage
  
email_subject = "Email test from Python"
sender_email_address = "a**********"
receiver_email_address = "y*********"
email_smtp = "smtp.gmail.com"
email_password = "**********"
  
# create an email message object
message = EmailMessage()
  
# configure email headers
message['Subject'] = email_subject
message['From'] = sender_email_address
message['To'] = receiver_email_address
# open image as a binary file and read the contents
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0
while True:
    sucess,img = cap.read()
    cv2.imwrite(img,'lion.jpg')
    time.sleep(2)
with open('lion.jpg', 'rb') as file:
   image_data = file.read()
   
   # create an email message object
#message = EmailMessage()
  
# open image as a binary file and read the contents
# with open('image.jpg', 'rb') as file:
#     
#    image_data = file.read()
   # set smtp server and port
server = smtplib.SMTP(email_smtp, '587')
# identify this client to the SMTP server
server.ehlo()
# secure the SMTP connection
server.starttls()
  
# login to email account
server.login(sender_email_address, email_password)
# send email

  
message.set_content("Email from Python with image attachment")
# attach image to email
message.add_attachment(image_data, maintype='image', subtype=imghdr.what(None, image_data))
  
server.send_message(message)
# close connection to server
server.quit()
   
'''  
# set email body text
message.set_content("Hello from Python!")
  
# set smtp server and port
server = smtplib.SMTP(email_smtp, '587')
# identify this client to the SMTP server
server.ehlo()
# secure the SMTP connection
server.starttls()
  
# login to email account
server.login(sender_email_address, email_password)
# send email
server.send_message(message)
# close connection to server
server.quit()
'''
