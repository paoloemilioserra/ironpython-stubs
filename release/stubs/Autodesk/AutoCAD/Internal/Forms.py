# encoding: utf-8
# module Autodesk.AutoCAD.Internal.Forms calls itself Forms
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ExColumnHeader(ColumnHeader):
    """ ExColumnHeader() """
    def Dispose(self):
        """ Dispose(self: ColumnHeader, disposing: bool) """
        pass

    AllowCellEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowCellEdit(self: ExColumnHeader) -> bool

Set: AllowCellEdit(self: ExColumnHeader) = value
"""

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ListView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ListView(self: ExColumnHeader) -> ExListView

"""


    m_allowCellEdit = None
    m_tag = None


class ExListView(ListView):
    """ ExListView() """
    def ChildWindowFromPoint(self, *args): #cannot find CLR method
        """ ChildWindowFromPoint(hWndParent: IntPtr, Point: POINT) -> IntPtr """
        pass

    def Dispose(self):
        """ Dispose(self: ExListView, disposing: bool) """
        pass

    def EditCell(self, rowIndex, colIndex):
        """ EditCell(self: ExListView, rowIndex: int, colIndex: int) """
        pass

    def EditColumnLabel(self, index):
        """ EditColumnLabel(self: ExListView, index: int) """
        pass

    def EndEditBox(self):
        """ EndEditBox(self: ExListView) """
        pass

    def GetClassName(self, *args): #cannot find CLR method
        """ GetClassName(h: IntPtr) -> str """
        pass

    def GetColumnHeaderFromPoint(self, *args): #cannot find CLR method
        """ GetColumnHeaderFromPoint(self: ExListView, lvClientPoint: Point) -> int """
        pass

    def GetColumnHeaderRect(self, *args): #cannot find CLR method
        """ GetColumnHeaderRect(self: ExListView, index: int) -> (bool, Rectangle) """
        pass

    def GetColumnHeadersInDisplayOrder(self):
        """ GetColumnHeadersInDisplayOrder(self: ExListView) -> Array[ExColumnHeader] """
        pass

    def GetColumnIndicesInDisplayOrder(self):
        """ GetColumnIndicesInDisplayOrder(self: ExListView) -> Array[int] """
        pass

    def GetItemFromPoint(self, pnt):
        """ GetItemFromPoint(self: ExListView, pnt: Point) -> int """
        pass

    def GetKeyState(self, *args): #cannot find CLR method
        """ GetKeyState(nVirtKey: int) -> int """
        pass

    def GetListViewItemText(self, *args): #cannot find CLR method
        """ GetListViewItemText(lvi: ListViewItem, colIndex: int) -> str """
        pass

    def GetMaxCellWidth(self, columnIndex, bIncludeHeader):
        """ GetMaxCellWidth(self: ExListView, columnIndex: int, bIncludeHeader: bool) -> int """
        pass

    def GetMessagePos(self, *args): #cannot find CLR method
        """ GetMessagePos() -> Point """
        pass

    def GetScrollPos(self, *args): #cannot find CLR method
        """ GetScrollPos(hwnd: IntPtr, n: int) -> IntPtr """
        pass

    def GetWindowLong(self, *args): #cannot find CLR method
        """ GetWindowLong(hwnd: IntPtr, nIndex: int) -> Int64 """
        pass

    def HIWORD(self, *args): #cannot find CLR method
        """ HIWORD(val: UInt32) -> int """
        pass

    def InitImageList(self, *args): #cannot find CLR method
        """ InitImageList(self: ExListView) """
        pass

    def LOWORD(self, *args): #cannot find CLR method
        """ LOWORD(val: UInt32) -> int """
        pass

    def OnAfterCellEdit(self, *args): #cannot find CLR method
        """ OnAfterCellEdit(self: ExListView, ea: ListViewCellEditEventArgs) """
        pass

    def OnAfterColumnLabelEdit(self, *args): #cannot find CLR method
        """ OnAfterColumnLabelEdit(self: ExListView, ea: LabelEditEventArgs) """
        pass

    def OnBeforeCellEdit(self, *args): #cannot find CLR method
        """ OnBeforeCellEdit(self: ExListView, ea: ListViewCellEditEventArgs) """
        pass

    def OnBeforeColumnLabelEdit(self, *args): #cannot find CLR method
        """ OnBeforeColumnLabelEdit(self: ExListView, ea: LabelEditEventArgs) """
        pass

    def OnColumnRightClick(self, *args): #cannot find CLR method
        """ OnColumnRightClick(self: ExListView, ea: ColumnClickEventArgs) """
        pass

    def OnHideCellEdit(self, *args): #cannot find CLR method
        """ OnHideCellEdit(self: ExListView, ea: ListViewCellEditEventArgs) """
        pass

    def OnHideColumnLabelEdit(self, *args): #cannot find CLR method
        """ OnHideColumnLabelEdit(self: ExListView, ea: LabelEditEventArgs) """
        pass

    def PostMessage(self, *args): #cannot find CLR method
        """ PostMessage(hWnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr) -> bool """
        pass

    def RegisterWindowMessage(self, *args): #cannot find CLR method
        """ RegisterWindowMessage(lpString: str) -> int """
        pass

    def ScreenToClient(self, *args): #cannot find CLR method
        """ ScreenToClient(hWnd: IntPtr, lpPoint: POINT) -> (bool, POINT) """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def SendMessage(self, *args): #cannot find CLR method
        """ SendMessage(hWnd: IntPtr, msg: int, wParam: IntPtr, lParam: IntPtr) -> IntPtr """
        pass

    def SendMessageGetItemRect(self, *args): #cannot find CLR method
        """ SendMessageGetItemRect(hWnd: IntPtr, msg: int, wparam: int, rect: RECT) -> (bool, RECT) """
        pass

    def SendMessageHitTest(self, *args): #cannot find CLR method
        """ SendMessageHitTest(hWnd: IntPtr, msg: int, wParam: IntPtr, hti: HD_HITTESTINFO) -> (int, HD_HITTESTINFO) """
        pass

    def SendMessageItemHitTest(self, *args): #cannot find CLR method
        """ SendMessageItemHitTest(hWnd: IntPtr, msg: int, wParam: IntPtr, hti: LVHITTESTINFO) -> (int, LVHITTESTINFO) """
        pass

    def SendMessageSetColumn(self, *args): #cannot find CLR method
        """ SendMessageSetColumn(hWnd: IntPtr, msg: int, wParam: IntPtr, lvc: LVCOLUMN) -> (bool, LVCOLUMN) """
        pass

    def SetColumnIndicesInDisplayOrder(self, indices):
        """ SetColumnIndicesInDisplayOrder(self: ExListView, indices: Array[int]) """
        pass

    def SetColumnSortImage(self, *args): #cannot find CLR method
        """ SetColumnSortImage(self: ExListView, columnIndex: int, order: SortOrder) """
        pass

    def Sort(self):
        """ Sort(self: ExListView) """
        pass

    def ToggleSortOrder(self, *args): #cannot find CLR method
        """ ToggleSortOrder(self: ExListView, index: int) """
        pass

    def UpdateColumnSortImage(self, *args): #cannot find CLR method
        """ UpdateColumnSortImage(self: ExListView, oldIndex: int, newIndex: int) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Columns(self: ExListView) -> ExColumnHeaderCollection

"""

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleClickActivation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoubleClickActivation(self: ExListView) -> bool

