import netmiko
import xlsxwriter

workbook = xlsxwriter.Workbook('ASR9K.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0,0, "Hostname")
worksheet.write(0,1, "IP Loopback")
worksheet.write(0,2, "RSP Type")
worksheet.write(0,3, "Version")
i = 0

f = open("ip_ASR.txt","r")
data_host = f.read()
data_host = data_host.strip()
data_host_lst = data_host.split(",")
f.close()
	
for IP_lo0 in data_host_lst:
    i = i + 1
    device_info = {
        "host": IP_lo0,
        "port": 22,
        "username": "tdhuy",
        "password": "muahoado1C",
        "device_type": "cisco_ios"
        }
    try:
        print("Connecting to {}...".format(device_info["host"]))
        conn = netmiko.ConnectHandler(**device_info)
    except:
	    print ("Fail to connect to: ", IP_lo0)
    else:
        #print("Connected successfully")
        output = conn.find_prompt()
        host_temp = output.replace('#','')
        #print (host_temp)
        host_ind = host_temp.find(":") +1
        #print (host_ind)
        host_name = host_temp [host_ind::]
        print(host_name)
	    
        command = "admin show platform | inc P0/CPU0"
        #command = input("Please enter your command: ")
        output = conn.send_command(command,use_textfsm=True)
        rsp_ind = output.find("A9K")
        rsp_type = output [45:58]
        print(rsp_type)	
	    
        command = "show  version | inc Software"
        output = conn.send_command(command)
        version = output[-14:-9]
        print(version)
	    
        conn.disconnect()
        #i = i + 1
        worksheet.write(i,0, host_name)
        #worksheet.write(i,1, IP_lo0)
        worksheet.write(i,2, rsp_type)
        worksheet.write(i,3, version)
    worksheet.write(i,1, IP_lo0)	
workbook.close()
print ("Done!")