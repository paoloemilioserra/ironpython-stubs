# encoding: utf-8
# module Autodesk.Civil.Runtime calls itself Runtime
# from AeccDbMgd, Version=13.3.854.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CorridorError(Enum):
    """ enum CorridorError, values: CorridorOutOfDate (-2147221486), CorridorStateNotFound (-2147221495), CouldNotSolveInLayoutMode (-2147221502), ElevationAtStationNotFound (-2147221488), Failure (-2147221503), InvalidArraySpecifiedForLinkDefinition (-2147221476), InvalidArraySpecifiedForLinkDefinitionFormat (-2147221475), InvalidArraySpecifiedForShapeDefinition (-2147221474), InvalidArraySpecifiedForShapeDefinitionFormat (-2147221473), InvalidCorridorStateObjectId (-2147221472), InvalidSubassemblyCOMClassId (-2147221471), LogicalNameNotFound (-2147221500), NoLinkIntersectFound (-2147221479), NoMarkedPointFound (-2147221478), None (0), NoSideslopeIntersectFound (-2147221499), NoSubgradeIntersectFound (-2147221498), ParameterNotFound (-2147221501), ReprocessAssembly (-2147221467), ReprocessBaseline (-2147221465), ReprocessRegion (-2147221466), ReprocessSubassembly (-2147221468), ScriptMacroNotFound (-2147221496), ScriptModuleNotFound (-2147221497), ScriptModulePathUpdated (-2147221487), ScriptPossibleSyntaxError (-2147221494), StopProcessingAssembly (-2147221492), StopProcessingBaseline (-2147221490), StopProcessingConditional (-2147221469), StopProcessingCorridor (-2147221489), StopProcessingGroup (-2147221493), StopProcessingRegion (-2147221491), Success (-2147221504), ValueInABadPosition (-2147221482), ValueShouldNotBeLessThanOrEqualToZero (-2147221485), ValueShouldNotBeLessThanZero (-2147221484), ValueShouldNotBeOdd (-2147221477), ValueShouldNotBeZero (-2147221483), ValueTooLarge (-2147221480), ValueTooSmall (-2147221481) """
    CorridorOutOfDate = None
    CorridorStateNotFound = None
    CouldNotSolveInLayoutMode = None
    ElevationAtStationNotFound = None
    Failure = None
    InvalidArraySpecifiedForLinkDefinition = None
    InvalidArraySpecifiedForLinkDefinitionFormat = None
    InvalidArraySpecifiedForShapeDefinition = None
    InvalidArraySpecifiedForShapeDefinitionFormat = None
    InvalidCorridorStateObjectId = None
    InvalidSubassemblyCOMClassId = None
    LogicalNameNotFound = None
    NoLinkIntersectFound = None
    NoMarkedPointFound = None
    None = None
    NoSideslopeIntersectFound = None
    NoSubgradeIntersectFound = None
    ParameterNotFound = None
    ReprocessAssembly = None
    ReprocessBaseline = None
    ReprocessRegion = None
    ReprocessSubassembly = None
    ScriptMacroNotFound = None
    ScriptModuleNotFound = None
    ScriptModulePathUpdated = None
    ScriptPossibleSyntaxError = None
    StopProcessingAssembly = None
    StopProcessingBaseline = None
    StopProcessingConditional = None
    StopProcessingCorridor = None
    StopProcessingGroup = None
    StopProcessingRegion = None
    Success = None
    ValueInABadPosition = None
    ValueShouldNotBeLessThanOrEqualToZero = None
    ValueShouldNotBeLessThanZero = None
    ValueShouldNotBeOdd = None
    ValueShouldNotBeZero = None
    ValueTooLarge = None
    ValueTooSmall = None
    value__ = None


class CorridorErrorLevel(Enum):
    """ enum CorridorErrorLevel, values: AsWarning (2), Informational (1), None (0), Severe (3) """
    AsWarning = None
    Informational = None
    None = None
    Severe = None
    value__ = None


class CorridorLayoutModeDisplay(Enum):
    """ enum CorridorLayoutModeDisplay, values: Conditional (4), DaylightBench (5), General (0), None (1), Sideslope (3), Subgrade (2) """
    Conditional = None
    DaylightBench = None
    General = None
    None = None
    Sideslope = None
    Subgrade = None
    value__ = None


class CorridorMode(Enum):
    """ enum CorridorMode, values: Design (2), Layout (1), None (0) """
    Design = None
    Layout = None
    None = None
    value__ = None


