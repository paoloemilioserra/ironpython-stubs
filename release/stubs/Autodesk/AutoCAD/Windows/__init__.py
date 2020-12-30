# encoding: utf-8
# module Autodesk.AutoCAD.Windows calls itself Windows
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null, accoremgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ColorDialog(object):
    """ ColorDialog() """
    def SetDialogTabs(self, value):
        """ SetDialogTabs(self: ColorDialog, value: ColorTabs) """
        pass

    def ShowDialog(self):
        """ ShowDialog(self: ColorDialog) -> DialogResult """
        pass

    def ShowModal(self):
        """ ShowModal(self: ColorDialog) -> Nullable[bool] """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: ColorDialog) -> Color

Set: Color(self: ColorDialog) = value
"""

    IncludeByBlockByLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeByBlockByLayer(self: ColorDialog) -> bool

Set: IncludeByBlockByLayer(self: ColorDialog) = value
"""


    ColorTabs = None


class Menu(object):
    # no doc
    MenuItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuItems(self: Menu) -> MenuItemCollection

"""



class ContextMenuExtension(Menu):
    """ ContextMenuExtension() """
    def Dispose(self):
        """ Dispose(self: ContextMenuExtension) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: ContextMenuExtension) -> str

Set: Title(self: ContextMenuExtension) = value
"""


    Popup = None


class DefaultPane(Enum):
    """ enum DefaultPane, values: All (24), CursorCoordinates (1), DynamicInput (18), DynamicUcs (19), Float (12), Grid (3), LayoutIcon (22), LayoutModelIcons (20), LayoutMoreIcon (23), LineWeight (7), Model (10), ModelIcon (21), ModeMacro (0), ObjectSnap (11), ObjectTrack (6), Ortho (4), Paper (9), PaperModel (8), Polar (5), Snap (2), Spacer (14), Table (13), ViewportMaximize (16), ViewportMaximizeNext (17), ViewportMaximizePrevious (15) """
    All = None
    CursorCoordinates = None
    DynamicInput = None
    DynamicUcs = None
    Float = None
    Grid = None
    LayoutIcon = None
    LayoutModelIcons = None
    LayoutMoreIcon = None
    LineWeight = None
    Model = None
    ModelIcon = None
    ModeMacro = None
    ObjectSnap = None
    ObjectTrack = None
    Ortho = None
    Paper = None
    PaperModel = None
    Polar = None
    Snap = None
    Spacer = None
    Table = None
    value__ = None
    ViewportMaximize = None
    ViewportMaximizeNext = None
    ViewportMaximizePrevious = None


class DockSides(Enum):
    """ enum (flags) DockSides, values: Bottom (32768), Left (4096), None (0), Right (16384), Top (8192) """
    Bottom = None
    Left = None
    None = None
    Right = None
    Top = None
    value__ = None


class Window(DisposableWrapper):
    # no doc
    def Close(self):
        """ Close(self: Window) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Focus(self):
        """ Focus(self: Window) -> bool """
        pass

    @staticmethod
    def FromHandle(handle):
        """ FromHandle(handle: IntPtr) -> Window """
        pass

    @staticmethod
    def GetDeviceIndependentScale(hWnd):
        """ GetDeviceIndependentScale(hWnd: IntPtr) -> Vector """
        pass

    def GetWndPtr(self, *args): #cannot find CLR method
        """ GetWndPtr(self: Window) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, ptr: IntPtr, autoDelete: bool) """
        pass

    DeviceIndependentLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentLocation(self: Window) -> Point

Set: DeviceIndependentLocation(self: Window) = value
"""

    DeviceIndependentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentSize(self: Window) -> Size

Set: DeviceIndependentSize(self: Window) = value
"""

    Handle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handle(self: Window) -> IntPtr

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: Window) -> str

Set: Text(self: Window) = value
"""

    UnmanagedWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnmanagedWindow(self: Window) -> IntPtr

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: Window) -> bool

Set: Visible(self: Window) = value
"""

    WindowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowState(self: Window) -> State

Set: WindowState(self: Window) = value
"""


    State = None


class DocumentWindow(Window):
    # no doc
    def Activate(self):
        """ Activate(self: DocumentWindow) """
        pass

    def Close(self):
        """ Close(self: DocumentWindow) """
        pass

    def Dispose(self):
        """ Dispose(self: DocumentWindow, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, docWindow: AcApDocWindow*) """
        pass

    CanClose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanClose(self: DocumentWindow) -> bool

"""

    CanUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanUpdate(self: DocumentWindow) -> bool

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DocumentWindow) -> object

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: DocumentWindow) -> str

