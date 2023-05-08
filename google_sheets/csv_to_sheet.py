import gspread
from google.oauth2.credentials import Credentials
import csv
import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow 
SCOPES = ['https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/docs','https://www.googleapis.com/auth/drive.metadata','https://www.googleapis.com/auth/drive.file']
def get_creds():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google_sheets/client_file/credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds
def create_sheet(filename, job):

    # load your OAuth credentials
    creds = get_creds()


    # create a client object and authorize it with the credentials
    client = gspread.authorize(creds)

    # create a new sheet in your Google Drive account
    new_sheet = client.create(f'Job Grab-{job}')

    # read your CSV file
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # write the data to your new sheet
    sheet = new_sheet.sheet1
    sheet.update(data)

    print('Sheet created successfully!')

if __name__ == '__main__':
    create_sheet('robert_half.csv','software engineer')
