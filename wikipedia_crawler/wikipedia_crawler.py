import wikipedia, time, sys, os

##############################################
# Functions
##############################################
def searchForPage():
    term = input("\nEnter your search term: ")
    print("")
    print(wikipedia.search(term, results=10))
    print("")

def printPageSummary():
    term = input("\nEnter the page name: ")
    print("")
    print(wikipedia.summary(term))
    print("")

def printPageContent():
    term = input("\nEnter the page name: ")
    print("")
    print(wikipedia.page(term).content)
    print("")

##############################################
# Main
##############################################
start = time.time()

while True:
    command = input('What would you like to do?\n'
    '1) Search for a page using a search term\n'
    '2) Print a page summary\n'
    '3) Print a page\'s entire content\n'
    '4) Quit\n')

    if (command == "1"):
        searchForPage()
    elif (command == "2"):
        printPageSummary()
    elif (command == "3"):
        printPageContent()
    elif (command == "4"):
        print("Quitting script...\n")
        break
    else:
        print("Invalid value entered. Try again.\n")

end = time.time()
runtime = end-start
print(f"Total run time: {runtime:.3f} seconds")
