import os
import time
time_lapse = 0
import sqlite3 as lite
con = lite.connect('C:\shunya\IOT.Device.SmartTrack\DATABASE\Time.db')
userid =1
temp = input("Enter pick start time (24hr) eg-:08:00:12-:")
cursor = con.cursor()
#cursor.execute('''INSERT INTO time(id, time) VALUES(?,?)''', (1,temp))
cursor.execute('''UPDATE time SET time = ? WHERE id = ? ''',(temp, userid))
con.commit()
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp1_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp2_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp3_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp4_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp5_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp6_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp7_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp8_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp9_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp10_pick_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp11_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp12_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp13_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp14_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp15_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp16_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp17_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp18_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp19_pick_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp20_pick_tst.py")
time.sleep(time_lapse)

os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp1_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp2_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp3_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp4_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp5_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp6_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp7_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp8_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp9_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp10_drop_tst.py")
time.sleep(time_lapse);
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp11_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp12_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp13_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp14_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp15_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp16_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp17_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp18_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp19_drop_tst.py")
time.sleep(time_lapse)
os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\temp20_drop_tst.py")
time.sleep(time_lapse)