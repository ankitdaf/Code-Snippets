#!/bin/bash
# Backup and restore packages to clone my environment faster

# TODO: Backup my sources list as well

# Backup my packages
sudo dpkg --get_selections  | grep -v deinstall > selections.list
# Backup my sources list
sudo cp /etc/apt/sources.list ./

#Restore my packages
sudo dpkg --clear-selections
sudo dpkg --set-selections < selections.list
sudo apt-get install dselect
sudo dselect update
sudo dselect install

#Restore my software sources, force overwrite but make a backup
#To append or to replace, that is the question

sudo cp -fb ./sources.list /etc/apt/