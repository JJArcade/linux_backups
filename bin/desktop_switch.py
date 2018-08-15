#!/usr/bin/env python
import subprocess
import re, sys

# Get current desktop
cmd = ['wmctrl', '-d']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
desks, err = p.communicate()
desks = desks.splitlines()
curr_desktop = 0
max_desktop = -1
for d in desks:
    if bool(re.search("\*", d)):
        curr_desktop = d.split()[0]
        #print("The current desktop is %s" % curr_desktop)
    max_desktop+=1
curr_desktop = int(curr_desktop)

if sys.argv[1] == "--next":
    if curr_desktop!=max_desktop:
        cmd = ["wmctrl", "-s", str(curr_desktop+1)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    else:
        cmd = ["wmctrl", "-s", "0"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
elif sys.argv[1] == "--prev":
    if curr_desktop!=0:
        cmd = ["wmctrl", "-s", str(curr_desktop-1)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    else:
        cmd = ["wmctrl", "-s", str(max_desktop)]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

