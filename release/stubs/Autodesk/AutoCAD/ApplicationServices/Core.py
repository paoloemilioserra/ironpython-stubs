# encoding: utf-8
# module Autodesk.AutoCAD.ApplicationServices.Core calls itself Core
# from accoremgd, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Application(object):
    # no doc
    def AddModelessWindow(self, *args): #cannot find CLR method
        """ AddModelessWindow(form: WeakReference) """
        pass

    def ConvertToDeviceIndependentCoords(self, *args): #cannot find CLR method
        """ ConvertToDeviceIndependentCoords(pt: POINT) -> Point """
        pass

    def ConvertToPixelCoords(self, *args): #cannot find CLR method
        """ ConvertToPixelCoords(pt: Point) -> POINT """
        pass

    @staticmethod
    def EvaluateDiesel(dieselCmd):
        """ EvaluateDiesel(dieselCmd: str) -> str """
        pass

    def GetSafeOwner(self, *args): #cannot find CLR method
        """ GetSafeOwner(owner: IntPtr) -> IntPtr """
        pass

    @staticmethod
    def GetSystemVariable(name):
        """ GetSystemVariable(name: str) -> object """
        pass

    @staticmethod
    def GetWhoHasInfo(pathname):
        """ GetWhoHasInfo(pathname: str) -> WhoHasInfo """
        pass

    @staticmethod
    def Invoke(args):
        """ Invoke(args: ResultBuffer) -> ResultBuffer """
        pass

    @staticmethod
    def IsFileLocked(pathname):
        """ IsFileLocked(pathname: str) -> bool """
        pass

    @staticmethod
    def LoadJSScript(urlJSFile):
        """ LoadJSScript(urlJSFile: Uri) """
        pass

    @staticmethod
    def Quit():
        """ Quit() """
        pass

    def raise_EnterModal(self, *args): #cannot find CLR method
        """ raise_EnterModal(value0: object, value1: EventArgs) """
        pass

    def raise_Idle(self, *args): #cannot find CLR method
        """ raise_Idle(value0: object, value1: EventArgs) """
        pass

    def raise_LeaveModal(self, *args): #cannot find CLR method
        """ raise_LeaveModal(value0: object, value1: EventArgs) """
        pass

    def SetCreateContextMenuHandler(self, *args): #cannot find CLR method
        """ SetCreateContextMenuHandler(handler: CreateContextMenuHandler) """
        pass

    def SetEnableWinFormHandler(self, *args): #cannot find CLR method
        """ SetEnableWinFormHandler(handler: EnableWinFormHandler) """
        pass

    def SetFilterMessageWinFormsHandler(self, *args): #cannot find CLR method
        """ SetFilterMessageWinFormsHandler(handler: FilterMessageWinFormsHandler) """
        pass

    def SetOnIdleWinFormsHandler(self, *args): #cannot find CLR method
        """ SetOnIdleWinFormsHandler(handler: OnIdleWinFormsHandler) """
        pass

    def SetOnWinFormsLoadedHandler(self, *args): #cannot find CLR method
        """ SetOnWinFormsLoadedHandler(handler: OnWinFormsLoadedHandler) """
        pass

    def SetOnWpfLoadedHandler(self, *args): #cannot find CLR method
        """ SetOnWpfLoadedHandler(handler: OnWpfLoadedHandler) """
        pass

    def SetPreProcessMessageWinFormsHandler(self, *args): #cannot find CLR method
        """ SetPreProcessMessageWinFormsHandler(handler: PreProcessMessageWinFormsHandler) """
        pass

    def SetShowExceptionDialogHandler(self, *args): #cannot find CLR method
        """ SetShowExceptionDialogHandler(handler: ShowExceptionDialogHandler) """
        pass

    @staticmethod
    def SetSystemVariable(name, value):
        """ SetSystemVariable(name: str, value: object) """
        pass

    @staticmethod
    def ShowAlertDialog(message):
        """ ShowAlertDialog(message: str) """
        pass

    @staticmethod
    def ShowModalWindow(*__args):
        """
        ShowModalWindow(owner: Window, formToShow: Window, persistSizeAndPosition: bool) -> Nullable[bool]
        ShowModalWindow(owner: IntPtr, formToShow: Window, persistSizeAndPosition: bool) -> Nullable[bool]
        ShowModalWindow(owner: IntPtr, formToShow: Window) -> Nullable[bool]
        ShowModalWindow(formToShow: Window) -> Nullable[bool]
        ShowModalWindow(owner: Window, formToShow: Window) -> Nullable[bool]
        """
        pass

    @staticmethod
    def ShowModelessWindow(*__args):
        """ ShowModelessWindow(owner: Window, formToShow: Window, persistSizeAndPosition: bool)ShowModelessWindow(owner: IntPtr, formToShow: Window, persistSizeAndPosition: bool)ShowModelessWindow(owner: IntPtr, formToShow: Window)ShowModelessWindow(formToShow: Window)ShowModelessWindow(owner: Window, formToShow: Window) """
        pass

    @staticmethod
    def TryGetSystemVariable(name):
        """ TryGetSystemVariable(name: str) -> object """
        pass

    @staticmethod
    def UpdateScreen():
        """ UpdateScreen() """
        pass

    BeginCloseAll = None
    BeginDoubleClick = None
    BeginQuit = None
    DocumentManager = None
    EnterModal = None
    HasPickFirst = False
    Idle = None
    IsInBackgroundMode = False
    IsInPlaceServer = False
    IsQuiescent = False
    LeaveModal = None
    LongTransactionManager = None
    MainWindow = None
    POINT = None
    PreTranslateMessage = None
    Publisher = None
    QuitAborted = None
    QuitWillStart = None
    RecentDocuments = None
    SystemVariableChanged = None
    SystemVariableChanging = None
    UnmanagedResources = None
    UserConfigurationManager = None
    Version = None


