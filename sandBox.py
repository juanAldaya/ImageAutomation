# def rotatePassword ():

#     svName = input("SV")

#     nameWimNew = "Win1122H2_WDS07_New.wim"
#     nameWimActual = "Win1122H2_WDS07_Actual.wim"

#     rutaWimNew = infoSvs[svName]["local"] + "\\NewWim11\\" + nameWimNew
#     rutaWimActual = infoSvs[svName]["local"] + "\\NewWim11\\" + nameWimActual


#     option = input("Mount NEW or ACTUAL? (1/2): ")

#     if option == 1:

#         mountFolder = input("Nombre carpeta MOUNT: ")

#         rutaMount = infoSvs[svName]["local"][1] + "\\" + str(mountFolder)

#         if folderIsEmpty(rutaMount):

#             c1 = "cd C:\\Program Files (x86)\\Windows Kits\\10\\Assessment and Deployment Kit\\Deployment Tool"
#             resultV = os.system(c1)

#             c2 = "imagex.exe /mountrw /check" + rutaWimNew + "1" + rutaMount

#             resultV = os.system(c2)
#             input("press any key to continue")
#             if resultV == '0':
#                 modifyBootstrapWim(rutaMount, "New")
#                 input("press any key to continue, bootstrap modified")

#     elif option == 2: 

#         mountFolder = input("Nombre carpeta MOUNT: ")

#         rutaMount = infoSvs[svName]["local"][1] + "\\" + str(mountFolder)

#         if folderIsEmpty(rutaMount):

#             c1 = "cd C:\\Program Files (x86)\\Windows Kits\\10\\Assessment and Deployment Kit\\Deployment Tool"
#             resultV = os.system(c1)

#             c2 = "imagex.exe /mountrw /check" + rutaWimActual + "1" + rutaMount

#             resultV = os.system(c2)
#             input("press any key to continue")
#             if resultV == '0':
#                 modifyBootstrapWim(rutaMount, "Actual")
#                 input("press any key to continue, bootstrap modified")
#         else:
#             print("Mount folder is corrupted")

#     return None

# def modifyBootstrapWim(iniFile): ## SETTINGS FILES AS INI FILES

#     config = configobj.ConfigObj(iniFile)

#     print(isNewOrActual(config))
    # config['Settings']['Priority'] = 'Default'

    # config['Default']['DeployRoot'] = '\\%WDSServer%\Win11' + optionWim + "$"
    # config['Default']['SkipBDDWelcome'] = 'YES'
    # config['Default']['UserPassword'] = "WK~=bGdafb)z6F0d1Wfk"
    # config['Default']['UserID'] = 'mpc.latam.app '


    # config.write()

