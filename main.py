import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'data-fellowship-7-363123-69b0298e444b.json'

storage_client = storage.Client()

# Create a New Bucket
bucket_name = 'data_fellowship_7'
bucket = storage_client.bucket(bucket_name)
bucket_location = 'US'
bucket = storage_client.create_bucket(bucket)

# Upload File
my_bucket = storage_client.get_bucket('data_fellowship_7')

def upload_to_bucket(blob_name, file_path, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob

file_path = r'D:\KURSUS\IYKRA\Tugas\Tugas1'
upload_to_bucket('Tugas 1', 'tugas1.csv', 'data_fellowship_7')