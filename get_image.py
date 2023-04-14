
# import pickle
# import os
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request
# from tabulate import tabulate
# from datetime import datetime

# now = datetime.now()
# today = now.strftime("%Y%m%d")
# print (today)

# SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# def get_gdrive_service():
#     creds = None
#     if os.path.exists('token.pickle'):
#         with open('toke.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)
#     return build('drive', 'v3', credentials = creds)

# def get_files():
#     service = get_gdrive_service()
#     results = service.files().list(pageSize = 10, fields = "nextPageToken, files(id, name)").execute()
#     items = results.get('files', [])
#     print(items)

# get_files()