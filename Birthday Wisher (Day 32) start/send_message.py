import random
import datetime as dt
import smtplib

my_email = "irinasaratovska@gmail.com"
password = "XXX"

content = open("quotes.txt", "r")
line = content.readlines()
advice_of_the_day = random.choice(line)

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 1:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="volodymyrsaratovskyy@yahoo.com",
            msg=f"Subject: Advice of the day\n\n{advice_of_the_day}")

