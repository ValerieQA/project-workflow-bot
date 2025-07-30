# notion.py

import requests
from config import NOTION_TOKEN, NOTION_DATABASE_ID

NOTION_API_URL = "https://api.notion.com/v1/pages"
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def create_ticket(title, status="Not started"):
    payload = {
        "parent": {"database_id": NOTION_DATABASE_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": title}}]
            },
            "Status": {
                "status": {"name": status}
            }
        }
    }

    response = requests.post(NOTION_API_URL, headers=HEADERS, json=payload)

    # NEW: Logging the outcome
    if response.status_code == 200 or response.status_code == 201:
        print("✅ Ticket created successfully!")
    else:
        print("❌ Failed to create ticket!")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
