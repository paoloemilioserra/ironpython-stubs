# encoding: utf-8
# module Autodesk.AutoCAD.Windows.Data calls itself Data
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AnimationEditor(object):
    """ AnimationEditor() """
    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: AnimationEditor, value0: object, value1: PropertyChangedEventArgs) """
        pass

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: AnimationEditor) -> bool

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: AnimationEditor) -> NavStatus

"""


    PropertyChanged = None


class IPECommandBase(object):
    # no doc
    def CanExecute(self, parameter):
        """ CanExecute(self: IPECommandBase, parameter: object) -> bool """
        pass

    def Execute(self, parameter):
        """ Execute(self: IPECommandBase, parameter: object) """
        pass

    def raise_CanExecuteChanged(self, *args): #cannot find CLR method
        """ raise_CanExecuteChanged(self: IPECommandBase, value0: object, value1: EventArgs) """
        pass

    def SetCanExecute(self, value):
        """ SetCanExecute(self: IPECommandBase, value: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, bPreviewAble: bool)
        __new__(cls: type)
        """
        pass

    CanExecuteChanged = None


class AttachmentPointCommand(IPECommandBase):
    """ AttachmentPointCommand() """
    def Execute(self, parameter):
        """ Execute(self: AttachmentPointCommand, parameter: object) """
        pass


class AutoCompleteList(DisposableWrapper):
    """
    AutoCompleteList(prefix: str, parsedSearch: str, cmdFlags: int, searchType: CommandCompletionType, abortIfMultipleMatchesFound: bool)
    AutoCompleteList(rawSearch: str, searchType: CommandCompletionType)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Sort(self):
        """ Sort(self: AutoCompleteList) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, prefix: str, parsedSearch: str, cmdFlags: int, searchType: CommandCompletionType, abortIfMultipleMatchesFound: bool)
        __new__(cls: type, rawSearch: str, searchType: CommandCompletionType)
        """
        pass

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: AutoCompleteList) -> int

"""



class AutoCompleteToolTipService(object):
    """ AutoCompleteToolTipService() """
    @staticmethod
    def HideToolTip():
        """ HideToolTip() """
        pass

    @staticmethod
    def ShowToolTip(pTooltipInfo):
        """ ShowToolTip(pTooltipInfo: ValueType) """
        pass


class AutoCorrectList(DisposableWrapper):
    """ AutoCorrectList(rawSearch: str, searchType: AutoCorrectType) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Sort(self):
        """ Sort(self: AutoCorrectList) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, rawSearch, searchType):
        """ __new__(cls: type, rawSearch: str, searchType: AutoCorrectType) """
        pass

    HasClearWinner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasClearWinner(self: AutoCorrectList) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: AutoCorrectList) -> int

"""



class AutoCorrectorService(object):
    """ AutoCorrectorService() """
    @staticmethod
    def IsAutoCorrectSupported():
        """ IsAutoCorrectSupported() -> bool """
        pass

    @staticmethod
    def IsInputCommand(isInput):
        """ IsInputCommand(isInput: bool) """
        pass

    @staticmethod
    def UpdateErrInputCount(errInput, cmdGlobalName, cmdLocalName):
        """ UpdateErrInputCount(errInput: str, cmdGlobalName: str, cmdLocalName: str) """
        pass


class AutoCorrectType(Enum):
    """ enum (flags) AutoCorrectType, values: CommandSysvar (0), InternalCommand (1) """
    CommandSysvar = None
    InternalCommand = None
    value__ = None


class BackgroundMaskCommand(IPECommandBase):
    """ BackgroundMaskCommand() """
    def Execute(self, parameter):
        """ Execute(self: BackgroundMaskCommand, parameter: object) """
        pass


class BlockDialogModelBase(object):
    # no doc
    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: BlockDialogModelBase, value0: object, value1: PropertyChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, dialogName: str) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BlockDialogModelBase) -> str

"""


    PropertyChanged = None


class BlockDialogModelInsert(BlockDialogModelBase):
    """ BlockDialogModelInsert() """
    def Dispose(self):
        """ Dispose(self: BlockDialogModelInsert) """
        pass

    def initBlockStreamUIData(self):
        """ initBlockStreamUIData(self: BlockDialogModelInsert) """
        pass

    def Insert(self, blockKey):
        """ Insert(self: BlockDialogModelInsert, blockKey: str) """
        pass

    def InsertAndRedefine(self, blockKey):
        """ InsertAndRedefine(self: BlockDialogModelInsert, blockKey: str) """
        pass

    def InsertSnapshot(self, snapshotPath, targetBlockName):
        """ InsertSnapshot(self: BlockDialogModelInsert, snapshotPath: str, targetBlockName: str) """
        pass

    def InsertSnapshotAndRedefine(self, snapshotPath, targetBlockName):
        """ InsertSnapshotAndRedefine(self: BlockDialogModelInsert, snapshotPath: str, targetBlockName: str) """
        pass

    def InsertSnapshotWithoutRedefine(self, snapshotPath, targetBlockName):
        """ InsertSnapshotWithoutRedefine(self: BlockDialogModelInsert, snapshotPath: str, targetBlockName: str) """
        pass

    def InsertWithoutRedefine(self, blockKey):
        """ InsertWithoutRedefine(self: BlockDialogModelInsert, blockKey: str) """
        pass

    def IsBlockCanBeRedefined(self, blockKey):
        """ IsBlockCanBeRedefined(self: BlockDialogModelInsert, blockKey: str) -> bool """
        pass

    def isPaletteVisible(self):
        """ isPaletteVisible(self: BlockDialogModelInsert) -> bool """
        pass

    def RedefineFromSnapshotOnly(self, snapshotPath, targetBlockName):
        """ RedefineFromSnapshotOnly(self: BlockDialogModelInsert, snapshotPath: str, targetBlockName: str) """
        pass

    def RedefineOnly(self, blockKey):
        """ RedefineOnly(self: BlockDialogModelInsert, blockKey: str) """
        pass

    def saveBlockStreamUIData(self):
        """ saveBlockStreamUIData(self: BlockDialogModelInsert) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Explode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Explode(self: BlockDialogModelInsert) -> BlockDialogModelValue<bool>

"""

    InsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPoint(self: BlockDialogModelInsert) -> BlockDialogModelInsertionPoint

"""

    IsDragingInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDragingInsert(self: BlockDialogModelInsert) -> bool

"""

    PaletteWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PaletteWindow(self: BlockDialogModelInsert) -> Window

Set: PaletteWindow(self: BlockDialogModelInsert) = value
"""

    Repeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Repeat(self: BlockDialogModelInsert) -> BlockDialogModelValue<bool>

"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: BlockDialogModelInsert) -> BlockDialogModelRotation

"""

    Scales = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scales(self: BlockDialogModelInsert) -> BlockDialogModelScales

"""

    SelectedBlockData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: SelectedBlockData(self: BlockDialogModelInsert) = value
"""

    Unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Unit(self: BlockDialogModelInsert) -> BlockDialogModelUnit

"""

    UseGeoData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseGeoData(self: BlockDialogModelInsert) -> BlockDialogModelValue<bool>

"""



class BlockDialogModelInsertionPoint(object):
    """ BlockDialogModelInsertionPoint(host: BlockDialogModelBase) """
    @staticmethod # known case of __new__
    def __new__(self, host):
        """ __new__(cls: type, host: BlockDialogModelBase) """
        pass

    PickOnScreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickOnScreen(self: BlockDialogModelInsertionPoint) -> BlockDialogModelValue<bool>

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: BlockDialogModelInsertionPoint) -> BlockDialogModelValue<double>

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: BlockDialogModelInsertionPoint) -> BlockDialogModelValue<double>

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: BlockDialogModelInsertionPoint) -> BlockDialogModelValue<double>

"""



class BlockDialogModelRotation(object):
    """ BlockDialogModelRotation(host: BlockDialogModelBase) """
    @staticmethod # known case of __new__
    def __new__(self, host):
        """ __new__(cls: type, host: BlockDialogModelBase) """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: BlockDialogModelRotation) -> BlockDialogModelValue<double>

"""

    PickOnScreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickOnScreen(self: BlockDialogModelRotation) -> BlockDialogModelValue<bool>

"""



class BlockDialogModelScales(object):
    """ BlockDialogModelScales(host: BlockDialogModelBase) """
    @staticmethod # known case of __new__
    def __new__(self, host):
        """ __new__(cls: type, host: BlockDialogModelBase) """
        pass

    ScaleOnScreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleOnScreen(self: BlockDialogModelScales) -> BlockDialogModelValue<bool>

"""

    UniformScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniformScale(self: BlockDialogModelScales) -> BlockDialogModelValue<bool>

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: BlockDialogModelScales) -> BlockDialogModelValue<double>

"""

    XLabelState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XLabelState(self: BlockDialogModelScales) -> BlockDialogModelValue<bool>

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: BlockDialogModelScales) -> BlockDialogModelValue<double>

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: BlockDialogModelScales) -> BlockDialogModelValue<double>

"""



class BlockDialogModelUnit(object):
    """ BlockDialogModelUnit(host: BlockDialogModelBase) """
    @staticmethod # known case of __new__
    def __new__(self, host):
        """ __new__(cls: type, host: BlockDialogModelBase) """
        pass

    ScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleFactor(self: BlockDialogModelUnit) -> BlockDialogModelValueString

"""

    UnitValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitValue(self: BlockDialogModelUnit) -> BlockDialogModelValueString

"""



class BlockDialogModelValue<bool>(object):
    """ BlockDialogModelValue<bool>(dataName: str, host: BlockDialogModelBase) """
    @staticmethod # known case of __new__
    def __new__(self, dataName, host):
        """ __new__(cls: type, dataName: str, host: BlockDialogModelBase) """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: BlockDialogModelValue<bool>) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: BlockDialogModelValue<bool>) -> bool

Set: Value(self: BlockDialogModelValue<bool>) = value
"""



class BlockDialogModelValue<double>(object):
    """ BlockDialogModelValue<double>(dataName: str, host: BlockDialogModelBase) """
    @staticmethod # known case of __new__
    def __new__(self, dataName, host):
        """ __new__(cls: type, dataName: str, host: BlockDialogModelBase) """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: BlockDialogModelValue<double>) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: BlockDialogModelValue<double>) -> float

Set: Value(self: BlockDialogModelValue<double>) = value
"""



class BlockDialogModelValueString(object):
    """ BlockDialogModelValueString(dataName: str, host: BlockDialogModelBase) """
    @staticmethod # known case of __new__
    def __new__(self, dataName, host):
        """ __new__(cls: type, dataName: str, host: BlockDialogModelBase) """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: BlockDialogModelValueString) -> bool

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: BlockDialogModelValueString) -> str

