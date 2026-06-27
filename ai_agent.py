import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.3
)

prompt = PromptTemplate(
    input_variables=["email"],
    template="""
You are an AI Email Assistant.

Read the email below carefully.

Your tasks:

1. Classify the email into ONLY one category:
- Inquiry
- Support
- Complaint
- Job Application
- Spam

2. Generate a professional reply.

IMPORTANT RULES:

- Return ONLY JSON.
- Do NOT write anything before or after the JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- The "reply" value MUST use \\n for new lines.
- Make sure the JSON is valid.

Example:

{{
    "category": "Inquiry",
    "reply": "Dear Customer,\\n\\nThank you for contacting us. We have received your email.\\n\\nBest regards,\\nCustomer Support Team"
}}

Email:

{email}
"""
)

chain = prompt | llm


def classify_email(email):

    response = chain.invoke({
        "email": email
    })

    text = response.content.strip()

    text = text.replace("```json", "")
    text = text.replace("```", "")
    text = text.strip()

    return text