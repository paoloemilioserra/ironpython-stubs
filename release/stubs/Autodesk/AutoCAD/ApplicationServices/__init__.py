# encoding: utf-8
# module Autodesk.AutoCAD.ApplicationServices calls itself ApplicationServices
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null, accoremgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Application(Application):
    # no doc
    @staticmethod
    def AddDefaultContextMenuExtension(menuExtension):
        """ AddDefaultContextMenuExtension(menuExtension: ContextMenuExtension) """
        pass

    @staticmethod
    def AddObjectContextMenuExtension(runtimeClass, menuExtension):
        """ AddObjectContextMenuExtension(runtimeClass: RXClass, menuExtension: ContextMenuExtension) """
        pass

    @staticmethod
    def CommitModalWindow(commitValue):
        """ CommitModalWindow(commitValue: bool) """
        pass

    @staticmethod
    def DoDragDrop(*__args):
        """ DoDragDrop(control: Control, data: object, allowedEffects: DragDropEffects, target: DropTarget)DoDragDrop(dragSource: DependencyObject, data: object, allowedEffects: DragDropEffects, target: DropTarget) """
        pass

    @staticmethod
    def InvokeContextHelp(window, contextId, helpPrefix=None, hlpevent=None):
        """ InvokeContextHelp(window: IntPtr, contextId: int)InvokeContextHelp(window: IntPtr, contextId: int, helpPrefix: str)InvokeContextHelp(window: IntPtr, contextId: int, helpPrefix: str, hlpevent: HelpEventArgs) """
        pass

    @staticmethod
    def InvokeHelp(fileName, topic):
        """ InvokeHelp(fileName: str, topic: str) """
        pass

    @staticmethod
    def InvokeHelpForExternal(functionName):
        """ InvokeHelpForExternal(functionName: str) -> bool """
        pass

    @staticmethod
    def IsConnectEnabled():
        """ IsConnectEnabled() -> bool """
        pass

    @staticmethod
    def LoadMainMenu(filename):
        """ LoadMainMenu(filename: str) -> bool """
        pass

    @staticmethod
    def LoadPartialMenu(filename):
        """ LoadPartialMenu(filename: str) -> bool """
        pass

    @staticmethod
    def PostSearchQuery(searchString):
        """ PostSearchQuery(searchString: str) """
        pass

    def raise_DisplayingCustomizeDialog(self, *args): #cannot find CLR method
        """ raise_DisplayingCustomizeDialog(value0: object, value1: TabbedDialogEventArgs) """
        pass

    def raise_DisplayingDraftingSettingsDialog(self, *args): #cannot find CLR method
        """ raise_DisplayingDraftingSettingsDialog(value0: object, value1: TabbedDialogEventArgs) """
        pass

    def raise_DisplayingOptionDialog(self, *args): #cannot find CLR method
        """ raise_DisplayingOptionDialog(value0: object, value1: TabbedDialogEventArgs) """
        pass

    @staticmethod
    def ReloadAllMenus():
        """ ReloadAllMenus() """
        pass

    @staticmethod
    def RemoveDefaultContextMenuExtension(menuExtension):
        """ RemoveDefaultContextMenuExtension(menuExtension: ContextMenuExtension) """
        pass

    @staticmethod
    def RemoveObjectContextMenuExtension(runtimeClass, menuExtension):
        """ RemoveObjectContextMenuExtension(runtimeClass: RXClass, menuExtension: ContextMenuExtension) """
        pass

    @staticmethod
    def SetCurrentWorkspace(workspacename):
        """ SetCurrentWorkspace(workspacename: str) -> bool """
        pass

    @staticmethod
    def ShowModalDialog(*__args):
        """
        ShowModalDialog(owner: IWin32Window, formToShow: Form) -> DialogResult
        ShowModalDialog(owner: IWin32Window, formToShow: Form, persistSizeAndPosition: bool) -> DialogResult
        ShowModalDialog(formToShow: Form) -> DialogResult
        ShowModalDialog(owner: IntPtr, formToShow: Form) -> DialogResult
        ShowModalDialog(owner: IntPtr, formToShow: Form, persistSizeAndPosition: bool) -> DialogResult
        """
        pass

    @staticmethod
    def ShowModalWindow(*__args):
        """
        ShowModalWindow(owner: IntPtr, htmlPage: Uri, persistSizeAndPosition: bool) -> bool
        ShowModalWindow(owner: IntPtr, htmlPage: Uri) -> bool
        ShowModalWindow(htmlPage: Uri) -> bool
        """
        pass

    @staticmethod
    def ShowModelessDialog(*__args):
        """ ShowModelessDialog(owner: IWin32Window, formToShow: Form)ShowModelessDialog(owner: IWin32Window, formToShow: Form, persistSizeAndPosition: bool)ShowModelessDialog(formToShow: Form)ShowModelessDialog(owner: IntPtr, formToShow: Form)ShowModelessDialog(owner: IntPtr, formToShow: Form, persistSizeAndPosition: bool) """
        pass

    @staticmethod
    def ShowModelessWindow(*__args):
        """ ShowModelessWindow(owner: IntPtr, htmlPage: Uri, persistSizeAndPosition: bool)ShowModelessWindow(owner: IntPtr, htmlPage: Uri)ShowModelessWindow(htmlPage: Uri) """
        pass

    @staticmethod
    def ToSystemDrawingPoint(point):
        """ ToSystemDrawingPoint(point: Point) -> Point """
        pass

    @staticmethod
    def ToSystemDrawingSize(point):
        """ ToSystemDrawingSize(point: Size) -> Size """
        pass

    @staticmethod
    def ToSystemWindowsPoint(point):
        """ ToSystemWindowsPoint(point: Point) -> Point """
        pass

    @staticmethod
    def ToSystemWindowsSize(point):
        """ ToSystemWindowsSize(point: Size) -> Size """
        pass

    @staticmethod
    def UnloadPartialMenu(filename):
        """ UnloadPartialMenu(filename: str) -> bool """
        pass

    AcadApplication = None
    BeginCustomizationMode = None
    DisplayingCustomizeDialog = None
    DisplayingDraftingSettingsDialog = None
    DisplayingOptionDialog = None
    DisplayTextScreen = False
    DocumentWindowCollection = None
    EndCustomizationMode = None
    InfoCenter = None
    IsInCustomizationMode = False
    MenuBar = None
    MenuGroups = None
    NonInPlaceMainWindow = None
    Preferences = None
    StatusBar = None
    UIBindings = None


