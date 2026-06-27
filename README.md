# Gmail Automation using LangChain

## Overview

This project is an AI-powered Gmail Automation system built using Python, LangChain, and Google Gemini API.

It automatically:

- Reads unread Gmail messages
- Classifies emails using AI
- Generates professional replies
- Sends replies automatically
- Marks processed emails as read
- Stores email details in Google Sheets

---

## Features

- Gmail Authentication using Gmail API
- AI Email Classification
- Automatic Email Reply
- Google Gemini Integration
- LangChain Prompt Chaining
- Google Sheets Logging
- Marks emails as read after processing
- Checks for new emails every 30 seconds

---

## Technologies Used

- Python
- LangChain
- Google Gemini API
- Gmail API
- Google Sheets API
- gspread
- Google OAuth

---

## Project Structure

```
gmail_automation/
│── ai_agent.py
│── app.py
│── gmail_auth.py
│── gmail_service.py
│── sheets_service.py
│── requirements.txt
│── .gitignore
│── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Techzone-Academy/gmail_automation.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Add your Gmail OAuth credentials:

- credentials.json
- token.json

Add Google Sheets Service Account:

- service_account.json

---

## Run

```bash
python app.py
```

---

## Workflow

```
Unread Email
      ↓
Read Email
      ↓
LangChain
      ↓
Gemini
      ↓
Classify Email
      ↓
Generate Reply
      ↓
Save to Google Sheets
      ↓
Send Reply
      ↓
Mark as Read
```

---

## Author

**Syeed Ahmed**