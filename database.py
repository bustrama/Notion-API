import datetime


class Database:
    def __init__(self, json):
        self.object = json['object']
        self.id = json['id']
        self.created_time = datetime.datetime.strptime(json['created_time'], "%Y-%m-%dT%H:%M:%S%z")
        self.last_edited_time = datetime.datetime.strptime(json['last_edited_time'], "%Y-%m-%dT%H:%M:%S%z")
        self.title = json['title']
        self.properties = json['properties']
