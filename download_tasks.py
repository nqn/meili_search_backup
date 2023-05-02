import requests
import os

# Emit error if data directory isn't empty
if len(os.listdir('data')) != 0:
    raise Exception('Data directory is not empty')

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

base_url = os.environ.get('MEILISEARCH_URL', 'http://localhost:7700')
token = os.environ.get('MEILISEARCH_MASTER_TOKEN', 'masterKey')

print(f"Starting using {base_url} with token {token}")
limit = 10000
cursor = None
count = 0
while True:
    file_name = f'data/tasks_{count}.json'
    start_query = f'&from={cursor}' if cursor else ''
    url = f'{base_url}/tasks?limit={limit}{start_query}'
    print(f"Downloading tasks from {url} into {file_name}")
    r = requests.get(url, headers={
                     'Accept': 'application/json', 'Authorization': f'Bearer {token}'})
    payload = r.json()

    with open(file_name, 'w') as f:
        f.write(r.text)

    print(payload)

    if payload["next"] == None:
        print("Done")
        break

    cursor = payload["next"]
    count += 1
