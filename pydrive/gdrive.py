import time
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

##############################################
# Functions
##############################################

def ListAllFiles():
    print("\nListing files in your Google Drive...\n------------------------------------")
    fileList = drive.ListFile({'q': 'trashed=false'}).GetList()
    for file in fileList:
        print(file['title'], file['id'])
        if(file == fileList[-1]):
            print("") # THIS IS ONLY REQUIRED IF PRINTING TO THE CONSOLE

def CreateAndUpload():
    fileName = input("\nWhat should the file name be?\n")
    fileExtension = input("\nWhat should the file extension be?\n")
    file = drive.CreateFile({'title': + fileName + '.' + fileExtension})
    file.SetContentString('Hello World!') # this writes a string directly to a file
    file.Upload()
    print("")

def FindFiles():
    subString = input("\nWhat string should the filename contain?\n")
    fileList = drive.ListFile({'q': "title contains '" + subString + "' and trashed=false"}).GetList()
    for file in fileList:
        if(file == fileList[0]):
            print("")
        print(file['title'])
    print("")

def UploadExistingFile():
    filePath = input("\nList the name of the file to be uploaded:\n")
    fileToUpload = drive.CreateFile()
    fileToUpload.SetContentFile(filePath) # load local file data into the File instance
    fileToUpload.Upload()
    print("")

def UploadExistingFolder():
    folderPath = input("\nList the path to the folder to be uploaded:\n")
    folderToUpload = drive.CreateFile({'title': folderPath, "mimeType": "application/vnd.google-apps.folder"})
    folderToUpload.Upload()

def UploadExistingFileToFolder():
    filePath = input("\nList the name of the file to be uploaded:\n")
    folderPath = input("List the path to the folder to be uploaded:\n")
    parentFolder = drive.ListFile({'q': 'title=' + folderPath + " and trashed=false"}).GetList()[0]
    file = drive.CreateFile({'title': filePath, 'parents': [{'id': parentFolder['id']}]})
    file.Upload()

# THIS FUNCTION IS INCOMPLETE
def DownloadFile():
    fileName = input("\nWhat file do you want to download?\n")
    if(file['title'] == fileName):
        fileId = file['id'] # get the file ID
        fileToDownload = drive.CreateFile({'id': fileId})
        fileToDownload.GetContentFile(fileName)

##############################################
# Main
##############################################
start = time.time()

gauth = GoogleAuth()
gauth.LoadCredentialsFile("..\..\credentials\mycreds.txt")
drive = GoogleDrive(gauth)

while True:
    filename = ""
    command = input('What would you like to do?\n'
    '1) List all files\n'
    '2) Create and upload a file\n'
    '3) Find files with names containing a specific string\n'
    '4) Upload an existing file\n'
    '5) Upload an existing folder\n'
    '6) Upload an existing file to a folder\n'
    '7) Quit\n')

    if (command == "1"):
        ListAllFiles()
    elif (command == "2"):
        CreateAndUpload()
    elif (command == "3"):
        FindFiles()
    elif (command == "4"):
        UploadExistingFile()
    elif (command == "5"):
        UploadExistingFolder()
    elif (command == "6"):
        UploadExistingFileToFolder()
    elif (command == "7"):
        print("Quitting script...\n")
        break
    else:
        print("Invalid value entered. Try again.\n")

end = time.time()
runtime = end-start
print(f"Total run time: {runtime:.3f} seconds")
