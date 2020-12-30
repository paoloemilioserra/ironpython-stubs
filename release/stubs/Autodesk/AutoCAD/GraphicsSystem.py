# encoding: utf-8
# module Autodesk.AutoCAD.GraphicsSystem calls itself GraphicsSystem
# from Acdbmgd, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null, accoremgd, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CertificationData(object):
    """ CertificationData() """
    CardName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CardName(self: CertificationData) -> str

Set: CardName(self: CertificationData) = value
"""

    CertificationStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CertificationStatus(self: CertificationData) -> int

Set: CertificationStatus(self: CertificationData) = value
"""

    DriverVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverVersion(self: CertificationData) -> str

Set: DriverVersion(self: CertificationData) = value
"""

    FailedDevices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FailedDevices(self: CertificationData) -> str

Set: FailedDevices(self: CertificationData) = value
"""

    HardwareFeatureLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardwareFeatureLevel(self: CertificationData) -> int

Set: HardwareFeatureLevel(self: CertificationData) = value
"""

    HardwareID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardwareID(self: CertificationData) -> int

Set: HardwareID(self: CertificationData) = value
"""

    ProductDriverURL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProductDriverURL(self: CertificationData) -> str

Set: ProductDriverURL(self: CertificationData) = value
"""

    SoftwareFeatureLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SoftwareFeatureLevel(self: CertificationData) -> int

Set: SoftwareFeatureLevel(self: CertificationData) = value
"""

    TuningDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TuningDate(self: CertificationData) -> str

Set: TuningDate(self: CertificationData) = value
"""



class ClientViewInfo(object):
    """ ClientViewInfo() """
    AcadWindowId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AcadWindowId(self: ClientViewInfo) -> int

Set: AcadWindowId(self: ClientViewInfo) = value
"""

    ViewportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportId(self: ClientViewInfo) -> int

Set: ViewportId(self: ClientViewInfo) = value
"""

    ViewportObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportObjectId(self: ClientViewInfo) -> int

Set: ViewportObjectId(self: ClientViewInfo) = value
"""



class Configuration(DisposableWrapper):
    """ Configuration() """
    def Configure(self):
        """ Configure(self: Configuration) -> bool """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> Configuration """
        pass

    def DegradationChainPosition(self, channel):
        """ DegradationChainPosition(self: Configuration, channel: DegradationChannel) -> int """
        pass

    def DegradationChannelAt(self, order):
        """ DegradationChannelAt(self: Configuration, order: int) -> DegradationChannel """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetCanDegradeChannel(self, channel):
        """ GetCanDegradeChannel(self: Configuration, channel: DegradationChannel) -> bool """
        pass

    def GetCertificationData(self):
        """ GetCertificationData(self: Configuration) -> CertificationData """
        pass

    def GetEffectList(self, type):
        """ GetEffectList(self: Configuration, type: EffectListType) -> List[EffectStatus] """
        pass

    def GetFeatureAvailableVal(self, feature):
        """ GetFeatureAvailableVal(self: Configuration, feature: UniqueString) -> int """
        pass

    def GetFeatureRecommendedVal(self, feature):
        """ GetFeatureRecommendedVal(self: Configuration, feature: UniqueString) -> int """
        pass

    def GetFeatureUsedVal(self, feature):
        """ GetFeatureUsedVal(self: Configuration, feature: UniqueString) -> int """
        pass

    def GetHardwareAcceleratedDrivers(self):
        """ GetHardwareAcceleratedDrivers(self: Configuration) -> Array[DriverInfo] """
        pass

    def GetVirtualDeviceName(self):
        """ GetVirtualDeviceName(self: Configuration) -> str """
        pass

    def IsFeatureAvailable(self, feature):
        """ IsFeatureAvailable(self: Configuration, feature: UniqueString) -> bool """
        pass

    def IsFeatureEnabled(self, feature):
        """ IsFeatureEnabled(self: Configuration, feature: UniqueString) -> bool """
        pass

    def IsFeatureRecommended(self, feature):
        """ IsFeatureRecommended(self: Configuration, feature: UniqueString) -> bool """
        pass

    def IsHardwareAccelerationAvailable(self):
        """ IsHardwareAccelerationAvailable(self: Configuration) -> bool """
        pass

    def IsHardwareAccelerationEnabled(self):
        """ IsHardwareAccelerationEnabled(self: Configuration) -> bool """
        pass

    def IsHardwareAccelerationRecommended(self):
        """ IsHardwareAccelerationRecommended(self: Configuration) -> bool """
        pass

    def IsNoHardwareOverrideEnabled(self):
        """ IsNoHardwareOverrideEnabled(self: Configuration) -> bool """
        pass

    def SetCanDegradeChannel(self, channel, degrade):
        """ SetCanDegradeChannel(self: Configuration, channel: DegradationChannel, degrade: bool) """
        pass

    def SetFeatureEnabled(self, feature, enable):
        """ SetFeatureEnabled(self: Configuration, feature: UniqueString, enable: bool) """
        pass

    def SetFeatureUsedVal(self, feature, value):
        """ SetFeatureUsedVal(self: Configuration, feature: UniqueString, value: int) """
        pass

    def setHardwareAcceleration(self, bEnable):
        """ setHardwareAcceleration(self: Configuration, bEnable: bool) """
        pass

    def ShiftDegradationChainPosition(self, channel, shiftDown):
        """ ShiftDegradationChainPosition(self: Configuration, channel: DegradationChannel, shiftDown: bool) """
        pass

    def ShowConfigDialog(self, dlgType):
        """ ShowConfigDialog(self: Configuration, dlgType: str) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AdaptiveDegradation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdaptiveDegradation(self: Configuration) -> bool

