class User:
    def __init__(self, user_id, user_type, user_name, user_avatar_url):
        self.object = 'user'
        self.id = user_id
        self.type = user_type
        self.name = user_name
        self.avatar_url = user_avatar_url


class UserType:
    Person = 'person'
    Bot = 'bot'


class Person(User):
    def __init__(self, user_id, user_name, user_avatar_url, user_email):
        super().__init__(user_id, UserType.Person, user_name, user_avatar_url)
        self.email = user_email


class Bot(User):
    def __init__(self, user_id, user_name, user_avatar_url):
        super().__init__(user_id, UserType.Bot, user_name, user_avatar_url)
