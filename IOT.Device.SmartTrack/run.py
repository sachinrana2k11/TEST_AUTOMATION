import multiprocessing
import os,time,sys
no_of_routes = 20
def check_for_db(foo):
    if(foo=="YES"):
        user_input_temp = input("DEV/TST/BOTH?")
        if (user_input_temp == "DEV"):
          os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\SET.py")
          return "Database changes done"
        if (user_input_temp == "TST"):
            os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\SET_tst.py")
            return "Database changes done"
        if(user_input_temp == "BOTH"):
            os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\SET.py")
            os.system("python3 C:\\shunya\\IOT.Device.SmartTrack\\DATABASE\\SET_tst.py")
            return "Database changes done"
        else:
            return "Invalid Input Try again..."
    if(foo =="NO"):
        return "You choose not to change database"
    else:
        return "Invalid Input Try again..."
def Route1_pick():
    print("Route-1 pick- Starting..")
    os.system("python3 Start_Route-pick-1.py")
def Route2_pick():
    print("Route-2 pick Starting..")
    os.system("python3 Start_Route-pick-2.py")
def Route3_pick():
    print("Route-3 pick Starting..")
    os.system("python3 Start_Route-pick-3.py")
def Route4_pick():
    print("Route-4 pick Starting..")
    os.system("python3 Start_Route-pick-4.py")
def Route5_pick():
    print("Route-5 pick Starting..")
    os.system("python3 Start_Route-pick-5.py")
def Route6_pick():
    print("Route-6 pick Starting..")
    os.system("python3 Start_Route-pick-6.py")
def Route7_pick():
    print("Route-7 pick Starting..")
    os.system("python3 Start_Route-pick-7.py")
def Route8_pick():
    print("Route-8 pick Starting..")
    os.system("python3 Start_Route-pick-8.py")
def Route9_pick():
    print("Route-9 pick Starting..")
    os.system("python3 Start_Route-pick-9.py")
def Route10_pick():
    print("Route-10 pick Starting..")
    os.system("python3 Start_Route-pick-10.py")
def Route11_pick():
    print("Route-11 pick Starting..")
    os.system("python3 Start_Route-pick-11.py")
def Route12_pick():
    print("Route-12 pick Starting..")
    os.system("python3 Start_Route-pick-12.py")
def Route13_pick():
    print("Route-13 pick Starting..")
    os.system("python3 Start_Route-pick-13.py")
def Route14_pick():
    print("Route-14 pick Starting..")
    os.system("python3 Start_Route-pick-14.py")
def Route15_pick():
    print("Route-15 pick Starting..")
    os.system("python3 Start_Route-pick-15.py")
def Route16_pick():
    print("Route-16 pick Starting..")
    os.system("python3 Start_Route-pick-16.py")
def Route17_pick():
    print("Route-17 pick Starting..")
    os.system("python3 Start_Route-pick-17.py")
def Route18_pick():
    print("Route-18 pick Starting..")
    os.system("python3 Start_Route-pick-18.py")
def Route19_pick():
    print("Route-19 pick Starting..")
    os.system("python3 Start_Route-pick-19.py")
def Route20_pick():
    print("Route-20 pick Starting..")
    os.system("python3 Start_Route-pick-20.py")

def Route1_drop():
    print("Route-1 drop  Starting..")
    os.system("python3 Start_Route-drop-1.py")
def Route2_drop():
    print("Route-2 drop Starting..")
    os.system("python3 Start_Route-drop-2.py")
def Route3_drop():
    print("Route-3 drop Starting..")
    os.system("python3 Start_Route-drop-3.py")
def Route4_drop():
    print("Route-4 drop Starting..")
    os.system("python3 Start_Route-drop-4.py")
def Route5_drop():
    print("Route-5 drop Starting..")
    os.system("python3 Start_Route-drop-5.py")
def Route6_drop():
    print("Route-6 drop Starting..")
    os.system("python3 Start_Route-drop-6.py")
