<h1>Phishing Email Detetctor </h1>
 This program connects to Gmail inboxes using an app password that needs to be configured on the GMAIL account itself.
 The user is asked to enter email and password to start the script.
 It then parses through the GMAIL inbox, retrieving the first 10 newest emails and looks for words from a suspicious word list
 and creates a phishing detection txt file identifying which email the words were found in. I wanted to add URL extraction
 but ran out of time and could not figure it out. I also wanted to do a risk score based on the number of suspicious elements
 found. These are features I want to add in the future

<h1>What it does</h1>

- Connects to a Gmail inbox using an app password configured on the Gmail account
- Prompts the user to enter their email and password to authenticate
- Retrieves the 10 most recent emails from the inbox
- Scans each email against a list of suspicious keywords
- Generates a phishing report as a .txt file identifying which emails triggered the keyword list

  <h1> Setup</h1>

To use this script you will need to enable App Passwords on your Gmail account under your Google security settings and use that generated password when prompted.

<h1>Planned Features</h1>
URL extraction and analysis from email body
Risk scoring based on the number of suspicious elements detected per email
