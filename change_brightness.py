#!/usr/bin/env python2
import os
import sys

max = os.popen("cat /sys/class/backlight/intel_backlight/max_brightness").read().strip()
cur = os.popen("cat /sys/class/backlight/intel_backlight/brightness").read().strip()

if len(sys.argv) > 1:
    if sys.argv[1] not in ['up', 'down']:
        print 'invalid argument'
        sys.exit(1)
else:
    print "max: " + max
    print "current: " + cur
    sys.exit(1)

max = int(max)
cur = int(cur)

dst = cur
if sys.argv[1] == 'up':
    dst += 50
else:
    dst -= 50

if dst < 1:
    dst = 1

if dst > max:
    dst = max

cmd = 'echo %d > /sys/class/backlight/intel_backlight/brightness' % dst
print cmd
os.system(cmd)
