# GetGmailLabels
This Python script is used to extract for a subset of Gmail users (Google apps for business only) all their labels and the number of items residing inside. 

Below you have a short how to:

-Create a google service account and authorize it for the following this scope: https://www.googleapis.com/auth/gmail.readonly

Use this procedure to guide you:
https://developers.google.com/identity/protocols/OAuth2ServiceAccount

Save the service account JSON to service_account_secret.json and copy it in the same folder as the file

-Enable the GMail API in your project:
https://support.google.com/cloud/answer/6158841?hl=en

-Make sure you have Python 2.7 installed
-Install the latest google API
pip install --upgrade google-api-python-client

-Populate the users.txt with the users' email addresses that you want to analyze

-Run the tool with "python getGmailLabels.py"

-Check the output.csv and enjoy the results