Set: AdaptiveDegradation(self: Configuration) = value
"""

    CurrentDisplayDriver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDisplayDriver(self: Configuration) -> DriverInfo

"""

    CurveTessellationTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveTessellationTolerance(self: Configuration) -> int

Set: CurveTessellationTolerance(self: Configuration) = value
"""

    DefaultHardwareAcceleratedDriver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultHardwareAcceleratedDriver(self: Configuration) -> DriverInfo

"""

    DiscardBackFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiscardBackFaces(self: Configuration) -> bool

Set: DiscardBackFaces(self: Configuration) = value
"""

    DriverName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverName(self: Configuration) -> str

"""

    DriverRevision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverRevision(self: Configuration) -> int

"""

    DriverSearchPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverSearchPath(self: Configuration) -> str

Set: DriverSearchPath(self: Configuration) = value
"""

    DriverVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriverVersion(self: Configuration) -> int

"""

    DynamicTessellation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DynamicTessellation(self: Configuration) -> bool

Set: DynamicTessellation(self: Configuration) = value
"""

    FrameRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRate(self: Configuration) -> int

Set: FrameRate(self: Configuration) = value
"""

    GenerateVertexNormals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GenerateVertexNormals(self: Configuration) -> bool

Set: GenerateVertexNormals(self: Configuration) = value
"""

    Handedness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handedness(self: Configuration) -> Handedness

Set: Handedness(self: Configuration) = value
"""

    HardwareAcceleratedDriver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardwareAcceleratedDriver(self: Configuration) -> DriverInfo

Set: HardwareAcceleratedDriver(self: Configuration) = value
"""

    MaxLODs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxLODs(self: Configuration) -> int

Set: MaxLODs(self: Configuration) = value
"""

    RedrawOnWindowExpose = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RedrawOnWindowExpose(self: Configuration) -> bool

Set: RedrawOnWindowExpose(self: Configuration) = value
"""

    SurfaceTessellationTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceTessellationTolerance(self: Configuration) -> int

Set: SurfaceTessellationTolerance(self: Configuration) = value
"""

    Transparency = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transparency(self: Configuration) -> Quality

Set: Transparency(self: Configuration) = value
"""



