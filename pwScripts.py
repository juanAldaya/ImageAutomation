import os
import time
import subprocess
import timeMgmt
import datetime
from infoSvs import infoSvs
import getpass

def get_output_as_list(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True)
    output = result.stdout.decode().split('\n')
    return output


def check_task_status(tn):
    opTask = get_output_as_list('schtasks /query /fo list /v /tn "Replication Tasks\\'+ tn + '"')

    status = opTask[5]

    statusFrank = status[38] + status[39]+ status[40]+ status[41]+ status[42]


    if statusFrank == 'Ready':
        return True
    else: 
        return False

   
def scriptsProv(scriptsLastReleaseProv, scriptsActualReleaseProv):

    os.system('robocopy.exe ' + '"' + scriptsLastReleaseProv + '" ' + '"' + scriptsActualReleaseProv + '"' +  " /e /xc /xn /xo")
    print("Scripts PROV copied successfully")


def copyCustomSettingsGDN(actualPrepRelease, lastPrepRelease):
    xcpyCustomSettingsGDN = "xcopy "+ lastPrepRelease + "\\$OEM$\\ProvisioningPackage\\Deploy\\Scripts\\CustomSettingsGDN.ini " + actualPrepRelease +"\\$OEM$\\ProvisioningPackage\\Deploy\\Scripts\\CustomSettingsGDN.ini  /c /q /e /k /h /y /i"
    os.system(xcpyCustomSettingsGDN)


def copyPrepScripts(lastPrepScripts, actualPrepScripts):
    ###Copy Scripts

    os.system('robocopy.exe ' + '"' + lastPrepScripts + '" ' + '"' + actualPrepScripts + '"' +  " /e /xc /xn /xo")
    print("Scripts PREP copied successfully")



def copyThingsPrep(lastPrepRelease, actualPrepRelease):

    ### $1 FOLDER FROM LASTCUSTOM RELEASE TO ACTUAL CURSTOM RELEASE
    xcpyBats = "xcopy " + lastPrepRelease + "\\$OEM$\\$1 " + actualPrepRelease + '\\$OEM$\\$1 /c /q /e /k /h /y /i'
    os.system(xcpyBats) ##COPIA EL $1

    xcpySmartCheck = "xcopy "+'"' + lastPrepRelease + "\\Applications\\Action - Pre-Flight Check_SMARTStatus"+'"'+" "+'"'+actualPrepRelease+"\\Applications\\Action - Pre-Flight Check_SMARTStatus"+'"'+" "+"/c /q /e /k /h /y /i"
    os.system(xcpySmartCheck) ##COPIA EL SMART CHECK

    xcpyOffice32Config = "xcopy "+'"'+lastPrepRelease+"\\Applications\\Accenture Office Click-to-Run EN-US\\configuration32.xml"+'"'+" "+'"'+actualPrepRelease+"\\Applications\\Accenture Office Click-to-Run EN-US\\configuration32.xml*"+'"'+" "+"/c /q /e /k /h /y /i"
    
    xcpyOffice32Installer = "xcopy "+'"'+lastPrepRelease+"\\Applications\\Accenture Office Click-to-Run EN-US\\Install_O365_C2R_32.wsf"+'"'+" "+'"'+actualPrepRelease+"\\Applications\\Accenture Office Click-to-Run EN-US\\Install_O365_C2R_32.wsf*"+'"'+" "+"/c /q /e /k /h /y /i"
    
    os.system(xcpyOffice32Config)
    
    os.system(xcpyOffice32Installer)

    ###THIS STEP DOWNLOAD THE CONFIG BY A CMD SCRIPT ### -IDEA- PUT IN A FUNCTION THAT MONITOR THE ENDING
    setupInstallerScript = open('C:\\Users\\ads.jaldaya\\Desktop\\setupOffice32.bat', 'w+') ###create the .bat
    setupInstallerScript.write(str(lastPrepRelease)[0]+":\n") ##moves in console to the wk disk
    setupInstallerScript.write("cd "+'"'+lastPrepRelease+"\\Applications\\Accenture Office Click-to-Run EN-US"+'"'+'\n')## move to the app  
    setupInstallerScript.write("setup.exe /download configuration32.xml\n")###download the 32 config
    setupInstallerScript.close()##save and close the .bat
 
    print("$1 & others copied successfully")


