### Phone List GUI
***
This small python app allows you to view, add, update, and delete contacts and their associated phone numbers.


![Screenshot](https://github.com/adabat64/Portfolio/blob/master/Python/img/Phone_Listscreenshot.png)

##### Instructions
Pre-reqs: Python 3+, Mac only, tkinter

* Download folder and cd into it
* Start Python 3
* Type exec(open("tkPhone.py").read())

Two fake contacts are pre-loaded.
* To add a contact: type in the name and number, then press add.
* To update a contact: click on a contact, click load, change information, click the contact again, then click update.
* To delete a contact: select a contact and press delete.

To save and load a save:
* Press save
* Open tkPhone.py in an editor, and scroll to the bottom.
* Comment out

  phonelist = [
  ['Doe, John', '343-4349'],
  ['Smith, Robert', '689-1234'],
  ]

* Uncomment

  phonelist = tksave.load()

* Save, and start program.
