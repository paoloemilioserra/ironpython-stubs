# encoding: utf-8
# module Autodesk.AutoCAD.PlottingServices calls itself PlottingServices
# from accoremgd, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AppPlotStatus(Enum):
    """ enum AppPlotStatus, values: DwfFilePlotted (-3), NoPlotYet (-1), PlotHadErrors (3), PlotHadSystemError (4), PlotStart (0), PlotSuccessful (2), PlottingMessage (-2), ViewPlotLog (1) """
    DwfFilePlotted = None
    NoPlotYet = None
    PlotHadErrors = None
    PlotHadSystemError = None
    PlotStart = None
    PlotSuccessful = None
    PlottingMessage = None
    value__ = None
    ViewPlotLog = None


class BeginDocumentEventArgs(EventArgs):
    """ BeginDocumentEventArgs(plotInfo: PlotInfo, documentName: str, copies: int, plotToFile: bool, fileName: str) """
    @staticmethod # known case of __new__
    def __new__(self, plotInfo, documentName, copies, plotToFile, fileName):
        """ __new__(cls: type, plotInfo: PlotInfo, documentName: str, copies: int, plotToFile: bool, fileName: str) """
        pass

    Copies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Copies(self: BeginDocumentEventArgs) -> int

"""

    DocumentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DocumentName(self: BeginDocumentEventArgs) -> str

"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: BeginDocumentEventArgs) -> str

"""

    PlotInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotInfo(self: BeginDocumentEventArgs) -> PlotInfo

"""

    PlotToFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotToFile(self: BeginDocumentEventArgs) -> bool

"""



class BeginDocumentEventHandler(MulticastDelegate):
    """ BeginDocumentEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginDocumentEventHandler, sender: object, e: BeginDocumentEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginDocumentEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginDocumentEventHandler, sender: object, e: BeginDocumentEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginPageEventArgs(EventArgs):
    """ BeginPageEventArgs(plotPageInfo: PlotPageInfo, plotInfo: PlotInfo, lastPage: bool) """
    @staticmethod # known case of __new__
    def __new__(self, plotPageInfo, plotInfo, lastPage):
        """ __new__(cls: type, plotPageInfo: PlotPageInfo, plotInfo: PlotInfo, lastPage: bool) """
        pass

    LastPage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastPage(self: BeginPageEventArgs) -> bool

"""

    PlotInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotInfo(self: BeginPageEventArgs) -> PlotInfo

"""

    PlotPageInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotPageInfo(self: BeginPageEventArgs) -> PlotPageInfo

"""



class BeginPageEventHandler(MulticastDelegate):
    """ BeginPageEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginPageEventHandler, sender: object, e: BeginPageEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginPageEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginPageEventHandler, sender: object, e: BeginPageEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginPlotEventArgs(EventArgs):
    """ BeginPlotEventArgs(progress: PlotProgress, plotType: PlotType) """
    @staticmethod # known case of __new__
    def __new__(self, progress, plotType):
        """ __new__(cls: type, progress: PlotProgress, plotType: PlotType) """
        pass

    PlotProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotProgress(self: BeginPlotEventArgs) -> PlotProgress

"""

    PlotType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotType(self: BeginPlotEventArgs) -> PlotType

"""



class BeginPlotEventHandler(MulticastDelegate):
    """ BeginPlotEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginPlotEventHandler, sender: object, e: BeginPlotEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginPlotEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginPlotEventHandler, sender: object, e: BeginPlotEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class CustomSizeResults(Enum):
    """ enum (flags) CustomSizeResults, values: DeviceLoadFailed (8192), Exception (256), MustCreatePC3 (1), PC3DirReadOnly (4), PC3FileReadOnly (64), PmpDirMissing (16), PmpDirReadOnly (8), PmpFileReadOnly (2048), Possible (0), RotationRequired (2), SizeTooBig (128), UnknownErrPC3File (512), UnknownErrPmpDir (32), UnknownErrPmpFile (1024), WidthAndHeightMustBePositive (4096) """
    DeviceLoadFailed = None
    Exception = None
    MustCreatePC3 = None
    PC3DirReadOnly = None
    PC3FileReadOnly = None
    PmpDirMissing = None
    PmpDirReadOnly = None
    PmpFileReadOnly = None
    Possible = None
    RotationRequired = None
    SizeTooBig = None
    UnknownErrPC3File = None
    UnknownErrPmpDir = None
    UnknownErrPmpFile = None
    value__ = None
    WidthAndHeightMustBePositive = None