Set: Value(self: BlockDialogModelValueString) = value
"""



class BlockEditor(object):
    """ BlockEditor() """
    def Dispose(self):
        """ Dispose(self: BlockEditor) """
        pass

    def OnDocumentActivated(self, sender, e):
        """ OnDocumentActivated(self: BlockEditor, sender: object, e: DocumentCollectionEventArgs) """
        pass

    def OnSystemVariableChanged(self, sender, e):
        """ OnSystemVariableChanged(self: BlockEditor, sender: object, e: PropertyChangedEventArgs) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: BlockEditor, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    BlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockName(self: BlockEditor) -> str

"""

    CurrentVisibilityStateName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentVisibilityStateName(self: BlockEditor) -> str

Set: CurrentVisibilityStateName(self: BlockEditor) = value
"""

    IsAuthorPaletteVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAuthorPaletteVisible(self: BlockEditor) -> bool

"""

    IsInBlockEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInBlockEditor(self: BlockEditor) -> bool

"""

    IsVisibilityParameterPresent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisibilityParameterPresent(self: BlockEditor) -> bool

"""

    Tooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tooltip(self: BlockEditor) -> str

"""

    VisibilitySets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisibilitySets(self: BlockEditor) -> ObservableCollection[str]

"""


    PropertyChanged = None


class BlockLibraryInterop(object):
    """ BlockLibraryInterop() """
    def Dispose(self):
        """ Dispose(self: BlockLibraryInterop) """
        pass

    def setWPFBrowserPalette(self, tabs):
        """ setWPFBrowserPalette(self: BlockLibraryInterop, tabs: Window) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class BlockRecentInterop(object):
    """ BlockRecentInterop() """
    def Dispose(self):
        """ Dispose(self: BlockRecentInterop) """
        pass

    def setWPFBrowserPalette(self, tabs):
        """ setWPFBrowserPalette(self: BlockRecentInterop, tabs: Window) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class CellStyleConverter(object):
    """ CellStyleConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: CellStyleConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: CellStyleConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    ByRowColumn = 'By Row/Column'
    Varies = '*VARIES*'


class CharacterSetCommand(IPECommandBase):
    """ CharacterSetCommand() """
    def Execute(self, parameter):
        """ Execute(self: CharacterSetCommand, parameter: object) """
        pass


class ClearLineSpaceCommand(IPECommandBase):
    """ ClearLineSpaceCommand() """
    def Execute(self, parameter):
        """ Execute(self: ClearLineSpaceCommand, parameter: object) """
        pass


class CloseCommand(IPECommandBase):
    """ CloseCommand() """
    def Execute(self, parameter):
        """ Execute(self: CloseCommand, parameter: object) """
        pass


class CMLContentSearchPreviews(object):
    """ CMLContentSearchPreviews() """
    @staticmethod
    def ClearDimStySampleObjects():
        """ ClearDimStySampleObjects() """
        pass

    @staticmethod
    def ConvertImageToImageSource(pImage):
        """ ConvertImageToImageSource(pImage: Image*) -> ImageSource """
        pass

    @staticmethod
    def CreateDimStySampleObjects():
        """ CreateDimStySampleObjects() """
        pass

    @staticmethod
    def GetBlockTRThumbnail(blockTR):
        """ GetBlockTRThumbnail(blockTR: BlockTableRecord) -> ImageSource """
        pass

    @staticmethod
    def GetColorFromSysvarSettings(sysvarName, outColor):
        """ GetColorFromSysvarSettings(sysvarName: str, outColor: Color) -> (bool, Color) """
        pass

    @staticmethod
    def GetDimStyleThumbnail(dimStyle):
        """ GetDimStyleThumbnail(dimStyle: DimStyleTableRecord) -> ImageSource """
        pass


class IInvalidateProperty:
    # no doc
    def InvalidateProperty(self, propertyName):
        """ InvalidateProperty(self: IInvalidateProperty, propertyName: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class INotifyCollectionItemsChanged:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ItemsChanged = None


class DataItemCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataItemCollection) """
        pass

    def InvalidateProperty(self, propertyName):
        """ InvalidateProperty(self: DataItemCollection, propertyName: str) """
        pass

    def raise_CollectionChanged(self, *args): #cannot find CLR method
        """ raise_CollectionChanged(self: DataItemCollection, value0: object, value1: NotifyCollectionChangedEventArgs) """
        pass

    def raise_ItemsChanged(self, *args): #cannot find CLR method
        """ raise_ItemsChanged(self: DataItemCollection, value0: object, value1: NotifyCollectionItemsChangedEventArgs) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: DataItemCollection, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[ICustomTypeDescriptor], item: ICustomTypeDescriptor) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
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

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: DataItemCollection) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DataItemCollection) -> int

"""

    CurrentItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentItem(self: DataItemCollection) -> ICustomTypeDescriptor

Set: CurrentItem(self: DataItemCollection) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: DataItemCollection) -> bool

"""


    CollectionChanged = None
    ItemsChanged = None
    PropertyChanged = None


class ColorCollection(DataItemCollection):
    # no doc
    def AddIfNotContain(self, value):
        """
        AddIfNotContain(self: ColorCollection, value: object) -> object
        AddIfNotContain(self: ColorCollection, value: Color) -> AcDiDynamicObject*
        """
        pass

    def Dispose(self):
        """ Dispose(self: DataItemCollection, A_0: bool) """
        pass

    Commands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Commands(self: ColorCollection) -> ILookup[ICommand]

"""



class ColorCommand(object):
    """
    ColorCommand(colorPropertyName: str, previewPropertyName: str)
    ColorCommand(colorPropertyName: str)
    """
    def CanExecute(self, parameter):
        """ CanExecute(self: ColorCommand, parameter: object) -> bool """
        pass

    def Execute(self, parameter):
        """ Execute(self: ColorCommand, parameter: object) """
        pass

    def raise_CanExecuteChanged(self, *args): #cannot find CLR method
        """ raise_CanExecuteChanged(self: ColorCommand, value0: object, value1: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, colorPropertyName, previewPropertyName=None):
        """
        __new__(cls: type, colorPropertyName: str, previewPropertyName: str)
        __new__(cls: type, colorPropertyName: str)
        """
        pass

    CanExecuteChanged = None


class ColorSetting(object):
    """ ColorSetting(name: str, value: Color) """
    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: ColorSetting, value0: object, value1: PropertyChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, value):
        """ __new__(cls: type, name: str, value: Color) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ColorSetting) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ColorSetting) -> Color

"""


    PropertyChanged = None


class ColorToNamedValueConverter(object):
    """ ColorToNamedValueConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: ColorToNamedValueConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: ColorToNamedValueConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass


class ColumnsSettingsDialogCommand(IPECommandBase):
    """ ColumnsSettingsDialogCommand() """
    def Execute(self, parameter):
        """ Execute(self: ColumnsSettingsDialogCommand, parameter: object) """
        pass


class Command(object):
    # no doc
    def CanExecute(self, parameter):
        """ CanExecute(self: Command, parameter: object) -> bool """
        pass

    def Clone(self):
        """ Clone(self: Command) -> object """
        pass

    def Execute(self, parameter):
        """ Execute(self: Command, parameter: object) """
        pass

    def raise_CanExecuteChanged(self, *args): #cannot find CLR method
        """ raise_CanExecuteChanged(self: Command, value0: object, value1: EventArgs) """
        pass

    Hidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hidden(self: Command) -> bool

Set: Hidden(self: Command) = value
"""

    IsFocusAble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFocusAble(self: Command) -> bool

Set: IsFocusAble(self: Command) = value
"""

    Synchronous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Synchronous(self: Command) -> bool

Set: Synchronous(self: Command) = value
"""


    CanExecuteChanged = None


class CommandCompletionType(Enum):
    """ enum (flags) CommandCompletionType, values: Command (1), File (4), Keyword (2) """
    Command = None
    File = None
    Keyword = None
    value__ = None


class CommandEditor(object):
    # no doc
    def ClearTempHistory(self):
        """ ClearTempHistory(self: CommandEditor) """
        pass

    def CopyHistoryToClipBoard(self):
        """ CopyHistoryToClipBoard(self: CommandEditor) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: CommandEditor, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def SyncHistoryViewList(self):
        """ SyncHistoryViewList(self: CommandEditor) """
        pass

    ActualDisplayedLinesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActualDisplayedLinesCount(self: CommandEditor) -> int

Set: ActualDisplayedLinesCount(self: CommandEditor) = value
"""

    CurrentCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCommand(self: CommandEditor) -> str

"""

    CurrentCommandIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCommandIcon(self: CommandEditor) -> IntPtr

"""

    History = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: History(self: CommandEditor) -> ObservableCollection[CommandHistory]

"""

    IsBusy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBusy(self: CommandEditor) -> bool

"""

    NeedShowClickableKeywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedShowClickableKeywords(self: CommandEditor) -> bool

"""

    PromptAndInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PromptAndInput(self: CommandEditor) -> PromptAndInput

"""

    RecentCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecentCommands(self: CommandEditor) -> List[str]

"""

    TemporaryHistory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemporaryHistory(self: CommandEditor) -> ObservableCollection[CommandHistory]

"""

    VisibleHistoryItemsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisibleHistoryItemsCount(self: CommandEditor) -> int

Set: VisibleHistoryItemsCount(self: CommandEditor) = value
"""


    PropertyChanged = None


class CommandEditorManager(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: CommandEditorManager) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: CommandEditorManager, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    ActiveEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveEditor(self: CommandEditorManager) -> CommandEditor

"""


    PropertyChanged = None


class CommandHistory(object):
    # no doc
    Command = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Command(self: CommandHistory) -> str

"""



class CommandLineItem(object):
    # no doc
    def AddRef(self):
        """ AddRef(self: CommandLineItem) """
        pass

    @staticmethod
    def ImageFromKey(key):
        """ ImageFromKey(key: str) -> BitmapSource """
        pass

    def Release(self):
        """ Release(self: CommandLineItem) """
        pass

    DisplayText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayText(self: CommandLineItem) -> str

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: CommandLineItem) -> int

"""

    GlobalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalName(self: CommandLineItem) -> str

"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Image(self: CommandLineItem) -> IntPtr

"""

    ImageKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageKey(self: CommandLineItem) -> str

"""

    LocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalName(self: CommandLineItem) -> str

"""

    Tooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tooltip(self: CommandLineItem) -> IntPtr

"""

    UnderlyingCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnderlyingCommand(self: CommandLineItem) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: CommandLineItem) -> str

"""



class Commands3DPrint(object):
    """ Commands3DPrint() """
    IsPrintStudioAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPrintStudioAvailable(self: Commands3DPrint) -> bool

"""



class CommandStack(object):
    # no doc
    def ContainsAny(self, commands):
        """ ContainsAny(self: CommandStack, *commands: Array[str]) -> bool """
        pass

    def ContainsOnly(self, commands):
        """ ContainsOnly(self: CommandStack, *commands: Array[str]) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommandStack) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: CommandStack, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    AllCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllCommands(self: CommandStack) -> str