class ConfigWasModifiedEventHandler(MulticastDelegate):
    """ ConfigWasModifiedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ConfigWasModifiedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ConfigWasModifiedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ConfigWasModifiedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DefaultLightingType(Enum):
    """ enum DefaultLightingType, values: OneLight (0), TwoLights (1) """
    OneLight = None
    TwoLights = None
    value__ = None


class DegradationChannel(Enum):
    """ enum DegradationChannel, values: Backgrounds (14), DegradationChannels (18), DiscardBackfaces (6), EdgeStyles (8), Faceted (16), FacetEdges (9), FastSilhouette (10), IntersectEdges (15), Lighting (2), LightingQuality (13), LineAntialias (1), Materials (12), ShadowsFull (4), ShadowsGround (7), Textures (11), Transparency (5), TransparencyQuality (3), ViewportDraw (0), Wireframe (17) """
    Backgrounds = None
    DegradationChannels = None
    DiscardBackfaces = None
    EdgeStyles = None
    Faceted = None
    FacetEdges = None
    FastSilhouette = None
    IntersectEdges = None
    Lighting = None
    LightingQuality = None
    LineAntialias = None
    Materials = None
    ShadowsFull = None
    ShadowsGround = None
    Textures = None
    Transparency = None
    TransparencyQuality = None
    value__ = None
    ViewportDraw = None
    Wireframe = None


class Device(DisposableWrapper):
    """
    Device(hwnd: IntPtr, deviceType: DeviceType)
    Device(hwnd: IntPtr)
    Device()
    """
    def Add(self, view):
        """ Add(self: Device, view: View) -> bool """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete, graphicsKernelPointer=None):
        """
        Create(unmanagedPointer: IntPtr, autoDelete: bool) -> Device
        Create(unmanagedPointer: IntPtr, autoDelete: bool, graphicsKernelPointer: IntPtr) -> Device
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Erase(self, view):
        """ Erase(self: Device, view: View) -> bool """
        pass

    def EraseAll(self):
        """ EraseAll(self: Device) """
        pass

    def GetSnapshot(self, rectangle):
        """ GetSnapshot(self: Device, rectangle: Rectangle) -> Bitmap """
        pass

    def Invalidate(self, rect=None):
        """ Invalidate(self: Device)Invalidate(self: Device, rect: Rectangle) """
        pass

    def OnDisplayChange(self, bitsPerPixel, xRes, yRes):
        """ OnDisplayChange(self: Device, bitsPerPixel: int, xRes: int, yRes: int) """
        pass

    def OnRealizeBackgroundPalette(self):
        """ OnRealizeBackgroundPalette(self: Device) """
        pass

    def OnRealizeForegroundPalette(self):
        """ OnRealizeForegroundPalette(self: Device) """
        pass

    def OnSize(self, size):
        """ OnSize(self: Device, size: Size) """
        pass

    def SetLogicalPalette(self, palette):
        """ SetLogicalPalette(self: Device, palette: Array[Color]) """
        pass

    def SetPhysicalPalette(self, palette):
        """ SetPhysicalPalette(self: Device, palette: Array[Color]) """
        pass

    def Update(self, updatedRect=None):
        """ Update(self: Device)Update(self: Device, updatedRect: Rectangle) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, hwnd=None, deviceType=None):
        """
        __new__(cls: type, hwnd: IntPtr, deviceType: DeviceType)
        __new__(cls: type, hwnd: IntPtr)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: Device) -> Color

Set: BackgroundColor(self: Device) = value
"""

    DeviceRenderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceRenderType(self: Device) -> RendererType

Set: DeviceRenderType(self: Device) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Device) -> bool

"""



class DeviceType(Enum):
    """ enum DeviceType, values: OffScreenDevice (1), ScreenDevice (0), SelectionDevice (2) """
    OffScreenDevice = None
    ScreenDevice = None
    SelectionDevice = None
    value__ = None


class DriverInfo(object):
    """
    DriverInfo(hardwareAccelerated: bool, path: str, driver: str)
    DriverInfo(path: str, driver: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[DriverInfo]() -> DriverInfo
        
        __new__(cls: type, hardwareAccelerated: bool, path: str, driver: str)
        __new__(cls: type, path: str, driver: str)
        """
        pass

    Driver = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Driver(self: DriverInfo) -> str

"""

    HardwareAccelerated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardwareAccelerated(self: DriverInfo) -> bool

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: DriverInfo) -> str

"""



class EffectListType(Enum):
    """ enum EffectListType, values: kEL_Current (0), kEL_File (3), kEL_HardwareAdvanced (6), kEL_HardwareBasic (4), kEL_HardwareMedium (5), kEL_RegistryHardware (1), kEL_RegistrySoftware (2) """
    kEL_Current = None
    kEL_File = None
    kEL_HardwareAdvanced = None
    kEL_HardwareBasic = None
    kEL_HardwareMedium = None
    kEL_RegistryHardware = None
    kEL_RegistrySoftware = None
    value__ = None


class EffectStatus(object):
    """ EffectStatus() """
    def raise_EffectOnChanged(self, *args): #cannot find CLR method
        """ raise_EffectOnChanged(self: EffectStatus, value0: object, value1: EventArgs) """
        pass

    Available = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Available(self: EffectStatus) -> int

Set: Available(self: EffectStatus) = value
"""

    EffectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectName(self: EffectStatus) -> str

Set: EffectName(self: EffectStatus) = value
"""

    EffectUniqueString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectUniqueString(self: EffectStatus) -> UniqueString

Set: EffectUniqueString(self: EffectStatus) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: EffectStatus) -> int

Set: Enabled(self: EffectStatus) = value
"""

    FeatureLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLevel(self: EffectStatus) -> int

Set: FeatureLevel(self: EffectStatus) = value
"""

    Recommended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Recommended(self: EffectStatus) -> int

Set: Recommended(self: EffectStatus) = value
"""


    EffectOnChanged = None


class ErrorStatus(Enum):
    """ enum ErrorStatus, values: InvalidInput (2), OutOfRange (1), Success (0) """
    InvalidInput = None
    OutOfRange = None
    Success = None
    value__ = None


class GetInterfaceFunction(MulticastDelegate):
    """ GetInterfaceFunction(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, objectId, bNeedsValidation, callback, obj):
        """ BeginInvoke(self: GetInterfaceFunction, objectId: int, bNeedsValidation: bool, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GetInterfaceFunction, result: IAsyncResult) -> Drawable """
        pass

    def Invoke(self, objectId, bNeedsValidation):
        """ Invoke(self: GetInterfaceFunction, objectId: int, bNeedsValidation: bool) -> Drawable """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class GraphicsKernel(DisposableWrapper):
    """
    GraphicsKernel(unmanagedPointer: IntPtr)
    GraphicsKernel()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: GraphicsKernel) -> AcGiGraphicsKernel* """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedPointer=None):
        """
        __new__(cls: type, unmanagedPointer: IntPtr)
        __new__(cls: type)
        """
        pass


