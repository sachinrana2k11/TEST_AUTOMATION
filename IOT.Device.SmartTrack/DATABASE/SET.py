import os
import time
import sqlite3 as lite

con = lite.connect('C:\shunya\IOT.Device.SmartTrack\DATABASE\Time.db')
userid =1
temp = input("Enter pick start time (24hr) eg-:08:00:12-:")
cursor = con.cursor()
#cursor.execute('''INSERT INTO time(id, time) VALUES(?,?)''', (1,temp))
cursor.execute('''UPDATE time SET time = ? WHERE id = ? ''',(temp, userid))
con.commit()

time_lapse = 0
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp1_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp2_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp3_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp4_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp5_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp6_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp7_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp8_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp9_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp10_pick.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp11_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp12_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp13_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp14_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp15_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp16_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp17_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp18_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp19_pick.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp20_pick.py")
time.sleep(time_lapse)


os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp1_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp2_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp3_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp4_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp5_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp6_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp7_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp8_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp9_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp10_drop.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp11_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp12_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp13_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp14_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp15_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp16_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp17_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp18_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp19_drop.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp20_drop.py")
time.sleep(time_lapse)