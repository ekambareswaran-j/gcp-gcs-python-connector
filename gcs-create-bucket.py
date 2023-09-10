from google.cloud import storage

# Authenticate ourselves using the service account private key
path_to_private_key = './gcp-gcs-python-connector/key/crypto-avenue-398207-698b23aebf53.json'
client = storage.Client.from_service_account_json(json_credentials_path=path_to_private_key)

bucket = client.create_bucket('example-bucket-1-eshwar')
print(f'Bucket with name [{bucket.name}] created on GCS!')