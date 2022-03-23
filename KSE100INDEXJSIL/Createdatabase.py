import sqlite3
conn = sqlite3.connect('kse100psx.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS Shows
              (Item TEXT, Indx INT)''')
c.execute ( '''SELECT * FROM Shows  ''' )
results = c.fetchall ( )
print ( results )
# close connection

conn.commit()
conn.close()