# encoding: utf-8
# module Autodesk.AutoCAD.Internal.Reactors calls itself Reactors
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcEdIPEReactorImpl(object):
    # no doc

class AcEdOPMObjectFilterReactorImpl(object):
    # no doc

class AcEdUcsReactorImpl(object):
    # no doc

class AcEdViewFinalChangeReactorImpl(object):
    # no doc

class AcSunViewportMonitorReactorImpl(object):
    # no doc

class AcVsESWDictionaryReactor(object):
    # no doc

class AcVsESWObjectReactor(object):
    # no doc

class ApplicationDockLayoutChangedEventHandler(MulticastDelegate):
    """ ApplicationDockLayoutChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ApplicationDockLayoutChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ApplicationDockLayoutChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ApplicationDockLayoutChangedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ApplicationDocumentFrameChangedEventHandler(MulticastDelegate):
    """ ApplicationDocumentFrameChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ApplicationDocumentFrameChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ApplicationDocumentFrameChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ApplicationDocumentFrameChangedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ApplicationEventManager(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> ApplicationEventManager """
        pass

    ApplicationDockLayoutChanged = None
    ApplicationDocumentFrameChanged = None
    ApplicationMainWindowMoved = None
    ApplicationMainWindowSized = None
    ApplicationMainWindowVisibleChanged = None


class ApplicationMainWindowMovedEventHandler(MulticastDelegate):
    """ ApplicationMainWindowMovedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ApplicationMainWindowMovedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ApplicationMainWindowMovedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ApplicationMainWindowMovedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ApplicationMainWindowSizedEventHandler(MulticastDelegate):
    """ ApplicationMainWindowSizedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ApplicationMainWindowSizedEventHandler, sender: object, e: ApplicationMainWindowStateChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ApplicationMainWindowSizedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ApplicationMainWindowSizedEventHandler, sender: object, e: ApplicationMainWindowStateChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ApplicationMainWindowStateChangedEventArgs(EventArgs):
    # no doc
    ChangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChangeType(self: ApplicationMainWindowStateChangedEventArgs) -> StateChangeType

"""

    NewSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewSize(self: ApplicationMainWindowStateChangedEventArgs) -> ValueType

"""


    StateChangeType = None


class ApplicationMainWindowVisibleChangedEventHandler(MulticastDelegate):
    """ ApplicationMainWindowVisibleChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ApplicationMainWindowVisibleChangedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ApplicationMainWindowVisibleChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ApplicationMainWindowVisibleChangedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class CuiEventManager(object):
    # no doc
    def FreeCustomizationSectionHandle(self, handle):
        """ FreeCustomizationSectionHandle(self: CuiEventManager, handle: GCHandle) """
        pass

    def GetCustomizationSectionHandle(self, menuGroupName):
        """ GetCustomizationSectionHandle(self: CuiEventManager, menuGroupName: str) -> GCHandle """
        pass

    @staticmethod
    def Instance():
        """ Instance() -> CuiEventManager """
        pass

    LoadRibbon = None
    WorkspaceRestore = None
    WorkspaceRibbonSave = None
    WorkspaceSettingsSaved = None


class CuiLoadEventArgs(EventArgs):
    """ CuiLoadEventArgs() """
    CurrentWorkspaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentWorkspaceId(self: CuiLoadEventArgs) -> str

"""

    CurrentWorkspaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentWorkspaceName(self: CuiLoadEventArgs) -> str

"""



class DictionaryEventManager(object):
    """
    DictionaryEventManager(dictionaryId: ValueType, bMonitorDictionaryObjects: bool, bNotifyImmediately: bool)
    DictionaryEventManager(dictionaryId: ValueType, bMonitorDictionaryObjects: bool)
    """
    def Dispose(self):
        """ Dispose(self: DictionaryEventManager) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dictionaryId, bMonitorDictionaryObjects, bNotifyImmediately=None):
        """
        __new__(cls: type, dictionaryId: ValueType, bMonitorDictionaryObjects: bool, bNotifyImmediately: bool)
        __new__(cls: type, dictionaryId: ValueType, bMonitorDictionaryObjects: bool)
        """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: DictionaryEventManager) -> bool

Set: Enabled(self: DictionaryEventManager) = value
"""


    DictionaryModified = None
    ObjectModified = None


class IPEEventArgs(EventArgs):
    """ IPEEventArgs() """
    Entity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entity(self: IPEEventArgs) -> Entity

"""

    ExitStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExitStatus(self: IPEEventArgs) -> IPEExitStatus

"""


    IPEExitStatus = None


class IPEEventHandler(MulticastDelegate):
    """ IPEEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: IPEEventHandler, sender: object, e: IPEEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: IPEEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: IPEEventHandler, sender: object, e: IPEEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class IPEEventManager(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> IPEEventManager """
        pass

    def invokeSetIPEMacroMode(self, iMode):
        """ invokeSetIPEMacroMode(self: IPEEventManager, iMode: int) """
        pass

    def invokeSetIPEString(self, contents):
        """ invokeSetIPEString(self: IPEEventManager, contents: str) """
        pass

    IPEEnded = None
    IPEWillStart = None


class LoadRibbonEventHandler(MulticastDelegate):
    """ LoadRibbonEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: LoadRibbonEventHandler, sender: object, e: CuiLoadEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LoadRibbonEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: LoadRibbonEventHandler, sender: object, e: CuiLoadEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OPMObjectFilterEventArgs(EventArgs):
    """ OPMObjectFilterEventArgs() """
    EntityCLSID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityCLSID(self: OPMObjectFilterEventArgs) -> Guid

"""

    EntityName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityName(self: OPMObjectFilterEventArgs) -> str

"""



class OPMObjectFilterEventHandler(MulticastDelegate):
    """ OPMObjectFilterEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: OPMObjectFilterEventHandler, sender: object, e: OPMObjectFilterEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OPMObjectFilterEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: OPMObjectFilterEventHandler, sender: object, e: OPMObjectFilterEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OPMObjectFilterEventManager(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> OPMObjectFilterEventManager """
        pass

    OPMObjectFilterChanged = None


class SunViewportMonitorEventManager(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> SunViewportMonitorEventManager """
        pass

    ActiveSunModified = None
    Goodbye = None
    ViewportModified = None


class TableSubSelectFilter(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> TableSubSelectFilter """
        pass

    CellSelected = None


class TableSubSelectFilterEventArgs(EventArgs):
    """ TableSubSelectFilterEventArgs() """
    Reposition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reposition(self: TableSubSelectFilterEventArgs) -> bool

"""

    Selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selected(self: TableSubSelectFilterEventArgs) -> bool

"""

    TableId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableId(self: TableSubSelectFilterEventArgs) -> ObjectId

"""



class TableSubSelectFilterEventHandler(MulticastDelegate):
    """ TableSubSelectFilterEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: TableSubSelectFilterEventHandler, sender: object, e: TableSubSelectFilterEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TableSubSelectFilterEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: TableSubSelectFilterEventHandler, sender: object, e: TableSubSelectFilterEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class UcsEventArgs(EventArgs):
    """ UcsEventArgs() """
    Matrix3dValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Matrix3dValue(self: UcsEventArgs) -> Matrix3d

"""



class UcsEventHandler(MulticastDelegate):
    """ UcsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: UcsEventHandler, sender: object, e: UcsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: UcsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: UcsEventHandler, sender: object, e: UcsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class UcsEventManager(object):
    # no doc
    @staticmethod
    def instance():
        """ instance() -> UcsEventManager """
        pass

    DynamicOriginUpdate = None
    UcsChanged = None
    UcsWillChange = None


class ViewChangeEventArgs(EventArgs):
    """ ViewChangeEventArgs() """
    UsedX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsedX(self: ViewChangeEventArgs) -> int

"""

    UsedY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsedY(self: ViewChangeEventArgs) -> int

"""



class ViewFinalChangeEventHandler(MulticastDelegate):
    """ ViewFinalChangeEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ViewFinalChangeEventHandler, sender: object, e: ViewChangeEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ViewFinalChangeEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ViewFinalChangeEventHandler, sender: object, e: ViewChangeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ViewFinalChangeEventManager(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> ViewFinalChangeEventManager """
        pass

    SendViewFinalChange = None
    SendViewportChanged = None
    SendViewportCycled = None
    SendViewportsResized = None


class ViewResizeEventArgs(EventArgs):
    """ ViewResizeEventArgs() """
    UsedEX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsedEX(self: ViewResizeEventArgs) -> float

"""

    UsedEY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsedEY(self: ViewResizeEventArgs) -> float

"""

    UsedSplit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsedSplit(self: ViewResizeEventArgs) -> bool

"""

    UsedSX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsedSX(self: ViewResizeEventArgs) -> float

"""

    UsedSY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsedSY(self: ViewResizeEventArgs) -> float

"""



class ViewResizeEventHandler(MulticastDelegate):
    """ ViewResizeEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ViewResizeEventHandler, sender: object, e: ViewResizeEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ViewResizeEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ViewResizeEventHandler, sender: object, e: ViewResizeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class VisualStyleEventManager(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: VisualStyleEventManager) """
        pass

    @staticmethod
    def Instance():
        """ Instance() -> VisualStyleEventManager """
        pass

    def SetDataBase(self, acadDatabase, bUpdateUI):
        """ SetDataBase(self: VisualStyleEventManager, acadDatabase: Database, bUpdateUI: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    VisualStyleDictionaryEvent = None
    VisualStyleObjectEvent = None


class VsESWDictionaryEventHandler(MulticastDelegate):
    """ VsESWDictionaryEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, callback, obj):
        """ BeginInvoke(self: VsESWDictionaryEventHandler, sender: object, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: VsESWDictionaryEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender):
        """ Invoke(self: VsESWDictionaryEventHandler, sender: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class VsESWObjectEventHandler(MulticastDelegate):
    """ VsESWObjectEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, callback, obj):
        """ BeginInvoke(self: VsESWObjectEventHandler, sender: object, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: VsESWObjectEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender):
        """ Invoke(self: VsESWObjectEventHandler, sender: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class WorkspaceEventArgs(EventArgs):
    """ WorkspaceEventArgs() """
    CustomizationSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomizationSection(self: WorkspaceEventArgs) -> CustomizationSection

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: WorkspaceEventArgs) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: WorkspaceEventArgs) -> str

"""

    Workspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Workspace(self: WorkspaceEventArgs) -> Workspace

"""



class WorkspaceRestoreEventHandler(MulticastDelegate):
    """ WorkspaceRestoreEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: WorkspaceRestoreEventHandler, sender: object, e: WorkspaceEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: WorkspaceRestoreEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: WorkspaceRestoreEventHandler, sender: object, e: WorkspaceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class WorkspaceRibbonSaveEventHandler(MulticastDelegate):
    """ WorkspaceRibbonSaveEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: WorkspaceRibbonSaveEventHandler, sender: object, e: WorkspaceEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: WorkspaceRibbonSaveEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: WorkspaceRibbonSaveEventHandler, sender: object, e: WorkspaceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class WorkspaceSettingsSavedEventHandler(MulticastDelegate):
    """ WorkspaceSettingsSavedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: WorkspaceSettingsSavedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: WorkspaceSettingsSavedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: WorkspaceSettingsSavedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


