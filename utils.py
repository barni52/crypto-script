def styleDecider(num):
    if float(num) >= 0:
        return "green";
    else:
        return "red";

def toHUF(num):
    return format(str(num * 405));

def toRON(num):
    return str(num * 5);