"""

    MainCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MainCommand(self: CommandStack) -> str

"""


    PropertyChanged = None


class CommonProperties(object):
    # no doc
    def ContainsAny(self, properties):
        """ ContainsAny(self: CommonProperties, *properties: Array[str]) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommonProperties) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: CommonProperties, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    PropertyChanged = None


class CommonProperty(PropertyDescriptor):
    # no doc
    def CanResetValue(self, component):
        """ CanResetValue(self: CommonProperty, component: object) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: CommonProperty) """
        pass

    def GetValue(self, component=None):
        """
        GetValue(self: CommonProperty, component: object) -> object
        GetValue(self: CommonProperty) -> object
        """
        pass

    def ResetValue(self, component):
        """ ResetValue(self: CommonProperty, component: object) """
        pass

    def SetValue(self, *__args):
        """ SetValue(self: CommonProperty, component: object, value: object)SetValue(self: CommonProperty, value: object) """
        pass

    def ShouldSerializeValue(self, component):
        """ ShouldSerializeValue(self: CommonProperty, component: object) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    AttributeArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: CommonProperty) -> Type

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: CommonProperty) -> bool

"""

    ITrueValueAble_Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    NameHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: CommonProperty) -> Type

"""

    SupportsChangeEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsChangeEvents(self: CommonProperty) -> bool

"""

    TrueValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrueValues(self: CommonProperty) -> TrueValues

"""



class CompositeConverter(object):
    """ CompositeConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: CompositeConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: CompositeConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    Converters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Converters(self: CompositeConverter) -> List[IValueConverter]

"""



class DataBindings(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataBindings) """
        pass

    def GetLocalColorName(self, acadColor):
        """ GetLocalColorName(self: DataBindings, acadColor: Color) -> str """
        pass

    def Refresh(self):
        """ Refresh(self: DataBindings) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    ActiveCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveCommands(self: DataBindings) -> CommandStack

"""

    AnimationEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnimationEditor(self: DataBindings) -> AnimationEditor

"""

    ArrayCreation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrayCreation(self: DataBindings) -> object

"""

    BlockDialogModelInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockDialogModelInsert(self: DataBindings) -> BlockDialogModelInsert

"""

    BlockEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockEditor(self: DataBindings) -> BlockEditor

"""

    Collections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Collections(self: DataBindings) -> DataItemCollections

"""

    ColorSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorSettings(self: DataBindings) -> ILookup[ColorSetting]

"""

    CommandEditorManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandEditorManager(self: DataBindings) -> CommandEditorManager

"""

    Commands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Commands(self: DataBindings) -> ILookup[Command]

"""

    Commands3DPrint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Commands3DPrint(self: DataBindings) -> Commands3DPrint

"""

    CurrentViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentViewport(self: DataBindings) -> object

"""

    EffectivePropertySource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectivePropertySource(self: DataBindings) -> EffectivePropertySource

"""

    EplotExport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EplotExport(self: DataBindings) -> EplotExport

"""

    GeoData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeoData(self: DataBindings) -> GeoData

"""

    HatchCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchCommands(self: DataBindings) -> HatchCommands

"""

    InplaceTextEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InplaceTextEditor(self: DataBindings) -> InplaceTextEditor

"""

    IsoDraft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsoDraft(self: DataBindings) -> IsoDraft

"""

    LightEngine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LightEngine(self: DataBindings) -> LightEngine

"""

    NativeFunctions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NativeFunctions(self: DataBindings) -> ILookup[NativeFunction]

"""

    RenderEngine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderEngine(self: DataBindings) -> RenderEngine

"""

    SystemVariables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SystemVariables(self: DataBindings) -> ILookup[SystemVariable]

"""

    SysvarMonitorState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SysvarMonitorState(self: DataBindings) -> SysvarMonitorState

"""

    TextSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextSize(self: DataBindings) -> TextSize

"""

    ThemeEngine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThemeEngine(self: DataBindings) -> ThemeEngine

"""

    ViewportsCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportsCommands(self: DataBindings) -> ILookup[ICommand]

"""

    Views2DCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Views2DCommands(self: DataBindings) -> Views2DCommands

"""

    Workspaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Workspaces(self: DataBindings) -> WorkspaceCollection

"""


    DoNothing = None


class DataItemCollections(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataItemCollections) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blocks(self: DataItemCollections) -> DataItemCollection

"""

    Colors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Colors(self: DataItemCollections) -> ColorCollection

"""

    DetailViewStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DetailViewStyles(self: DataItemCollections) -> DataItemCollection

"""

    DimensionStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionStyles(self: DataItemCollections) -> DataItemCollection

"""

    LayerFilters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerFilters(self: DataItemCollections) -> DataItemCollection

"""

    Layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layers(self: DataItemCollections) -> DataItemCollection

"""

    LayerStates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerStates(self: DataItemCollections) -> DataItemCollection

"""

    Linetypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetypes(self: DataItemCollections) -> DataItemCollection

"""

    Lineweights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lineweights(self: DataItemCollections) -> EnumItemCollection

"""

    MleaderStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MleaderStyles(self: DataItemCollections) -> DataItemCollection

"""

    NamedModelViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamedModelViews(self: DataItemCollections) -> DataItemCollection

"""

    NamedViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamedViews(self: DataItemCollections) -> DataItemCollection

"""

    PlotStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotStyles(self: DataItemCollections) -> DataItemCollection

"""

    PointCloudClassificationSchemes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointCloudClassificationSchemes(self: DataItemCollections) -> DataItemCollection

"""

    PointCloudColorSchemes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointCloudColorSchemes(self: DataItemCollections) -> DataItemCollection

"""

    PointClouds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointClouds(self: DataItemCollections) -> DataItemCollection

"""

    RecentBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecentBlocks(self: DataItemCollections) -> DataItemCollection

"""

    RenderPresets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderPresets(self: DataItemCollections) -> DataItemCollection

"""

    SectionViewStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewStyles(self: DataItemCollections) -> DataItemCollection

"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection(self: DataItemCollections) -> Selection

"""

    TableCellStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableCellStyles(self: DataItemCollections) -> DataItemCollection

"""

    TableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableStyles(self: DataItemCollections) -> DataItemCollection

"""

    TextStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyles(self: DataItemCollections) -> DataItemCollection

"""

    UcsPlanes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UcsPlanes(self: DataItemCollections) -> DataItemCollection

"""

    UIFontInfoCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UIFontInfoCollection(self: DataItemCollections) -> IList[UIFontInfo]

"""

    VisualStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisualStyles(self: DataItemCollections) -> DataItemCollection

"""



class DataItemFactoryMethod(MulticastDelegate):
    """ DataItemFactoryMethod(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, objId, wrapper, callback, obj):
        """ BeginInvoke(self: DataItemFactoryMethod, objId: FullSubentityPath, wrapper: object, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DataItemFactoryMethod, result: IAsyncResult) -> DataItem """
        pass

    def Invoke(self, objId, wrapper):
        """ Invoke(self: DataItemFactoryMethod, objId: FullSubentityPath, wrapper: object) -> DataItem """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DbBlockImageCache(object):
    """ DbBlockImageCache() """
    def addDbReactors(self):
        """ addDbReactors(self: DbBlockImageCache) """
        pass

    def addToCache(self, fileName, blockName, width, height, backgroundColor, thumbnail, previewImagePath):
        """ addToCache(self: DbBlockImageCache, fileName: str, blockName: str, width: int, height: int, backgroundColor: AcGsColor*, thumbnail: ImageSource, previewImagePath: str) """
        pass

    def getCachedBlockBitmap(self, fileName, blockName, width, height, gsBkColor, imgSource, previewImagePath):
        """ getCachedBlockBitmap(self: DbBlockImageCache, fileName: str, blockName: str, width: int, height: int, gsBkColor: AcGsColor*, imgSource: ImageSource, previewImagePath: str) -> (bool, ImageSource, str) """
        pass

    def OnDatabaseToBeDestroyed(self, sender, e):
        """ OnDatabaseToBeDestroyed(self: DbBlockImageCache, sender: object, e: EventArgs) """
        pass

    def OnDocumentCreated(self, sender, e):
        """ OnDocumentCreated(self: DbBlockImageCache, sender: object, e: DocumentCollectionEventArgs) """
        pass

    def OnObjectErased(self, sender, e):
        """ OnObjectErased(self: DbBlockImageCache, sender: object, e: ObjectErasedEventArgs) """
        pass

    def OnObjectModified(self, sender, e):
        """ OnObjectModified(self: DbBlockImageCache, sender: object, e: ObjectEventArgs) """
        pass

    def OnObjectUnAppended(self, sender, e):
        """ OnObjectUnAppended(self: DbBlockImageCache, sender: object, e: ObjectEventArgs) """
        pass

    AcGsColorRef = None
    BlockImageCacheStruct = None


class DbObjectCollection(DataItemCollection):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataItemCollection, A_0: bool) """
        pass


class DefinedSymbolsCommand(IPECommandBase):
    """ DefinedSymbolsCommand() """
    def Execute(self, parameter):
        """ Execute(self: DefinedSymbolsCommand, parameter: object) """
        pass


class DisposingEventHandler(MulticastDelegate):
    """ DisposingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DisposingEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DisposingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DisposingEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DoubleToStringConverter(object):
    """ DoubleToStringConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: DoubleToStringConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: DoubleToStringConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: DoubleToStringConverter) -> float

Set: DefaultValue(self: DoubleToStringConverter) = value
"""



class EffectiveProperties(object):
    # no doc
    def Invalidate(self, propertyName):
        """ Invalidate(self: EffectiveProperties, propertyName: str) """
        pass

    def InvalidateProperty(self, propertyName):
        """ InvalidateProperty(self: EffectiveProperties, propertyName: str) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: EffectiveProperties, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    PropertyChanged = None


class EffectiveProperty(PropertyDescriptor):
    # no doc
    def CanResetValue(self, component):
        """ CanResetValue(self: EffectiveProperty, component: object) -> bool """
        pass

    def GetValue(self, component):
        """ GetValue(self: EffectiveProperty, component: object) -> object """
        pass

    def ResetValue(self, component):
        """ ResetValue(self: EffectiveProperty, component: object) """
        pass

    def SetValue(self, component, value):
        """ SetValue(self: EffectiveProperty, component: object, value: object) """
        pass

    def ShouldSerializeValue(self, component):
        """ ShouldSerializeValue(self: EffectiveProperty, component: object) -> bool """
        pass

    AttributeArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: EffectiveProperty) -> Type

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: EffectiveProperty) -> bool

"""

    NameHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: EffectiveProperty) -> Type

"""

    SupportsChangeEvents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsChangeEvents(self: EffectiveProperty) -> bool

