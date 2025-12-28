import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
# from gspread_dataframe import set_with_dataframe

import json
import os

cred_dict = json.loads(os.environ["GOOGLE_CREDENTIALS"])

print(cred_dict)

scopes = [ "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

creds = Credentials.from_service_account_info(cred_dict, scopes=scopes)
client = gspread.authorize(creds)

sheet = client.open("Economic Calendar").worksheet("Sheet1")
sheet.append_row(["Hi bro"])

# gsapi = gspread.service_account(filename="credentials.json")

# sheet = gsapi.open("Economic Calendar")
# work_sheet = sheet.sheet1

# df = pd.DataFrame({
#     "Name": ["Alice", "Bob", "Charlie"],
#     "Age": [24, 30, 28],
#     "City": ["Colombo", "kalutara", "Galle"]
# })


# set_with_dataframe(work_sheet,df)

# work_sheet.append_row(["Hi bro"])
