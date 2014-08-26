'''
Created on Aug 26, 2014

@author: samu
'''

import argparse
import logging

args = None



def parse_args():
    parser = argparse.ArgumentParser(description='Installs a CSS Server from the scratch using the given user and paths.')
    parser.add_argument('user_name', type=str, help='Name of the user starting the css server')
    parser.add_argument('-n', metavar='slotcount', type=int, help='Number of slots', default=12)
    parser.add_argument('-p', action='store_true', type=int, help='Enables password protection')
    args = parser.parse_args()
    
def create_user(user_name):
    print('GE')

if __name__ == '__main__':
    pass