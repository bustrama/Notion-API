# https://developers.notion.com/reference/page

from datetime import datetime

import Property
import PropertyValue


class Page:
    def __init__(self, page):
        self.object = 'page'
        self.id = page['id']
        self.created_time = datetime.strptime(page['created_time'], "%Y-%m-%dT%H:%M:%S.%f%z")
        self.last_edited_time = datetime.strptime(page['last_edited_time'], "%Y-%m-%dT%H:%M:%S.%f%z")

        if page['parent']['type'] == 'database_id':
            self.parent = Parent(page['parent']['type'], page['parent']['database_id'])
        elif page['parent']['type'] == 'page_id':
            self.parent = Parent(page['parent']['type'], page['parent']['page_id'])
        else:
            self.parent = Parent(page['parent']['type'])
        self.archived = page['archived']

        self.properties = []
        for prop in page['properties']:
            self.properties.append(PropertyValue.GetPropertyValue(page['properties'][prop], prop))


class Parent:
    def __init__(self, parent_type, parent_id=''):
        self.id = parent_id
        self.type = parent_type