class GsToBeUnloadedEventHandler(MulticastDelegate):
    """ GsToBeUnloadedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: GsToBeUnloadedEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GsToBeUnloadedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: GsToBeUnloadedEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class Handedness(Enum):
    """ enum Handedness, values: Left (0), Right (1) """
    Left = None
    Right = None
    value__ = None


class HighlightStyle(Enum):
    """ enum HighlightStyle, values: HighlightDashed (0) """
    HighlightDashed = None
    value__ = None


class InvalidationHint(Enum):
    """ enum InvalidationHint, values: InvalidateAll (3), InvalidateAllStatic (4), InvalidateFacets (5), InvalidateFills (6), InvalidateIsolines (1), InvalidateLinetypes (7), InvalidateMaterials (8), InvalidateNone (0), InvalidateViewportCache (2) """
    InvalidateAll = None
    InvalidateAllStatic = None
    InvalidateFacets = None
    InvalidateFills = None
    InvalidateIsolines = None
    InvalidateLinetypes = None
    InvalidateMaterials = None
    InvalidateNone = None
    InvalidateViewportCache = None
    value__ = None


class KernelDescriptor(DisposableWrapper):
    """ KernelDescriptor() """
    def addRequirement(self, capability):
        """ addRequirement(self: KernelDescriptor, capability: UniqueString) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: KernelDescriptor) -> AcGiKernelDescriptor* """
        pass

    def supports(self, capability):
        """ supports(self: KernelDescriptor, capability: UniqueString) -> bool """
        pass

    Drawing2D = None
    Drawing3D = None
    RapidRTRendering3D = None
    Selection3D = None


class LinePattern(Enum):
    """ enum LinePattern, values: DashDot (3), Dashed (1), DefaultLinePattern (2), Dotted (2), DoubleLongDash (9), DoubleMediumDash (8), DoubleShortDash (7), LongDash (6), LongDashDot (14), LongDashDotDot (13), LongDashShortDash (12), MediumDash (5), MediumDashDotShortDashDot (15), MediumDashShortDashShortDash (11), MediumLongDash (10), ShortDash (4), Solid (0), SparseDot (16) """
    DashDot = None
    Dashed = None
    DefaultLinePattern = None
    Dotted = None
    DoubleLongDash = None
    DoubleMediumDash = None
    DoubleShortDash = None
    LongDash = None
    LongDashDot = None
    LongDashDotDot = None
    LongDashShortDash = None
    MediumDash = None
    MediumDashDotShortDashDot = None
    MediumDashShortDashShortDash = None
    MediumLongDash = None
    ShortDash = None
    Solid = None
    SparseDot = None
    value__ = None


class LineWeight(Enum):
    """ enum LineWeight, values: kLnWt000 (0), kLnWt005 (5), kLnWt009 (9), kLnWt013 (13), kLnWt015 (15), kLnWt018 (18), kLnWt020 (20), kLnWt025 (25), kLnWt030 (30), kLnWt035 (35), kLnWt040 (40), kLnWt050 (50), kLnWt053 (53), kLnWt060 (60), kLnWt070 (70), kLnWt080 (80), kLnWt090 (90), kLnWt100 (100), kLnWt106 (106), kLnWt120 (120), kLnWt140 (140), kLnWt158 (158), kLnWt200 (200), kLnWt211 (211), kLnWtByBlock (-2), kLnWtByLayer (-1), kLnWtByLwDefault (-3) """
    kLnWt000 = None
    kLnWt005 = None
    kLnWt009 = None
    kLnWt013 = None
    kLnWt015 = None
    kLnWt018 = None
    kLnWt020 = None
    kLnWt025 = None
    kLnWt030 = None
    kLnWt035 = None
    kLnWt040 = None
    kLnWt050 = None
    kLnWt053 = None
    kLnWt060 = None
    kLnWt070 = None
    kLnWt080 = None
    kLnWt090 = None
    kLnWt100 = None
    kLnWt106 = None
    kLnWt120 = None
    kLnWt140 = None
    kLnWt158 = None
    kLnWt200 = None
    kLnWt211 = None
    kLnWtByBlock = None
    kLnWtByLayer = None
    kLnWtByLwDefault = None
    value__ = None


class Manager(DisposableWrapper):
    # no doc
    @staticmethod
    def AcquireGraphicsKernel(desc):
        """ AcquireGraphicsKernel(desc: KernelDescriptor) -> GraphicsKernel """
        pass

    def CreateAutoCADDevice(self, __unnamed000, hwnd):
        """ CreateAutoCADDevice(self: Manager, __unnamed000: GraphicsKernel, hwnd: IntPtr) -> Device """
        pass

    def CreateAutoCADModel(self, A_0):
        """ CreateAutoCADModel(self: Manager, A_0: GraphicsKernel) -> Model """
        pass

    def CreateAutoCADOffScreenDevice(self, A_0):
        """ CreateAutoCADOffScreenDevice(self: Manager, A_0: GraphicsKernel) -> Device """
        pass

    def CreateAutoCADView(self, __unnamed000, drawable):
        """ CreateAutoCADView(self: Manager, __unnamed000: GraphicsKernel, drawable: Drawable) -> View """
        pass

    def CreateAutoCADViewport(self, __unnamed000, vp):
        """ CreateAutoCADViewport(self: Manager, __unnamed000: GraphicsKernel, vp: ViewportTableRecord) -> View """
        pass

    def CreateView(self, A_0):
        """ CreateView(self: Manager, A_0: Device) -> View """
        pass

    def CreateViewport(self, __unnamed000, vp):
        """ CreateViewport(self: Manager, __unnamed000: Device, vp: ViewportTableRecord) -> View """
        pass

    def DestroyView(self, view, vp):
        """ DestroyView(self: Manager, view: View, vp: ViewportTableRecord) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetCurrent3dAcGsView(self, viewportNumber):
        """ GetCurrent3dAcGsView(self: Manager, viewportNumber: int) -> View """
        pass

    def GetCurrentAcGsView(self, viewportNumber):
        """ GetCurrentAcGsView(self: Manager, viewportNumber: int) -> View """
        pass

    def GetDBModel(self, A_0):
        """ GetDBModel(self: Manager, A_0: GraphicsKernel) -> Model """
        pass

    def GetGsModel(self, mode, subDrawingMode, viewportNumber):
        """ GetGsModel(self: Manager, mode: TransientDrawingMode, subDrawingMode: int, viewportNumber: int) -> Model """
        pass

    def GetGUIDevice(self, A_0):
        """ GetGUIDevice(self: Manager, A_0: GraphicsKernel) -> Device """
        pass

    def GetOffScreenDevice(self, A_0):
        """ GetOffScreenDevice(self: Manager, A_0: GraphicsKernel) -> Device """
        pass

    def GetOffScreenView(self, A_0, A_1):
        """ GetOffScreenView(self: Manager, A_0: GraphicsKernel, A_1: ClientViewInfo) -> View """
        pass

    def ObtainAcGsView(self, viewportNumber, createIfNone):
        """ ObtainAcGsView(self: Manager, viewportNumber: int, createIfNone: KernelDescriptor) -> View """
        pass

    @staticmethod
    def ReleaseGraphicsKernel(kernel):
        """ ReleaseGraphicsKernel(kernel: GraphicsKernel) """
        pass

    def SetViewFromViewport(self, view, viewportNumber):
        """ SetViewFromViewport(self: Manager, view: View, viewportNumber: int) """
        pass

    def SetViewportFromView(self, viewportNumber, view, regenRequired=None, rescaleRequired=None, syncRequired=None):
        """ SetViewportFromView(self: Manager, viewportNumber: int, view: View)SetViewportFromView(self: Manager, viewportNumber: int, view: View, regenRequired: bool, rescaleRequired: bool, syncRequired: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr) """
        pass

    DeviceIndependentDisplaySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeviceIndependentDisplaySize(self: Manager) -> Size

