from models import devicedata, basepayload, gpspayload, rfidpayload, shutpayload, panicpayload, camerapayload
import json
import time
from helpers import ConfigHelper
import datetime
from helpers import *
import uuid
from events import Events
import serial
from managers import hardwareevents
# from Adafruit_CharLCD import Adafruit_CharLCD
# import picamera
# import RPi.GPIO as GPIO
import os, shutil, glob


# hardware base class
class hardwarebase(object):
    """this is a base class for all different hardware helpers"""

    # log = LoggingHelper(ConfigHelper.logconfig.disabled, ConfigHelper.logconfig.logtoconsole)
    def __init__(self, name):

        try:

            # Init objects & Default
            # --------------------------------------
            self.payload = basepayload()
            self.data = devicedata()
            self.started = False
            self.DateString = '%Y-%m-%d'
            self.TimeString = '%H:%M:%S'
            # self.lcd = LCD()

            # --------------------------------------

            # Init configs
            # --------------------------------------

            # set the name
            self.name = name
            # Get the hardware id
            self.hardwareid = ConfigHelper.config[self.name]['HARDWARE_ID']
            # check if hardware is enabled or not
            self.enabled = ConfigHelper.hardwares[name]

            # --------------------------------------

        except:
            e = sys.exc_info()[0]
            print(e)
            # self.events.hardware_exception(e)
            return

    def inithardware(self):
        pass

    def start(self):

        # Set the started to True
        self.started = True

    def stop(self):
        """Stop the hardware"""
        print(self.name + ' stop called')
        self.started = False

    def getdata(self):
        pass

    def isstarted(self):
        """ Return the status of the hardware """
        return self.started

    def savedata(self):
        try:
            """ Saved the data to local storage """
            self.data.deviceid = ConfigHelper.deviceid
            self.data.id = uuid.uuid4()
            self.data.save(force_insert=True)
        except:
            e = sys.exc_info()[0]
            print(e)
            return

    def isenabled(self):

        return self.enabled;

    def enable(self):
        """ Enable hardware """
        self.enabled = True
        # Save the value in config file
        ConfigHelper.enabledevice(self.name)

    def disable(self):
        """ Disable hardware """
        self.enabled = False
        # Save the value
        ConfigHelper.disabledevice(self.name)


class gpshardware(hardwarebase):

    def __init__(self):
        hardwarebase.__init__(self, 'GPS')
        # self.cam = camera()
        self.payload = gpspayload()
        self.serial1 = None
        # self.lcd.data_print("GPS Initialize..",0,0)
        time.sleep(2)

    def start(self):
        try:
            print("Starting GPS Hardware ..")
            # self.lcd.data_print("GPS Started..",0,0)
            time.sleep(2)
            """ Read lat,long,speed from config """

            self.serial1 = serial.Serial(ConfigHelper.gpsconfig.Com_Port, ConfigHelper.gpsconfig.Baud_Rate,
                                         timeout=ConfigHelper.gpsconfig.Refresh_Interval)
            # self.cam.cmaera_start()
            super().start()
            self.getdata()

            self.started = True
        except:
            e = sys.exc_info()[0]
            print("1" + str(e))
            return

    def stop(self):

        self.serial1 = None
        self.started = False
        print("Stopping GPS Hardware ..")

    def getdata(self):

        try:
            while self.isstarted():
                a = str(self.serial1.readline())
                data = a.split(",")
                if data[0] == "b'$GPRMC":

                    if data[2] == "A":  # gps data available
                        a = data[3]  # raw lat
                        b = data[5]  # raw lon
                        c = data[7]  # raw speed
                        lati = float(a) / 100
                        longi = float(b) / 100
                        speed = float(data[7]) * 1.852
                        lati_int = int(lati)
                        longi_int = int(longi)
                        raw_lat = float(lati - lati_int) / 60.0
                        raw_lon = float(longi - longi_int) / 60.0
                        latitude = (lati_int + (raw_lat * 100))
                        longitude = (longi_int + (raw_lon * 100))
                        self.payload.latitude = str(format(latitude, '.6f'))
                        self.payload.longitude = str(format(longitude, '.6f'))
                        self.payload.speed = str(format(speed, '.1f'))
                        print(self.payload.latitude, self.payload.longitude, self.payload.speed + "-Km/h")
                        # self.lcd.data_print("Speed-"+self.payload.speed+"-Km/h",0,0)
                        self.data.deviceid = ConfigHelper.deviceid
                        self.data.organizationid = ConfigHelper.orgid
                        self.data.routeid = ConfigHelper.routeid
                        self.data.hardwareid = ConfigHelper.gpsconfig.hardwareid
                        self.data.hardwaretype = 'GPS'
                        self.data.payload = self.payload.payloadjson()
                        today_date = str(datetime.datetime.now().strftime(self.DateString))
                        time_now = str(datetime.datetime.now().strftime(self.TimeString))
                        self.data.datestamp = today_date
                        self.data.timestamp = time_now
                        self.savedata()
                        time.sleep(ConfigHelper.gpsconfig.Refresh_Interval)
                    if data[2] == "V":  # gps data not available
                        print("GPS data not Available..")
                        # self.lcd.data_print("!!GPS signal..",0,0)
        except:
            e = sys.exc_info()[0]
            print("2" + str(e))
            return


