#!/usr/bin/python3
'''
Created on Sep 23, 2014

@author: samuel
'''
import argparse
import installation_helpers

SRV_SUBPATH = 'srv'
INSTALL_CMD = './steamcmd.sh +login anonymous +force_install_dir %s +app_update 740 validate +quit' %(SRV_SUBPATH)
UPDATE_CMD = './steamcmd.sh +login anonymous +force_install_dir %s +app_update 740 +quit' %(SRV_SUBPATH)

class CS_GO_Server(object):

    def __init__(self, username):
        self.user = username
        installation_helpers.add_user_ubuntu(username, True)

    def download_server_files(self):
        installation_helpers.download_and_extract_steam_cmd('~', self.user)
        #installation_helpers.execute_cmd_on_shell('mkdir %s' %(SRV_SUBPATH), self.user, '~')
        installation_helpers.execute_cmd_on_shell(INSTALL_CMD, self.user, '~')

    def update_server_files(self):
        installation_helpers.execute_cmd_on_shell(UPDATE_CMD, self.user, '~')
    

def parse_args():
    parser = argparse.ArgumentParser(description='Install CS GO server as given user')
    parser.add_argument('user', type=str, help='name of the user to create and use for csgo server installation')
    return parser.parse_args()

if __name__=='__main__':
    args = parse_args()
    srv = CS_GO_Server(args.user)
    srv.download_server_files()
    srv.update_server_files()