Set: Title(self: DocumentWindow) = value
"""


    DocumentWindowLoaded = None
    DocumentWindowUpdated = None


class DocumentWindowLoadedEventHandler(MulticastDelegate):
    """ DocumentWindowLoadedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentWindowLoadedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentWindowLoadedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentWindowLoadedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DocumentWindowUpdatedEventHandler(MulticastDelegate):
    """ DocumentWindowUpdatedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DocumentWindowUpdatedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DocumentWindowUpdatedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DocumentWindowUpdatedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DrawingDocumentWindow(DocumentWindow):
    # no doc
    def Dispose(self):
        """ Dispose(self: DocumentWindow, A_0: bool) """
        pass

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DrawingDocumentWindow) -> Document

"""



class DropTarget(object):
    # no doc
    def OnDragEnter(self, e):
        """ OnDragEnter(self: DropTarget, e: DragEventArgs) """
        pass

    def OnDragLeave(self):
        """ OnDragLeave(self: DropTarget) """
        pass

    def OnDragOver(self, e):
        """ OnDragOver(self: DropTarget, e: DragEventArgs) """
        pass

    def OnDrop(self, e):
        """ OnDrop(self: DropTarget, e: DragEventArgs) """
        pass


class IconType(Enum):
    """ enum IconType, values: Critical (2), Information (1), None (0), Warning (3) """
    Critical = None
    Information = None
    None = None
    value__ = None
    Warning = None


class InfoCenter(object):
    """ InfoCenter() """
    def InfoToolbarSizeChanged(self, bExpand):
        """ InfoToolbarSizeChanged(self: InfoCenter, bExpand: bool) """
        pass

    def InvokeToolbarMoveEvent(self):
        """ InvokeToolbarMoveEvent(self: InfoCenter) """
        pass

    def InvokeToolbarResizeEvent(self, width):
        """ InvokeToolbarResizeEvent(self: InfoCenter, width: int) """
        pass

    def LaunchSubAwareModule(self, resReqid, strCourseId, strModuleId):
        """ LaunchSubAwareModule(self: InfoCenter, resReqid: Int16, strCourseId: str, strModuleId: str) """
        pass

    Host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Host(self: InfoCenter) -> HwndSource

Set: Host(self: InfoCenter) = value
"""

    KeepFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeepFocus(self: InfoCenter) -> bool

Set: KeepFocus(self: InfoCenter) = value
"""

    SubAwareClientInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubAwareClientInfo(self: InfoCenter) -> str

"""

    UPIXMLData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UPIXMLData(self: InfoCenter) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: InfoCenter) -> bool

Set: Visible(self: InfoCenter) = value
"""


    mInitWidth = None
    m_pToolbarMoveDelegate = None
    m_pToolbarResizeDelegate = None


class InfoToolbarMoveDelegate(MulticastDelegate):
    """ InfoToolbarMoveDelegate(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: InfoToolbarMoveDelegate, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InfoToolbarMoveDelegate, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: InfoToolbarMoveDelegate) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class InfoToolbarResizeTo(MulticastDelegate):
    """ InfoToolbarResizeTo(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, width, callback, obj):
        """ BeginInvoke(self: InfoToolbarResizeTo, width: int, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InfoToolbarResizeTo, result: IAsyncResult) """
        pass

    def Invoke(self, width):
        """ Invoke(self: InfoToolbarResizeTo, width: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class LayerTransparencyDialog(object):
    """ LayerTransparencyDialog() """
    def ShowDialog(self):
        """ ShowDialog(self: LayerTransparencyDialog) -> DialogResult """
        pass

    def ShowModal(self):
        """ ShowModal(self: LayerTransparencyDialog) -> Nullable[bool] """
        pass

    Percent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Percent(self: LayerTransparencyDialog) -> UInt32

Set: Percent(self: LayerTransparencyDialog) = value
"""



class LinetypeDialog(object):
    """ LinetypeDialog() """
    def ShowDialog(self):
        """ ShowDialog(self: LinetypeDialog) -> DialogResult """
        pass

    def ShowModal(self):
        """ ShowModal(self: LinetypeDialog) -> Nullable[bool] """
        pass

    IncludeByBlockByLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeByBlockByLayer(self: LinetypeDialog) -> bool

Set: IncludeByBlockByLayer(self: LinetypeDialog) = value
"""

    Linetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetype(self: LinetypeDialog) -> ObjectId

Set: Linetype(self: LinetypeDialog) = value
"""



class LineWeightDialog(object):
    """ LineWeightDialog() """
    def ShowDialog(self):
        """ ShowDialog(self: LineWeightDialog) -> DialogResult """
        pass

    def ShowModal(self):
        """ ShowModal(self: LineWeightDialog) -> Nullable[bool] """
        pass

    IncludeByBlockByLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeByBlockByLayer(self: LineWeightDialog) -> bool