class DeviceType(Enum):
    """ enum DeviceType, values: OneOffConfig (2), PC3File (1), SystemPrinter (0), Uninitialized (-1) """
    OneOffConfig = None
    PC3File = None
    SystemPrinter = None
    Uninitialized = None
    value__ = None


class DsdData(RXObject):
    """ DsdData() """
    def Copy(self):
        """ Copy(self: DsdData) -> DsdData """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetDsdEntryCollection(self):
        """ GetDsdEntryCollection(self: DsdData) -> DsdEntryCollection """
        pass

    def ReadDsd(self, fileName):
        """ ReadDsd(self: DsdData, fileName: str) """
        pass

    def SetDsdEntryCollection(self, entries):
        """ SetDsdEntryCollection(self: DsdData, entries: DsdEntryCollection) """
        pass

    def SetUnrecognizedData(self, *__args):
        """ SetUnrecognizedData(self: DsdData, sectionName: str, sectionData: str)SetUnrecognizedData(self: DsdData, sectionNames: StringCollection, sectionData: StringCollection) """
        pass

    def WriteDsd(self, fileName):
        """ WriteDsd(self: DsdData, fileName: str) """
        pass

    CategoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CategoryName(self: DsdData) -> str

Set: CategoryName(self: DsdData) = value
"""

    DestinationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DestinationName(self: DsdData) -> str

Set: DestinationName(self: DsdData) = value
"""

    Dwf3dOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dwf3dOptions(self: DsdData) -> Dwf3dOptions

"""

    IsHomogeneous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHomogeneous(self: DsdData) -> bool

Set: IsHomogeneous(self: DsdData) = value
"""

    IsSheetSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSheetSet(self: DsdData) -> bool

Set: IsSheetSet(self: DsdData) = value
"""

    LogFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogFilePath(self: DsdData) -> str

Set: LogFilePath(self: DsdData) = value
"""

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorVersion(self: DsdData) -> int

Set: MajorVersion(self: DsdData) = value
"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorVersion(self: DsdData) -> int

Set: MinorVersion(self: DsdData) = value
"""

    NoOfCopies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NoOfCopies(self: DsdData) -> int

Set: NoOfCopies(self: DsdData) = value
"""

    Password = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Password(self: DsdData) -> str

Set: Password(self: DsdData) = value
"""

    PlotStampOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotStampOn(self: DsdData) -> bool

Set: PlotStampOn(self: DsdData) = value
"""

    ProjectPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectPath(self: DsdData) -> str

Set: ProjectPath(self: DsdData) = value
"""

    PromptForDwfName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PromptForDwfName(self: DsdData) -> bool

Set: PromptForDwfName(self: DsdData) = value
"""

    SelectionSetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionSetName(self: DsdData) -> str

Set: SelectionSetName(self: DsdData) = value
"""

    SheetSetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetSetName(self: DsdData) -> str

Set: SheetSetName(self: DsdData) = value
"""

    SheetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetType(self: DsdData) -> SheetType

Set: SheetType(self: DsdData) = value
"""

    UnrecognizedDataSectionNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnrecognizedDataSectionNames(self: DsdData) -> StringCollection

"""

    UnrecognizedDataSections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnrecognizedDataSections(self: DsdData) -> StringCollection

"""



class DsdEntry(RXObject):
    """ DsdEntry() """
    def Copy(self):
        """ Copy(self: DsdEntry) -> DsdEntry """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    DwgName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwgName(self: DsdEntry) -> str

Set: DwgName(self: DsdEntry) = value
"""

    Layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layout(self: DsdEntry) -> str

Set: Layout(self: DsdEntry) = value
"""

    Nps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nps(self: DsdEntry) -> str

Set: Nps(self: DsdEntry) = value
"""

    NpsSourceDwg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NpsSourceDwg(self: DsdEntry) -> str