class BeginCloseAllEventArgs(EventArgs):
    # no doc
    IsVetoed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVetoed(self: BeginCloseAllEventArgs) -> bool

Set: IsVetoed(self: BeginCloseAllEventArgs) = value
"""



class BeginCloseAllEventHandler(MulticastDelegate):
    """ BeginCloseAllEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginCloseAllEventHandler, sender: object, e: BeginCloseAllEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginCloseAllEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginCloseAllEventHandler, sender: object, e: BeginCloseAllEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginDoubleClickEventArgs(EventArgs):
    # no doc
    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: BeginDoubleClickEventArgs) -> Point3d

"""



class BeginDoubleClickEventHandler(MulticastDelegate):
    """ BeginDoubleClickEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginDoubleClickEventHandler, sender: object, e: BeginDoubleClickEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginDoubleClickEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginDoubleClickEventHandler, sender: object, e: BeginDoubleClickEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginQuitEventArgs(EventArgs):
    # no doc
    IsVetoed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVetoed(self: BeginQuitEventArgs) -> bool

Set: IsVetoed(self: BeginQuitEventArgs) = value
"""



class BeginQuitEventHandler(MulticastDelegate):
    """ BeginQuitEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginQuitEventHandler, sender: object, e: BeginQuitEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginQuitEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginQuitEventHandler, sender: object, e: BeginQuitEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class CheckingOutEventArgs(EventArgs):
    """ CheckingOutEventArgs(longTrans: LongTransaction, objCollection: ObjectIdCollection) """
    def Veto(self):
        """ Veto(self: CheckingOutEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, longTrans, objCollection):
        """ __new__(cls: type, longTrans: LongTransaction, objCollection: ObjectIdCollection) """
        pass

    CheckOutSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckOutSet(self: CheckingOutEventArgs) -> ObjectIdCollection

"""

    Transaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transaction(self: CheckingOutEventArgs) -> LongTransaction

"""



class CheckingOutEventHandler(MulticastDelegate):
    """ CheckingOutEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: CheckingOutEventHandler, sender: object, e: CheckingOutEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CheckingOutEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: CheckingOutEventHandler, sender: object, e: CheckingOutEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class CommandEventArgs(EventArgs):
    """ CommandEventArgs() """
    GlobalCommandName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalCommandName(self: CommandEventArgs) -> str

"""



class CommandEventHandler(MulticastDelegate):
    """ CommandEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: CommandEventHandler, sender: object, e: CommandEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CommandEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: CommandEventHandler, sender: object, e: CommandEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ConfigurationSectionNameAttribute(Attribute):
    """ ConfigurationSectionNameAttribute(name: str) """
    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ConfigurationSectionNameAttribute) -> str

"""



class DatabaseExtension(object):
    # no doc
    @staticmethod
    def Audit(db, bFixErrors, bCmdLnEcho):
        """ Audit(db: Database, bFixErrors: bool, bCmdLnEcho: bool) """
        pass

    __all__ = [
        'Audit',
    ]


class Document(DisposableWrapper):
    # no doc
    @staticmethod
    def Create(unmanagedPointer):
        """ Create(unmanagedPointer: IntPtr) -> Document """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def DowngradeDocOpen(self, bPromptForSave):
        """ DowngradeDocOpen(self: Document, bPromptForSave: bool) """
        pass

    def GetLispSymbol(self, name):
        """ GetLispSymbol(self: Document, name: str) -> object """
        pass

    def LockDocument(self, lockMode=None, globalCommandName=None, localCommandName=None, promptIfFails=None):
        """
        LockDocument(self: Document, lockMode: DocumentLockMode, globalCommandName: str, localCommandName: str, promptIfFails: bool) -> DocumentLock
        LockDocument(self: Document) -> DocumentLock
        """
        pass

    def LockMode(self, bIncludeMyLocks=None):
        """
        LockMode(self: Document) -> DocumentLockMode
        LockMode(self: Document, bIncludeMyLocks: bool) -> DocumentLockMode
        """
        pass

    def PopDbmod(self):
        """ PopDbmod(self: Document) """
        pass

    def PushDbmod(self):
        """ PushDbmod(self: Document) """
        pass

    def SendStringToExecute(self, command, activate, wrapUpInactiveDoc, echoCommand):
        """ SendStringToExecute(self: Document, command: str, activate: bool, wrapUpInactiveDoc: bool, echoCommand: bool) """
        pass

    def SetLispSymbol(self, name, value):
        """ SetLispSymbol(self: Document, name: str, value: object) """
        pass

    def TryGetDatabase(self):
        """ TryGetDatabase(self: Document) -> Database """
        pass

    def UpgradeDocOpen(self):
        """ UpgradeDocOpen(self: Document) """
        pass

    CommandInProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandInProgress(self: Document) -> str

"""

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: Document) -> Database

"""

    Editor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Editor(self: Document) -> Editor

"""

    FormatForSave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormatForSave(self: Document) -> DocumentSaveFormat

"""

    GraphicsManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsManager(self: Document) -> Manager

"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: Document) -> bool

"""

    IsNamedDrawing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNamedDrawing(self: Document) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: Document) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Document) -> str

"""

    TransactionManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransactionManager(self: Document) -> TransactionManager

"""

    UserData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserData(self: Document) -> Hashtable

"""

    Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Window(self: Document) -> Window

"""


    BeginDocumentClose = None
    BeginDwgOpen = None
    CloseAborted = None
    CloseWillStart = None
    CommandCancelled = None
    CommandEnded = None
    CommandFailed = None
    CommandWillStart = None
    EndDwgOpen = None
    ImpliedSelectionChanged = None
    LayoutSwitched = None
    LayoutSwitching = None
    LispCancelled = None
    LispEnded = None
    LispWillStart = None
    ModelessOperationEnded = None
    ModelessOperationWillStart = None
    UnknownCommand = None
    ViewChanged = None


