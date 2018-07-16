import glob,os,time,os.path
import datetime,shutil
time_lap=15
filelist = glob.glob(os.path.join('image1', "*.jpg"))
for f in filelist:
    os.remove(f)
dir_src = ("temp1\\")
dir_dst = ("image1\\")
directory = "image1\*.jpg"
for filename in os.listdir(dir_src):
    if filename.endswith('.jpg'):
        shutil.copy( dir_src + filename, dir_dst)
    #print(filename)
    for file in list(glob.glob(directory)):
        MyDateTime = str(datetime.datetime.now().strftime("%m%d%Y_%H%M%S"))
        final_time = "\\"+MyDateTime
        #print(final_time)
        filename = os.path.basename(file)
        filehandle = open(file, "rb")
        source = filehandle.read()
        # Rename the file
        filehandle.close()
        newfilename = "image1"+final_time+".jpg"
        print("capture file :" + MyDateTime + ".jpg")
        os.rename(file, newfilename)
        time.sleep(time_lap)