Set: IncludeByBlockByLayer(self: LineWeightDialog) = value
"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWeight(self: LineWeightDialog) -> LineWeight

Set: LineWeight(self: LineWeightDialog) = value
"""



class MenuItem(Menu):
    """
    MenuItem(value: str, icon: Icon)
    MenuItem(value: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, value, icon=None):
        """
        __new__(cls: type, value: str, icon: Icon)
        __new__(cls: type, value: str)
        """
        pass

    Checked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Checked(self: MenuItem) -> bool

Set: Checked(self: MenuItem) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: MenuItem) -> bool

Set: Enabled(self: MenuItem) = value
"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: MenuItem) -> Icon

Set: Icon(self: MenuItem) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: MenuItem) -> str

Set: Text(self: MenuItem) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: MenuItem) -> bool

Set: Visible(self: MenuItem) = value
"""


    Click = None


class MenuItemCollection(object):
    """ MenuItemCollection(owner: Menu) """
    def Add(self, value):
        """ Add(self: MenuItemCollection, value: MenuItem) -> int """
        pass

    def Clear(self):
        """ Clear(self: MenuItemCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MenuItemCollection, value: MenuItem) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: MenuItemCollection, array: Array[MenuItem], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MenuItemCollection) -> IEnumerator[IMenuItem] """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MenuItemCollection, value: MenuItem) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MenuItemCollection, index: int, value: MenuItem) """
        pass

    def Remove(self, value):
        """ Remove(self: MenuItemCollection, value: MenuItem) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MenuItemCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, owner):
        """ __new__(cls: type, owner: Menu) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MenuItemCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: MenuItemCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MenuItemCollection) -> bool

"""



class OpenFileDialog(object):
    """ OpenFileDialog(title: str, defaultName: str, extension: str, dialogName: str, flags: OpenFileDialogFlags) """
    def GetFilenames(self):
        """ GetFilenames(self: OpenFileDialog) -> Array[str] """
        pass

    def ShowDialog(self):
        """ ShowDialog(self: OpenFileDialog) -> DialogResult """
        pass

    def ShowModal(self):
        """ ShowModal(self: OpenFileDialog) -> Nullable[bool] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, title, defaultName, extension, dialogName, flags):
        """ __new__(cls: type, title: str, defaultName: str, extension: str, dialogName: str, flags: OpenFileDialogFlags) """
        pass

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filename(self: OpenFileDialog) -> str

"""


    OpenFileDialogFlags = None


class OpenFileOrFolderDialog(object):
    """ OpenFileOrFolderDialog(title: str, defaultName: str, extension: str, dialogName: str, flags: OpenFileDialogFlags) """
    def ShowDialog(self):
        """ ShowDialog(self: OpenFileOrFolderDialog) -> DialogResult """
        pass

    @staticmethod # known case of __new__
    def __new__(self, title, defaultName, extension, dialogName, flags):
        """ __new__(cls: type, title: str, defaultName: str, extension: str, dialogName: str, flags: OpenFileDialogFlags) """
        pass

    FileOrFoldername = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileOrFoldername(self: OpenFileOrFolderDialog) -> str

"""



class Palette(object):
    # no doc
    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Palette) -> str

Set: Name(self: Palette) = value
"""

    PaletteSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PaletteSet(self: Palette) -> PaletteSet

"""



class PaletteActivatedEventArgs(EventArgs):
    """ PaletteActivatedEventArgs(activated: Palette, deactivated: Palette) """
    @staticmethod # known case of __new__
    def __new__(self, activated, deactivated):
        """ __new__(cls: type, activated: Palette, deactivated: Palette) """
        pass

    Activated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Activated(self: PaletteActivatedEventArgs) -> Palette

"""

    Deactivated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Deactivated(self: PaletteActivatedEventArgs) -> Palette

"""



class PaletteActivatedEventHandler(MulticastDelegate):
    """ PaletteActivatedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteActivatedEventHandler, sender: object, e: PaletteActivatedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteActivatedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteActivatedEventHandler, sender: object, e: PaletteActivatedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteAddContextMenuEventArgs(EventArgs):
    """ PaletteAddContextMenuEventArgs(menuitems: List[MenuItem], removeMenuItems: List[int], nHitFlag: int, nRightClkTab: int) """
    @staticmethod # known case of __new__
    def __new__(self, menuitems, removeMenuItems, nHitFlag, nRightClkTab):
        """ __new__(cls: type, menuitems: List[MenuItem], removeMenuItems: List[int], nHitFlag: int, nRightClkTab: int) """
        pass

    HitFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HitFlag(self: PaletteAddContextMenuEventArgs) -> int

"""

    MenuItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuItems(self: PaletteAddContextMenuEventArgs) -> List[MenuItem]

