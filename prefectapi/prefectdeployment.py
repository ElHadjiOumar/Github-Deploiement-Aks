import requests
import json

PREFECT_API_URL = "http://51.138.206.187:4200/api/deployments"

data = {
    "name": "my-deployment",
    "flow_id": "8adad023-4be1-4abf-af34-34de3aafd114",
    "is_schedule_active": True,
    "parameters": {},
    "tags": ["tag-1", "tag-2"],
    # Include any other required parameters here
    "work_pool_name": "default-agent-pool",
}

response = requests.post(PREFECT_API_URL, data=json.dumps(data))

if response.status_code == 200 | response.status_code == 201:
    print("Deployment created successfully: ", response.json())
elif response.status_code == 422:
    print("Validation error: ", response.json())
else:
    print(f"Unrecognized response status: {response.status_code}")
