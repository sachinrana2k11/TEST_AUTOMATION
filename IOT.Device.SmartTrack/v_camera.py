import multiprocessing
import os,time,sys

def start_cam1():
    print("starting cam 1")
    os.system("python3 image1.py")

def start_cam4():
    print("starting cam 4")
    os.system("python3 image4.py")

def start_cam6():
    print("starting cam 6")
    os.system("python3 image6.py")

if __name__ == '__main__':
    x=input("Do you want to start virtual camera(yes/no):-")
    if(x=='yes'):
        print("Wait camera will be start in 5 Sec...")
        time.sleep(5)
        p1 = multiprocessing.Process(target=start_cam1)
        p2 = multiprocessing.Process(target=start_cam4)
        p3 = multiprocessing.Process(target=start_cam6)
        p1.start()
        p2.start()
        p3.start()
    if(x =='no'):
        print("you choose not to start camera..")
        time.sleep(10)