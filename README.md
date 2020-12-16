# pyImportMusic
Imports music from a specified source folder and creates target diretories in the specified target folder based on ID3 album name and copies the files to it.
Supported extension in the script: mp3, ogg, opus, flac, wma, m4a.
Tested with Python 3.8.6

## Required python modules:

* tinytag
* shutil

## Usage:

python3 pyMusicImport.py [inputFolder] [outputFolder]

## Parameters:

* inputFolder:    
  * Folder which contains the music files
* outputFolder:        
  * Folder where the directories should be created and the files should be then copied
                
## Exmaple:

python3 pyMusicImport.py ~/input/ ~/output/
