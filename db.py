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
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Marie Bette', '105 E Water St, Charlottesville, VA 22902', 'walk', 'Bus 7' )")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Kardinal Hall', '722 Preston Ave #101, Charlottesville, VA 22903', 'Green Line', 'Bus 9' )")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Dairy Market', '946 Grady Ave, Charlottesville, VA 22903', 'Green Line', 'Bus 9')")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('The Lawn', '400 Emmet St S, Charlottesville, VA 22903', 'Yellow Line, Green Line', '')")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('The End Games', '390 Hillsdale Dr, Charlottesville, VA 22901', 'walk', 'Bus 7')")
connection.execute("INSERT INTO location (name, address, uva, cville) VALUES ('Moores Creek', 'Moores Creek Park, Charlottesville, VA 22903')")


#populate post table
connection.execute("")