"""

    TrueValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    TrueValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrueValues(self: EffectiveProperty) -> TrueValues

"""



class EffectivePropertySource(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: EffectivePropertySource) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: EffectivePropertySource, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    EffectiveProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveProperties(self: EffectivePropertySource) -> EffectiveProperties

"""


    PropertyChanged = None


class EnumItemCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: EnumItemCollection) """
        pass

    def InvalidateProperty(self, propertyName):
        """ InvalidateProperty(self: EnumItemCollection, propertyName: str) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: EnumItemCollection, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[ICustomTypeDescriptor], item: ICustomTypeDescriptor) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
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
    """Get: Count(self: EnumItemCollection) -> int

"""

    CurrentItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentItem(self: EnumItemCollection) -> ICustomTypeDescriptor

Set: CurrentItem(self: EnumItemCollection) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: EnumItemCollection) -> bool

"""


    PropertyChanged = None


class EnumSubsetConverter(object):
    """ EnumSubsetConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: EnumSubsetConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: EnumSubsetConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass


class EplotExport(object):
    """ EplotExport() """
    def Dispose(self):
        """ Dispose(self: EplotExport) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: EplotExport, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def UpdateCurrentItemExport(self):
        """ UpdateCurrentItemExport(self: EplotExport) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CurrentItemExport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentItemExport(self: EplotExport) -> str

Set: CurrentItemExport(self: EplotExport) = value
"""

    CurrentItemPageSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentItemPageSetup(self: EplotExport) -> str

Set: CurrentItemPageSetup(self: EplotExport) = value
"""

    EnablePageSetupBtn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnablePageSetupBtn(self: EplotExport) -> bool

"""

    EnableWindowBtn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableWindowBtn(self: EplotExport) -> bool

"""

    ExportSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExportSet(self: EplotExport) -> ObservableCollection[str]

"""

    PageSetupSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageSetupSet(self: EplotExport) -> ObservableCollection[str]

"""


    PropertyChanged = None


class Expression(object):
    """ Expression(value: object, text: str) """
    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: Expression, value0: object, value1: PropertyChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value, text):
        """ __new__(cls: type, value: object, text: str) """
        pass

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: Expression) -> str

Set: Text(self: Expression) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: Expression) -> object

Set: Value(self: Expression) = value
"""


    PropertyChanged = None


class ExtendedPropertyEventArgs(EventArgs):
    """ ExtendedPropertyEventArgs(propertyName: str, dataItem: ICustomTypeDescriptor, dataItemType: str) """
    @staticmethod # known case of __new__
    def __new__(self, propertyName, dataItem, dataItemType):
        """ __new__(cls: type, propertyName: str, dataItem: ICustomTypeDescriptor, dataItemType: str) """
        pass

    DataItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataItem(self: ExtendedPropertyEventArgs) -> ICustomTypeDescriptor

"""

    DataItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataItemType(self: ExtendedPropertyEventArgs) -> str

"""

    PropertyDesc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyDesc(self: ExtendedPropertyEventArgs) -> PropertyDescriptor

Set: PropertyDesc(self: ExtendedPropertyEventArgs) = value
"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyName(self: ExtendedPropertyEventArgs) -> str

"""



class ExtendedPropertyEventHandler(MulticastDelegate):
    """ ExtendedPropertyEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ExtendedPropertyEventHandler, sender: object, e: ExtendedPropertyEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ExtendedPropertyEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ExtendedPropertyEventHandler, sender: object, e: ExtendedPropertyEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ExtendedPropertyManager(object):
    """ ExtendedPropertyManager() """
    @staticmethod
    def TryGetExtendedProperty(propertyName, dataItem, dataItemType):
        """ TryGetExtendedProperty(propertyName: str, dataItem: ICustomTypeDescriptor, dataItemType: str) -> PropertyDescriptor """
        pass

    RegisterExtendedProperty = None


class FieldDialogCommand(IPECommandBase):
    """ FieldDialogCommand() """
    def Execute(self, parameter):
        """ Execute(self: FieldDialogCommand, parameter: object) """
        pass


class FindReplaceCommand(IPECommandBase):
    """ FindReplaceCommand() """
    def Execute(self, parameter):
        """ Execute(self: FindReplaceCommand, parameter: object) """
        pass


class FindTextCommand(IPECommandBase):
    """ FindTextCommand() """
    def Dispose(self):
        """ Dispose(self: FindTextCommand) """
        pass

    def Execute(self, parameter):
        """ Execute(self: FindTextCommand, parameter: object) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: FindTextCommand, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    PropertyChanged = None


class GeoData(object):
    """ GeoData() """
    def Dispose(self):
        """ Dispose(self: GeoData) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: GeoData, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    IsGeoCsSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeoCsSupported(self: GeoData) -> ValueType

"""

    IsGeomapImageUpdateAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGeomapImageUpdateAllowed(self: GeoData) -> ValueType

"""

    IsMyGeoDataAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMyGeoDataAvailable(self: GeoData) -> ValueType

"""

    IsMyLocationAvaliable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMyLocationAvaliable(self: GeoData) -> ValueType

"""

    IsSnapShotAllowed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSnapShotAllowed(self: GeoData) -> ValueType

"""


    Instance = None
    PropertyChanged = None


class HatchCommands(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: HatchCommands) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: HatchCommands, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    HasDefinedBoundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasDefinedBoundaries(self: HatchCommands) -> bool

Set: HasDefinedBoundaries(self: HatchCommands) = value
"""

    IsHatchCreation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHatchCreation(self: HatchCommands) -> bool

"""

    LaunchDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LaunchDialog(self: HatchCommands) -> ICommand

"""

    MatchProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchProperties(self: HatchCommands) -> ICommand

"""

    PickPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickPoints(self: HatchCommands) -> ICommand

"""

    RecreateBoundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecreateBoundaries(self: HatchCommands) -> ICommand

"""

    RemoveBoundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemoveBoundaries(self: HatchCommands) -> ICommand

"""

    SelectObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectObjects(self: HatchCommands) -> ICommand

"""

    SetOrigin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetOrigin(self: HatchCommands) -> ICommand

"""


    PropertyChanged = None


class HatchPatterns(object):
    # no doc
    def AppendUnknownPattern(self, unknownPattern):
        """ AppendUnknownPattern(self: HatchPatterns, unknownPattern: str) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: HatchPatterns) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: HatchPatterns, value0: object, value1: PropertyChangedEventArgs) """
        pass

    @staticmethod
    def ValidPatternName(patternName):
        """ ValidPatternName(patternName: str) -> PatPatternCategory """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    AllPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllPatterns(self: HatchPatterns) -> ObservableCollection[HatchRibbonItem]

"""

    CustomPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomPatterns(self: HatchPatterns) -> ObservableCollection[str]

"""

    GradientPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradientPatterns(self: HatchPatterns) -> ObservableCollection[str]

"""

    IsUnknownPatternSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnknownPatternSelected(self: HatchPatterns) -> bool

Set: IsUnknownPatternSelected(self: HatchPatterns) = value
"""

    PredefinedANSIPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PredefinedANSIPatterns(self: HatchPatterns) -> ObservableCollection[str]

"""

    PredefinedISOPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PredefinedISOPatterns(self: HatchPatterns) -> ObservableCollection[str]

"""

    PredefinedOtherPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PredefinedOtherPatterns(self: HatchPatterns) -> ObservableCollection[str]

"""

    PredefinedPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PredefinedPatterns(self: HatchPatterns) -> ObservableCollection[str]

"""

    UnknownPatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnknownPatterns(self: HatchPatterns) -> ObservableCollection[str]

"""


    Instance = None
    PropertyChanged = None


class HatchRibbonItem(RibbonItem):
    """ HatchRibbonItem(patternName: str, enable: bool) """
    def Equals(self, obj):
        """ Equals(self: HatchRibbonItem, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: HatchRibbonItem) -> int """
        pass

    def ToString(self):
        """ ToString(self: HatchRibbonItem) -> str """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, patternName, enable):
        """ __new__(cls: type, patternName: str, enable: bool) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ImageOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabled(self: HatchRibbonItem) -> bool

"""

    ItemOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    LargeImageOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SupportedHostControls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IDataItem:
    # no doc
    def StartTransaction(self, mode):
        """ StartTransaction(self: IDataItem, mode: OpenMode) -> IDataItemTransaction """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: IDataItem) -> ObjectId

"""



class IDataItemTransaction(IDisposable):
    # no doc
    def Commit(self):
        """ Commit(self: IDataItemTransaction) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Item = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Item(self: IDataItemTransaction) -> object

"""



class ILookup:
    # no doc
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImportCommand(IPECommandBase):
    """ ImportCommand() """
    def Execute(self, parameter):
        """ Execute(self: ImportCommand, parameter: object) """
        pass


class INamedImageProvider:
    # no doc
    def GetNamedImage(self, objectName):
        """ GetNamedImage(self: INamedImageProvider, objectName: str) -> ImageSource """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class INamedValue:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: INamedValue) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: INamedValue) -> object

"""



class InplaceTextEditor(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: InplaceTextEditor) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: InplaceTextEditor, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Annotative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Annotative(self: InplaceTextEditor) -> bool

Set: Annotative(self: InplaceTextEditor) = value
"""

    AttachmentPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttachmentPoint(self: InplaceTextEditor) -> ICommand

"""

    AttachmentPointType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttachmentPointType(self: InplaceTextEditor) -> IPEAttachmentPoint

Set: AttachmentPointType(self: InplaceTextEditor) = value
"""

    AutoCAPS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAPS(self: InplaceTextEditor) -> bool

Set: AutoCAPS(self: InplaceTextEditor) = value
"""

    BackgroundMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundMask(self: InplaceTextEditor) -> ICommand

"""

    Bold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bold(self: InplaceTextEditor) -> bool

Set: Bold(self: InplaceTextEditor) = value
"""

    CharacterSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CharacterSet(self: InplaceTextEditor) -> ICommand

"""

    ClearLineSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClearLineSpace(self: InplaceTextEditor) -> ICommand

"""

    Close = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Close(self: InplaceTextEditor) -> ICommand

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: InplaceTextEditor) -> Color

Set: Color(self: InplaceTextEditor) = value
"""

    ColumnsSettingsDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnsSettingsDialog(self: InplaceTextEditor) -> ICommand

"""

    ColumnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnType(self: InplaceTextEditor) -> IPEColumnType

Set: ColumnType(self: InplaceTextEditor) = value
"""

    CurrentFont = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentFont(self: InplaceTextEditor) -> UIFontInfo

Set: CurrentFont(self: InplaceTextEditor) = value
"""

    CurrentLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentLayer(self: InplaceTextEditor) -> str

Set: CurrentLayer(self: InplaceTextEditor) = value
"""

    DefinedSymbols = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefinedSymbols(self: InplaceTextEditor) -> ICommand

