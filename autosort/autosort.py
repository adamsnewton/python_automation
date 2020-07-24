from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time
import sys

#TODO: Add more destinations and file extensions to handle
#TODO: Log the sorting?
#TODO: Create a configuration file?

start = time.time()
currentTime = time.strftime("%Y%m%d-%H%M%S")

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            file, file_extension = os.path.splitext(filename)
            src = folder_to_track + "/" + filename
            if(file_extension in installers):
                folder_destination = r"C:\Users\adamn\Documents\installers"
            elif(file_extension in images):
                folder_destination = r"C:\Users\adamn\Pictures"
            elif(file_extension in pyfiles):
                folder_destination = r"C:\Users\adamn\Documents\scripting\python"
            elif(file_extension in cfiles):
                folder_destination = r"C:\Users\adamn\Documents\scripting\c"
            elif(file_extension in pdfs):
                folder_destination = r"C:\Users\adamn\Documents\pdfs"
            else:
                folder_destination = r"C:\Users\adamn\Documents"
            index = ""
            while True:
                new_destination = folder_destination + "/" + file + index + file_extension
                try:
                    print("Moving " + src + " to " + new_destination, file=logFile)
                    os.rename(src, new_destination)
                    break
                except Exception as e:
                    if index:
                        index = "(" + str(int(index[1:-1])+1)+")"
                    else:
                        index = "(1)"
                    pass

folder_to_track = r"C:\Users\adamn\Downloads"
installers = [".exe", ".msi"]
images = [".jpg", ".jpeg", ".png"]
cfiles = [".c", ".h"]
pyfiles = [".py", ".pyw"]
pdfs = [".pdf"]

logFile = open("autosort_" + currentTime + "log.log", "a")

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

logFile.close()

end = time.time()
runtime = end-start
print(f"Total run time: {runtime:.3f} seconds")