class RuntimeState(CivilWrapper<AeccDbRuntimeState>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbRuntimeState>, A_0: bool) """
        pass

    CurrentMacroName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentMacroName(self: RuntimeState) -> str

"""

    CurrentMacroProject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentMacroProject(self: RuntimeState) -> str

"""



class CorridorState(RuntimeState):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbRuntimeState>, A_0: bool) """
        pass

    def IntersectAlignment(self, targetAlignmentId, alignmentId, origin, lookRight, maxDistance=None):
        """
        IntersectAlignment(self: CorridorState, targetAlignmentId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool, maxDistance: float) -> IPoint
        IntersectAlignment(self: CorridorState, targetAlignmentId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool) -> IPoint
        """
        pass

    def IntersectLink(self, origin, lookRight, slope, linkCode):
        """ IntersectLink(self: CorridorState, origin: IPoint, lookRight: bool, slope: float, linkCode: str) -> IPoint """
        pass

    def IntersectSurface(self, surfaceId, alignmentId, origin, lookRight, slope, maxDistance=None):
        """
        IntersectSurface(self: CorridorState, surfaceId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool, slope: float, maxDistance: float) -> IPoint
        IntersectSurface(self: CorridorState, surfaceId: ObjectId, alignmentId: ObjectId, origin: IPoint, lookRight: bool, slope: float) -> IPoint
        """
        pass

    def IsAboveSurface(self, surfaceId, alignmentId, point, minimumAmountAbove=None):
        """
        IsAboveSurface(self: CorridorState, surfaceId: ObjectId, alignmentId: ObjectId, point: IPoint, minimumAmountAbove: float) -> bool
        IsAboveSurface(self: CorridorState, surfaceId: ObjectId, alignmentId: ObjectId, point: IPoint) -> bool
        """
        pass

    def RecordError(self, error, errorLevel, description, source, showInEventViewer):
        """ RecordError(self: CorridorState, error: CorridorError, errorLevel: CorridorErrorLevel, description: str, source: str, showInEventViewer: bool) """
        pass

    def SampleSection(self, surfaceId, alignmentId, point1, point2):
        """ SampleSection(self: CorridorState, surfaceId: ObjectId, alignmentId: ObjectId, point1: IPoint, point2: IPoint) -> SampledSectionLinkCollection """
        pass

    def SetAxisOfRotationCrownPoint(self, nCrownPointIndex):
        """ SetAxisOfRotationCrownPoint(self: CorridorState, nCrownPointIndex: UInt32) """
        pass

    def SetAxisOfRotationInformation(self, isPotentialPivot, superElevationSlope, superElevationSlopeType, isReversedSlope):
        """ SetAxisOfRotationInformation(self: CorridorState, isPotentialPivot: bool, superElevationSlope: float, superElevationSlopeType: SuperelevationCrossSegmentType, isReversedSlope: bool) """
        pass

    def SetAxisOfRotationSERange(self, dApplySE_StartOffset, dApplySE_EndOffset):
        """ SetAxisOfRotationSERange(self: CorridorState, dApplySE_StartOffset: float, dApplySE_EndOffset: float) """
        pass

    def SoeToXyz(self, alignmentId, station, offset, elevation, X, Y, Z):
        """ SoeToXyz(self: CorridorState, alignmentId: ObjectId, station: float, offset: float, elevation: float, X: float, Y: float, Z: float) -> (float, float, float) """
        pass

    def XyzToSoe(self, alignmentId, X, Y, Z, station, offset, elevation):
        """ XyzToSoe(self: CorridorState, alignmentId: ObjectId, X: float, Y: float, Z: float, station: float, offset: float, elevation: float) -> (float, float, float) """
        pass

    CurrentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAlignmentId(self: CorridorState) -> ObjectId

"""

    CurrentAlignmentIsOffsetAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAlignmentIsOffsetAlignment(self: CorridorState) -> bool

"""

    CurrentAssemblyElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAssemblyElevation(self: CorridorState) -> float

"""

    CurrentAssemblyFixedElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAssemblyFixedElevation(self: CorridorState) -> float

"""

    CurrentAssemblyFixedOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAssemblyFixedOffset(self: CorridorState) -> float

"""

    CurrentAssemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAssemblyId(self: CorridorState) -> ObjectId

"""

    CurrentAssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAssemblyName(self: CorridorState) -> str

"""

    CurrentAssemblyOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAssemblyOffset(self: CorridorState) -> float

"""

    CurrentAssemblyOffsetIsFixed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentAssemblyOffsetIsFixed(self: CorridorState) -> bool

