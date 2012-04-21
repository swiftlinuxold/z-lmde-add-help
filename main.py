#! /usr/bin/env python

# Check for root user login
import os, sys
if not os.geteuid()==0:
    sys.exit("\nOnly root can run this script\n")

# Get your username (not root)
import pwd
uname=pwd.getpwuid(1000)[0]

# The remastering process uses chroot mode.
# Check to see if this script is operating in chroot mode.
# /home/mint directory only exists in chroot mode
is_chroot = os.path.exists('/home/mint')
dir_develop=''
if (is_chroot):
	dir_develop='/usr/local/bin/develop'
	dir_user = '/home/mint'
else:
	dir_develop='/home/' + uname + '/develop'
	dir_user = '/home/' + uname

# Everything up to this point is common to all Python scripts called by shared-* scripts
# ======================================================================================

import shutil

def message (string):
    os.system ('echo ' + string)

def elim_dir (dir_to_elim): 
	if (os.path.exists(dir_to_elim)):
		shutil.rmtree (dir_to_elim)

def create_dir (dir_to_create):
    if not (os.path.exists(dir_to_create)):
        os.mkdir (dir_to_create)
    
message ('=======================')
message ('BEGIN ADDING HELP PAGES')

dir1 = '/usr/share/swiftlinux'
create_dir (dir1)
dir2 = '/usr/share/swiftlinux/help'
create_dir (dir2)

source = dir_develop + '/add-help/help/*'
dest = dir2
os.system ('cp ' + source + ' ' + dest)

message ('FINISHED ADDING HELP PAGES')
message ('==========================')
