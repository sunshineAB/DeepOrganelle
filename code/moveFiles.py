#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 21:36:04 2018

@author: laser
"""

import os
import shutil

from os import listdir
from os.path import isfile, join
from sklearn.utils import shuffle

path = "G:/CompleteDataset"


def main():
    # chlo_enlarged

    sourceFolderPath = path + "/train/chlo_enlarged"
    destinationFolderPath = path + "/val/chlo_enlarged"
    destinationFolderPath1 = path + "/test/chlo_enlarged"
    numOfFiles = 30

    # chlo_normal
    '''
    sourceFolderPath = path+"/train/chlo_normal"
    destinationFolderPath = path+"/val/chlo_normal"
    destinationFolderPath1 = path+"/test/chlo_normal"
    numOfFiles = 30
    '''

    # mito_elongated
    '''
    sourceFolderPath = path+"/train/mito_elongated"
    destinationFolderPath = path+"/val/mito_elongated"
    destinationFolderPath1 = path+"/test/mito_elongated"
    numOfFiles = 30
    '''

    # mito_normal
    '''
    sourceFolderPath = path+"/train/mito_normal"
    destinationFolderPath = path+"/val/mito_normal"
    destinationFolderPath1 = path+"/test/mito_normal"
    numOfFiles = 30
    '''

    # pex_elongated
    '''
    sourceFolderPath = path+"/train/pex_elongated"
    destinationFolderPath = path+"/val/pex_elongated"
    destinationFolderPath1 = path+"/test/pex_elongated"
    numOfFiles = 30
    '''

    # pex_normal
    '''
    sourceFolderPath = path+"/train/pex_normal"
    destinationFolderPath = path+"/val/pex_normal"
    destinationFolderPath1 = path+"/test/pex_normal"
    numOfFiles = 30
    '''

    moveSomeFilesFromFolderToFolder(sourceFolderPath, destinationFolderPath, numOfFiles)
    moveSomeFilesFromFolderToFolder(sourceFolderPath, destinationFolderPath1, numOfFiles)

    # createFolder(sourceFolderPath)
    # createFolder(destinationFolderPath)
    # creat100FilesInFolder(newFileSourceFolderPath)

    """
    files = os.listdir(sourceFolderPath)
    for file in files:
        print("file name: ", file)
    """


def createFolder(folderPath):
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)
        print(folderPath, " is just created.")
    print("folderPath exist? ", os.path.exists(folderPath))


def creat100FilesInFolder(folderPath):
    for i in range(20):
        fileName = str(i) + ".txt"
        # print(fileName)
        fileStream = open(folderPath + "/" + fileName, "w")
        fileStream.close()


def moveSomeFilesFromFolderToFolder(sourceFolder, destinationFolder, numOfFiles):
    # First, get the file list of the sourceFolder.
    onlyfiles = [file for file in listdir(sourceFolder) if isfile(join(sourceFolder, file))]
    # onlyfiles.sort()
    onlyfiles = shuffle(onlyfiles)
    # Second, iterate the list and set limit on the number of file to move.
    i = 0
    for file in onlyfiles:
        if i >= numOfFiles:
            break

        i += 1
        src = join(sourceFolder, file)
        dst = join(destinationFolder, file)
        shutil.move(src, dst)


def testing():
    b = 10


# The following section is a must. Something like a.out arg1 arg2, to specify
# which program to run.

if __name__ == "__main__":
    main()

elif __name__ == "__testing__":
    testing()