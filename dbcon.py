import sqlite3
from sqlite3 import Error

class db:
    def __init__(self, dbname='mydb.db'):    
        try:
            self.connection = sqlite3.connect(dbname)
        except:
            print('Error')
        finally:
            pass
        
