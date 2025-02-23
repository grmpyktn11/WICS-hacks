import sqlite3

connection = sqlite3.connect('post.db')

connection.execute(''' 
        CREATE TABLE IF NOT EXISTS location(
            name TEXT NOT NULL PRIMARY KEY,
            address TEXT NOT NULL,
            uva TEXT NOT NULL,
            cville TEXT NOT NULL);
        ''')

connection.execute(''' 
        CREATE TABLE IF NOT EXISTS post(
            postID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            picture TEXT NOT NULL,
            content TEXT NOT NULL,
            locationname TEXT,
            FOREIGN KEY(locationname) REFERENCES LOCATION(name));
        ''')

#populate location table
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Marie Bette', '105 E Water St, Charlottesville, VA 22902', 'walk', 'Bus 7' )")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Kardinal Hall', '722 Preston Ave #101, Charlottesville, VA 22903', 'Green Line', 'Bus 9' )")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Dairy Market', '946 Grady Ave, Charlottesville, VA 22903', 'Green Line', 'Bus 9')")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('The Lawn', '400 Emmet St S, Charlottesville, VA 22903', 'Yellow Line, Green Line', '')")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('The End Games', '390 Hillsdale Dr, Charlottesville, VA 22901', 'walk', 'Bus 7')")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Moores Creek', 'Moores Creek Park, Charlottesville, VA 22903', '', '')")

#populate post table
connection.execute("INSERT INTO post (username, picture, content, locationname) Values ('kyler5442', 'img/mariebette.JPG', 'love this cafe!!!! always come here on tuesday', 'Marie Bette')")
connection.execute("INSERT INTO post (username, picture, content, locationname) Values ('klye76666', 'img/kardinal hall.JPG', 'Perfect place to sit outside and enjoy the vibe in on a breeze sunny day. Miss my wife.', 'Kardinal Hall')")
connection.execute("INSERT INTO post (username, picture, content, locationname) Values ('kaile1112', 'img/dairy market.JPG', 'BOOO!!!!!! Im not a fan of this place because I got food poisoning from the ramen store >:T', 'Dairy Market')")
connection.execute("INSERT INTO post (username, picture, content, locationname) Values ('evilraidersxxXx', 'img/the lawn.JPG', 'so many bug bites in the summer but great place for a picnic', 'The Lawn')")
connection.execute("INSERT INTO post (username, picture, content, locationname) Values ('MissKylie', 'img/the end games.JPG', 'yeah dawg me and my boys always pu to play hmu if ur chill like that', 'The End Games')")
connection.execute("INSERT INTO post (username, picture, content, locationname) Values ('charlottesvilleresidentlover10', 'img/moores creek.JPG', 'i like to go here to scream. sometimes.', 'Moores Creek')")

#cursor = connection.execute("SELECT name from location")

connection.execute("")


