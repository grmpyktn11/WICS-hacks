import location
class Post:
    def __init__(self, picture, content, location, hashtag=None, username=None):
        self.username = username
        self.location = location
        self.content = content
        self.picture = picture
        self.hashtag = hashtag
        pass

#sample posts
post_mb = Post("img/mariebette.JPG", "love this cafe!!!! always come here on tuesday", location.marieB)
post_kh = Post("img/kardinal hall.JPG", "Perfect place to sit outside and enjoy the vibe in on a breeze sunny day. Miss my wife.", location.kardinal)
post_dm = Post("img/dairy market.JPG", "BOOO!!!!!! I'm not a fan of this place because I got food poisoning from the ramen store >:(", location.dairy)
post_lawn = Post("img/the lawn.JPG", "so many bug bites in the summer but great place for a picnic", location.lawn)
post_eg = Post("img/the end games.JPG", "yeah dawg me and my boys always pu to play hmu if ur chill like that", location.endgames)
post_mc = Post("img/moore's creek.JPG", "i like to go here to scream. sometimes.", location.moorescreek)