
import subprocess

import time
import datetime
import calendar
from datetime import date
import os
from infoSvs import infoSvs


def threeFirstChars (previousMonth):
    abvMonth = previousMonth[0] + previousMonth[1] + previousMonth[2]
    return abvMonth


def previousMonthName ():
        
            # Get the current month
            currentMonth = datetime.datetime.now().month
            currentMonthName = calendar.month_name[currentMonth]

            # Get the previous month
            previousMont = currentMonth - 1 if currentMonth > 1 else 12 #way to write in one line. a lit dirty
            previousMonthName = calendar.month_name[previousMont]

            return previousMonthName

def get_prev_month_name():
    today = date.today()# Get the current date
    prev_month = (today.month - 2) % 12# Get the month number of two months ago
    month_name = calendar.month_name[prev_month]# Get the name of the previous month from the calen
    return month_name[:3] # Return the first three characters of the month name




def addShareToActualPrep(actualPrepRelease, share):
    
    prepShareName = "Win11" + str(share) + '$'
    grantedPermissionGroups = "DIR\\IE.ISS.ISA.LATAM.HSA.TS, DIR\\IE.ISS.ISA.LATAM.Argentina.RO.Servers, DIR\\AMPC.Admin, DIR\\mpc.latam.app, DIR\\IE.ISS.ISA.LATAM.HSA.Deployment.ADS"

    removeShareCommand = 'Remove-SmbShare -Name ' + prepShareName + " -Force"
    subprocess.run(['powershell', '-Command', removeShareCommand], capture_output=True, text=True)
   

    addSharePrep =  'New-SmbShare -Name ' + prepShareName + " -Path " + actualPrepRelease
    subprocess.run(['powershell', '-Command', addSharePrep], capture_output=True, text=True)
    
    addPermissionsPrepShare = "Grant-SmbShareAccess -Name " + prepShareName + " -AccountName " + grantedPermissionGroups + " -AccessRight Full -Force"
    subprocess.run(['powershell', '-Command', addPermissionsPrepShare], capture_output=True, text=True)

    revokeEveryonePermisions = "Revoke-SmbShareAccess -Name "+ prepShareName + " -AccountName Everyone -Force"
    subprocess.run(['powershell', '-Command', revokeEveryonePermisions], capture_output=True, text=True)

    print(prepShareName + " added to last release")

def addShareToActualProv(actualPrepRelease, share):
    provShareName = "APP" +str(share)  + "_11$"
    grantedPermissionGroups = "DIR\\IE.ISS.ISA.LATAM.HSA.TS, DIR\\IE.ISS.ISA.LATAM.Argentina.RO.Servers, DIR\\AMPC.Admin, DIR\\mpc.latam.app, DIR\\IE.ISS.ISA.LATAM.HSA.Deployment.ADS"
    provPath =  actualPrepRelease + "\\'$OEM'$\\ProvisioningPackage\\Deploy"
  
   
    removeShareCommand = 'Remove-SmbShare -Name ' + provShareName + " -Force"
    subprocess.run(['powershell', '-Command', removeShareCommand], capture_output=True, text=True)


    addShareProv = 'New-SmbShare -Name ' + provShareName + " -Path " + provPath

    std = subprocess.run(['powershell', '-Command', addShareProv], capture_output=True, text=True)

    addPermissionsProvShare = "Grant-SmbShareAccess -Name " + provShareName + " -AccountName " + grantedPermissionGroups + " -AccessRight Full -Force"
    subprocess.run(['powershell', '-Command', addPermissionsProvShare], capture_output=True, text=True)

    revokeEveryonePermisions = "Revoke-SmbShareAccess -Name "+ provShareName + " -AccountName Everyone -Force"
    subprocess.run(['powershell', '-Command', revokeEveryonePermisions], capture_output=True, text=True)
    print(provShareName + " added to last release")







   