Set: NpsSourceDwg(self: DsdEntry) = value
"""

    OriginalSheetPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalSheetPath(self: DsdEntry) -> str

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: DsdEntry) -> str

Set: Title(self: DsdEntry) = value
"""



class DsdEntryCollection(DisposableWrapper):
    """ DsdEntryCollection() """
    def Add(self, value):
        """ Add(self: DsdEntryCollection, value: DsdEntry) -> int """
        pass

    def Clear(self):
        """ Clear(self: DsdEntryCollection) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: DsdEntryCollection, array: Array[DsdEntry], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DsdEntryCollection) -> IEnumerator """
        pass

    def Insert(self, index, value):
        """ Insert(self: DsdEntryCollection, index: int, value: DsdEntry) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: DsdEntryCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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
    """Get: Count(self: DsdEntryCollection) -> int

"""



class Dwf3dOptions(object):
    # no doc
    GroupByXrefHierarchy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupByXrefHierarchy(self: Dwf3dOptions) -> bool

Set: GroupByXrefHierarchy(self: Dwf3dOptions) = value
"""

    PublishWithMaterials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublishWithMaterials(self: Dwf3dOptions) -> bool

Set: PublishWithMaterials(self: Dwf3dOptions) = value
"""



class EndDocumentEventArgs(EventArgs):
    """ EndDocumentEventArgs(status: PlotCancelStatus) """
    @staticmethod # known case of __new__
    def __new__(self, status):
        """ __new__(cls: type, status: PlotCancelStatus) """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: EndDocumentEventArgs) -> PlotCancelStatus

"""



class EndDocumentEventHandler(MulticastDelegate):
    """ EndDocumentEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: EndDocumentEventHandler, sender: object, e: EndDocumentEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EndDocumentEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: EndDocumentEventHandler, sender: object, e: EndDocumentEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class EndPageEventArgs(EventArgs):
    """ EndPageEventArgs(status: SheetCancelStatus) """
    @staticmethod # known case of __new__
    def __new__(self, status):
        """ __new__(cls: type, status: SheetCancelStatus) """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: EndPageEventArgs) -> SheetCancelStatus

"""



class EndPageEventHandler(MulticastDelegate):
    """ EndPageEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: EndPageEventHandler, sender: object, e: EndPageEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EndPageEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: EndPageEventHandler, sender: object, e: EndPageEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class EndPlotEventArgs(EventArgs):
    """ EndPlotEventArgs(status: PlotCancelStatus) """
    @staticmethod # known case of __new__
    def __new__(self, status):
        """ __new__(cls: type, status: PlotCancelStatus) """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: EndPlotEventArgs) -> PlotCancelStatus

"""