Set: DoubleClickActivation(self: ExListView) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    HeaderContextMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderContextMenu(self: ExListView) -> ContextMenu

Set: HeaderContextMenu(self: ExListView) = value
"""

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsHorizontalScrollBarVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHorizontalScrollBarVisible(self: ExListView) -> bool

"""

    IsVerticalScrollBarVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVerticalScrollBarVisible(self: ExListView) -> bool

"""

    LastRightClickedColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastRightClickedColumn(self: ExListView) -> int

Set: LastRightClickedColumn(self: ExListView) = value
"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SortColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortColumn(self: ExListView) -> int

Set: SortColumn(self: ExListView) = value
"""

    Sorting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sorting(self: ExListView) -> SortOrder

Set: Sorting(self: ExListView) = value
"""

    SortOnColumnClick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortOnColumnClick(self: ExListView) -> bool

Set: SortOnColumnClick(self: ExListView) = value
"""


    AfterCellEdit = None
    AfterColumnLabelEdit = None
    AfterItemCheck = None
    BeforeCellEdit = None
    BeforeColumnLabelEdit = None
    CDDS_ITEM = 65536
    CDDS_ITEMPREPAINT = 65537
    CDDS_PREPAINT = 1
    CDDS_SUBITEM = 131072
    CDDS_SUBITEMPREPAINT = 131073
    CDRF_DODEFAULT = 0
    CDRF_NOTIFYITEMDRAW = 32
    CDRF_NOTIFYSUBITEMDRAW = 32
    CellEditEventHandler = None
    ColumnRightClick = None
    DWL_DLGPROC = 4
    DWL_MSGRESULT = 0
    DWL_USER = 8
    ExColumnHeaderCollection = None
    GWL_EXSTYLE = -20
    GWL_HINSTANCE = -6
    GWL_HWNDPARENT = -8
    GWL_ID = -12
    GWL_STYLE = -16
    GWL_USERDATA = -21
    GWL_WNDPROC = -4
    HDM_FIRST = 4608
    HDM_GETITEMRECT = 4615
    HDM_HITTEST = 4614
    HDM_SETBITMAPMARGIN = 4628
    HDM_SETIMAGELIST = 4616
    HDN_DIVIDERDBLCLICKA = -305
    HDN_DIVIDERDBLCLICKW = -325
    HDN_FIRST = -300
    HD_HITTESTINFO = None
    HideCellEdit = None
    HideColumnLabelEdit = None
    LVCFMT_BITMAP_ON_RIGHT = 4096
    LVCFMT_COL_HAS_IMAGES = 32768
    LVCFMT_IMAGE = 2048
    LVCFMT_JUSTIFYMASK = 3
    LVCFMT_RIGHT = 1
    LVCF_FMT = 1
    LVCF_IMAGE = 16
    LVCOLUMN = None
    LVHITTESTINFO = None
    LVM_FIRST = 4096
    LVM_GETCOLUMNORDERARRAY = 4155
    LVM_GETHEADER = 4127
    LVM_HITTEST = 4114
    LVM_SCROLL = 4116
    LVM_SETCOLUMN = 4192
    LVM_SETCOLUMNORDERARRAY = 4154
    LVSIL_NORMAL = 0
    LVSIL_SMALL = 1
    LVSIL_STATE = 2
    MIN_VISIBLE_WIDTH = 4
    m_columns = None
    m_filteredColumns = None
    m_headerContextMenu = None
    m_imageIndexAscending = None
    m_imageIndexDescending = None
    m_imageList = None
    m_lastRightClickedColumn = None
    m_sortColumn = None
    m_sortOnColumnClick = None
    m_sortOrder = None
    m_textbox = None
    NMCUSTOMDRAW = None
    NMHDR = None
    NMHEADER = None
    NMLVCUSTOMDRAW = None
    NM_CUSTOMDRAW = -12
    NM_FIRST = 0
    NM_RCLICK = -5
    OCM_NOTIFY = 8270
    OCM__BASE = 8192
    POINT = None
    RECT = None
    SB_HORZ = 0
    SB_VERT = 1
    VK_LCONTROL = 162
    VK_LSHIFT = 160
    VK_RCONTROL = 163
    VK_RSHIFT = 161
    WM_AFTER_ITEM_CHECK = 0
    WM_ERASEBKGND = 20
    WM_HIDE_CH_TEXTBOX = 0
    WM_HSCROLL = 276
    WM_KEYDOWN = 256
    WM_LBUTTONDOWN = 513
    WM_LBUTTONUP = 514
    WM_NOTIFY = 78
    WM_PAINT = 15
    WM_REFLECT = 8192
    WM_SIZE = 5
    WM_USER = 1024
    WM_VSCROLL = 277
    WS_HSCROLL = None
    WS_VSCROLL = None


