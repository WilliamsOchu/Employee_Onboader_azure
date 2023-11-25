import csv, os
import smtplib, ssl
from faker import Faker




# Generate 1 random employee data using the faker module
fake = Faker()
data = []
for _ in range(1):
    name = fake.name()
    contact = fake.phone_number()
    department = fake.random_element(elements=('Finance', 'Human Resources', 'Marketing', 'IT', 'Operations', 'Research and Development', 'Maintenance'))
    name_splitter= name.split(' ')
    mail_address = name_splitter[0]+name_splitter[1]+fake.random_element(elements=('@outlook.com', '@gmail.com', '@yahoo.com', '@protonmail.com'))   
    data.append([name, contact, department, mail_address])




# Write the generated data to a CSV file
with open('organization_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Contact", "Department", "Mail"])
    writer.writerows(data)




## Read and extract generated data from CSV
with open('organization_data.csv') as csvfile2:
    reader2 = csv.DictReader(csvfile2)
    for row in reader2:
        print(row)

names = row['Name']
contact = row['Contact']
dept = row['Department']
email_add = row['Mail']




## Send an email to the IT admin with new employee details
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ochuwilliamsirawo@gmail.com"  # Enter your address
receiver_email = "williamsochu001@gmail.com"  # Enter receiver address
password = os.environ['SMTP_pass']
message = """\
Subject: Hi there

Here are the details of the new employee. \nName:{} \nPhone:{} \nDepartment:{} \nEmail_Address: {}""" .format(names, contact, dept, email_add)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print('Email sent succesfully')