def Route7_drop():
    print("Route-7 drop Starting..")
    os.system("python3 Start_Route-drop-7.py")
def Route8_drop():
    print("Route-8 drop Starting..")
    os.system("python3 Start_Route-drop-8.py")
def Route9_drop():
    print("Route-9 drop Starting..")
    os.system("python3 Start_Route-drop-9.py")
def Route10_drop():
    print("Route-10 drop Starting..")
    os.system("python3 Start_Route-drop-10.py")
def Route11_drop():
    print("Route-11 drop Starting..")
    os.system("python3 Start_Route-drop-11.py")
def Route12_drop():
    print("Route-12 drop Starting..")
    os.system("python3 Start_Route-drop-12.py")
def Route13_drop():
    print("Route-13 drop Starting..")
    os.system("python3 Start_Route-drop-13.py")
def Route14_drop():
    print("Route-14 drop Starting..")
    os.system("python3 Start_Route-drop-14.py")
def Route15_drop():
    print("Route-15 drop Starting..")
    os.system("python3 Start_Route-drop-15.py")
def Route16_drop():
    print("Route-16 drop Starting..")
    os.system("python3 Start_Route-drop-16.py")
def Route17_drop():
    print("Route-17 drop Starting..")
    os.system("python3 Start_Route-drop-17.py")
def Route18_drop():
    print("Route-18 drop Starting..")
    os.system("python3 Start_Route-drop-18.py")
def Route19_drop():
    print("Route-19 drop Starting..")
    os.system("python3 Start_Route-drop-19.py")
def Route20_drop():
    print("Route-20 drop Starting..")
    os.system("python3 Start_Route-drop-20.py")


def Route1_pick_tst():
    print("Route-1 pick- Starting..")
    os.system("python3 Start_Route-pick-1_tst.py")
def Route2_pick_tst():
    print("Route-2 pick Starting..")
    os.system("python3 Start_Route-pick-2_tst.py")
def Route3_pick_tst():
    print("Route-3 pick Starting..")
    os.system("python3 Start_Route-pick-3_tst.py")
def Route4_pick_tst():
    print("Route-4 pick Starting..")
    os.system("python3 Start_Route-pick-4_tst.py")
def Route5_pick_tst():
    print("Route-5 pick Starting..")
    os.system("python3 Start_Route-pick-5_tst.py")
def Route6_pick_tst():
    print("Route-6 pick Starting..")
    os.system("python3 Start_Route-pick-6_tst.py")
def Route7_pick_tst():
    print("Route-7 pick Starting..")
    os.system("python3 Start_Route-pick-7_tst.py")
def Route8_pick_tst():
    print("Route-8 pick Starting..")
    os.system("python3 Start_Route-pick-8_tst.py")
def Route9_pick_tst():
    print("Route-9 pick Starting..")
    os.system("python3 Start_Route-pick-9_tst.py")
def Route10_pick_tst():
    print("Route-10 pick Starting..")
    os.system("python3 Start_Route-pick-10_tst.py")
def Route11_pick_tst():
    print("Route-11 pick Starting..")
    os.system("python3 Start_Route-pick-11_tst.py")
def Route12_pick_tst():
    print("Route-12 pick Starting..")
    os.system("python3 Start_Route-pick-12_tst.py")
def Route13_pick_tst():
    print("Route-13 pick Starting..")
    os.system("python3 Start_Route-pick-13_tst.py")
def Route14_pick_tst():
    print("Route-14 pick Starting..")
    os.system("python3 Start_Route-pick-14_tst.py")
def Route15_pick_tst():
    print("Route-15 pick Starting..")
    os.system("python3 Start_Route-pick-15_tst.py")
def Route16_pick_tst():
    print("Route-16 pick Starting..")
    os.system("python3 Start_Route-pick-16_tst.py")
