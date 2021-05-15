# https://developers.notion.com/reference/rich-text

from User import *


def GetRichText(rich_text):
    if rich_text['type'] == RichType.Text:
        return Text(
            rich_text['plain_text'],
            rich_text['annotations'],
            rich_text['text']['content'],
            rich_text['text']['link']
        )
    if rich_text['type'] == RichType.Mention:
        if rich_text['mention']['type'] == MentionType.User:
            return UserMention(
                rich_text['plain_text'],
                rich_text['annotations'],
                rich_text['mention']['user']
            )
        if rich_text['mention']['type'] == MentionType.Page:
            return PageMention(
                rich_text['plain_text'],
                rich_text['annotations'],
                rich_text['mention']['page_id']
            )
        if rich_text['mention']['type'] == MentionType.Database:
            return DatabaseMention(
                rich_text['plain_text'],
                rich_text['annotations'],
                rich_text['mention']['database']
            )
        if rich_text['mention']['type'] == MentionType.Date:
            return DateMention(
                rich_text['plain_text'],
                rich_text['annotations'],
                rich_text['mention']['date']
            )
    if rich_text['type'] == RichType.Equation:
        return Equation(
            rich_text['plain_text'],
            rich_text['annotations'],
            rich_text['expression']
        )


class RichText:
    def __init__(self, text, text_annotations, text_type, link=''):
        self.plain_text = text
        self.href = link
        self.annotations = Annotations(text_annotations)
        self.type = text_type


class RichType:
    Text = 'text'
    Mention = 'mention'
    Equation = 'equation'


class Annotations:
    def __init__(self, annotations):
        self.bold = annotations['bold']
        self.italic = annotations['italic']
        self.strikethrough = annotations['strikethrough']
        self.underline = annotations['underline']
        self.code = annotations['code']
        self.color = annotations['color']


class AnnotationsColor:
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
    Gray_background = 'gray_background'
    Brown_background = 'brown_background'
    Orange_background = 'orange_background'
    Yellow_background = 'yellow_background'
    Green_background = 'green_background'
    Blue_background = 'blue_background'
    Purple_background = 'purple_background'
    Pink_background = 'pink_background'
    Red_background = 'red_background'


class Text(RichText):
    def __init__(self, text, text_annotations, text_content, text_link=None):
        super().__init__(text, text_annotations, RichType.Text)
        self.content = text_content
        self.link = text_link


class TextLink:
    def __init__(self, link):
        self.type = 'url'
        self.url = link


class Mention(RichText):
    def __init__(self, text, text_annotations, mention_type):
        super().__init__(text, text_annotations, RichType.Mention)
        self.mention_type = mention_type


class MentionType:
    User = 'user'
    Page = 'page'
    Database = 'database'
    Date = 'date'


class UserMention(Mention):
    def __init__(self, text, text_annotations, user_mentioned):
        super().__init__(text, text_annotations, MentionType.User)
        if user_mentioned['type'] == UserType.Person:
            self.user = Person(
                user_mentioned['id'],
                user_mentioned['name'],
                user_mentioned['avatar_url'],
                user_mentioned['person']['email']
            )
        if user_mentioned['type'] == UserType.Bot:
            self.user = Bot(
                user_mentioned['id'],
                user_mentioned['name'],
                user_mentioned['avatar_url']
            )


class PageMention(Mention):
    def __init__(self, text, text_annotations, page_id_mentioned):
        super().__init__(text, text_annotations, MentionType.Page)
        self.page_id = page_id_mentioned


class DatabaseMention(Mention):
    def __init__(self, text, text_annotations, database_id_mentioned):
        super().__init__(text, text_annotations, MentionType.Database)
        self.database_id = database_id_mentioned


class DateMention(Mention):
    def __init__(self, text, text_annotations, date_mentioned):
        super().__init__(text, text_annotations, MentionType.Date)
        self.date = date_mentioned


class Equation(RichText):
    def __init__(self, text, text_annotations, exp):
        super().__init__(text, text_annotations, RichType.Equation)
        self.expression = exp
