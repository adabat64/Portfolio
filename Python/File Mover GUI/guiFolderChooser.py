import os
import os.path
import wx
import time
from datetime import datetime
from datetime import timedelta
import shutil
import guiFCdb

########################################################################
class Frame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
                          "Mover GUI")
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.currentDirectory = os.getcwd()

        ### First folder choice
        self.dirDlgBtn = wx.Button(self.panel, label="Choose Folder")
        self.dirDlgBtn.Bind(wx.EVT_BUTTON, self.firstFolder)
        # self.dirDlgBtn.Bind(wx.EVT_BUTTON, self.binding1)
        self.selectedfolder1 = wx.TextCtrl(self.panel,wx.ID_ANY,"Folder Path",size=(490,25))


        ### Second folder choice
        self.dirDlgBtn2 = wx.Button(self.panel, label="Choose Folder")
        self.dirDlgBtn2.Bind(wx.EVT_BUTTON, self.secondFolder)
        # self.dirDlgBtn2.Bind(wx.EVT_BUTTON, self.binding2)

        self.selectedfolder2 = wx.TextCtrl(self.panel,wx.ID_ANY,"Folder Path",size=(490,25))

        ### File chooser implementation
        self.exportBtn = wx.Button(self.panel, label="Export Files")
        self.exportBtn.Bind(wx.EVT_BUTTON, self.export)

        ### UI table
        self.listCtrl = wx.ListCtrl(self.panel, style=wx.LC_REPORT | wx.BORDER_SUNKEN, size=(490,400))
        self.listCtrl.InsertColumn(0, "Last Pressed Time")
        self.fillListCtrl()

        ### Frame organization
        row1 = wx.BoxSizer(wx.VERTICAL)
        row1.Add(self.dirDlgBtn,0,wx.BOTTOM | wx.LEFT,5)
        row1.Add(self.selectedfolder1)
        row1.Add(self.dirDlgBtn2,0,wx.BOTTOM | wx.LEFT,5)
        row1.Add(self.selectedfolder2)
        row1.Add(self.exportBtn,0,wx.BOTTOM | wx.LEFT,5)
        row1.Add(self.listCtrl, 0,wx.BOTTOM | wx.LEFT,5)
        self.panel.SetSizer(row1)

#----------------------------------------------------------------------
    def firstFolder(self, event):

        self.dlg = wx.DirDialog(self, "Choose the first directory",
                           style=wx.DD_DEFAULT_STYLE
                        #    | wx.DD_DIR_MUST_EXIST
                        #    | wx.DD_CHANGE_DIR
                           )
        if self.dlg.ShowModal() == wx.ID_OK:
             self.selectedfolder1.SetValue(self.dlg.GetPath())
             self.folder1 = self.selectedfolder1.GetValue()

        self.dlg.Destroy()

#----------------------------------------------------------------------
    def fillListCtrl(self):
        # Get data from the database
        self.allData = guiFCdb.viewAll()

        # Delete old data before adding new data
        self.listCtrl.DeleteAllItems()

        # Append data to the table
        for row in self.allData:
            # Loop though and append data
            self.listCtrl.Append(row)

    def export(self, event):

        self.src = self.folder1 +'/'
        self.dst = self.folder2 +'/'
        print (self.src)
        print (self.dst)


        self.now = datetime.now()


        self.timecheck = (self.now - timedelta(hours=24)).strftime("%s")
        print(self.timecheck)

        self.str_now = self.now.strftime("%A, %B %d at %H:%M")
        print(self.str_now)
        guiFCdb.newPressTime(self.str_now)
        print (guiFCdb.viewAll())

        for file in os.listdir(self.src):
            self.path = os.path.join(self.src, file)
            self.last_mod = os.stat(self.path).st_mtime
            self.lastmod = "{:.1f}".format(self.last_mod)
            print (self.lastmod)
            if self.lastmod < self.timecheck:
                print ("Version is old.. no movement")

            else:
                print("Verion is newer that the last 24hrs")
                shutil.move(self.path, self.dst)

        self.fillListCtrl()
#----------------------------------------------------------------------
    def secondFolder(self, event):

        self.dlg2 = wx.DirDialog(self, "Choose the second directory",
                            style = wx.DD_DEFAULT_STYLE)

        if self.dlg2.ShowModal() == wx.ID_OK:
             self.selectedfolder2.SetValue(self.dlg2.GetPath())
             self.folder2 = self.selectedfolder2.GetValue()
        self.dlg2.Destroy()


# Run the program
if __name__ == "__main__":
    app = wx.App(True)
    frame = Frame()
    frame.Show()
    app.MainLoop()
