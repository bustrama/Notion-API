# https://developers.notion.com/reference/database#database-property

def GetProperty(json, prop_name):
    if json['type'] == PropertyType.Number:
        return Number(
            json,
            prop_name
        )
    elif json['type'] == PropertyType.Select:
        return Select(
            json,
            prop_name
        )
    elif json['type'] == PropertyType.Multi_select:
        return MultiSelect(
            json['id'],
            prop_name,

        )
    elif json['type'] == PropertyType.Formula:
        return Formula(
            json,
            prop_name
        )
    elif json['type'] == PropertyType.Relation:
        return Relation(
            json,
            prop_name
        )
    elif json['type'] == PropertyType.Rollup:
        return Rollup(
            json['id'],
            prop_name
        )
    else:
        return Property(
            json,
            prop_name
        )


class Property:
    def __init__(self, json, prop_name):
        self.id = json['id']
        self.name = prop_name
        self.type = json['type']


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
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        if type(json['number']) is dict:
            self.format = json['number']['format']


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
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.options = []
        if 'options' in json['select']:
            for option in json['select']['options']:
                self.options.append(
                    Option(
                        option['id'],
                        option['name'],
                        option['color']
                    )
                )


class MultiSelect(Property):
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


class Formula(Property):
    def __init__(self, json,  prop_name):
        super().__init__(json, prop_name)
        if 'expression' in json['formula']:
            self.expression = json['formula']['expression']


class Relation(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        if 'database_id' in json:
            self.database_id = json['database_id']
            self.synced_property_name = json['synced_property_name']
            self.synced_property_id = json['synced_property_id']


class Rollup(Property):
    def __init__(self, json, prop_name):
        super().__init__(json, prop_name)
        self.relation_property_name = json['relation_property_name']
        self.relation_property_id = json['relation_property_id']
        self.rollup_property_name = json['rollup_property_name']
        self.rollup_property_id = json['rollup_property_id']
        self.function = json['function']


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
