# encoding: utf-8
# module Autodesk.AutoCAD.Internal.Windows calls itself Windows
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ClicFixedUi(object):
    """ ClicFixedUi(pFixedControl: adlsdkFixedControl*) """
    @staticmethod # known case of __new__
    def __new__(self, pFixedControl):
        """ __new__(cls: type, pFixedControl: adlsdkFixedControl*) """
        pass

    Avatar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Avatar(self: ClicFixedUi) -> str

"""

    Display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display(self: ClicFixedUi) -> bool

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: ClicFixedUi) -> bool

"""

    ItemCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemCount(self: ClicFixedUi) -> UInt32

"""

    MenuItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuItems(self: ClicFixedUi) -> List[ClicMenuUi]

"""

    MenuStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuStyle(self: ClicFixedUi) -> ClicUiStyle

"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Style(self: ClicFixedUi) -> ClicUiStyle

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: ClicFixedUi) -> str

"""



class ClicMenuUi(object):
    """ ClicMenuUi(pMenuItem: adlsdkUiMenuItem*) """
    @staticmethod # known case of __new__
    def __new__(self, pMenuItem):
        """ __new__(cls: type, pMenuItem: adlsdkUiMenuItem*) """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: ClicMenuUi) -> Array[Byte]

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: ClicMenuUi) -> bool

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: ClicMenuUi) -> str

"""



class ClicTemporalUi(object):
    """ ClicTemporalUi(pTemporalControl: adlsdkTemporalControl*) """
    @staticmethod # known case of __new__
    def __new__(self, pTemporalControl):
        """ __new__(cls: type, pTemporalControl: adlsdkTemporalControl*) """
        pass

    Action = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Action(self: ClicTemporalUi) -> Array[Byte]

"""

    Badge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Badge(self: ClicTemporalUi) -> str

"""

    Display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display(self: ClicTemporalUi) -> bool

"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: ClicTemporalUi) -> bool

"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Style(self: ClicTemporalUi) -> ClicUiStyle

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: ClicTemporalUi) -> str

"""



class ClicUi(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> ClicUi """
        pass

    def SendUiAction(self, action, left, top, right, bottom):
        """ SendUiAction(self: ClicUi, action: Array[Byte], left: int, top: int, right: int, bottom: int) """
        pass

    ClicUiDisplay = None


class ClicUiDisplayEventHandler(MulticastDelegate):
    """ ClicUiDisplayEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ClicUiDisplayEventHandler, sender: object, e: ClicUiEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ClicUiDisplayEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ClicUiDisplayEventHandler, sender: object, e: ClicUiEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ClicUiElementColors(object):
    """ ClicUiElementColors(pUiElementColors: adlsdkUiElementColors*) """
    @staticmethod # known case of __new__
    def __new__(self, pUiElementColors):
        """ __new__(cls: type, pUiElementColors: adlsdkUiElementColors*) """
        pass

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: ClicUiElementColors) -> Array[Byte]

"""

    BorderColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BorderColor(self: ClicUiElementColors) -> Array[Byte]

"""

    FontColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontColor(self: ClicUiElementColors) -> Array[Byte]

"""



class ClicUiEventArgs(EventArgs):
    # no doc
    FixedUi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedUi(self: ClicUiEventArgs) -> ClicFixedUi

"""

    TemporalUi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemporalUi(self: ClicUiEventArgs) -> ClicTemporalUi

"""



class ClicUiStyle(object):
    """ ClicUiStyle(pUiStyle: adlsdkUiStyle*) """
    @staticmethod # known case of __new__
    def __new__(self, pUiStyle):
        """ __new__(cls: type, pUiStyle: adlsdkUiStyle*) """
        pass

    FontBold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontBold(self: ClicUiStyle) -> bool

"""

    FontFamily = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontFamily(self: ClicUiStyle) -> str

"""

    FontItalic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontItalic(self: ClicUiStyle) -> bool

