# https://developers.notion.com/reference/page#page-property-value
from datetime import datetime

from Property import PropertyType, Option, Property
import RichText
from User import Person


def GetPropertyValue(json, prop_name):
    if json['type'] == PropertyType.Title:
        return TitleValue(json, prop_name)
    elif json['type'] == PropertyType.Rich_text:
        return TextValue(json, prop_name)
    elif json['type'] == PropertyType.Number:
        return NumberValue(json, prop_name)
    elif json['type'] == PropertyType.Select:
        return SelectValue(json, prop_name)
    elif json['type'] == PropertyType.Multi_select:
        return MultiSelectValue(json, prop_name)
    elif json['type'] == PropertyType.Date:
        return DateValue(json, prop_name)
    elif json['type'] == PropertyType.Formula:
        return FormulaValue(json, prop_name)
    elif json['type'] == PropertyType.Relation:
        return RelationValue(json, prop_name)
    elif json['type'] == PropertyType.Rollup:
        return RollupValue(json, prop_name)
    elif json['type'] == PropertyType.People:
        return PeopleValue(json, prop_name)
    elif json['type'] == PropertyType.Created_by:
        return CreatedByValue(json, prop_name)
    elif json['type'] == PropertyType.Last_edited_by:
        return LastEditedByValue(json, prop_name)
    else:
        return PropertyValue(json, prop_name)


class PropertyValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.value = json[json['type']]
        if self.type == 'last_edited_time' or self.type == 'created_time':
            self.value = datetime.strptime(self.value, "%Y-%m-%dT%H:%M:%S.%f%z")


class TitleValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.title = []
        for t in json['title']:
            self.title.append(RichText.GetRichText(t))


class TextValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.text = []
        for t in json['text']:
            self.text.append(RichText.GetRichText(t))


class NumberValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.number = json['number']


class SelectValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.select = Option(json['select']['id'], json['select']['name'], json['select']['color'])


class MultiSelectValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.options = []
        if 'options' in json['multi_select']:
            for option in json['multi_select']['options']:
                self.options.append(
                    Option(
                        option['id'],
                        option['name'],
                        option['color']
                    )
                )


class DateValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.start = json['date']['start']
        self.end = json['date']['end']


class FormulaValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.formula_type = json['formula']['type']
        if json['formula']['type'] == 'date':
            self.formula_start = json['formula']['date']['start']
            self.formula_end = json['formula']['date']['end']
        else:
            self.formula_value = json['formula'][json['formula']['type']]


class RelationValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.pages = []
        for page in json['relation']:
            self.pages.append(page['id'])


class RollupValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.relation_property_name = json['relation_property_name']
        self.relation_property_id = json['relation_property_id']
        self.rollup_property_name = json['rollup_property_name']
        self.rollup_property_id = json['rollup_property_id']
        self.function = json['function']


class PeopleValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.people = []
        for p in json['people']:
            self.people.append(Person(p['id'], p['name'], p['avatar_url'], p['person']['email']))


class CreatedByValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        p = json['created_by']
        self.created_by = Person(p['id'], p['name'], p['avatar_url'], p['person']['email'])


class LastEditedByValue(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        p = json['last_edited_by']
        self.last_edited_by = Person(p['id'], p['name'], p['avatar_url'], p['person']['email'])
