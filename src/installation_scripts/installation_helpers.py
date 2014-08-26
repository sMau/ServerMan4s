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

def execute_cmd_on_shell(cmd, as_user=None): 
    '''
    executes a command on the shell, either as the current user
    or as the user in the as_user param.
    '''
    cmd.strip()
    if as_user == None:
        subprocess.call(cmd, shell=True)
    else:
        subprocess.call('sudo -H -u %s bash -c ' + cmd %(as_user))
        