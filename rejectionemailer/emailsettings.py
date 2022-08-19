from mailjet_rest import Client
import csv
import os

with open('test.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t Hi {row["name"]} your email is {row["email"]} and your case was rejected dut to {row["rejectionreason"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')


#Mailjet API credentials
api_key = '9bf02177f912845b7c30e874d0a2e316'
api_secret = 'a4dd73f6dd3599f0f5affa6153d52343'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
# Mailjet message parameters
data = {
  'Messages': [
    {
      "From": {
        "Email": "daniel.horn90@gmail.com",
        "Name": "Daniel"
      },
      "To": [
        {
          "Email": {row["email"]},
          "Name": {row["name"]}
        }
      ],
      "Subject": "Test Send from Mailjet",
      "HTMLPart": '\t<h3>This is a test message with your rejection {row["rejectionreason"]}</h3><br />ignore this',
      "CustomID": "test-send"
    }
  ]
}
# Send message
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())
