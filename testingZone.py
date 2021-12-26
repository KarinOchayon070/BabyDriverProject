import sqlite3
con = sqlite3.connect('crawlerData.db')
con.execute('UPDATE main SET turbo=0 WHERE turbo IS "yove"')
con.execute('UPDATE main SET turbo=1 WHERE turbo IS "טורבו"')

con.commit()
con.close()