"""

    RemoveMenuItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemoveMenuItems(self: PaletteAddContextMenuEventArgs) -> List[int]

"""

    RightClickTab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightClickTab(self: PaletteAddContextMenuEventArgs) -> int

"""



class PaletteAddContextMenuEventHandler(MulticastDelegate):
    """ PaletteAddContextMenuEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteAddContextMenuEventHandler, sender: object, e: PaletteAddContextMenuEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteAddContextMenuEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteAddContextMenuEventHandler, sender: object, e: PaletteAddContextMenuEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteEnterSizeMoveEventArgs(EventArgs):
    """ PaletteEnterSizeMoveEventArgs(bEnterSizeMove: bool) """
    @staticmethod # known case of __new__
    def __new__(self, bEnterSizeMove):
        """ __new__(cls: type, bEnterSizeMove: bool) """
        pass

    EnterSizeMove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnterSizeMove(self: PaletteEnterSizeMoveEventArgs) -> bool

"""



class PaletteEnterSizeMoveEventHandler(MulticastDelegate):
    """ PaletteEnterSizeMoveEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteEnterSizeMoveEventHandler, sender: object, e: PaletteEnterSizeMoveEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteEnterSizeMoveEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteEnterSizeMoveEventHandler, sender: object, e: PaletteEnterSizeMoveEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PalettePersistEventArgs(EventArgs):
    """ PalettePersistEventArgs(configurationSection: IConfigurationSection) """
    @staticmethod # known case of __new__
    def __new__(self, configurationSection):
        """ __new__(cls: type, configurationSection: IConfigurationSection) """
        pass

    ConfigurationSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigurationSection(self: PalettePersistEventArgs) -> IConfigurationSection

"""



class PalettePersistEventHandler(MulticastDelegate):
    """ PalettePersistEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PalettePersistEventHandler, sender: object, e: PalettePersistEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PalettePersistEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PalettePersistEventHandler, sender: object, e: PalettePersistEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSet(Window):
    """
    PaletteSet(name: str, cmd: str, toolID: Guid)
    PaletteSet(name: str, toolID: Guid)
    PaletteSet(name: str)
    """
    def Activate(self, index):
        """ Activate(self: PaletteSet, index: int) """
        pass

    def Add(self, name, *__args):
        """
        Add(self: PaletteSet, name: str, control: Control) -> Palette
        Add(self: PaletteSet, name: str, htmlPage: Uri) -> Palette
        """
        pass

    def AddVisual(self, name, control, bResizeContentToPaletteSize=None):
        """
        AddVisual(self: PaletteSet, name: str, control: Visual) -> Palette
        AddVisual(self: PaletteSet, name: str, control: Visual, bResizeContentToPaletteSize: bool) -> Palette
        """
        pass

    def AddVisualBrowser(self, name, control, htmlPage, scriptableName, bShowBrowserFirst):
        """ AddVisualBrowser(self: PaletteSet, name: str, control: Visual, htmlPage: str, scriptableName: str, bShowBrowserFirst: bool) -> Palette """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: PaletteSet, array: Array[Palette], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EnableTransparency(self, value):
        """ EnableTransparency(self: PaletteSet, value: bool) -> bool """
        pass

    def FloatControl(self, *__args):
        """ FloatControl(self: PaletteSet, pointOnScreen: Point)FloatControl(self: PaletteSet, value: Rect) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PaletteSet) -> IEnumerator """
        pass

    def GetThemedIcon(self, bBigIcon):
        """ GetThemedIcon(self: PaletteSet, bBigIcon: bool) -> Icon """
        pass

    def InitializeFloatingPosition(self, value):
        """ InitializeFloatingPosition(self: PaletteSet, value: Rect) """
        pass

    def RecalculateDockSiteLayout(self):
        """ RecalculateDockSiteLayout(self: PaletteSet) """
        pass

    def Remove(self, index):
        """ Remove(self: PaletteSet, index: int) """
        pass

    def SetThemedIcon(self, value, theme):
        """ SetThemedIcon(self: PaletteSet, value: Icon, theme: ColorThemeEnum) """
        pass

    def switchVisualBrowser(self, index, bVisual):
        """ switchVisualBrowser(self: PaletteSet, index: int, bVisual: bool) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, *__args):
        """
        __new__(cls: type, name: str, cmd: str, toolID: Guid)
        __new__(cls: type, name: str, toolID: Guid)
        __new__(cls: type, name: str)
        """
        pass

    Anchored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Anchored(self: PaletteSet) -> bool

"""

    AutoRollUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoRollUp(self: PaletteSet) -> bool

Set: AutoRollUp(self: PaletteSet) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PaletteSet) -> int

