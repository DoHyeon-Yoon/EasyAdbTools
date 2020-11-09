##made by Rasbi##
import os

##variable##

number=''  # menu number variable

##main code##

while True :
    print("-----EasyAdbTools------")
    print('USB & ADB Driver must be installed.')
    print("--------------------")
    print("1. Reboot to Recover\n2. Reboot to bootloader\n3. Reboot in Fast Boot Mode\n4. Use adb\n5. Help / tip\n6. exit")
    print("------------------------")
    number=input("Please select a number. =>")


    if number == '1': ##Reboot Recovery
        print("Please wait a moment...")
        os.system('adb devices {}'.format("C:\Windows\System32\cmd.exe"))
        output = os.popen('adb devices').read()
        print(output)
        os.system('adb reboot recovery {}'.format("C:\Windows\System32\cmd.exe"))
        for i in range(0,20):
            print("\n")
        print("------------------------")
        print("Device has been booted. Please check the device.")
        print("------------------------")
        print("\n")


    if number == '2': ##Reboot Bootloader
        print("Please wait a moment...")
        os.system('adb devices {}'.format("C:\Windows\System32\cmd.exe"))
        output = os.popen('adb devices').read()
        print(output)
        os.system('adb reboot bootloader {}'.format("C:\Windows\System32\cmd.exe"))
        for i in range(0,20):
            print("\n")
        print("------------------------")
        print("Device has been booted. Please check the device.")
        print("------------------------")
        print("\n")
        
        
    if number == '3': ##Fast Boot Reboot
        print("Please wait a moment...")
        os.system('fastboot reboot {}'.format("C:\Windows\System32\cmd.exe"))
        for i in range(0,20):
            print("\n")
        print("------------------------")
        print("Device has been booted. Please check the device.")
        print("------------------------")
        print("\n")


    if number == '4': ##adb command function
        print("\n")
        print("------------------------")
        input("When the cmd window opens, you can enter the adb command there.\nPress enter to continue....\n------------------------")
        os.system(' {}'.format("C:\Windows\System32\cmd.exe"))
        for i in range(0,20):
            print("\n")
        continue
        

    
    if number == '5': #Help / tip Code
        print("\n") 
        print("--------------------")
        print("Made by Rasbi \n--------------------\nUsing a program, caused by broken and the failure of devices that are responsible users.\n")
        print("1. This program can only be used by setting up usb debugging and oem unlocking.")
        print("2. Also, if you install Recover or boot.img, your warranty (Samsung Knox) will be broken.   In this case, all Knox-related functions are not available (including Samsung Pay).")
        print("--------------------")
        input("Press enter to continue...")
        for i in range(0,20):
            print("\n") 
        continue


    if number == '6': #exit code
        print("\n") 
        print("--------------------")
        input("Press enter to continue....\n--------------------")
        os.system('adb kill-server {}'.format("C:\Windows\System32\cmd.exe"))
        exit()

##error prevention code##

    if number == "" :
        print("\n") 
        print("--------------------")
        print("Invalid number selected.")
        print("--------------------")
        input("Press enter to continue...")
        for i in range(0,20):
            print("\n") 
        continue


    else :
        print("\n") 
        print("--------------------")
        print("Invalid number selected.")
        print("--------------------")
        input("Press enter to continue...")
        for i in range(0,20):
            print("\n") 
        continue


    

    
