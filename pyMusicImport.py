import os
import sys
from tinytag import TinyTag
from shutil import copy2

fromDir = ''
toDir = ''
musicList = []
albumErrorList = []

def getAlbumName(file):
    tag = TinyTag.get(file)
    if tag.album is not None:
        return tag.album
    else:
        return ""

def getMusicFiles(thisPath):
    for subdir, dirs, files in os.walk(thisPath):
        for file in files:
            if (file.endswith('.mp3') or 
                file.endswith('.ogg') or 
                file.endswith('.opus') or 
                file.endswith('.flac') or 
                file.endswith('.wma') or 
                file.endswith('.m4a')):
                musicList.append(subdir + '/' + file)   

def printProgressBar(actualCount, totalCount):
    totalLength = 100
    singleStepPercent = 100 / totalLength
    actualPercent = (1 / (int(totalCount) / int(actualCount))) * 100

    print('[', end='')

    for element in range(totalLength):
        if actualPercent > (element * singleStepPercent):
            print('#', end='')
        else:
            print(' ', end='')
        

    print('] ', end='')
    print('%.2f'%actualPercent + '% ' + '(Element %i '%actualCount + 'of %i)'%totalCount, end='\r')                

def importMusic():

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: musicImport.py [InputDir] [OutputDir]')
        exit(-1)    

    fromDir = sys.argv[1]
    toDir = sys.argv[2]
    
    if os.path.isdir(fromDir) == False:
        print('Input Dir (Param 1) doesn\'t exist / isn\'t a dir, please check params!!!')
        exit(-2)   

    if os.path.isdir(toDir) == False:
        os.makedirs(toDir)

    getMusicFiles(fromDir)    
    items = int(len(musicList))
    counter = 0
    skippedCounter = 0
    copiedCounter = 0

    for file in musicList:
        
        albumName = getAlbumName(file)
        if len(albumName) > 0:
            
            if toDir.endswith('/'):
                targetPath = toDir + albumName            
            else:
                targetPath = toDir + '/' + albumName         

            if os.path.isdir(targetPath) == False:
                os.makedirs(targetPath)        

            if os.path.isfile(targetPath + '/' + os.path.basename(file)) == False:
                copy2(file, targetPath)
                copiedCounter += 1
            else:
                skippedCounter += 1

        else:
            albumErrorList.append(file)
            skippedCounter += 1

        counter += 1

        printProgressBar(counter, items)

    print('')
    print('Copied: %i files'%copiedCounter + ' | Skipped %i files'%skippedCounter)
        
    if len(albumErrorList) > 0:
        for element in albumErrorList:
            print('Error in album ID3 Tag, this file was skipped: %s'%element)


if __name__ == "__main__":
    importMusic()                
