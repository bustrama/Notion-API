# https://developers.notion.com/reference/database

from datetime import datetime
from RichText import *
import Property
import RichText


class Database:
    def __init__(self, json):
        self.object = 'database'
        self.id = json['id']
        self.created_time = datetime.strptime(json['created_time'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.last_edited_time = datetime.strptime(json['last_edited_time'], "%Y-%m-%dT%H:%M:%S.%f%z")

        self.title = []
        for rich_text in json['title']:
            self.title.append(RichText.GetRichText(rich_text))

        self.properties = []
        for prop in json['properties']:
            self.properties.append(Property.GetProperty(json['properties'][prop], prop))
