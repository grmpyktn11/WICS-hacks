class location:
    def __init__(self, name, address, uva = "", cville = "", bus = None):
        self.name = name
        self.address = address
        self.uva = uva
        self.cville = cville
        self.bus = bus


marieB = location("Marie Bette", "105 E Water St Charlottesville, VA 22902","walk", "Bus 7" )
kardinal = location("Kardinal Hall", "722 Preston Ave #101, Charlottesville, VA 22903", "Green Line", "Bus 9" )
dairy = location("Dairy Market", "946 Grady Ave, Charlottesville, VA 22903", "Green Line", "Bus 9")
lawn = location("The Lawn", "400 Emmet St S, Charlottesville, VA 22903", "Yellow Line, Green Line", "")
endGames = location("The End Games", "390 Hillsdale Dr, Charlottesville, VA 22901", "walk", "Bus 7")
