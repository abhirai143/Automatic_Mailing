import smtplib
import datetime as dt
import random

my_email = "abhiopg@gmail.com"

my_password = "sjarmlmbzalazzfk"


with open("quotes.txt") as quotes_file:

    all_quotes = quotes_file.readlines()

now = dt.datetime(year=2023, month=6, day=25)

print(now.weekday())

random_quotes = random.choice(all_quotes)

if now.weekday() == 0:

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()

        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email,
                            to_addrs="abhishekraibagi81@gmail.com",
                            msg=f"Subject:Monday Quotes\n\n {random_quotes}")







