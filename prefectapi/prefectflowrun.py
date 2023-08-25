import requests
import json

PREFECT_API_URL = "http://51.138.206.187:4200/api/flow_runs"

data = {
    "state": {
        "type": "SCHEDULED",
        "name": "string",
        "message": "Run started",
        "data": None,
        "state_details": {},
        "timestamp": "2019-08-24T14:15:22Z",
    },
    "name": "my-flow-run",
    "flow_id": "8adad023-4be1-4abf-af34-34de3aafd114",
    # Include any other required parameters here
    "tags": ["tag-1", "tag-2"],
    "idempotency_key": "string"
}

response = requests.post(PREFECT_API_URL, data=json.dumps(data))

if response.status_code == 200 | response.status_code == 201:
    print("Flow run created successfully: ", response.json())
elif response.status_code == 422:
    print("Validation error: ", response.json())
else:
    print(f"Unrecognized response status: {response.status_code}")
