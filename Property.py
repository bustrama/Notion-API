# https://developers.notion.com/reference/database#database-property


def GetProperty(json, prop_name):
    if json['type'] == PropertyType.Number:
        return Number(
            json['id'],
            prop_name,
            json['number']['format']
        )
    elif json['type'] == PropertyType.Select:
        return Select(
            json['id'],
            prop_name,
            json['select']['options']
        )
    elif json['type'] == PropertyType.Multi_select:
        return MultiSelect(
            json['id'],
            prop_name,
            json['multi_select']['options']
        )
    elif json['type'] == PropertyType.Formula:
        return Formula(
            json['id'],
            prop_name,
            json['formula']['expression']
        )
    elif json['type'] == PropertyType.Relation:
        return Relation(
            json['id'],
            prop_name,
            json['database_id'],
            json['synced_property_name'],
            json['synced_property_id']
        )
    elif json['type'] == PropertyType.Rollup:
        return Rollup(
            json['id'],
            prop_name,
            json['relation_property_name'],
            json['relation_property_id'],
            json['rollup_property_name'],
            json['rollup_property_id'],
            json['function']
        )
    else:
        return Property(
            json['id'],
            prop_name,
            json['type']
        )


class Property:
    def __init__(self, prop_id, prop_name, prop_type):
        self.id = prop_id
        self.name = prop_name
        self.type = prop_type


class PropertyType:
    Title = 'title'
    Rich_text = 'rich_text'
    Number = 'number'
    Select = 'select'
    Multi_select = 'multi_select'
    Date = 'date'
    People = 'people'
    File = 'file'
    Checkbox = 'checkbox'
    Url = 'url'
    Email = 'email'
    Phone_number = 'phone_number'
    Formula = 'formula'
    Relation = 'relation'
    Rollup = 'rollup'
    Created_time = 'created_time'
    Created_by = 'created_by'
    Last_edited_time = 'last_edited_time'
    Last_edited_by = 'last_edited_by'


class Number(Property):
    def __init__(self, prop_id, prop_name, number_format):
        super().__init__(prop_id, prop_name, PropertyType.Number)
        self.format = number_format


class NumberFormat:
    Number = 'number'
    Number_with_commas = 'number_with_commas'
    Percent = 'percent'
    Dollar = 'dollar'
    Euro = 'euro'
    Pound = 'pound'
    Yen = 'yen'
    Ruble = 'ruble'
    Rupee = 'rupee'
    Won = 'won'
    Yuan = 'yuan'


class Select(Property):
    def __init__(self, prop_id, prop_name, options_arr):
        super().__init__(prop_id, prop_name, PropertyType.Select)
        self.options = []
        for option in options_arr:
            self.options.append(
                Option(
                    option['id'],
                    option['name'],
                    option['color']
                )
            )


class MultiSelect(Property):
    def __init__(self, prop_id, prop_name, options_arr):
        super().__init__(prop_id, prop_name, PropertyType.Multi_select)
        self.options = []
        for option in options_arr:
            self.options.append(
                Option(
                    option['id'],
                    option['name'],
                    option['color']
                )
            )


class Option:
    def __init__(self, option_id, option_name, option_color):
        self.id = option_id
        self.name = option_name
        self.color = option_color


class OptionColor:
    Default = 'default'
    Gray = 'gray'
    Brown = 'brown'
    Orange = 'orange'
    Yellow = 'yellow'
    Green = 'green'
    Blue = 'blue'
    Purple = 'purple'
    Pink = 'pink'
    Red = 'red'


class Date(Property):
    def __init__(self, prop_id, prop_name, json):
        super().__init__(prop_id, prop_name, PropertyType.Date)
        self.start = json['start']
        self.end = json['end']


class Formula(Property):
    def __init__(self, prop_id,  prop_name, prop_expression):
        super().__init__(prop_id, prop_name, PropertyType.Formula)
        self.expression = prop_expression


class Relation(Property):
    def __init__(self, prop_id, prop_name, db_id, synced_prop_name='', synced_prop_id=''):
        super().__init__(prop_id, prop_name, PropertyType.Relation)
        self.database_id = db_id
        self.synced_property_name = synced_prop_name
        self.synced_property_id = synced_prop_id


class Rollup(Property):
    def __init__(self, prop_id, prop_name, relation_prop_name, relation_prop_id, rollup_prop_name,
                 rollup_prop_id, prop_function):
        super().__init__(prop_id, prop_name, PropertyType.Rollup)
        self.relation_property_name = relation_prop_name
        self.relation_property_id = relation_prop_id
        self.rollup_property_name = rollup_prop_name
        self.rollup_property_id = rollup_prop_id
        self.function = prop_function


class RollupFunction:
    Count_all = 'count_all'
    Count_values = 'count_values'
    Count_unique_values = 'count_unique_values'
    Count_empty = 'count_empty'
    Count_not_empty = 'count_not_empty'
    Percent_empty = 'percent_empty'
    Percent_not_empty = 'percent_not_empty'
    Sum = 'sum'
    Average = 'average'
    Median = 'median'
    Min = 'min'
    Max = 'max'
    Range = 'range'
