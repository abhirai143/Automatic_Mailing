import pandas
import datetime as dt
import smtplib
import random


my_email = "abhiopg@gmail.com"

my_password = "sjarmlmbzalazzfk"

now = dt.datetime.now()
date_tuple = (now.month, now.day)


birthday_data = pandas.read_csv("birthdays.csv")

birthday_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in birthday_data.iterrows()}


if date_tuple in birthday_dict:

    birthday_person = birthday_dict[date_tuple]

    generate_number = random.randint(1, 3)

    file_path = f"letter_templates/letter_{generate_number}.txt"

    letter = open(file_path).read()

    update_letter = letter.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()

        connection.login(user=my_email, password=my_password)

        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n {update_letter}")




