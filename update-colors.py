import sys, re
import subprocess
import os

def wallpaper_select():
    x=1
    pngs=[]
    for a in os.listdir('/home/jess/Pictures/wallpapers/'):
        if bool(re.search(".png",a)):
            print("%s:\t%s" % (x,a))
            x+=1
            pngs.append(a)
        choice_made=False
    while not choice_made:
        choice=input("Enter just the number of your selection:\n")
        if re.match("[0-9]", choice):
            choice_made=True
        else:
            print("Invalid selection, try again.")
    return "/home/jess/Pictures/wallpapers/" + pngs[int(choice)-1]

def replace_hex(new_hex, old_line):
        temp = old_line


def change_urxvt():
    #Pick a background image
    wallpaper = wallpaper_select()
    print(wallpaper)

    #break down colors of wallpaper
    os.system("~/Pictures/wallpapers/colors/colors -n 16 %s > ~/Pictures/wallpapers/tmp-colors.txt" % wallpaper)
    colors_files = open("/home/jess/Pictures/wallpapers/tmp-colors.txt", 'r')
    x=0
    colors={}
    for a in colors_files.readlines():
        #print("color%s:\t%s" %(x,a))
        colors[x] = a[:len(a)-1]    #trim off the new line delimeter
        x+=1

    #Open the .xresources file
    xres = open("/home/jess/.Xresources", 'r')
    lines = xres.readlines()
    print(lines)
    xres.close()

    #find locations of color settings in file
    xres_color_locs = {"fg":0, "bg":0}
    plain_color_locs=[]
    i = 0
    for a in range(0,len(lines)):
        current_line = lines[a]
        b = re.search("#.{6}", current_line)
        if bool(b):
            print(current_line[0:len(current_line)-1])
            c = re.search("foreground", current_line)
            if bool(c):
                xres_color_locs["fg"] = a
            c = re.search("background", current_line)
            if bool(c):
                xres_color_locs["bg"] = a
            c = re.search("color", current_line)
            if bool(c):
                plain_color_locs.append(a)

    #Color selection of background and foreground
    os.system("~/Pictures/wallpapers/colors/colors -n 16 %s | ~/Pictures/wallpapers/colors/bin/hex2col" % wallpaper)
    #print("Pick a color for the foreground.")
    for a in range(0,16):
        print("%s:\t%s" % (a, colors[a]))
    selected = False
    while not selected:
        fg_pick = input("Pick a color for the foreground: ")
        if bool(re.match("[0-9]+", fg_pick)):
            selected = True
            fg_pick = int(fg_pick)
        else:
            print("Invalid selection, try again.")
    selected = False
    while not selected:
        bg_pick = input("Pick a color for the background: ")
        if bool(re.match("[0-9]+", bg_pick)):
            selected = True
            bg_pick = int(bg_pick)
        else:
            print("Invalid selection, try again.")

    #write changes to Xresources
    new_fg = "*.foreground:\t%s\n" % colors[fg_pick]
    lines[xres_color_locs["fg"]] = new_fg
    new_bg = "*.background:\t%s\n" % colors[bg_pick]
    lines[xres_color_locs["bg"]] = new_bg
    for a in plain_color_locs:
        new_str = "*color%s:\t%s\n" % (a-8, colors[a-8])
        lines[a] = new_str
    new_xres = open("/home/jess/.Xresources", 'w')
    for a in lines:
        new_xres.write(a)
    new_xres.close()
    os.system("feh --bg-fill %s" % wallpaper)
    os.system("xrdb /home/jess/.Xresources")
    change_i3([colors[fg_pick], colors[bg_pick]], wallpaper)

def change_i3(fg_and_bg, background):
    #open and get config file
    i3_config = open("/home/jess/.config/i3/config", 'r')
    config_lines = i3_config.readlines()
    #find fg and bg variables
    print("FINDING VARIABLES")
    fg_bg_locs = {"bg":0, "fg":0}
    backgrond_loc = 0
    for x in range(0, len(config_lines)):
        a = config_lines[x]
        money_bg = re.search("set \$bg", a)
        money_fg = re.search("set \$fg", a)
        feh_setting = re.search('exec feh', a)
        if bool(money_fg):
            fg_bg_locs["fg"] = x
            print(a)
            print(x)
        if bool(money_bg):
            fg_bg_locs["bg"] = x
            print(a)
            print(x)
        if bool(feh_setting):
            backgrond_loc = x
    #change hexcodes
    print("CHANGING VARIABLES")
    for a in ["fg", "bg"]:
        temp_str = "set $%s\t%s"
        if a == "fg":
            temp_str = temp_str % (a, fg_and_bg[0])
        else:
            temp_str = temp_str % (a, fg_and_bg[1])
        config_lines[fg_bg_locs[a]] = temp_str + "\n"
        print(config_lines[fg_bg_locs[a]])
    #change background
    config_lines[backgrond_loc] = "exec feh --bg-fill " + background + "\n"
    #write to config files
    i3_config = open("/home/jess/.config/i3/config", 'w')
    for a in config_lines:
        i3_config.write(a)
    i3_config.close()
    os.system("i3 reload")
    os.system("i3 restart")


def main():
    change_urxvt()

main()
