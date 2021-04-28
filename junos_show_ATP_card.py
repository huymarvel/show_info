import netmiko
from netmiko import ConnectHandler
import os.path, shutil
from datetime import date, datetime
import time
import pathlib

moment = datetime.now()
time_hms = moment.strftime("%H-%M-%S")
now = date.today()

output_ATP = ""

def get_output(commd):
    output_promt = net_connect.find_prompt()
    output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
    #print(output_promt)
    output_ATP = net_connect.send_command(commd)
    outFile.write(output_promt)
    outFile.write(output_ATP)
    outFile.write("\n")
    output_promt = ""
    output_ATP = ""   

while True:
    IP_lo0 = input("Please enter your IP lo0(quit/exit to finish): ")
    if IP_lo0 != "exit" and IP_lo0 != "quit":
    #    
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
            #output_promt = net_connect.find_prompt()            
            ATP_file = f"D:\Temp_py\ATP_{IP_lo0}_{now.day}{now.month}_{time_hms }.txt"
            open(ATP_file,'w').close() #Create the file
            FPC_type = input("Please enter FPC type (MPC7E:1,other:2): ")
            FPC = input("Please enter FPC slot: ")
            if FPC_type == "1":
                split_seg = "*"*50 + "Linecard and Module" +"*"*50
                outFile=open(ATP_file, "a")
                outFile.write(split_seg)
                outFile.write("\n")
                #
                commd = "show chassis hardware | no-more"
                get_output(commd)
                #
                commd = "show chassis fpc"
                get_output(commd)
                #
                commd = "show chassis fpc " + FPC + " detail"
                get_output(commd)
                #
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "show chassis pic fpc-slot " + FPC + " pic-slot 0"
                get_output(commd)
                #
                commd = "show chassis pic fpc-slot " + FPC + " pic-slot 1"
                get_output(commd)
                #
                commd = "show interface terse | match \"et-" + FPC + "/|xe-" + FPC + "/\""
                get_output(commd)
                #
                commd = "request chassis fpc slot " + FPC + " offline"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                outFile.write("Offline initiated, use \"show chassis fpc\" to verify")
                outFile.write("\n")
		#
                commd = "show chassis fpc"
                get_output(commd)
                #
                commd = "request chassis fpc slot " + FPC + " online"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                outFile.write("Online initiated, use \"show chassis fpc\" to verify")
                outFile.write("\n")
		#
                commd = "show chassis fpc"
                get_output(commd)
                #
                commd = "show chassis fpc " + FPC + " detail"
                get_output(commd)
                #
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "show interface terse | match \"et-" + FPC + "/|xe-" + FPC + "/\""
                get_output(commd)
                #
                commd = "request chassis pic offline fpc-slot " + FPC + " pic-slot 0"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                temp = "fpc " + FPC + " pic 0 offline initiated, use \"show chassis fpc pic-status\" to verify"
                outFile.write(temp)
                outFile.write("\n")
		#                
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "request chassis pic online fpc-slot " + FPC + " pic-slot 0"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                temp = "fpc " + FPC + " pic 0 online initiated, use \"show chassis fpc pic-status\" to verify"
                outFile.write(temp)
                outFile.write("\n")
		#
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "request chassis pic offline fpc-slot " + FPC + " pic-slot 1"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                temp = "fpc " + FPC + " pic 1 offline initiated, use \"show chassis fpc pic-status\" to verify"
                outFile.write(temp)
                outFile.write("\n")
		#                
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "request chassis pic online fpc-slot " + FPC + " pic-slot 1"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                temp = "fpc " + FPC + " pic 1 online initiated, use \"show chassis fpc pic-status\" to verify"
                outFile.write(temp)
                outFile.write("\n")
		#
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "show interface terse | match \"et-" + FPC + "/|xe-" + FPC + "/\""
                get_output(commd)
                #

            else:
                MIC = input("Please enter MIC slot: ")
                split_seg = "*"*20 + "Linecard and Module" +"*"*20
                outFile=open(ATP_file, "a")
                outFile.write(split_seg)
                outFile.write("\n")
                #
                commd = "show chassis hardware | no-more"
                get_output(commd)
                #
                commd = "show chassis fpc"
                get_output(commd)
                #
                commd = "show chassis fpc " + FPC + " detail"
                get_output(commd)
                #
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "show chassis pic fpc-slot " + FPC + " pic-slot " + MIC
                get_output(commd)
                #
                commd = "show interface terse | match \"et-" + FPC + "/|xe-" + FPC + "/\""
                get_output(commd)
                #
                commd = "request chassis fpc slot " + FPC + " offline"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                outFile.write("Offline initiated, use \"show chassis fpc\" to verify")
                outFile.write("\n")
		#
                commd = "show chassis fpc"
                get_output(commd)
                #
                commd = "request chassis fpc slot " + FPC + " online"
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                outFile.write("Online initiated, use \"show chassis fpc\" to verify")
                outFile.write("\n")
		#
                commd = "show chassis fpc"
                get_output(commd)
                #
                commd = "show chassis fpc " + FPC + " detail"
                get_output(commd)
                #
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "show interface terse | match \"et-" + FPC + "/|xe-" + FPC + "/\""
                get_output(commd)
                #
                commd = "request chassis mic offline fpc-slot " + FPC + " mic-slot " + MIC
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                temp = "fpc " + FPC + " mic " + MIC + " offline initiated, use \"show chassis fpc pic-status " + FPC + "\" to verify"
                outFile.write(temp)
                outFile.write("\n")
		#                
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "request chassis mic online fpc-slot " + FPC + " mic-slot " + MIC
                output_promt = net_connect.find_prompt()
                output_promt = output_promt.replace("tdhuy","juniper") + " " + commd
                outFile.write(output_promt)
                outFile.write("\n")
                temp = "fpc " + FPC + " mic " + MIC + " online initiated, use \"show chassis fpc pic-status " + FPC + "\" to verify"
                outFile.write(temp)
                outFile.write("\n")
		#
                commd = "show chassis fpc pic-status"
                get_output(commd)
                #
                commd = "show interface terse | match \"et-" + FPC + "/|xe-" + FPC + "/\""
                get_output(commd)
                #               

            split_seg = "*"*50 + "License" +"*"*50
            outFile.write(split_seg)
            outFile.write("\n")
            #
            commd = "show chassis hardware | no-more"
            get_output(commd)
            #
            commd = "show system license"
            get_output(commd)
            #
            outFile.close()
            net_connect.disconnect()
            print ("Done!")
    #   
    else:
        break
