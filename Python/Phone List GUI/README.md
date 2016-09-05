### Phone List GUI
***
This small python app allows you to view, add, update, and delete contacts and their associated phone numbers.

![alt text]("https://github.com/adabat64/Portfolio/Python/Phone List GUI/Screenshot.png")

##### Instructions
Pre-reqs: Python 3+

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
  ```python
  #phonelist = [
  #['Doe, John', '343-4349'],
  #['Smith, Robert', '689-1234'],
  #]
 ```
* Uncomment
  ```python
  phonelist = tksave.load()
  ```
* Save, and start program.
