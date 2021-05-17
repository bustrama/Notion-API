# https://developers.notion.com/reference/database

from datetime import datetime
from RichText import *
import Property
import RichText


class Database:
    def __init__(self, database):
        self.object = 'database'
        self.id = database['id']
        self.created_time = datetime.strptime(database['created_time'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.last_edited_time = datetime.strptime(database['last_edited_time'], "%Y-%m-%dT%H:%M:%S.%f%z")

        self.title = []
        for rich_text in database['title']:
            self.title.append(RichText.GetRichText(rich_text))

        self.properties = []
        for prop in database['properties']:
            self.properties.append(Property.GetProperty(database['properties'][prop], prop))
