import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

# Constants
url = "https://ps-internal.thoughtspot.cloud/api/rest/2.0/vcs/git/commits/deploy"
bearer_token = get.dotenv('AUTH_TOKEN_DEPLOY')

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {bearer_token}"
}

payload = {
    "branch_name": "deploy",
    "deploy_type": "DELTA",
    "deploy_policy": "ALL_OR_NONE",
    "comment": "This is deploying the changes to the orgs"
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Output
print(f"Status Code: {response.status_code}")
print("Response:")
print(json.dumps(response.json(), indent=2))
