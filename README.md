<h1>Phishing Email Detetctor </h1>
 This was a project that I did as part of my Security Scripting with Python course at Champlain College. I managed to create a script that took words from a suspicious word
 list that I created. These are words that are common in Phishing emails. I used Imap to connect to the Gmail inbox and the date module to set the time to retrieve the first 10 emails.
 The email module was used to parse through these emails. In the future I want to be able to read the header and extract urls.

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
