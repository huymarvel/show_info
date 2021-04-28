import netmiko
from netmiko import ConnectHandler
import json

confirm = "y"
while True:
    if confirm == "n":
        break
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
            output_re0 = net_connect.send_command("show chassis environment routing-engine 0 | display json")  
            if output_re0[-8::] == "{master}":
                 output_re0 = output_re0.rstrip("{master}")
            output_re0_json = json.loads(output_re0)
            #print (output_re0)
            output_re0_json = output_re0_json["environment-component-information"][0]['environment-component-item'][0]['state'][0]['data']
			#
            output_re1 = net_connect.send_command("show chassis environment routing-engine 1 | display json")  
            if output_re1[-8::] == "{master}":
                 output_re1 = output_re1.rstrip("{master}")
            output_re1_json = json.loads(output_re1)
            output_re1_json = output_re1_json["environment-component-information"][0]['environment-component-item'][0]['state'][0]['data']
            if (output_re0_json[0:6] == "Online") and (output_re0_json[0:6] == "Online"):
                 print ("Both of 2 cards are online.")
                 if output_re0_json[7::] == "Master":
                     print ("RE0 is Master Card")
                 elif output_re1_json[7::] == "Master":
                     print ("RE1 is Master Card")
            else:
                 print ("Only 1 card online!")			
            print ("Done!")
            net_connect.disconnect()          
        confirm = input("Do you want to continue? (y/n)")
    #   
    else:
        break