import sqlite3

connection = sqlite3.connect('post.db')

connection.execute(''' 
        CREATE TABLE IF NOT EXISTS location(
            locationID INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            uva TEXT NOT NULL,
            cville TEXT NOT NULL);
        ''')

connection.execute(''' 
        CREATE TABLE IF NOT EXISTS post(
            postID INTEGER PRIMARY KEY AUTOINCREMENT,
            picture TEXT NOT NULL,
            content TEXT NOT NULL,
            locationID INT,
            FOREIGN KEY(locationID) REFERENCES LOCATION(locationID));
        ''')

#populate location table
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Marie Bette', '105 E Water St Charlottesville VA 22902', 'walk', 'Bus 7' )")

#populate post table
connection.execute("INSERT INTO post (picture, content, locationID) Values ('img/mariebette.JPG', 'love this cafe!!!! always come here on tuesday', 1)")
connection.execute("INSERT INTO post (picture, content, locationID) Values ('img/kardinal hall.JPG', 'Perfect place to sit outside and enjoy the vibe in on a breeze sunny day. Miss my wife.', 2)")
connection.execute("INSERT INTO post (picture, content, locationID) Values ('img/dairy market.JPG', 'BOOO!!!!!! I'm not a fan of this place because I got food poisoning from the ramen store >:(', 3)")
connection.execute("INSERT INTO post (picture, content, locationID) Values ('img/the lawn.JPG', 'so many bug bites in the summer but great place for a picnic', 4)")
connection.execute("INSERT INTO post (picture, content, locationID) Values ('img/the end games.JPG', 'yeah dawg me and my boys always pu to play hmu if ur chill like that', 5)")
connection.execute("INSERT INTO post (picture, content, locationID) Values ('img/moore's creek.JPG, 'i like to go here to scream. sometimes.', 6)")

#cursor = connection.execute("SELECT name from location")