class CreateContextMenuHandler(MulticastDelegate):
    """ CreateContextMenuHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, type, callback, obj):
        """ BeginInvoke(self: CreateContextMenuHandler, type: Type, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CreateContextMenuHandler, result: IAsyncResult) -> AcEdUIContext* """
        pass

    def Invoke(self, type):
        """ Invoke(self: CreateContextMenuHandler, type: Type) -> AcEdUIContext* """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class EnableWinFormHandler(MulticastDelegate):
    """ EnableWinFormHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, o, enable, callback, obj):
        """ BeginInvoke(self: EnableWinFormHandler, o: object, enable: bool, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EnableWinFormHandler, result: IAsyncResult) -> bool """
        pass

    def Invoke(self, o, enable):
        """ Invoke(self: EnableWinFormHandler, o: object, enable: bool) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class FilterMessageWinFormsHandler(MulticastDelegate):
    """ FilterMessageWinFormsHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, msg, callback, obj):
        """ BeginInvoke(self: FilterMessageWinFormsHandler, msg: tagMSG*, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FilterMessageWinFormsHandler, result: IAsyncResult) -> bool """
        pass

    def Invoke(self, msg):
        """ Invoke(self: FilterMessageWinFormsHandler, msg: tagMSG*) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OnIdleWinFormsHandler(MulticastDelegate):
    """ OnIdleWinFormsHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: OnIdleWinFormsHandler, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnIdleWinFormsHandler, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: OnIdleWinFormsHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OnWinFormsLoadedHandler(MulticastDelegate):
    """ OnWinFormsLoadedHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: OnWinFormsLoadedHandler, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnWinFormsLoadedHandler, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: OnWinFormsLoadedHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OnWpfLoadedHandler(MulticastDelegate):
    """ OnWpfLoadedHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: OnWpfLoadedHandler, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnWpfLoadedHandler, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: OnWpfLoadedHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PreProcessMessageWinFormsHandler(MulticastDelegate):
    """ PreProcessMessageWinFormsHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, msg, callback, obj):
        """ BeginInvoke(self: PreProcessMessageWinFormsHandler, msg: tagMSG*, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PreProcessMessageWinFormsHandler, result: IAsyncResult) -> bool """
        pass

    def Invoke(self, msg):
        """ Invoke(self: PreProcessMessageWinFormsHandler, msg: tagMSG*) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