class EndPlotEventHandler(MulticastDelegate):
    """ EndPlotEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: EndPlotEventHandler, sender: object, e: EndPlotEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EndPlotEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: EndPlotEventHandler, sender: object, e: EndPlotEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class HostAppServices(object):
    # no doc
    @staticmethod
    def UpdatePlotJobStatus(status, message):
        """ UpdatePlotJobStatus(status: AppPlotStatus, message: str) """
        pass

    PlotLogger = None


class MatchingPolicy(Enum):
    """ enum MatchingPolicy, values: MatchDisabled (1), MatchEnabled (2), MatchEnabledCustom (3), MatchEnabledTemporaryCustom (4) """
    MatchDisabled = None
    MatchEnabled = None
    MatchEnabledCustom = None
    MatchEnabledTemporaryCustom = None
    value__ = None


class MediaBounds(object):
    """ MediaBounds(pageSize: Point2d, lowerLeftPrintableArea: Point2d, upperRightPrintableArea: Point2d) """
    def Equals(self, obj):
        """ Equals(self: MediaBounds, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MediaBounds) -> int """
        pass

    def IsEqualTo(self, a, tolerance=None):
        """
        IsEqualTo(self: MediaBounds, a: MediaBounds, tolerance: Tolerance) -> bool
        IsEqualTo(self: MediaBounds, a: MediaBounds) -> bool
        """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: MediaBounds, provider: IFormatProvider) -> str
        ToString(self: MediaBounds) -> str
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pageSize, lowerLeftPrintableArea, upperRightPrintableArea):
        """
        __new__[MediaBounds]() -> MediaBounds
        
        __new__(cls: type, pageSize: Point2d, lowerLeftPrintableArea: Point2d, upperRightPrintableArea: Point2d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    LowerLeftPrintableArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerLeftPrintableArea(self: MediaBounds) -> Point2d

Set: LowerLeftPrintableArea(self: MediaBounds) = value
"""

    PageSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageSize(self: MediaBounds) -> Point2d

Set: PageSize(self: MediaBounds) = value
"""

    UpperRightPrintableArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperRightPrintableArea(self: MediaBounds) -> Point2d

Set: UpperRightPrintableArea(self: MediaBounds) = value
"""



class MergeStatus(Enum):
    """ enum (flags) MergeStatus, values: CanonicalMediaName (8), CurrentStyleSheet (524288), DrawViewportsFirst (4194304), NoChanges (0), PlotCentered (1024), PlotConfigurationName (1), PlotHidden (2048), PlotOrigin (16), PlotPaperMargins (2), PlotPaperSize (4), PlotPaperUnits (32), PlotPlotStyles (128), PlotRotation (512), PlotTransparency (8388608), PlotType (32768), PlotViewName (131072), PlotViewportBorders (64), PlotWindowArea (65536), PrintLineWeights (2097152), Scale (262144), ScaleLineWeights (1048576), ShadePlot (4096), ShadePlotCustomDpi (16384), ShadePlotResLevel (8192), ShowPlotStyles (256) """
    CanonicalMediaName = None
    CurrentStyleSheet = None
    DrawViewportsFirst = None
    NoChanges = None
    PlotCentered = None
    PlotConfigurationName = None
    PlotHidden = None
    PlotOrigin = None
    PlotPaperMargins = None
    PlotPaperSize = None
    PlotPaperUnits = None
    PlotPlotStyles = None
    PlotRotation = None
    PlotTransparency = None
    PlotType = None
    PlotViewName = None
    PlotViewportBorders = None
    PlotWindowArea = None
    PrintLineWeights = None
    Scale = None
    ScaleLineWeights = None
    ShadePlot = None
    ShadePlotCustomDpi = None
    ShadePlotResLevel = None
    ShowPlotStyles = None
    value__ = None


class PageCancelledEventHandler(MulticastDelegate):
    """ PageCancelledEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PageCancelledEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PageCancelledEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PageCancelledEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PlotCancelledEventHandler(MulticastDelegate):
    """ PlotCancelledEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PlotCancelledEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PlotCancelledEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PlotCancelledEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PlotCancelStatus(Enum):
    """ enum PlotCancelStatus, values: CanceledByCaller (1), CanceledByCancelAllButton (2), Continue (0) """
    CanceledByCaller = None
    CanceledByCancelAllButton = None
    Continue = None
    value__ = None


class PlotConfig(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetLocalMediaName(self, canonicalMediaName):
        """ GetLocalMediaName(self: PlotConfig, canonicalMediaName: str) -> str """
        pass

    def GetMediaBounds(self, canonicalMediaName):
        """ GetMediaBounds(self: PlotConfig, canonicalMediaName: str) -> MediaBounds """
        pass

    def RefreshMediaNameList(self):
        """ RefreshMediaNameList(self: PlotConfig) """
        pass

    def SaveToPC3(self, name):
        """ SaveToPC3(self: PlotConfig, name: str) """
        pass

    CanonicalMediaNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanonicalMediaNames(self: PlotConfig) -> StringCollection

"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: PlotConfig) -> str

"""

    DefaultFileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultFileExtension(self: PlotConfig) -> str

"""

    DeviceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceName(self: PlotConfig) -> str

"""

    DeviceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceType(self: PlotConfig) -> int

"""

    DriverName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverName(self: PlotConfig) -> str

"""

    FullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullPath(self: PlotConfig) -> str

"""

    IsPlotToFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPlotToFile(self: PlotConfig) -> bool

Set: IsPlotToFile(self: PlotConfig) = value
"""

    LocationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationName(self: PlotConfig) -> str

"""

    MaximumDeviceDotsPerInch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumDeviceDotsPerInch(self: PlotConfig) -> int

"""

    PlotToFileCapability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotToFileCapability(self: PlotConfig) -> PlotToFileCapability

"""

    PortName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PortName(self: PlotConfig) -> str

"""

    ServerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ServerName(self: PlotConfig) -> str

"""

    TagLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagLine(self: PlotConfig) -> str

"""



class PlotConfigInfo(RXObject):
    """ PlotConfigInfo() """
    def Clone(self):
        """ Clone(self: PlotConfigInfo) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    DeviceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceName(self: PlotConfigInfo) -> str

Set: DeviceName(self: PlotConfigInfo) = value
"""

    DeviceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceType(self: PlotConfigInfo) -> DeviceType

Set: DeviceType(self: PlotConfigInfo) = value
"""

    FullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullPath(self: PlotConfigInfo) -> str

Set: FullPath(self: PlotConfigInfo) = value
"""



class PlotConfigInfoCollection(DisposableWrapper):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: PlotConfigInfoCollection, array: Array[PlotConfigInfo], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PlotConfigInfoCollection) -> IEnumerator """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PlotConfigInfoCollection) -> int

"""



