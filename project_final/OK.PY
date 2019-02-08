import sqlite3
conn = sqlite3.connect('bike.db')
c = conn.cursor()


rig = "1h"
cc = 120 
engine = "Dtsi"


c.execute("""select * from bike_info""")
rows = c.fetchall()
 
for row in rows:
    print(row)



conn.commit()

conn.close()

