import wx, BDdb, sys

class Frame(wx.Frame):

    def __init__(self, title):
        wx.Frame.__init__(self, None, title = title, size = (1300,700))
        self.panel = wx.Panel(self) #initiating menu bar in panel

        ## MENU ##
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        exitItem = fileMenu.Append(wx.NewId(), "Exit")
        menuBar.Append(fileMenu, "File")

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.exitProgram, exitItem)
        self.CreateStatusBar()

        ### --ADDING BD-- ###

        wx.StaticBox(self.panel, label='Add New BD', pos=(20, 40), size=(280,150))

        wx.StaticText(self.panel, label='Title', pos=(30, 70))
        wx.StaticText(self.panel, label='Author', pos=(30, 110))
        wx.StaticText(self.panel, label='Publisher', pos=(30, 150))

        self.add_title = wx.TextCtrl(self.panel, size=(150, -1), pos=(130, 70))
        self.add_author = wx.TextCtrl(self.panel, size=(150, -1), pos=(130, 110))
        self.add_publisher = wx.TextCtrl(self.panel, size=(150, -1), pos=(130, 150))

        self.save = wx.Button(self.panel, label='Add BD', pos=(100,190))
        self.save.Bind(wx.EVT_BUTTON, self.newBD)

        ### --LISTING BD-- ###
        self.BD_listCtrl = wx.ListCtrl(self.panel, size=(400,400), pos=(350,40), style=wx.LC_REPORT |wx.BORDER_SUNKEN)
        self.BD_listCtrl.InsertColumn(1, "Title")
        self.BD_listCtrl.InsertColumn(2, "Authors")
        self.BD_listCtrl.InsertColumn(3, "Publisher")

        # Add data to the list of BD
        self.fill_BD_ListCtrl()

        ### --ISSUES-- ###

        wx.StaticBox(self.panel, label='Add New Issue', pos=(20, 240), size=(280,150))

        wx.StaticText(self.panel, label='BD Title', pos=(30, 270))
        wx.StaticText(self.panel, label='BD Number', pos=(30, 310))
        wx.StaticText(self.panel, label='Issue Title', pos=(30, 350))

        self.add_BD_title = wx.TextCtrl(self.panel, size=(150, -1), pos=(130, 270))
        self.add_issue_number = wx.TextCtrl(self.panel, size=(150, -1), pos=(130, 310))
        self.add_issue_title = wx.TextCtrl(self.panel, size=(150, -1), pos=(130, 350))

        self.save_issue = wx.Button(self.panel, label='Add Issue', pos=(100,390))
        self.save_issue.Bind(wx.EVT_BUTTON, self.newIssue)

        self.Issue_listCtrl = wx.ListCtrl(self.panel, size=(400,400), pos=(800,40), style=wx.LC_REPORT |wx.BORDER_SUNKEN)
        self.Issue_listCtrl.InsertColumn(1, "BD Title")
        self.Issue_listCtrl.InsertColumn(2, "Issue Number")
        self.Issue_listCtrl.InsertColumn(3, "Issue Title")

        # Add data to the list control
        # self.fill_Issue_listCtrl()

        # Run onSelect function when item is selected
        self.BD_listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect) #onSelect for updating information
        self.Issue_listCtrl.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onSelect_Issue)

#
#         # Setup a delete button
#         deleteBtn = wx.Button(self.panel, label="Delete", pos=(640, 450))
#         # Bind delete button to onDelete function
#         deleteBtn.Bind(wx.EVT_BUTTON, self.onDelete)
#         wx.StaticBox(self.panel, label='Update BD', pos=(20,340), size=(280,190))

#
#
#         # Setup a delete button
        self.delete_BD = wx.Button(self.panel, label="Delete BD", pos=(640, 450))
#         # Bind delete button to onDelete function
        self.delete_BD.Bind(wx.EVT_BUTTON, self.onDelete_BD)

        self.delete_Issue = wx.Button(self.panel, label="Delete Issue", pos=(1040, 450))
#         # Bind delete button to onDelete function
        self.delete_Issue.Bind(wx.EVT_BUTTON, self.onDelete_Issues)
#         # wx.StaticBox(self.panel, label='Update BD', pos=(20,340), size=(280,190))
#
#         #Update
#         # Text for name, gender etc
#         wx.StaticText(self.panel, label='ID:', pos=(30,370))
#         wx.StaticText(self.panel, label='Title:', pos=(30,410))
#         wx.StaticText(self.panel, label='Authors:', pos=(30,450))
#         wx.StaticText(self.panel, label='Publisher:', pos=(30,490))
#
#         # Single line text boxes
#         self.bdBD_ID_Updt = wx.SpinCtrl(self.panel, value = '0', pos= (130,370), size=(70,25))
#         self.bdTitle_Updt = wx.TextCtrl(self.panel, size=(150, -1), pos=(130,410))
#         self.bdAuthor_Updt = wx.TextCtrl(self.panel, size=(150, -1), pos=(130,450))
#         self.bdPublisher_Updt = wx.TextCtrl(self.panel, size=(150, -1), pos=(130,490))
#
#         # Up_date Save button
#         save_Updt = wx.Button(self.panel, label="Update BD", pos=(100, 530))
#         save_Updt.Bind(wx.EVT_BUTTON, self.updateBD)


