import os
import smtplib
from datetime import datetime
import pandas
import random

#email details
my_email = os.environ.get(my_email)
my_password = os.environ.get(my_password)
#get the time for now
today = datetime.now()
today_tuple= (today.month,today.day)

#use panda to read from csv file
data = pandas.read_csv("birthdays.csv")

#creating a dictionary
birthday_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}
#checking to see if today matches birthday
if today_tuple in birthday_dict:
    #gets specific row of birthday
    birthday_person = birthday_dict[today_tuple]
    #chooses a random letter amoung the availible letters
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    #searches letter to replace placeholder with name of person
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    #sending the birthday message as email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!!!\n\n{contents}!")
