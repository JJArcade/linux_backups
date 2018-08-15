#!/usr/bin/env python
import subprocess, sys, os
import re

# GET SCREEN SIZE
cmd = ['xrandr']
cmd2 = ['grep', '*']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
p.stdout.close()

res_str, junk = p2.communicate()
res = res_str.split()[0]
w, h = res.split('x')
w = int(w)
h = int(h)

print("Height:\t%d\nWidth:\t%d" % (h, w))

# LIST WINDOWS IN DESKTOP
cmd = ['wmctrl', '-l']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
windows, err = p.communicate()
windows = windows.splitlines()
win_store = []
for a in windows:
    print("A:")
    i = 0
    temp = {}
    for b in a.split():
        print("\tB:\t{}".format(b))
        if i == 0:
            temp["id"]=b
        elif i == 1:
            temp["desktop"]=b
        i+=1
    win_store.append(temp)

# Get current desktop
cmd = ['wmctrl', '-d']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
desks, err = p.communicate()
desks = desks.splitlines()
curr_desktop = 0
for d in desks:
    if bool(re.search("\*", d)):
        curr_desktop = d.split()[0]
        print("The current desktop is %s" % curr_desktop)

# Get tile count
tile_count = 0
for a in win_store:
    if a["desktop"] == curr_desktop:
        tile_count+=1

# Get tile case
handle_padding = 10
border_size = 3
if tile_count>1:
    if tile_count==2:   #Vertical tiling
        x = 0
        y = 0
        win_w = w
        win_h = (h/2)
        for a in win_store:
            if a["desktop"]==curr_desktop:
                cmd = ["wmctrl", "-i", "-r", a["id"], \
                        "-e", "0,{},{},{},{}".format(x,y,win_w,win_h)]
                print(cmd)
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                y = h-win_h
                y+=border_size
                win_h = h-(win_h+(2*handle_padding)+border_size)
    elif tile_count==3:
        subprocess.Popen(["/home/jess/popup.sh", "Select the main window"])
        x = 0
        y = 0
        win_h = h - handle_padding - (border_size*3)
        win_w = w/2
        cmd = ["wmctrl", "-r", ":SELECT:", "-e", \
                "0,0,0,{},{}".format(win_w, win_h)]
        p = subprocess.call(cmd, stdout=subprocess.PIPE)
        #find the moved window
        cmd = ["wmctrl", "-lG"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        wins, err = p.communicate()
        main_win = ""
        for a in wins.splitlines():
            if curr_desktop==a.split()[1]:
                x = int(a.split()[2])
                y = int(a.split()[3])
                x-=2
                y-=44
                if x==0 and y==0:
                    main_win=a.split()[0]
        #move the other windows
        x = win_w
        y=0
        win_h = (h/2) - handle_padding
        for a in win_store:
            if a["desktop"]==curr_desktop and a["id"]!=main_win:
                cmd = ["wmctrl", "-i", "-r", a["id"], \
                        "-e", "0,{},{},{},{}".format(x,y,win_w,win_h)]
                subprocess.Popen(cmd)
                y = win_h
                win_h = h-(win_h+(2*handle_padding)+(2*border_size))