###############################################################################
    def exitProgram(self, event):
        sys.exit()

###############################################################################
    def newBD(self, event):

        self.title = self.add_title.GetValue()
        self.author = self.add_author.GetValue()
        self.publisher = self.add_publisher.GetValue()


        #Checking for blank input
        if (self.title == '') or (self.author == '') or (self.publisher == ''):
            #Dialogue Box for user input
            dlg = wx.MessageDialog(None, 'Details missing', wx.OK)
            dlg.ShowModal()
            dlg.Destroy()

        BDdb.newBD(self.title, self.author, self.publisher)

        # Clearing entries when done
        self.add_title.Clear()
        self.add_author.Clear()
        self.add_publisher.Clear()

        # Refresh list of BD
        self.fill_BD_ListCtrl()

###############################################################################

    def fill_BD_ListCtrl(self):
        # Get data from the database
        self.allData = BDdb.viewAll_BD()

        # Delete old data before adding new data
        self.BD_listCtrl.DeleteAllItems()

        # Append data to the table
        for row in self.allData:
            # Loop though and append data
            self.BD_listCtrl.Append(row)

###############################################################################

    def newIssue(self, event):

        self.issue_bd_title = self.add_BD_title.GetValue()
        self.issue_num = self.add_issue_number.GetValue()
        self.issue_title = self.add_issue_title.GetValue()

        #Checking for blank input
        # if (self.title == '') or (self.author == '') or (self.publisher == ''):
        #     #Dialogue Box for user input
        #     dlg = wx.MessageDialog(None, 'Details missing', wx.OK)
        #     dlg.ShowModal()
        #     dlg.Destroy()

        BDdb.newIssue(self.issue_bd_title, self.issue_num, self.issue_title)

        # Clearing entries when done
        self.add_BD_title.Clear()
        self.add_issue_number.Clear()
        self.add_issue_title.Clear()

        # Refresh list of BD
        self.fill_Issue_listCtrl(self.issue_bd_title)

###############################################################################

    def fill_Issue_listCtrl(self, title):
        # Get data from the database
        self.all_IssueData = BDdb.viewAll_Issues(title)

        #Deleting all data before adding more database
        self.Issue_listCtrl.DeleteAllItems()

        for row in self.all_IssueData:
            self.Issue_listCtrl.Append(row)



###############################################################################

    def onSelect(self, event):

        index = event.GetIndex()
        BD_info = self.allData[index]
        title = BD_info[0]
        titles = str(title)

        self.selected_title = titles

        self.fill_Issue_listCtrl(titles)

###############################################################################

    def onSelect_Issue(self, event):

        index = event.GetIndex()
        issue_info = self.all_IssueData[index]
        title = issue_info[0]
        titles = str(title)
        self.bdTitle = titles
        self.issue_num = issue_info[1]

    def onDelete_BD(self, event):
        BDdb.deleteBD(self.selected_title)
        self.fill_BD_ListCtrl()
        self.fill_Issue_listCtrl(self.selected_title)

    def onDelete_Issues(self, event):
        BDdb.deleteIssue(self.bdTitle, self.issue_num)
        self.fill_Issue_listCtrl(self.bdTitle)

#         self.selectedId = event.GetText()        # Get index of selected row
#         index = event.GetIndex()
#
#         # Get BDinfo info

#         print (BD_Info)
#
#         # Set value of update text boxes
#         self.bdBD_ID_Updt.SetValue(BD_Info[0])
#         self.bdTitle_Updt.SetValue(BD_Info[1])
#         self.bdAuthor_Updt.SetValue(BD_Info[2])
#         self.bdPublisher_Updt.SetValue(BD_Info[3])
#
#         bd_id = self.selectedID
#         self.fillIssueListCtrl(bdid)
#
#     def onDelete(self, event):
#         BDdb.deleteBD(self.selectedId)
#         self.fillListCtrl()
#
#     def updateBD(self, event):
#          # Get the updated values
#          bd_id = self.bdBD_ID_Updt.GetValue()
#          title = self.bdTitle_Updt.GetValue()
#          author = self.bdAuthor_Updt.GetValue()
#          publisher = self.bdPublisher_Updt.GetValue()
#
#          # Get character ID
#          bdID = self.selectedId
#
#          # Update the character
#          BDdb.updateBD(bdID, title, author, publisher)
#
#          # Refresh list control
#          self.fillListCtrl()
#
app = wx.App(True)
frame = Frame("BD Tracker")
frame.Show()
app.MainLoop()
