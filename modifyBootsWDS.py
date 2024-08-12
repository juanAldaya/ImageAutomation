import time
import subprocess
import calendar
from datetime import datetime, timedelta
from infoSvs import infoSvs
def get_month_three_months_ago():
    # Get the current date
    today = datetime.today()

    # Calculate the date three months ago
    three_months_ago = today - timedelta(days=90)

    # Get the month from the three months ago date
    month_name = calendar.month_name[three_months_ago.month]

    return month_name

def get_month_two_months_ago():
    # Get the current date
    today = datetime.today()

    # Calculate the date two months ago
    two_months_ago = today - timedelta(days=60)

    # Get the month from the two months ago date
    month_name = calendar.month_name[two_months_ago.month]

    return month_name

def get_month_one_month_ago():
    # Get the current date
    today = datetime.today()

    # Calculate the date two months ago
    one_month_ago = today - timedelta(days=30)

    # Get the month from the two months ago date
    month_name = calendar.month_name[one_month_ago.month]

    return month_name



def modifyBoots():

    relaseToReplace = 'Set-WdsBootImage -Architecture x64 -ImageName "02 - ' + str(get_month_three_months_ago()) + ' Accenture Global Image" -DisplayOrder 1 -NewImageName "01 - ' + str(get_month_one_month_ago()) + ' Accenture Global Image" '
    subprocess.run(['powershell', '-Command', relaseToReplace], capture_output=True, text=True)
    time.sleep(10)

    relaseToUpdate = 'Set-WdsBootImage -Architecture x64 -ImageName "01 - ' + str(get_month_two_months_ago()) + ' Accenture Global Image" -DisplayOrder 2 -NewImageName "02 - ' + str(get_month_two_months_ago()) + ' Accenture Global Image" '
    subprocess.run(['powershell', '-Command', relaseToUpdate], capture_output=True, text=True)
    time.sleep(15)
    print("Boot options in WDS modified successfuly")