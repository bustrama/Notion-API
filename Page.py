# https://developers.notion.com/reference/page

from datetime import datetime


class Page:
    def __init__(self, page_id, time_created, time_last_edited, arch, props):
        self.object = 'page'
        self.id = page_id
        self.created_time = datetime.strptime(time_created, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.last_edited_time = datetime.strptime(time_last_edited, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.archive = arch
        self.properties = props
