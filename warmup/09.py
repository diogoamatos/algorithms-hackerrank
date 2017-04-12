#!/bin/python
# Time convertion

import sys
from time import strptime

time = raw_input().strip()

time = strptime(time, "%I:%M:%S%p")

print "%02d:%02d:%02d" % (time.tm_hour, time.tm_min, time.tm_sec)
