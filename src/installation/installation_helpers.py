#!/usr/bin/env python3
'''
Created on Aug 26, 2014

@author: samu
'''

import subprocess

def add_user_ubuntu(username, home_dir_creation=True):
    if home_dir_creation:
        cmd = 'useradd -m %s' %(username)
    else:
        cmd = 'useradd %s' %(username)
        
    subprocess.call(cmd, shell=True)

def del_user_ubuntu(username, home_dir_removal=True):
    if home_dir_removal:
        cmd = 'userdel -r %s' %(username)
    else:
        cmd = 'userdel %s' %(username)
    subprocess.call(cmd %(username), shell=True)

def execute_cmd_on_shell(cmd, as_user=None, where='.'): 
    '''
    executes a command on the shell, either as the current user
    or as the user in the as_user param.
    '''
    cmd.strip()
    if as_user == None:
        subprocess.call('cd %s &&' %(where) + cmd, shell=True)
    else:
        subprocess.call('sudo -H -u %s bash -c ' %(as_user) + '\'' + 'cd %s &&' %(where) + cmd + '\'', shell=True)

def download_and_extract_steam_cmd(where, as_user=None):
    execute_cmd_on_shell('curl -O http://media.steampowered.com/installer/steamcmd_linux.tar.gz', as_user, where)
    execute_cmd_on_shell('tar -xvzf steamcmd_linux.tar.gz', as_user, where)
    execute_cmd_on_shell('rm steamcmd_linux.tar.gz', as_user, where)