class DocumentActivationChangedEventArgs(EventArgs):
    # no doc
    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewValue(self: DocumentActivationChangedEventArgs) -> bool

"""



class DocumentActivationChangedEventHandler(MulticastDelegate):
    """ DocumentActivationChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentActivationChangedEventHandler, sender: object, e: DocumentActivationChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentActivationChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentActivationChangedEventHandler, sender: object, e: DocumentActivationChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentBeginCloseEventArgs(EventArgs):
    """ DocumentBeginCloseEventArgs() """
    def Veto(self):
        """ Veto(self: DocumentBeginCloseEventArgs) """
        pass


class DocumentBeginCloseEventHandler(MulticastDelegate):
    """ DocumentBeginCloseEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentBeginCloseEventHandler, sender: object, e: DocumentBeginCloseEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentBeginCloseEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentBeginCloseEventHandler, sender: object, e: DocumentBeginCloseEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentClosedEventArgs(EventArgs):
    # no doc
    RecentDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecentDocument(self: DocumentClosedEventArgs) -> RecentDocument

"""



class DocumentClosedEventHandler(MulticastDelegate):
    """ DocumentClosedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentClosedEventHandler, sender: object, e: DocumentClosedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentClosedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentClosedEventHandler, sender: object, e: DocumentClosedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentCollection(MarshalByRefObject):
    # no doc
    def AppContextNewDocument(self, templateFileName):
        """ AppContextNewDocument(self: DocumentCollection, templateFileName: str) """
        pass

    def AppContextOpenDocument(self, fileName):
        """ AppContextOpenDocument(self: DocumentCollection, fileName: str) """
        pass

    def AppContextRecoverDocument(self, fileName):
        """ AppContextRecoverDocument(self: DocumentCollection, fileName: str) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: DocumentCollection, array: Array[Document], index: int) """
        pass

    def ExecuteInApplicationContext(self, callback, data):
        """ ExecuteInApplicationContext(self: DocumentCollection, callback: ExecuteInApplicationContextCallback, data: object) """
        pass

    def ExecuteInCommandContextAsync(self, callback, data):
        """ ExecuteInCommandContextAsync(self: DocumentCollection, callback: Func[object, Task], data: object) -> ExecutionResult """
        pass

    def GetDocument(self, db):
        """ GetDocument(self: DocumentCollection, db: Database) -> Document """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DocumentCollection) -> IEnumerator """
        pass

    def GetPendingDocumentForSwitch(self):
        """ GetPendingDocumentForSwitch(self: DocumentCollection) -> Tuple[bool, Document] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DocumentCollection) -> int

"""

    CurrentDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDocument(self: DocumentCollection) -> Document

Set: CurrentDocument(self: DocumentCollection) = value
"""

    DefaultFormatForSave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultFormatForSave(self: DocumentCollection) -> DocumentSaveFormat

Set: DefaultFormatForSave(self: DocumentCollection) = value
"""

    DocumentActivationEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentActivationEnabled(self: DocumentCollection) -> bool

Set: DocumentActivationEnabled(self: DocumentCollection) = value
"""

    IsApplicationContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsApplicationContext(self: DocumentCollection) -> bool

"""

    MdiActiveDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MdiActiveDocument(self: DocumentCollection) -> Document

Set: MdiActiveDocument(self: DocumentCollection) = value
"""


    DocumentActivated = None
    DocumentActivationChanged = None
    DocumentBecameCurrent = None
    DocumentCreated = None
    DocumentCreateStarted = None
    DocumentCreationCanceled = None
    DocumentDestroyed = None
    DocumentLockModeChanged = None
    DocumentLockModeChangeVetoed = None
    DocumentLockModeWillChange = None
    DocumentToBeActivated = None
    DocumentToBeDeactivated = None
    DocumentToBeDestroyed = None
    ExecutionResult = None


class DocumentCollectionEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DocumentCollectionEventArgs) -> Document

"""



class DocumentCollectionEventHandler(MulticastDelegate):
    """ DocumentCollectionEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentCollectionEventHandler, sender: object, e: DocumentCollectionEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentCollectionEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentCollectionEventHandler, sender: object, e: DocumentCollectionEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentCollectionExtension(object):
    # no doc
    @staticmethod
    def Add(docCol, templateFileName):
        """ Add(docCol: DocumentCollection, templateFileName: str) -> Document """
        pass

    @staticmethod
    def CloseAll(docCol):
        """ CloseAll(docCol: DocumentCollection) """
        pass

    @staticmethod
    def Open(docCol, fileName, forReadOnly=None, password=None):
        """
        Open(docCol: DocumentCollection, fileName: str, forReadOnly: bool, password: str) -> Document
        Open(docCol: DocumentCollection, fileName: str) -> Document
        Open(docCol: DocumentCollection, fileName: str, forReadOnly: bool) -> Document
        """
        pass

    __all__ = [
        'Add',
        'CloseAll',
        'Open',
    ]


class DocumentDestroyedEventArgs(EventArgs):
    # no doc
    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: DocumentDestroyedEventArgs) -> str

"""