class rfidhardware(hardwarebase):

    def __init__(self):
        hardwarebase.__init__(self, 'RFID')
        self.payload = rfidpayload()
        self.serial0 = None
        # self.lcd.data_print("RFID Initialize..",0,1)
        time.sleep(2)

    def start(self):
        print("Starting RFID Hardware ..")
        # self.lcd.data_print("RFID  Started..",0,1)
        time.sleep(2)
        """ Read values from config """
        self.serial0 = serial.Serial(ConfigHelper.rfidconfig.Com_Port, ConfigHelper.rfidconfig.Baud_Rate,
                                     timeout=ConfigHelper.rfidconfig.Refresh_Interval)
        super().start()
        self.getdata()
        self.started = True

    def stop(self):

        self.serial0 = None
        self.started = False
        print("Stopping RFID Hardware ..")

    def getdata(self):

        while self.isstarted():

            a = str(self.serial0.readline())
            if len(a) > 10:
                data_raw = a.split("'")
                b = data_raw[1]
                print(b)
                self.payload.id = str(b)

                print('RFID data recieved ' + self.payload.id)
                # self.lcd.data_print("ID-"+self.payload.id,0,1)
                self.data.deviceid = ConfigHelper.deviceid
                self.data.hardwareid = ConfigHelper.rfidconfig.hardwareid
                self.data.hardwaretype = 'RFID'
                self.data.payload = self.payload.payloadjson()
                self.data.organizationid = ConfigHelper.orgid
                self.data.routeid = ConfigHelper.routeid
                today_date = str(datetime.datetime.now().strftime(self.DateString))

                time_now = str(datetime.datetime.now().strftime(self.TimeString))
                self.data.datestamp = today_date
                self.data.timestamp = time_now
                self.savedata()
            else:
                pass


'''class shuthardware(hardwarebase):
    def __init__(self):
        hardwarebase.__init__(self,'SHUT')
        print("starting shutdown function ")
        """self.cam = camerahardware()"""
        self.gps = gpshardware()
        self.rfid = rfidhardware()
        self.payload = shutpayload()
        #self.dummy = dummyhardware()
        self.cam = camerahardware()
        GPIO.setmode(GPIO.BCM)
        self.a=0
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def start(self):

        time.sleep(2)
        """self.cam.camera_live_images()"""
        super().start()
        self.getdata()
        """print("hello shut...")"""

    def getdata(self):
        while self.isstarted():
            button_state = GPIO.input(4)
            if button_state == True:
               GPIO.output(24, True)
               print('Button Pressed...')
               self.gps.stop()
               self.rfid.stop()
               self.cam.stop()
               #self.dummy.stop()
               #os.system('shutdown now -h')
               time.sleep(5)

            else:
               continue



class LCD:
    def __init__(self):
        self.lcd = Adafruit_CharLCD(25,24,23,17,21,22,16,2)


    def data_print(self,msg,a,b):
        #self.lcd.clear()
        self.lcd.set_cursor(a,b)
        self.lcd.message(msg)

'''


