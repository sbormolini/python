import requests
import json
import warnings
import sys

# workaround to supress warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")

# api ~\Workspace\.NET\ApiEndpointsDemo
api_url = 'https://localhost:7174/'

# custom class
class Customer:
    def __init__(self, id, fullname):
        self.id = id
        self.fullname = fullname

# helper functions
def CreateCustomers(base_url, customers):
    "This prints a passed string into this function"
    headers = {
        'Content-type':'application/json', 
        'Accept':'application/json'
    }  
    uri = base_url + 'Customers'
    for c in customers:
        response = requests.post(
            uri, 
            headers=headers, 
            data=json.dumps(c.__dict__), 
            verify=False
        )
        if response.status_code == 201:
            print(f'Created customer: {c.fullname}')
        else:
            print(f'Failed to create customer: {c.fullname}! Error code {response.status_code}')

# main function
if __name__ == '__main__':
    # create two new customer objects
    c1 = Customer('f50ec0b7-f960-400d-91f0-c42a6d44e3d0', 'Microsoft')
    c2 = Customer('c1c0be67-e14f-4664-8a47-8ab26e15d444', 'Google')

    # create customer in api
    CreateCustomers(api_url, [c1, c2])