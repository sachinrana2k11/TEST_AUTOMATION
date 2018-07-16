import sqlite3 as lite
import datetime
DateString= '%Y-%m-%d'
today_date = str(datetime.datetime.now().strftime(DateString))
a = str("UPDATE devicedata SET datestamp ="+"'"+today_date+"'")
con = lite.connect('C:\shunya\IOT.Device.SmartTrack\DATABASE\Demo_Route_drop_2.db')
cur = con.cursor()
cur.execute("select count(*) from sqlite_master where type='table' and name='devicedata'")
#print(a)
cur.execute(a)
cur.execute("UPDATE devicedata SET synced ='0'")
con.commit()
print('Done with Demo_Route_drop_2.db')