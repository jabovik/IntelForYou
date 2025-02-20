import sqlite3

class DB():
    def __init__(self,db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
    def __del__(self):
        self.con.close()
    
    def create_tables(self):
        self.cur.execute("""
        CREATE TABLE articles
                         """)