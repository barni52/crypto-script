from os.path import exists, getmtime
from datetime import datetime, timedelta

def olderThan(fileName, hours = 1):
    if exists(fileName):
        fileTime = getmtime(fileName);
        return datetime.now() - datetime.fromtimestamp(fileTime) > timedelta(hours = hours);
    else:
        return True;

def styleDecider(num):
    if float(num) >= 0:
        return "green";
    else:
        return "red";

def toHUF(num):
    return format(str(num * 405));

def toRON(num):
    return str(num * 5);