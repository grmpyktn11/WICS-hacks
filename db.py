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



