This program connects to Gmail inboxes using an app password that needs to be configured on the GMAIL account itself.
 The user is asked to enter email and password to start the script.
 It then parses through the GMAIL inbox, retrieving the first 10 newest emails and looks for words from a suspicious word list
 and creates a phishing detection txt file identifying which email the words were found in. I wanted to add URL extraction
 but ran out of time and could not figure it out. I also wanted to do a risk score based on the number of suspicious elements
 found. These are features I want to add in the future"""