class PlotConfigManager(object):
    # no doc
    @staticmethod
    def RefreshList(refreshCode):
        """ RefreshList(refreshCode: RefreshCode) """
        pass

    @staticmethod
    def SetCurrentConfig(deviceName):
        """ SetCurrentConfig(deviceName: str) -> PlotConfig """
        pass

    ColorDependentPlotStyles = None
    Devices = None
    NamedPlotStyles = None


class PlotEngine(DisposableWrapper):
    # no doc
    def BeginDocument(self, plotInfo, documentName, parameters, copies, plotToFile, fileName):
        """ BeginDocument(self: PlotEngine, plotInfo: PlotInfo, documentName: str, parameters: object, copies: int, plotToFile: bool, fileName: str) """
        pass

    def BeginGenerateGraphics(self, parameters):
        """ BeginGenerateGraphics(self: PlotEngine, parameters: object) """
        pass

    def BeginPage(self, pageInfo, plotInfo, lastPage, parameters):
        """ BeginPage(self: PlotEngine, pageInfo: PlotPageInfo, plotInfo: PlotInfo, lastPage: bool, parameters: object) """
        pass

    def BeginPlot(self, plotProgress, parameters):
        """ BeginPlot(self: PlotEngine, plotProgress: PlotProgress, parameters: object) """
        pass

    def Destroy(self):
        """ Destroy(self: PlotEngine) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EndDocument(self, parameters):
        """ EndDocument(self: PlotEngine, parameters: object) """
        pass

    def EndGenerateGraphics(self, parameters):
        """ EndGenerateGraphics(self: PlotEngine, parameters: object) """
        pass

    def EndPage(self, parameters):
        """ EndPage(self: PlotEngine, parameters: object) """
        pass

    def EndPlot(self, parameters):
        """ EndPlot(self: PlotEngine, parameters: object) """
        pass

    IsBackgroundPackaging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBackgroundPackaging(self: PlotEngine) -> bool

"""



class PlotFactory(object):
    # no doc
    @staticmethod
    def CreatePreviewEngine(previewFlags):
        """ CreatePreviewEngine(previewFlags: int) -> PlotEngine """
        pass

    @staticmethod
    def CreatePublishEngine():
        """ CreatePublishEngine() -> PlotEngine """
        pass

    ProcessPlotState = None


class PlotInfo(RXObject):
    """ PlotInfo() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IsCompatibleDocument(self, info):
        """ IsCompatibleDocument(self: PlotInfo, info: PlotInfo) -> bool """
        pass

    DeviceOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceOverride(self: PlotInfo) -> PlotConfig

Set: DeviceOverride(self: PlotInfo) = value
"""

    IsValidated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidated(self: PlotInfo) -> bool

"""

    Layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layout(self: PlotInfo) -> ObjectId

Set: Layout(self: PlotInfo) = value
"""

    MergeStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MergeStatus(self: PlotInfo) -> int

"""

    OverrideSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideSettings(self: PlotInfo) -> PlotSettings

Set: OverrideSettings(self: PlotInfo) = value
"""

    ValidatedConfig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidatedConfig(self: PlotInfo) -> PlotConfig