"""

    DarkThemedIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DarkThemedIcon(self: PaletteSet) -> Icon

Set: DarkThemedIcon(self: PaletteSet) = value
"""

    DeviceIndependentLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentLocation(self: PaletteSet) -> Point

Set: DeviceIndependentLocation(self: PaletteSet) = value
"""

    DeviceIndependentMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentMinimumSize(self: PaletteSet) -> Size

Set: DeviceIndependentMinimumSize(self: PaletteSet) = value
"""

    DeviceIndependentSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentSize(self: PaletteSet) -> Size

Set: DeviceIndependentSize(self: PaletteSet) = value
"""

    Dock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dock(self: PaletteSet) -> DockSides

Set: Dock(self: PaletteSet) = value
"""

    DockEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DockEnabled(self: PaletteSet) -> DockSides

Set: DockEnabled(self: PaletteSet) = value
"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: PaletteSet) -> Icon

Set: Icon(self: PaletteSet) = value
"""

    KeepFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeepFocus(self: PaletteSet) -> bool

Set: KeepFocus(self: PaletteSet) = value
"""

    LargeDarkThemedIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeDarkThemedIcon(self: PaletteSet) -> Icon

Set: LargeDarkThemedIcon(self: PaletteSet) = value
"""

    LargeLightThemedIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeLightThemedIcon(self: PaletteSet) -> Icon

Set: LargeLightThemedIcon(self: PaletteSet) = value
"""

    LightThemedIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LightThemedIcon(self: PaletteSet) -> Icon

Set: LightThemedIcon(self: PaletteSet) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: PaletteSet) -> Point

Set: Location(self: PaletteSet) = value
"""

    MinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumSize(self: PaletteSet) -> Size

Set: MinimumSize(self: PaletteSet) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PaletteSet) -> str

Set: Name(self: PaletteSet) = value
"""

    Opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Opacity(self: PaletteSet) -> int

Set: Opacity(self: PaletteSet) = value
"""

    PaletteSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PaletteSize(self: PaletteSet) -> Size

"""

    RolledUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RolledUp(self: PaletteSet) -> bool

Set: RolledUp(self: PaletteSet) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: PaletteSet) -> Size

Set: Size(self: PaletteSet) = value
"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Style(self: PaletteSet) -> PaletteSetStyles

Set: Style(self: PaletteSet) = value
"""

    TitleBarLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleBarLocation(self: PaletteSet) -> PaletteSetTitleBarLocation

Set: TitleBarLocation(self: PaletteSet) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: PaletteSet) -> bool

Set: Visible(self: PaletteSet) = value
"""


    Focused = None
    Help = None
    Load = None
    PaletteActivated = None
    PaletteAddContextMenu = None
    PaletteSetDestroy = None
    PaletteSetEnterSizeMove = None
    PaletteSetHostMoved = None
    PaletteSetMoved = None
    PaletteSetShowDockBar = None
    PaletteSetTitleBarLocationChange = None
    Save = None
    Saving = None
    SizeChanged = None
    StateChanged = None


class PaletteSetDestroyEventHandler(MulticastDelegate):
    """ PaletteSetDestroyEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetDestroyEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetDestroyEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetDestroyEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSetDockSite(object):
    """ PaletteSetDockSite() """
    def CanDock(self, mousePosition):
        """ CanDock(self: PaletteSetDockSite, mousePosition: Point) -> Nullable[Rect] """
        pass

    def Dock(self, paletteset):
        """ Dock(self: PaletteSetDockSite, paletteset: PaletteSet) -> bool """
        pass

    def Initialize(self, paletteset, desiredSize, dockSyle):
        """ Initialize(self: PaletteSetDockSite, paletteset: PaletteSet, desiredSize: Size, dockSyle: int) """
        pass

    def Uninitialize(self):
        """ Uninitialize(self: PaletteSetDockSite) """
        pass


class PaletteSetFocusedEventArgs(EventArgs):
    """ PaletteSetFocusedEventArgs() """

class PaletteSetFocusedEventHandler(MulticastDelegate):
    """ PaletteSetFocusedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetFocusedEventHandler, sender: object, e: PaletteSetFocusedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetFocusedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetFocusedEventHandler, sender: object, e: PaletteSetFocusedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSetHelpEventArgs(EventArgs):
    """ PaletteSetHelpEventArgs() """

class PaletteSetHelpEventHandler(MulticastDelegate):
    """ PaletteSetHelpEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetHelpEventHandler, sender: object, e: PaletteSetHelpEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetHelpEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetHelpEventHandler, sender: object, e: PaletteSetHelpEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSetMoveEventArgs(EventArgs):
    """ PaletteSetMoveEventArgs(x: int, y: int) """
    @staticmethod # known case of __new__
    def __new__(self, x, y):
        """ __new__(cls: type, x: int, y: int) """
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: PaletteSetMoveEventArgs) -> int

"""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: y(self: PaletteSetMoveEventArgs) -> int