class DocumentDestroyedEventHandler(MulticastDelegate):
    """ DocumentDestroyedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentDestroyedEventHandler, sender: object, e: DocumentDestroyedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentDestroyedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentDestroyedEventHandler, sender: object, e: DocumentDestroyedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentExtension(object):
    # no doc
    @staticmethod
    def CapturePreviewImage(doc, width, height):
        """ CapturePreviewImage(doc: Document, width: UInt32, height: UInt32) -> Bitmap """
        pass

    @staticmethod
    def CloseAndDiscard(doc):
        """ CloseAndDiscard(doc: Document) """
        pass

    @staticmethod
    def CloseAndSave(doc, fileName):
        """ CloseAndSave(doc: Document, fileName: str) """
        pass

    @staticmethod
    def FromAcadDocument(acadDocument):
        """ FromAcadDocument(acadDocument: object) -> Document """
        pass

    @staticmethod
    def GetAcadDocument(doc):
        """ GetAcadDocument(doc: Document) -> object """
        pass

    @staticmethod
    def GetStatusBar(doc):
        """ GetStatusBar(doc: Document) -> StatusBar """
        pass

    __all__ = [
        'CapturePreviewImage',
        'CloseAndDiscard',
        'CloseAndSave',
        'FromAcadDocument',
        'GetAcadDocument',
        'GetStatusBar',
    ]


class DocumentLock(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: DocumentLock) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class DocumentLockMode(Enum):
    """ enum DocumentLockMode, values: AutoWrite (1), ExclusiveWrite (64), None (0), NotLocked (2), ProtectedAutoWrite (20), Read (32), Write (4) """
    AutoWrite = None
    ExclusiveWrite = None
    None = None
    NotLocked = None
    ProtectedAutoWrite = None
    Read = None
    value__ = None
    Write = None


class DocumentLockModeChangedEventArgs(EventArgs):
    # no doc
    def Veto(self):
        """ Veto(self: DocumentLockModeChangedEventArgs) """
        pass

    CurrentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentMode(self: DocumentLockModeChangedEventArgs) -> DocumentLockMode

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DocumentLockModeChangedEventArgs) -> Document

"""

    GlobalCommandName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalCommandName(self: DocumentLockModeChangedEventArgs) -> str

"""

    MyCurrentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MyCurrentMode(self: DocumentLockModeChangedEventArgs) -> DocumentLockMode

"""

    MyPreviousMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MyPreviousMode(self: DocumentLockModeChangedEventArgs) -> DocumentLockMode

"""



class DocumentLockModeChangedEventHandler(MulticastDelegate):
    """ DocumentLockModeChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentLockModeChangedEventHandler, sender: object, e: DocumentLockModeChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentLockModeChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentLockModeChangedEventHandler, sender: object, e: DocumentLockModeChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentLockModeChangeVetoedEventArgs(EventArgs):
    # no doc
    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DocumentLockModeChangeVetoedEventArgs) -> Document

"""

    GlobalCommandName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalCommandName(self: DocumentLockModeChangeVetoedEventArgs) -> str

"""



class DocumentLockModeChangeVetoedEventHandler(MulticastDelegate):
    """ DocumentLockModeChangeVetoedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentLockModeChangeVetoedEventHandler, sender: object, e: DocumentLockModeChangeVetoedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentLockModeChangeVetoedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentLockModeChangeVetoedEventHandler, sender: object, e: DocumentLockModeChangeVetoedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentLockModeWillChangeEventArgs(EventArgs):
    # no doc
    CurrentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentMode(self: DocumentLockModeWillChangeEventArgs) -> DocumentLockMode

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DocumentLockModeWillChangeEventArgs) -> Document

"""

    GlobalCommandName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalCommandName(self: DocumentLockModeWillChangeEventArgs) -> str

"""

    MyCurrentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MyCurrentMode(self: DocumentLockModeWillChangeEventArgs) -> DocumentLockMode

"""

    MyNewMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MyNewMode(self: DocumentLockModeWillChangeEventArgs) -> DocumentLockMode

"""



class DocumentLockModeWillChangeEventHandler(MulticastDelegate):
    """ DocumentLockModeWillChangeEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentLockModeWillChangeEventHandler, sender: object, e: DocumentLockModeWillChangeEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentLockModeWillChangeEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentLockModeWillChangeEventHandler, sender: object, e: DocumentLockModeWillChangeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentPinStateChangedEventArgs(EventArgs):
    # no doc
    RecentDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecentDocument(self: DocumentPinStateChangedEventArgs) -> RecentDocument

"""



class DocumentPinStateChangedEventHandler(MulticastDelegate):
    """ DocumentPinStateChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentPinStateChangedEventHandler, sender: object, e: DocumentPinStateChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentPinStateChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentPinStateChangedEventHandler, sender: object, e: DocumentPinStateChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentSaveFormat(Enum):
    """ enum DocumentSaveFormat, values: Native (64), R12Dxf (1), R13Dwg (4), R13Dxf (5), R14Dwg (8), R14Dxf (9), R2000Dwg (12), R2000Dxf (13), R2000Standard (15), R2000Template (14), R2000Xml (16), R2004Dwg (24), R2004Dxf (25), R2004Standard (27), R2004Template (26), R2007Dwg (36), R2007Dxf (37), R2007Standard (39), R2007Template (38), R2010Dwg (48), R2010Dxf (49), R2010Standard (51), R2010Template (50), R2013Dwg (60), R2013Dxf (61), R2013Standard (63), R2013Template (62), R2018Dwg (64), R2018Dxf (65), R2018Standard (67), R2018Template (66), Unknown (-1) """
    Native = None
    R12Dxf = None
    R13Dwg = None
    R13Dxf = None
    R14Dwg = None
    R14Dxf = None
    R2000Dwg = None
    R2000Dxf = None
    R2000Standard = None
    R2000Template = None
    R2000Xml = None
    R2004Dwg = None
    R2004Dxf = None
    R2004Standard = None
    R2004Template = None
    R2007Dwg = None
    R2007Dxf = None
    R2007Standard = None
    R2007Template = None
    R2010Dwg = None
    R2010Dxf = None
    R2010Standard = None
    R2010Template = None
    R2013Dwg = None
    R2013Dxf = None
    R2013Standard = None
    R2013Template = None
    R2018Dwg = None
    R2018Dxf = None
    R2018Standard = None
    R2018Template = None
    Unknown = None
    value__ = None


class DocumentWindowActivatedEventArgs(EventArgs):
    # no doc
    DocumentWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentWindow(self: DocumentWindowActivatedEventArgs) -> DocumentWindow