def Route17_pick_tst():
    print("Route-17 pick Starting..")
    os.system("python3 Start_Route-pick-17_tst.py")
def Route18_pick_tst():
    print("Route-18 pick Starting..")
    os.system("python3 Start_Route-pick-18_tst.py")
def Route19_pick_tst():
    print("Route-19 pick Starting..")
    os.system("python3 Start_Route-pick-19_tst.py")
def Route20_pick_tst():
    print("Route-20 pick Starting..")
    os.system("python3 Start_Route-pick-20_tst.py")

def Route1_drop_tst():
    print("Route-1 drop  Starting..")
    os.system("python3 Start_Route-drop-1_tst.py")
def Route2_drop_tst():
    print("Route-2 drop Starting..")
    os.system("python3 Start_Route-drop-2_tst.py")
def Route3_drop_tst():
    print("Route-3 drop Starting..")
    os.system("python3 Start_Route-drop-3_tst.py")
def Route4_drop_tst():
    print("Route-4 drop Starting..")
    os.system("python3 Start_Route-drop-4_tst.py")
def Route5_drop_tst():
    print("Route-5 drop Starting..")
    os.system("python3 Start_Route-drop-5_tst.py")
def Route6_drop_tst():
    print("Route-6 drop Starting..")
    os.system("python3 Start_Route-drop-6_tst.py")
def Route7_drop_tst():
    print("Route-7 drop Starting..")
    os.system("python3 Start_Route-drop-7_tst.py")
def Route8_drop_tst():
    print("Route-8 drop Starting..")
    os.system("python3 Start_Route-drop-8_tst.py")
def Route9_drop_tst():
    print("Route-9 drop Starting..")
    os.system("python3 Start_Route-drop-9_tst.py")
def Route10_drop_tst():
    print("Route-10 drop Starting..")
    os.system("python3 Start_Route-drop-10_tst.py")
def Route11_drop_tst():
    print("Route-11 drop Starting..")
    os.system("python3 Start_Route-drop-11_tst.py")
def Route12_drop_tst():
    print("Route-12 drop Starting..")
    os.system("python3 Start_Route-drop-12_tst.py")
def Route13_drop_tst():
    print("Route-13 drop Starting..")
    os.system("python3 Start_Route-drop-13_tst.py")
def Route14_drop_tst():
    print("Route-14 drop Starting..")
    os.system("python3 Start_Route-drop-14_tst.py")
def Route15_drop_tst():
    print("Route-15 drop Starting..")
    os.system("python3 Start_Route-drop-15_tst.py")
def Route16_drop_tst():
    print("Route-16 drop Starting..")
    os.system("python3 Start_Route-drop-16_tst.py")
def Route17_drop_tst():
    print("Route-17 drop Starting..")
    os.system("python3 Start_Route-drop-17_tst.py")
def Route18_drop_tst():
    print("Route-18 drop Starting..")
    os.system("python3 Start_Route-drop-18_tst.py")
def Route19_drop_tst():
    print("Route-19 drop Starting..")
    os.system("python3 Start_Route-drop-19_tst.py")
def Route20_drop_tst():
    print("Route-20 drop Starting..")
    os.system("python3 Start_Route-drop-20_tst.py")


def thred_for_pick(list1):
    a =[Route1_pick,Route2_pick,Route3_pick,Route4_pick,Route5_pick,Route6_pick,Route7_pick,Route8_pick,Route9_pick,Route10_pick,Route11_pick,Route12_pick,Route13_pick,Route14_pick,Route15_pick,Route16_pick,Route17_pick,Route18_pick,Route19_pick,Route20_pick]
    i=0
    j=0
    while(i<len(list1)):
      j=0
      fnc1 = str(list1[i])
      while(j<no_of_routes):
        fnc = str(a[j])
        temp1= str(i)
        temp2 = str("P")
        temp3 =temp2+temp1
        if fnc1 in fnc:
           #print("yes")
           temp3 = multiprocessing.Process(target=a[j])
           temp3.start()
           i=i+1
           j=j+1
        else:
           #print("No")
           j=j+1