"""

    DynamicColumnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DynamicColumnType(self: InplaceTextEditor) -> IPEDynamicColumnType

Set: DynamicColumnType(self: InplaceTextEditor) = value
"""

    FieldDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldDialog(self: InplaceTextEditor) -> ICommand

"""

    FindReplace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FindReplace(self: InplaceTextEditor) -> ICommand

"""

    FlowAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowAlignment(self: InplaceTextEditor) -> IPEFlowAlignmentType

"""

    FontSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontSizes(self: InplaceTextEditor) -> ObservableCollection[str]

"""

    HaveSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HaveSelection(self: InplaceTextEditor) -> bool

"""

    Import = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Import(self: InplaceTextEditor) -> ICommand

"""

    InsertColumnBreak = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertColumnBreak(self: InplaceTextEditor) -> bool

Set: InsertColumnBreak(self: InplaceTextEditor) = value
"""

    InsertField = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertField(self: InplaceTextEditor) -> bool

Set: InsertField(self: InplaceTextEditor) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: InplaceTextEditor) -> bool

"""

    IsAnnotativeEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAnnotativeEnabled(self: InplaceTextEditor) -> bool

"""

    IsAutoListEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAutoListEnabled(self: InplaceTextEditor) -> bool

Set: IsAutoListEnabled(self: InplaceTextEditor) = value
"""

    IsBoldEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBoldEnabled(self: InplaceTextEditor) -> bool

"""

    IsChangeCaseAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsChangeCaseAvailable(self: InplaceTextEditor) -> bool

"""

    IsColumnsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsColumnsEnabled(self: InplaceTextEditor) -> bool

"""

    IsInsertColumnBreak = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsertColumnBreak(self: InplaceTextEditor) -> bool

"""

    IsInsertFieldEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInsertFieldEnabled(self: InplaceTextEditor) -> bool

"""

    IsItalicEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsItalicEnabled(self: InplaceTextEditor) -> bool

"""

    IsLineSpacingFactorAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLineSpacingFactorAvailable(self: InplaceTextEditor) -> bool

"""

    IsMatchPropertiesState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMatchPropertiesState(self: InplaceTextEditor) -> bool

Set: IsMatchPropertiesState(self: InplaceTextEditor) = value
"""

    IsOpaqueBackgroundEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOpaqueBackgroundEnabled(self: InplaceTextEditor) -> bool

"""

    IsOverlineEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverlineEnabled(self: InplaceTextEditor) -> bool

"""

    IsParagraphAlignmentAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsParagraphAlignmentAvailable(self: InplaceTextEditor) -> bool

"""

    IsRedoEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRedoEnabled(self: InplaceTextEditor) -> bool

"""

    IsRulerChecked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRulerChecked(self: InplaceTextEditor) -> bool

"""

    IsRulerEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRulerEnabled(self: InplaceTextEditor) -> bool

"""

    IsShowToolbarEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShowToolbarEnabled(self: InplaceTextEditor) -> bool

"""

    IsSpellerEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSpellerEnabled(self: InplaceTextEditor) -> bool

"""

    IsStackOrUnstackEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStackOrUnstackEnabled(self: InplaceTextEditor) -> bool

"""

    IsStrikeThroughEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStrikeThroughEnabled(self: InplaceTextEditor) -> bool

"""

    IsTabOnlyDelimiterEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTabOnlyDelimiterEnabled(self: InplaceTextEditor) -> bool

"""

    IsUnderlineEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUnderlineEnabled(self: InplaceTextEditor) -> bool

"""

    IsUndoEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUndoEnabled(self: InplaceTextEditor) -> bool

"""

    IsWysiwyg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsWysiwyg(self: InplaceTextEditor) -> bool

"""

    Italic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Italic(self: InplaceTextEditor) -> bool

Set: Italic(self: InplaceTextEditor) = value
"""

    LanguageIndexType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LanguageIndexType(self: InplaceTextEditor) -> int

"""

    LineSpacingFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSpacingFactor(self: InplaceTextEditor) -> float

Set: LineSpacingFactor(self: InplaceTextEditor) = value
"""

    LineSpacingFactors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSpacingFactors(self: InplaceTextEditor) -> Collection[float]

"""

    LineSpacingMultiples = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSpacingMultiples(self: InplaceTextEditor) -> ICommand

"""

    LineSpacingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSpacingType(self: InplaceTextEditor) -> LineSpacingTypes

Set: LineSpacingType(self: InplaceTextEditor) = value
"""

    Lowercase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lowercase(self: InplaceTextEditor) -> ICommand

"""

    MoreLineSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MoreLineSpace(self: InplaceTextEditor) -> ICommand

"""

    Numbering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Numbering(self: InplaceTextEditor) -> ICommand

"""

    NumberingAvailable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingAvailable(self: InplaceTextEditor) -> bool

Set: NumberingAvailable(self: InplaceTextEditor) = value
"""

    NumberingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberingType(self: InplaceTextEditor) -> IPENumberingType

Set: NumberingType(self: InplaceTextEditor) = value
"""

    ObliqueAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObliqueAngle(self: InplaceTextEditor) -> float

Set: ObliqueAngle(self: InplaceTextEditor) = value
"""

    OpaqueBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpaqueBackground(self: InplaceTextEditor) -> bool

Set: OpaqueBackground(self: InplaceTextEditor) = value
"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: InplaceTextEditor) -> ICommand

"""

    Overline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Overline(self: InplaceTextEditor) -> bool

Set: Overline(self: InplaceTextEditor) = value
"""

    ParagraphAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParagraphAlignment(self: InplaceTextEditor) -> IPEParagraphAlignmentType

Set: ParagraphAlignment(self: InplaceTextEditor) = value
"""

    ParagraphAlignmentOpions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParagraphAlignmentOpions(self: InplaceTextEditor) -> ICommand

"""

    ParagraphDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParagraphDialog(self: InplaceTextEditor) -> ICommand

"""

    QuickFindText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuickFindText(self: InplaceTextEditor) -> ICommand

"""

    Redo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Redo(self: InplaceTextEditor) -> ICommand

"""

    Ruler = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ruler(self: InplaceTextEditor) -> bool

Set: Ruler(self: InplaceTextEditor) = value
"""

    Scriptable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scriptable(self: InplaceTextEditor) -> bool

"""

    ShowToolbar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowToolbar(self: InplaceTextEditor) -> bool

Set: ShowToolbar(self: InplaceTextEditor) = value
"""

    Speller = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Speller(self: InplaceTextEditor) -> bool

Set: Speller(self: InplaceTextEditor) = value
"""

    Stacked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Stacked(self: InplaceTextEditor) -> bool

Set: Stacked(self: InplaceTextEditor) = value
"""

    StaticColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticColumns(self: InplaceTextEditor) -> ICommand

"""

    StaticColumnsList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticColumnsList(self: InplaceTextEditor) -> Collection[float]

"""

    StaticColumnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaticColumnType(self: InplaceTextEditor) -> IPEStaticColumnType

Set: StaticColumnType(self: InplaceTextEditor) = value
"""

    StrikeThrough = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StrikeThrough(self: InplaceTextEditor) -> bool

Set: StrikeThrough(self: InplaceTextEditor) = value
"""

    Subscript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Subscript(self: InplaceTextEditor) -> bool

Set: Subscript(self: InplaceTextEditor) = value
"""

    Superscript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Superscript(self: InplaceTextEditor) -> bool

Set: Superscript(self: InplaceTextEditor) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: InplaceTextEditor) -> object

Set: TextHeight(self: InplaceTextEditor) = value
"""

    TextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyle(self: InplaceTextEditor) -> object

Set: TextStyle(self: InplaceTextEditor) = value
"""

    TrackingFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrackingFactor(self: InplaceTextEditor) -> float

Set: TrackingFactor(self: InplaceTextEditor) = value
"""

    Underline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Underline(self: InplaceTextEditor) -> bool

Set: Underline(self: InplaceTextEditor) = value
"""

    Undo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Undo(self: InplaceTextEditor) -> ICommand

"""

    Uppercase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Uppercase(self: InplaceTextEditor) -> ICommand

"""

    WidthScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WidthScale(self: InplaceTextEditor) -> float

Set: WidthScale(self: InplaceTextEditor) = value
"""


    PropertyChanged = None


class InputBuffer(object):
    # no doc
    def ExecuteKeyword(self, keyword):
        """ ExecuteKeyword(self: InputBuffer, keyword: str) -> bool """
        pass

    def IsPromptingForCommandName(self):
        """ IsPromptingForCommandName(self: InputBuffer) -> bool """
        pass

    def OnCharQueue(self, inputChar, repCnt, flags):
        """ OnCharQueue(self: InputBuffer, inputChar: UInt32, repCnt: UInt32, flags: UInt32) -> bool """
        pass

    def OnKeyDownQueue(self, inputChar, repCnt, flags):
        """ OnKeyDownQueue(self: InputBuffer, inputChar: UInt32, repCnt: UInt32, flags: UInt32) -> bool """
        pass

    def OnSetSelectedTextQueue(self, start, end):
        """ OnSetSelectedTextQueue(self: InputBuffer, start: int, end: int) -> bool """
        pass

    def OnSysKeyDownQueue(self, inputChar, repCnt, flags):
        """ OnSysKeyDownQueue(self: InputBuffer, inputChar: UInt32, repCnt: UInt32, flags: UInt32) -> bool """
        pass

    def ParseKeywordForExecute(self, keyword):
        """ ParseKeywordForExecute(self: InputBuffer, keyword: str) -> str """
        pass

    def PasteString(self, originalString, stringToPaste):
        """ PasteString(self: InputBuffer, originalString: str, stringToPaste: str) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: InputBuffer, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def ReplaceInputQueue(self, newInput):
        """ ReplaceInputQueue(self: InputBuffer, newInput: str) """
        pass

    HasSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasSelection(self: InputBuffer) -> bool

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: InputBuffer) -> int

"""

    SelectPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectPosition(self: InputBuffer) -> int

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: InputBuffer) -> str

"""


    PropertyChanged = None


class InputSearchOptions(Enum):
    """ enum (flags) InputSearchOptions, values: AutoComplete (1), AutoCorrect (2), ContentSearch (8), MidString (16), None (0), SysvarSearch (4) """
    AutoComplete = None
    AutoCorrect = None
    ContentSearch = None
    MidString = None
    None = None
    SysvarSearch = None
    value__ = None


class Int32ToImageConverter(object):
    """ Int32ToImageConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: Int32ToImageConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: Int32ToImageConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    Images = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Images(self: Int32ToImageConverter) -> List[ImageSource]

