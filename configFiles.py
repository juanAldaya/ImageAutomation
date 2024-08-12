import configobj
import os
from infoSvs import infoSvs

def print_config(config_file_path):
    """
    Reads a config file and prints the entire dictionary.
    Args:
        config_file_path (str): Path to the config file.
    """
    try:
        config = configobj.ConfigObj(config_file_path)
        for section, section_dict in config.items():
            print(f"[{section}]")
            for key, value in section_dict.items():
                print(f"    {key} = {value}")
        
    except Exception as e:
        print(f"Error reading the config file: {e}")





def configSettingsPrep(lastShare, configFinalCS):
     

    


    ##KEY SETTINGS 
    
    configFinalCS['Settings']['Priority'] = 'SetModel', 'DefaultGateway', 'Default', 'CPWinXUEFI', 'WebSenseCheck'

    configFinalCS['Settings']['Properties'] = 'EIDName', 'SkipEIDName','myStrSite','LocalUser','CIOGDNORG','SkipOrg', 'ModelAlias', 'InstallWebSense', 'MDTBuildDate','SMSMDTDeployDate', 'AppDeployRoot', 'IsNVMe'

    ##KEY DEFAULT##


    configFinalCS['Default']['SkipAdminPassword'] = 'YES'
    configFinalCS['Default']['SkipSummary'] = 'YES'
    configFinalCS['Default']['AdminPassword'] = 'Empanada1'
    configFinalCS['Default']['SkipTimeZone'] = 'YES'

    file = "\\"+'\\%WDSServer%\\'+'APP'+ str(isNewOrActual(lastShare))+'_11$'##RESOLVE IF THIS RELEASE IS NEW OR ACTUAL

    configFinalCS['Default']['SkipFinalSummary'] = 'YES'
    configFinalCS['Default']['APPDeployRoot'] = file
    configFinalCS['Default']['SkipOrg'] = 'NO'
    configFinalCS['Default']['ProjectOU'] = 'BPO'
    configFinalCS['Default']['CIOGDNORG'] = 'CIO'

    configFinalCS.write()
    print("Custom Settings Prep modified successfully")


def generateNewCSPrep (lastCS, actualCS, actualRelease):##########

    
    fileTestPath = actualRelease + "\\Control\\CustomSettings1.ini"

    try:
        



        os.system('echo # > ' + fileTestPath)



        configActualCS = configobj.ConfigObj(actualCS)
        configFinalCS = configobj.ConfigObj(fileTestPath)
        
       

        itSections = 1

        for section, section_dict in configActualCS.items(): ## Itera entre todas las secciones (default, arg, etc) en el custom settings prep que llego este mes
            
            configFinalCS[section] = {}
            for key, value in section_dict.items():
                    
                    configFinalCS[section][key] = value
                    
            if itSections == 2: ## se asegura de copiar solo los primeros dos             
            ###########acá tengo que copiar los default y los paises del ultimo prep CS solo va a copiar las secciones abajo declaradas
                configLastCS = configobj.ConfigObj(lastCS)
                
                for section, section_dict in configLastCS.items():
                    
                    if section == 'DefaultGateway' or section == 'CHI' or section == 'ARG' or section == 'COL'  or section == 'CRI':

                        configFinalCS[section] = {}

                        for key, value in section_dict.items():

                            configFinalCS[section][key] = value

            itSections += 1
     
        configFinalCS.write()

        configSettingsPrep(lastCS, configFinalCS)
        os.system('del ' + actualCS)
        os.system('ren ' + fileTestPath  + ' ' + actualCS)

    except Exception as e:
        print(f"Error reading the config file: {e}")

    return None


def configCSProv (csProvMay):

    configActualCS = configobj.ConfigObj(csProvMay)

    configActualCS['Settings']['Properties'] = 'EIDName','SkipEIDName','SkipApp','myStrSite','LocalUser','CIOGDNORG','SkipOrg','ModelAlias','SkipGDNSiteName','CPLocalization','CPOEMInfo','InstallWebSense','SMSMDTDeployDate','CurrentOSVer','PreviousOSVer','SkipProvisionSelect','ManagePC','LineOfBusiness','BETSInstall','CPStrict','InstallGDNAvecto','SkipComputerName','SkipDomainMembership','DeploymentType','OtherOwner','IsTech','ISSCOS','SkipPDRPanel', 'SkipCPCredentials'
    configActualCS['Default']['SkipAdminPassword'] = 'YES'
    configActualCS['CP_UEFI']['SkipBitlocker'] = 'YES'
    configActualCS['Default']['TimeZone'] = ''
    configActualCS['Default']['TimeZonaName'] = ''

    configActualCS.write()
    return None



def modifyBootstrapWim(rutaMount, optionWim):

    iniFile = rutaMount + "\\Deploy\\Scripts\\Bootstrap.ini"

    config = configobj.ConfigObj(iniFile)

    # config['Settings']['Priority'] = 'Default'

    # config['Default']['DeployRoot'] = '\\%WDSServer%\Win11' + optionWim + "$"
    # config['Default']['SkipBDDWelcome'] = 'YES'
    # config['Default']['UserPassword'] = "WK~=bGdafb)z6F0d1Wfk"
    # config['Default']['UserID'] = 'mpc.latam.app '


    # config.write()


def isNewOrActual(configFile):

    configRoot = configobj.ConfigObj(configFile)

    appRoot = configRoot['Default']['APPDeployRoot']




    if appRoot[-5] == 'l':
        appRoot = "New"
    else:
        appRoot = 'Actual'
    return appRoot



def boostrapProv (actualReleaseProv):

    bootstrapProv = actualReleaseProv + "\\Control\\bootstrap.ini"
    config = configobj.ConfigObj(bootstrapProv)
    config['Default']['UserDomain'] = 'DIR'
    config['Default']['UserID'] = 'mpc.latam.app'

    config['Default']['UserID'] = 'mpc.latam.app'
    config['Default']['UserPassword'] = "G2i7u4)*|E4Xz3zvFlslz"
    config['Default']['DomainAdminDomain'] = 'DIR'
    config['Default']['DomainAdmin'] = 'mpc.latam.app'
    config['Default']['DomainAdminPassword'] = "G2i7u4)*|E4Xz3zvFlslz"
    config['Default']['UserDomain'] = 'DIR'

    config.write()
    

    print("Boostrap Prov modified successfully")










