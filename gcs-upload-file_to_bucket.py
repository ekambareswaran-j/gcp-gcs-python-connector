from google.cloud import storage
# Authenticate ourselves using the service account private key
path_to_private_key = './gcp-gcs-python-connector/key/crypto-avenue-398207-698b23aebf53.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)

bucket = storage.Bucket(client, 'example-bucket-1-eshwar')
# Name of the file on the GCS once uploaded
blob = bucket.blob('uploaded_sample.txt')
# Path of the local file
blob.upload_from_filename('./gcp-gcs-python-connector/data/uploaded_sample.txt')