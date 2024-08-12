
from infoSvs import infoSvs
import configFiles
import pwScripts
import csvFiles
import timeMgmt
import xmlFiles
import fileMgmt
import ConfigTestShares
import time
import datetime
import ConfigSharesPermissions
import modifyBootsWDS
import os



def get_user_choices():

    choices = []
    while True:
        choice = input("Enter an option (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        choices.append(choice)
    return choices


def execute_scripts_prep(choices):

    script_mapping = {
            '1': lambda: pwScripts.copyThingsPrep(lastPrepRelease, actualPrepRelease),
            '2': lambda: pwScripts.copyPrepScripts(scriptFolderLastRelease, scriptFolderActualRelease),
            '3': lambda: xmlFiles.deployWizardPrep(actualDw, lastDw),
            '4': lambda: csvFiles.modelAliasPrep(scriptFolderLastRelease, scriptFolderActualRelease),
            '5': lambda: xmlFiles.modifyTaskSequencePrep(lastPrepTaskSequence, actualPrepTaskSequence)
            # Add more mappings for additional choices
        }
        
    for choice in choices:
        if choice in script_mapping:
            (script_mapping[str(choice)])()  # Call the corresponding script function
        else:
            print(f"No script found for choice: {choice}")



def execute_scripts_prov(choices):

    script_mapping = {
            '1': lambda: pwScripts.scriptsProv(scriptsLastReleaseProv, scriptsActualReleaseProv),
            '2': lambda: configFiles.boostrapProv(actualReleaseProv),
            '3': lambda: xmlFiles.removeItemDWProv(actualDwProv),
            '4': lambda: xmlFiles.modifyTaskSequenceProv(lastProvTaskSequence, actualProvTaskSequence)
            # Add more mappings for additional choices
        }
        
    for choice in choices:
        if choice in script_mapping:
            
            (script_mapping[str(choice)])() # Call the corresponding script function
        else:
            print(f"No script found for choice: {choice}")




def prepMenu ():
    print("1. Copy $1, Scripts PREP")
    print("2. Custom Settings PREP")
    print("3. Deploy Wizard PREP")
    print("4. Model Alias PREP")
    print("5. Task Sequence PREP\n")

    choices = get_user_choices()
    execute_scripts_prep(choices)

def provMenu():
    print("1. Copy Scripts PROV")
    print("2. Boostrap PROV")
    print("3. Deploy Wizard PROV")
    print("4. Task Sequence PROV\n")
    
    choices = get_user_choices()
    execute_scripts_prov(choices)





def main_menu ():
    os.system('cls')
    print("\n\n##############################################################################")
    print("\nWelcome to the image script, please select an option to do\n")
    print("1.   Replicate PREP")
    print("2.   Replicate PROV")
    print("3.   PREP Customs")
    print("4.   PROV Customs")
    print("5.   Create Shares TEST")
    print("6.   Create shares PROD")
    print("7.   Modify WDS List")
    print("\n##############################################################################")
    choice = int(input("\nEnter an option: "))

    if choice == 1:
        os.system('cls')
        print("PREP replication begin: \n")
        pwScripts.replicationPrep(actualMonthYear, svName)
    elif choice == 2:
        os.system('cls')
        pwScripts.replicationProv(actualMonthYear, svName)
    elif choice == 3:
        os.system('cls')
        prepMenu()
    elif choice == 4:
        os.system('cls')
        provMenu()
    elif choice == 5:
        os.system('cls')
        ConfigTestShares.addShareToTestPrep(actualPrepRelease)
        ConfigTestShares.addShareToTestProv(actualPrepRelease)

    elif choice == 6:
        os.system('cls')
        share = input("Enter this month share: New or Actual \n")

        ConfigSharesPermissions.addShareToActualPrep(actualPrepRelease, share)

        ConfigSharesPermissions.addShareToActualProv(actualPrepRelease, share)
    elif choice == 7:
        os.system('cls')
        modifyBootsWDS.modifyBoots()
    
def serverChoice():
    print("\nPP1 (FS)")
    print("PP2 (DMM)")
    print("ROS (Rosario)")
    print("BMP (Mardel)")
    print("CHI (Chile)")
    print("C7 (Carrera 7)")
    print("MDW (Medellin)")
    print("BQI (Barranquilla)")
    print("CRI (?)")
    print("CAR (Real Cariari)\n")
    svName = input('\nEnter the Server Name: (ex. BMP): ')
    return svName


svName = serverChoice()

#########  VARIABLES THAT NEED THE PREVIOUS FUNCTIONS AND NEEDED FROM PREP REP####


actualMonthYear = str(timeMgmt.threeFirstChars(timeMgmt.previousMonthName())+timeMgmt.lastTwoDigitsOfTheYear()) # EX. MAY 24 ACTUAL

lastMonthYear = str(timeMgmt.get_month_name_two_months_ago()+str(timeMgmt.lastTwoDigitsOfTheYear()))# EX. APRIL 24 LAST

actualYear = str(datetime.datetime.now().year)

imagesPath = infoSvs[svName]['local']

WkPath = infoSvs[svName]['global']  ## WK DISK GLOB TEAM. SOURCE



actualPrepRelease = imagesPath + '\\Win11_' + timeMgmt.threeFirstChars(timeMgmt.previousMonthName())+ "_" + actualYear + '\\Deploy'
lastPrepRelease = imagesPath + '\\Win11_' + str(timeMgmt.threeFirstChars(timeMgmt.get_month_name_two_months_ago())) + "_" + actualYear + "\\Deploy" #possible error when the year is still last one and not the actual (like december)



### SCRIPTS FOLDERS
scriptFolderActualRelease = actualPrepRelease + "\\Scripts"
scriptFolderLastRelease = lastPrepRelease + "\\Scripts"


## TASK SEQUENCE

actualPrepTaskSequence = actualPrepRelease+"\\Control\\WIN11PREP_" + str(timeMgmt.last_month_number()) + str(timeMgmt.lastTwoDigitsOfTheYear()) + "\\ts.xml"
lastPrepTaskSequence = lastPrepRelease+ "\\Control\\WIN11PREP_" + str(timeMgmt.get_month_two_months_ago()) + str(timeMgmt.lastTwoDigitsOfTheYear()) + "\\ts.xml"



actualCSPrep = actualPrepRelease + "\\Control\\CustomSettings.ini"
lastCSPrep = lastPrepRelease + "\\Control\\CustomSettings.ini"

##DEPLOY WIZRD FILES
actualDw = scriptFolderActualRelease + "\\DeployWiz_Definition_ENU.xml"
lastDw = scriptFolderLastRelease + "\\DeployWiz_Definition_ENU.xml"


lastReleaseProv = lastPrepRelease + "\\$OEM$\\ProvisioningPackage\\Deploy"
actualReleaseProv = actualPrepRelease + "\\$OEM$\\ProvisioningPackage\\Deploy"

scriptsLastReleaseProv = lastReleaseProv+'\\Scripts' # The source directory
scriptsActualReleaseProv = actualReleaseProv+'\\Scripts' # The destination directory

actualProvTaskSequence = actualReleaseProv + "\\Control\\APP-WINX-CIO\\ts.xml"
lastProvTaskSequence = lastReleaseProv  + "\\Control\\APP-WINX-CIO\\ts.xml"

lastCustomSettingsGDN = lastReleaseProv + "\\Control\\CustomSettingsGDN.ini"
actualCustomSettingsGDN = actualReleaseProv + "\\Control\\CustomSettingsGDN.ini"

lastProvCustomSettings = lastReleaseProv + "\\Control\\CustomSettings.ini"
actualProvCustomSettings = actualReleaseProv + "\\Control\\CustomSettings.ini"        

actualDwProv = scriptsActualReleaseProv + "\\DeplowWiz_Definition_ENU.xml"









main_menu()

