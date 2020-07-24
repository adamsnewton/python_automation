import time
from github import Github

##############################################
# Functions
##############################################

def ListRepos():
  repo=g.search_repositories(query="language:python")
  for repo in g.get_user().get_repos():
    print(repo.name)

def CreateRepo():
  repoName = input("Enter a name for your new repository:\n")
  user = g.get_user()
  newRepo = user.create_repo(repoName)

def UploadFileToRepo():
  print("function currently undefined")
  #repoName = "test"
  #repoName.create_file("new_file.txt", "init commit", "file_content ------ ")

def UploadFolderToExistingRepo():
  print("function currently undefined")

##############################################
# Main
##############################################
start = time.time()

credFile = open("..\..\credentials\credentials.txt")
credentials = credFile.readline().rstrip('\n')
credFile.close()
g=Github(credentials)

while True:
    command = input('What would you like to do?\n'
    '1) List repos\n'
    '2) Create a new repo\n'
    '3) Upload a file to a repo\n'
    '4) Upload folder contents to an existing repo\n'
    '5) Quit\n')

    if (command == "1"):
        ListRepos()
    elif (command == "2"):
        CreateRepo()
    elif (command == "3"):
        UploadFileToRepo()
    elif (command == "4"):
        UploadFolderToExistingRepo()
    elif (command == "5"):
        print("Quitting script...\n")
        break
    else:
        print("Invalid value entered. Try again.\n")

end = time.time()
runtime = end-start
print(f"Total run time: {runtime:.3f} seconds")
