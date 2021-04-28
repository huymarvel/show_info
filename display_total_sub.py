import netmiko
from netmiko import ConnectHandler
import xmltodict

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
            output_hostname = net_connect.send_command("show version | match Hostname") 
            output_hostname = output_hostname[11::].strip()
            print(output_hostname)
            output_sub = net_connect.send_command("show subscribers summary port | match \"port-total\" | display xml")  
            if output_sub[-8::] == "{master}":
                output_sub = output_sub.rstrip("{master}")
            data_dict = xmltodict.parse(output_sub, dict_constructor=dict)
            data_dict = data_dict["port-total"]
            print ("Total subscribers: {}".format(data_dict))
        net_connect.disconnect()          
    #   
    else:
        break