"""

    CurrentBaselineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentBaselineId(self: CorridorState) -> ObjectId

"""

    CurrentCorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCorridorId(self: CorridorState) -> ObjectId

"""

    CurrentCorridorName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCorridorName(self: CorridorState) -> str

"""

    CurrentElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentElevation(self: CorridorState) -> float

"""

    CurrentOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentOffset(self: CorridorState) -> float

"""

    CurrentProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentProfileId(self: CorridorState) -> ObjectId

"""

    CurrentRegionEndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentRegionEndStation(self: CorridorState) -> float

"""

    CurrentRegionStartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentRegionStartStation(self: CorridorState) -> float

"""

    CurrentStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentStation(self: CorridorState) -> float

"""

    CurrentSubassemblyElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSubassemblyElevation(self: CorridorState) -> float

"""

    CurrentSubassemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSubassemblyId(self: CorridorState) -> ObjectId

"""

    CurrentSubassemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSubassemblyName(self: CorridorState) -> str

"""

    CurrentSubassemblyOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSubassemblyOffset(self: CorridorState) -> float

"""

    LayoutModeDisplayType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutModeDisplayType(self: CorridorState) -> CorridorLayoutModeDisplay

Set: LayoutModeDisplayType(self: CorridorState) = value
"""

    Links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Links(self: CorridorState) -> LinkCollection

"""

    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mode(self: CorridorState) -> CorridorMode

"""

    ParamsAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsAlignment(self: CorridorState) -> ParamAlignmentCollection

"""

    ParamsAlignmentGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsAlignmentGlobal(self: CorridorState) -> ParamAlignmentCollection

"""

    ParamsBool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsBool(self: CorridorState) -> ParamBoolCollection

"""

    ParamsBoolGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsBoolGlobal(self: CorridorState) -> ParamBoolCollection

"""

    ParamsDouble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsDouble(self: CorridorState) -> ParamDoubleCollection

"""

    ParamsDoubleGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsDoubleGlobal(self: CorridorState) -> ParamDoubleCollection

"""

    ParamsElevationTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsElevationTarget(self: CorridorState) -> ParamElevationTargetCollection

"""

    ParamsElevationTargetGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsElevationTargetGlobal(self: CorridorState) -> ParamElevationTargetCollection

"""

    ParamsLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsLong(self: CorridorState) -> ParamLongCollection

"""

    ParamsLongGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsLongGlobal(self: CorridorState) -> ParamLongCollection

"""

    ParamsOffsetTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsOffsetTarget(self: CorridorState) -> ParamOffsetTargetCollection

"""

    ParamsOffsetTargetGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsOffsetTargetGlobal(self: CorridorState) -> ParamOffsetTargetCollection

"""

    ParamsPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsPoint(self: CorridorState) -> ParamPointCollection

"""

    ParamsPointGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsPointGlobal(self: CorridorState) -> ParamPointCollection

"""

    ParamsProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsProfile(self: CorridorState) -> ParamProfileCollection

"""

    ParamsProfileGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsProfileGlobal(self: CorridorState) -> ParamProfileCollection

"""

    ParamsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsString(self: CorridorState) -> ParamStringCollection

"""

    ParamsStringGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsStringGlobal(self: CorridorState) -> ParamStringCollection

"""

    ParamsSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsSurface(self: CorridorState) -> ParamSurfaceCollection

"""

    ParamsSurfaceGlobal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsSurfaceGlobal(self: CorridorState) -> ParamSurfaceCollection

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: CorridorState) -> PointCollection

"""

    Shapes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shapes(self: CorridorState) -> ShapeCollection

"""



class IParam:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: IParam) -> ParamAccessType

Set: Access(self: IParam) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: IParam) -> str

Set: Comment(self: IParam) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IParam) -> str

Set: Description(self: IParam) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: IParam) -> str

Set: DisplayName(self: IParam) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: IParam) -> UInt16

Set: DisplayOrder(self: IParam) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: IParam) -> bool

Set: IsReadOnly(self: IParam) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: IParam) -> object

Set: Value(self: IParam) = value
"""



class Param(object):
    """ Param() """

class ParamAccessType(Enum):
    """ enum ParamAccessType, values: Input (1), InputAndOutput (3), None (0), Output (2) """
    Input = None
    InputAndOutput = None
    None = None
    Output = None
    value__ = None


class ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> ParamAccessType

Set: Access(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> str

Set: Comment(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> str

Set: Description(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> str

Set: DisplayName(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> UInt16

Set: DisplayOrder(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> bool

Set: IsReadOnly(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) -> ObjectId

Set: Value(self: ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>) = value
"""



