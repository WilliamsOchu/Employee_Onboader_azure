## Import necessary modules 
import json
import os
from faker import Faker


## Generate a class for the faker module to create random users
fake = Faker()

## Create a dictionary to store generated random names and details 
data_dict ={}

## Create random employee details 
for _ in range(1):
    name = fake.name()
    contact = fake.phone_number()
    department = fake.random_element(elements=('Finance', 'Human Resources', 'IT', 'Operations'))
    name_splitter= name.split(' ')
    mail_address = name_splitter[0]+name_splitter[1]+fake.random_element(elements=('@outlook.com', '@gmail.com', '@yahoo.com', '@protonmail.com'))   
    ## Create details for creating user identity in Entra ID
    mail_nickname_init = mail_address.split('@')
    mail_nickname = name_splitter[0] + name_splitter[1] + '_' + mail_nickname_init[1] + '#EXT#'
    user_princ = mail_nickname + os.environ['domain']
    full_name = name_splitter [0]+ '_' + name_splitter[1]
    full_name_lower =  name_splitter [0] + name_splitter[1]



    ## Create groupid
    if department == 'Finance':
        group_id = os.environ['financeid']

    elif department == 'Human Resources':
        group_id = os.environ['hrid']

    elif department == 'IT':
        group_id = os.environ['itid']

    else:
        group_id = os.environ['operationsid']


    ## Add the items to a dictionary
    data_dict["name"]=name
    data_dict["phone"]=contact
    data_dict['dept']=department
    data_dict['email']=mail_address
    data_dict['first_name']=name_splitter[0]
    data_dict['last_name']=name_splitter[1]
    data_dict['mail_nickname']=mail_nickname
    data_dict['user_princ_name']=user_princ
    data_dict['group_id']=group_id
    data_dict['fullname']=full_name
    data_dict['fullname_lower']=full_name_lower.lower()

## Write the generated details to a CSV file
with open('employee_json.json', 'w') as file:
    json.dump(data_dict, file)