"""



class PaletteSetMoveEventHandler(MulticastDelegate):
    """ PaletteSetMoveEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetMoveEventHandler, sender: object, e: PaletteSetMoveEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetMoveEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetMoveEventHandler, sender: object, e: PaletteSetMoveEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSetShowDockBarEventHandler(MulticastDelegate):
    """ PaletteSetShowDockBarEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetShowDockBarEventHandler, sender: object, e: PaletteShowDockBarEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetShowDockBarEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetShowDockBarEventHandler, sender: object, e: PaletteShowDockBarEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSetSizeEventArgs(EventArgs):
    """ PaletteSetSizeEventArgs(cx: int, cy: int, dx: float, dy: float) """
    @staticmethod # known case of __new__
    def __new__(self, cx, cy, dx, dy):
        """ __new__(cls: type, cx: int, cy: int, dx: float, dy: float) """
        pass

    DeviceIndependentHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentHeight(self: PaletteSetSizeEventArgs) -> float

"""

    DeviceIndependentWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentWidth(self: PaletteSetSizeEventArgs) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: PaletteSetSizeEventArgs) -> int

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: PaletteSetSizeEventArgs) -> int

"""



class PaletteSetSizeEventHandler(MulticastDelegate):
    """ PaletteSetSizeEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetSizeEventHandler, sender: object, e: PaletteSetSizeEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetSizeEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetSizeEventHandler, sender: object, e: PaletteSetSizeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSetStateEventArgs(EventArgs):
    """ PaletteSetStateEventArgs(state: StateEventIndex) """
    @staticmethod # known case of __new__
    def __new__(self, state):
        """ __new__(cls: type, state: StateEventIndex) """
        pass

    NewState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewState(self: PaletteSetStateEventArgs) -> StateEventIndex

"""



class PaletteSetStateEventHandler(MulticastDelegate):
    """ PaletteSetStateEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetStateEventHandler, sender: object, e: PaletteSetStateEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetStateEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetStateEventHandler, sender: object, e: PaletteSetStateEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteSetStyles(Enum):
    """ enum (flags) PaletteSetStyles, values: NameEditable (16), Notify (1024), NoTitleBar (32768), PauseAutoRollupForChildModalDialog (65536), ShowAutoHideButton (2), ShowCloseButton (8), ShowPropertiesMenu (4), ShowTabForSingle (64), SingleColDock (4096), SingleRowDock (512), SingleRowNoVertResize (2048), Snappable (32), UsePaletteNameAsTitleForSingle (128) """
    NameEditable = None
    Notify = None
    NoTitleBar = None
    PauseAutoRollupForChildModalDialog = None
    ShowAutoHideButton = None
    ShowCloseButton = None
    ShowPropertiesMenu = None
    ShowTabForSingle = None
    SingleColDock = None
    SingleRowDock = None
    SingleRowNoVertResize = None
    Snappable = None
    UsePaletteNameAsTitleForSingle = None
    value__ = None


class PaletteSetTitleBarLocation(Enum):
    """ enum PaletteSetTitleBarLocation, values: Left (0), Right (1) """
    Left = None
    Right = None
    value__ = None


class PaletteSetTitleBarLocationChangeEventHandler(MulticastDelegate):
    """ PaletteSetTitleBarLocationChangeEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PaletteSetTitleBarLocationChangeEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PaletteSetTitleBarLocationChangeEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PaletteSetTitleBarLocationChangeEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PaletteShowDockBarEventArgs(EventArgs):
    """ PaletteShowDockBarEventArgs(bShowDockBar: bool) """
    @staticmethod # known case of __new__
    def __new__(self, bShowDockBar):
        """ __new__(cls: type, bShowDockBar: bool) """
        pass

    ShowDockBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowDockBar(self: PaletteShowDockBarEventArgs) -> bool

"""



class StatusBarItem(DisposableWrapper):
    # no doc
    def DisplayContextMenu(self, menu, p):
        """ DisplayContextMenu(self: StatusBarItem, menu: ContextMenu, p: Point) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def PointToClient(self, p):
        """ PointToClient(self: StatusBarItem, p: Point) -> Point """
        pass

    def PointToScreen(self, p):
        """ PointToScreen(self: StatusBarItem, p: Point) -> Point """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        __new__(cls: type)
        """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: StatusBarItem) -> bool

Set: Enabled(self: StatusBarItem) = value
"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: StatusBarItem) -> Icon

Set: Icon(self: StatusBarItem) = value
"""

    ToolTipText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTipText(self: StatusBarItem) -> str

Set: ToolTipText(self: StatusBarItem) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: StatusBarItem) -> bool

Set: Visible(self: StatusBarItem) = value
"""


    Deleted = None
    MouseDown = None


