### File Transfer GUI
Python 3+, Mac only, sqlite3, wxPhoenix

This small file transfer program I created checks a source folder for files that were last modified after t-24hrs, and automatically moves them to a destination folder. Unlike the [C# version](#), this one allows you to choose your folder interactively. It also logs the last time you pressed the "Export Files" button in a database and displays it.

![Widget Image](/screenshot.png?raw=true "File Transfer GUI screenshot")

##### Instructions

* Download folder and cd into it
* Start Python 3
* Type exec(open("guiFolderChooser").read())

* Choose source folder
* Choose destination folder
* Press "Export Files" button

* To quit press cmd+Q or force quit Python.
