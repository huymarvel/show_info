import netmiko
from netmiko import ConnectHandler
import os.path, shutil
from datetime import date, datetime
import time
import pathlib

moment = datetime.now()
time_hms = moment.strftime("%H-%M-%S")
now = date.today()


def compare(File1,File2):
    with open(File1,'r') as f:
        d=set(f.readlines())

    with open(File2,'r') as f:
        e=set(f.readlines())

    compare_file = f"{dir_of_file}\Compare_offline_{IP_lo0}_{now.day}{now.month}_{time_hms }.txt"
    open(compare_file,'w').close() #Create the file

    with open(compare_file,'a') as f:
        for line in list(e-d):
            f.write("\n")           
            f.write(line)
    print("Subscriber chua len luu tai {}".format(compare_file))
#

def before_sub_info(outFileName):
    f = open(file_path,"r")
    data_content = f.read()
    data_content_lst = data_content.split(",")
    for subscriber in data_content_lst:
        subscriber = subscriber.strip()
        commd = "show subscribers user-name " + subscriber
        #print (commd)
        output_sub = net_connect.send_command(commd)          			   
        print (output_sub)
        if subscriber not in output_sub:
            outFile=open(outFileName, "a")
            outFile.write(subscriber)
            outFile.write("\n")
            outFile.close()
            print("File is saved at {}".format(outFileName))
        else:
            clear_sub(subscriber)		
    f.close()

	
def after_sub_info(outFileName):
    f = open(file_path,"r")
    data_content = f.read()
    data_content_lst = data_content.split(",")
    for subscriber in data_content_lst:
        subscriber = subscriber.strip()
        commd = "show subscribers user-name " + subscriber
        #print (commd)
        output_sub = net_connect.send_command(commd)          			   
        print (output_sub)
        if subscriber not in output_sub:
            outFile=open(outFileName, "a")
            outFile.write(subscriber)
            outFile.write("\n")
            outFile.close()
            print("File is saved at {}".format(outFileName))		
    f.close()
#
def clear_sub(subscriber):
    print("Clearing subscriber :{}".format(subscriber))					
    commd1 = "clear network-access aaa subscriber username " + subscriber
    output_sub = net_connect.send_command(commd1)
#
file_path = input("Please enter path of file (ex. D:/loi_interim_inoc2.txt)(quit/exit to finish): ")
file_path = file_path.strip()
dir_of_file = pathlib.Path(file_path).parent.absolute()

if file_path != "exit" and file_path != "quit":
    IP_lo0 = input("Please enter your IP lo0(quit/exit to finish): ")
    if IP_lo0 != "exit" and IP_lo0 != "quit":
        device_info={
        "device_type":"juniper",
        "host":IP_lo0,
        "username":"tdhuy",
        "password":"muahoado1C",
        }
        net_connect = ConnectHandler(**device_info)
        try:
            print("Connecting to {}...".format(device_info["host"]))
            net_connect = netmiko.ConnectHandler(**device_info)
        except:
            print ("Fail to connect to: ", IP_lo0)
        else:
            if os.path.isfile(file_path):
                outFileName=f"{dir_of_file}\Sub_offline_truoc_{now.day}{now.month}_{time_hms }.txt"
                outFile=open(outFileName, "w").close()
                outFileName2=f"{dir_of_file}\Sub_offline_sau_{now.day}{now.month}_{time_hms }.txt"
                outFile2=open(outFileName2, "w").close()
			    #lấy thông tin thuê bao trước khi clear & thực hiện clear
                before_sub_info(outFileName)            
               	#chờ thuê bao xác thực
                print ("Please wait about <1 mins ...")
                time.sleep(5)
				#lấy thông tin thuê bao sau khi clear
                after_sub_info(outFileName2)
				
				#so sánh sau và trước
                compare(outFileName,outFileName2)

            else:
                print ("File does not exist, please check again!")
            net_connect.disconnect() 
else:
    print ("End.")