"""



class DocumentWindowActivatedEventHandler(MulticastDelegate):
    """ DocumentWindowActivatedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentWindowActivatedEventHandler, sender: object, e: DocumentWindowActivatedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentWindowActivatedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentWindowActivatedEventHandler, sender: object, e: DocumentWindowActivatedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentWindowCollection(object):
    """ DocumentWindowCollection() """
    def AddDocumentWindow(self, *__args):
        """
        AddDocumentWindow(self: DocumentWindowCollection, documentWindow: DocumentWindow) -> bool
        AddDocumentWindow(self: DocumentWindowCollection, title: str, htmlPage: Uri) -> DocumentWindow
        """
        pass

    def ArrangeIcons(self):
        """ ArrangeIcons(self: DocumentWindowCollection) """
        pass

    def Cascade(self):
        """ Cascade(self: DocumentWindowCollection) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: DocumentWindowCollection, array: Array, index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DocumentWindowCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DocumentWindowCollection) -> IEnumerator """
        pass

    def LookupDocumentWindow(self, docWindow):
        """ LookupDocumentWindow(self: DocumentWindowCollection, docWindow: AcApDocWindow*) -> DocumentWindow """
        pass

    def MoveDocumentWindow(self, documentWindow, newIndex):
        """ MoveDocumentWindow(self: DocumentWindowCollection, documentWindow: DocumentWindow, newIndex: int) -> bool """
        pass

    def raise_CollectionChanged(self, *args): #cannot find CLR method
        """ raise_CollectionChanged(self: DocumentWindowCollection, value0: object, value1: NotifyCollectionChangedEventArgs) """
        pass

    def TileHorizontally(self):
        """ TileHorizontally(self: DocumentWindowCollection) """
        pass

    def TileVertically(self):
        """ TileVertically(self: DocumentWindowCollection) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    ActiveDocumentWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveDocumentWindow(self: DocumentWindowCollection) -> DocumentWindow

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DocumentWindowCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: DocumentWindowCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: DocumentWindowCollection) -> object

"""


    CollectionChanged = None
    DocumentWindowActivated = None


class DrawingOpenEventArgs(EventArgs):
    # no doc
    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: DrawingOpenEventArgs) -> Database

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: DrawingOpenEventArgs) -> str

"""



class DrawingOpenEventHandler(MulticastDelegate):
    """ DrawingOpenEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DrawingOpenEventHandler, sender: object, e: DrawingOpenEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DrawingOpenEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DrawingOpenEventHandler, sender: object, e: DrawingOpenEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ExecuteInApplicationContextCallback(MulticastDelegate):
    """ ExecuteInApplicationContextCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, userData, callback, obj):
        """ BeginInvoke(self: ExecuteInApplicationContextCallback, userData: object, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ExecuteInApplicationContextCallback, result: IAsyncResult) """
        pass

    def Invoke(self, userData):
        """ Invoke(self: ExecuteInApplicationContextCallback, userData: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class IConfigurationSection(IDisposable):
    # no doc
    def Close(self):
        """ Close(self: IConfigurationSection) """
        pass

    def Contains(self, name):
        """ Contains(self: IConfigurationSection, name: str) -> bool """
        pass

    def ContainsSubsection(self, name):
        """ ContainsSubsection(self: IConfigurationSection, name: str) -> bool """
        pass

    def CreateSubsection(self, name):
        """ CreateSubsection(self: IConfigurationSection, name: str) -> IConfigurationSection """
        pass

    def Delete(self, name):
        """ Delete(self: IConfigurationSection, name: str) """
        pass

    def DeleteSubsection(self, name):
        """ DeleteSubsection(self: IConfigurationSection, name: str) """
        pass

    def OpenSubsection(self, name):
        """ OpenSubsection(self: IConfigurationSection, name: str) -> IConfigurationSection """
        pass

    def ReadProperty(self, name, defaultValue):
        """ ReadProperty(self: IConfigurationSection, name: str, defaultValue: object) -> object """
        pass

    def WriteProperty(self, name, value):
        """ WriteProperty(self: IConfigurationSection, name: str, value: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: IConfigurationSection) -> bool

"""



class InplaceTextEditor(TextEditor):
    # no doc
    def AddUndoMarker(self, undoType):
        """ AddUndoMarker(self: InplaceTextEditor, undoType: TextUndoType) """
        pass

    def AttachmentMenus(self, pos, parent):
        """ AttachmentMenus(self: InplaceTextEditor, pos: Point, parent: Window) """
        pass

    def ColumnMenus(self, pos, parent):
        """ ColumnMenus(self: InplaceTextEditor, pos: Point, parent: Window) """
        pass

    def ColumnsDialog(self, staticColumnCount):
        """ ColumnsDialog(self: InplaceTextEditor, staticColumnCount: int) """
        pass

    def ContextMenus(self, pos, parent):
        """ ContextMenus(self: InplaceTextEditor, pos: Point, parent: Window) """
        pass

    def Copy(self):
        """ Copy(self: InplaceTextEditor) """
        pass

    def Cut(self):
        """ Cut(self: InplaceTextEditor) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def DrawHightlight(self):
        """ DrawHightlight(self: InplaceTextEditor) """
        pass

    def FieldDialog(self, field):
        """ FieldDialog(self: InplaceTextEditor, field: Field) """
        pass

    def FindAndReplaceDialog(self):
        """ FindAndReplaceDialog(self: InplaceTextEditor) """
        pass

    def FindMatchItem(self, flags, findStr):
        """ FindMatchItem(self: InplaceTextEditor, flags: int, findStr: str) """
        pass

    def HelpDialog(self):
        """ HelpDialog(self: InplaceTextEditor) """
        pass

    def HightlightColorDialog(self):
        """ HightlightColorDialog(self: InplaceTextEditor) """
        pass

    def ImportTextDialog(self):
        """ ImportTextDialog(self: InplaceTextEditor) """
        pass

    def InsertFile(self, filename):
        """ InsertFile(self: InplaceTextEditor, filename: str) """
        pass

    @staticmethod
    def Invoke(*__args):
        """ Invoke(mtext: MText, settings: InplaceTextEditorSettings)Invoke(text: DBText) -> Array[ObjectId] """
        pass

    def LineSpaceMenus(self, pos, parent):
        """ LineSpaceMenus(self: InplaceTextEditor, pos: Point, parent: Window) """
        pass

    def NewFeatureWorkShop(self):
        """ NewFeatureWorkShop(self: InplaceTextEditor) """
        pass

    def NumberingMenus(self, pos, parent):
        """ NumberingMenus(self: InplaceTextEditor, pos: Point, parent: Window) """
        pass

    def OtherSymbol(self):
        """ OtherSymbol(self: InplaceTextEditor) """
        pass

    def ParagraphDialog(self):
        """ ParagraphDialog(self: InplaceTextEditor) """
        pass

    def Paste(self):
        """ Paste(self: InplaceTextEditor) """
        pass

    def PasteWithoutFormats(self):
        """ PasteWithoutFormats(self: InplaceTextEditor) """
        pass

    def Redo(self):
        """ Redo(self: InplaceTextEditor) """
        pass

    def RemoveHightlight(self):
        """ RemoveHightlight(self: InplaceTextEditor) """
        pass

    def ReplaceAllMatches(self, flags, findStr, replaceStr):
        """ ReplaceAllMatches(self: InplaceTextEditor, flags: int, findStr: str, replaceStr: str) """
        pass

    def ReplaceCurrentMatch(self, flags, findStr, replaceStr):
        """ ReplaceCurrentMatch(self: InplaceTextEditor, flags: int, findStr: str, replaceStr: str) """
        pass

    def SetStaticColumnsWithCount(self, columnCount):
        """ SetStaticColumnsWithCount(self: InplaceTextEditor, columnCount: int) """
        pass

    def SpellDictionaryDialog(self):
        """ SpellDictionaryDialog(self: InplaceTextEditor) """
        pass

    def SpellSettingDialog(self):
        """ SpellSettingDialog(self: InplaceTextEditor) """
        pass

    def StackPropertyDialog(self):
        """ StackPropertyDialog(self: InplaceTextEditor) """
        pass

    def SymbolMenus(self, pos, parent):
        """ SymbolMenus(self: InplaceTextEditor, pos: Point, parent: Window) """
        pass

    def Undo(self):
        """ Undo(self: InplaceTextEditor) """
        pass

    def WipeoutDialog(self):
        """ WipeoutDialog(self: InplaceTextEditor) """
        pass

    alginment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: alginment(self: InplaceTextEditor) -> AlignmentType

"""

    Annotative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Annotative(self: InplaceTextEditor) -> bool

Set: Annotative(self: InplaceTextEditor) = value
"""

    CanCopy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanCopy(self: InplaceTextEditor) -> bool

"""

    CanCut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanCut(self: InplaceTextEditor) -> bool

"""

    CanExitEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanExitEditor(self: InplaceTextEditor) -> bool

Set: CanExitEditor(self: InplaceTextEditor) = value
"""

    CanPaste = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanPaste(self: InplaceTextEditor) -> bool

"""

    CanRedo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRedo(self: InplaceTextEditor) -> bool

"""

    CanUndo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanUndo(self: InplaceTextEditor) -> bool

"""

    ForcedOpaqueBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForcedOpaqueBackground(self: InplaceTextEditor) -> bool

"""

    LayerColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerColor(self: InplaceTextEditor) -> Color

"""

    MultiAttribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiAttribute(self: InplaceTextEditor) -> bool

"""

    OpaqueBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpaqueBackground(self: InplaceTextEditor) -> bool

Set: OpaqueBackground(self: InplaceTextEditor) = value
"""

    ParagraphSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParagraphSupported(self: InplaceTextEditor) -> bool

"""

    RulerHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RulerHidden(self: InplaceTextEditor) -> bool

Set: RulerHidden(self: InplaceTextEditor) = value
"""

    RulerSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RulerSupported(self: InplaceTextEditor) -> bool

"""

    SimpleMText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimpleMText(self: InplaceTextEditor) -> bool

"""

    SpellerEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpellerEnabled(self: InplaceTextEditor) -> bool

Set: SpellerEnabled(self: InplaceTextEditor) = value
"""

    TableCell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableCell(self: InplaceTextEditor) -> bool

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: InplaceTextEditor) -> bool

