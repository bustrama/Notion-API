from enum import Enum


class Property:
    def __init__(self, prop_id, prop_type):
        self.id = prop_id
        self.type = prop_type


class PropertyType(Enum):
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
    def __init__(self, prop_id, prop_type, number_format):
        super().__init__(prop_id, prop_type)
        self.format = number_format

    class Format(Enum):
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
    def __init__(self, prop_id, prop_type, options_arr):
        super().__init__(prop_id, prop_type)
        self.options = options_arr


class MultiSelect(Property):
    def __init__(self, prop_id, prop_type, options_arr):
        super().__init__(prop_id, prop_type)
        self.options = options_arr


class Option:
    def __init__(self, option_name, option_id, option_color):
        self.name = option_name
        self.id = option_id
        self.color = option_color

    class Color(Enum):
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
    def __init__(self, prop_id, prop_type, prop_expression):
        super().__init__(prop_id, prop_type)
        self.expression = prop_expression


class Relation(Property):
    def __init__(self, prop_id, prop_type, db_id, synced_prop_name='', synced_prop_id=''):
        super().__init__(prop_id, prop_type)
        self.database_id = db_id
        self.synced_property_name = synced_prop_name
        self.synced_property_id = synced_prop_id


class Rollup(Property):
    def __init__(self, prop_id, prop_type, relation_prop_name, relation_prop_id, rollup_prop_name, rollup_prop_id, prop_function):
        super().__init__(prop_id, prop_type)
        self.relation_property_name = relation_prop_name
        self.relation_property_id = relation_prop_id
        self.rollup_property_name = rollup_prop_name
        self.rollup_property_id = rollup_prop_id
        self.function = prop_function

    class Function(Enum):
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






















