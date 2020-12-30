# encoding: utf-8
# module Autodesk.Aec.ApplicationServices calls itself ApplicationServices
# from AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null, AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AecApplicationVersion(DisposableWrapper):
    # no doc
    @staticmethod
    def Base():
        """ Base() -> AecApplicationVersion """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def DwgInFields(self, filer):
        """ DwgInFields(self: AecApplicationVersion, filer: DwgFiler) """
        pass

    def DwgOutFields(self, filer):
        """ DwgOutFields(self: AecApplicationVersion, filer: DwgFiler) """
        pass

    @staticmethod
    def Specific(major, minor, buildMajor, buildMinor):
        """ Specific(major: Int16, minor: Int16, buildMajor: Int16, buildMinor: Int16) -> AecApplicationVersion """
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    BuildMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BuildMajor(self: AecApplicationVersion) -> Int16

"""

    BuildMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BuildMinor(self: AecApplicationVersion) -> Int16

"""

    Major = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Major(self: AecApplicationVersion) -> Int16

"""

    Minor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minor(self: AecApplicationVersion) -> Int16

"""



class DatabaseDataManager(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetAllDatabaseData(self):
        """ GetAllDatabaseData(self: DatabaseDataManager) -> Array[DatabaseData] """
        pass

    def GetDatabaseData(self, database):
        """ GetDatabaseData(self: DatabaseDataManager, database: Database) -> DatabaseData """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class DatabaseDataManagerDictionary(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetManager(keyName):
        """ GetManager(keyName: str) -> DatabaseDataManager """
        pass

    @staticmethod
    def GetManagers():
        """ GetManagers() -> DBObjectCollection """
        pass

    @staticmethod
    def RegisterPacketType(keyName, packetClassType):
        """ RegisterPacketType(keyName: str, packetClassType: RXClass) """
        pass

    @staticmethod
    def UnRegisterPacketType(keyName):
        """ UnRegisterPacketType(keyName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class DBVariables(DictionaryRecord):
    """ DBVariables() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DrawingSetupVariables(DBVariables):
    """ DrawingSetupVariables() """
    def ConvertToCurrentAreaDisplay(self, area):
        """ ConvertToCurrentAreaDisplay(self: DrawingSetupVariables, area: float) -> float """
        pass

    def ConvertToCurrentVolumeDisplay(self, volume):
        """ ConvertToCurrentVolumeDisplay(self: DrawingSetupVariables, volume: float) -> float """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetInstance(db, createIfNotFound):
        """ GetInstance(db: Database, createIfNotFound: bool) -> ObjectId """
        pass

    def SaveAsDefault(self):
        """ SaveAsDefault(self: DrawingSetupVariables) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AecBasePtNE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AecBasePtNE(self: DrawingSetupVariables) -> Point3d

Set: AecBasePtNE(self: DrawingSetupVariables) = value
"""

    AecDwgBasePt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AecDwgBasePt(self: DrawingSetupVariables) -> Point3d

Set: AecDwgBasePt(self: DrawingSetupVariables) = value
"""

    AecNorthRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AecNorthRotation(self: DrawingSetupVariables) -> float

Set: AecNorthRotation(self: DrawingSetupVariables) = value
"""

    AlwaysUpdateLayerKeyStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlwaysUpdateLayerKeyStyle(self: DrawingSetupVariables) -> bool

Set: AlwaysUpdateLayerKeyStyle(self: DrawingSetupVariables) = value
"""

    AngularAzimuth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngularAzimuth(self: DrawingSetupVariables) -> int

Set: AngularAzimuth(self: DrawingSetupVariables) = value
"""

    AngularDisplayFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngularDisplayFormat(self: DrawingSetupVariables) -> int

Set: AngularDisplayFormat(self: DrawingSetupVariables) = value
"""

    AngularPrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngularPrecision(self: DrawingSetupVariables) -> int

Set: AngularPrecision(self: DrawingSetupVariables) = value
"""

    AreaDisplayUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaDisplayUnit(self: DrawingSetupVariables) -> BuiltInUnit

Set: AreaDisplayUnit(self: DrawingSetupVariables) = value
"""

    AreaPrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaPrecision(self: DrawingSetupVariables) -> int

Set: AreaPrecision(self: DrawingSetupVariables) = value
"""

    AreaSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaSuffix(self: DrawingSetupVariables) -> str

Set: AreaSuffix(self: DrawingSetupVariables) = value
"""

    BlockBasedLayerOffBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockBasedLayerOffBehavior(self: DrawingSetupVariables) -> bool

Set: BlockBasedLayerOffBehavior(self: DrawingSetupVariables) = value
"""

    CivilDimaltd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilDimaltd(self: DrawingSetupVariables) -> int

Set: CivilDimaltd(self: DrawingSetupVariables) = value
"""

    CivilDimaltf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilDimaltf(self: DrawingSetupVariables) -> float

Set: CivilDimaltf(self: DrawingSetupVariables) = value
"""

    CivilDimapost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilDimapost(self: DrawingSetupVariables) -> str

Set: CivilDimapost(self: DrawingSetupVariables) = value
"""

    CivilDimexo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilDimexo(self: DrawingSetupVariables) -> float

Set: CivilDimexo(self: DrawingSetupVariables) = value
"""

    CivilDimpost = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilDimpost(self: DrawingSetupVariables) -> str

Set: CivilDimpost(self: DrawingSetupVariables) = value
"""

    CivilDimscale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilDimscale(self: DrawingSetupVariables) -> float

Set: CivilDimscale(self: DrawingSetupVariables) = value
"""

    CivilStateFlag1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilStateFlag1(self: DrawingSetupVariables) -> int

Set: CivilStateFlag1(self: DrawingSetupVariables) = value
"""

    CivilStateFlag2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilStateFlag2(self: DrawingSetupVariables) -> int

Set: CivilStateFlag2(self: DrawingSetupVariables) = value
"""

    CivilStateFlag3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilStateFlag3(self: DrawingSetupVariables) -> int

Set: CivilStateFlag3(self: DrawingSetupVariables) = value
"""

    CivilTextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CivilTextStyle(self: DrawingSetupVariables) -> str

Set: CivilTextStyle(self: DrawingSetupVariables) = value
"""

    CoordinatePrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinatePrecision(self: DrawingSetupVariables) -> int

Set: CoordinatePrecision(self: DrawingSetupVariables) = value
"""

    CreateDimOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateDimOverride(self: DrawingSetupVariables) -> bool

Set: CreateDimOverride(self: DrawingSetupVariables) = value
"""

    CurrentDimUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDimUnit(self: DrawingSetupVariables) -> BuiltInUnit

Set: CurrentDimUnit(self: DrawingSetupVariables) = value
"""

    DwgScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwgScale(self: DrawingSetupVariables) -> float

Set: DwgScale(self: DrawingSetupVariables) = value
"""

    ElevationLabelPlus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationLabelPlus(self: DrawingSetupVariables) -> bool

Set: ElevationLabelPlus(self: DrawingSetupVariables) = value
"""

    ElevationLabelPlusMinus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationLabelPlusMinus(self: DrawingSetupVariables) -> bool

Set: ElevationLabelPlusMinus(self: DrawingSetupVariables) = value
"""

    ElevationPrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationPrecision(self: DrawingSetupVariables) -> int

Set: ElevationPrecision(self: DrawingSetupVariables) = value
"""

    FacetDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FacetDeviation(self: DrawingSetupVariables) -> float

Set: FacetDeviation(self: DrawingSetupVariables) = value
"""

    GeometrySharingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometrySharingEnabled(self: DrawingSetupVariables) -> bool

Set: GeometrySharingEnabled(self: DrawingSetupVariables) = value
"""

    IsMetric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMetric(self: DrawingSetupVariables) -> bool

"""

    LastLayerStyleUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastLayerStyleUpdate(self: DrawingSetupVariables) -> Int64

"""

    LayerFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerFile(self: DrawingSetupVariables) -> str

Set: LayerFile(self: DrawingSetupVariables) = value
"""

    LayerStandard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerStandard(self: DrawingSetupVariables) -> str

Set: LayerStandard(self: DrawingSetupVariables) = value
"""

    LayerStandardLegacy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerStandardLegacy(self: DrawingSetupVariables) -> str

"""

    LinearDisplayFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinearDisplayFormat(self: DrawingSetupVariables) -> int

Set: LinearDisplayFormat(self: DrawingSetupVariables) = value
"""

    LinearPrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinearPrecision(self: DrawingSetupVariables) -> int

Set: LinearPrecision(self: DrawingSetupVariables) = value
"""

    LinearUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinearUnit(self: DrawingSetupVariables) -> BuiltInUnit

Set: LinearUnit(self: DrawingSetupVariables) = value
"""

    MaxFacetsOnCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxFacetsOnCircle(self: DrawingSetupVariables) -> Int16

Set: MaxFacetsOnCircle(self: DrawingSetupVariables) = value
"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectName(self: DrawingSetupVariables) -> str

Set: ProjectName(self: DrawingSetupVariables) = value
"""

    ScaleOnInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleOnInsert(self: DrawingSetupVariables) -> bool

Set: ScaleOnInsert(self: DrawingSetupVariables) = value
"""

    SuperScript = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperScript(self: DrawingSetupVariables) -> bool

Set: SuperScript(self: DrawingSetupVariables) = value
"""

    SuperScriptZeroSupression = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperScriptZeroSupression(self: DrawingSetupVariables) -> bool

Set: SuperScriptZeroSupression(self: DrawingSetupVariables) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: DrawingSetupVariables) -> float

Set: TextHeight(self: DrawingSetupVariables) = value
"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitType(self: DrawingSetupVariables) -> MeasurementValue

"""

    VerticalScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalScale(self: DrawingSetupVariables) -> float

Set: VerticalScale(self: DrawingSetupVariables) = value
"""

    VolumeDisplayUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeDisplayUnit(self: DrawingSetupVariables) -> BuiltInUnit

Set: VolumeDisplayUnit(self: DrawingSetupVariables) = value
"""

    VolumePrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumePrecision(self: DrawingSetupVariables) -> int

Set: VolumePrecision(self: DrawingSetupVariables) = value
"""

    VolumeSuffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeSuffix(self: DrawingSetupVariables) -> str

Set: VolumeSuffix(self: DrawingSetupVariables) = value
"""

    XrefOverlaysUseOwnDisplayConfig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XrefOverlaysUseOwnDisplayConfig(self: DrawingSetupVariables) -> bool

Set: XrefOverlaysUseOwnDisplayConfig(self: DrawingSetupVariables) = value
"""



class LegacyDrawingUnitMode(Enum):
    """ enum LegacyDrawingUnitMode, values: Automatic (0), Imperial (1), Metric (2) """
    Automatic = None
    Imperial = None
    Metric = None
    value__ = None


class Preferences(object):
    """ Preferences() """
    @staticmethod
    def GetApplyCommonProperties(fromRegistry):
        """ GetApplyCommonProperties(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetDisplayEnhancedReferenceObjectRelationshipGraphMessages(fromRegistry):
        """ GetDisplayEnhancedReferenceObjectRelationshipGraphMessages(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetDraftWarningSymbol(fromRegistry):
        """ GetDraftWarningSymbol(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetEnableProgressiveUpdate(fromRegistry):
        """ GetEnableProgressiveUpdate(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetExportExplodedToAcadBindXrefs(fromRegistry):
        """ GetExportExplodedToAcadBindXrefs(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetExportExplodedToAcadExportFormat(fromRegistry):
        """ GetExportExplodedToAcadExportFormat(fromRegistry: bool) -> DwgVersion """
        pass

    @staticmethod
    def GetExportExplodedToAcadFilePrefix(fromRegistry):
        """ GetExportExplodedToAcadFilePrefix(fromRegistry: bool) -> str """
        pass

    @staticmethod
    def GetExportExplodedToAcadFileSuffix(fromRegistry):
        """ GetExportExplodedToAcadFileSuffix(fromRegistry: bool) -> str """
        pass

    @staticmethod
    def GetExportExplodedToAcadInsertWhenBinding(fromRegistry):
        """ GetExportExplodedToAcadInsertWhenBinding(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetGeometryDiagnostics(fromRegistry):
        """ GetGeometryDiagnostics(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetLegacyDrawingUnitMode(fromRegistry):
        """ GetLegacyDrawingUnitMode(fromRegistry: bool) -> LegacyDrawingUnitMode """
        pass

    @staticmethod
    def GetMaintainExplodedObjectBlockProperties(fromRegistry):
        """ GetMaintainExplodedObjectBlockProperties(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetObjectRelationshipGraphDiagnostics(fromRegistry):
        """ GetObjectRelationshipGraphDiagnostics(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetPlotOrPublishWarningSymbol(fromRegistry):
        """ GetPlotOrPublishWarningSymbol(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetQuickOsnapMode(fromRegistry):
        """ GetQuickOsnapMode(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def GetViewManagementSystemDiagnostics(fromRegistry):
        """ GetViewManagementSystemDiagnostics(fromRegistry: bool) -> bool """
        pass

    @staticmethod
    def SetApplyCommonProperties(enabled, updateVariable, updateRegistry):
        """ SetApplyCommonProperties(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetDisplayEnhancedReferenceObjectRelationshipGraphMessages(enabled, updateVariable, updateRegistry):
        """ SetDisplayEnhancedReferenceObjectRelationshipGraphMessages(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetDraftWarningSymbol(enabled, updateVariable, updateRegistry):
        """ SetDraftWarningSymbol(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetEnableProgressiveUpdate(enable, updateVar, updateReg):
        """ SetEnableProgressiveUpdate(enable: bool, updateVar: bool, updateReg: bool) """
        pass

    @staticmethod
    def SetExportExplodedToAcadBindXrefs(enabled, updateVariable, updateRegistry):
        """ SetExportExplodedToAcadBindXrefs(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetExportExplodedToAcadExportFormat(dwgFormat, updateVariable, updateRegistry):
        """ SetExportExplodedToAcadExportFormat(dwgFormat: DwgVersion, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetExportExplodedToAcadFilePrefix(prefix, updateVariable, updateRegistry):
        """ SetExportExplodedToAcadFilePrefix(prefix: str, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetExportExplodedToAcadFileSuffix(suffix, updateVariable, updateRegistry):
        """ SetExportExplodedToAcadFileSuffix(suffix: str, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetExportExplodedToAcadInsertWhenBinding(enabled, updateVariable, updateRegistry):
        """ SetExportExplodedToAcadInsertWhenBinding(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetGeometryDiagnostics(enabled, updateVariable, updateRegistry):
        """ SetGeometryDiagnostics(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetLegacyDrawingUnitMode(mode, updateVariable, updateRegistry):
        """ SetLegacyDrawingUnitMode(mode: LegacyDrawingUnitMode, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetMaintainExplodedObjectBlockProperties(enabled, updateVariable, updateRegistry):
        """ SetMaintainExplodedObjectBlockProperties(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetObjectRelationshipGraphDiagnostics(enabled, updateVariable, updateRegistry):
        """ SetObjectRelationshipGraphDiagnostics(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetPlotOrPublishWarningSymbol(enabled, updateVariable, updateRegistry):
        """ SetPlotOrPublishWarningSymbol(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetQuickOsnapMode(enabled, updateVariable, updateRegistry):
        """ SetQuickOsnapMode(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    @staticmethod
    def SetViewManagementSystemDiagnostics(enabled, updateVariable, updateRegistry):
        """ SetViewManagementSystemDiagnostics(enabled: bool, updateVariable: bool, updateRegistry: bool) """
        pass

    AllowSnapToSurfaceHatch = False
    ApplyCommonProperties = True
    DisableOsnapGsMarkerOptimization = False
    DisplayEnhancedReferenceObjectRelationshipGraphMessages = False
    DraftWarningSymbol = True
    EnableProgressiveUpdate = False
    ExportExplodedToAcadBindXrefs = True
    ExportExplodedToAcadExportFormat = None
    ExportExplodedToAcadFilePrefix = 'ACAD-'
    ExportExplodedToAcadFileSuffix = ''
    ExportExplodedToAcadInsertWhenBinding = True
    GeometryDiagnostics = False
    LegacyDrawingUnitMode = None
    MaintainExplodedObjectBlockProperties = True
    ObjectRelationshipGraphDiagnostics = False
    PlotOrPublishWarningSymbol = False
    QuickOsnapMode = False
    ViewManagementSystemDiagnostics = False


