import gspread 
from google.oauth2.service_account import Credentials 
from datetime import datetime 

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

creds = Credentials.from_service_account_file(
    "service_account.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

SHEET_ID = "1S6nASPc0346iBKbg2pri6_ovR6pUAnYye9b_sLwK1Oo"

sheet = client.open_by_key(SHEET_ID).sheet1


def save_to_sheet(sender, subject, category, reply):

    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    sheet.append_row([
        date,
        sender,
        subject,
        category,
        reply
    ])

    print("Saved to Google Sheets")