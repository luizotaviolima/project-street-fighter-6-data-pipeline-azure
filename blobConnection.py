from azure.storage.blob import BlobServiceClient
import os
import glob

storageAccountName = "ststreetfighter6"
storageAccountKey = "STORAGE_ACCOUNT_KEY"
storageConnectionString = "STORAGE_CONNECTION_STRING"

folderName = "data/"

filePath = os.path.join(os.getcwd(), folderName)

print(filePath)

def upload_to_blog_storage(file_path, file_name):
    blob_service_client = BlobServiceClient.from_connection_string(storageConnectionString)
    blob_client = blob_service_client.get_blob_client(container=storageContainerName, blob=file_name)
    with open(file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)
        print(f"uploaded {file_name}")


for csvPathFile in glob.glob(filePath + '*.csv'):
    fileName = csvPathFile.split('/')[-1]
    upload_to_blog_storage(file_path = csvPathFile, file_name = fileName)



