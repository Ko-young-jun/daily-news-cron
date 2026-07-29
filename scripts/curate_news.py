import os
from datetime import datetime

print("Script started")
api_key = os.getenv('NEWSAPI_KEY')
print(f"API Key set: {bool(api_key)}")

filename = f"news_{datetime.now().strftime('%Y-%m-%d')}.md"
print(f"Creating file: {filename}")

with open(filename, 'w') as f:
    f.write(f"# Daily News - {datetime.now().strftime('%Y-%m-%d')}\n")
    f.write("Successfully created!\n")

print(f"File created: {filename}")
