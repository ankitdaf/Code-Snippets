#!/bin/bash
# Backup and restore packages to clone my environment faster

# TODO: Backup my sources list as well

# Backup my packages
sudo dpkg --get_selections  | grep -v deinstall > selections.list

#Restore my packages
sudo dpkg --clear-selections
sudo dpkg --set-selections < selections.list
sudo apt-get install dselect
sudo dselect update
sudo dselect install