Set: ValidatedConfig(self: PlotInfo) = value
"""

    ValidatedSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidatedSettings(self: PlotInfo) -> PlotSettings

Set: ValidatedSettings(self: PlotInfo) = value
"""



class PlotInfoValidator(RXObject):
    """ PlotInfoValidator() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IsCustomPossible(self, info):
        """ IsCustomPossible(self: PlotInfoValidator, info: PlotInfo) -> int """
        pass

    def Validate(self, info):
        """ Validate(self: PlotInfoValidator, info: PlotInfo) """
        pass

    DimensionalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionalWeight(self: PlotInfoValidator) -> int

Set: DimensionalWeight(self: PlotInfoValidator) = value
"""

    MediaBoundsWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MediaBoundsWeight(self: PlotInfoValidator) -> int

Set: MediaBoundsWeight(self: PlotInfoValidator) = value
"""

    MediaGroupWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MediaGroupWeight(self: PlotInfoValidator) -> int

Set: MediaGroupWeight(self: PlotInfoValidator) = value
"""

    MediaMatchingPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MediaMatchingPolicy(self: PlotInfoValidator) -> MatchingPolicy

Set: MediaMatchingPolicy(self: PlotInfoValidator) = value
"""

    MediaMatchingThreshold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MediaMatchingThreshold(self: PlotInfoValidator) -> int

Set: MediaMatchingThreshold(self: PlotInfoValidator) = value
"""

    PrintableBoundsWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintableBoundsWeight(self: PlotInfoValidator) -> int

Set: PrintableBoundsWeight(self: PlotInfoValidator) = value
"""

    SheetDimensionalWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetDimensionalWeight(self: PlotInfoValidator) -> int

Set: SheetDimensionalWeight(self: PlotInfoValidator) = value
"""

    SheetMediaGroupWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetMediaGroupWeight(self: PlotInfoValidator) -> int

Set: SheetMediaGroupWeight(self: PlotInfoValidator) = value
"""



class PlotLogger(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EndJob(self):
        """ EndJob(self: PlotLogger) """
        pass

    def EndSheet(self):
        """ EndSheet(self: PlotLogger) """
        pass

    def LogAbortRetryIgnoreError(self, message):
        """ LogAbortRetryIgnoreError(self: PlotLogger, message: str) """
        pass

    def LogError(self, message):
        """ LogError(self: PlotLogger, message: str) """
        pass

    def LogInformation(self, message):
        """ LogInformation(self: PlotLogger, message: str) """
        pass

    def LogMessage(self, message):
        """ LogMessage(self: PlotLogger, message: str) """
        pass

    def LogSevereError(self, message):
        """ LogSevereError(self: PlotLogger, message: str) """
        pass

    def LogTerminalError(self, message):
        """ LogTerminalError(self: PlotLogger, message: str) """
        pass

    def LogWarning(self, message):
        """ LogWarning(self: PlotLogger, message: str) """
        pass

    def StartJob(self):
        """ StartJob(self: PlotLogger) """
        pass

    def StartSheet(self):
        """ StartSheet(self: PlotLogger) """
        pass

    ErrorHasHappenedInJob = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorHasHappenedInJob(self: PlotLogger) -> bool

"""

    ErrorHasHappenedInSheet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorHasHappenedInSheet(self: PlotLogger) -> bool

"""

    WarningHasHappenedInJob = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarningHasHappenedInJob(self: PlotLogger) -> bool

"""

    WarningHasHappenedInSheet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WarningHasHappenedInSheet(self: PlotLogger) -> bool

"""



class PlotMessageIndex(Enum):
    """ enum PlotMessageIndex, values: CancelJobButtonMessage (9), CancelSheetButtonMessage (8), DialogTitle (0), MessageCanceling (6), MessageCancelingCurrent (7), MessageCount (10), SheetName (1), SheetNameToolTip (2), SheetProgressCaption (4), SheetSetProgressCaption (5), Status (3) """
    CancelJobButtonMessage = None
    CancelSheetButtonMessage = None
    DialogTitle = None
    MessageCanceling = None
    MessageCancelingCurrent = None
    MessageCount = None
    SheetName = None
    SheetNameToolTip = None
    SheetProgressCaption = None
    SheetSetProgressCaption = None
    Status = None
    value__ = None


class PlotPageInfo(RXObject):
    """ PlotPageInfo() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    EntityCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityCount(self: PlotPageInfo) -> int

