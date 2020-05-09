import os
import time

#This script is to allow the user to select a wireless interface and then use that interface through the duration of the attack...
# PYTHON VERSION 2.7.13

def interfaceSelectionChoice():
    try:
        print("***Below will be your available wireless interfaces, please type any, but with no spaces***")
        iwconfigCheck = False
        os.system("iwconfig")
        iwconfigCheck = True
        if iwconfigCheck == True:
            interface = raw_input("Type you interface here: ")
            print("You have entered the interface: {0}".format(interface))
            question = raw_input("Is this interface correct? Y/n: ")
            if question == "Y":
                print("***Starting INA now***")
                return interface
            elif question == "N" or question == "n":
                print("***RESTARTING***")
                return interfaceSelectionChoice()
            else:
                print("Why must you type incorrectly???")
                return interfaceSelectionChoice()
    except KeyboardInterrupt: 
        print("\n")
        print ("[-] Program Stopping...")
        exit()

def interfaceSelectionChoiceDos():
    try:
        print("***Below will be your available wireless interfaces, please type any, but with no spaces***")
        os.system("iwconfig")
        interface = raw_input("Type you interface here: ")
        print("You have entered the interface: {0}".format(interface))
        question = raw_input("Is this interface correct? Y/n: ")
        if question == "Y":
            print("***Starting INA now***")
            return interface
        elif question == "N" or question == "n":
            print("***RESTARTING***")
            return interfaceSelectionChoice()
        else:
            print("Why must you type incorrectly???")
            return interfaceSelectionChoice()
    except KeyboardInterrupt: 
        print("\n")
        print ("[-] Program Stopping...")
        exit()
