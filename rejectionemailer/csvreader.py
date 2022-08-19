from mailjet_rest import Client
import csv
import os

api_key = '9bf02177f912845b7c30e874d0a2e316'
api_secret = 'a4dd73f6dd3599f0f5affa6153d52343'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')


with open('test.csv', mode='r') as csv_file:
    csv_reader=csv.reader(csv_file)
    line_count = 0
    for line in csv_reader:    
        if line_count == 0:
            print(f'Column names are {", ".join(line)}')
            line_count += 1
        data = {
          'Messages': [
            {
              "From": {
                "Email": "daniel.horn90@gmail.com",
                "Name": "Daniel"
              },
              "To": [
                {
                  "Email": '{}'.format(line["email"]),
                  "Name": '{}'.format(line["name"])
                }
              ],
              "Subject": "Test Send from Mailjet",
              "HTMLPart": '<h3>This is a test message with rejection {}</h3><br />ignore this'.format(line["rejectionreason"]),
              "CustomID": "test-send"
            }
          ]
        }
# Send message
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())