"""

    FontSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontSize(self: ClicUiStyle) -> UInt32

"""

    Hover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hover(self: ClicUiStyle) -> ClicUiElementColors

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: ClicUiStyle) -> ClicUiElementColors

"""



class CommandThroat(object):
    """ CommandThroat() """
    InputCharactersQueued = None


class CommandToolTipData(object):
    """ CommandToolTipData() """
    BasicContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasicContent(self: CommandToolTipData) -> str

Set: BasicContent(self: CommandToolTipData) = value
"""

    CLICommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CLICommand(self: CommandToolTipData) -> str

Set: CLICommand(self: CommandToolTipData) = value
"""

    EnableHelp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableHelp(self: CommandToolTipData) -> bool

Set: EnableHelp(self: CommandToolTipData) = value
"""

    ExtendedContentKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendedContentKey(self: CommandToolTipData) -> str

Set: ExtendedContentKey(self: CommandToolTipData) = value
"""

    ExtendedContentSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtendedContentSource(self: CommandToolTipData) -> str

Set: ExtendedContentSource(self: CommandToolTipData) = value
"""

    HelpSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpSource(self: CommandToolTipData) -> str

Set: HelpSource(self: CommandToolTipData) = value
"""

    HelpTopic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpTopic(self: CommandToolTipData) -> str

Set: HelpTopic(self: CommandToolTipData) = value
"""

    Macro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Macro(self: CommandToolTipData) -> str

Set: Macro(self: CommandToolTipData) = value
"""

    Shortcut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shortcut(self: CommandToolTipData) -> str

Set: Shortcut(self: CommandToolTipData) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: CommandToolTipData) -> str

Set: Title(self: CommandToolTipData) = value
"""

    UserTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserTag(self: CommandToolTipData) -> str

Set: UserTag(self: CommandToolTipData) = value
"""



class InputCharactersQueuedEventArgs(EventArgs):
    # no doc
    Characters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Characters(self: InputCharactersQueuedEventArgs) -> str

"""



class InputCharactersQueuedEventHandler(MulticastDelegate):
    """ InputCharactersQueuedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: InputCharactersQueuedEventHandler, sender: object, e: InputCharactersQueuedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InputCharactersQueuedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: InputCharactersQueuedEventHandler, sender: object, e: InputCharactersQueuedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class MenuGroupData(object):
    """ MenuGroupData(nMenuGroupType: MenuGroupTypeEnum, sName: str, sFileName: str, pMenuGroupData: AcMenuGroupData*) """
    def Dispose(self):
        """ Dispose(self: MenuGroupData) """
        pass

    def GetMenuMacro(self, sId=None):
        """
        GetMenuMacro(self: MenuGroupData, sId: str) -> RibbonMenuMacro
        GetMenuMacro(self: MenuGroupData) -> Dictionary[str, RibbonMenuMacro]
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, nMenuGroupType, sName, sFileName, pMenuGroupData):
        """ __new__(cls: type, nMenuGroupType: MenuGroupTypeEnum, sName: str, sFileName: str, pMenuGroupData: AcMenuGroupData*) """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: MenuGroupData) -> str

"""

    MenuGroupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuGroupType(self: MenuGroupData) -> MenuGroupTypeEnum

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MenuGroupData) -> str

"""

    PartialMenus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartialMenus(self: MenuGroupData) -> List[MenuGroupData]

