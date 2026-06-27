from gmail_service import get_unread_emails, send_reply, mark_as_read
from ai_agent import classify_email
from sheets_service import save_to_sheet

import re
import time

print("=" * 50)
print("AI Email Assistant Started...")
print("Checking for new emails every 30 seconds...")
print("=" * 50)

while True:

    emails = get_unread_emails()

    if len(emails) == 0:
        print("\nNo new emails.")

    else:

        for email in emails:

            print("\nNew Email Found")
            print("FROM :", email["from"])
            print("SUBJECT :", email["subject"])

            email_text = f"""
Subject:
{email["subject"]}

Body:
{email["body"]}
"""

            response = classify_email(email_text)

            try:

                category_match = re.search(
                    r'"category"\s*:\s*"([^"]+)"',
                    response
                )

                reply_match = re.search(
                    r'"reply"\s*:\s*"([\s\S]*)"',
                    response
                )

                if not category_match or not reply_match:
                    print("Invalid AI Response")
                    print(response)
                    continue

                category = category_match.group(1)

                reply = reply_match.group(1)

                if reply.endswith('"'):
                    reply = reply[:-1]

                reply = reply.replace("\\n", "\n")

            except Exception as e:

                print("Error :", e)
                print(response)
                continue

            print("\nCategory :", category)

            print("\nGenerated Reply:\n")
            print(reply)

            # Save data in Google Sheets
            save_to_sheet(
                email["from"],
                email["subject"],
                category,
                reply
            )

            # Send Email Reply
            send_reply(
                email["from"],
                email["subject"],
                reply,
                email["threadId"]
            )

            # Mark Email as Read
            mark_as_read(email["id"])

            print("\nReply Sent Successfully")
            print("=" * 50)

    print("\nWaiting 30 seconds...\n")

    time.sleep(30)