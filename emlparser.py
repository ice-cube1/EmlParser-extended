import datetime
import json
import eml_parser
import os

def json_serial(obj):
  if isinstance(obj, datetime.datetime):
      serial = obj.isoformat()
      return serial

adresses = []

files = os.listdir("/path/to/your/.emls/")

for file in files:

    with open("/path/to/your/.emls/"+file, 'rb') as fhdl:
        raw_email = fhdl.read()

    ep = eml_parser.EmlParser()
    parsed_eml = ep.decode_email_bytes(raw_email)
    completejson = (json.dumps(parsed_eml, default=json_serial))
    dicc = json.loads(completejson)

    try:
        print(dicc['header']['from'])
        adresses.append(dicc['header']['from'])
    except:
        print("\n")

adresses = list(dict.fromkeys(adresses))

with open("/path/to/your/output.csv", 'w') as f:
    for adress in adresses:
        f.write(str(adresses)+"\n")
