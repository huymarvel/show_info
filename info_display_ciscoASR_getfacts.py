import napalm

f = open("ip_ASR.txt","r")
data_host = f.read()
data_host = data_host.strip()
data_host_lst = data_host.split(",")
f.close()
	
for IP_lo0 in data_host_lst:
    device={
        "hostname": IP_lo0,
        "username":"tdhuy",
        "password":"muahoado1C",
        "optional_args": {"port":22}
        }
    driver = napalm.get_network_driver("iosxr")
    try:
        print("Connecting to {}...".format(device["hostname"]))
        conn = driver(**device)
        conn.open()
    except:
        print("Check IP, username, password, port")
    else:
        print ("Connected successfully")
    output = conn.get_facts()
    #print (output)
    for k, v in output.items():
        print("{:<15}: {}".format(k, v))
print ("Done!")