"""


    ConfigWasModified = None
    GsToBeUnloaded = None
    ViewToBeDestroyed = None
    ViewToBeUpdated = None
    ViewWasCreated = None
    ViewWasUpdated = None


class Model(DisposableWrapper):
    """ Model(renderType: RenderType) """
    def AddSceneGraphRoot(self, pRoot):
        """ AddSceneGraphRoot(self: Model, pRoot: Drawable) -> bool """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete, graphicsKernelPointer=None):
        """
        Create(unmanagedPointer: IntPtr, autoDelete: bool) -> Model
        Create(unmanagedPointer: IntPtr, autoDelete: bool, graphicsKernelPointer: IntPtr) -> Model
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EraseSceneGraphRoot(self, pRoot):
        """ EraseSceneGraphRoot(self: Model, pRoot: Drawable) -> bool """
        pass

    def Invalidate(self, hint):
        """ Invalidate(self: Model, hint: InvalidationHint) """
        pass

    def OnAdded(self, added, *__args):
        """ OnAdded(self: Model, added: Drawable, parent: Drawable)OnAdded(self: Model, added: Drawable, parentId: int) """
        pass

    def OnErased(self, erased, *__args):
        """ OnErased(self: Model, erased: Drawable, parent: Drawable)OnErased(self: Model, erased: Drawable, parentId: int) """
        pass

    def OnModified(self, modified, *__args):
        """ OnModified(self: Model, modified: Drawable, parent: Drawable)OnModified(self: Model, modified: Drawable, parentId: int) """
        pass

    def OnPaletteModified(self):
        """ OnPaletteModified(self: Model) """
        pass

    def SetExtents(self, point3dx, point3dy):
        """ SetExtents(self: Model, point3dx: Point3d, point3dy: Point3d) """
        pass

    def SetSectioning(self, pts, upVector, top=None, bottom=None):
        """
        SetSectioning(self: Model, pts: Point3dCollection, upVector: Vector3d) -> bool
        SetSectioning(self: Model, pts: Point3dCollection, upVector: Vector3d, top: float, bottom: float) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, renderType):
        """
        __new__(cls: type, renderType: RenderType)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BackgroundId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundId(self: Model) -> ObjectId