class ParamAlignment(ParamBase<6\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpAlignmentId>):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamAlignment) -> ParamAccessType

Set: Access(self: ParamAlignment) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamAlignment) -> str

Set: Comment(self: ParamAlignment) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamAlignment) -> str

Set: Description(self: ParamAlignment) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamAlignment) -> str

Set: DisplayName(self: ParamAlignment) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamAlignment) -> UInt16

Set: DisplayOrder(self: ParamAlignment) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamAlignment) -> bool

Set: IsReadOnly(self: ParamAlignment) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamAlignment) -> ObjectId

Set: Value(self: ParamAlignment) = value
"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>) -> IEnumerator[ParamAlignment] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>, index: int) -> ObjectId
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>, index: str) -> ObjectId
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamAlignment](enumerable: IEnumerable[ParamAlignment], value: ParamAlignment) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>) -> int

"""



class ParamAlignmentCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamAlignment\,Autodesk::Civil::Runtime::ParamAlignment ^>):
    # no doc

class ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> ParamAccessType

Set: Access(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

Set: Comment(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

Set: Description(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

Set: DisplayName(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> UInt16

Set: DisplayOrder(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> bool

Set: IsReadOnly(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> SlopeElevationTarget

Set: Value(self: ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""



class ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> ParamAccessType

Set: Access(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> str

Set: Comment(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> str

Set: Description(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> str

Set: DisplayName(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> UInt16

Set: DisplayOrder(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> bool

Set: IsReadOnly(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) -> bool

Set: Value(self: ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >) = value
"""



class ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> ParamAccessType

Set: Access(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> str

Set: Comment(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> str

Set: Description(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> str

Set: DisplayName(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> UInt16

Set: DisplayOrder(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> bool

Set: IsReadOnly(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) -> int

Set: Value(self: ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >) = value
"""



class ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> ParamAccessType

Set: Access(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> str

Set: Comment(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> str

Set: Description(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> str

Set: DisplayName(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> UInt16

Set: DisplayOrder(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> bool

Set: IsReadOnly(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) -> float

Set: Value(self: ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >) = value
"""



class ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> ParamAccessType

Set: Access(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> str

Set: Comment(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> str

Set: Description(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> str

Set: DisplayName(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> UInt16

Set: DisplayOrder(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> bool

Set: IsReadOnly(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) -> str

Set: Value(self: ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >) = value
"""



class ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> ParamAccessType

Set: Access(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> str

Set: Comment(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> str

Set: Description(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> str

Set: DisplayName(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> UInt16

Set: DisplayOrder(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> bool

Set: IsReadOnly(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) -> Point3d

Set: Value(self: ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >) = value
"""



class ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> ParamAccessType

Set: Access(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> str

Set: Comment(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> str

Set: Description(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> str

Set: DisplayName(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> UInt16

Set: DisplayOrder(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> bool

Set: IsReadOnly(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) -> ObjectId

Set: Value(self: ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>) = value
"""



class ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> ParamAccessType

Set: Access(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> str

Set: Comment(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> str

Set: Description(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> str

Set: DisplayName(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> UInt16

Set: DisplayOrder(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> bool

Set: IsReadOnly(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) -> ObjectId

Set: Value(self: ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>) = value
"""



class ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >(object):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> ParamAccessType

Set: Access(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

Set: Comment(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

Set: Description(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

Set: DisplayName(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> UInt16

Set: DisplayOrder(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> bool

Set: IsReadOnly(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) -> WidthOffsetTarget

Set: Value(self: ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >) = value
"""



class ParamBool(ParamBase<1\,bool\,bool\,Autodesk::Civil::Runtime::CastOp<bool\,bool> >):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamBool) -> ParamAccessType

Set: Access(self: ParamBool) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamBool) -> str

Set: Comment(self: ParamBool) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamBool) -> str

Set: Description(self: ParamBool) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamBool) -> str

Set: DisplayName(self: ParamBool) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamBool) -> UInt16

Set: DisplayOrder(self: ParamBool) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamBool) -> bool

Set: IsReadOnly(self: ParamBool) = value
"""

    TypeInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeInfo(self: ParamBool) -> TypeInfoBool

Set: TypeInfo(self: ParamBool) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamBool) -> bool

Set: Value(self: ParamBool) = value
"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>) -> IEnumerator[ParamBool] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>, index: int) -> bool
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>, index: str) -> bool
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamBool](enumerable: IEnumerable[ParamBool], value: ParamBool) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>) -> int

"""



class ParamBoolCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamBool\,Autodesk::Civil::Runtime::ParamBool ^>):
    # no doc
    def Add(self, name, value):
        """ Add(self: ParamBoolCollection, name: str, value: bool) -> ParamBool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass


class ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>) -> IEnumerator[ParamDouble] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>, index: int) -> float
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>, index: str) -> float
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamDouble](enumerable: IEnumerable[ParamDouble], value: ParamDouble) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>) -> int

"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>) -> IEnumerator[ParamElevationTarget] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>, index: int) -> SlopeElevationTarget
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>, index: str) -> SlopeElevationTarget
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamElevationTarget](enumerable: IEnumerable[ParamElevationTarget], value: ParamElevationTarget) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>) -> int

"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>) -> IEnumerator[ParamLong] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>, index: int) -> int
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>, index: str) -> int
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamLong](enumerable: IEnumerable[ParamLong], value: ParamLong) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>) -> int

"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>) -> IEnumerator[ParamOffsetTarget] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>, index: int) -> WidthOffsetTarget
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>, index: str) -> WidthOffsetTarget
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamOffsetTarget](enumerable: IEnumerable[ParamOffsetTarget], value: ParamOffsetTarget) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>) -> int

"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>) -> IEnumerator[ParamPoint] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>, index: int) -> Point3d
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>, index: str) -> Point3d
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamPoint](enumerable: IEnumerable[ParamPoint], value: ParamPoint) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>) -> int

