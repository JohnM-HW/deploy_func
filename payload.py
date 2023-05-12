import requests
import json

def send_payload_to_cloud_function(app_name, date, time, deployment_version):
    payload = {'app_name': app_name, 'date': date, 'time': time, 'deployment_version': deployment_version}
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://us-central1-hw-sre.cloudfunctions.net/register', data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        print('Payload sent successfully!')
    else:
        print('Error sending payload.')



send_payload_to_cloud_function('myapp', '2023-05-12', '12:00:00', 'v1.0')