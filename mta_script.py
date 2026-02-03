#!/proj/sot/ska3/flight/bin/python

from cxotime import CxoTime
import foobar

def main():

    now = CxoTime()
    contents = f"{now.date} - {now.secs}\n"
    contents += f"{foobar.core.VAR1}\n"
    contents += f"{foobar.functions.useful_function(foobar.core.VAR2)}\n"

    with open("test.txt",'w') as f:
        f.write(contents)

if __name__ == "__main__":

    main()