def thred_for_drop(list1):
    a =[Route1_drop,Route2_drop,Route3_drop,Route4_drop,Route5_drop,Route6_drop,Route7_drop,Route8_drop,Route9_drop,Route10_drop,Route11_drop,Route12_drop,Route13_drop,Route14_drop,Route15_drop,Route16_drop,Route17_drop,Route18_drop,Route19_drop,Route20_drop]
    i=0
    j=0
    while(i<len(list1)):
      j=0
      fnc1 = str(list1[i])
      while(j<no_of_routes):
        fnc = str(a[j])
        temp1= str(i)
        temp2 = str("P")
        temp3 =temp2+temp1
        if fnc1 in fnc:
           #print("yes")
           temp3 = multiprocessing.Process(target=a[j])
           temp3.start()
           i=i+1
           j=j+1
        else:
           #print("No")
           j=j+1


def thred_for_pick_tst(list1):
    a =[Route1_pick_tst,Route2_pick_tst,Route3_pick_tst,Route4_pick_tst,Route5_pick_tst,Route6_pick_tst,Route7_pick_tst,Route8_pick_tst,Route9_pick_tst,Route10_pick_tst,Route11_pick_tst,Route12_pick_tst,Route13_pick_tst,Route14_pick_tst,Route15_pick_tst,Route15_pick_tst,Route16_pick_tst,Route17_pick_tst,Route18_pick_tst,Route20_pick_tst]
    i=0
    j=0
    while(i<len(list1)):
      j=0
      fnc1 = str(list1[i])
      while(j<no_of_routes):
        fnc = str(a[j])
        temp1= str(i)
        temp2 = str("P")
        temp3 =temp2+temp1
        if fnc1 in fnc:
           #print("yes")
           temp3 = multiprocessing.Process(target=a[j])
           temp3.start()
           i=i+1
           j=j+1
        else:
           #print("No")
           j=j+1


def thred_for_drop_tst(list1):
    a =[Route1_drop_tst,Route2_drop_tst,Route3_drop_tst,Route4_drop_tst,Route5_drop_tst,Route6_drop_tst,Route7_drop_tst,Route8_drop_tst,Route9_drop_tst,Route10_drop_tst,Route11_drop_tst,Route12_drop_tst,Route13_drop_tst,Route14_drop_tst,Route15_drop_tst,Route16_drop_tst,Route17_drop_tst,Route18_drop_tst,Route19_drop_tst,Route20_drop_tst]
    i=0
    j=0
    while(i<len(list1)):
      j=0
      fnc1 = str(list1[i])
      while(j<no_of_routes):
        fnc = str(a[j])
        temp1= str(i)
        temp2 = str("P")
        temp3 =temp2+temp1
        if fnc1 in fnc:
           #print("yes")
           temp3 = multiprocessing.Process(target=a[j])
           temp3.start()
           i=i+1
           j=j+1
        else:
           #print("No")
           j=j+1

