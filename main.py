import os
import datetime
import json
import threading
import time
import tkinter as tk
from tkinter import messagebox
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import schedule
from email.mime.text import MIMEText
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly', 'https://www.googleapis.com/auth/gmail.send']

def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def send_reminders():
    creds = authenticate()
    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        messagebox.showinfo("Info", "No upcoming events found.")
        return

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        attendees = event.get('attendees', [])
        if attendees:
            for attendee in attendees:
                email = attendee['email']
                send_email(creds, email, event)
        else:
            print(f"No attendees found for event: {event['summary']}")

def load_config():
    with open('config.json', 'r') as file:
        return json.load(file)

def send_email(creds, to_email, event):
    service = build('gmail', 'v1', credentials=creds)
    
    config = load_config()
    template = config["email_template"]
    message_text = template.format(
        name=to_email,
        event_summary=event['summary'],
        event_time=event['start'].get('dateTime', event['start'].get('date'))
    )
    
    message = MIMEText(message_text)
    message['to'] = to_email
    message['subject'] = f"Reminder: Upcoming Meeting - {event['summary']}"
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    body = {'raw': raw_message}
    try:
        message = service.users().messages().send(userId="me", body=body).execute()
        print(f"Message sent to {to_email} with Id: {message['id']}")
    except Exception as error:
        print(f"An error occurred: {error}")

def create_gui():
    root = tk.Tk()
    root.title("MeetingMate")
    root.geometry("400x200")
    
    label = tk.Label(root, text="Google Calendar Reminder Tool", font=("Helvetica", 16))
    label.pack(pady=20)
    
    reminder_button = tk.Button(root, text="Send Reminders", command=send_reminders, font=("Helvetica", 14))
    reminder_button.pack(pady=20)
    
    root.mainloop()

def job():
    send_reminders()

def run_scheduler():
    schedule.every().day.at("08:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # Start GUI in a separate thread
    gui_thread = threading.Thread(target=create_gui)
    gui_thread.start()

    # Run scheduler in the main thread
    run_scheduler()