class Pane(StatusBarItem):
    """ Pane() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        __new__(cls: type)
        """
        pass

    MaximumWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumWidth(self: Pane) -> int

Set: MaximumWidth(self: Pane) = value
"""

    MinimumWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumWidth(self: Pane) -> int

Set: MinimumWidth(self: Pane) = value
"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Style(self: Pane) -> PaneStyles

Set: Style(self: Pane) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: Pane) -> str

Set: Text(self: Pane) = value
"""



class PaneCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: PaneCollection, value: Pane) -> int """
        pass

    def Clear(self):
        """ Clear(self: PaneCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: PaneCollection, value: Pane) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: PaneCollection, array: Array[Pane], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PaneCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: PaneCollection, value: Pane) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: PaneCollection, index: int, value: Pane) """
        pass

    def Remove(self, value):
        """ Remove(self: PaneCollection, value: Pane) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: PaneCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PaneCollection) -> int

Set: Count(self: PaneCollection) = value
"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: PaneCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: PaneCollection) -> bool

"""



class PaneStyles(Enum):
    """ enum (flags) PaneStyles, values: Command (16), NoBorders (1), Normal (8), PopOut (2), PopUp (32), Stretch (4) """
    Command = None
    NoBorders = None
    Normal = None
    PopOut = None
    PopUp = None
    Stretch = None
    value__ = None


class PlotStyleDialog(object):
    """ PlotStyleDialog() """
    def ShowDialog(self):
        """ ShowDialog(self: PlotStyleDialog) -> DialogResult """
        pass

    def ShowModal(self):
        """ ShowModal(self: PlotStyleDialog) -> Nullable[bool] """
        pass

    IncludeByBlockByLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeByBlockByLayer(self: PlotStyleDialog) -> bool

Set: IncludeByBlockByLayer(self: PlotStyleDialog) = value
"""

    PlotStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotStyle(self: PlotStyleDialog) -> str

Set: PlotStyle(self: PlotStyleDialog) = value
"""



class SaveFileDialog(object):
    """ SaveFileDialog(title: str, defaultName: str, extension: str, dialogName: str, flags: SaveFileDialogFlags) """
    def ShowDialog(self):
        """ ShowDialog(self: SaveFileDialog) -> DialogResult """
        pass

    def ShowModal(self):
        """ ShowModal(self: SaveFileDialog) -> Nullable[bool] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, title, defaultName, extension, dialogName, flags):
        """ __new__(cls: type, title: str, defaultName: str, extension: str, dialogName: str, flags: SaveFileDialogFlags) """
        pass

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filename(self: SaveFileDialog) -> str

"""


    SaveFileDialogFlags = None


class StateEventIndex(Enum):
    """ enum StateEventIndex, values: Hide (0), Show (1), ThemeChange (4) """
    Hide = None
    Show = None
    ThemeChange = None
    value__ = None


class StatusBar(object):
    # no doc
    def CloseBubbleWindows(self):
        """ CloseBubbleWindows(self: StatusBar) """
        pass

    def GetDefaultPane(self, pane):
        """ GetDefaultPane(self: StatusBar, pane: DefaultPane) -> Pane """
        pass

    def RemoveDefaultPane(self, pane):
        """ RemoveDefaultPane(self: StatusBar, pane: DefaultPane) """
        pass

    def Update(self):
        """ Update(self: StatusBar) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, impObj: AcApStatusBar*) """
        pass

    Panes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Panes(self: StatusBar) -> PaneCollection

"""

    TrayItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrayItems(self: StatusBar) -> TrayItemCollection

"""

    Window = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Window(self: StatusBar) -> Window

"""



class StatusBarMouseDownEventArgs(EventArgs):
    # no doc
    Button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Button(self: StatusBarMouseDownEventArgs) -> MouseButtons

"""

    DoubleClick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoubleClick(self: StatusBarMouseDownEventArgs) -> bool

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: StatusBarMouseDownEventArgs) -> int

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: StatusBarMouseDownEventArgs) -> int

"""



class StatusBarMouseDownEventHandler(MulticastDelegate):
    """ StatusBarMouseDownEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: StatusBarMouseDownEventHandler, sender: object, e: StatusBarMouseDownEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: StatusBarMouseDownEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: StatusBarMouseDownEventHandler, sender: object, e: StatusBarMouseDownEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class TrayItem(StatusBarItem):
    """ TrayItem() """
    def CloseBubbleWindows(self):
        """ CloseBubbleWindows(self: TrayItem) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def ShowBubbleWindow(self, bubble):
        """ ShowBubbleWindow(self: TrayItem, bubble: TrayItemBubbleWindow) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        __new__(cls: type)
        """
        pass


