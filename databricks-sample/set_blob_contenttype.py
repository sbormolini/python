#%pip install azure.identity
#%pip install azure.storage.blob


from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient, ContentSettings
import re


tenant_id = "<tenantId>"
client_id = "<clientId>"
client_secret = dbutils.secrets.get(scope="<databricksSecretScope>",key="<secretKey>")
storageaccount_name = "<storageAccountName>"
container_name = "output"

# Get a token credential for authentication
token_credential = ClientSecretCredential(
    tenant_id,
    client_id,
    client_secret
)

# Instantiate a BlobServiceClient using a token credential
blob_service_client = BlobServiceClient(account_url=f"https://{storageaccount_name}.blob.core.windows.net", credential=token_credential)

# Instantiate a ContainerClient
container_client = blob_service_client.get_container_client(container_name)

# List files in blob folder
blobs_list = container_client.list_blobs()
for blob in blobs_list:
    blob_client = blob_service_client.get_blob_client(container_name, blob)
    if re.match(r"^.*\.html$", blob.name):   
        blob_client.set_http_headers(
            content_settings = ContentSettings(
                content_type = "text/html"
            )
        )
