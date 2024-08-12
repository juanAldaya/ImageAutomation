import pandas as pd



# 
# 
# 
# 
# ##gdnoumapping
def gdnOUMapping (scriptsLastReleaseProv, scriptsActualReleaseProv):

    lastGdnMapping = scriptsLastReleaseProv+ "\\GDNOUMapping.csv"
    actualGdnMapping = scriptsActualReleaseProv + "\\GDNOUMapping.csv"

    df1 = pd.read_csv(lastGdnMapping)
    df1.to_csv(actualGdnMapping)

    print("GDN OU Mapping succesfully updated")


def modelAliasPrep(scriptFolderLastRelease, scriptFolderActualRelease):
    lastModelAliasPrep = str(scriptFolderLastRelease)+"\\ModelAlias.csv"
    actualModelAliasPrep = str(scriptFolderActualRelease)+"\\ModelAlias.csv"
    df1 = pd.read_csv(lastModelAliasPrep)
    df2 = pd.read_csv(actualModelAliasPrep)

    totalRowsLast = len(df1)
    totalRowsActual = len(df2)
    dif = totalRowsLast - totalRowsActual
    copyRows(lastModelAliasPrep, actualModelAliasPrep,dif, totalRowsActual)
    print("Model Alias succesfully updated")

def copyEntireFile (source_file, target_file, totalRowsLast):

    # Read the source file as a dataframe
    df = pd.read_csv (source_file)
    # Slice the dataframe from the start row to the end
    while totalRowsLast != 0:
        i = 0
        row = df.iloc [i]
        newDf = pd.DataFrame([row])
        newDf.to_csv (target_file, mode='a', header=False, index=False)
        i = i + 1
        totalRowsLast = totalRowsLast -1 


def copyRows (source_file, target_file, dif, totalRowsActual): ##csv for the MODEL ALIAS script.
    # Read the source file as a dataframe
    df = pd.read_csv (source_file)
    # Slice the dataframe from the start row to the end
    while dif != 0:

        row = df.iloc [totalRowsActual]
        newDf = pd.DataFrame([row])
        newDf.to_csv (target_file, mode='a', header=False, index=False)
        dif = dif - 1
        totalRowsActual = totalRowsActual + 1

          
# def keep_comments(text):
#   if isinstance(text, Comment):
#     return "<!--" + text + "-->"
#   else:
#     return text
