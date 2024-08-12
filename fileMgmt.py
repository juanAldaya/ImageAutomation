import timeMgmt
import os
import shutil




def check_file_exists(folder_path, filePath):
    file_path = os.path.join(folder_path, filePath)
    return os.path.isfile(file_path)


def folderIsEmpty (path):
    if len(os.listdir(path)) == 0:
        return True
    else:
        return False



def checkReleases (wkPath, imagesPath):
    folderActual = str((timeMgmt.threeFirstChars(timeMgmt.previousMonthName())+timeMgmt.lastTwoDigitsOfTheYear())) 
 
    newRelease = search_folder(wkPath, folderActual)
    if newRelease:
        
        checkFile = str(timeMgmt.threeFirstChars(timeMgmt.previousMonthName())) + str(timeMgmt.datetime.datetime.now().year) + "_Ready.txt"
    
        isReleaseCustomized = check_folder_exists(imagesPath, "Win11_"+ timeMgmt.threeFirstChars(timeMgmt.previousMonthName())+"_"+timeMgmt.lastTwoDigitsOfTheYear())
        
        if check_file_exists(newRelease, checkFile) and isReleaseCustomized == False: ###CAMBIAR A FALSEEEEE

            return newRelease
    else:
       return None


def search_folder(root_folder, folder_name):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        if folder_name in dirnames:
            return os.path.join(dirpath, folder_name)
    return None

def check_folder_exists(parent_folder, child_folder):

    folder_path = os.path.join(parent_folder, child_folder)
    return os.path.isdir(folder_path)


def compare_and_copy(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_folder, file)
            if not os.path.exists(dest_file):
                print("copio " + str(src_file.title))
                shutil.copy2(src_file, dest_folder)



# def formatter(element):
#         if isinstance(element, Comment):
#             return f"<!--{element if element is not None else ''}-->"
#         else:
#             return None

# def captureOutput():
#     command = 'wmic logicaldisk get deviceid'
#     result = subprocess.run(command, capture_output=True, text=True)
#     output = result.stdout.strip()
#     return output



