import time
import sys


pykafe = ("Welcome " "to " + "Pykafe")

for item in range(17):
    time.sleep(0.1)
    sys.stdout.write(pykafe[item % len(pykafe)])
    sys.stdout.flush()
