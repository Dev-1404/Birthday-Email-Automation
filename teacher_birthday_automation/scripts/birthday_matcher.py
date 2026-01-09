import csv
import smtplib
from datetime import datetime
from email.message import EmailMessage
import os

LOG_FILE_PATH = "birthday_automation.log"
CSV_FILE_PATH = "../data/teachers.csv"


DRY_RUN = False   

SENDER_EMAIL = "your_email_id"
APP_PASSWORD = "16_char_app_password"


def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def get_today_date():
    today = datetime.now()
    return today.day, today.month


def parse_birthdate(birthdate_str):
    return datetime.strptime(birthdate_str, "%d-%m-%Y")


def read_teachers_from_csv(file_path):
    teachers = []

    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)

        for row in reader:
            birthdate = parse_birthdate(row["BirthDate"].strip())

            teachers.append({
                "name": row["Name"].strip(),
                "email": row["Email"].strip(),
                "birth_day": birthdate.day,
                "birth_month": birthdate.month
            })

    return teachers


def find_today_birthdays(teachers, today_day, today_month):
    birthday_teachers = []

    for teacher in teachers:
        if teacher["birth_day"] == today_day and teacher["birth_month"] == today_month:
            birthday_teachers.append(teacher)

    return birthday_teachers


# -------- EMAIL CONTENT --------
def generate_email_content(teacher_name):
    subject = "🎉 Happy Birthday!"

    # Plain text fallback (important for some clients)
    text_body = f"""
Dear {teacher_name},

Wishing you a very Happy Birthday 🎂🎉

May your day be filled with joy, good health, and success.

Warm regards,
Birthday Automation System
"""

    # HTML version
    html_body = f"""
<html>
  <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
    <div style="max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 8px;">
      <h2 style="color: #2c3e50;">🎉 Happy Birthday, {teacher_name}! 🎉</h2>

      <p style="font-size: 15px;">
        Wishing you a very happy birthday! May your day be filled with
        <b>joy, good health, and success</b>.
      </p>

      <p style="font-size: 14px;">
        Thank you for your dedication and the positive impact you make every day.
      </p>

      <br>
      <p style="font-size: 14px;">
        Warm regards,<br>
        <b>Birthday Automation System</b>
      </p>
    </div>
  </body>
</html>
"""

    return subject, text_body, html_body




def send_email(receiver_email, subject, text_body, html_body):
    msg = EmailMessage()
    msg["From"] = SENDER_EMAIL
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.set_content(text_body)           # fallback
    msg.add_alternative(html_body, subtype="html")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)



def main():
    log("Program started.")

    today_day, today_month = get_today_date()
    teachers = read_teachers_from_csv(CSV_FILE_PATH)
    today_birthdays = find_today_birthdays(teachers, today_day, today_month)

    if not today_birthdays:
        print("No birthdays today.")
        log("No birthdays today.")
        return

    print("Today's Birthdays Found:\n")

    for teacher in today_birthdays:
        subject, text_body, html_body = generate_email_content(teacher["name"])

        print("--------------------------------------------------")
        print(f"To      : {teacher['email']}")
        print(f"Subject : {subject}")
        print("Body:")
        print(text_body.strip())
        print("--------------------------------------------------")

        if not DRY_RUN:
            try:
                send_email(teacher["email"], subject, text_body, html_body)
                print("Email sent successfully.\n")
                log(f"Email sent to {teacher['email']}")
            except Exception as e:
                print("Failed to send email.")
                print("Error:", e, "\n")
                log(f"Failed to send email to {teacher['email']} | Error: {e}")
        else:
            print("DRY RUN: Email not sent.\n")
    log("Program finished.\n")

if __name__ == "__main__":
    main()
