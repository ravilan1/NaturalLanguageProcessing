from pathlib import Path
from datetime import datetime
import zipfile
#https://docs.python.org/3/library/pathlib.html
#https://docs.python.org/3/library/datetime.html
class FileOperations:

    #Finding file from computer
    @staticmethod
    def _getFiles_(path,filename):
        directory=Path(path)
        for fname in directory.rglob("*"):
            if filename in fname.stem:
                print(fname.absolute())

    #create file
    @staticmethod
    def _createfile_(path,filename):
        directory = Path(path)
        print(directory)
        print(directory.is_dir())
        if directory.is_dir():
            print(directory)
            with open(path+"\\"+filename, 'w') as f:
                f.write("Hello Mylove...")

    #Changing prefix
    @staticmethod
    def _renameFiles_(_path):
        path=Path(_path)
        dire=path.iterdir()
        for file in dire:
            state=file.stat()
            createTime=state.st_ctime
            cttime=datetime.fromtimestamp(createTime)
            tstmp=cttime.strftime("%Y-%m-%dT%H-%M-%S")
            filename=file.stem+"_"+tstmp+file.suffix
            print(filename)
            newfilepath=file.with_name(filename)
            #newfilepath=Path(_path+filename)
            file.rename(newfilepath)

    #Renaming all files in folder
    @staticmethod
    def _renameAllFiles_(path,fileName):
        dirpath=Path(path)
        allFolders=dirpath.glob("*") #* is for inside parent directory if u want to go subdirectory give **/*
        for file in allFolders:
            print(file)
            #parts=file.parts
            #print(parts)
            fName=file.stem+fileName+".txt"
            print(fName)
            newFile=file.with_name(fName)
            file.rename(newFile)
            fName=""

    #Renaming all files in subfolder
    @staticmethod
    def _renameAllFilesInSubfolder_(path,fileName):
        dirpath=Path(path)
        allFolders=dirpath.glob("**/*") #* is for inside parent directory if u want to go subdirectory give **/*
        for file in allFolders:
            if file.is_file():
                print(file)
                #parts=file.parts
                #print(parts)
                fName=file.stem+fileName+".txt"
                print(fName)
                newFile=file.with_name(fName)
                file.rename(newFile)
                fName=""

    #Create zrchieve file
    @staticmethod
    def _createArchieveFile_(path):
        path=Path(path)
        zip= path/Path("allfiles.zip")
        with zipfile.ZipFile(zip, 'w') as myzip:
            for f in path.rglob('*.txt'):
                myzip.write(f)


    #extract files from zip file
    @staticmethod
    def _extractFiles_(path):
        path=Path(path)
        for zip in path.glob('*.zip'):
            with zipfile.ZipFile(zip, 'r') as myzip:
                myzip.extractall(path=path/Path('allzipfiles'))



    


    #_getFiles_("C:\\test","Containers")
    #_createfile_("C:\\test\\","sample.txt")
    #_renameFiles_("C:\\test\\")
    #_createArchieveFile_("C:\\test\\")
    #_extractFiles_("C:\\test\\")
    #_renameAllFilesInSubfolder_("C:\\test\\","_first")
    #_name_("Ravi")