"""

    GradientCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradientCount(self: PlotPageInfo) -> int

"""

    OleObjectCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OleObjectCount(self: PlotPageInfo) -> int

"""

    RasterCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RasterCount(self: PlotPageInfo) -> int

"""

    ShadedViewportType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadedViewportType(self: PlotPageInfo) -> int

"""



class PlotProgress(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Heartbeat(self):
        """ Heartbeat(self: PlotProgress) """
        pass

    IsPlotCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPlotCancelled(self: PlotProgress) -> bool

"""

    IsSheetCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSheetCancelled(self: PlotProgress) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: PlotProgress) -> bool

Set: IsVisible(self: PlotProgress) = value
"""

    LowerPlotProgressRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerPlotProgressRange(self: PlotProgress) -> int

Set: LowerPlotProgressRange(self: PlotProgress) = value
"""

    LowerSheetProgressRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerSheetProgressRange(self: PlotProgress) -> int

Set: LowerSheetProgressRange(self: PlotProgress) = value
"""

    PlotCancelStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotCancelStatus(self: PlotProgress) -> PlotCancelStatus

Set: PlotCancelStatus(self: PlotProgress) = value
"""

    PlotProgressPos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotProgressPos(self: PlotProgress) -> int

Set: PlotProgressPos(self: PlotProgress) = value
"""

    SheetCancelStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetCancelStatus(self: PlotProgress) -> SheetCancelStatus

Set: SheetCancelStatus(self: PlotProgress) = value
"""

    SheetProgressPos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetProgressPos(self: PlotProgress) -> int

Set: SheetProgressPos(self: PlotProgress) = value
"""

    StatusMsgString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StatusMsgString(self: PlotProgress) -> str

Set: StatusMsgString(self: PlotProgress) = value
"""

    UpperPlotProgressRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperPlotProgressRange(self: PlotProgress) -> int

Set: UpperPlotProgressRange(self: PlotProgress) = value
"""

    UpperSheetProgressRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperSheetProgressRange(self: PlotProgress) -> int

Set: UpperSheetProgressRange(self: PlotProgress) = value
"""



class PlotProgressDialog(PlotProgress):
    """ PlotProgressDialog(isPreview: bool, sheetCount: int, showCancelSheetButton: bool) """
    def Destroy(self):
        """ Destroy(self: PlotProgressDialog) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def OnBeginPlot(self):
        """ OnBeginPlot(self: PlotProgressDialog) """
        pass

    def OnBeginSheet(self):
        """ OnBeginSheet(self: PlotProgressDialog) """
        pass

    def OnEndPlot(self):
        """ OnEndPlot(self: PlotProgressDialog) """
        pass

    def OnEndSheet(self):
        """ OnEndSheet(self: PlotProgressDialog) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, isPreview, sheetCount, showCancelSheetButton):
        """ __new__(cls: type, isPreview: bool, sheetCount: int, showCancelSheetButton: bool) """
        pass

    IsSingleSheetPlot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSingleSheetPlot(self: PlotProgressDialog) -> bool

