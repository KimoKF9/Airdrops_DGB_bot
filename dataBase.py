import sqlite3

class DataBase:

    #creates a user database and sets a connection
    def __init__(self):
        self.connection = sqlite3.connect("dgb_data.db",check_same_thread=False)
        self.cursor = self.connection.cursor()

    #creating events table
    def createEventsTable(self):
        try:
            self.cursor.execute("""CREATE TABLE events(id
, Instagram text, Telegram text,
            DGB text,code integer )""")
            self.connection.commit()
        except:
            print("Run θ⁠‿⁠θ")

  
    #adding event
    def addEvent(self, id, Instagram, Telegram,DGB,code):
        sql = "INSERT INTO events VALUES (?,?,?,?,?)"
        self.cursor.execute(sql, (id, Instagram, Telegram,DGB,code))
        self.connection.commit()
