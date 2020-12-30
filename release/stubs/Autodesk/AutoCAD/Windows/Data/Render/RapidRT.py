# encoding: utf-8
# module Autodesk.AutoCAD.Windows.Data.Render.RapidRT calls itself RapidRT
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class RenderData(object):
    """ RenderData(A_0: Document) """
    def Dispose(self):
        """ Dispose(self: RenderData) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: RenderData, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def ReRender(self):
        """ ReRender(self: RenderData) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0):
        """ __new__(cls: type, A_0: Document) """
        pass

    AbortFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbortFlag(self: RenderData) -> bool

Set: AbortFlag(self: RenderData) = value
"""

    CurrentTileIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentTileIndex(self: RenderData) -> int

Set: CurrentTileIndex(self: RenderData) = value
"""

    IsIndeterminate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIndeterminate(self: RenderData) -> bool

"""

    IsRendering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRendering(self: RenderData) -> bool

"""

    IsRenderOK = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRenderOK(self: RenderData) -> bool

Set: IsRenderOK(self: RenderData) = value
"""

    IsViewportRender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsViewportRender(self: RenderData) -> bool

"""

    JobIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobIndex(self: RenderData) -> Nullable[int]

Set: JobIndex(self: RenderData) = value
"""

    LevelProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LevelProgress(self: RenderData) -> Single

Set: LevelProgress(self: RenderData) = value
"""

    OutputFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputFileName(self: RenderData) -> str

Set: OutputFileName(self: RenderData) = value
"""

    OutputImageFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputImageFormat(self: RenderData) -> str

Set: OutputImageFormat(self: RenderData) = value
"""

    OutputResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputResolution(self: RenderData) -> str

Set: OutputResolution(self: RenderData) = value
"""

    OutputSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputSize(self: RenderData) -> str

"""

    OutputView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputView(self: RenderData) -> str

"""

    OverallProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverallProgress(self: RenderData) -> Single

Set: OverallProgress(self: RenderData) = value
"""

    OwningDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OwningDocument(self: RenderData) -> Document

"""

    RenderLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderLevel(self: RenderData) -> int

Set: RenderLevel(self: RenderData) = value
"""

    RenderPreset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderPreset(self: RenderData) -> str

"""

    RenderStatistics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderStatistics(self: RenderData) -> str

Set: RenderStatistics(self: RenderData) = value
"""

    RenderTileImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderTileImage(self: RenderData) -> RenderImage

Set: RenderTileImage(self: RenderData) = value
"""

    RenderTime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderTime(self: RenderData) -> int

Set: RenderTime(self: RenderData) = value
"""


    PropertyChanged = None


class RenderDataSet(object):
    """ RenderDataSet() """
    def Dispose(self):
        """ Dispose(self: RenderDataSet) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: RenderDataSet, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CurrentRenderData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentRenderData(self: RenderDataSet) -> RenderData

Set: CurrentRenderData(self: RenderDataSet) = value
"""

    Reactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reactor(self: RenderDataSet) -> RenderDataReactorImp*

Set: Reactor(self: RenderDataSet) = value
"""

    RenderJobs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderJobs(self: RenderDataSet) -> ObservableCollection[RenderData]

Set: RenderJobs(self: RenderDataSet) = value
"""


    PropertyChanged = None


class RenderEngine(object):
    """ RenderEngine() """
    def Dispose(self):
        """ Dispose(self: RenderEngine) """
        pass

    def MakeRenderJobSettingsCurrent(self, doc, jobIndex):
        """ MakeRenderJobSettingsCurrent(self: RenderEngine, doc: Document, jobIndex: int) """
        pass

    def NotifyRenderEnd(self, doc):
        """ NotifyRenderEnd(self: RenderEngine, doc: Document) """
        pass

    def NotifyRenderStart(self, doc, jobIndex):
        """ NotifyRenderStart(self: RenderEngine, doc: Document, jobIndex: int) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: RenderEngine, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def RegisterDocument(self, doc):
        """ RegisterDocument(self: RenderEngine, doc: Document) """
        pass

    def UnregisterDocument(self, doc):
        """ UnregisterDocument(self: RenderEngine, doc: Document) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CurrentOutputFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentOutputFile(self: RenderEngine) -> str

