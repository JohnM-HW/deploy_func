from flask import jsonify, request
import datetime
import os
import functions_framework
from google.cloud import firestore

def write_payload_to_file(payload):
    with open('/tmp/payload.txt', 'a') as f:
        f.write(payload + '\n')


def write_to_firestore(payload):
    db = firestore.Client()
    collection_name = 'deploy_register'

    doc_ref = db.collection(collection_name).document()
    doc_ref.set(payload)

    print('Payload inserted successfully into Firestore.')
    

def register(request):
    app_name = request.json['app_name']
    date = request.json['date']
    time = request.json['time']
    deployment_version = request.json['deployment_version']
    
    payload = f"{app_name} {date} {time} {deployment_version}"
    write_payload_to_file(payload)
    write_to_firestore(payload)

    return jsonify({'message': 'Payload received successfully!'})

