import subprocess


def toprint(cont):
    print(cont)
    with open("/dev/usb/lp0", "w") as outFile:
        subprocess.run(["echo", cont], stdout=outFile)

def eightyCharChunk(string):
    splits = []
    while len(string) >= 80:
        splits.append(string[0:80])
        string = string[80: len(string)]
    splits.append(string)
    return splits

def sanitize(string):
    return ascii(string)[1:-1]