Set: BackgroundId(self: Model) = value
"""

    EnableSectioning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableSectioning(self: Model) -> bool

Set: EnableSectioning(self: Model) = value
"""

    LinetypesEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypesEnabled(self: Model) -> bool

Set: LinetypesEnabled(self: Model) = value
"""

    RenderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderType(self: Model) -> RenderType

"""

    SectioningVisualStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: SectioningVisualStyle(self: Model) = value
"""

    Selectable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selectable(self: Model) -> bool

Set: Selectable(self: Model) = value
"""

    ShadowPlaneLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShadowPlaneLocation(self: Model) -> float

Set: ShadowPlaneLocation(self: Model) = value
"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: Model) -> Matrix3d

Set: Transform(self: Model) = value
"""

    ViewClippingOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: ViewClippingOverride(self: Model) = value
"""

    VisualStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisualStyle(self: Model) -> VisualStyle

Set: VisualStyle(self: Model) = value
"""

    VisualStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisualStyleId(self: Model) -> ObjectId

Set: VisualStyleId(self: Model) = value
"""



class Node(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Drawable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Drawable(self: Node) -> Drawable

"""



class Projection(Enum):
    """ enum Projection, values: Parallel (0), Perspective (1) """
    Parallel = None
    Perspective = None
    value__ = None


class Quality(Enum):
    """ enum Quality, values: HighQuality (2), LowQuality (0), MediumQuality (1) """
    HighQuality = None
    LowQuality = None
    MediumQuality = None
    value__ = None


class ReleaseInterfaceFunction(MulticastDelegate):
    """ ReleaseInterfaceFunction(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, __unnamed000, callback, obj):
        """ BeginInvoke(self: ReleaseInterfaceFunction, __unnamed000: Drawable, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ReleaseInterfaceFunction, result: IAsyncResult) """
        pass

    def Invoke(self, A_0):
        """ Invoke(self: ReleaseInterfaceFunction, A_0: Drawable) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class RendererType(Enum):
    """ enum RendererType, values: Default (0), FullRender (3), SelectionRender (4), Software (1), SoftwareNewViewsOnly (2) """
    Default = None
    FullRender = None
    SelectionRender = None
    Software = None
    SoftwareNewViewsOnly = None
    value__ = None


class RenderType(Enum):
    """ enum RenderType, values: Contrast (6), Count (7), Direct (2), DirectTopmost (5), Highlight (3), HighlightSelection (4), Main (0), Sprite (1) """
    Contrast = None
    Count = None
    Direct = None
    DirectTopmost = None
    Highlight = None
    HighlightSelection = None
    Main = None
    Sprite = None
    value__ = None


class StereoParameters(object):
    """ StereoParameters(magnitude: float, parallax: float) """
    @staticmethod # known case of __new__
    def __new__(self, magnitude, parallax):
        """
        __new__[StereoParameters]() -> StereoParameters
        
        __new__(cls: type, magnitude: float, parallax: float)
        """
        pass

    Magnitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Magnitude(self: StereoParameters) -> float

"""

    Parallax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parallax(self: StereoParameters) -> float

"""



class View(DisposableWrapper):
    """
    View(clientViewInfo: ClientViewInfo, enableLayerVisibilityPerView: bool)
    View()
    """
    def Add(self, drawable, model):
        """ Add(self: View, drawable: Drawable, model: Model) -> bool """
        pass

    def BeginInteractivity(self, frameRateInHZ):
        """ BeginInteractivity(self: View, frameRateInHZ: float) """
        pass

    def ClearFrozenLayers(self):
        """ ClearFrozenLayers(self: View) """
        pass

    def Clone(self, cloneViewParameters=None, cloneGeometry=None):
        """
        Clone(self: View, cloneViewParameters: bool, cloneGeometry: bool) -> View
        Clone(self: View) -> View
        """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete, autoCADView, graphicsKernelPointer=None):
        """
        Create(unmanagedPointer: IntPtr, autoDelete: bool, autoCADView: bool) -> View
        Create(unmanagedPointer: IntPtr, autoDelete: bool, autoCADView: bool, graphicsKernelPointer: IntPtr) -> View
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Dolly(self, *__args):
        """ Dolly(self: View, vector: Vector3d)Dolly(self: View, x: float, y: float, z: float) """
        pass

    def EnableDefaultLighting(self, bEnable, type=None):
        """ EnableDefaultLighting(self: View, bEnable: bool, type: DefaultLightingType)EnableDefaultLighting(self: View, bEnable: bool) """
        pass

    def EndInteractivity(self):
        """ EndInteractivity(self: View) """
        pass

    def Erase(self, drawable):
        """ Erase(self: View, drawable: Drawable) -> bool """
        pass

    def EraseAll(self):
        """ EraseAll(self: View) """
        pass

    def ExtentsInView(self, minPoint, maxPoint):
        """ ExtentsInView(self: View, minPoint: Point3d, maxPoint: Point3d) -> bool """
        pass

    def Flush(self):
        """ Flush(self: View) """
        pass

    def FreezeLayer(self, layerId):
        """ FreezeLayer(self: View, layerId: Int64)FreezeLayer(self: View, layerId: IntPtr) """
        pass

    def GetModel(self, drw):
        """ GetModel(self: View, drw: Drawable) -> Model """
        pass

    def GetModelList(self):
        """ GetModelList(self: View) -> Array[Model] """
        pass

    def GetNumPixelsInUnitSquare(self, givenWorldpt, includePerspective=None):
        """
        GetNumPixelsInUnitSquare(self: View, givenWorldpt: Point3d, includePerspective: bool) -> Point2d
        GetNumPixelsInUnitSquare(self: View, givenWorldpt: Point3d) -> Point2d
        """
        pass

    def GetSnapshot(self, rectangle):
        """ GetSnapshot(self: View, rectangle: Rectangle) -> Bitmap """
        pass

    def Hide(self):
        """ Hide(self: View) """
        pass

    def Invalidate(self, rect=None):
        """ Invalidate(self: View)Invalidate(self: View, rect: Rectangle) """
        pass

    def InvalidateCachedViewportGeometry(self):
        """ InvalidateCachedViewportGeometry(self: View) """
        pass

    def Orbit(self, x, y):
        """ Orbit(self: View, x: float, y: float) """
        pass

    def Pan(self, x, y):
        """ Pan(self: View, x: float, y: float) """
        pass

    def PointInView(self, point):
        """ PointInView(self: View, point: Point3d) -> bool """
        pass

    def RemoveViewportClipRegion(self):
        """ RemoveViewportClipRegion(self: View) """
        pass

    def RenderToImage(self, settings=None, rectScreen=None, flipImage=None):
        """
        RenderToImage(self: View, settings: Drawable, rectScreen: Rectangle, flipImage: bool) -> Bitmap
        RenderToImage(self: View, settings: Drawable, rectScreen: Rectangle) -> Bitmap
        RenderToImage(self: View) -> Bitmap
        """
        pass

    def Roll(self, angle):
        """ Roll(self: View, angle: float) """
        pass

    def SetView(self, position, target, upVector, fieldWidth, fieldHeight, projection=None):
        """ SetView(self: View, position: Point3d, target: Point3d, upVector: Vector3d, fieldWidth: float, fieldHeight: float, projection: Projection)SetView(self: View, position: Point3d, target: Point3d, upVector: Vector3d, fieldWidth: float, fieldHeight: float) """
        pass

    def SetViewportClipRegion(self, contours, counts, points):
        """ SetViewportClipRegion(self: View, contours: int, counts: Array[int], points: Array[Point]) """
        pass

    def Show(self):
        """ Show(self: View) """
        pass

    def ThawLayer(self, layerId):
        """ ThawLayer(self: View, layerId: Int64)ThawLayer(self: View, layerId: IntPtr) """
        pass

    def Update(self):
        """ Update(self: View) """
        pass

    def Zoom(self, factor):
        """ Zoom(self: View, factor: float) """
        pass

    def ZoomExtents(self, minPoint, maxPoint):
        """ ZoomExtents(self: View, minPoint: Point3d, maxPoint: Point3d) """
        pass

    def ZoomWindow(self, lowerLeft, upperRight):
        """ ZoomWindow(self: View, lowerLeft: Point2d, upperRight: Point2d) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, clientViewInfo=None, enableLayerVisibilityPerView=None):
        """
        __new__(cls: type, clientViewInfo: ClientViewInfo, enableLayerVisibilityPerView: bool)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool, autoCADView: bool)
        """
        pass

    AcadWindowId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AcadWindowId(self: View) -> int

"""

    BackClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackClip(self: View) -> float