"""



class IPEAttachmentPoint(Enum):
    """ enum IPEAttachmentPoint, values: BottomCenter (8), BottomLeft (7), BottomRight (9), MiddleCenter (5), MiddleLeft (4), MiddleRight (6), TopCenter (2), TopLeft (1), TopRight (3) """
    BottomCenter = None
    BottomLeft = None
    BottomRight = None
    MiddleCenter = None
    MiddleLeft = None
    MiddleRight = None
    TopCenter = None
    TopLeft = None
    TopRight = None
    value__ = None


class IPEColumnType(Enum):
    """ enum IPEColumnType, values: DynamicColumns (2), NoColumns (0), StaticColumns (1) """
    DynamicColumns = None
    NoColumns = None
    StaticColumns = None
    value__ = None


class IPEDynamicColumnType(Enum):
    """ enum IPEDynamicColumnType, values: DynamicAutoHeight (0), DynamicManualHeight (1) """
    DynamicAutoHeight = None
    DynamicManualHeight = None
    value__ = None


class IPEEditorSettings(Enum):
    """ enum IPEEditorSettings, values: AlwaysDisplayWysiwyg (0), CheckSpelling (4), OpaqueBackground (3), ShowRuler (2), ShowToolbar (1) """
    AlwaysDisplayWysiwyg = None
    CheckSpelling = None
    OpaqueBackground = None
    ShowRuler = None
    ShowToolbar = None
    value__ = None


class IPEFlowAlignmentType(Enum):
    """ enum IPEFlowAlignmentType, values: FlowBase (0), FlowCenter (1), FlowTop (2) """
    FlowBase = None
    FlowCenter = None
    FlowTop = None
    value__ = None


class IPENumberingType(Enum):
    """ enum IPENumberingType, values: NumberingBullet (1), NumberingLettered (5), NumberingLetterLower (3), NumberingLetterUpper (4), NumberingNumber (2), NumberingOff (0) """
    NumberingBullet = None
    NumberingLettered = None
    NumberingLetterLower = None
    NumberingLetterUpper = None
    NumberingNumber = None
    NumberingOff = None
    value__ = None


class IPENumberingTypeEnumConverter(EnumConverter):
    """ IPENumberingTypeEnumConverter(type: Type) """
    def CanConvertFrom(self, *__args):
        """ CanConvertFrom(self: IPENumberingTypeEnumConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        pass

    def ConvertFrom(self, *__args):
        """ ConvertFrom(self: IPENumberingTypeEnumConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: IPENumberingTypeEnumConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: Type) """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    EnumType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class IPEParagraphAlignmentType(Enum):
    """ enum IPEParagraphAlignmentType, values: AlignmentCenter (2), AlignmentDefault (0), AlignmentDistribute (5), AlignmentJustify (4), AlignmentLeft (1), AlignmentRight (3), NumAlignmentTypes (6) """
    AlignmentCenter = None
    AlignmentDefault = None
    AlignmentDistribute = None
    AlignmentJustify = None
    AlignmentLeft = None
    AlignmentRight = None
    NumAlignmentTypes = None
    value__ = None


class IPEStaticColumnType(Enum):
    """ enum IPEStaticColumnType, values: FiveColumns (5), FourColumns (4), OneColumn (1), SixColumns (6), ThreeColumns (3), TwoColumns (2) """
    FiveColumns = None
    FourColumns = None
    OneColumn = None
    SixColumns = None
    ThreeColumns = None
    TwoColumns = None
    value__ = None


class IsoDraft(object):
    """ IsoDraft() """
    def Dispose(self):
        """ Dispose(self: IsoDraft) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: IsoDraft, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    State = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: State(self: IsoDraft) -> Int16

Set: State(self: IsoDraft) = value
"""


    PropertyChanged = None


class NamedObjectCollection(DataItemCollection):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataItemCollection, A_0: bool) """
        pass


class LayerFilterCollection(NamedObjectCollection):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataItemCollection, A_0: bool) """
        pass


class LayerRecordCollection(DbObjectCollection):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataItemCollection, A_0: bool) """
        pass


class LightEngine(object):
    """ LightEngine() """
    def Dispose(self):
        """ Dispose(self: LightEngine) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: LightEngine, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Date = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Date(self: LightEngine) -> float

Set: Date(self: LightEngine) = value
"""

    DateTicks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateTicks(self: LightEngine) -> DoubleCollection

"""

    IsDateTimeEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDateTimeEnabled(self: LightEngine) -> bool

"""

    IsUsingGenericLightingUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUsingGenericLightingUnits(self: LightEngine) -> bool

"""

    MaxDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxDate(self: LightEngine) -> float

"""

    MaxTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxTime(self: LightEngine) -> float

"""

    MinDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinDate(self: LightEngine) -> float

"""

    MinTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinTime(self: LightEngine) -> float

"""

    Time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Time(self: LightEngine) -> float

Set: Time(self: LightEngine) = value
"""


    PropertyChanged = None


class LineSpacingMultiplesCommand(IPECommandBase):
    """ LineSpacingMultiplesCommand() """
    def Execute(self, parameter):
        """ Execute(self: LineSpacingMultiplesCommand, parameter: object) """
        pass


class LineSpacingTypes(Enum):
    """ enum LineSpacingTypes, values: LineSpacingAtLeast (2), LineSpacingExactly (1), LineSpacingMultiple (3) """
    LineSpacingAtLeast = None
    LineSpacingExactly = None
    LineSpacingMultiple = None
    value__ = None


class LineSpacingTypesEnumConverter(EnumConverter):
    """ LineSpacingTypesEnumConverter(type: Type) """
    def CanConvertFrom(self, *__args):
        """ CanConvertFrom(self: LineSpacingTypesEnumConverter, context: ITypeDescriptorContext, sourceType: Type) -> bool """
        pass

    def ConvertFrom(self, *__args):
        """ ConvertFrom(self: LineSpacingTypesEnumConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: LineSpacingTypesEnumConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type):
        """ __new__(cls: type, type: Type) """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    EnumType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LineWeightCollection(EnumItemCollection):
    # no doc
    def Dispose(self):
        """ Dispose(self: EnumItemCollection, A_0: bool) """
        pass


class LowercaseCommand(IPECommandBase):
    """ LowercaseCommand() """
    def Execute(self, parameter):
        """ Execute(self: LowercaseCommand, parameter: object) """
        pass


class MoreLineSpaceCommand(IPECommandBase):
    """ MoreLineSpaceCommand() """
    def Execute(self, parameter):
        """ Execute(self: MoreLineSpaceCommand, parameter: object) """
        pass


class MultiReplaceConverter(object):
    """ MultiReplaceConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: MultiReplaceConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: MultiReplaceConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    DefaultConverter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultConverter(self: MultiReplaceConverter) -> IValueConverter

Set: DefaultConverter(self: MultiReplaceConverter) = value
"""

    Filters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filters(self: MultiReplaceConverter) -> List[ReplaceConverter]

"""



class NamedImageProvider(object):
    """ NamedImageProvider() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: NamedImageProvider, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: NamedImageProvider, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    ImageProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageProvider(self: NamedImageProvider) -> INamedImageProvider

Set: ImageProvider(self: NamedImageProvider) = value
"""



class NativeFunction(object):
    # no doc
    def CanExecute(self, parameter):
        """ CanExecute(self: NativeFunction, parameter: object) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: NativeFunction) """
        pass

    def Execute(self, parameter):
        """ Execute(self: NativeFunction, parameter: object) """
        pass

    def raise_CanExecuteChanged(self, *args): #cannot find CLR method
        """ raise_CanExecuteChanged(self: NativeFunction, value0: object, value1: EventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CanExecuteChanged = None


class NavStatus(Enum):
    """ enum (flags) NavStatus, values: Default (4), None (0), Paused (1), Recording (2) """
    Default = None
    None = None
    Paused = None
    Recording = None
    value__ = None


class NotifyCollectionItemsChangedEventArgs(EventArgs):
    """ NotifyCollectionItemsChangedEventArgs(items: IList) """
    @staticmethod # known case of __new__
    def __new__(self, items):
        """ __new__(cls: type, items: IList) """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: NotifyCollectionItemsChangedEventArgs) -> IList

"""



class NotifyCollectionItemsChangedEventHandler(MulticastDelegate):
    """ NotifyCollectionItemsChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: NotifyCollectionItemsChangedEventHandler, sender: object, e: NotifyCollectionItemsChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: NotifyCollectionItemsChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: NotifyCollectionItemsChangedEventHandler, sender: object, e: NotifyCollectionItemsChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class NullToVariesConverter(object):
    """ NullToVariesConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: NullToVariesConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: NullToVariesConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass


class NumberingCommand(IPECommandBase):
    """ NumberingCommand() """
    def Execute(self, parameter):
        """ Execute(self: NumberingCommand, parameter: object) """
        pass


class OptionsCommand(IPECommandBase):
    """ OptionsCommand() """
    def Execute(self, parameter):
        """ Execute(self: OptionsCommand, parameter: object) """
        pass


class ParagraphAlignmentOpionsCommand(IPECommandBase):
    """ ParagraphAlignmentOpionsCommand() """
    def Execute(self, parameter):
        """ Execute(self: ParagraphAlignmentOpionsCommand, parameter: object) """
        pass


class ParagraphDialogCommand(IPECommandBase):
    """ ParagraphDialogCommand() """
    def Execute(self, parameter):
        """ Execute(self: ParagraphDialogCommand, parameter: object) """
        pass


class PatPatternCategory(Enum):
    """ enum PatPatternCategory, values: kCustomdef (2), kInvalid (-1), kISOdef (4), kPredef (0), kSolid_fill (3), kUserdef (1) """
    kCustomdef = None
    kInvalid = None
    kISOdef = None
    kPredef = None
    kSolid_fill = None
    kUserdef = None
    value__ = None


class PlotStyleCollection(DbObjectCollection):
    # no doc
    def Dispose(self):
        """ Dispose(self: DataItemCollection, A_0: bool) """
        pass


class PlotStyleNameToDataItemConverter(object):
    """ PlotStyleNameToDataItemConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: PlotStyleNameToDataItemConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: PlotStyleNameToDataItemConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass


class PromptAndInput(object):
    # no doc
    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: PromptAndInput, value0: object, value1: PropertyChangedEventArgs) """
        pass

    InputBuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InputBuffer(self: PromptAndInput) -> InputBuffer

"""

    KeywordsStringLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeywordsStringLength(self: PromptAndInput) -> int

"""

    KeywordsStringStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeywordsStringStart(self: PromptAndInput) -> int

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: PromptAndInput) -> int

"""

    Prompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prompt(self: PromptAndInput) -> str

"""

    PromptDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PromptDefault(self: PromptAndInput) -> str

"""

    PromptKeywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PromptKeywords(self: PromptAndInput) -> ObservableCollection[str]

