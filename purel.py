# PRPL simple launcher
# by fahmiyufrizal@2024

import os
import subprocess
from os import path
import sys
from sys import exit
import time
import pathlib
import click
import configparser
#import PySimpleGUI as sg
import dearpygui.dearpygui as dpg

# parameters
version = 'v1.0'
titlewindow = 'fahmiyufrizal@2024 [github.com/fahmiyufrizal]'
PRPLFN = (r'Purple_NetCafe_Launcher.exe')
PRPLLN = (r'_App_\ProgramFiles\Purple\PurpleLauncher.exe')
dp0 = os.getcwd()

#paramdata
config_PRPL = path.expandvars(r'%appdata%\Purple')
dataconfig = (r'_Data_\Roaming\Purple')
config_PRPL_local = path.expandvars(r'%localappdata%\Purple')
dataconfig_local = (r'_Data_\Local\Purple')
config_PRPL_local_dome = path.expandvars(r'%localappdata%\PurpleDome')
dataconfig_local_dome = (r'_Data_\Local\PurpleDome')

# create-registry
l1 = '@echo off\n'
l2 = r'reg import "%~dp0_Data_\Reg\HKLM_SOFTWARE_WOW6432Node_plaync.reg"'

#window_init
os.system('title ' + titlewindow)
print(" ")
print("     Purple Launcher Netcafe      ")
print("     " + version)
print("     by fahmiyufrizal@2024        ")
print(" ")
print("     Special Thanks to : Iam November // Sena WaLker Wibowo // Ignatius Wisnu")
print("     Donate me at bit.ly/danain/fahmiyufrizal")
print(" ")
print("[+] Initializing....")
print("[+] Importing module & config...")