"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>) -> IEnumerator[ParamProfile] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>, index: int) -> ObjectId
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>, index: str) -> ObjectId
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamProfile](enumerable: IEnumerable[ParamProfile], value: ParamProfile) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>) -> int

"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>) -> IEnumerator[ParamString] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>, index: int) -> str
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>, index: str) -> str
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamString](enumerable: IEnumerable[ParamString], value: ParamString) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>) -> int

"""



class ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>) -> IEnumerator[ParamSurface] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>) -> IEnumerator """
        pass

    def Value(self, index):
        """
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>, index: int) -> ObjectId
        Value(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>, index: str) -> ObjectId
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ParamSurface](enumerable: IEnumerable[ParamSurface], value: ParamSurface) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>) -> int

"""



class ParamDouble(ParamBase<3\,double\,double\,Autodesk::Civil::Runtime::CastOp<double\,double> >):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamDouble) -> ParamAccessType

Set: Access(self: ParamDouble) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamDouble) -> str

Set: Comment(self: ParamDouble) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamDouble) -> str

Set: Description(self: ParamDouble) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamDouble) -> str

Set: DisplayName(self: ParamDouble) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamDouble) -> UInt16

Set: DisplayOrder(self: ParamDouble) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamDouble) -> bool

Set: IsReadOnly(self: ParamDouble) = value
"""

    TypeInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeInfo(self: ParamDouble) -> TypeInfoDouble

Set: TypeInfo(self: ParamDouble) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamDouble) -> float

Set: Value(self: ParamDouble) = value
"""



class ParamDoubleCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamDouble\,Autodesk::Civil::Runtime::ParamDouble ^>):
    # no doc
    def Add(self, name, value):
        """ Add(self: ParamDoubleCollection, name: str, value: float) -> ParamDouble """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass


class ParamElevationTarget(ParamBase<10\,Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::SlopeElevationTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamElevationTarget) -> ParamAccessType

Set: Access(self: ParamElevationTarget) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamElevationTarget) -> str

Set: Comment(self: ParamElevationTarget) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamElevationTarget) -> str

Set: Description(self: ParamElevationTarget) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamElevationTarget) -> str

Set: DisplayName(self: ParamElevationTarget) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamElevationTarget) -> UInt16

Set: DisplayOrder(self: ParamElevationTarget) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamElevationTarget) -> bool