class HelpProvider(object):
    """ HelpProvider() """
    def Add(self, comp, id):
        """ Add(self: HelpProvider, comp: object, id: str) """
        pass

    def ctrl_HelpRequested(self, sender, hlpevent):
        """ ctrl_HelpRequested(self: HelpProvider, sender: object, hlpevent: HelpEventArgs) """
        pass

    def InvokeHelp(self, topicToDisplay=None):
        """ InvokeHelp(self: HelpProvider)InvokeHelp(self: HelpProvider, topicToDisplay: str) """
        pass

    def Remove(self, comp):
        """ Remove(self: HelpProvider, comp: object) """
        pass

    def SetToolTip(self, comp, content=None, includeChildItems=None):
        """ SetToolTip(self: HelpProvider, comp: object)SetToolTip(self: HelpProvider, comp: object, content: object)SetToolTip(self: HelpProvider, comp: object, content: object, includeChildItems: bool) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    ContextHelpFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContextHelpFileName(self: HelpProvider) -> str

Set: ContextHelpFileName(self: HelpProvider) = value
"""

    HelpFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpFileName(self: HelpProvider) -> str

Set: HelpFileName(self: HelpProvider) = value
"""

    HelpPrefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpPrefix(self: HelpProvider) -> str

Set: HelpPrefix(self: HelpProvider) = value
"""

    HelpTopic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpTopic(self: HelpProvider) -> str

