from google.cloud import firestore
from datetime import datetime


class FirestoreDataSender:
    def __init__(self):
        # Initialize the Firestore client
        #cred = credentials.Certificate(service_account_key_path)
        #firebase_admin.initialize_app(cred, {'projectId': project_id})
        self.db = firestore.Client()

    def send_data(self, date, deployment_version, app_name, rollback_version):
        # Create a document reference with an auto-generated ID
        doc_ref = self.db.collection('deployments').document()
        timestamp = firestore.SERVER_TIMESTAMP


        # Create the data dictionary
        data = {
            'timestamp': timestamp,
            'deployment_version': deployment_version,
            'app_name': app_name,
            'rollback_version': rollback_version
        }

        # Write the data to Firestore
        doc_ref.set(data)


def read_deploy_register():
    # Get a reference to the "deploy_register" collection
    db = firestore.Client()
    collection_ref = db.collection("deployments")

    # Retrieve all documents in the collection
    docs = collection_ref.get()

    # Iterate over the documents
    for doc in docs:
        print(f"Document ID: {doc.id}")
        print(f"Data: {doc.to_dict()}")



sender = FirestoreDataSender()
sender.send_data('2023-05-24', 'v1.0.1', 'John', 'v1.0.0')
print("Data Sent")

print("Reading Firestore Doc")
read_deploy_register()