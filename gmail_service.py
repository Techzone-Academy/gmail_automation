from googleapiclient.discovery import build
from gmail_auth import authenticate
from email.mime.text import MIMEText
import base64
import re

creds = authenticate()

service = build("gmail", "v1", credentials=creds)


def get_unread_emails():

    results = service.users().messages().list(
        userId="me",
        labelIds=["INBOX"],
        q="is:unread",
        maxResults=1
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for message in messages:

        msg = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="full"
        ).execute()

        headers = msg["payload"]["headers"]

        sender = ""
        subject = ""

        for header in headers:

            if header["name"] == "From":
                sender = header["value"]

            elif header["name"] == "Subject":
                subject = header["value"]

        body = ""

        if "parts" in msg["payload"]:

            for part in msg["payload"]["parts"]:

                if part["mimeType"] == "text/plain":

                    data = part["body"].get("data")

                    if data:
                        body = base64.urlsafe_b64decode(data).decode("utf-8")

        else:

            data = msg["payload"]["body"].get("data")

            if data:
                body = base64.urlsafe_b64decode(data).decode("utf-8")

        emails.append({

            "id": message["id"],
            "threadId": msg["threadId"],
            "from": sender,
            "subject": subject,
            "body": body

        })

    return emails


def send_reply(to_email, subject, reply_text, thread_id):

    match = re.search(r"<(.+?)>", to_email)

    if match:
        to_email = match.group(1)

    message = MIMEText(reply_text)

    message["To"] = to_email
    message["Subject"] = "Re: " + subject

    raw = base64.urlsafe_b64encode(
        message.as_bytes()
    ).decode()

    service.users().messages().send(
        userId="me",
        body={
            "raw": raw,
            "threadId": thread_id
        }
    ).execute()


def mark_as_read(message_id):

    service.users().messages().modify(
        userId="me",
        id=message_id,
        body={
            "removeLabelIds": ["UNREAD"]
        }
    ).execute()