class TrayItemBubbleWindow(DisposableWrapper):
    """ TrayItemBubbleWindow() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    HyperLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HyperLink(self: TrayItemBubbleWindow) -> str

Set: HyperLink(self: TrayItemBubbleWindow) = value
"""

    HyperText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HyperText(self: TrayItemBubbleWindow) -> str

Set: HyperText(self: TrayItemBubbleWindow) = value
"""

    IconType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IconType(self: TrayItemBubbleWindow) -> IconType

Set: IconType(self: TrayItemBubbleWindow) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: TrayItemBubbleWindow) -> str

Set: Text(self: TrayItemBubbleWindow) = value
"""

    Text2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text2(self: TrayItemBubbleWindow) -> str

Set: Text2(self: TrayItemBubbleWindow) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: TrayItemBubbleWindow) -> str

Set: Title(self: TrayItemBubbleWindow) = value
"""


    Closed = None


class TrayItemBubbleWindowClosedEventArgs(EventArgs):
    # no doc
    CloseReason = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloseReason(self: TrayItemBubbleWindowClosedEventArgs) -> TrayItemBubbleWindowCloseReason

"""



class TrayItemBubbleWindowClosedEventHandler(MulticastDelegate):
    """ TrayItemBubbleWindowClosedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: TrayItemBubbleWindowClosedEventHandler, sender: object, e: TrayItemBubbleWindowClosedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: TrayItemBubbleWindowClosedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: TrayItemBubbleWindowClosedEventHandler, sender: object, e: TrayItemBubbleWindowClosedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class TrayItemBubbleWindowCloseReason(Enum):
    """ enum TrayItemBubbleWindowCloseReason, values: ClosedByUser (3), DocumentDeactivated (7), FailedToCreate (0), HyperlinkClicked (5), NoIcons (1), NoNotifications (2), TimedOut (4) """
    ClosedByUser = None
    DocumentDeactivated = None
    FailedToCreate = None
    HyperlinkClicked = None
    NoIcons = None
    NoNotifications = None
    TimedOut = None
    value__ = None


class TrayItemCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: TrayItemCollection, value: TrayItem) -> int """
        pass

    def Clear(self):
        """ Clear(self: TrayItemCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: TrayItemCollection, value: TrayItem) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: TrayItemCollection, array: Array[TrayItem], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: TrayItemCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: TrayItemCollection, value: TrayItem) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: TrayItemCollection, index: int, value: TrayItem) """
        pass

    def Remove(self, value):
        """ Remove(self: TrayItemCollection, value: TrayItem) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: TrayItemCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: TrayItemCollection) -> int

Set: Count(self: TrayItemCollection) = value
"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFixedSize(self: TrayItemCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: TrayItemCollection) -> bool

"""



class Visuals(object):
    # no doc
    ApplicationIcon = None
    PickSetBitmap = None


class WindowExtension(object):
    # no doc
    @staticmethod
    def GetIcon(window):
        """ GetIcon(window: Window) -> Icon """
        pass

    @staticmethod
    def GetLocation(window):
        """ GetLocation(window: Window) -> Point """
        pass

    @staticmethod
    def GetSize(window):
        """ GetSize(window: Window) -> Size """
        pass

    @staticmethod
    def SetIcon(window, value):
        """ SetIcon(window: Window, value: Icon) """
        pass

    @staticmethod
    def SetLocation(window, value):
        """ SetLocation(window: Window, value: Point) """
        pass

    @staticmethod
    def SetSize(window, value):
        """ SetSize(window: Window, value: Size) """
        pass

    __all__ = [
        'GetIcon',
        'GetLocation',
        'GetSize',
        'SetIcon',
        'SetLocation',
        'SetSize',
    ]


class WPFDocumentWindow(DocumentWindow):
    """ WPFDocumentWindow(wpfVisual: Visual) """
    def Dispose(self):
        """ Dispose(self: DocumentWindow, A_0: bool) """
        pass

    def OnActivate(self, *args): #cannot find CLR method
        """ OnActivate(self: WPFDocumentWindow) """
        pass

    def OnCreate(self, *args): #cannot find CLR method
        """ OnCreate(self: WPFDocumentWindow) """
        pass

    def OnDestroy(self, *args): #cannot find CLR method
        """ OnDestroy(self: WPFDocumentWindow) """
        pass

    def OnLoad(self, *args): #cannot find CLR method
        """ OnLoad(self: WPFDocumentWindow) """
        pass

    def SetDocument(self, *args): #cannot find CLR method
        """ SetDocument(self: WPFDocumentWindow, document: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, wpfVisual):
        """ __new__(cls: type, wpfVisual: Visual) """
        pass


# variables with complex values