if __name__ == '__main__':
    user_input = input("Do you want to update/clear Database(YES/NO)?")
    foo_bar = check_for_db(user_input)
    print(foo_bar)
    if(foo_bar == "Database changes done" or foo_bar=="You choose not to change database"):
      user_input2 = input("Enter Envirment TST/DEV/BOTH-")
      if (user_input2 == "DEV"):
        user_input1 = input("Enter PICK / DROP before route starting-:")
        if user_input1 == "PICK":
          a = [x for x in input("Enter route no for PICK with (,) separate -(like Route1_pick,Route3_pick,....)").split(",")]
          if(a[0]=="all"):
           print("You choose all Routes to start..")
           p1 = multiprocessing.Process(target=Route1_pick)
           p2 = multiprocessing.Process(target=Route2_pick)
           p3 = multiprocessing.Process(target=Route3_pick)
           p4 = multiprocessing.Process(target=Route4_pick)
           p5 = multiprocessing.Process(target=Route5_pick)
           p6 = multiprocessing.Process(target=Route6_pick)
           p7 = multiprocessing.Process(target=Route7_pick)
           p8 = multiprocessing.Process(target=Route8_pick)
           p9 = multiprocessing.Process(target=Route9_pick)
           p10 = multiprocessing.Process(target=Route10_pick)
           p11 = multiprocessing.Process(target=Route11_pick)
           p12 = multiprocessing.Process(target=Route12_pick)
           p13 = multiprocessing.Process(target=Route13_pick)
           p14 = multiprocessing.Process(target=Route14_pick)
           p15 = multiprocessing.Process(target=Route15_pick)
           p16 = multiprocessing.Process(target=Route16_pick)
           p17 = multiprocessing.Process(target=Route17_pick)
           p18 = multiprocessing.Process(target=Route18_pick)
           p19 = multiprocessing.Process(target=Route19_pick)
           p20 = multiprocessing.Process(target=Route20_pick)
           p1.start()
           p2.start()
           p3.start()
           p4.start()
           p5.start()
           p6.start()
           p7.start()
           p8.start()
           p9.start()
           p10.start()
           p11.start()
           p12.start()
           p13.start()
           p14.start()
           p15.start()
           p16.start()
           p17.start()
           p18.start()
           p19.start()
           p20.start()
          else:
            print("selected Route are"+str(a))
            thred_for_pick(a);

        if user_input1 == "DROP":
           a1 = [x for x in input("Enter route no for DROP with (,) separate -(like Route1_drop,Route3_drop,....)").split(",")]
           if (a1[0] == "all"):
               print("You choose all Routes to start..")
               p1 = multiprocessing.Process(target=Route1_drop)
               p2 = multiprocessing.Process(target=Route2_drop)
               p3 = multiprocessing.Process(target=Route3_drop)
               p4 = multiprocessing.Process(target=Route4_drop)
               p5 = multiprocessing.Process(target=Route5_drop)
               p6 = multiprocessing.Process(target=Route6_drop)
               p7 = multiprocessing.Process(target=Route7_drop)
               p8 = multiprocessing.Process(target=Route8_drop)
               p9 = multiprocessing.Process(target=Route9_drop)
               p10 = multiprocessing.Process(target=Route10_drop)
               p11 = multiprocessing.Process(target=Route11_drop)
               p12 = multiprocessing.Process(target=Route12_drop)
               p13 = multiprocessing.Process(target=Route13_drop)
               p14 = multiprocessing.Process(target=Route14_drop)
               p15 = multiprocessing.Process(target=Route15_drop)
               p16 = multiprocessing.Process(target=Route16_drop)
               p17 = multiprocessing.Process(target=Route17_drop)
               p18 = multiprocessing.Process(target=Route18_drop)
               p19 = multiprocessing.Process(target=Route19_drop)
               p20 = multiprocessing.Process(target=Route20_drop)
               p1.start()
               p2.start()
               p3.start()
               p4.start()
               p5.start()
               p6.start()
               p7.start()
               p8.start()
               p9.start()
               p10.start()
               p11.start()
               p12.start()
               p13.start()
               p14.start()
               p15.start()
               p15.start()
               p16.start()
               p17.start()
               p18.start()
               p19.start()
               p20.start()
           else:
               print("selected Route are" + str(a1))
               thred_for_drop(a1);
      if (user_input2 == "TST"):
        user_input1 = input("Enter PICK / DROP before route starting-:")
        if user_input1 == "PICK":
          a = [x for x in input("Enter route no for PICK with (,) separate -(like Route1_pick_tst,Route3_pick_tst,....)").split(",")]
          if(a[0]=="all"):
           print("You choose all Routes to start..")
           p1 = multiprocessing.Process(target=Route1_pick_tst)
           p2 = multiprocessing.Process(target=Route2_pick_tst)
           p3 = multiprocessing.Process(target=Route3_pick_tst)
           p4 = multiprocessing.Process(target=Route4_pick_tst)
           p5 = multiprocessing.Process(target=Route5_pick_tst)
           p6 = multiprocessing.Process(target=Route6_pick_tst)
           p7 = multiprocessing.Process(target=Route7_pick_tst)
           p8 = multiprocessing.Process(target=Route8_pick_tst)
           p9 = multiprocessing.Process(target=Route9_pick_tst)
           p10 = multiprocessing.Process(target=Route10_pick_tst)
           p11 = multiprocessing.Process(target=Route11_pick_tst)
           p12 = multiprocessing.Process(target=Route12_pick_tst)
           p13 = multiprocessing.Process(target=Route13_pick_tst)
           p14 = multiprocessing.Process(target=Route14_pick_tst)
           p15 = multiprocessing.Process(target=Route15_pick_tst)
           p16 = multiprocessing.Process(target=Route16_pick_tst)
           p17 = multiprocessing.Process(target=Route17_pick_tst)
           p18 = multiprocessing.Process(target=Route18_pick_tst)
           p19 = multiprocessing.Process(target=Route19_pick_tst)
           p20 = multiprocessing.Process(target=Route20_pick_tst)
           p1.start()
           p2.start()
           p3.start()
           p4.start()
           p5.start()
           p6.start()
           p7.start()
           p8.start()
           p9.start()
           p10.start()
           p11.start()
           p12.start()
           p13.start()
           p14.start()
           p15.start()
           p16.start()
           p17.start()
           p18.start()
           p19.start()
           p20.start()
          else:
            print("selected Route are"+str(a))
            thred_for_pick_tst(a);

        if user_input1 == "DROP":
           a1 = [x for x in input("Enter route no for DROP with (,) separate -(like Route1_drop_tst,Route3_drop_tst,....)").split(",")]
           if (a1[0] == "all"):
               print("You choose all Routes to start..")
               p1 = multiprocessing.Process(target=Route1_drop_tst)
               p2 = multiprocessing.Process(target=Route2_drop_tst)
               p3 = multiprocessing.Process(target=Route3_drop_tst)
               p4 = multiprocessing.Process(target=Route4_drop_tst)
               p5 = multiprocessing.Process(target=Route5_drop_tst)
               p6 = multiprocessing.Process(target=Route6_drop_tst)
               p7 = multiprocessing.Process(target=Route7_drop_tst)
               p8 = multiprocessing.Process(target=Route8_drop_tst)
               p9 = multiprocessing.Process(target=Route9_drop_tst)
               p10 = multiprocessing.Process(target=Route10_drop_tst)
               p11 = multiprocessing.Process(target=Route11_drop_tst)
               p12 = multiprocessing.Process(target=Route12_drop_tst)
               p13 = multiprocessing.Process(target=Route13_drop_tst)
               p14 = multiprocessing.Process(target=Route14_drop_tst)
               p15 = multiprocessing.Process(target=Route15_drop_tst)
               p16 = multiprocessing.Process(target=Route16_drop_tst)
               p17 = multiprocessing.Process(target=Route17_drop_tst)
               p18 = multiprocessing.Process(target=Route18_drop_tst)
               p19 = multiprocessing.Process(target=Route19_drop_tst)
               p20 = multiprocessing.Process(target=Route20_drop_tst)
               p1.start()
               p2.start()
               p3.start()
               p4.start()
               p5.start()
               p6.start()
               p7.start()
               p8.start()
               p9.start()
               p10.start()
               p11.start()
               p12.start()
               p13.start()
               p14.start()
               p15.start()
               p15.start()
               p16.start()
               p17.start()
               p18.start()
               p19.start()
               p20.start()
           else:
               print("selected Route are" + str(a1))
               thred_for_drop_tst(a1);
     