Set: IsReadOnly(self: ParamElevationTarget) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Value(self: ParamElevationTarget) = value
"""



class ParamElevationTargetCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamElevationTarget\,Autodesk::Civil::Runtime::ParamElevationTarget ^>):
    # no doc

class ParamLogicalNameType(Enum):
    """ enum ParamLogicalNameType, values: Alignment (2), ElevationTarget (5), ElevationTargetPipe (7), None (0), OffsetTarget (4), OffsetTargetPipe (6), Profile (3), Surface (1) """
    Alignment = None
    ElevationTarget = None
    ElevationTargetPipe = None
    None = None
    OffsetTarget = None
    OffsetTargetPipe = None
    Profile = None
    Surface = None
    value__ = None


class ParamLong(ParamBase<2\,long\,long\,Autodesk::Civil::Runtime::CastOp<long\,long> >):
    # no doc
    def AddEnumData(self, name, displayName, value):
        """ AddEnumData(self: ParamLong, name: str, displayName: str, value: int) """
        pass

    def EnumCount(self):
        """ EnumCount(self: ParamLong) -> UInt32 """
        pass

    def GetEnumData(self, index, name, displayName, value):
        """ GetEnumData(self: ParamLong, index: UInt32, name: str, displayName: str, value: int) -> (str, str, int) """
        pass

    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamLong) -> ParamAccessType

Set: Access(self: ParamLong) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamLong) -> str

Set: Comment(self: ParamLong) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamLong) -> str

Set: Description(self: ParamLong) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamLong) -> str

Set: DisplayName(self: ParamLong) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamLong) -> UInt16

Set: DisplayOrder(self: ParamLong) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamLong) -> bool

Set: IsReadOnly(self: ParamLong) = value
"""

    TypeInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeInfo(self: ParamLong) -> TypeInfoLong

Set: TypeInfo(self: ParamLong) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamLong) -> int

Set: Value(self: ParamLong) = value
"""



class ParamLongCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamLong\,Autodesk::Civil::Runtime::ParamLong ^>):
    # no doc
    def Add(self, name, value):
        """ Add(self: ParamLongCollection, name: str, value: int) -> ParamLong """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass


class ParamOffsetTarget(ParamBase<9\,Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> >\,Autodesk::Civil::Runtime::CastOp<Autodesk::Civil::DatabaseServices::WidthOffsetTarget ^\,AcArray<AcDbObjectId\,AcArrayMemCopyReallocator<AcDbObjectId> > > >):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamOffsetTarget) -> ParamAccessType

Set: Access(self: ParamOffsetTarget) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamOffsetTarget) -> str

Set: Comment(self: ParamOffsetTarget) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamOffsetTarget) -> str

Set: Description(self: ParamOffsetTarget) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamOffsetTarget) -> str

Set: DisplayName(self: ParamOffsetTarget) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamOffsetTarget) -> UInt16

Set: DisplayOrder(self: ParamOffsetTarget) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamOffsetTarget) -> bool

Set: IsReadOnly(self: ParamOffsetTarget) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Value(self: ParamOffsetTarget) = value
"""



class ParamOffsetTargetCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamOffsetTarget\,Autodesk::Civil::Runtime::ParamOffsetTarget ^>):
    # no doc

class ParamPoint(ParamBase<5\,Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d\,Autodesk::Civil::Runtime::CastOp<Autodesk::AutoCAD::Geometry::Point3d\,AcGePoint3d> >):
    # no doc
    def GetPoint(self, station, offset, elevation):
        """ GetPoint(self: ParamPoint, station: float, offset: float, elevation: float) -> (float, float, float) """
        pass

    def SetPoint(self, station, offset, elevation):
        """ SetPoint(self: ParamPoint, station: float, offset: float, elevation: float) """
        pass

    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamPoint) -> ParamAccessType

Set: Access(self: ParamPoint) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamPoint) -> str

Set: Comment(self: ParamPoint) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamPoint) -> str

Set: Description(self: ParamPoint) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamPoint) -> str

Set: DisplayName(self: ParamPoint) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamPoint) -> UInt16

Set: DisplayOrder(self: ParamPoint) = value
"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: ParamPoint) -> float

Set: Elevation(self: ParamPoint) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamPoint) -> bool

Set: IsReadOnly(self: ParamPoint) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: ParamPoint) -> float

Set: Offset(self: ParamPoint) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: ParamPoint) -> float

Set: Station(self: ParamPoint) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamPoint) -> Point3d

Set: Value(self: ParamPoint) = value
"""



class ParamPointCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamPoint\,Autodesk::Civil::Runtime::ParamPoint ^>):
    # no doc
    def Add(self, name, value=None):
        """
        Add(self: ParamPointCollection, name: str, value: Point3d) -> ParamPoint
        Add(self: ParamPointCollection, name: str) -> ParamPoint
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass


class ParamProfile(ParamBase<7\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpProfileId>):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamProfile) -> ParamAccessType

