import csv
import json
import os
import requests

# Constants
CSV_FILE = 'tmls.csv'
COLUMN_NAME = 'tmls'
API_URL = 'https://ps-internal.thoughtspot.cloud/api/rest/2.0/vcs/git/branches/commit'
AUTH_TOKEN = "YWRpdHlhLnBva2hhcmthckB0aG91Z2h0c3BvdC5jb206SkhOb2FYSnZNU1JUU0VFdE1qVTJKRFV3TURBd01DUmliM2w2ZDNsTE1WQlRkazVaTjJwdWJHYzVPVmRCUFQwa04wNUllWFprVkc5MVVuWmxMM05NWlVGc1YyMVhUR3RHYlRKbWJUQXJReTlUVTIxdVRUUnVabmx2TkQw"
BRANCH_NAME = 'commit'
RESPONSE_DIR = 'response'

# Ensure the response directory exists
os.makedirs(RESPONSE_DIR, exist_ok=True)

# Read GUIDs from CSV
with open(CSV_FILE, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        guid = row[COLUMN_NAME]
        payload = {
            "metadata": [
                {"identifier": guid}
            ],
            "delete_aware": True,
            "comment": "committed via cicd script",
            "branch_name": BRANCH_NAME
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {AUTH_TOKEN}"
        }

        try:
            response = requests.post(API_URL, headers=headers, json=payload)
            response.raise_for_status()  # Raises error if status >= 400
            print(f"✅ Success for GUID {guid}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Failure for GUID {guid}: {e}")

        # Save the response
        response_filename = os.path.join(RESPONSE_DIR, f"response_{guid[:8]}.json")
        with open(response_filename, 'w') as f:
            json.dump(response.json(), f, indent=2)