"""


    DefaultToolTipHelpSource = ''


class MenuGroupTypeEnum(Enum):
    """ enum MenuGroupTypeEnum, values: Enterprise (0), Main (1), Partial (2) """
    Enterprise = None
    Main = None
    Partial = None
    value__ = None


class ProfileManager(object):
    """ ProfileManager() """
    @staticmethod
    def GetProfileNode(pNode, pszNodePath, bCreateIfNotExists, bCurrentProfile):
        """ GetProfileNode(pNode: _com_ptr_t<_com_IIID<MSXML::IXMLDOMNode\,\&_GUID_2933bf80_7b36_11d2_b20e_00c04f983e60> >*, pszNodePath: Char*, bCreateIfNotExists: bool, bCurrentProfile: bool) -> bool """
        pass

    @staticmethod
    def LoadData(sNodePath, sWSName, bCurrentProfile):
        """ LoadData(sNodePath: str, sWSName: str, bCurrentProfile: bool) -> str """
        pass

    @staticmethod
    def LoadHideableDialogSettingsDictionary():
        """ LoadHideableDialogSettingsDictionary() -> bool """
        pass

    @staticmethod
    def SaveData(sXmlData, sNodePath, sWorkspaceName, bCurrentProfile):
        """ SaveData(sXmlData: str, sNodePath: str, sWorkspaceName: str, bCurrentProfile: bool) -> bool """
        pass

    @staticmethod
    def SaveHideableDialogSettingsDictionary():
        """ SaveHideableDialogSettingsDictionary() -> bool """
        pass


class RibbonData(object):
    """ RibbonData() """
    @staticmethod
    def CreateHwndControl(sControlName, sModule, hwndParent):
        """ CreateHwndControl(sControlName: str, sModule: str, hwndParent: IntPtr) -> IntPtr """
        pass

    @staticmethod
    def CreateInvalidHwndControl(hWndParent):
        """ CreateInvalidHwndControl(hWndParent: IntPtr) -> IntPtr """
        pass

    @staticmethod
    def GetDefaultToolTipContentSources():
        """ GetDefaultToolTipContentSources() -> Collection[Uri] """
        pass

    @staticmethod
    def GetMenuGroups():
        """ GetMenuGroups() -> List[MenuGroupData] """
        pass

    @staticmethod
    def GetProfileStorageFilename():
        """ GetProfileStorageFilename() -> str """
        pass

    @staticmethod
    def GetWindowSize(hWnd):
        """ GetWindowSize(hWnd: IntPtr) -> Size """
        pass

    @staticmethod
    def Load(*__args):
        """
        Load(sImage: str, sModule: str, sGroupName: str, bSmall: bool) -> ImageSource
        Load(sCompoundName: str, sGroupName: str, bSmall: bool) -> ImageSource
        """
        pass

    @staticmethod
    def LoadXml(sNodeName, sWSName):
        """ LoadXml(sNodeName: str, sWSName: str) -> str """
        pass

    @staticmethod
    def SaveXml(sData, sWSName):
        """ SaveXml(sData: str, sWSName: str) -> bool """
        pass


class RibbonMenuMacro(object):
    """ RibbonMenuMacro(pAcMenuMacroData: AcMenuMacroData*) """
    def GetAcMenuMacroData(self, *args): #cannot find CLR method
        """ GetAcMenuMacroData(self: RibbonMenuMacro) -> AcMenuMacroData* """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pAcMenuMacroData):
        """ __new__(cls: type, pAcMenuMacroData: AcMenuMacroData*) """
        pass

    CLICommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CLICommand(self: RibbonMenuMacro) -> str

"""

    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Command(self: RibbonMenuMacro) -> str

"""

    ElementID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementID(self: RibbonMenuMacro) -> str

"""

    LargeImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeImage(self: RibbonMenuMacro) -> ImageSource

"""

    LargeImageStr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeImageStr(self: RibbonMenuMacro) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: RibbonMenuMacro) -> str

"""

    Shortcut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shortcut(self: RibbonMenuMacro) -> str

"""

    SmallImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallImage(self: RibbonMenuMacro) -> ImageSource

"""

    SmallImageStr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallImageStr(self: RibbonMenuMacro) -> str

"""

    ToolTipData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTipData(self: RibbonMenuMacro) -> CommandToolTipData

"""

    UserTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserTag(self: RibbonMenuMacro) -> str

"""



