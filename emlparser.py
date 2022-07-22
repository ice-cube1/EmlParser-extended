import datetime
import json
import eml_parser
import os
import pandas as pd

# I have no idea what this does. I copied it from the eml_parser pypi's site.
def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial

    
#Blank list in which we'll add our data
adresses = []
timestamps = []
subjects = []

#Folder in which we have our emails
mail_folder = "./mail_folder/"
files = os.listdir(mail_folder)

#We iterate over every email
for file in files:

    with open(mail_folder+file, 'rb') as fhdl:
        raw_email = fhdl.read()

    #Decode the email
    ep = eml_parser.EmlParser()
    parsed_eml = ep.decode_email_bytes(raw_email)
    
    #Convert the decoded email to JSON
    completejson = (json.dumps(parsed_eml, default=json_serial))
    dicc = json.loads(completejson)

    #For some reason, a few of my .emls didn't seem to have a sender.
    try:
        print(dicc['header']['from'])
        adresses.append(dicc['header']['from'])
        print(dicc['header']['date'])
        timestamps.append(dicc['header']['date'])
        print(dicc['header']['subject'])
        subjects.append(dicc['header']['subject'])
    except:
        print("\n")

df_books = pd.DataFrame({'Sender':adresses ,'Timestamp': timestamps, 'Subject': subjects})
df_books.to_csv('exported_email_list.csv', index=False)
