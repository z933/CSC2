import sys
import time 

a = 'something  something 2'

for char in a:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(1)