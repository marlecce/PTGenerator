'''
Created on Aug 1, 2013

@author: mlecce
'''
import wx
import googl
 
class MyApp(wx.Frame):
    def __init__(self):
        # Every wx app must create one App object
        # before it does anything else using wx.
        self.app = wx.App()
 
        # Set up the main window
        wx.Frame.__init__(self,
                          parent=None,
                          title='Publish your tweet!',
                          size=(500, 200))
 
        # The greetings available
        self.greetings = ['hello', 'goodbye', 'heyo']
 
        # Layout panel and hbox
        self.panel = wx.Panel(self, size=(480, 200))
        self.box = wx.BoxSizer(wx.VERTICAL)
 
        #Greeting combobox
        self.greeting = wx.ComboBox(parent=self.panel,
                                  value='hello',
                                  size=(480, -1),
                                  choices=self.greetings)
 
        # Add the greeting combo to the hbox
        self.box.Add(self.greeting, 0, wx.TOP)
        self.box.Add((-1, 10))
 
        # Recipient entry
        self.recipient = wx.TextCtrl(parent=self.panel,
                                     size=(480, -1),
                                     value='')
 
        # Add the greeting combo to the hbox
        self.box.Add(self.recipient, 0, wx.TOP)
 
        # Add padding to lower the button position
        self.box.Add((-1, 100))
 
        # The go button
        self.go_button = wx.Button(self.panel, 10, '&Tweet!')
 
        # Bind an event for the button
        self.Bind(wx.EVT_BUTTON, self.print_result, self.go_button)
 
        # Make the button the default action for the form
        self.go_button.SetDefault()
 
        # Add the button to the hbox
        self.box.Add(self.go_button, 0, flag=wx.ALIGN_RIGHT | wx.BOTTOM)
 
        # Tell the panel to use the hbox
        self.panel.SetSizer(self.box)
 
    def print_result(self, *args):
        ''' Print a greeting constructed from
            the selections made by the user. '''
        print('%s, %s!' % (self.greeting.GetValue().title(),
                           googl.shorten(self.recipient.GetValue())))
 
    def run(self):
        ''' Run the app '''
        self.Show()
        self.app.MainLoop()
 
# Instantiate and run
# app = ExampleApp()
# app.run()
"""
class MyApp(wx.Frame):
    
    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.
        
    def OnExit(self,e):
        self.Close(True)  # Close the frame.
        
    def OnChange(self, e):
        pass
    
    def OnKeyPress(self, e):
        pass    
    
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(400,300))
        #self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # Setting up the menu.
        configmenu= wx.Menu()
        filemenu= wx.Menu()
        
        # config menu 
        configmenu.Append(1, "&General","Set some general configurations")

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuExit = filemenu.Append(wx.ID_EXIT,"&Exit"," Terminate the program")

        # Set events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append(configmenu,"&Configuration") # Adding the "configmenu" to the MenuBar
        menuBar.Append(filemenu,"&Tools") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
        self.Show(True)
        
        #creating text field
        text = wx.TextCtrl(self)
        self.Bind(wx.EVT_TEXT, self.OnChange, text)
        self.Bind(wx.EVT_CHAR, self.OnKeyPress, text)
        
        
        
class MyApp(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        # create some sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        grid = wx.GridBagSizer(hgap=5, vgap=5)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.quote = wx.StaticText(self, label="Your quote: ")
        grid.Add(self.quote, pos=(0,0))

        # A multiline TextCtrl - This is here to show how the events work in this program, don't pay too much attention to it
        self.logger = wx.TextCtrl(self, size=(200,300), style=wx.TE_MULTILINE | wx.TE_READONLY)

        # A button
        self.button =wx.Button(self, label="Save")
        self.Bind(wx.EVT_BUTTON, self.OnClick,self.button)

        # the edit control - one line version.
        self.lblname = wx.StaticText(self, label="Your name :")
        grid.Add(self.lblname, pos=(1,0))
        self.editname = wx.TextCtrl(self, value="Enter here your name", size=(140,-1))
        grid.Add(self.editname, pos=(1,1))
        self.Bind(wx.EVT_TEXT, self.EvtText, self.editname)
        self.Bind(wx.EVT_CHAR, self.EvtChar, self.editname)

        # the combobox Control
        self.sampleList = ['friends', 'advertising', 'web search', 'Yellow Pages']
        self.lblhear = wx.StaticText(self, label="How did you hear from us ?")
        grid.Add(self.lblhear, pos=(3,0))
        self.edithear = wx.ComboBox(self, size=(95, -1), choices=self.sampleList, style=wx.CB_DROPDOWN)
        grid.Add(self.edithear, pos=(3,1))
        self.Bind(wx.EVT_COMBOBOX, self.EvtComboBox, self.edithear)
        self.Bind(wx.EVT_TEXT, self.EvtText,self.edithear)

        # add a spacer to the sizer
        grid.Add((10, 40), pos=(2,0))

        # Checkbox
        self.insure = wx.CheckBox(self, label="Do you want Insured Shipment ?")
        grid.Add(self.insure, pos=(4,0), span=(1,2), flag=wx.BOTTOM, border=5)
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, self.insure)

        # Radio Boxes
        radioList = ['blue', 'red', 'yellow', 'orange', 'green', 'purple', 'navy blue', 'black', 'gray']
        rb = wx.RadioBox(self, label="What color would you like ?", pos=(20, 210), choices=radioList,  majorDimension=3,
                         style=wx.RA_SPECIFY_COLS)
        grid.Add(rb, pos=(5,0), span=(1,2))
        self.Bind(wx.EVT_RADIOBOX, self.EvtRadioBox, rb)

        hSizer.Add(grid, 0, wx.ALL, 5)
        hSizer.Add(self.logger)
        mainSizer.Add(hSizer, 0, wx.ALL, 5)
        mainSizer.Add(self.button, 0, wx.CENTER)
        self.SetSizerAndFit(mainSizer)        
        
    #app = wx.App(False)
    """
