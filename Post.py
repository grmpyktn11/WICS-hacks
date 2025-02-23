import location
class Post:
    def __init__(self, picture, content, location, hashtag=None, username=None):
        self.username = username
        self.location = location
        self.content = content
        self.picture = picture
        self.hashtag = hashtag
        pass