"""

    SelectPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectPosition(self: PromptAndInput) -> int

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: PromptAndInput) -> str

"""


    Accepted = None
    Canceled = None
    PropertyChanged = None


class RedoCommand(IPECommandBase):
    """ RedoCommand() """
    def Execute(self, parameter):
        """ Execute(self: RedoCommand, parameter: object) """
        pass


class ReplaceConverter(object):
    """ ReplaceConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: ReplaceConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: ReplaceConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    Converter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Converter(self: ReplaceConverter) -> IValueConverter

Set: Converter(self: ReplaceConverter) = value
"""

    SourceValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceValue(self: ReplaceConverter) -> object

Set: SourceValue(self: ReplaceConverter) = value
"""

    TargetValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetValue(self: ReplaceConverter) -> object

Set: TargetValue(self: ReplaceConverter) = value
"""



class Selection(DbObjectCollection):
    # no doc
    def ContainsAny(self, types):
        """ ContainsAny(self: Selection, *types: Array[str]) -> bool """
        pass

    def ContainsAnyDrawingView(self):
        """ ContainsAnyDrawingView(self: Selection) -> bool """
        pass

    def ContainsOnly(self, types):
        """ ContainsOnly(self: Selection, *types: Array[str]) -> bool """
        pass

    def ContainsOnlyCoordinationModel(self):
        """ ContainsOnlyCoordinationModel(self: Selection) -> bool """
        pass

    def ContainsOnlyDrawingView(self):
        """ ContainsOnlyDrawingView(self: Selection) -> bool """
        pass

    def ContainsOnlyGeoMapImage(self):
        """ ContainsOnlyGeoMapImage(self: Selection) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DataItemCollection, A_0: bool) """
        pass

    def isContainSectionViewHatch(self):
        """ isContainSectionViewHatch(self: Selection) -> bool """
        pass

    def isOnlySectionViewHatchs(self):
        """ isOnlySectionViewHatchs(self: Selection) -> bool """
        pass

    def RemoveNonEditableObjects(self, type):
        """ RemoveNonEditableObjects(self: Selection, type: NonEditableType) -> int """
        pass

    CommonProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommonProperties(self: Selection) -> CommonProperties

"""

    IsContinuing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsContinuing(self: Selection) -> bool

Set: IsContinuing(self: Selection) = value
"""


    NonEditableType = None


class SourceToTypeConverter(object):
    """ SourceToTypeConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: SourceToTypeConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: SourceToTypeConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    ConverterType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConverterType(self: SourceToTypeConverter) -> Type

Set: ConverterType(self: SourceToTypeConverter) = value
"""

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceType(self: SourceToTypeConverter) -> Type

Set: SourceType(self: SourceToTypeConverter) = value
"""



class StandardConverter(object):
    """ StandardConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: StandardConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: StandardConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceType(self: StandardConverter) -> Type

Set: SourceType(self: StandardConverter) = value
"""

    TargetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetType(self: StandardConverter) -> Type

Set: TargetType(self: StandardConverter) = value
"""



class StandardUcsPlane(object):
    # no doc
    Back = None
    Bottom = None
    Front = None
    Left = None
    Right = None
    Top = None
    Unnamed = None
    World = None


class StaticColumnsCommand(IPECommandBase):
    """ StaticColumnsCommand() """
    def Execute(self, parameter):
        """ Execute(self: StaticColumnsCommand, parameter: object) """
        pass


class SubEntity(object):
    # no doc
    @staticmethod
    def Create(path):
        """ Create(path: FullSubentityPath) -> SubEntity """
        pass

    def Dispose(self):
        """ Dispose(self: SubEntity) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    ParentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentType(self: SubEntity) -> Type

"""



class SystemVariable(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: SystemVariable) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: SystemVariable, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabled(self: SystemVariable) -> bool

"""

    ITrueValueAble_Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Maximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Maximum(self: SystemVariable) -> float

"""

    Minimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minimum(self: SystemVariable) -> float

"""

    MutedValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MutedValue(self: SystemVariable) -> object

Set: MutedValue(self: SystemVariable) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SystemVariable) -> str

"""

    TrueValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrueValues(self: SystemVariable) -> TrueValues

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: SystemVariable) -> object

Set: Value(self: SystemVariable) = value
"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueType(self: SystemVariable) -> Type

"""


    PropertyChanged = None


class SysvarMonitorState(object):
    """ SysvarMonitorState() """
    def Dispose(self):
        """ Dispose(self: SysvarMonitorState) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: SysvarMonitorState, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def ShowDialog(self):
        """ ShowDialog(self: SysvarMonitorState) """
        pass

    def SyncState(self):
        """ SyncState(self: SysvarMonitorState) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    DifferenceNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DifferenceNumber(self: SysvarMonitorState) -> Int16

"""

    HasDifference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasDifference(self: SysvarMonitorState) -> bool

"""

    ShowBalloon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowBalloon(self: SysvarMonitorState) -> bool

"""


    PropertyChanged = None


class TextSize(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: TextSize) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: TextSize, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    FontSizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontSizes(self: TextSize) -> ObservableCollection[str]

"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: TextSize) -> object

Set: TextHeight(self: TextSize) = value
"""


    m_TextSize = None
    PropertyChanged = None


class ThemeEngine(object):
    """ ThemeEngine() """
    def Dispose(self):
        """ Dispose(self: ThemeEngine) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: ThemeEngine, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Brightness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brightness(self: ThemeEngine) -> float

"""

    Hue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hue(self: ThemeEngine) -> float

"""

    Saturation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Saturation(self: ThemeEngine) -> float

"""


    PropertyChanged = None


class TransparencyItem(object):
    """ TransparencyItem(transparency: Transparency, ErrorText: str) """
    @staticmethod # known case of __new__
    def __new__(self, transparency, ErrorText):
        """
        __new__[TransparencyItem]() -> TransparencyItem
        
        __new__(cls: type, transparency: Transparency, ErrorText: str)
        """
        pass

    ErrorText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorText(self: TransparencyItem) -> str

"""

    LayerValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerValue(self: TransparencyItem) -> int

"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transparency(self: TransparencyItem) -> Transparency

"""



class TrueValues(object):
    # no doc
    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: TrueValues, value0: object, value1: PropertyChangedEventArgs) """
        pass

    AcadColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AcadColor(self: TrueValues) -> Color

Set: AcadColor(self: TrueValues) = value
"""

    HPBACKGROUNDCOLOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HPBACKGROUNDCOLOR(self: TrueValues) -> str

Set: HPBACKGROUNDCOLOR(self: TrueValues) = value
"""

    HPCOLOR = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HPCOLOR(self: TrueValues) -> str

Set: HPCOLOR(self: TrueValues) = value
"""

    StringValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringValue(self: TrueValues) -> str

Set: StringValue(self: TrueValues) = value
"""


    PropertyChanged = None


class UIFontInfo(object):
    """ UIFontInfo(fontName: str, isTrueType: bool) """
    @staticmethod
    def GetFontInfo(fontName):
        """ GetFontInfo(fontName: str) -> UIFontInfo """
        pass

    @staticmethod
    def GetFontInfoCollection():
        """ GetFontInfoCollection() -> Collection[UIFontInfo] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fontName, isTrueType):
        """ __new__(cls: type, fontName: str, isTrueType: bool) """
        pass

    IsTrueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTrueType(self: UIFontInfo) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: UIFontInfo) -> str

"""



class UndoCommand(IPECommandBase):
    """ UndoCommand() """
    def Execute(self, parameter):
        """ Execute(self: UndoCommand, parameter: object) """
        pass


class UppercaseCommand(IPECommandBase):
    """ UppercaseCommand() """
    def Execute(self, parameter):
        """ Execute(self: UppercaseCommand, parameter: object) """
        pass


class ValueToNamedValueConverter(object):
    """ ValueToNamedValueConverter() """
    def Convert(self, value, targetType, parameter, culture):
        """ Convert(self: ValueToNamedValueConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def ConvertBack(self, value, targetType, parameter, culture):
        """ ConvertBack(self: ValueToNamedValueConverter, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass


class View2DRibbonItemData(object):
    """
    View2DRibbonItemData(id: int, text: Char*, iconkey: Char*, id2: UInt32)
    View2DRibbonItemData()
    """
    def Dispose(self):
        """ Dispose(self: View2DRibbonItemData) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id=None, text=None, iconkey=None, id2=None):
        """
        __new__(cls: type, id: int, text: Char*, iconkey: Char*, id2: UInt32)
        __new__(cls: type)
        """
        pass

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: View2DRibbonItemData) -> str

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: View2DRibbonItemData) -> str

"""


    mIconKey = None
    mId = None
    mId2 = None
    mKey = None
    mText = None


class Views2DCommands(object):
    # no doc
    def ConvertDoubleToStr(self, value, targetType, parameter, culture):
        """ ConvertDoubleToStr(self: Views2DCommands, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def convertItemData2Image(self, item):
        """ convertItemData2Image(self: Views2DCommands, item: object) -> str """
        pass

    def ConvertStrToDouble(self, value, targetType, parameter, culture):
        """ ConvertStrToDouble(self: Views2DCommands, value: object, targetType: Type, parameter: object, culture: CultureInfo) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: Views2DCommands) """
        pass

    def isVetoSetCurrentDetailViewStyle(self):
        """ isVetoSetCurrentDetailViewStyle(self: Views2DCommands) -> bool """
        pass

    def isVetoSetCurrentSectionViewStyle(self):
        """ isVetoSetCurrentSectionViewStyle(self: Views2DCommands) -> bool """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: Views2DCommands, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def showVetoWarning(self):
        """ showVetoWarning(self: Views2DCommands) """
        pass

    def vetoSetCurrentDetailViewStyle(self, value):
        """ vetoSetCurrentDetailViewStyle(self: Views2DCommands, value: object) -> bool """
        pass

    def vetoSetCurrentSectionViewStyle(self, value):
        """ vetoSetCurrentSectionViewStyle(self: Views2DCommands, value: object) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    AutoUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoUpdate(self: Views2DCommands) -> bool

Set: AutoUpdate(self: Views2DCommands) = value
"""

    CircularRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CircularRbt(self: Views2DCommands) -> bool

Set: CircularRbt(self: Views2DCommands) = value
"""

    CutInheritance_1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutInheritance_1(self: Views2DCommands) -> bool

Set: CutInheritance_1(self: Views2DCommands) = value
"""

    DeferUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeferUpdate(self: Views2DCommands) -> bool

Set: DeferUpdate(self: Views2DCommands) = value
"""

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: Views2DCommands) -> float

Set: Depth(self: Views2DCommands) = value
"""

    DepthType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthType(self: Views2DCommands) -> object

Set: DepthType(self: Views2DCommands) = value
"""

    DepthTypeList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthTypeList(self: Views2DCommands) -> ObservableCollection[View2DRibbonItemData]

