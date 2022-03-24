import datetime
import json
import eml_parser
import os

# I have no idea what this does. I copied it from the eml_parser pypi's site.
def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial

    
#Blank list in which we'll add our data
adresses = []

#Folder in which we have our emails
files = os.listdir("/path/to/your/.emls/")

#We iterate over every email
for file in files:

    with open("/path/to/your/.emls/"+file, 'rb') as fhdl:
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
    except:
        print("\n")

#We turn our list into a dictionary and then back to a list to get rid of the duplicates
adresses = list(dict.fromkeys(adresses))

#Final output
with open("/path/to/your/output.csv", 'w') as f:
    for adress in adresses:
        f.write(str(adresses)+"\n")
