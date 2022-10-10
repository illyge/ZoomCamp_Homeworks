# Before running this, please run:
# gunicorn --bind 0.0.0.0:9696 credit_service:app

import requests

def call_credit_service():
    client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}
    print(requests.post('http://localhost:9696/proba', json=client).json())

if __name__ == '__main__':
    call_credit_service()
