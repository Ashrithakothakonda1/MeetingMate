# Meetingmate

The Google Calendar Reminder Tool, named MeetingMate, is a Python application designed to automate the process of sending reminders to participants about upcoming one-on-one meetings scheduled in the H7 Accelerator Program. This tool seamlessly integrates with the Google Calendar API and Gmail API to authenticate users, access upcoming events, and send reminder emails automatically.

## Features

- **Authentication**: Authenticate MeetingMate using your Google account to access Google Calendar and Gmail services securely.
- **Send Reminders**: Automatically send reminder emails to all participants before their scheduled one-on-one meetings.
- **Customizable Email Template**: Customize the reminder email template to include participant's name, meeting summary, and scheduled time.
- **User-Friendly GUI**: Simple and intuitive graphical user interface (GUI) for easy operation and interaction.

## Installation

To install and run MeetingMate on your local machine, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine using Git:

   ```bash
   git clone https://github.com/Ashrithakothakonda1/Meetingmate.git
   ```

2. **Navigate to the Directory**: Change to the project directory:

   ```bash
   cd Meetingmate
   ```

3. **Install Dependencies**: Install the required Python dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup Google API Credentials**: Obtain your `credentials.json` file from the Google Cloud Console and place it in the project directory. Make sure to enable the Google Calendar API and Gmail API for your project.

5. **Run the Application**: Run the main Python script to start the application:

   ```bash
   python main.py
   ```

6. **Configure Email Template**: Customize the email template by editing the `config.json` file in the project directory. Update the `email_template` value with your desired email content.

7. Obtain a token.json file with your authentication token.

## Usage

1. **Authentication**: Upon launching the application, click on the "Authenticate with Google" button to authenticate MeetingMate with your Google account.

2. **Send Reminders**: Click on the "Send Reminders" button to trigger the automated process of sending reminder emails to participants of upcoming one-on-one meetings.

3. **Customize Email Template**: Customize the email template by modifying the content in the `config.json` file. Ensure to maintain placeholders like `{name}`, `{event_summary}`, and `{event_time}` for dynamic content insertion.

## GUI Usage

MeetingMate provides a graphical user interface (GUI) for easy interaction:

- Launch the application to access the main window displaying options for authentication and sending reminders.
- Click on the respective buttons to perform authentication and send reminders.

**Note**: Ensure that your `credentials.json` and `token.json` files are securely stored in the project directory. These files contain sensitive information required for authentication and access to Google services.


Feel free to customize this README with additional information or updates as needed. Happy automating with MeetingMate!