Set: CurrentOutputFile(self: RenderEngine) = value
"""

    CurrentOutputSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentOutputSize(self: RenderEngine) -> str

Set: CurrentOutputSize(self: RenderEngine) = value
"""

    CurrentRenderData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentRenderData(self: RenderEngine) -> RenderData

"""

    CurrentRenderEnvironment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentRenderEnvironment(self: RenderEngine) -> RenderEnvironment

"""

    CurrentRenderExposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentRenderExposure(self: RenderEngine) -> RenderExposure

"""

    IsRendering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRendering(self: RenderEngine) -> bool

"""

    IsViewportChanging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsViewportChanging(self: RenderEngine) -> bool

Set: IsViewportChanging(self: RenderEngine) = value
"""

    OutputSaveEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputSaveEnabled(self: RenderEngine) -> bool

Set: OutputSaveEnabled(self: RenderEngine) = value
"""

    RenderDataMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderDataMap(self: RenderEngine) -> Dictionary[Document, RenderDataSet]

"""

    RenderDestination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderDestination(self: RenderEngine) -> int

Set: RenderDestination(self: RenderEngine) = value
"""

    SkipGlobalUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SkipGlobalUpdate(self: RenderEngine) -> bool

Set: SkipGlobalUpdate(self: RenderEngine) = value
"""


    PropertyChanged = None


class RenderEnvironment(object):
    """ RenderEnvironment() """
    def Dispose(self):
        """ Dispose(self: RenderEnvironment) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: RenderEnvironment, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def SuppressDatabaseUpdate(self, newValue):
        """ SuppressDatabaseUpdate(self: RenderEnvironment, newValue: bool) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Brightness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brightness(self: RenderEnvironment) -> Nullable[float]

Set: Brightness(self: RenderEnvironment) = value
"""

    DisplayImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayImage(self: RenderEnvironment) -> bool

Set: DisplayImage(self: RenderEnvironment) = value
"""

    Enable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enable(self: RenderEnvironment) -> bool

Set: Enable(self: RenderEnvironment) = value
"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: RenderEnvironment) -> Nullable[float]

Set: Exposure(self: RenderEnvironment) = value
"""

    IBLImageName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IBLImageName(self: RenderEnvironment) -> str

Set: IBLImageName(self: RenderEnvironment) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: RenderEnvironment) -> float

Set: Rotation(self: RenderEnvironment) = value
"""

    WhitePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WhitePoint(self: RenderEnvironment) -> Nullable[float]

Set: WhitePoint(self: RenderEnvironment) = value
"""


    PropertyChanged = None


class RenderExposure(object):
    """ RenderExposure() """
    def Dispose(self):
        """ Dispose(self: RenderExposure) """
        pass

    def InvalidateUI(self):
        """ InvalidateUI(self: RenderExposure) """
        pass

    def raise_PropertyChanged(self, *args): #cannot find CLR method
        """ raise_PropertyChanged(self: RenderExposure, value0: object, value1: PropertyChangedEventArgs) """
        pass

    def ResetDefault(self):
        """ ResetDefault(self: RenderExposure) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: RenderExposure) -> bool

Set: Active(self: RenderExposure) = value
"""

    Exposure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Exposure(self: RenderExposure) -> float

Set: Exposure(self: RenderExposure) = value
"""

    IBLActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IBLActive(self: RenderExposure) -> bool

Set: IBLActive(self: RenderExposure) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RenderExposure) -> ExposureType

"""

    WhitePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WhitePoint(self: RenderExposure) -> float

Set: WhitePoint(self: RenderExposure) = value
"""


    ExposureType = None
    PropertyChanged = None


class RenderImage(object):
    """ RenderImage() """
    def Dispose(self):
        """ Dispose(self: RenderImage) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: RenderImage) -> int

Set: Height(self: RenderImage) = value
"""

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Image(self: RenderImage) -> Bitmap

Set: Image(self: RenderImage) = value
"""

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Left(self: RenderImage) -> int

Set: Left(self: RenderImage) = value
"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Top(self: RenderImage) -> int

Set: Top(self: RenderImage) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: RenderImage) -> int

Set: Width(self: RenderImage) = value
"""



