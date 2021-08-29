import subprocess


def toprint(cont):

    print("Printing: ", cont)
    with open("/dev/usb/lp0", "w") as outFile:
        subprocess.run(["echo", cont], stdout=outFile)

def eightyCharChunk(string):
    splits = []
    length = 0
    curstr = ""
    for char in string:
        curstr += char
        length += 1
        if length == 80:
            splits.append(curstr)
            curstr = ""
            length = 0
    splits.append(curstr)
    #while len(string) >= 80:
    #    splits.append(string[0:80])
    #    string = string[80: len(string)]
    #splits.append(string)
    return splits

def sanitize(string):
    return ascii(string)[1:-1]