class camerahardware(hardwarebase):

    def __init__(self):
        hardwarebase.__init__(self, 'CAMERA')
        self.payload = camerapayload()
        self.dateString = '%d%m%y%H%M%S'
        self.dir_src = ("temp\\")
        self.dir_dst = ("image\\")
        self.directory = "image\[^0-9]*.jpg"

    def start(self):
        print("starting camera function ")
        # camerahardware.camera = picamera.PiCamera(resolution=(ConfigHelper.cameraconfig.camera_resulution_r1,ConfigHelper.cameraconfig.camera_resulution_r2),framerate=ConfigHelper.cameraconfig.video_framerate)
        MyDateTime = datetime.datetime.now().strftime(self.dateString)
        # camerahardware.camera.start_recording(ConfigHelper.cameraconfig.video_file_path+str(MyDateTime)+ConfigHelper.cameraconfig.video_format)
        # print("recording starts at-"+MyDateTime)
        super().start()
        self.getdata()
        print("camera image capturing started")

    def stop(self):

        # MyDateTime = datetime.datetime.now().strftime(self.dateString)
        # camerahardware.camera.stop_recording()
        # print("recording stops at-"+MyDateTime)
        camerahardware.camera.close()

    def getdata(self):
        while self.isstarted():
            # camerahardware.camera.capture(ConfigHelper.cameraconfig.image_file_path+filename1+ConfigHelper.cameraconfig.image_format, use_video_port=True)
            for filename in os.listdir(self.dir_src):
                if filename.endswith('.jpg'):
                    shutil.copy(self.dir_src + filename, self.dir_dst)
                #print(filename)
                for file in list(glob.glob(self.directory)):
                  MyDateTime = str(datetime.datetime.now().strftime("%m%d%Y_%H%M%S"))
                  final_time = "\\" + MyDateTime
                  #print(final_time)
                  filename = os.path.basename(file)
                  filehandle = open(file, "rb")
                  source = filehandle.read()
                  # Rename the file
                  filehandle.close()
                  newfilename = "image" + final_time + ".jpg"
                  #print("Renaming file :" + filename + " to " + newfilename)
                  os.rename(file, newfilename)
                  time.sleep(5)
                  print("file captures - " + newfilename)
                  time.sleep(ConfigHelper.cameraconfig.image_capture_time)


'''
class panichardware(hardwarebase):
    def __init__(self):
        hardwarebase.__init__(self,'PANIC')
        print("starting panic button function ")
        self.payload = panicpayload()
        #self.cam = camera()
        #self.gps = gpshardware()
        #self.rfid = rfidhardware()
        #self.payload = shutpayload()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def start(self):
        #self.cam.cmaera_start()
        super().start()
        self.getdata()

    def getdata(self):
        while self.isstarted():
            input_state = GPIO.input(26)
            if input_state == True:

               print('Panic Button Pressed...')
               #self.gps.stop()
               #self.rfid.stop()
               #self.cam.camera_stop()
               #os.system('shutdown now -h')
               self.payload.status=str("panic_butoon_pressed")
               self.data.deviceid = ConfigHelper.deviceid
               self.data.hardwareid =ConfigHelper.panicconfig.hardwareid
               self.data.hardwaretype = 'PANIC'
               self.data.payload = self.payload.payloadjson()
               self.data.organizationid = ConfigHelper.orgid
               self.data.routeid = ConfigHelper.routeid
               today_date = str(datetime.datetime.now().strftime(self.DateString))
               time_now = str(datetime.datetime.now().strftime(self.TimeString))
               self.data.datestamp = today_date
               self.data.timestamp = time_now
               self.savedata()
               time.sleep(ConfigHelper.panicconfig.Refresh_Interval)

            else:
               pass'''


