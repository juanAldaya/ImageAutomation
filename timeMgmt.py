import timedelta
import subprocess

import calendar
import datetime


def captureOutput():
    command = 'wmic logicaldisk get deviceid'
    result = subprocess.run(command, capture_output=True, text=True)
    output = result.stdout.strip()
    return output


def get_month_name_two_months_ago():
    # Get today's date
    today = datetime.date.today()

    # Calculate the date for two months ago
    two_months_ago = today - datetime.timedelta(days=60)

    # Get the month name (full name)
    month_name = two_months_ago.strftime("%B")

    # Return the first 3 characters of the month name
    return month_name[:3]


def format_month_number(month_number):
    # Convert the month number to a string
    month_str = str(month_number)

    # Add a leading zero if the month number is one digit
    if len(month_str) == 1:
        month_str = "0" + month_str

    return month_str

def get_month_two_months_ago():
    # Get the current date
    today = datetime.date.today()

    # Subtract two months from the current date
    two_months_ago = today - datetime.timedelta(days=60)

    # Get the formatted month number (with leading zero if needed)
    formatted_month = two_months_ago.strftime("%m")

    return formatted_month



def previousMonthName ():
        
            # Get the current month
            currentMonth = datetime.datetime.now().month
            currentMonthName = calendar.month_name[currentMonth]

            # Get the previous month
            previousMont = currentMonth - 1 if currentMonth > 1 else 12 #way to write in one line. a lit dirty
            previousMonthName = calendar.month_name[previousMont]

            return previousMonthName


def last_month_number():
    today = datetime.date.today()
    first = today.replace(day=1)
    last_month = first - datetime.timedelta(days=1)
    return last_month.strftime("%m")

def get_prev_month_name():
    today = datetime.date.today()# Get the current date
 
    prev_month = (today.month - 1) % 12# Get the month number of two months ago
    month_name = calendar.month_name[prev_month]# Get the name of the previous month from the calen
    print(prev_month)
    return month_name[:3] # Return the first three characters of the month name

def get_prev_Twomonth_name():
    today = datetime.date.today()# Get the current date
    prev_month = (today.month - 3) % 12# Get the month number of two months ago
    month_name = calendar.month_name[prev_month]# Get the name of the previous month from the calen
    return month_name[:3]




def threeFirstChars (previousMonth):
    abvMonth = previousMonth[0] + previousMonth[1] + previousMonth[2]
    return abvMonth

def lastTwoDigitsOfTheYear ():
    actualYear = str((datetime.datetime.now().year))
    abvYear = actualYear[-2] + actualYear[-1]
    return abvYear


def get_two_months_ago_month_number():
    # Get the current date
    today = datetime.date.today()

    # Calculate the date two months ago
    two_months_ago = today - datetime.timedelta(days=60)

    # Get the month number of the date two months ago
    month_number = two_months_ago.month

    # Return the month number as a two-digit string
    return f"{month_number:02d}"
        