def replicationProv(actualMonthYear, svName):


    actualPrepRelease = infoSvs[str(svName)]['local'] + "\\Win11_" + timeMgmt.threeFirstChars(timeMgmt.previousMonthName())+"_"+str(datetime.datetime.now().year)+ "\\Deploy"

    sourcepathProv = str(infoSvs[str(svName)]['global']) + "\\" + actualMonthYear + "\\APP_"+timeMgmt.threeFirstChars(timeMgmt.previousMonthName())+"_"+str(datetime.datetime.now().year)
    robocopyProv = "robocopy.exe " +sourcepathProv +" "+ actualPrepRelease + "\\$OEM$\\ProvisioningPackage /mir /v /r:3 /w:4 /v /mt:64"

    ads = input('Enter ADS account: ')
    auth = getpass.getpass('Enter the ADS phrase: ') 


    myProvBat = open('C:\\Users\\' + ads + '\\Desktop\\repProv' + actualMonthYear +'.bat', 'w+') ##CREATE THE .BAT AND NAME IT
    myProvBat.write(robocopyProv) ##ADD THE ROBOCOPY LINE TO THE .BAT
    myProvBat.close() ##SAVE AND CLOSE THE .BAT

    now = datetime.datetime.now() + datetime.timedelta(minutes=1)
    current_time = now.strftime("%H:%M")

    tnProv = "PROV Replication " + actualMonthYear

    os.system('schtasks /Create /TN "Replication Tasks\\' +tnProv + '"' + ' /TR "C:\\Users\\' + ads + '\\Desktop\\repProv' + actualMonthYear +'.bat" /SC ONCE /ST ' + str(current_time) + ' /RU ' + str(ads) + ' /RP ' + str(auth))
    statusProv = input("Press anything when the PROV replication finish")
    #statusProv = False
    #time.sleep(300)
    #while (statusProv != True):
    #    statusProv = check_task_status(tnProv)
    #    if statusProv == True:
    #        print("PROV Replication successfully resolved")
    #
    return statusProv

def replicationPrep(actualMonthYear, svName):
        
        
        
        sourcePathPrep = str(infoSvs[str(svName)]['global']) + "\\" + actualMonthYear + "\\Win11_"+  timeMgmt.threeFirstChars(timeMgmt.previousMonthName())+"_"+ str(datetime.datetime.now().year) + "\\Content"
        robocopyPrep = "robocopy.exe " + sourcePathPrep + " " + infoSvs[svName]['local'] + "\\Win11_" + timeMgmt.threeFirstChars(timeMgmt.previousMonthName()) + "_"+ str(datetime.datetime.now().year) +" /mir /v /r:3 /w:4 /v /mt:64"

        ads = input('Enter ADS account: ')
        auth = getpass.getpass('Enter the ADS phrase: ') 


        myBat = open('C:\\Users\\' + ads +  '\\Desktop\\repPrep' + actualMonthYear +'.bat', 'w+')
        myBat.write(robocopyPrep)
        myBat.close()

        now = datetime.datetime.now() + datetime.timedelta(minutes=1)
        current_time = now.strftime("%H:%M")

        tnPrep = "PREP Replication " + actualMonthYear

        task = 'schtasks /Create /TN "Replication Tasks\\' + str(tnPrep) + '"' + ' /TR "C:\\Users\\' + str(ads)  +  '\\Desktop\\repPrep' + str(actualMonthYear) + '.bat" /sc ONCE /ST ' + str(current_time) + ' /RU ' + str(ads) + ' /RP ' + str(auth)
        print (task)
        os.system(task)
        statusPrep = False

        time.sleep(7200)
        while (statusPrep != True):

            statusPrep = check_task_status(tnPrep)

            if statusPrep == True:
                print("PREP Replication successfully resolved")
                return statusPrep
            
def addOffice32App (actualPrepRelease):
    with open('addAppToPrep.ps1', 'w') as f:
        
        f.write('Import-Module "C:\\Program Files\\Microsoft Deployment Toolkit\\Bin\\MicrosoftDeploymentToolkit.psd1"\n')
        f.write('New-PSDrive -Name "DS001" -PSProvider "MDTProvider" -Root "' + actualPrepRelease + '"\n') 
        f.write (('Import-MDTApplication -Path "DS001:\\Applications\\Accenture Core Applications" -Enable "True" -Name "Microsoft Office Click-to-Run EN-US x86" -ShortName "Office Click-to-Run " -Version "1.0" -Publisher "Microsoft" -Language "en-US" -CommandLine "cscript.exe Install_O365_C2R_32.wsf" -WorkingDirectory ".\\Applications\\Accenture Office Click-to-Run EN-US" -ApplicationSourcePath ' ) + '"' + ( actualPrepRelease) + ("\\Applications\\Accenture Office Click-to-Run EN-US") + '"' +   '-DestinationFolder "Accenture Core Applications" -Verbose ')

    office32App = subprocess.Popen(['powershell.exe', '-File', "C:\\Users\\ads.jaldaya\\Desktop\\addAppToPrep.ps1"], stdout=subprocess.PIPE, shell=True)
    office32App.wait()
    print("Office32 added to deploy share")