Set: Access(self: ParamProfile) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamProfile) -> str

Set: Comment(self: ParamProfile) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamProfile) -> str

Set: Description(self: ParamProfile) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamProfile) -> str

Set: DisplayName(self: ParamProfile) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamProfile) -> UInt16

Set: DisplayOrder(self: ParamProfile) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamProfile) -> bool

Set: IsReadOnly(self: ParamProfile) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamProfile) -> ObjectId

Set: Value(self: ParamProfile) = value
"""



class ParamProfileCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamProfile\,Autodesk::Civil::Runtime::ParamProfile ^>):
    # no doc

class ParamScope(Enum):
    """ enum ParamScope, values: Global (1), Local (0) """
    Global = None
    Local = None
    value__ = None


class ParamsOwnerType(Enum):
    """ enum ParamsOwnerType, values: PipeNetworkPart (2), PipeNetworkRule (4), PipeNetworkState (3), RoadwayState (1), Subassembly (0) """
    PipeNetworkPart = None
    PipeNetworkRule = None
    PipeNetworkState = None
    RoadwayState = None
    Subassembly = None
    value__ = None


class ParamString(ParamBase<4\,System::String ^\,AecRmCString\,Autodesk::Civil::Runtime::CastOp<System::String ^\,AecRmCString> >):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamString) -> ParamAccessType

Set: Access(self: ParamString) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamString) -> str

Set: Comment(self: ParamString) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamString) -> str

Set: Description(self: ParamString) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamString) -> str

Set: DisplayName(self: ParamString) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamString) -> UInt16

Set: DisplayOrder(self: ParamString) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamString) -> bool

Set: IsReadOnly(self: ParamString) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamString) -> str

Set: Value(self: ParamString) = value
"""



class ParamStringCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamString\,Autodesk::Civil::Runtime::ParamString ^>):
    # no doc
    def Add(self, name, value):
        """ Add(self: ParamStringCollection, name: str, value: str) -> ParamString """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass


class ParamSurface(ParamBase<8\,Autodesk::AutoCAD::DatabaseServices::ObjectId\,AcDbObjectId\,Autodesk::Civil::Runtime::CastOpSurfaceId>):
    # no doc
    Access = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Access(self: ParamSurface) -> ParamAccessType

Set: Access(self: ParamSurface) = value
"""

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: ParamSurface) -> str

Set: Comment(self: ParamSurface) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ParamSurface) -> str

Set: Description(self: ParamSurface) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ParamSurface) -> str

Set: DisplayName(self: ParamSurface) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOrder(self: ParamSurface) -> UInt16

Set: DisplayOrder(self: ParamSurface) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: ParamSurface) -> bool

Set: IsReadOnly(self: ParamSurface) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: ParamSurface) -> ObjectId

Set: Value(self: ParamSurface) = value
"""



class ParamSurfaceCollection(ParamCollectionBase<Autodesk::Civil::Runtime::ParamSurface\,Autodesk::Civil::Runtime::ParamSurface ^>):
    # no doc

class ParamType(Enum):
    """ enum ParamType, values: Alignment (6), Bool (1), Double (3), ElevationTarget (10), Int (2), OffsetTarget (9), Point3d (5), Profile (7), String (4), Surface (8), Unknown (0) """
    Alignment = None
    Bool = None
    Double = None
    ElevationTarget = None
    Int = None
    OffsetTarget = None
    Point3d = None
    Profile = None
    String = None
    Surface = None
    Unknown = None
    value__ = None