"""

    ToolbarHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolbarHidden(self: InplaceTextEditor) -> bool

Set: ToolbarHidden(self: InplaceTextEditor) = value
"""

    ToolbarOptionHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolbarOptionHidden(self: InplaceTextEditor) -> bool

Set: ToolbarOptionHidden(self: InplaceTextEditor) = value
"""

    UndoRecordingDisabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UndoRecordingDisabled(self: InplaceTextEditor) -> bool

Set: UndoRecordingDisabled(self: InplaceTextEditor) = value
"""

    Wysiwyg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wysiwyg(self: InplaceTextEditor) -> bool

Set: Wysiwyg(self: InplaceTextEditor) = value
"""


    Current = None
    TextUndoType = None


class InplaceTextEditorSettings(DisposableWrapper):
    """ InplaceTextEditorSettings() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    DefinedHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefinedHeight(self: InplaceTextEditorSettings) -> float

Set: DefinedHeight(self: InplaceTextEditorSettings) = value
"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: InplaceTextEditorSettings) -> EditFlags

Set: Flags(self: InplaceTextEditorSettings) = value
"""

    SimpleMText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimpleMText(self: InplaceTextEditorSettings) -> bool

Set: SimpleMText(self: InplaceTextEditorSettings) = value
"""

    TabSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TabSupported(self: InplaceTextEditorSettings) -> bool

Set: TabSupported(self: InplaceTextEditorSettings) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: InplaceTextEditorSettings) -> EntityType

Set: Type(self: InplaceTextEditorSettings) = value
"""


    EditFlags = None
    EntityType = None


class LayoutSwitchedEventArgs(EventArgs):
    # no doc
    NewLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewLayout(self: LayoutSwitchedEventArgs) -> str

"""



class LayoutSwitchedEventHandler(MulticastDelegate):
    """ LayoutSwitchedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: LayoutSwitchedEventHandler, sender: object, e: LayoutSwitchedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayoutSwitchedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: LayoutSwitchedEventHandler, sender: object, e: LayoutSwitchedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class LayoutSwitchingEventArgs(EventArgs):
    # no doc
    NewLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewLayout(self: LayoutSwitchingEventArgs) -> str

"""

    OldLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldLayout(self: LayoutSwitchingEventArgs) -> str

"""



class LayoutSwitchingEventHandler(MulticastDelegate):
    """ LayoutSwitchingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: LayoutSwitchingEventHandler, sender: object, e: LayoutSwitchingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayoutSwitchingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: LayoutSwitchingEventHandler, sender: object, e: LayoutSwitchingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class LispWillStartEventArgs(EventArgs):
    # no doc
    FirstLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstLine(self: LispWillStartEventArgs) -> str

