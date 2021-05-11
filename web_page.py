class WebPage:
    def __init__(self, page_name, page_type, users=None):
        self.page_name = page_name
        self.page_type = page_type
        if users is None:
            self.users = []
        else:
            self.users = users

    def get_page_name(self):
        return self.page_name

    def get_page_type(self):
        return self.page_type

    def add_user(self, user):
        self.users.append(user)

    def delete_user(self, user):
        self.users.remove(user)
