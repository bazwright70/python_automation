import argparse
import netmiko
# TODO import required modules

def my_function():
    pass

def main():
   """
    The script...
   """
# todo: create device list
   dev_list = ["192.168.120.10","192.168.120.20"]
# create list of commands
   all_commands = ["show version", "show inventory", "show run"]

# loop though all devices
   for dev in dev_list:

    # todo: create a dictionary for each device 

    # todo: create a temporary list which is reinitialized in each iteration of devices
   
    # todo: create connection object for each device

    # todo: loop through show commands and concatenate into string

    # save device id and concatenate show output to temporary list


       
# if __name__ == main:
    main()