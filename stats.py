# Load tasks.json file from data directory and print the number of tasks
#
# Usage: python stats.py
#
# Output: Number of tasks
#

import json
import os

# Emit error if data directory doesn't exists
if not os.path.exists('data'):
    raise Exception('Data directory does not exist')

# Load combined tasks from data/tasks.json
tasks = []
with open('data/tasks.json') as f:
    tasks = json.load(f)

# Print number of tasks
print(f"Number of tasks: {len(tasks)}\n")

# Count number of tasks by status
status_count = {}
for task in tasks:
    status = task["status"]
    if status not in status_count:
        status_count[status] = 0
    status_count[status] += 1

# Print number of tasks by status
print("Number of tasks by status:")
for status, count in status_count.items():
    print(f"{status}: {count}")