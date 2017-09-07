
from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from oauth2client.service_account import ServiceAccountCredentials

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'


def main():
   
    credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account_secret.json', SCOPES)
    http = credentials.authorize(httplib2.Http())
    f = open("output.csv",'w')
    lines = [line.rstrip('\n') for line in open('users.txt')]
    for line in lines:
        delegated_credentials = credentials.create_delegated(line)
        http_auth = delegated_credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http_auth)
        results = service.users().labels().list(userId=line).execute()
        for label in results['labels']:
            f.write(line)
            f.write(",")
            f.write(label['name'])
            f.write(",")
            queryLabel = service.users().labels().get(id=label['id'],userId=line).execute()
            f.write("%d" % (queryLabel['messagesTotal']))
            f.write("\n")
    f.close()
if __name__ == '__main__':
    main()