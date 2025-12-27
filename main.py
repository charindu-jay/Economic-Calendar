import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from gspread_dataframe import set_with_dataframe

gsapi = gspread.service_account(filename="credentials.json")

sheet = gsapi.open("Economic Calendar")
work_sheet = sheet.sheet1


df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 28],
    "City": ["Colombo", "kalutara", "Galle"]
})


set_with_dataframe(work_sheet,df)