Set: HelpTopic(self: HelpProvider) = value
"""

    ToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTip(self: HelpProvider) -> ControlToolTip

"""


    HIDCANCEL = 'HIDCANCEL'
    HIDHELP = 'HIDHELP'
    HIDOK = 'HIDOK'


class IInPlaceEditUpdater:
    # no doc
    def IpeIsValidText(self, edit, text):
        """ IpeIsValidText(self: IInPlaceEditUpdater, edit: InPlaceEditControl, text: str) -> bool """
        pass

    def IpeUpdateText(self, edit, text):
        """ IpeUpdateText(self: IInPlaceEditUpdater, edit: InPlaceEditControl, text: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class InPlaceEditControl(TextBox):
    """ InPlaceEditControl(updater: IInPlaceEditUpdater) """
    def BeginEdit(self, rect, text):
        """ BeginEdit(self: InPlaceEditControl, rect: Rectangle, text: str) """
        pass

    def Dispose(self):
        """ Dispose(self: TextBox, disposing: bool) """
        pass

    def PreFilterMessage(self, m):
        """ PreFilterMessage(self: InPlaceEditControl, m: Message) -> (bool, Message) """
        pass

    def Select(self, start=None, length=None):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    def StopEdit(self, bUpdate):
        """ StopEdit(self: InPlaceEditControl, bUpdate: bool) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, updater):
        """ __new__(cls: type, updater: IInPlaceEditUpdater) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    OriginalText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalText(self: InPlaceEditControl) -> str

Set: OriginalText(self: InPlaceEditControl) = value
"""

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LabelEllipsis(Label):
    """ LabelEllipsis() """
    def Dispose(self):
        """ Dispose(self: Label, disposing: bool) """
        pass

    def Select(self):
        """ Select(self: Control, directed: bool, forward: bool) """
        pass

    CanEnableIme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CanRaiseEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    CreateParams = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultImeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMargin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultMinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DefaultSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DesignMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    DoubleBuffered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FontHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImeModeBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderRightToLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    RenderTransparent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ResizeRedraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ScaleChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowFocusCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowKeyboardCues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ListViewCellEditEventArgs(LabelEditEventArgs):
    """ ListViewCellEditEventArgs(rowIndex: int, colIndex: int, sLabel: str) """
    @staticmethod # known case of __new__
    def __new__(self, rowIndex, colIndex, sLabel):
        """ __new__(cls: type, rowIndex: int, colIndex: int, sLabel: str) """
        pass

    ColumnIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnIndex(self: ListViewCellEditEventArgs) -> int

"""

    RowIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowIndex(self: ListViewCellEditEventArgs) -> int

"""


    m_colIndex = None


