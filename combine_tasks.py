# Load json files from data directory and combine them into a single file
#
# Usage: python combine_tasks.py
#
# Output: data/tasks.json
#

import json
import os

# Emit error if data directory isn't empty
if len(os.listdir('data')) == 0:
    raise Exception('Data directory is empty')

# Load json files from data directory
tasks = []
for file_name in os.listdir('data'):
    if file_name.endswith('.json'):
        with open(f'data/{file_name}') as f:
            content = json.load(f)
            tasks.extend(content["results"])

# Write combined tasks to data/tasks.json
with open('data/tasks.json', 'w') as f:
    json.dump(tasks, f)