Set: BackClip(self: View) = value
"""

    BackgroundId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundId(self: View) -> ObjectId

Set: BackgroundId(self: View) = value
"""

    Device = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Device(self: View) -> Device

"""

    EnableBackClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableBackClip(self: View) -> bool

Set: EnableBackClip(self: View) = value
"""

    EnableFrontClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableFrontClip(self: View) -> bool

Set: EnableFrontClip(self: View) = value
"""

    EnableStereo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableStereo(self: View) -> bool

Set: EnableStereo(self: View) = value
"""

    ExceededBounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExceededBounds(self: View) -> bool

"""

    FieldHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldHeight(self: View) -> float

"""

    FieldWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldWidth(self: View) -> float

"""

    FrontClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrontClip(self: View) -> float

Set: FrontClip(self: View) = value
"""

    IsInteractive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInteractive(self: View) -> bool

"""

    IsPerspective = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPerspective(self: View) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: View) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: View) -> bool

"""

    ObjectToDeviceMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectToDeviceMatrix(self: View) -> Matrix3d

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: View) -> Point3d

"""

    ProjectionMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionMatrix(self: View) -> Matrix3d

"""

    ScreenMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScreenMatrix(self: View) -> Matrix3d

"""

    StereoParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StereoParameters(self: View) -> StereoParameters

Set: StereoParameters(self: View) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: View) -> Point3d

"""

    UpVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpVector(self: View) -> Vector3d

