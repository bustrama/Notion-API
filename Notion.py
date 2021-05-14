from APIs import KEYS
import requests


headers = {'Authorization': 'Bearer ' + KEYS.NOTION_TOKEN}
db_id = KEYS.DATABASE_ID


def getDatabase():
    r = requests.get('https://api.notion.com/v1/databases/'+db_id, headers=headers)
    if r.status_code == 200:
        return r.json()