"""



class PlotReactorManager(object):
    """ PlotReactorManager() """
    def raise_BeginDocument(self, *args): #cannot find CLR method
        """ raise_BeginDocument(self: PlotReactorManager, sender: object, arguments: BeginDocumentEventArgs) """
        pass

    def raise_BeginPage(self, *args): #cannot find CLR method
        """ raise_BeginPage(self: PlotReactorManager, sender: object, arguments: BeginPageEventArgs) """
        pass

    def raise_BeginPlot(self, *args): #cannot find CLR method
        """ raise_BeginPlot(self: PlotReactorManager, sender: object, arguments: BeginPlotEventArgs) """
        pass

    def raise_EndDocument(self, *args): #cannot find CLR method
        """ raise_EndDocument(self: PlotReactorManager, sender: object, arguments: EndDocumentEventArgs) """
        pass

    def raise_EndPage(self, *args): #cannot find CLR method
        """ raise_EndPage(self: PlotReactorManager, sender: object, arguments: EndPageEventArgs) """
        pass

    def raise_EndPlot(self, *args): #cannot find CLR method
        """ raise_EndPlot(self: PlotReactorManager, sender: object, arguments: EndPlotEventArgs) """
        pass

    def raise_PageCancelled(self, *args): #cannot find CLR method
        """ raise_PageCancelled(self: PlotReactorManager, sender: object, arguments: EventArgs) """
        pass

    def raise_PlotCancelled(self, *args): #cannot find CLR method
        """ raise_PlotCancelled(self: PlotReactorManager, sender: object, arguments: EventArgs) """
        pass

    BeginDocument = None
    BeginPage = None
    BeginPlot = None
    EndDocument = None
    EndPage = None
    EndPlot = None
    PageCancelled = None
    PlotCancelled = None


class PlotToFileCapability(Enum):
    """ enum PlotToFileCapability, values: MustPlotToFile (2), NoPlotToFile (0), PlotToFileAllowed (1) """
    MustPlotToFile = None
    NoPlotToFile = None
    PlotToFileAllowed = None
    value__ = None


class PlotType(Enum):
    """ enum PlotType, values: BackgroundPackaging (2), BackgroundPlot (3), Plot (0), Preview (1) """
    BackgroundPackaging = None
    BackgroundPlot = None
    Plot = None
    Preview = None
    value__ = None


class PreviewEndPlotInfo(DisposableWrapper):
    """ PreviewEndPlotInfo() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: PreviewEndPlotInfo) -> PreviewEndPlotStatus

"""



class PreviewEndPlotStatus(Enum):
    """ enum PreviewEndPlotStatus, values: Cancel (2), Next (3), Normal (0), Plot (1), Previous (4) """
    Cancel = None
    Next = None
    Normal = None
    Plot = None
    Previous = None
    value__ = None


class PreviewEngineFlags(Enum):
    """ enum (flags) PreviewEngineFlags, values: NextSheet (2), Plot (1), PreviousSheet (4) """
    NextSheet = None
    Plot = None
    PreviousSheet = None
    value__ = None


class ProcessPlotState(Enum):
    """ enum ProcessPlotState, values: BackgroundPlotting (2), ForegroundPlotting (1), NotPlotting (0) """
    BackgroundPlotting = None
    ForegroundPlotting = None
    NotPlotting = None
    value__ = None


class RefreshCode(Enum):
    """ enum RefreshCode, values: All (0), RefreshDevicesList (1), RefreshPC3DevicesList (4), RefreshStyleList (2), RefreshSystemDevicesList (3) """
    All = None
    RefreshDevicesList = None
    RefreshPC3DevicesList = None
    RefreshStyleList = None
    RefreshSystemDevicesList = None
    value__ = None


class SheetCancelStatus(Enum):
    """ enum SheetCancelStatus, values: CanceledByCaller (3), CanceledByCancelAllButton (2), CanceledByCancelButton (1), Continue (0) """
    CanceledByCaller = None
    CanceledByCancelAllButton = None
    CanceledByCancelButton = None
    Continue = None
    value__ = None


class SheetType(Enum):
    """ enum SheetType, values: MultiDwf (1), MultiDwfx (4), MultiPdf (6), OriginalDevice (2), SingleDwf (0), SingleDwfx (3), SinglePdf (5) """
    MultiDwf = None
    MultiDwfx = None
    MultiPdf = None
    OriginalDevice = None
    SingleDwf = None
    SingleDwfx = None
    SinglePdf = None
    value__ = None


class StdConfiguration(Enum):
    """ enum StdConfiguration, values: DefaultWindowsSysPrinter (1), Dwf6ePlot (2), DwfEplotOptForPlotting (3), DwfEplotOptForViewing (4), DWFxePlot (8), NoneDevice (0), PublishToWebDwf (5), PublishToWebDWFx (9), PublishToWebJpg (6), PublishToWebPng (7) """
    DefaultWindowsSysPrinter = None
    Dwf6ePlot = None
    DwfEplotOptForPlotting = None
    DwfEplotOptForViewing = None
    DWFxePlot = None
    NoneDevice = None
    PublishToWebDwf = None
    PublishToWebDWFx = None
    PublishToWebJpg = None
    PublishToWebPng = None
    value__ = None


