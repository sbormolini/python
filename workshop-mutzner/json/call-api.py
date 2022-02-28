import requests

# call
api_url = "https://localhost:7174/Customers/3fa85f64-5717-4562-b3fc-2c963f66afa6"
response = requests.get(api_url, verify=False)
customer = response.json()

# single object
if response.status_code == 200:
    print(customer["fullName"])