class PipeNetworkState(RuntimeState):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbRuntimeState>, A_0: bool) """
        pass

    def RuleResourceString(self, resId):
        """ RuleResourceString(self: PipeNetworkState, resId: str) -> str """
        pass

    def SetAlignmentOnPart(self, paramName, alignmentId):
        """ SetAlignmentOnPart(self: PipeNetworkState, paramName: str, alignmentId: ObjectId) """
        pass

    def SetBoolOnPart(self, paramName, value):
        """ SetBoolOnPart(self: PipeNetworkState, paramName: str, value: bool) """
        pass

    def SetDoubleOnCurrentPart(self, paramKey, value):
        """ SetDoubleOnCurrentPart(self: PipeNetworkState, paramKey: str, value: float) """
        pass

    def SetErrorMsgOnCurrentPart(self, paramKey, errorMessage):
        """ SetErrorMsgOnCurrentPart(self: PipeNetworkState, paramKey: str, errorMessage: str) """
        pass

    def SetLongOnPart(self, paramName, value):
        """ SetLongOnPart(self: PipeNetworkState, paramName: str, value: int) """
        pass

    def SetPointOnPart(self, paramName, value):
        """ SetPointOnPart(self: PipeNetworkState, paramName: str, value: Point3d) """
        pass

    def SetProfileOnPart(self, paramName, profileId):
        """ SetProfileOnPart(self: PipeNetworkState, paramName: str, profileId: ObjectId) """
        pass

    def SetStringOnPart(self, paramName, value):
        """ SetStringOnPart(self: PipeNetworkState, paramName: str, value: str) """
        pass

    def SetSurfaceOnPart(self, paramName, surfaceId):
        """ SetSurfaceOnPart(self: PipeNetworkState, paramName: str, surfaceId: ObjectId) """
        pass

    CurrentPipeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPipeId(self: PipeNetworkState) -> ObjectId

"""

    CurrentStructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentStructureId(self: PipeNetworkState) -> ObjectId

"""

    IsBreakingPipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBreakingPipe(self: PipeNetworkState) -> bool

"""

    IsConnectingToStructure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnectingToStructure(self: PipeNetworkState) -> bool

"""

    IsCurrentPartBeingAdd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCurrentPartBeingAdd(self: PipeNetworkState) -> bool

"""

    IsInLayoutMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInLayoutMode(self: PipeNetworkState) -> bool

"""

    IsLayoutUpStream = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLayoutUpStream(self: PipeNetworkState) -> bool

"""

    LastPipeElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastPipeElevation(self: PipeNetworkState) -> float

Set: LastPipeElevation(self: PipeNetworkState) = value
"""

    ParamsBool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsBool(self: PipeNetworkState) -> ParamBoolCollection

"""

    ParamsDouble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsDouble(self: PipeNetworkState) -> ParamDoubleCollection

"""

    ParamsLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsLong(self: PipeNetworkState) -> ParamLongCollection

"""



class TypeInfoBool(Enum):
    """ enum TypeInfoBool, values: Bool (0), DecimalFractional (8), DisabledEnabled (5), InOutCurve (9), LabelTag (2), NoYes (1), OffOn (6), RightLeft (7), StackedText (4), StraightSpline (3) """
    Bool = None
    DecimalFractional = None
    DisabledEnabled = None
    InOutCurve = None
    LabelTag = None
    NoYes = None
    OffOn = None
    RightLeft = None
    StackedText = None
    StraightSpline = None
    value__ = None


class TypeInfoDouble(Enum):
    """ enum TypeInfoDouble, values: Angle (14), Area (20), Azimuth (26), ConvergenceAngle (15), Coordinate (18), DerivedStation (7), Dimension (17), Direction (11), Distance (16), Double (0), Elevation (21), ElevationPoint (22), Grade (8), Latitude (13), LatLong (12), NonNegativeDouble (1), NonNegativeNonZeroDouble (2), NonPositiveDouble (3), NonPositiveNonZeroDouble (4), NonZeroDouble (5), Percent (25), PlotHeight (23), Station (6), TransparentCmdGrade (9), TransparentCmdSlope (10), Volume (24), XYCoordinatePair (19) """
    Angle = None
    Area = None
    Azimuth = None
    ConvergenceAngle = None
    Coordinate = None
    DerivedStation = None
    Dimension = None
    Direction = None
    Distance = None
    Double = None
    Elevation = None
    ElevationPoint = None
    Grade = None
    Latitude = None
    LatLong = None
    NonNegativeDouble = None
    NonNegativeNonZeroDouble = None
    NonPositiveDouble = None
    NonPositiveNonZeroDouble = None
    NonZeroDouble = None
    Percent = None
    PlotHeight = None
    Station = None
    TransparentCmdGrade = None
    TransparentCmdSlope = None
    value__ = None
    Volume = None
    XYCoordinatePair = None


class TypeInfoLong(Enum):
    """ enum TypeInfoLong, values: Color (6), LineWeight (8), Long (0), NonNegativeLong (2), NonNegativeNonZeroLong (3), NonPositiveLong (4), NonPositiveNonZeroLong (5), NonZeroLong (1), PDMODE (7) """
    Color = None
    LineWeight = None
    Long = None
    NonNegativeLong = None
    NonNegativeNonZeroLong = None
    NonPositiveLong = None
    NonPositiveNonZeroLong = None
    NonZeroLong = None
    PDMODE = None
    value__ = None