"""

    DesignView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignView(self: Views2DCommands) -> object

Set: DesignView(self: Views2DCommands) = value
"""

    DesignViewList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignViewList(self: Views2DCommands) -> ObservableCollection[str]

"""

    DetailLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DetailLevel(self: Views2DCommands) -> object

Set: DetailLevel(self: Views2DCommands) = value
"""

    DetailLevelList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DetailLevelList(self: Views2DCommands) -> ObservableCollection[str]

"""

    Identifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Identifier(self: Views2DCommands) -> str

Set: Identifier(self: Views2DCommands) = value
"""

    IsEmptyMS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmptyMS(self: Views2DCommands) -> int

"""

    IsEnabledAccept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledAccept(self: Views2DCommands) -> bool

"""

    IsEnabledAutoUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledAutoUpdate(self: Views2DCommands) -> bool

"""

    IsEnabledBoundaryRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledBoundaryRbt(self: Views2DCommands) -> bool

"""

    IsEnabledCancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledCancel(self: Views2DCommands) -> bool

"""

    IsEnabledCutInheritance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledCutInheritance(self: Views2DCommands) -> bool

"""

    IsEnabledCutInheritance1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledCutInheritance1(self: Views2DCommands) -> bool

"""

    IsEnabledDeferUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledDeferUpdate(self: Views2DCommands) -> bool

"""

    IsEnabledDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledDepth(self: Views2DCommands) -> bool

"""

    IsEnabledDepthDrag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledDepthDrag(self: Views2DCommands) -> bool

"""

    IsEnabledDepthType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledDepthType(self: Views2DCommands) -> bool

"""

    IsEnabledDesignView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledDesignView(self: Views2DCommands) -> bool

"""

    IsEnabledDetailLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledDetailLevel(self: Views2DCommands) -> bool

"""

    IsEnabledIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledIdentifier(self: Views2DCommands) -> bool

"""

    IsEnabledMember = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledMember(self: Views2DCommands) -> bool

"""

    IsEnabledModelEdgeRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledModelEdgeRbt(self: Views2DCommands) -> bool

"""

    IsEnabledMove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledMove(self: Views2DCommands) -> bool

"""

    IsEnabledOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledOption(self: Views2DCommands) -> bool

"""

    IsEnabledOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledOrientation(self: Views2DCommands) -> bool

"""

    IsEnabledPosRepresentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledPosRepresentation(self: Views2DCommands) -> bool

"""

    IsEnabledPresentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledPresentation(self: Views2DCommands) -> bool

"""

    IsEnabledProjectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledProjectionView(self: Views2DCommands) -> bool

"""

    IsEnabledScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledScale(self: Views2DCommands) -> bool

"""

    IsEnabledSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledSelect(self: Views2DCommands) -> bool

"""

    IsEnabledSheetMetal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledSheetMetal(self: Views2DCommands) -> bool

"""

    IsEnabledShowHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledShowHatch(self: Views2DCommands) -> bool

"""

    IsEnabledSViewLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledSViewLabel(self: Views2DCommands) -> bool

"""

    IsEnabledViewStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledViewStyle(self: Views2DCommands) -> bool

"""

    IsEnabledVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledVisibility(self: Views2DCommands) -> bool

"""

    IsEnabledVisibility1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledVisibility1(self: Views2DCommands) -> bool

"""

    IsEnabledVisibility2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledVisibility2(self: Views2DCommands) -> bool

"""

    IsEnabledVisibility3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledVisibility3(self: Views2DCommands) -> bool

"""

    IsEnabledVisibility4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledVisibility4(self: Views2DCommands) -> bool

"""

    IsEnabledVisibility5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledVisibility5(self: Views2DCommands) -> bool

"""

    IsEnabledVisibility6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledVisibility6(self: Views2DCommands) -> bool

"""

    IsEnabledWeldment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabledWeldment(self: Views2DCommands) -> bool

"""

    IsEnableGradientPatern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnableGradientPatern(self: Views2DCommands) -> bool

"""

    IsEnableReturn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnableReturn(self: Views2DCommands) -> bool

"""

    IsSynergyObjServiceRegistered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynergyObjServiceRegistered(self: Views2DCommands) -> bool

"""

    JaggedRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JaggedRbt(self: Views2DCommands) -> bool

Set: JaggedRbt(self: Views2DCommands) = value
"""

    Member = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Member(self: Views2DCommands) -> object

Set: Member(self: Views2DCommands) = value
"""

    MemberList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberList(self: Views2DCommands) -> ObservableCollection[View2DRibbonItemData]

"""

    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Orientation(self: Views2DCommands) -> object

Set: Orientation(self: Views2DCommands) = value
"""

    OrientationList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrientationList(self: Views2DCommands) -> ObservableCollection[View2DRibbonItemData]

"""

    PosRepresentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PosRepresentation(self: Views2DCommands) -> object

Set: PosRepresentation(self: Views2DCommands) = value
"""

    PosRepresentationList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PosRepresentationList(self: Views2DCommands) -> ObservableCollection[str]

"""

    Presentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Presentation(self: Views2DCommands) -> object

Set: Presentation(self: Views2DCommands) = value
"""

    PresentationList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PresentationList(self: Views2DCommands) -> ObservableCollection[str]

"""

    ProjectionView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionView(self: Views2DCommands) -> object

Set: ProjectionView(self: Views2DCommands) = value
"""

    ProjectionViewList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionViewList(self: Views2DCommands) -> ObservableCollection[View2DRibbonItemData]

"""

    RectangularRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RectangularRbt(self: Views2DCommands) -> bool

Set: RectangularRbt(self: Views2DCommands) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: Views2DCommands) -> object

Set: Scale(self: Views2DCommands) = value
"""

    ScaleList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleList(self: Views2DCommands) -> ObservableCollection[str]

"""

    SheetMetal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetMetal(self: Views2DCommands) -> object

Set: SheetMetal(self: Views2DCommands) = value
"""

    SheetMetalList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetMetalList(self: Views2DCommands) -> ObservableCollection[View2DRibbonItemData]

"""

    ShowHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowHatch(self: Views2DCommands) -> bool

Set: ShowHatch(self: Views2DCommands) = value
"""

    SmoothRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothRbt(self: Views2DCommands) -> bool

Set: SmoothRbt(self: Views2DCommands) = value
"""

    SmoothWBRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothWBRbt(self: Views2DCommands) -> bool

Set: SmoothWBRbt(self: Views2DCommands) = value
"""

    SmoothWCRbt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothWCRbt(self: Views2DCommands) -> bool

Set: SmoothWCRbt(self: Views2DCommands) = value
"""

    StyleObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleObject(self: Views2DCommands) -> RibbonListButton

Set: StyleObject(self: Views2DCommands) = value
"""

    SViewLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SViewLabel(self: Views2DCommands) -> bool

Set: SViewLabel(self: Views2DCommands) = value
"""

    ViewAccept = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewAccept(self: Views2DCommands) -> ICommand

"""

    ViewBaseINV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewBaseINV(self: Views2DCommands) -> ICommand

"""

    ViewBaseMS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewBaseMS(self: Views2DCommands) -> ICommand

"""

    ViewCancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewCancel(self: Views2DCommands) -> ICommand

"""

    ViewMove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewMove(self: Views2DCommands) -> ICommand

"""

    ViewOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewOption(self: Views2DCommands) -> ICommand

"""

    ViewReturn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewReturn(self: Views2DCommands) -> ICommand

"""

    ViewSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewSelect(self: Views2DCommands) -> ICommand

"""

    ViewSelectDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewSelectDepth(self: Views2DCommands) -> ICommand

"""

    ViewStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyle(self: Views2DCommands) -> Int16

Set: ViewStyle(self: Views2DCommands) = value
"""

    ViewStyleFB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyleFB(self: Views2DCommands) -> ICommand

"""

    ViewStyleFBImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyleFBImage(self: Views2DCommands) -> object

"""

    ViewStyleFBText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyleFBText(self: Views2DCommands) -> str

"""

    ViewStyleSH = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyleSH(self: Views2DCommands) -> ICommand

"""

    ViewStyleSV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyleSV(self: Views2DCommands) -> ICommand

"""

    ViewStyleWH = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyleWH(self: Views2DCommands) -> ICommand

"""

    ViewStyleWV = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewStyleWV(self: Views2DCommands) -> ICommand

"""

    ViewUpdateAll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewUpdateAll(self: Views2DCommands) -> ICommand

"""

    Visibility_1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility_1(self: Views2DCommands) -> bool

Set: Visibility_1(self: Views2DCommands) = value
"""

    Visibility_2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility_2(self: Views2DCommands) -> bool

Set: Visibility_2(self: Views2DCommands) = value
"""

    Visibility_3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility_3(self: Views2DCommands) -> bool

Set: Visibility_3(self: Views2DCommands) = value
"""

    Visibility_4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility_4(self: Views2DCommands) -> bool

Set: Visibility_4(self: Views2DCommands) = value
"""

    Visibility_5 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility_5(self: Views2DCommands) -> bool

Set: Visibility_5(self: Views2DCommands) = value
"""

    Visibility_6 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility_6(self: Views2DCommands) -> bool

Set: Visibility_6(self: Views2DCommands) = value
"""

    Weldment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weldment(self: Views2DCommands) -> object

Set: Weldment(self: Views2DCommands) = value
"""

    WeldmentList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeldmentList(self: Views2DCommands) -> ObservableCollection[View2DRibbonItemData]

"""


    PropertyChanged = None


class WorkspaceCollection(ObservableCollection[RibbonItem]):
    # no doc
    def CUILoaded(self, sender, e):
        """ CUILoaded(self: WorkspaceCollection, sender: object, e: CuiLoadEventArgs) """
        pass

    def OnSysvarCmdNamesChanged(self, sender, e):
        """ OnSysvarCmdNamesChanged(self: WorkspaceCollection, sender: object, e: PropertyChangedEventArgs) """
        pass

    def OnSysvarWSCurrentChanged(self, sender, e):
        """ OnSysvarWSCurrentChanged(self: WorkspaceCollection, sender: object, e: PropertyChangedEventArgs) """
        pass

    def WorkspaceSaved(self, sender, e):
        """ WorkspaceSaved(self: WorkspaceCollection, sender: object, e: WorkspaceEventArgs) """
        pass

    def WorkspaceSettingsSaved(self, sender, e):
        """ WorkspaceSettingsSaved(self: WorkspaceCollection, sender: object, e: EventArgs) """
        pass

    CurrentWorkspace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentWorkspace(self: WorkspaceCollection) -> RibbonItem

Set: CurrentWorkspace(self: WorkspaceCollection) = value
"""

    IsEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEnabled(self: WorkspaceCollection) -> bool

"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

