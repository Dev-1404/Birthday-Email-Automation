# Birthday-Email-Automation (Python)

This is a simple Python automation project that sends birthday wishes automatically via email by reading teacher details from a CSV file and checking whose birthday is today.

The goal of this project is to demonstrate how Python can be used for real-life automation tasks like email sending, file handling, and scheduling-ready scripts.


# Features:
- Reads teacher details from a CSV file
- Checks whose birthday is today
- Sends personalized birthday emails
- Supports HTML + plain text emails
- Maintains a log file for tracking activity
- Has a DRY RUN mode to test without sending emails

# Project Structure:
```text
teacher_birthday_automation/
├── data/
│   └── teachers.csv
└── scripts/
    ├── birthday_automation.log
    └── birthday_matcher.py
```

# CSV File Format:
The CSV file should be inside the "data" folder and must have these columns:
           Name,BirthDate,Email

Note: BirthDate must be in the DD-MM-YYYY format

# Configuration(Important):
Inside the Python file, update these:
SENDER_EMAIL = "your_email_id"
APP_PASSWORD = "16_char_app_password"
DRY_RUN = False

# App Password
If you are using Gmail, you must:
1. Enable 2-step verification
2. Generate an App Password
3. Use that password here (not your real Gmail password)

# How to Run
1. Make sure Python is installed (Python 3.8+ recommended)
2. Open terminal in project scripts folder
3. Run: python birthday_matcher.py

If today matches any birthday in the CSV, an email will be sent.

# Testing Without Sending Emails
To test safely, set:
DRY_RUN = True
This will:
- Print email content in terminal
- NOT send real emails

# Log File
All actions are saved in: birthday_automation.log
It records:
- Program start & end
- Emails sent
- Errors (if any)
This helps in debugging and monitoring automation.

# Why This Project?

This project was built to practice and demonstrate:
- Python automation
- File handling with CSV
- Email protocols (SMTP)
- Writing clean and modular code
- Real-world problem solving using scripts

It is part of a larger plan to convert this into a complete automated system in future versions.

# Note:
- I have kept the teachers.csv file empty here
- The log file contains dummy data


I'll be happy to discuss alternate approaches, more additions to this project.

