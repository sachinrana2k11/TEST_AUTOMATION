import sqlite3 as lite
import datetime
DateString= '%Y-%m-%d'
con = lite.connect('C:\shunya\IOT.Device.SmartTrack\DATABASE\Demo_Route_pick_6.db')
cur = con.cursor()
def check_timefeed():
    conn = lite.connect('C:\shunya\IOT.Device.SmartTrack\DATABASE\Time.db')
    cur = conn.cursor()
    cursor2 = cur.execute("SELECT time from time")
    for row in cursor2:
        temp_data1 = str(row[0])
        break
    return temp_data1

def check_time():
   cursor1 = cur.execute("SELECT timestamp from devicedata")
   for row in cursor1:
      temp_data = str(row[0])
      break
   return temp_data

def check_num(s):
    return int(s)

def deiffrence(data_enter,data):
    hh_enter = check_num(data_enter[0:2])
    mm_enter = check_num(data_enter[3:5])
    ss_enter = check_num(data_enter[6:8])
    hh_data = check_num(data[0:2])
    mm_data = check_num(data[3:5])
    ss_ddata = check_num(data[6:8])
    diff_hh=hh_data-hh_enter;
    diff_mm = mm_data-mm_enter;
    total_min=(diff_hh*60)+diff_mm
    return total_min

def change_database(min_rcv):
    a = str("UPDATE devicedata SET timestamp = time(timestamp,'" + min_rcv + " minutes')")
    print(a)
    cursor = cur.execute(a)
    print("done")
    con.commit()

data_enter=check_timefeed()
data = check_time()
min_rcv=str(deiffrence(data,data_enter))
print(data,min_rcv)
change_database(min_rcv)
today_date = str(datetime.datetime.now().strftime(DateString))
a = str("UPDATE devicedata SET datestamp ="+"'"+today_date+"'")
cur.execute("select count(*) from sqlite_master where type='table' and name='devicedata'")
#print(a)
cur.execute(a)
cur.execute("UPDATE devicedata SET synced ='0'")
con.commit()
print('Done with Demo_Route_pick_6.db')