class SaveFileDialog(FileDialog,IComponent,IDisposable):
 """
 Prompts the user to select a location for saving a file. This class cannot be inherited.
 
 SaveFileDialog()
 """
 def Dispose(self):
  """
  Dispose(self: Component,disposing: bool)
   Releases the unmanaged resources used by the System.ComponentModel.Component and optionally 
    releases the managed resources.
  
  
   disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
  """
  pass
 def GetService(self,*args):
  """
  GetService(self: Component,service: Type) -> object
  
   Returns an object that represents a service provided by the System.ComponentModel.Component or 
    by its System.ComponentModel.Container.
  
  
   service: A service provided by the System.ComponentModel.Component.
   Returns: An System.Object that represents a service provided by the System.ComponentModel.Component,or 
    null if the System.ComponentModel.Component does not provide the specified service.
  """
  pass
 def HookProc(self,*args):
  """
  HookProc(self: FileDialog,hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> IntPtr
  
   Defines the common dialog box hook procedure that is overridden to add specific functionality to 
    the file dialog box.
  
  
   hWnd: The handle to the dialog box window.
   msg: The message received by the dialog box.
   wparam: Additional information about the message.
   lparam: Additional information about the message.
   Returns: Returns zero if the default dialog box procedure processes the message; returns a nonzero value 
    if the default dialog box procedure ignores the message.
  """
  pass
 def MemberwiseClone(self,*args):
  """
  MemberwiseClone(self: MarshalByRefObject,cloneIdentity: bool) -> MarshalByRefObject
  
   Creates a shallow copy of the current System.MarshalByRefObject object.
  
   cloneIdentity: false to delete the current System.MarshalByRefObject object's identity,which will cause the 
    object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
    false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
    identity to its clone,which will cause remoting client calls to be routed to the remote server 
    object.
  
   Returns: A shallow copy of the current System.MarshalByRefObject object.
  MemberwiseClone(self: object) -> object
  
   Creates a shallow copy of the current System.Object.
   Returns: A shallow copy of the current System.Object.
  """
  pass
 def OnFileOk(self,*args):
  """
  OnFileOk(self: FileDialog,e: CancelEventArgs)
   Raises the System.Windows.Forms.FileDialog.FileOk event.
  
   e: A System.ComponentModel.CancelEventArgs that contains the event data.
  """
  pass
 def OnHelpRequest(self,*args):
  """
  OnHelpRequest(self: CommonDialog,e: EventArgs)
   Raises the System.Windows.Forms.CommonDialog.HelpRequest event.
  
   e: An System.Windows.Forms.HelpEventArgs that provides the event data.
  """
  pass
 def OpenFile(self):
  """
  OpenFile(self: SaveFileDialog) -> Stream
  
   Opens the file with read/write permission selected by the user.
   Returns: The read/write file selected by the user.
  """
  pass
 def OwnerWndProc(self,*args):
  """
  OwnerWndProc(self: CommonDialog,hWnd: IntPtr,msg: int,wparam: IntPtr,lparam: IntPtr) -> IntPtr
  
   Defines the owner window procedure that is overridden to add specific functionality to a common 
    dialog box.
  
  
   hWnd: The window handle of the message to send.
   msg: The Win32 message to send.
   wparam: The wparam to send with the message.
   lparam: The lparam to send with the message.
   Returns: The result of the message processing,which is dependent on the message sent.
  """
  pass
 def Reset(self):
  """
  Reset(self: SaveFileDialog)
   Resets all dialog box options to their default values.
  """
  pass
 def RunDialog(self,*args):
  """
  RunDialog(self: FileDialog,hWndOwner: IntPtr) -> bool
  
   Specifies a common dialog box.
  
   hWndOwner: A value that represents the window handle of the owner window for the common dialog box.
   Returns: true if the file could be opened; otherwise,false.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object
  
   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)
   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __str__(self,*args):
  pass
 CanRaiseEvents=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the component can raise an event.

"""

 CreatePrompt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the dialog box prompts the user for permission to create a file if the user specifies a file that does not exist.

Get: CreatePrompt(self: SaveFileDialog) -> bool

Set: CreatePrompt(self: SaveFileDialog)=value
"""

 DesignMode=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that indicates whether the System.ComponentModel.Component is currently in design mode.

"""

 Events=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the list of event handlers that are attached to this System.ComponentModel.Component.

"""

 Instance=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the Win32 instance handle for the application.

"""

 Options=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets values to initialize the System.Windows.Forms.FileDialog.

"""

 OverwritePrompt=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value indicating whether the Save As dialog box displays a warning if the user specifies a file name that already exists.

Get: OverwritePrompt(self: SaveFileDialog) -> bool

Set: OverwritePrompt(self: SaveFileDialog)=value
"""

