import Tools.tools as tool
tool.T.conf()
#Socket connection
tool.T.sck()
#Panel
tool.T.dashboard()
#Choice condition
if (tool.T.choice == "1"): #terminal
    tool.T.terminal()
    
elif (tool.T.choice == "2"):
    tool.T.filemanager() #filemanager
    
else :
    tool.T.logout()

