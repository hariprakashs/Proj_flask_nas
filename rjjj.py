#Date to Epoch Time convertor
#using time.mktime package in Python

import time
#function to check the date is in prefect format
def check_date(date):
    date_len=len(date)
    if date_len == 8:
        if date[0] > '1' and date[1] > '2':
            format='%d%m%Y'
        elif date[2] > '1' and date[3] > '2':
            format='%m%d%Y'
        else:
            format='%d%m%Y'
    elif date_len == 11:
        if date[2]=='/' or date[2]=='.' or date[2]=='-':
            if date[2]==date[5]:
                split=date[2]
                if split=='/':
                    if date[0] > '1' and date[1] > '2':
                        format='%d/%m/%Y'
                    elif date[3] > '1' and date[4] > '2':
                        format='%m/%d/%Y'
                    else:
                        format='%d/%m/%Y'
                elif split=='.':
                    if date[0] > '1' and date[1] > '2':
                        format='%d.%m.%Y'
                    elif date[3] > '1' and date[4] > '2':
                        format='%m.%d.%Y'
                    else:
                        format='%d.%m.%Y'
                elif split=='-':
                    if date[0] > '1' and date[1] > '2':
                        format='%d-%m-%Y'
                    elif date[3] > '1' and date[4] > '2':
                        format='%m-%d-%Y'
                    else:
                        format='%d-%m-%Y'
                else:
                    print("Unable to convert theprovided date")
            else:
                print("Unable to convert theprovided date")
        else:
            print("Unable to convert theprovided date")
    else:
        print("Unable to convert theprovided date")
        format='NULL'

    return format


def get_input():
    ip=input("Enter the date")
    return ip


def change_to_epoch(date,format):
    epoch = int(time.mktime(time.strptime(date, format)))
    return epoch
#Main Code starts

iput=get_input()

format=check_date(iput)
if format !='NULL':
    print(change_to_epoch(iput,format))
