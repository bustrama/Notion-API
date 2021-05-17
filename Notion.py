from Database import Database
import requests

from Page import Page


class Notion:
    def __init__(self, auth_token):
        self.headers = {'Authorization': 'Bearer ' + auth_token}

    def getDatabase(self, database_id):
        r = requests.get('https://api.notion.com/v1/databases/' + database_id, headers=self.headers)
        if r.status_code == 200:
            return Database(r.json())
        else:
            return 'Bad Request'

    def queryDatabase(self, database_id):
        r = requests.post('https://api.notion.com/v1/databases/' + database_id + '/query', headers=self.headers)
        if r.status_code == 200:
            results = []
            for result in r.json()['results']:
                results.append(Page(result))
            return results
        else:
            return 'Bad Request'

    def listDatabases(self):
        r = requests.get('https://api.notion.com/v1/databases', headers=self.headers)
        if r.status_code == 200:
            return r.json()
        else:
            return 'Bad Request'

    def getPage(self, page_id):
        r = requests.get('https://api.notion.com/v1/pages/page_id' + page_id, headers=self.headers)
        if r.status_code == 200:
            return Page(r.json())
        else:
            return 'Bad Request'

    def getBlock(self, block_id):
        r = requests.get('https://api.notion.com/v1/blocks/' + block_id + '/children', headers=self.headers)
        if r.status_code == 200:
            return r.json()
        else:
            return 'Bad Request'

    def searchPage(self, page_name):
        params = {
            'query': page_name
        }
        r = requests.get('https://api.notion.com/v1/search',
                         headers=self.headers, params=params)
        if r.status_code == 200:
            return r
        else:
            return 'Bad Request'
