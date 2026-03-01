
"""
Jonathan Wcislo CYBR-260-45: Security Scripting With Python- Fall 2025 Week 7 Final project
****************************************Phishing Email Detector***************************************************
This program connects to Gmail inboxes using an app password that needs to be configured on the GMAIL account itself.
 The user is asked to enter email and password to start the script.
 It then parses through the GMAIL inbox, retrieving the first 10 newest emails and looks for words from a suspicious word list
 and creates a phishing detection txt file identifying which email the words were found in. I wanted to add URL extraction
 but ran out of time and could not figure it out. I also wanted to do a risk score based on the number of suspicious elements
 found. These are features I want to add in the future"""


#Importing all modules needed for script
import imaplib
import email
from datetime import datetime, timedelta
import getpass

#This a function I created to check the email body against the suspicious word list
def check_suspicious_words(email_body, suspicious_words_list):
   word_count=0 #The variable that stores the number of words
   words_found=[] #Words that are found are put into a list
   for word in suspicious_words_list:  # For loop that checks the suspicious words list
        if word in email_body.lower():  # Checks email for words and changes them to lower case even if they are capitalized so it matches
         words_found.append(word)  # This adds the words to the list (.append)
         word_count = word_count + 1 #When words are found it adds 1 and stores the value

   return word_count, words_found #Returns the results

#This function parses through email message body looking plain text and returns the content
def parse_email_body(email_msg):
    email_body=""# Variable created to store body of email
    for part in email_msg.walk():# msg.walk helps break down different parts of the email body
        if part.get_content_type() == 'text/plain': #Type of content the script is looking for
            email_body = part.get_payload(decode=True).decode()# Gets the email body text and decodes it from bytes to string
    return email_body#Returns the body of the email

#Suspicious word list that emails are compared to
suspicious_words=["password","urgent","compromise ,click here, verify account"]

#User input asking for email and using getpass module to hide password for security
EMAIL=input("Enter your email:")
PASSWORD=getpass.getpass("Enter your app password:")

#Used to avoid unidentified variable in try block
mail=None

#Created try block in case user enters password or email address that  wrong
try:
    mail=imaplib.IMAP4_SSL('imap.gmail.com')#Connects to GMAIL inbox
    mail.login(EMAIL, PASSWORD) #Checks email address and password
    mail.select('inbox')#Selects inbox to connect to
    print ("Connected to Gmail successfully!")
except imaplib.IMAP4.error: #If wrong password entered exception doesn't let program crash
    print("Login failed! Check your email and password!")

#Used datetime module to get emails from the last 7 days and display the date for the emails
date=(datetime.now() - timedelta(days=7)).strftime("%d-%b-%Y")
print(f"Searching for emails since: {date}")
result, messages =mail.search(None, f"SINCE {date} NOT X-GM-LABELS CATEGORY_PROMOTIONS")#Parses through emails excludes promotions label in inbox

#try block incase no emails are found and program doesn't crash
try:
    email_ids=messages[0].split()
    print(f"Total emails: {len(email_ids)} emails from last 7 days")#Counts number of email IDs returned by search query. Shows how many emails matched search
except IndexError:
    print("No emails found")
    exit()
recent_ids=email_ids[-10:] if len(email_ids) > 10 else email_ids# More than 10 emails gets the last 10 items from the list. If there are less than ten takes all of them
recent_ids.reverse()# Reverses the way email IDS are displayed and begins with new messages

#For loop that checks the emails
for email_id in recent_ids:
    status, msg_data=mail.fetch(email_id, '(RFC822)')# RFC822 standard format for email messages. Tells IMAP server to return complete, raw email message
    msg=email.message_from_bytes(msg_data[0][1]) #0 is the Meta data string and 1 is actual raw email data. These are tuple positions
    print(f"Subject: {msg.get('Subject')}")#Prints subject of each email using f string
    print(f"From:{msg.get('From')}")#Prints from address with f string
    print(f"Body:{parse_email_body(msg)} ")#Prints body of email
    print ("-" *50)#Prints 50 dashes



    #Calls Function
    body =parse_email_body(msg)
    # Calls Function
    count, found_words=check_suspicious_words(body, suspicious_words)

    #Prints to console for testing
    if count > 0:
        print(f"\n SUSPICIOUS EMAIL DETECTED!")
        print(f"Subject:{msg.get('Subject')}")
        print(f"From:{msg.get('From')}")
        print(f"Found {count} suspicious words: {found_words}")


   #Prints to file phishing_report.txt
    if count > 0:
        with open("phishing_report.txt", "w") as f:  # Creates and writes a file of my findings
         f.write("*****PHISHING EMAIL REPORT*****")#Title of report
         f.write(f"\n SUSPICIOUS EMAIL DETECTED!")#New line informing of suspicious email detected
         f.write(f"Subject:{msg.get('Subject')}")#Subject of email
         f.write(f"From:{msg.get('From')}\n")#From address on a new line
         f.write(f"Subject: {msg.get('Subject')}\n")  # Writes the count in first line
         f.write(f"Words:{found_words}\n") #Writes the found words on a new line
         f.write("-" * 50 + "\n") #50 dashes and a new line












