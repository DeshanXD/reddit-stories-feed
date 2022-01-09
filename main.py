import sys
import subprocess
import os
import * from lib

def install_dependancies():
    subprocess.check_call(['apt', 'install', 'git']) # use to to auto commits
    subprocess.check_call([sys.executable, '-m' , 'pip', 'install',  'requests'])
    subprocess.check_call([sys.executable, '-m' , 'pip', 'install',  'discord-webhook']) # Request is dependancy of discord-webhook


def main():
    install_dependancies()
    
if __name__ == "__main__":
    main()
    
