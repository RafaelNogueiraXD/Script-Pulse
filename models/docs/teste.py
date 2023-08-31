from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from models.docs.funcoesDocs import *
SCOPES = ['https://www.googleapis.com/auth/documents']
DOCUMENT_ID = '1M8993QV8YrkSSYCX08pPgndboWSO2FR0M6wZcceFrNw'

def main():
    creds = None



    if os.path.exists('token1.json'):
        creds = Credentials.from_authorized_user_file('token1.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
    
        with open('token1.json', 'w') as token:
            token.write(creds.to_json())

    service = build('docs', 'v1', credentials=creds)
    text = "Esta é uma frase com texto branco e fundo preto."


    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1,
                },
                'text': text
            }
        }
    ]
    service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()



    start_index = 1
    end_index = len(text)

    requests = [
        {
            'updateTextStyle': {
                'range': {
                    'startIndex': start_index,
                    'endIndex': end_index
                },
                'textStyle': {
                    'foregroundColor': {
                        'color': {
                            'rgbColor': {
                                'red': 1.0,
                                'green': 1.0,
                                'blue': 1.0
                            }
                        }
                    },
                    'backgroundColor': {
                            'color': {
                                'rgbColor': {
                                    'red': 0.0,
                                    'green': 0.0,
                                    'blue': 0.0
                                }
                            }
                        }
                }, 
                'fields': 'foregroundColor,backgroundColor'
            }
        }
    ]

    service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()

if __name__ == '__main__':
    main()