"""



class LispWillStartEventHandler(MulticastDelegate):
    """ LispWillStartEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: LispWillStartEventHandler, sender: object, e: LispWillStartEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LispWillStartEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: LispWillStartEventHandler, sender: object, e: LispWillStartEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class LongTransactionEventArgs(EventArgs):
    """ LongTransactionEventArgs(longTrans: LongTransaction) """
    @staticmethod # known case of __new__
    def __new__(self, longTrans):
        """ __new__(cls: type, longTrans: LongTransaction) """
        pass

    Transaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transaction(self: LongTransactionEventArgs) -> LongTransaction

"""



class LongTransactionEventHandler(MulticastDelegate):
    """ LongTransactionEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: LongTransactionEventHandler, sender: object, e: LongTransactionEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LongTransactionEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: LongTransactionEventHandler, sender: object, e: LongTransactionEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class LongTransactionManager(RXObject):
    # no doc
    def AbortLongTransaction(self, transId, keepObjs):
        """ AbortLongTransaction(self: LongTransactionManager, transId: ObjectId, keepObjs: bool) """
        pass

    def AddClassFilter(self, filter):
        """ AddClassFilter(self: LongTransactionManager, filter: RXClass) """
        pass

    def CheckIn(self, transId, errorMap, keepObjs):
        """ CheckIn(self: LongTransactionManager, transId: ObjectId, errorMap: IdMapping, keepObjs: bool) """
        pass

    def CheckOut(self, checkoutSet, toBlock, errorMap, blkRef):
        """ CheckOut(self: LongTransactionManager, checkoutSet: ObjectIdCollection, toBlock: ObjectId, errorMap: IdMapping, blkRef: ObjectId) -> ObjectId """
        pass

    def CurrentLongTransactionFor(self, doc):
        """ CurrentLongTransactionFor(self: LongTransactionManager, doc: Document) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IsFiltered(self, A_0):
        """ IsFiltered(self: LongTransactionManager, A_0: RXClass) -> bool """
        pass

    Aborted = None
    CheckedIn = None
    CheckedOut = None
    CheckingIn = None
    CheckingOut = None


class Marshaler(object):
    # no doc
    @staticmethod
    def AdsNameToSelectionSet(pointerToAdsName):
        """ AdsNameToSelectionSet(pointerToAdsName: IntPtr) -> SelectionSet """
        pass

    @staticmethod
    def SelectionSetToAdsName(selectionSet, pointerToAdsName):
        """ SelectionSetToAdsName(selectionSet: SelectionSet, pointerToAdsName: IntPtr) """
        pass

    __all__ = [
        'AdsNameToSelectionSet',
        'SelectionSetToAdsName',
    ]


class ModelessOperationEventArgs(EventArgs):
    # no doc
    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Context(self: ModelessOperationEventArgs) -> str

"""



class ModelessOperationEventHandler(MulticastDelegate):
    """ ModelessOperationEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ModelessOperationEventHandler, sender: object, e: ModelessOperationEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModelessOperationEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModelessOperationEventHandler, sender: object, e: ModelessOperationEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PreTranslateMessageEventArgs(EventArgs):
    # no doc
    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handled(self: PreTranslateMessageEventArgs) -> bool

Set: Handled(self: PreTranslateMessageEventArgs) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: PreTranslateMessageEventArgs) -> MSG

Set: Message(self: PreTranslateMessageEventArgs) = value
"""



class PreTranslateMessageEventHandler(MulticastDelegate):
    """ PreTranslateMessageEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PreTranslateMessageEventHandler, sender: object, e: PreTranslateMessageEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PreTranslateMessageEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PreTranslateMessageEventHandler, sender: object, e: PreTranslateMessageEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ProfileEventArgs(EventArgs):
    # no doc
    ProfileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileName(self: ProfileEventArgs) -> str

"""



class ProfileEventHandler(MulticastDelegate):
    """ ProfileEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ProfileEventHandler, sender: object, e: ProfileEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ProfileEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ProfileEventHandler, sender: object, e: ProfileEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class RecentDocument(object):
    # no doc
    CurrentlyOpenBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentlyOpenBy(self: RecentDocument) -> str

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: RecentDocument) -> bool

"""

    IsPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPinned(self: RecentDocument) -> bool

Set: IsPinned(self: RecentDocument) = value
"""

    LastOpenedTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastOpenedTime(self: RecentDocument) -> ValueType

"""

    LastSavedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastSavedBy(self: RecentDocument) -> str

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: RecentDocument) -> str

"""

    Preview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preview(self: RecentDocument) -> BitmapSource

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: RecentDocument) -> str

"""



class RecentDocumentCollection(ReadOnlyObservableCollection[RecentDocument]):
    # no doc
    def Dispose(self):
        """ Dispose(self: RecentDocumentCollection) """
        pass

    @staticmethod
    def Remove(path):
        """ Remove(path: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    UsePinnedItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsePinnedItems(self: RecentDocumentCollection) -> bool

Set: UsePinnedItems(self: RecentDocumentCollection) = value
"""


    DocumentClosed = None
    DocumentPinStateChanged = None
    Instance = None


class SystemVariableChangedEventArgs(EventArgs):
    # no doc
    Changed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Changed(self: SystemVariableChangedEventArgs) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SystemVariableChangedEventArgs) -> str

"""



class SystemVariableChangedEventHandler(MulticastDelegate):
    """ SystemVariableChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: SystemVariableChangedEventHandler, sender: object, e: SystemVariableChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SystemVariableChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SystemVariableChangedEventHandler, sender: object, e: SystemVariableChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SystemVariableChangingEventArgs(EventArgs):
    # no doc
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SystemVariableChangingEventArgs) -> str

