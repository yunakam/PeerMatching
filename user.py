class User:

    def __init__(self, username, pwd, subject):
        self.username = username
        self.pwd = pwd
        self.subject = subject

    @property
    def __repr__(self):
        return "User('{}', '{}', '{}')".format(self.username, self.pwd, self.subject)

### User attributes to insert into subject tables
class User_details:

    def __init__(self, username, category, language, subcateg = None, comment = None, **kwargs) -> object:
        self.username = username
        self.category = category
        self.language = language
        self.subcateg = subcateg
        self.comment = comment

        # define default attributes = can accept None value
        # default_attr = dict()
        # default_attr.update(kwargs)  # Create a new dictionary combined subcateg.. and kwargs
        self.__dict__.update(kwargs)
        # define (additional) allowed attributes with no default value = needs input
        # more_allowed_attr = ['age','profession','purpose']

        # create a list of [subcateg, comment, age, profession, purpose]
        # allowed_attr = list(default_attr.keys()) + more_allowed_attr

        # # self.__dict__.update((k,v) for k,v in default_attr.items() if k in allowed_attr)


# ## Allowing *kwargs ver.
# class User_details:
#
#     def __init__(self, username, category, language, **kwargs):
#         # define default attributes = can accept None value
#         default_attr = dict(subcateg = None, comment = None)
#
#         # define (additional) allowed attributes with no default value = needs input
#         more_allowed_attr = ['age','profession','purpose']
#
#         # create a list of [subcateg, comment, age, profession, purpose]
#         allowed_attr = list(default_attr.keys()) + more_allowed_attr
#         default_attr.update(kwargs)
#         self.__dict__.update((k,v) for k,v in default_attr.items() if k in allowed_attr