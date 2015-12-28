#!/usr/bin/python3

'''
This script os for backing up a profile, encrypting the backup and then sending that
backup to Google Drive, or other cloud storage providers that might be available later

example:
./backup.py backup /home/$USERNAME
./backup.py restore /home/$USERNAME

'''
from sys import argv as argv
import os
import tarfile

#constants, there's no constants in Python... so just don't change these
DEBUG = True

def checkPath(path):
    #This will check if a path exsists
    debugMessage(path)
    debugMessage(os.path.exists(path))
    return os.path.exists(path)

def debugMessage(message):
    #This is for printing debug messages for troubleshooting issues
    if DEBUG == True:
        print('DEBUG: ', message)


def startTar(path):
    #This will start the tar process for the given path
    debugMessage('startTar, ' + path)
    try:
        tar = tarfile.open("backup.tar", "w")
        tar.add(path)
        tar.close()
    except Exception as ex:
        print('Error: ',ex)



def main():
    #Print this message if no arguments have been passed
    if len(argv) <= 1:
        debugMessage('Args less than or equal to 1')
        print('Please provide the location of what you would like to backup.')
        print('You can also just provide the username of the /home profile you want to backup')
        return
    debugMessage(argv)
    usernameProvided = False
    pathProvided = False
    profilePath = ""
    #Check the passed argument for a / meaning they are passing a path
    if any("/" in s for s in argv[1]):
        pathProvided = True
    else:
        usernameProvided = True

    #Check if the path exsists
    if pathProvided == True:
        profileExists = checkPath(argv[1])
        profilePath = argv[1]
    else:
        debugMessage(argv[1])
        profileExists = checkPath("/home/" + argv[1])
        profilePath = "/home/" + argv[1]

    if profileExists == True:
        debugMessage('Profile exsists')
        startTar(profilePath)
    else:
        debugMessage('profileExists is')
        debugMessage(profileExists)




#Keep this at bottom
if __name__ == "__main__":
    main()