"""



class SystemVariableChangingEventHandler(MulticastDelegate):
    """ SystemVariableChangingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: SystemVariableChangingEventHandler, sender: object, e: SystemVariableChangingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SystemVariableChangingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SystemVariableChangingEventHandler, sender: object, e: SystemVariableChangingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class TabbedDialogAction(MulticastDelegate):
    """ TabbedDialogAction(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: TabbedDialogAction, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TabbedDialogAction, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: TabbedDialogAction) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class TabbedDialogEventArgs(EventArgs):
    # no doc
    def AddTab(self, name, extension):
        """ AddTab(self: TabbedDialogEventArgs, name: str, extension: TabbedDialogExtension) """
        pass


class TabbedDialogEventHandler(MulticastDelegate):
    """ TabbedDialogEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: TabbedDialogEventHandler, sender: object, e: TabbedDialogEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TabbedDialogEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: TabbedDialogEventHandler, sender: object, e: TabbedDialogEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class TabbedDialogExtension(object):
    """
    TabbedDialogExtension(control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction, onApply: TabbedDialogAction)
    TabbedDialogExtension(control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction)
    TabbedDialogExtension(control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction)
    TabbedDialogExtension(control: object, onOK: TabbedDialogAction)
    TabbedDialogExtension(control: Control, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction, onApply: TabbedDialogAction)
    TabbedDialogExtension(control: Control, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction)
    TabbedDialogExtension(control: Control, onOK: TabbedDialogAction, onCancel: TabbedDialogAction)
    TabbedDialogExtension(control: Control, onOK: TabbedDialogAction)
    """
    @staticmethod
    def SetDirty(control, dirty):
        """ SetDirty(control: Control, dirty: bool)SetDirty(control: object, dirty: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, control, onOK, onCancel=None, onHelp=None, onApply=None):
        """
        __new__(cls: type, control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction, onApply: TabbedDialogAction)
        __new__(cls: type, control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction)
        __new__(cls: type, control: object, onOK: TabbedDialogAction, onCancel: TabbedDialogAction)
        __new__(cls: type, control: object, onOK: TabbedDialogAction)
        __new__(cls: type, control: Control, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction, onApply: TabbedDialogAction)
        __new__(cls: type, control: Control, onOK: TabbedDialogAction, onCancel: TabbedDialogAction, onHelp: TabbedDialogAction)
        __new__(cls: type, control: Control, onOK: TabbedDialogAction, onCancel: TabbedDialogAction)
        __new__(cls: type, control: Control, onOK: TabbedDialogAction)
        """
        pass

    Control = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Control(self: TabbedDialogExtension) -> object

"""

    OnApply = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnApply(self: TabbedDialogExtension) -> TabbedDialogAction

"""

    OnCancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnCancel(self: TabbedDialogExtension) -> TabbedDialogAction

"""

    OnHelp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnHelp(self: TabbedDialogExtension) -> TabbedDialogAction

"""

    OnOk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnOk(self: TabbedDialogExtension) -> TabbedDialogAction

"""



class TransactionManager(TransactionManager):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EnableGraphicsFlush(self, doEnable):
        """ EnableGraphicsFlush(self: TransactionManager, doEnable: bool) """
        pass

    def FlushGraphics(self):
        """ FlushGraphics(self: TransactionManager) """
        pass

    def StartTransaction(self):
        """ StartTransaction(self: TransactionManager) -> Transaction """
        pass

    TopTransaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopTransaction(self: TransactionManager) -> Transaction

"""



class UnknownCommandEventArgs(EventArgs):
    # no doc
    GlobalCommandName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalCommandName(self: UnknownCommandEventArgs) -> str

"""



class UnknownCommandEventHandler(MulticastDelegate):
    """ UnknownCommandEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: UnknownCommandEventHandler, sender: object, e: UnknownCommandEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UnknownCommandEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: UnknownCommandEventHandler, sender: object, e: UnknownCommandEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class UserConfigurationManager(MarshalByRefObject):
    # no doc
    def OpenCurrentProfile(self):
        """ OpenCurrentProfile(self: UserConfigurationManager) -> IConfigurationSection """
        pass

    def OpenDialogSection(self, dialog):
        """ OpenDialogSection(self: UserConfigurationManager, dialog: object) -> IConfigurationSection """
        pass

    def OpenGlobalSection(self):
        """ OpenGlobalSection(self: UserConfigurationManager) -> IConfigurationSection """
        pass

    def SetCurrentProfile(self, profileName):
        """ SetCurrentProfile(self: UserConfigurationManager, profileName: str) """
        pass

    CurrentProfileChanged = None
    CurrentProfileChanging = None
    CurrentProfileReset = None
    CurrentProfileResetting = None
    CurrentProfileSaved = None
    CurrentProfileSaving = None
    ProfileReset = None
    ProfileResetting = None
    ProfileSaved = None
    ProfileSaving = None


class WhoHasInfo(object):
    # no doc
    ComputerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComputerName(self: WhoHasInfo) -> str

"""

    IsFileLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFileLocked(self: WhoHasInfo) -> bool

"""

    OpenTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpenTime(self: WhoHasInfo) -> str

"""

    UserName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserName(self: WhoHasInfo) -> str

"""



class XrefFileLock(DisposableWrapper):
    # no doc
    @staticmethod
    def ConsistencyCheck(selectedBlockId=None):
        """ ConsistencyCheck(self: XrefFileLock)ConsistencyCheck(selectedBlockId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def ConsistencyCheckLocal(selectedBlockId):
        """ ConsistencyCheckLocal(selectedBlockId: ObjectId) -> ObjectIdCollection """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetXloadCtlType(selectedBlockId):
        """ GetXloadCtlType(selectedBlockId: ObjectId) -> int """
        pass

    @staticmethod
    def LockFile(selectedBlockId):
        """ LockFile(selectedBlockId: ObjectId) -> XrefFileLock """
        pass

    def ReleaseFile(self, skipSaveback=None, reload=None):
        """ ReleaseFile(self: XrefFileLock, skipSaveback: bool, reload: bool)ReleaseFile(self: XrefFileLock) """
        pass

    @staticmethod
    def ReloadFile(*__args):
        """ ReloadFile(self: XrefFileLock)ReloadFile(self: XrefFileLock, xldCtlType: int)ReloadFile(blocks: ObjectIdCollection)ReloadFile(blocks: ObjectIdCollection, xldCtlType: int) """
        pass

    OutOfSyncBlockIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutOfSyncBlockIds(self: XrefFileLock) -> ObjectIdCollection

"""

    XloadCtlType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XloadCtlType(self: XrefFileLock) -> int

"""



# variables with complex values