"""

    ViewingMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewingMatrix(self: View) -> Matrix3d

"""

    ViewportBorderProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportBorderProperties(self: View) -> ViewportBorderProperties

Set: ViewportBorderProperties(self: View) = value
"""

    ViewportBorderVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportBorderVisibility(self: View) -> bool

Set: ViewportBorderVisibility(self: View) = value
"""

    ViewportExtents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportExtents(self: View) -> Extents2d

Set: ViewportExtents(self: View) = value
"""

    ViewportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportId(self: View) -> IntPtr

"""

    ViewportObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportObjectId(self: View) -> ObjectId

"""

    VisualStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisualStyle(self: View) -> VisualStyle

Set: VisualStyle(self: View) = value
"""

    VisualStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisualStyleId(self: View) -> ObjectId

Set: VisualStyleId(self: View) = value
"""

    WorldToDeviceMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorldToDeviceMatrix(self: View) -> Matrix3d

"""



class ViewEventArgs(EventArgs):
    """ ViewEventArgs() """
    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: ViewEventArgs) -> View

"""



class ViewportBorderProperties(object):
    """ ViewportBorderProperties(color: Color, weight: int) """
    @staticmethod # known case of __new__
    def __new__(self, color, weight):
        """
        __new__[ViewportBorderProperties]() -> ViewportBorderProperties
        
        __new__(cls: type, color: Color, weight: int)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: ViewportBorderProperties) -> Color

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: ViewportBorderProperties) -> int

"""



class ViewToBeDestroyedEventHandler(MulticastDelegate):
    """ ViewToBeDestroyedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ViewToBeDestroyedEventHandler, sender: object, e: ViewEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ViewToBeDestroyedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ViewToBeDestroyedEventHandler, sender: object, e: ViewEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ViewToBeUpdatedEventHandler(MulticastDelegate):
    """ ViewToBeUpdatedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ViewToBeUpdatedEventHandler, sender: object, e: ViewUpdateEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ViewToBeUpdatedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ViewToBeUpdatedEventHandler, sender: object, e: ViewUpdateEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ViewUpdateEventArgs(EventArgs):
    """ ViewUpdateEventArgs() """
    View = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: View(self: ViewUpdateEventArgs) -> View

"""

    viewUpdateFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: viewUpdateFlags(self: ViewUpdateEventArgs) -> ViewUpdateFlags

"""



class ViewUpdateFlags(Enum):
    """ enum (flags) ViewUpdateFlags, values: CameraChanged (1) """
    CameraChanged = None
    value__ = None


class ViewWasCreatedEventHandler(MulticastDelegate):
    """ ViewWasCreatedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ViewWasCreatedEventHandler, sender: object, e: ViewEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ViewWasCreatedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ViewWasCreatedEventHandler, sender: object, e: ViewEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ViewWasUpdatedEventHandler(MulticastDelegate):
    """ ViewWasUpdatedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ViewWasUpdatedEventHandler, sender: object, e: ViewUpdateEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ViewWasUpdatedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ViewWasUpdatedEventHandler, sender: object, e: ViewUpdateEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


