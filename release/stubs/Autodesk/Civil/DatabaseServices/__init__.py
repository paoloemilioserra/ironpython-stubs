# encoding: utf-8
# module Autodesk.Civil.DatabaseServices calls itself DatabaseServices
# from AeccDbMgd, Version=13.3.854.0, Culture=neutral, PublicKeyToken=null, AeccPressurePipesMgd, Version=13.3.854.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AdditionalAppliedAssemblyInfo(object):
    """ AdditionalAppliedAssemblyInfo(station: float, description: str) """
    @staticmethod # known case of __new__
    def __new__(self, station, description):
        """ __new__(cls: type, station: float, description: str) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: AdditionalAppliedAssemblyInfo) -> str

Set: Description(self: AdditionalAppliedAssemblyInfo) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: AdditionalAppliedAssemblyInfo) -> float

Set: Station(self: AdditionalAppliedAssemblyInfo) = value
"""



class Entity(Entity):
    # no doc
    def ComputeFingerPrint(self):
        """ ComputeFingerPrint(self: Entity) -> UInt64 """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: Entity) -> object

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Entity) -> str

Set: Description(self: Entity) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: Entity) -> str

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: Entity) -> object

"""

    FingerPrint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FingerPrint(self: Entity) -> UInt64

Set: FingerPrint(self: Entity) = value
"""

    FolderId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FolderId(self: Entity) -> ObjectId

"""

    IsReferenceObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferenceObject(self: Entity) -> bool

"""

    IsReferenceStale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferenceStale(self: Entity) -> bool

"""

    IsReferenceSubObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferenceSubObject(self: Entity) -> bool

"""

    IsReferenceValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReferenceValid(self: Entity) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Entity) -> str

Set: Name(self: Entity) = value
"""

    ShowToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowToolTip(self: Entity) -> bool

Set: ShowToolTip(self: Entity) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: Entity) -> ObjectId

Set: StyleId(self: Entity) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: Entity) -> str

Set: StyleName(self: Entity) = value
"""



class Feature(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def IsEditableFeature(featureId):
        """ IsEditableFeature(featureId: ObjectId) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    IsEditable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEditable(self: Feature) -> bool

"""



class Alignment(Feature):
    # no doc
    def CopyToSite(self, *__args):
        """ CopyToSite(self: Alignment, siteId: ObjectId)CopyToSite(self: Alignment, siteName: str) """
        pass

    @staticmethod
    def Create(*__args):
        """
        Create(corridorFeatureLine: CorridorFeatureLine, alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, alignmentType: AlignmentType) -> ObjectId
        Create(document: CivilDocument, plineOptions: PolylineOptions, alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId
        Create(document: CivilDocument, plineOptions: PolylineOptions, alignmentName: str, siteName: str, layerName: str, styleName: str, labelSetName: str) -> ObjectId
        Create(document: CivilDocument, alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, type: AlignmentType) -> ObjectId
        Create(document: CivilDocument, alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId
        Create(document: CivilDocument, alignmentName: str, siteName: str, layerName: str, styleName: str, labelSetName: str) -> ObjectId
        """
        pass

    @staticmethod
    def CreateOffsetAlignment(*__args):
        """
        CreateOffsetAlignment(alignmentName: str, parentAlignmentId: ObjectId, offset: float, styleId: ObjectId) -> ObjectId
        CreateOffsetAlignment(self: Alignment, offsetDistance: float) -> ObjectId
        CreateOffsetAlignment(alignmentName: str, parentAlignmentId: ObjectId, offset: float, styleId: ObjectId, startStation: float, endStation: float) -> ObjectId
        CreateOffsetAlignment(database: Database, alignmentName: str, parentAlignmentName: str, offset: float, styleName: str, startStation: float, endStation: float) -> ObjectId
        CreateOffsetAlignment(database: Database, alignmentName: str, parentAlignmentName: str, offset: float, styleName: str) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def DistanceToAlignment(self, stationOnThisAlignment, otherAlignment, *__args):
        """
        DistanceToAlignment(self: Alignment, stationOnThisAlignment: float, otherAlignment: Alignment, distanceToOtherAlignment: float, stationOnOtherAlignment: float) -> (float, float)
        DistanceToAlignment(self: Alignment, stationOnThisAlignment: float, otherAlignment: Alignment, enumSide: AlignmentSide, distanceToOtherAlignment: float, stationOnOtherAlignment: float) -> (float, float)
        """
        pass

    def GetAlignmentLabelGroupIds(self):
        """ GetAlignmentLabelGroupIds(self: Alignment) -> ObjectIdCollection """
        pass

    def GetAlignmentLabelIds(self):
        """ GetAlignmentLabelIds(self: Alignment) -> ObjectIdCollection """
        pass

    def GetChildOffsetAlignmentIds(self, onlyDynamicUpdate=None):
        """
        GetChildOffsetAlignmentIds(self: Alignment) -> ObjectIdCollection
        GetChildOffsetAlignmentIds(self: Alignment, onlyDynamicUpdate: bool) -> ObjectIdCollection
        """
        pass

    def GetCrossSlopeAtStation(self, station, crossSegmentType, applySmoothing):
        """ GetCrossSlopeAtStation(self: Alignment, station: float, crossSegmentType: SuperelevationCrossSegmentType, applySmoothing: bool) -> float """
        pass

    def GetInstantaneousRadius(self, rawStation):
        """ GetInstantaneousRadius(self: Alignment, rawStation: float) -> float """
        pass

    def GetLabelGroupIds(self):
        """ GetLabelGroupIds(self: Alignment) -> ObjectIdCollection """
        pass

    def GetLabelIds(self):
        """ GetLabelIds(self: Alignment) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetNextUniqueName(alignmentName):
        """ GetNextUniqueName(alignmentName: str) -> str """
        pass

    def GetPolyline(self):
        """ GetPolyline(self: Alignment) -> ObjectId """
        pass

    def GetProfileIds(self):
        """ GetProfileIds(self: Alignment) -> ObjectIdCollection """
        pass

    def GetProfileViewIds(self):
        """ GetProfileViewIds(self: Alignment) -> ObjectIdCollection """
        pass

    def GetRegions(self):
        """ GetRegions(self: Alignment) -> AlignmentRegionCollection """
        pass

    def GetSampleLineGroupIds(self):
        """ GetSampleLineGroupIds(self: Alignment) -> ObjectIdCollection """
        pass

    def GetStationSet(self, stationType, *__args):
        """
        GetStationSet(self: Alignment, stationType: StationTypes, majorInterval: float, minorInterval: float) -> Array[Station]
        GetStationSet(self: Alignment, stationType: StationTypes, interval: float) -> Array[Station]
        GetStationSet(self: Alignment, stationType: StationTypes) -> Array[Station]
        """
        pass

    def GetStationStringWithEquations(self, rawStation):
        """ GetStationStringWithEquations(self: Alignment, rawStation: float) -> str """
        pass

    def ImportLabelSet(self, *__args):
        """ ImportLabelSet(self: Alignment, labelSetStyleId: ObjectId)ImportLabelSet(self: Alignment, labelSetStyleName: str) """
        pass

    def PointLocation(self, station, offset, *__args):
        """
        PointLocation(self: Alignment, station: float, offset: float, easting: float, northing: float) -> (float, float)
        PointLocation(self: Alignment, station: float, offset: float, tolerance: float, easting: float, northing: float, Bearing: float) -> (float, float, float)
        """
        pass

    def Reverse(self):
        """ Reverse(self: Alignment) """
        pass

    def StationOffset(self, easting, northing, *__args):
        """
        StationOffset(self: Alignment, easting: float, northing: float, station: float, offset: float) -> (float, float)
        StationOffset(self: Alignment, easting: float, northing: float, tolerance: float, station: float, offset: float) -> (float, float)
        """
        pass

    def Update(self):
        """ Update(self: Alignment) """
        pass

    AlignmentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentType(self: Alignment) -> AlignmentType

"""

    CANTCriticalStaitons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CANTCriticalStaitons(self: Alignment) -> CANTCriticalStationCollection

"""

    CANTCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CANTCurves(self: Alignment) -> CANTCurveCollection

"""

    CreationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationMode(self: Alignment) -> AlignmentCreationType

"""

    CriteriaFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CriteriaFileName(self: Alignment) -> str

Set: CriteriaFileName(self: Alignment) = value
"""

    DesignCheckSetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignCheckSetId(self: Alignment) -> ObjectId

Set: DesignCheckSetId(self: Alignment) = value
"""

    DesignCheckSetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignCheckSetName(self: Alignment) -> str

Set: DesignCheckSetName(self: Alignment) = value
"""

    DesignSpeeds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignSpeeds(self: Alignment) -> DesignSpeedCollection

"""

    EndingStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndingStation(self: Alignment) -> float

"""

    EndingStationWithEquations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndingStationWithEquations(self: Alignment) -> float

"""

    Entities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entities(self: Alignment) -> AlignmentEntityCollection

"""

    HasRoundabout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasRoundabout(self: Alignment) -> bool

"""

    IsConnectedAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnectedAlignment(self: Alignment) -> bool

"""

    IsOffsetAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOffsetAlignment(self: Alignment) -> bool

"""

    IsSiteless = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSiteless(self: Alignment) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Alignment) -> float

"""

    OffsetAlignmentInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetAlignmentInfo(self: Alignment) -> OffsetAlignmentInfo

"""

    RailAlignmentInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RailAlignmentInfo(self: Alignment) -> RailAlignmentInfo

"""

    ReferencePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencePoint(self: Alignment) -> Point2d

Set: ReferencePoint(self: Alignment) = value
"""

    ReferencePointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencePointStation(self: Alignment) -> float

Set: ReferencePointStation(self: Alignment) = value
"""

    SiteId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SiteId(self: Alignment) -> ObjectId

"""

    SiteName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SiteName(self: Alignment) -> str

"""

    StartingStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartingStation(self: Alignment) -> float

"""

    StationEquations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationEquations(self: Alignment) -> StationEquationCollection

"""

    StationIndexIncrement = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationIndexIncrement(self: Alignment) -> float

Set: StationIndexIncrement(self: Alignment) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Alignment) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: Alignment) = value
"""

    SuperelevationCriticalStations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperelevationCriticalStations(self: Alignment) -> SuperelevationCriticalStationCollection

"""

    SuperelevationCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperelevationCurves(self: Alignment) -> SuperelevationCurveCollection

"""

    SuperelevationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperelevationType(self: Alignment) -> SuperelevationType

"""

    UpdateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateMode(self: Alignment) -> AlignmentUpdateType

"""

    UseDesignCheckSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDesignCheckSet(self: Alignment) -> bool

Set: UseDesignCheckSet(self: Alignment) = value
"""

    UseDesignCriteriaFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDesignCriteriaFile(self: Alignment) -> bool

Set: UseDesignCriteriaFile(self: Alignment) = value
"""

    UseDesignSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDesignSpeed(self: Alignment) -> bool

Set: UseDesignSpeed(self: Alignment) = value
"""



class AlignmentEntity(DisposableWrapper):
    # no doc
    def CreateAlignmentSubEntity(self, *args): #cannot find CLR method
        """ CreateAlignmentSubEntity(self: AlignmentEntity, subEntityType: kHintSubEntityType) -> AlignmentSubEntity """
        pass

    def DesignChecks(self):
        """ DesignChecks(self: AlignmentEntity) -> Collection[AlignmentDesignCheck] """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: AlignmentEntity, obj: object) -> bool """
        pass

    def getSubEntities(self, *args): #cannot find CLR method
        """ getSubEntities(self: AlignmentEntity, : vector<std::pair<AeccGeCurveBase const \*\,enum AeccHAlignment::kHintSubEntityType>\,std::allocator<std::pair<AeccGeCurveBase const \*\,enum AeccHAlignment::kHintSubEntityType> > >*) -> vector<std::pair<AeccGeCurveBase const \*\,enum AeccHAlignment::kHintSubEntityType>\,std::allocator<std::pair<AeccGeCurveBase const \*\,enum AeccHAlignment::kHintSubEntityType> > >* """
        pass

    def getSubEntityType(self, *args): #cannot find CLR method
        """ getSubEntityType(self: AlignmentEntity, index: int) -> kHintSubEntityType """
        pass

    def InternalCheckRGObjectSubEntity(self, *args): #cannot find CLR method
        """ InternalCheckRGObjectSubEntity(self: AlignmentEntity, pRGObj: AeccGeCurveBase*) """
        pass

    def InternalGetRGObject(self, *args): #cannot find CLR method
        """ InternalGetRGObject(self: AlignmentEntity) -> AeccRGObject* """
        pass

    def ValidateDesignCheck(self, designCheck):
        """ ValidateDesignCheck(self: AlignmentEntity, designCheck: AlignmentDesignCheck) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Constraint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint1(self: AlignmentEntity) -> AlignmentEntityConstraintType

"""

    EntityAfter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityAfter(self: AlignmentEntity) -> int

"""

    EntityBefore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityBefore(self: AlignmentEntity) -> int

"""

    EntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityId(self: AlignmentEntity) -> int

"""

    EntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityType(self: AlignmentEntity) -> AlignmentEntityType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SubEntityCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityCount(self: AlignmentEntity) -> int

"""



class AlignmentCurve(AlignmentEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: AlignmentCurve) -> Point2d

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: AlignmentCurve) -> float

"""

    HighestDesignSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighestDesignSpeed(self: AlignmentCurve) -> float

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: AlignmentCurve) -> float

Set: Length(self: AlignmentCurve) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: AlignmentCurve) -> Point2d

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: AlignmentCurve) -> float

"""



class AlignmentArc(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: AlignmentArc) -> Point2d

Set: CenterPoint(self: AlignmentArc) = value
"""

    ChordDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChordDirection(self: AlignmentArc) -> float

"""

    ChordLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChordLength(self: AlignmentArc) -> float

Set: ChordLength(self: AlignmentArc) = value
"""

    Clockwise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Clockwise(self: AlignmentArc) -> bool

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentArc) -> AlignmentArcConstraintType

"""

    CurveGroupIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupIndex(self: AlignmentArc) -> str

Set: CurveGroupIndex(self: AlignmentArc) = value
"""

    CurveGroupSubEntityIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupSubEntityIndex(self: AlignmentArc) -> str

Set: CurveGroupSubEntityIndex(self: AlignmentArc) = value
"""

    DeflectedAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeflectedAngle(self: AlignmentArc) -> float

Set: DeflectedAngle(self: AlignmentArc) = value
"""

    Delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Delta(self: AlignmentArc) -> float

Set: Delta(self: AlignmentArc) = value
"""

    DirectionAtPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionAtPoint1(self: AlignmentArc) -> float

Set: DirectionAtPoint1(self: AlignmentArc) = value
"""

    DirectionAtPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionAtPoint2(self: AlignmentArc) -> float

Set: DirectionAtPoint2(self: AlignmentArc) = value
"""

    EndDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDirection(self: AlignmentArc) -> float

"""

    ExternalSecant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalSecant(self: AlignmentArc) -> float

Set: ExternalSecant(self: AlignmentArc) = value
"""

    ExternalTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalTangent(self: AlignmentArc) -> float

Set: ExternalTangent(self: AlignmentArc) = value
"""

    GreaterThan180 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GreaterThan180(self: AlignmentArc) -> bool

Set: GreaterThan180(self: AlignmentArc) = value
"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Length(self: AlignmentArc) = value
"""

    MidOrdinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidOrdinate(self: AlignmentArc) -> float

Set: MidOrdinate(self: AlignmentArc) = value
"""

    MinimumRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumRadius(self: AlignmentArc) -> float

"""

    PassThroughPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint1(self: AlignmentArc) -> Point2d

Set: PassThroughPoint1(self: AlignmentArc) = value
"""

    PassThroughPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint2(self: AlignmentArc) -> Point2d

Set: PassThroughPoint2(self: AlignmentArc) = value
"""

    PassThroughPoint3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint3(self: AlignmentArc) -> Point2d

Set: PassThroughPoint3(self: AlignmentArc) = value
"""

    PIStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PIStation(self: AlignmentArc) -> float

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: AlignmentArc) -> float

Set: Radius(self: AlignmentArc) = value
"""

    ReverseCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseCurve(self: AlignmentArc) -> bool

"""

    StartDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDirection(self: AlignmentArc) -> float

"""



class AlignmentArcConstraintType(Enum):
    """ enum AlignmentArcConstraintType, values: BestFitArc (784), CenterPassThroughPoint (771), CenterRadius (770), PassThrough (776), PassThroughDirection (774), PassThroughHoldEnd (773), PassThroughRadius (772), Radius (775), RadiusAndLength (777), ThreePoints (769) """
    BestFitArc = None
    CenterPassThroughPoint = None
    CenterRadius = None
    PassThrough = None
    PassThroughDirection = None
    PassThroughHoldEnd = None
    PassThroughRadius = None
    Radius = None
    RadiusAndLength = None
    ThreePoints = None
    value__ = None


class LabelBase(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    AllowsAnchorMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsAnchorMarker(self: LabelBase) -> bool

"""

    AllowsDimensionAnchors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsDimensionAnchors(self: LabelBase) -> bool

"""

    AllowsDragging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsDragging(self: LabelBase) -> bool

"""

    AllowsFlipping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsFlipping(self: LabelBase) -> bool

"""

    AllowsLeaderAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsLeaderAttachment(self: LabelBase) -> bool

"""

    AllowsPinning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsPinning(self: LabelBase) -> bool

"""

    AllowsReversing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsReversing(self: LabelBase) -> bool

"""

    AutoStagger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoStagger(self: LabelBase) -> StaggerLabelType

Set: AutoStagger(self: LabelBase) = value
"""

    DefaultDimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorOption(self: LabelBase) -> DimensionAnchorOptionType

Set: DefaultDimensionAnchorOption(self: LabelBase) = value
"""

    DefaultDimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorValue(self: LabelBase) -> float

Set: DefaultDimensionAnchorValue(self: LabelBase) = value
"""

    FeatureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureId(self: LabelBase) -> ObjectId

"""

    LabelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelType(self: LabelBase) -> LabelType

"""

    Mask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mask(self: LabelBase) -> LabelMaskType

Set: Mask(self: LabelBase) = value
"""

    RotationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationType(self: LabelBase) -> LabelRotationType

"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewId(self: LabelBase) -> ObjectId

"""


    m_SubData = None


class LabelGroup(LabelBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAt(self, index):
        """ GetAt(self: LabelGroup, index: UInt32) -> LabelGroupSubEntity """
        pass

    def ResetAllSubCommonLabelLocations(self):
        """ ResetAllSubCommonLabelLocations(self: LabelGroup) """
        pass

    def ResetAllSubCommonLabelProperties(self):
        """ ResetAllSubCommonLabelProperties(self: LabelGroup) """
        pass

    def ResetAllSubCommonLabels(self):
        """ ResetAllSubCommonLabels(self: LabelGroup) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    DefaultDimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorOption(self: LabelGroup) -> DimensionAnchorOptionType

Set: DefaultDimensionAnchorOption(self: LabelGroup) = value
"""

    DefaultDimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorValue(self: LabelGroup) -> float

Set: DefaultDimensionAnchorValue(self: LabelGroup) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: LabelGroup) -> ObjectId

Set: StyleId(self: LabelGroup) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: LabelGroup) -> str

Set: StyleName(self: LabelGroup) = value
"""

    SubEntities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntities(self: LabelGroup) -> IList[LabelGroupSubEntity]

"""

    SubEntityCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityCount(self: LabelGroup) -> UInt32

"""


    m_SubData = None


class AutoFeatureLabelGroup(LabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetFeatureEndStation(self, *args): #cannot find CLR method
        """ GetFeatureEndStation(self: AutoFeatureLabelGroup) -> float """
        pass

    def GetFeatureStartStation(self, *args): #cannot find CLR method
        """ GetFeatureStartStation(self: AutoFeatureLabelGroup) -> float """
        pass

    def SetRange(self, rangeStart, rangeEnd):
        """ SetRange(self: AutoFeatureLabelGroup, rangeStart: float, rangeEnd: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    RangeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeEnd(self: AutoFeatureLabelGroup) -> float

Set: RangeEnd(self: AutoFeatureLabelGroup) = value
"""

    RangeEndFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeEndFromFeature(self: AutoFeatureLabelGroup) -> bool

Set: RangeEndFromFeature(self: AutoFeatureLabelGroup) = value
"""

    RangeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeStart(self: AutoFeatureLabelGroup) -> float

Set: RangeStart(self: AutoFeatureLabelGroup) = value
"""

    RangeStartFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeStartFromFeature(self: AutoFeatureLabelGroup) -> bool

Set: RangeStartFromFeature(self: AutoFeatureLabelGroup) = value
"""


    m_SubData = None


class AlignmentLabelGroup(AutoFeatureLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(rxClass, alignmentId, includeDerived):
        """ GetAvailableLabelGroupIds(rxClass: RXClass, alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(rxClass, alignmentId, includeDerived):
        """ GetAvailableLabelGroups(rxClass: RXClass, alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentCantLabelGroup(AlignmentLabelGroup):
    # no doc
    @staticmethod
    def Create(alignmentId, styleId=None):
        """
        Create(alignmentId: ObjectId, styleId: ObjectId) -> ObjectId
        Create(alignmentId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection """
        pass

    def GetGeometryPointsOptions(self):
        """ GetGeometryPointsOptions(self: AlignmentCantLabelGroup) -> GeometryPointSelector[CantPointType] """
        pass

    def SetGeometryPointsOptions(self, transitionPointsOptions):
        """ SetGeometryPointsOptions(self: AlignmentCantLabelGroup, transitionPointsOptions: GeometryPointSelector[CantPointType]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentCCRC(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Arc1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc1(self: AlignmentCCRC) -> AlignmentSubEntityArc

"""

    Arc2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc2(self: AlignmentCCRC) -> AlignmentSubEntityArc

"""

    Arc3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc3(self: AlignmentCCRC) -> AlignmentSubEntityArc

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentCCRC) -> AlignmentCCRCConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class AlignmentCCRCConstraintType(Enum):
    """ enum AlignmentCCRCConstraintType, values: TransitionLengthRadius1Radius2Radius3 (3073) """
    TransitionLengthRadius1Radius2Radius3 = None
    value__ = None


class AlignmentCRC(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Arc1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc1(self: AlignmentCRC) -> AlignmentSubEntityArc

"""

    Arc2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc2(self: AlignmentCRC) -> AlignmentSubEntityArc

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentCRC) -> AlignmentCRCConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class AlignmentCRCConstraintType(Enum):
    """ enum AlignmentCRCConstraintType, values: Radius1 (3073), Radius2 (3074) """
    Radius1 = None
    Radius2 = None
    value__ = None


class AlignmentCreationType(Enum):
    """ enum AlignmentCreationType, values: ManuallyCreation (2), RuleBasedCreation (1) """
    ManuallyCreation = None
    RuleBasedCreation = None
    value__ = None


class AlignmentCTC(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Arc1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc1(self: AlignmentCTC) -> AlignmentSubEntityArc

"""

    Arc2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc2(self: AlignmentCTC) -> AlignmentSubEntityArc

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentCTC) -> AlignmentCTCConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Tangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tangent(self: AlignmentCTC) -> AlignmentSubEntityLine

"""



class AlignmentCTCConstraintType(Enum):
    """ enum AlignmentCTCConstraintType, values: RadiusRadiusLength (2817) """
    RadiusRadiusLength = None
    value__ = None


class Label(LabelBase):
    # no doc
    def checkStyleId(self, *args): #cannot find CLR method
        """ checkStyleId(self: Label, styleId: ObjectId) """
        pass

    def ClearAllTextComponentOverrides(self):
        """ ClearAllTextComponentOverrides(self: Label) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetReferenceTextTarget(self, referenceTextComponentId):
        """ GetReferenceTextTarget(self: Label, referenceTextComponentId: ObjectId) -> ObjectId """
        pass

    def GetTextComponentIds(self):
        """ GetTextComponentIds(self: Label) -> ObjectIdCollection """
        pass

    def GetTextComponentJustificationOverride(self, labelStyleComponentId):
        """ GetTextComponentJustificationOverride(self: Label, labelStyleComponentId: ObjectId) -> TextJustificationType """
        pass

    def GetTextComponentOverride(self, labelStyleComponentId):
        """ GetTextComponentOverride(self: Label, labelStyleComponentId: ObjectId) -> str """
        pass

    def IsTextComponentOverriden(self, labelStyleComponentId):
        """ IsTextComponentOverriden(self: Label, labelStyleComponentId: ObjectId) -> bool """
        pass

    def Reset(self):
        """ Reset(self: Label) """
        pass

    def ResetLocation(self):
        """ ResetLocation(self: Label) """
        pass

    def ResetProperties(self):
        """ ResetProperties(self: Label) """
        pass

    def SetReferenceTextTarget(self, referenceTextComponentId, referenceObjectId):
        """ SetReferenceTextTarget(self: Label, referenceTextComponentId: ObjectId, referenceObjectId: ObjectId) """
        pass

    def SetTextComponentJustificationOverride(self, labelStyleComponentId, textJustificationType):
        """ SetTextComponentJustificationOverride(self: Label, labelStyleComponentId: ObjectId, textJustificationType: TextJustificationType) """
        pass

    def SetTextComponentOverride(self, labelStyleComponentId, textOverride, textJustificationType=None):
        """ SetTextComponentOverride(self: Label, labelStyleComponentId: ObjectId, textOverride: str)SetTextComponentOverride(self: Label, labelStyleComponentId: ObjectId, textOverride: str, textJustificationType: TextJustificationType) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    AnchorInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorInfo(self: Label) -> AnchorInfo

"""

    AnchorMarkerRotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorMarkerRotationAngle(self: Label) -> float

Set: AnchorMarkerRotationAngle(self: Label) = value
"""

    AnchorMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorMarkerStyleId(self: Label) -> ObjectId

Set: AnchorMarkerStyleId(self: Label) = value
"""

    CanRotate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRotate(self: Label) -> bool

"""

    DimensionAnchorInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorInfo(self: Label) -> AnchorInfo

"""

    DimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorOption(self: Label) -> DimensionAnchorOptionType

Set: DimensionAnchorOption(self: Label) = value
"""

    DimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorValue(self: Label) -> float

Set: DimensionAnchorValue(self: Label) = value
"""

    Dragged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dragged(self: Label) -> bool

"""

    DraggedOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DraggedOffset(self: Label) -> Vector3d

Set: DraggedOffset(self: Label) = value
"""

    Flipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flipped(self: Label) -> bool

Set: Flipped(self: Label) = value
"""

    LabelLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelLocation(self: Label) -> Point3d

Set: LabelLocation(self: Label) = value
"""

    LeaderAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderAttachment(self: Label) -> LeaderAttachmentBehaviorType

Set: LeaderAttachment(self: Label) = value
"""

    LeaderTailVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderTailVisibility(self: Label) -> LeaderTailVisibilityType

Set: LeaderTailVisibility(self: Label) = value
"""

    LeaderVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderVisibility(self: Label) -> LeaderVisibilityType

Set: LeaderVisibility(self: Label) = value
"""

    Pinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pinned(self: Label) -> bool

Set: Pinned(self: Label) = value
"""

    Reversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reversed(self: Label) -> bool

Set: Reversed(self: Label) = value
"""

    RotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationAngle(self: Label) -> float

Set: RotationAngle(self: Label) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: Label) -> ObjectId

Set: StyleId(self: Label) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: Label) -> str

Set: StyleName(self: Label) = value
"""


    m_SubData = None


class FeatureLabel(Label):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetFeatureAnchorDefinition(self, *args): #cannot find CLR method
        """ GetFeatureAnchorDefinition(entity: AlignmentEntity, anchorDef: AeccFeatureAnchorDefinition*)GetFeatureAnchorDefinition(subEntity: AlignmentSubEntity, anchorDef: AeccFeatureAnchorDefinition*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentCurveLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(entity: AlignmentArc, labelStyleId: ObjectId) -> ObjectId
        Create(subEntityArc: AlignmentSubEntityArc, labelStyleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentDesignSpeedLabelGroup(AlignmentLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, alignmentId):
        """ Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(alignmentId, includeDerived):
        """ GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentEntityCollection(CivilWrapper<AeccDbAlignment>):
    # no doc
    def AddFixedCurve(self, *__args):
        """
        AddFixedCurve(self: AlignmentEntityCollection, centerPoint: Point3d, passThroughPoint: Point3d, isClockwise: bool) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, passThroughPoint1: Point3d, directionAtPassThroughPoint1: Vector3d, passThroughPoint2: Point3d) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, previousEntityId: int, startPoint: Point3d, middlePoint: Point3d, endPoint: Point3d) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, centerPoint: Point3d, radius: float, isClockwise: bool) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, passThroughPoint1: Point3d, passThroughPoint2: Point3d, directionAtPassThroughPoint2: Vector3d) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, passThroughPoint1: Point3d, directionAtPassThroughPoint1: Vector3d, radius: float, isClockwise: bool) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, previousEntityId: int, passThroughPoint: Point3d) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, passThroughPoint1: Point3d, passThroughPoint2: Point3d, radius: float, isClockwise: bool) -> AlignmentArc
        AddFixedCurve(self: AlignmentEntityCollection, previousEntityId: int, passThroughPoint1: Point3d, passThroughPoint2: Point3d, radius: float, isClockwise: bool, isGreaterThan180: bool) -> AlignmentArc
        """
        pass

    def AddFixedLine(self, *__args):
        """
        AddFixedLine(self: AlignmentEntityCollection, previousEntityId: int, startPoint: Point3d, endPoint: Point3d) -> AlignmentLine
        AddFixedLine(self: AlignmentEntityCollection, startPoint: Point3d, endPoint: Point3d) -> AlignmentLine
        AddFixedLine(self: AlignmentEntityCollection, previousEntityId: int, distance: float) -> AlignmentLine
        """
        pass

    def AddFixedSpiral(self, previousEntityId, *__args):
        """
        AddFixedSpiral(self: AlignmentEntityCollection, previousEntityId: int, startPoint: Point3d, spiralPI: Point3d, startRadius: float, endRadius: float, length: float, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSpiral
        AddFixedSpiral(self: AlignmentEntityCollection, previousEntityId: int, startPoint: Point3d, spiralPI: Point3d, radius: float, length: float, spiralCurveType: SpiralCurveType, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSpiral
        AddFixedSpiral(self: AlignmentEntityCollection, previousEntityId: int, startPoint: Point3d, spiralPI: Point3d, endPoint: Point3d, definitionType: SpiralType) -> AlignmentSpiral
        AddFixedSpiral(self: AlignmentEntityCollection, previousEntityId: int, startRadius: float, endRadius: float, length: float, spiralDefinition: SpiralType) -> AlignmentSpiral
        AddFixedSpiral(self: AlignmentEntityCollection, previousEntityId: int, radius: float, length: float, spiralCurveType: SpiralCurveType, spiralDefinition: SpiralType) -> AlignmentSpiral
        """
        pass

    def AddFloatingArcWithSpiral(self, attachEntityId, attachType, spParam, spType, radius, *__args):
        """
        AddFloatingArcWithSpiral(self: AlignmentEntityCollection, attachEntityId: int, attachType: EntityAttachType, spParam: float, spType: SpiralParamType, radius: float, passThroughPoint: Point3d, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSCS
        AddFloatingArcWithSpiral(self: AlignmentEntityCollection, attachEntityId: int, attachType: EntityAttachType, spParam: float, spType: SpiralParamType, radius: float, arcLength: float, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSCS
        """
        pass

    def AddFloatingCSS(self, nextEntityId, *__args):
        """
        AddFloatingCSS(self: AlignmentEntityCollection, nextEntityId: int, radius: float, passThroughPoint: Point3d, sp3Param: float, sp4Param: float, spType: SpiralParamType, spiralDefinition: SpiralType) -> AlignmentSSCSS
        AddFloatingCSS(self: AlignmentEntityCollection, nextEntityId: int, passThroughPoint1: Point3d, passThroughPoint2: Point3d, sp3Param: float, sp4Param: float, spType: SpiralParamType, spiralDefinition: SpiralType) -> AlignmentSSCSS
        """
        pass

    def AddFloatingCurve(self, *__args):
        """
        AddFloatingCurve(self: AlignmentEntityCollection, passThroughPoint: Point3d, nextEntityId: int) -> AlignmentArc
        AddFloatingCurve(self: AlignmentEntityCollection, passThroughPoint: Point3d, radius: float, isGreaterThan180: bool, curveType: CurveType, nextEntityId: int) -> AlignmentArc
        AddFloatingCurve(self: AlignmentEntityCollection, previousEntityId: int, passThroughPoint: Point3d, radius: float, isGreaterThan180: bool, curveType: CurveType) -> AlignmentArc
        AddFloatingCurve(self: AlignmentEntityCollection, passThroughPoint: Point3d, directionAtPassThroughPoint: Vector3d, nextEntityId: int) -> AlignmentArc
        AddFloatingCurve(self: AlignmentEntityCollection, previousEntityId: int, radius: float, paramValue: float, paramType: CurveParamType, isClockwise: bool) -> AlignmentArc
        AddFloatingCurve(self: AlignmentEntityCollection, radius: float, paramValue: float, paramType: CurveParamType, isClockwise: bool, nextEntityId: int) -> AlignmentArc
        AddFloatingCurve(self: AlignmentEntityCollection, previousEntityId: int, passThroughPoint: Point3d, directionAtPassThroughPoint: Vector3d) -> AlignmentArc
        AddFloatingCurve(self: AlignmentEntityCollection, previousEntityId: int, passThroughPoint: Point3d) -> AlignmentArc
        """
        pass

    def AddFloatingLine(self, *__args):
        """
        AddFloatingLine(self: AlignmentEntityCollection, previousEntityId: int, length: float) -> AlignmentLine
        AddFloatingLine(self: AlignmentEntityCollection, previousEntityId: int, passThroughPoint: Point3d) -> AlignmentLine
        AddFloatingLine(self: AlignmentEntityCollection, length: float, nextEntityId: int) -> AlignmentLine
        AddFloatingLine(self: AlignmentEntityCollection, passThroughPoint: Point3d, nextEntityId: int) -> AlignmentLine
        """
        pass

    def AddFloatingLineWithSpiral(self, attachEntityId, attachType, spParam, spType, *__args):
        """
        AddFloatingLineWithSpiral(self: AlignmentEntityCollection, attachEntityId: int, attachType: EntityAttachType, spParam: float, spType: SpiralParamType, passThroughPoint: Point3d, spiralDefinition: SpiralType) -> AlignmentSTS
        AddFloatingLineWithSpiral(self: AlignmentEntityCollection, attachEntityId: int, attachType: EntityAttachType, spParam: float, spType: SpiralParamType, tanLength: float, spiralDefinition: SpiralType) -> AlignmentSTS
        """
        pass

    def AddFloatingSSC(self, previousEntityId, sp1Param, sp2Param, spType, *__args):
        """
        AddFloatingSSC(self: AlignmentEntityCollection, previousEntityId: int, sp1Param: float, sp2Param: float, spType: SpiralParamType, radius: float, passThroughPoint: Point3d, spiralDefinition: SpiralType) -> AlignmentSSCSS
        AddFloatingSSC(self: AlignmentEntityCollection, previousEntityId: int, sp1Param: float, sp2Param: float, spType: SpiralParamType, passThroughPoint1: Point3d, passThroughPoint2: Point3d, spiralDefinition: SpiralType) -> AlignmentSSCSS
        """
        pass

    def AddFloatSpiral(self, *__args):
        """
        AddFloatSpiral(self: AlignmentEntityCollection, previousEntityId: int, radius: float, length: float, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSpiral
        AddFloatSpiral(self: AlignmentEntityCollection, radius: float, length: float, nextEntityId: int, isClockwise: bool, spiralDefinition: SpiralType) -> AlignmentSpiral
        """
        pass

    def AddFreeCurve(self, previousEntityId, nextEntityId, *__args):
        """
        AddFreeCurve(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, paramValue: float, paramType: CurveParamType, isGreaterThan180: bool, curveType: CurveType) -> AlignmentArc
        AddFreeCurve(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, passThroughPoint: Point3d) -> AlignmentArc
        """
        pass

    def AddFreeLine(self, previousEntityId, nextEntityId):
        """ AddFreeLine(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int) -> AlignmentLine """
        pass

    def AddFreeSCS(self, previousEntityId, nextEntityId, spiral1Param, spiral2Param, spType, radius, isGreaterThan180, spiralDefinition):
        """ AddFreeSCS(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, spiral1Param: float, spiral2Param: float, spType: SpiralParamType, radius: float, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSCS """
        pass

    def AddFreeSCSCS(self, previousEntityId, nextEntityId, constraintValue, spiralDefinition):
        """ AddFreeSCSCS(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, constraintValue: SCSCSConstraints, spiralDefinition: SpiralType) -> AlignmentSCSCS """
        pass

    def AddFreeSCSSCS(self, previousEntityId, nextEntityId, constraintValue, spiralDefinition):
        """ AddFreeSCSSCS(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, constraintValue: SCSSCSConstraints, spiralDefinition: SpiralType) -> AlignmentSCSSCS """
        pass

    def AddFreeSpiral(self, previousEntityId, nextEntityId, spParam, spType, spiralCurveType, spiralDefinition):
        """ AddFreeSpiral(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, spParam: float, spType: SpiralParamType, spiralCurveType: SpiralCurveType, spiralDefinition: SpiralType) -> AlignmentSCS """
        pass

    def AddFreeSSBetweenCurves(self, previousEntityId, nextEntityId, spRatio, spType, spiralDefinition):
        """ AddFreeSSBetweenCurves(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, spRatio: float, spType: SpiralParamType, spiralDefinition: SpiralType) -> AlignmentSTS """
        pass

    def AddFreeSSBetweenTangents(self, previousEntityId, nextEntityId, spiral1Param, spiral2Param, spType, isGreaterThan180, spiralDefinition):
        """ AddFreeSSBetweenTangents(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, spiral1Param: float, spiral2Param: float, spType: SpiralParamType, isGreaterThan180: bool, spiralDefinition: SpiralType) -> AlignmentSCS """
        pass

    def AddFreeSTS(self, previousEntityId, nextEntityId, *__args):
        """
        AddFreeSTS(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, sp1Param: float, sp2Param: float, spType: SpiralParamType, spiralDefinition: SpiralType) -> AlignmentSTS
        AddFreeSTS(self: AlignmentEntityCollection, previousEntityId: int, nextEntityId: int, tanLength: float, spiralDefinition: SpiralType) -> AlignmentSTS
        """
        pass

    def Clear(self):
        """ Clear(self: AlignmentEntityCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    def EntityAtId(self, id):
        """ EntityAtId(self: AlignmentEntityCollection, id: int) -> AlignmentEntity """
        pass

    def EntityAtStation(self, rawStation):
        """ EntityAtStation(self: AlignmentEntityCollection, rawStation: float) -> AlignmentEntity """
        pass

    def GetEntityByOrder(self, index):
        """ GetEntityByOrder(self: AlignmentEntityCollection, index: int) -> AlignmentEntity """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AlignmentEntityCollection) -> IEnumerator[AlignmentEntity] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AlignmentEntityCollection) -> IEnumerator """
        pass

    def Remove(self, entity):
        """ Remove(self: AlignmentEntityCollection, entity: AlignmentEntity) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: AlignmentEntityCollection, index: int) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AlignmentEntity](enumerable: IEnumerable[AlignmentEntity], value: AlignmentEntity) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AlignmentEntityCollection) -> int

"""

    FirstEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstEntity(self: AlignmentEntityCollection) -> int

"""

    LastEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastEntity(self: AlignmentEntityCollection) -> int

"""



class AlignmentEntityConstraintType(Enum):
    """ enum AlignmentEntityConstraintType, values: Fixed (289), FloatOnNext (291), FloatOnPrev (290), Free (292) """
    Fixed = None
    FloatOnNext = None
    FloatOnPrev = None
    Free = None
    value__ = None


class AlignmentEntityType(Enum):
    """ enum AlignmentEntityType, values: Arc (258), CurveCurveReverseCurve (275), CurveLineCurve (273), CurveReverseCurve (274), CurveSpiral (265), CurveSpiralSpiral (272), Line (257), LineSpiral (263), MultipleSegments (267), Spiral (259), SpiralCurve (264), SpiralCurveSpiral (260), SpiralCurveSpiralCurveSpiral (268), SpiralCurveSpiralSpiralCurveSpiral (269), SpiralLine (262), SpiralLineSpiral (261), SpiralSpiral (270), SpiralSpiralCurve (271), SpiralSpiralCurveSpiralSpiral (266) """
    Arc = None
    CurveCurveReverseCurve = None
    CurveLineCurve = None
    CurveReverseCurve = None
    CurveSpiral = None
    CurveSpiralSpiral = None
    Line = None
    LineSpiral = None
    MultipleSegments = None
    Spiral = None
    SpiralCurve = None
    SpiralCurveSpiral = None
    SpiralCurveSpiralCurveSpiral = None
    SpiralCurveSpiralSpiralCurveSpiral = None
    SpiralLine = None
    SpiralLineSpiral = None
    SpiralSpiral = None
    SpiralSpiralCurve = None
    SpiralSpiralCurveSpiralSpiral = None
    value__ = None


class AlignmentGeometryPointLabelGroup(AlignmentLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, alignmentId):
        """ Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(alignmentId, includeDerived):
        """ GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    def GetGeometryPointsOptions(self):
        """ GetGeometryPointsOptions(self: AlignmentGeometryPointLabelGroup) -> GeometryPointSelector[AlignmentPointType] """
        pass

    def SetGeometryPointsOptions(self, alignmentGeometryPoints):
        """ SetGeometryPointsOptions(self: AlignmentGeometryPointLabelGroup, alignmentGeometryPoints: GeometryPointSelector[AlignmentPointType]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentGeometryPointStationType(Enum):
    """ enum AlignmentGeometryPointStationType, values: BeginFullSuper (516), BeginNormalCrown (514), BeginNormalShoulder (515), BegOfAlign (257), CPI (271), CurveCompCurve (262), CurveRevCurve (263), CurveSpiral (266), CurveTan (261), EndFullSuper (517), EndNormalCrown (519), EndNormalShoulder (518), EndOfAlign (258), LevelCrown (521), LowShoulderMatch (522), Manual (524), PI (270), ProfileBegOfAlign (280), ProfileCurveCompCurve (275), ProfileCurveHighPoint (278), ProfileCurveLowPoint (277), ProfileCurvePVI (279), ProfileCurveRevCurve (276), ProfileCurveTan (274), ProfileEndOfAlign (281), ProfileOverallHighPoint (284), ProfileOverallLowPoint (283), ProfileTanCurve (273), ProfileTanTan (282), ReverseCrown (523), ShoulderBreakOver (525), SPI (272), SpiralCompSpiral (268), SpiralCurve (267), SpiralRevSpiral (269), SpiralTan (265), TanCurve (260), TanSpiral (264), TanTan (259) """
    BeginFullSuper = None
    BeginNormalCrown = None
    BeginNormalShoulder = None
    BegOfAlign = None
    CPI = None
    CurveCompCurve = None
    CurveRevCurve = None
    CurveSpiral = None
    CurveTan = None
    EndFullSuper = None
    EndNormalCrown = None
    EndNormalShoulder = None
    EndOfAlign = None
    LevelCrown = None
    LowShoulderMatch = None
    Manual = None
    PI = None
    ProfileBegOfAlign = None
    ProfileCurveCompCurve = None
    ProfileCurveHighPoint = None
    ProfileCurveLowPoint = None
    ProfileCurvePVI = None
    ProfileCurveRevCurve = None
    ProfileCurveTan = None
    ProfileEndOfAlign = None
    ProfileOverallHighPoint = None
    ProfileOverallLowPoint = None
    ProfileTanCurve = None
    ProfileTanTan = None
    ReverseCrown = None
    ShoulderBreakOver = None
    SPI = None
    SpiralCompSpiral = None
    SpiralCurve = None
    SpiralRevSpiral = None
    SpiralTan = None
    TanCurve = None
    TanSpiral = None
    TanTan = None
    value__ = None


class AlignmentIndexedPILabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(tangentIn: AlignmentLine, labelStyleId: ObjectId) -> ObjectId
        Create(arc: AlignmentArc, labelStyleId: ObjectId) -> ObjectId
        Create(scs: AlignmentSCS, labelStyleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentLine(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentLine) -> AlignmentLineConstraintType

"""

    CurveGroupIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupIndex(self: AlignmentLine) -> str

Set: CurveGroupIndex(self: AlignmentLine) = value
"""

    CurveGroupSubEntityIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupSubEntityIndex(self: AlignmentLine) -> str

Set: CurveGroupSubEntityIndex(self: AlignmentLine) = value
"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: AlignmentLine) -> float

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Length(self: AlignmentLine) = value
"""

    MidPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidPoint(self: AlignmentLine) -> Point2d

"""

    PassThroughPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint1(self: AlignmentLine) -> Point2d

Set: PassThroughPoint1(self: AlignmentLine) = value
"""

    PassThroughPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint2(self: AlignmentLine) -> Point2d

Set: PassThroughPoint2(self: AlignmentLine) = value
"""



class AlignmentLineConstraintType(Enum):
    """ enum AlignmentLineConstraintType, values: BestFit (517), Length (515), NoConstraint (516), ThroughPoint (514), TwoPoints (513) """
    BestFit = None
    Length = None
    NoConstraint = None
    ThroughPoint = None
    TwoPoints = None
    value__ = None


class AlignmentStationLabelGroup(AlignmentLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, alignmentId, increment):
        """ Create(styleId: ObjectId, alignmentId: ObjectId, increment: float) -> ObjectId """
        pass

    @staticmethod
    def CreateMajor(styleId, alignmentId, increment):
        """ CreateMajor(styleId: ObjectId, alignmentId: ObjectId, increment: float) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId, includeDerived):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(alignmentId, includeDerived):
        """ GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: AlignmentStationLabelGroup) -> float

Set: Increment(self: AlignmentStationLabelGroup) = value
"""

    RangeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeEnd(self: AlignmentStationLabelGroup) = value
"""

    RangeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeStart(self: AlignmentStationLabelGroup) = value
"""


    m_SubData = None


class AlignmentMinorStationLabelGroup(AlignmentStationLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, majorStationId, increment):
        """ Create(styleId: ObjectId, majorStationId: ObjectId, increment: float) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(alignmentId, includeDerived):
        """ GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    def SetRange(self, rangeStart, rangeEnd):
        """ SetRange(self: AlignmentMinorStationLabelGroup, rangeStart: float, rangeEnd: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    MajorStationLabelGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorStationLabelGroup(self: AlignmentMinorStationLabelGroup) -> ObjectId

Set: MajorStationLabelGroup(self: AlignmentMinorStationLabelGroup) = value
"""

    RangeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeEnd(self: AlignmentMinorStationLabelGroup) = value
"""

    RangeEndFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeEndFromFeature(self: AlignmentMinorStationLabelGroup) = value
"""

    RangeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeStart(self: AlignmentMinorStationLabelGroup) = value
"""

    RangeStartFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeStartFromFeature(self: AlignmentMinorStationLabelGroup) = value
"""


    m_SubData = None


class AlignmentMultipleSegments(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentMultipleSegments) -> AlignmentMultipleSegmentsConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SubEntityCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityCount(self: AlignmentMultipleSegments) -> int

"""



class AlignmentMultipleSegmentsConstraintType(Enum):
    """ enum AlignmentMultipleSegmentsConstraintType, values: KeyPoints (2563), RadiiAndLengths (2561), RatiosAndLengths (2562) """
    KeyPoints = None
    RadiiAndLengths = None
    RatiosAndLengths = None
    value__ = None


class AlignmentPILabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(tangentIn: AlignmentLine, labelStyleId: ObjectId) -> ObjectId
        Create(arc: AlignmentArc, labelStyleId: ObjectId) -> ObjectId
        Create(scs: AlignmentSCS, labelStyleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentRegion(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: AlignmentRegion, A_0: bool) """
        pass

    def Split(self):
        """ Split(self: AlignmentRegion) """
        pass

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: AlignmentRegion) -> float

Set: EndStation(self: AlignmentRegion) = value
"""

    EntryTransition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryTransition(self: AlignmentRegion) -> AlignmentTransition

"""

    ExitTransition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExitTransition(self: AlignmentRegion) -> AlignmentTransition

"""

    IncreasedWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncreasedWidth(self: AlignmentRegion) -> float

Set: IncreasedWidth(self: AlignmentRegion) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: AlignmentRegion) -> float

Set: Length(self: AlignmentRegion) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: AlignmentRegion) -> float

Set: Offset(self: AlignmentRegion) = value
"""

    OffsetDist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetDist(self: AlignmentRegion) -> float

Set: OffsetDist(self: AlignmentRegion) = value
"""

    RegionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegionType(self: AlignmentRegion) -> AlignmentRegionType

Set: RegionType(self: AlignmentRegion) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: AlignmentRegion) -> float

Set: StartStation(self: AlignmentRegion) = value
"""

    WideningCriteria = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WideningCriteria(self: AlignmentRegion) -> OffsetAlignmentWideningCriteria

"""



class AlignmentRegionCollection(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AlignmentRegionCollection) -> IEnumerator[AlignmentRegion] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AlignmentRegionCollection) -> IEnumerator """
        pass

    def MergeToNeighborRegion(self, index, preRegion):
        """ MergeToNeighborRegion(self: AlignmentRegionCollection, index: int, preRegion: bool) -> bool """
        pass

    def Remove(self, index):
        """ Remove(self: AlignmentRegionCollection, index: int) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AlignmentRegion](enumerable: IEnumerable[AlignmentRegion], value: AlignmentRegion) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AlignmentRegionCollection) -> int

"""



class AlignmentRegionType(Enum):
    """ enum AlignmentRegionType, values: Automatic (12), Norminal (2), Specific (1) """
    Automatic = None
    Norminal = None
    Specific = None
    value__ = None


class AlignmentSCS(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Arc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc(self: AlignmentSCS) -> AlignmentSubEntityArc

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentSCS) -> AlignmentSCSConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpiralIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralIn(self: AlignmentSCS) -> AlignmentSubEntitySpiral

"""

    SpiralOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralOut(self: AlignmentSCS) -> AlignmentSubEntitySpiral

"""



class AlignmentSCSConstraintType(Enum):
    """ enum AlignmentSCSConstraintType, values: SpInAValSpOutAVal (1031), SpInLenSpOutLen (1030), Spiral1AValRadiusSpiral2AVal (1201), SpiralAVal (1205), SpiralAValRadius (1204), SpiralAValRadiusArcLen (1203), SpiralAValRadiusPassPt (1202), SpiralInRadiusSpiralOut (1025), SpiralLength (1029), SpiralLenRadius (1028), SpiralLenRadiusArcLen (1027), SpiralLenRadiusPassPt (1026), SpiralNoParameter (1206) """
    SpInAValSpOutAVal = None
    SpInLenSpOutLen = None
    Spiral1AValRadiusSpiral2AVal = None
    SpiralAVal = None
    SpiralAValRadius = None
    SpiralAValRadiusArcLen = None
    SpiralAValRadiusPassPt = None
    SpiralInRadiusSpiralOut = None
    SpiralLength = None
    SpiralLenRadius = None
    SpiralLenRadiusArcLen = None
    SpiralLenRadiusPassPt = None
    SpiralNoParameter = None
    value__ = None


class AlignmentSCSCS(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Arc1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc1(self: AlignmentSCSCS) -> AlignmentSubEntityArc

"""

    Arc2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc2(self: AlignmentSCSCS) -> AlignmentSubEntityArc

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentSCSCS) -> AlignmentSCSCSConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Spiral1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral1(self: AlignmentSCSCS) -> AlignmentSubEntitySpiral

"""

    Spiral2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral2(self: AlignmentSCSCS) -> AlignmentSubEntitySpiral

"""

    Spiral3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral3(self: AlignmentSCSCS) -> AlignmentSubEntitySpiral

"""



class AlignmentSCSCSConstraintType(Enum):
    """ enum AlignmentSCSCSConstraintType, values: SpAValAndArc1Angle (2055), SpAValAndArc1Length (2067), SpAValAndArc1PassPt (2056), SpAValAndArc2Angle (2063), SpAValAndArc2Length (2068), SpAValAndArc2PassPt (2064), SpAValAndEndPoint (2062), SpAValAndStartPoint (2054), SpAValAndTanLenIn (2053), SpAValAndTanLenOut (2061), SpLenAndArc1Angle (2051), SpLenAndArc1Length (2065), SpLenAndArc1PassPt (2052), SpLenAndArc2Angle (2059), SpLenAndArc2Length (2066), SpLenAndArc2PassPt (2060), SpLenAndEndPoint (2058), SpLenAndStartPoint (2050), SpLenAndTanLenIn (2049), SpLenAndTanLenOut (2057) """
    SpAValAndArc1Angle = None
    SpAValAndArc1Length = None
    SpAValAndArc1PassPt = None
    SpAValAndArc2Angle = None
    SpAValAndArc2Length = None
    SpAValAndArc2PassPt = None
    SpAValAndEndPoint = None
    SpAValAndStartPoint = None
    SpAValAndTanLenIn = None
    SpAValAndTanLenOut = None
    SpLenAndArc1Angle = None
    SpLenAndArc1Length = None
    SpLenAndArc1PassPt = None
    SpLenAndArc2Angle = None
    SpLenAndArc2Length = None
    SpLenAndArc2PassPt = None
    SpLenAndEndPoint = None
    SpLenAndStartPoint = None
    SpLenAndTanLenIn = None
    SpLenAndTanLenOut = None
    value__ = None


class AlignmentSCSSCS(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Arc1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc1(self: AlignmentSCSSCS) -> AlignmentSubEntityArc

"""

    Arc2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc2(self: AlignmentSCSSCS) -> AlignmentSubEntityArc

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentSCSSCS) -> AlignmentSCSSCSConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Spiral1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral1(self: AlignmentSCSSCS) -> AlignmentSubEntitySpiral

"""

    Spiral2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral2(self: AlignmentSCSSCS) -> AlignmentSubEntitySpiral

"""

    Spiral3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral3(self: AlignmentSCSSCS) -> AlignmentSubEntitySpiral

"""

    Spiral4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral4(self: AlignmentSCSSCS) -> AlignmentSubEntitySpiral

"""



class AlignmentSCSSCSConstraintType(Enum):
    """ enum AlignmentSCSSCSConstraintType, values: SpAValAndArc1Angle (2309), SpAValAndArc1Length (2319), SpAValAndArc1PassPt (2310), SpAValAndArc2Angle (2315), SpAValAndArc2Length (2320), SpAValAndArc2PassPt (2316), SpAValAndEndPoint (2314), SpAValAndStartPoint (2308), SpLenAndArc1Angle (2306), SpLenAndArc1Length (2317), SpLenAndArc1PassPt (2307), SpLenAndArc2Angle (2312), SpLenAndArc2Length (2318), SpLenAndArc2PassPt (2313), SpLenAndEndPoint (2311), SpLenAndStartPoint (2305) """
    SpAValAndArc1Angle = None
    SpAValAndArc1Length = None
    SpAValAndArc1PassPt = None
    SpAValAndArc2Angle = None
    SpAValAndArc2Length = None
    SpAValAndArc2PassPt = None
    SpAValAndEndPoint = None
    SpAValAndStartPoint = None
    SpLenAndArc1Angle = None
    SpLenAndArc1Length = None
    SpLenAndArc1PassPt = None
    SpLenAndArc2Angle = None
    SpLenAndArc2Length = None
    SpLenAndArc2PassPt = None
    SpLenAndEndPoint = None
    SpLenAndStartPoint = None
    value__ = None


class AlignmentSide(Enum):
    """ enum AlignmentSide, values: Both (0), Left (1), Right (2) """
    Both = None
    Left = None
    Right = None
    value__ = None


class AlignmentSpiral(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: AlignmentSpiral) -> float

Set: A(self: AlignmentSpiral) = value
"""

    Compound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Compound(self: AlignmentSpiral) -> bool

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentSpiral) -> AlignmentSpiralConstraintType

"""

    CurveGroupIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupIndex(self: AlignmentSpiral) -> str

Set: CurveGroupIndex(self: AlignmentSpiral) = value
"""

    CurveGroupSubEntityIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupSubEntityIndex(self: AlignmentSpiral) -> str

Set: CurveGroupSubEntityIndex(self: AlignmentSpiral) = value
"""

    CurveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveType(self: AlignmentSpiral) -> SpiralCurveType

"""

    Delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Delta(self: AlignmentSpiral) -> float

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: AlignmentSpiral) -> SpiralDirectionType

"""

    EndDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDirection(self: AlignmentSpiral) -> float

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: K(self: AlignmentSpiral) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Length(self: AlignmentSpiral) = value
"""

    LongTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongTangent(self: AlignmentSpiral) -> float

"""

    MinimumTransitionLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumTransitionLength(self: AlignmentSpiral) -> float

"""

    P = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P(self: AlignmentSpiral) -> float

"""

    RadialPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadialPoint(self: AlignmentSpiral) -> Point2d

"""

    RadiusIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiusIn(self: AlignmentSpiral) -> float

"""

    RadiusOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiusOut(self: AlignmentSpiral) -> float

"""

    ShortTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShortTangent(self: AlignmentSpiral) -> float

"""

    SPIAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SPIAngle(self: AlignmentSpiral) -> float

"""

    SPIPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SPIPoint(self: AlignmentSpiral) -> Point2d

"""

    SpiralDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralDefinition(self: AlignmentSpiral) -> SpiralType

"""

    SPIStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SPIStation(self: AlignmentSpiral) -> float

"""

    StartDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDirection(self: AlignmentSpiral) -> float

"""

    TotalX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalX(self: AlignmentSpiral) -> float

"""

    TotalY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalY(self: AlignmentSpiral) -> float

"""



class AlignmentSpiralConstraintType(Enum):
    """ enum AlignmentSpiralConstraintType, values: StartPtAndDirRadiusLength (1281), StartPtAndDirStartAndEndRadiusLength (1282) """
    StartPtAndDirRadiusLength = None
    StartPtAndDirStartAndEndRadiusLength = None
    value__ = None


class AlignmentSpiralLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(entitySpiral: AlignmentSpiral, labelStyleId: ObjectId) -> ObjectId
        Create(subEntitySpiral: AlignmentSubEntitySpiral, labelStyleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentSSCSS(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Arc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc(self: AlignmentSSCSS) -> AlignmentSubEntityArc

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentSSCSS) -> AlignmentSSCSSConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Spiral1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral1(self: AlignmentSSCSS) -> AlignmentSubEntitySpiral

"""

    Spiral2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral2(self: AlignmentSSCSS) -> AlignmentSubEntitySpiral

"""

    Spiral3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral3(self: AlignmentSSCSS) -> AlignmentSubEntitySpiral

"""

    Spiral4 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spiral4(self: AlignmentSSCSS) -> AlignmentSubEntitySpiral

"""



class AlignmentSSCSSConstraintType(Enum):
    """ enum AlignmentSSCSSConstraintType, values: kSp1AValSp2AValPt1Pt2 (1796), kSp1AValSp2AValRadiusPt (1795), kSp1LenSp2LenPt1Pt2 (1794), kSp1LenSp2LenRadiusPt (1793) """
    kSp1AValSp2AValPt1Pt2 = None
    kSp1AValSp2AValRadiusPt = None
    kSp1LenSp2LenPt1Pt2 = None
    kSp1LenSp2LenRadiusPt = None
    value__ = None


class AlignmentStationEquationLabelGroup(AlignmentLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, alignmentId):
        """ Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(alignmentId, includeDerived):
        """ GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentSTS(AlignmentCurve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: AlignmentSTS) -> AlignmentSTSConstraintType

"""

    InternalConstraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SpiralIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralIn(self: AlignmentSTS) -> AlignmentSubEntitySpiral

"""

    SpiralOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralOut(self: AlignmentSTS) -> AlignmentSubEntitySpiral

"""

    Tangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tangent(self: AlignmentSTS) -> AlignmentSubEntityLine

"""



class AlignmentSTSConstraintType(Enum):
    """ enum AlignmentSTSConstraintType, values: Spiral1AValSpiral2AVal (1539), Spiral1LengthSpiral2Length (1537), SpiralAValTangentLength (1551), SpiralAValTangentPassPt (1550), SpiralLengthTangentLength (1547), SpiralLengthTangentPassPt (1546), TangentLength (1538) """
    Spiral1AValSpiral2AVal = None
    Spiral1LengthSpiral2Length = None
    SpiralAValTangentLength = None
    SpiralAValTangentPassPt = None
    SpiralLengthTangentLength = None
    SpiralLengthTangentPassPt = None
    TangentLength = None
    value__ = None


class AlignmentSubEntity(DisposableWrapper):
    # no doc
    def DesignChecks(self):
        """ DesignChecks(self: AlignmentSubEntity) -> Collection[AlignmentDesignCheck] """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: AlignmentSubEntity, obj: object) -> bool """
        pass

    def ValidateDesignCheck(self, designCheck):
        """ ValidateDesignCheck(self: AlignmentSubEntity, designCheck: AlignmentDesignCheck) -> bool """
        pass

    CurveGroupIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupIndex(self: AlignmentSubEntity) -> str

Set: CurveGroupIndex(self: AlignmentSubEntity) = value
"""

    CurveGroupSubEntityIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveGroupSubEntityIndex(self: AlignmentSubEntity) -> str

Set: CurveGroupSubEntityIndex(self: AlignmentSubEntity) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: AlignmentSubEntity) -> Point2d

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: AlignmentSubEntity) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: AlignmentSubEntity) -> float

Set: Length(self: AlignmentSubEntity) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: AlignmentSubEntity) -> Point2d

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: AlignmentSubEntity) -> float

"""

    SubEntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityType(self: AlignmentSubEntity) -> AlignmentSubEntityType

"""



class AlignmentSubEntityArc(AlignmentSubEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterPoint(self: AlignmentSubEntityArc) -> Point2d

Set: CenterPoint(self: AlignmentSubEntityArc) = value
"""

    ChordDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChordDirection(self: AlignmentSubEntityArc) -> float

"""

    ChordLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChordLength(self: AlignmentSubEntityArc) -> float

Set: ChordLength(self: AlignmentSubEntityArc) = value
"""

    Clockwise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Clockwise(self: AlignmentSubEntityArc) -> bool

"""

    DeflectedAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeflectedAngle(self: AlignmentSubEntityArc) -> float

Set: DeflectedAngle(self: AlignmentSubEntityArc) = value
"""

    Delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Delta(self: AlignmentSubEntityArc) -> float

Set: Delta(self: AlignmentSubEntityArc) = value
"""

    DirectionAtPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionAtPoint1(self: AlignmentSubEntityArc) -> float

Set: DirectionAtPoint1(self: AlignmentSubEntityArc) = value
"""

    DirectionAtPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionAtPoint2(self: AlignmentSubEntityArc) -> float

Set: DirectionAtPoint2(self: AlignmentSubEntityArc) = value
"""

    EndDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDirection(self: AlignmentSubEntityArc) -> float

"""

    ExternalSecant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalSecant(self: AlignmentSubEntityArc) -> float

Set: ExternalSecant(self: AlignmentSubEntityArc) = value
"""

    ExternalTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExternalTangent(self: AlignmentSubEntityArc) -> float

Set: ExternalTangent(self: AlignmentSubEntityArc) = value
"""

    GreaterThan180 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GreaterThan180(self: AlignmentSubEntityArc) -> bool

Set: GreaterThan180(self: AlignmentSubEntityArc) = value
"""

    MidOrdinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidOrdinate(self: AlignmentSubEntityArc) -> float

Set: MidOrdinate(self: AlignmentSubEntityArc) = value
"""

    MinimumRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumRadius(self: AlignmentSubEntityArc) -> float

"""

    PassThroughPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint1(self: AlignmentSubEntityArc) -> Point2d

Set: PassThroughPoint1(self: AlignmentSubEntityArc) = value
"""

    PassThroughPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint2(self: AlignmentSubEntityArc) -> Point2d

Set: PassThroughPoint2(self: AlignmentSubEntityArc) = value
"""

    PassThroughPoint3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint3(self: AlignmentSubEntityArc) -> Point2d

Set: PassThroughPoint3(self: AlignmentSubEntityArc) = value
"""

    PIPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PIPoint(self: AlignmentSubEntityArc) -> Point2d

"""

    PIStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PIStation(self: AlignmentSubEntityArc) -> float

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: AlignmentSubEntityArc) -> float

Set: Radius(self: AlignmentSubEntityArc) = value
"""

    ReverseCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseCurve(self: AlignmentSubEntityArc) -> bool

"""

    StartDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDirection(self: AlignmentSubEntityArc) -> float

"""

    SubEntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityType(self: AlignmentSubEntityArc) -> AlignmentSubEntityType

"""



class AlignmentSubEntityLine(AlignmentSubEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: AlignmentSubEntityLine) -> float

"""

    MidPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidPoint(self: AlignmentSubEntityLine) -> Point2d

"""

    PassThroughPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint1(self: AlignmentSubEntityLine) -> Point2d

Set: PassThroughPoint1(self: AlignmentSubEntityLine) = value
"""

    PassThroughPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassThroughPoint2(self: AlignmentSubEntityLine) -> Point2d

Set: PassThroughPoint2(self: AlignmentSubEntityLine) = value
"""

    SubEntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityType(self: AlignmentSubEntityLine) -> AlignmentSubEntityType

"""



class AlignmentSubEntitySpiral(AlignmentSubEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    A = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: A(self: AlignmentSubEntitySpiral) -> float

Set: A(self: AlignmentSubEntitySpiral) = value
"""

    Compound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Compound(self: AlignmentSubEntitySpiral) -> bool

"""

    CurveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveType(self: AlignmentSubEntitySpiral) -> SpiralCurveType

"""

    Delta = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Delta(self: AlignmentSubEntitySpiral) -> float

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: AlignmentSubEntitySpiral) -> SpiralDirectionType

"""

    EndDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndDirection(self: AlignmentSubEntitySpiral) -> float

"""

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: K(self: AlignmentSubEntitySpiral) -> float

"""

    LongTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongTangent(self: AlignmentSubEntitySpiral) -> float

"""

    MinimumTransitionLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumTransitionLength(self: AlignmentSubEntitySpiral) -> float

"""

    P = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: P(self: AlignmentSubEntitySpiral) -> float

"""

    RadialPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadialPoint(self: AlignmentSubEntitySpiral) -> Point2d

"""

    RadiusIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiusIn(self: AlignmentSubEntitySpiral) -> float

"""

    RadiusOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiusOut(self: AlignmentSubEntitySpiral) -> float

"""

    ShortTangent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShortTangent(self: AlignmentSubEntitySpiral) -> float

"""

    SPIAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SPIAngle(self: AlignmentSubEntitySpiral) -> float

"""

    SPIPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SPIPoint(self: AlignmentSubEntitySpiral) -> Point2d

"""

    SpiralDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralDefinition(self: AlignmentSubEntitySpiral) -> SpiralType

"""

    SPIStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SPIStation(self: AlignmentSubEntitySpiral) -> float

"""

    StartDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDirection(self: AlignmentSubEntitySpiral) -> float

"""

    SubEntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityType(self: AlignmentSubEntitySpiral) -> AlignmentSubEntityType

"""

    TotalX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalX(self: AlignmentSubEntitySpiral) -> float

"""

    TotalY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TotalY(self: AlignmentSubEntitySpiral) -> float

"""



class AlignmentSubEntityType(Enum):
    """ enum AlignmentSubEntityType, values: Arc (1), Line (0), Spiral (2) """
    Arc = None
    Line = None
    Spiral = None
    value__ = None


class AlignmentSuperelevationLabelGroup(AlignmentLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, alignmentId):
        """ Create(styleId: ObjectId, alignmentId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(alignmentId, includeDerived):
        """ GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    def GetGeometryPointsOptions(self):
        """ GetGeometryPointsOptions(self: AlignmentSuperelevationLabelGroup) -> GeometryPointSelector[SuperelevationPointType] """
        pass

    def SetGeometryPointsOptions(self, transitionPoints):
        """ SetGeometryPointsOptions(self: AlignmentSuperelevationLabelGroup, transitionPoints: GeometryPointSelector[SuperelevationPointType]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class Table(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class AlignmentTable(Table):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class AlignmentTangentLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(entityLine: AlignmentLine, labelStyleId: ObjectId) -> ObjectId
        Create(subEntityLine: AlignmentSubEntityLine, labelStyleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class AlignmentTransition(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: AlignmentTransition, A_0: bool) """
        pass

    def Slim(self):
        """ Slim(self: AlignmentTransition) """
        pass

    NextRegion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextRegion(self: AlignmentTransition) -> AlignmentRegion

"""

    PreviousRegion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviousRegion(self: AlignmentTransition) -> AlignmentRegion

"""

    TransitionDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionDescription(self: AlignmentTransition) -> TransitionDescriptionBase

"""

    TransitionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionType(self: AlignmentTransition) -> TransitionType

Set: TransitionType(self: AlignmentTransition) = value
"""



class AlignmentTransitionCollection(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AlignmentTransitionCollection) -> IEnumerator[AlignmentTransition] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AlignmentTransitionCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AlignmentTransition](enumerable: IEnumerable[AlignmentTransition], value: AlignmentTransition) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AlignmentTransitionCollection) -> int

"""



class AlignmentType(Enum):
    """ enum AlignmentType, values: Centerline (1), CurbReturn (3), Offset (2), Rail (5), Utility (4) """
    Centerline = None
    CurbReturn = None
    Offset = None
    Rail = None
    Utility = None
    value__ = None


class AlignmentUpdateType(Enum):
    """ enum AlignmentUpdateType, values: DynamicUpdate (1), StaticUpdate (2) """
    DynamicUpdate = None
    StaticUpdate = None
    value__ = None


class AlignmentVerticalGeometryPointLabelGroup(AlignmentLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, alignmentId, verticalAlignmentId):
        """ Create(styleId: ObjectId, alignmentId: ObjectId, verticalAlignmentId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(alignmentId):
        """ GetAvailableLabelGroupIds(alignmentId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(alignmentId, includeDerived):
        """ GetAvailableLabelGroups(alignmentId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    def GetGeometryPointsOptions(self):
        """ GetGeometryPointsOptions(self: AlignmentVerticalGeometryPointLabelGroup) -> GeometryPointSelector[ProfilePointType] """
        pass

    def SetGeometryPointsOptions(self, alignmentVerticalGeometryPoints):
        """ SetGeometryPointsOptions(self: AlignmentVerticalGeometryPointLabelGroup, alignmentVerticalGeometryPoints: GeometryPointSelector[ProfilePointType]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    VerticalAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalAlignment(self: AlignmentVerticalGeometryPointLabelGroup) -> ObjectId

Set: VerticalAlignment(self: AlignmentVerticalGeometryPointLabelGroup) = value
"""


    m_SubData = None


class AnchorInfo(object):
    """ AnchorInfo(isOnCurve: bool, centerOfCurve: Point2d, directionAtLocation: Vector3d, location: Point3d) """
    @staticmethod # known case of __new__
    def __new__(self, isOnCurve, centerOfCurve, directionAtLocation, location):
        """ __new__(cls: type, isOnCurve: bool, centerOfCurve: Point2d, directionAtLocation: Vector3d, location: Point3d) """
        pass

    CenterOfCurve = None
    DirectionAtLocation = None
    IsOnCurve = None
    Location = None


class AppliedAssembly(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: AppliedAssembly, A_0: bool) """
        pass

    def GetAppliedSubassemblies(self):
        """ GetAppliedSubassemblies(self: AppliedAssembly) -> AppliedSubassemblyCollection """
        pass

    def GetLinksByCode(self, code):
        """ GetLinksByCode(self: AppliedAssembly, code: str) -> CalculatedLinkCollection """
        pass

    def GetPointsByCode(self, code):
        """ GetPointsByCode(self: AppliedAssembly, code: str) -> CalculatedPointCollection """
        pass

    def GetShapesByCode(self, code):
        """ GetShapesByCode(self: AppliedAssembly, code: str) -> CalculatedShapeCollection """
        pass

    AdjustedElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjustedElevation(self: AppliedAssembly) -> float

"""

    AssemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyId(self: AppliedAssembly) -> ObjectId

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: AppliedAssembly) -> ObjectId

"""

    Links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Links(self: AppliedAssembly) -> CalculatedLinkCollection

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: AppliedAssembly) -> CalculatedPointCollection

"""

    Shapes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shapes(self: AppliedAssembly) -> CalculatedShapeCollection

"""



class AppliedAssemblyCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: AppliedAssemblyCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AppliedAssemblyCollection) -> IEnumerator[AppliedAssembly] """
        pass

    def GetItemAt(self, station):
        """ GetItemAt(self: AppliedAssemblyCollection, station: float) -> AppliedAssembly """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AppliedAssemblyCollection) -> IEnumerator """
        pass

    def Stations(self):
        """ Stations(self: AppliedAssemblyCollection) -> Array[float] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AppliedAssembly](enumerable: IEnumerable[AppliedAssembly], value: AppliedAssembly) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: AppliedAssemblyCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AppliedAssemblyCollection) -> int

"""



class AppliedAssemblySetting(object):
    # no doc
    AdditionalAppliedAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdditionalAppliedAssemblies(self: AppliedAssemblySetting) -> List[AdditionalAppliedAssemblyInfo]

Set: AdditionalAppliedAssemblies(self: AppliedAssemblySetting) = value
"""

    AppliedAdjacentToOffsetTargetStartEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAdjacentToOffsetTargetStartEnd(self: AppliedAssemblySetting) -> bool

Set: AppliedAdjacentToOffsetTargetStartEnd(self: AppliedAssemblySetting) = value
"""

    AppliedAtHorizontalGeometryPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAtHorizontalGeometryPoints(self: AppliedAssemblySetting) -> bool

Set: AppliedAtHorizontalGeometryPoints(self: AppliedAssemblySetting) = value
"""

    AppliedAtOffsetTargetGeometryPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAtOffsetTargetGeometryPoints(self: AppliedAssemblySetting) -> bool

Set: AppliedAtOffsetTargetGeometryPoints(self: AppliedAssemblySetting) = value
"""

    AppliedAtProfileGeometryPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAtProfileGeometryPoints(self: AppliedAssemblySetting) -> bool

Set: AppliedAtProfileGeometryPoints(self: AppliedAssemblySetting) = value
"""

    AppliedAtProfileHighLowPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAtProfileHighLowPoints(self: AppliedAssemblySetting) -> bool

Set: AppliedAtProfileHighLowPoints(self: AppliedAssemblySetting) = value
"""

    AppliedAtSuperelevationCriticalPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAtSuperelevationCriticalPoints(self: AppliedAssemblySetting) -> bool

Set: AppliedAtSuperelevationCriticalPoints(self: AppliedAssemblySetting) = value
"""

    CorridorAlongCurvesOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorAlongCurvesOption(self: AppliedAssemblySetting) -> CorridorAlongCurveOption

Set: CorridorAlongCurvesOption(self: AppliedAssemblySetting) = value
"""

    FrequencyAlongCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyAlongCurves(self: AppliedAssemblySetting) -> float

Set: FrequencyAlongCurves(self: AppliedAssemblySetting) = value
"""

    FrequencyAlongProfileCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyAlongProfileCurves(self: AppliedAssemblySetting) -> float

Set: FrequencyAlongProfileCurves(self: AppliedAssemblySetting) = value
"""

    FrequencyAlongSpirals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyAlongSpirals(self: AppliedAssemblySetting) -> float

Set: FrequencyAlongSpirals(self: AppliedAssemblySetting) = value
"""

    FrequencyAlongTangents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyAlongTangents(self: AppliedAssemblySetting) -> float

Set: FrequencyAlongTangents(self: AppliedAssemblySetting) = value
"""

    FrequencyAlongTargetCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrequencyAlongTargetCurves(self: AppliedAssemblySetting) -> float

Set: FrequencyAlongTargetCurves(self: AppliedAssemblySetting) = value
"""

    MODAlongCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MODAlongCurves(self: AppliedAssemblySetting) -> float

Set: MODAlongCurves(self: AppliedAssemblySetting) = value
"""

    MODAlongTargetCurves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MODAlongTargetCurves(self: AppliedAssemblySetting) -> float

Set: MODAlongTargetCurves(self: AppliedAssemblySetting) = value
"""

    TargetCurveOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetCurveOption(self: AppliedAssemblySetting) -> CorridorAlongOffsetTargetCurveOption

Set: TargetCurveOption(self: AppliedAssemblySetting) = value
"""



class AppliedSubassembly(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Contains(self, paramKeyName):
        """ Contains(self: AppliedSubassembly, paramKeyName: str) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: AppliedSubassembly, A_0: bool) """
        pass

    def GetParameter(self, paramKeyName):
        """ GetParameter[T](self: AppliedSubassembly, paramKeyName: str) -> AppliedSubassemblyParam[T] """
        pass

    BaselineHookedTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineHookedTo(self: AppliedSubassembly) -> BaseBaseline

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: AppliedSubassembly) -> ObjectId

"""

    Links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Links(self: AppliedSubassembly) -> CalculatedLinkCollection

"""

    OriginStationOffsetElevationToBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginStationOffsetElevationToBaseline(self: AppliedSubassembly) -> Point3d

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: AppliedSubassembly) -> Array[IAppliedSubassemblyParam]

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: AppliedSubassembly) -> CalculatedPointCollection

"""

    Shapes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shapes(self: AppliedSubassembly) -> CalculatedShapeCollection

"""

    SubassemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubassemblyId(self: AppliedSubassembly) -> ObjectId

"""



class AppliedSubassemblyCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: AppliedSubassemblyCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AppliedSubassemblyCollection) -> IEnumerator[AppliedSubassembly] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AppliedSubassemblyCollection) -> IEnumerator """
        pass

    def ObjectIds(self):
        """ ObjectIds(self: AppliedSubassemblyCollection) -> Array[ObjectId] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AppliedSubassembly](enumerable: IEnumerable[AppliedSubassembly], value: AppliedSubassembly) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: AppliedSubassemblyCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AppliedSubassemblyCollection) -> int

"""



class AppliedSubassemblyParam(object):
    # no doc
    def ClearOverride(self):
        """ ClearOverride(self: AppliedSubassemblyParam[T]) -> bool """
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: AppliedSubassemblyParam[T]) -> str

Set: Comment(self: AppliedSubassemblyParam[T]) = value
"""

    DesignValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignValue(self: AppliedSubassemblyParam[T]) -> T

"""

    DesignValueAsObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignValueAsObject(self: AppliedSubassemblyParam[T]) -> object

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: AppliedSubassemblyParam[T]) -> str

"""

    IsOverriden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverriden(self: AppliedSubassemblyParam[T]) -> bool

"""

    KeyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyName(self: AppliedSubassemblyParam[T]) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: AppliedSubassemblyParam[T]) -> T

Set: Value(self: AppliedSubassemblyParam[T]) = value
"""

    ValueAsObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueAsObject(self: AppliedSubassemblyParam[T]) -> object

"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueType(self: AppliedSubassemblyParam[T]) -> Type

"""



class GeoEntity(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class Assembly(GeoEntity):
    # no doc
    def AddSubassembly(self, subassemblyId, pointHookTo=None):
        """
        AddSubassembly(self: Assembly, subassemblyId: ObjectId) -> AssemblyGroup
        AddSubassembly(self: Assembly, subassemblyId: ObjectId, pointHookTo: Point)
        """
        pass

    def CopySubassembly(self, subassemblyIdFrom, pointHookTo=None):
        """
        CopySubassembly(self: Assembly, subassemblyIdFrom: ObjectId) -> AssemblyGroup
        CopySubassembly(self: Assembly, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetOffsetBaselineNames(self):
        """ GetOffsetBaselineNames(self: Assembly) -> Array[str] """
        pass

    def InsertSubassemblyAfter(self, subassemblyId, pointHookTo):
        """ InsertSubassemblyAfter(self: Assembly, subassemblyId: ObjectId, pointHookTo: Point) """
        pass

    def InsertSubassemblyBefore(self, subassemblyId, targetSubassemblyId):
        """ InsertSubassemblyBefore(self: Assembly, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) """
        pass

    def MirrorSubassembly(self, subassemblyIdFrom, pointHookTo=None):
        """
        MirrorSubassembly(self: Assembly, subassemblyIdFrom: ObjectId) -> AssemblyGroup
        MirrorSubassembly(self: Assembly, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId
        """
        pass

    def ReplaceSubassembly(self, subassemblyId, targetSubassemblyId):
        """ ReplaceSubassembly(self: Assembly, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) """
        pass

    CodeSetStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeSetStyleId(self: Assembly) -> ObjectId

Set: CodeSetStyleId(self: Assembly) = value
"""

    CodeSetStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeSetStyleName(self: Assembly) -> str

Set: CodeSetStyleName(self: Assembly) = value
"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Groups(self: Assembly) -> AssemblyGroupCollection

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Assembly) -> Point3d

Set: Location(self: Assembly) = value
"""

    OffsetAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetAssemblies(self: Assembly) -> OffsetAssemblyCollection

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Assembly) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: Assembly) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Assembly) -> AssemblyType

Set: Type(self: Assembly) = value
"""



class AssemblyCollection(CivilWrapper<AcDbDatabase>):
    # no doc
    def Add(self, assemblyName, type, location, styleId=None, codeSetStyleId=None):
        """
        Add(self: AssemblyCollection, assemblyName: str, type: AssemblyType, location: Point3d) -> ObjectId
        Add(self: AssemblyCollection, assemblyName: str, type: AssemblyType, location: Point3d, styleId: ObjectId, codeSetStyleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AcDbDatabase>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AssemblyCollection) -> IEnumerator[ObjectId] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AssemblyCollection) -> IEnumerator """
        pass

    def ImportAssembly(self, assemblyName, *__args):
        """
        ImportAssembly(self: AssemblyCollection, assemblyName: str, atcFilePath: str, itemId: str, location: Point3d) -> ObjectId
        ImportAssembly(self: AssemblyCollection, assemblyName: str, sourceDatabase: Database, sourceAssemblyName: str, location: Point3d) -> ObjectId
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerable: IEnumerable[ObjectId], value: ObjectId) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AssemblyCollection) -> int

"""



class AssemblyGroup(object):
    # no doc
    def generateGroupName(self, *args): #cannot find CLR method
        """ generateGroupName(self: AssemblyGroup, strOldGroupName: AecRmCString*, strNewGroupName: AecRmCString*) -> bool """
        pass

    def getAssemblyGroupName(self, *args): #cannot find CLR method
        """ getAssemblyGroupName(self: AssemblyGroup, : AecRmCString*) -> AecRmCString* """
        pass

    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: AssemblyGroup) -> AeccDbAssembly* """
        pass

    def getSubassemblyIds(self, *args): #cannot find CLR method
        """ getSubassemblyIds(self: AssemblyGroup, subassemblies: vector<AcDbObjectId\,std::allocator<AcDbObjectId> >*) """
        pass

    def GetSubassemblyIds(self):
        """ GetSubassemblyIds(self: AssemblyGroup) -> ObjectIdCollection """
        pass

    def renameGroup(self, *args): #cannot find CLR method
        """ renameGroup(self: AssemblyGroup, strNewGroupName: AecRmCString*) -> bool """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AssemblyGroup) -> str

Set: Name(self: AssemblyGroup) = value
"""



class AssemblyGroupCollection(object):
    # no doc
    def contains(self, *args): #cannot find CLR method
        """ contains(self: AssemblyGroupCollection, group: AssemblyGroup) -> bool """
        pass

    def createAssemblyGroup(self, *args): #cannot find CLR method
        """ createAssemblyGroup(self: AssemblyGroupCollection, index: int) -> AssemblyGroup """
        pass

    def deleteGroup(self, *args): #cannot find CLR method
        """ deleteGroup(self: AssemblyGroupCollection, strGroupName: AecRmCString*) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AssemblyGroupCollection) -> IEnumerator[AssemblyGroup] """
        pass

    def getGroupCount(self, *args): #cannot find CLR method
        """ getGroupCount(self: AssemblyGroupCollection) -> int """
        pass

    def getGroupNames(self, *args): #cannot find CLR method
        """ getGroupNames(self: AssemblyGroupCollection, groupNames: AecRmCStringArray*) """
        pass

    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: AssemblyGroupCollection) -> AeccDbAssembly* """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AssemblyGroupCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """
        Remove(self: AssemblyGroupCollection, groupName: str) -> bool
        Remove(self: AssemblyGroupCollection, group: AssemblyGroup) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: AssemblyGroupCollection, index: int) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AssemblyGroup](enumerable: IEnumerable[AssemblyGroup], value: AssemblyGroup) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AssemblyGroupCollection) -> int

"""



class AssemblyType(Enum):
    """ enum AssemblyType, values: DividedCrownedRoad (3), DividedPlanarRoad (4), Other (5), Railway (6), UndividedCrownedRoad (1), UndividedPlanarRoad (2) """
    DividedCrownedRoad = None
    DividedPlanarRoad = None
    Other = None
    Railway = None
    UndividedCrownedRoad = None
    UndividedPlanarRoad = None
    value__ = None


class AttributeTypeInfo(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def getValidDefaultValue(self, *args): #cannot find CLR method
        """ getValidDefaultValue(self: AttributeTypeInfo, defaultValue: object) -> object """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: AttributeTypeInfo) -> object

Set: DefaultValue(self: AttributeTypeInfo) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: AttributeTypeInfo) -> str

Set: Description(self: AttributeTypeInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AttributeTypeInfo) -> str

Set: Name(self: AttributeTypeInfo) = value
"""

    UseDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultValue(self: AttributeTypeInfo) -> bool

Set: UseDefaultValue(self: AttributeTypeInfo) = value
"""



class AttributeTypeInfoBool(AttributeTypeInfo):
    """ AttributeTypeInfoBool(name: str) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: AttributeTypeInfoBool) -> bool

Set: DefaultValue(self: AttributeTypeInfoBool) = value
"""



class AttributeTypeInfoDouble(AttributeTypeInfo):
    """
    AttributeTypeInfoDouble(name: str, dataType: AttributeTypeInfoDoubleDataType)
    AttributeTypeInfoDouble(name: str)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, dataType=None):
        """
        __new__(cls: type, name: str, dataType: AttributeTypeInfoDoubleDataType)
        __new__(cls: type, name: str)
        """
        pass

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: AttributeTypeInfoDouble) -> AttributeTypeInfoDoubleDataType

Set: DataType(self: AttributeTypeInfoDouble) = value
"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: AttributeTypeInfoDouble) -> float

Set: DefaultValue(self: AttributeTypeInfoDouble) = value
"""

    LowerBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundInclusive(self: AttributeTypeInfoDouble) -> bool

Set: LowerBoundInclusive(self: AttributeTypeInfoDouble) = value
"""

    LowerBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundValue(self: AttributeTypeInfoDouble) -> float

Set: LowerBoundValue(self: AttributeTypeInfoDouble) = value
"""

    UpperBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundInclusive(self: AttributeTypeInfoDouble) -> bool

Set: UpperBoundInclusive(self: AttributeTypeInfoDouble) = value
"""

    UpperBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundValue(self: AttributeTypeInfoDouble) -> float

Set: UpperBoundValue(self: AttributeTypeInfoDouble) = value
"""



class AttributeTypeInfoDoubleDataType(Enum):
    """ enum AttributeTypeInfoDoubleDataType, values: Angle (1), Area (2), Azimuth (3), Coordinate (4), Dimension (5), Direction (6), Distance (7), Double (0), Elevation (8), GradeSlope (9), Latitude (10), Longitude (11), Percent (13), Rotation (12), Station (14), Volume (15) """
    Angle = None
    Area = None
    Azimuth = None
    Coordinate = None
    Dimension = None
    Direction = None
    Distance = None
    Double = None
    Elevation = None
    GradeSlope = None
    Latitude = None
    Longitude = None
    Percent = None
    Rotation = None
    Station = None
    value__ = None
    Volume = None


class AttributeTypeInfoEnum(AttributeTypeInfo):
    """ AttributeTypeInfoEnum(name: str, vecArray: IEnumerable[str]) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumValues(self):
        """ GetEnumValues(self: AttributeTypeInfoEnum) -> Array[str] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name, vecArray):
        """ __new__(cls: type, name: str, vecArray: IEnumerable[str]) """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: AttributeTypeInfoEnum) -> str

Set: DefaultValue(self: AttributeTypeInfoEnum) = value
"""



class AttributeTypeInfoInt(AttributeTypeInfo):
    """ AttributeTypeInfoInt(name: str) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: AttributeTypeInfoInt) -> int

Set: DefaultValue(self: AttributeTypeInfoInt) = value
"""

    LowerBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundInclusive(self: AttributeTypeInfoInt) -> bool

Set: LowerBoundInclusive(self: AttributeTypeInfoInt) = value
"""

    LowerBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundValue(self: AttributeTypeInfoInt) -> int

Set: LowerBoundValue(self: AttributeTypeInfoInt) = value
"""

    UpperBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundInclusive(self: AttributeTypeInfoInt) -> bool

Set: UpperBoundInclusive(self: AttributeTypeInfoInt) = value
"""

    UpperBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundValue(self: AttributeTypeInfoInt) -> int

Set: UpperBoundValue(self: AttributeTypeInfoInt) = value
"""



class AttributeTypeInfoString(AttributeTypeInfo):
    """ AttributeTypeInfoString(name: str) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: AttributeTypeInfoString) -> str

Set: DefaultValue(self: AttributeTypeInfoString) = value
"""



class AutoWideningCriteriaInfo(object):
    """ AutoWideningCriteriaInfo() """
    AttainmentMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttainmentMethod(self: AutoWideningCriteriaInfo) -> str

Set: AttainmentMethod(self: AutoWideningCriteriaInfo) = value
"""

    CriteriaFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CriteriaFileName(self: AutoWideningCriteriaInfo) -> str

Set: CriteriaFileName(self: AutoWideningCriteriaInfo) = value
"""

    LaneWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LaneWidth(self: AutoWideningCriteriaInfo) -> float

Set: LaneWidth(self: AutoWideningCriteriaInfo) = value
"""

    LeftLanesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftLanesCount(self: AutoWideningCriteriaInfo) -> int

Set: LeftLanesCount(self: AutoWideningCriteriaInfo) = value
"""

    MinimumRadiusTableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumRadiusTableName(self: AutoWideningCriteriaInfo) -> str

Set: MinimumRadiusTableName(self: AutoWideningCriteriaInfo) = value
"""

    RightLanesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightLanesCount(self: AutoWideningCriteriaInfo) -> int

Set: RightLanesCount(self: AutoWideningCriteriaInfo) = value
"""

    SpiralPercentForSC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralPercentForSC(self: AutoWideningCriteriaInfo) -> float

Set: SpiralPercentForSC(self: AutoWideningCriteriaInfo) = value
"""

    TangentPercentForTC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentPercentForTC(self: AutoWideningCriteriaInfo) -> float

Set: TangentPercentForTC(self: AutoWideningCriteriaInfo) = value
"""

    TransitionLengthTableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionLengthTableName(self: AutoWideningCriteriaInfo) -> str

Set: TransitionLengthTableName(self: AutoWideningCriteriaInfo) = value
"""

    WheelbaseLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WheelbaseLength(self: AutoWideningCriteriaInfo) -> float

Set: WheelbaseLength(self: AutoWideningCriteriaInfo) = value
"""

    WideningMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WideningMethod(self: AutoWideningCriteriaInfo) -> str

Set: WideningMethod(self: AutoWideningCriteriaInfo) = value
"""

    WideningSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WideningSide(self: AutoWideningCriteriaInfo) -> WideningSide

Set: WideningSide(self: AutoWideningCriteriaInfo) = value
"""



class AutoWideningInfo(object):
    """ AutoWideningInfo() """
    IncreasedWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncreasedWidth(self: AutoWideningInfo) -> float

Set: IncreasedWidth(self: AutoWideningInfo) = value
"""

    Side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Side(self: AutoWideningInfo) -> WideningSide

Set: Side(self: AutoWideningInfo) = value
"""

    TransitionLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionLength(self: AutoWideningInfo) -> float

Set: TransitionLength(self: AutoWideningInfo) = value
"""



class BaseBaseline(CivilWrapper<AeccDbCorridor>):
    # no doc
    def checkAlignmentProfile(self, *args): #cannot find CLR method
        """ checkAlignmentProfile(self: BaseBaseline, oidAlignment: AcDbObjectId*, oidProfile: AcDbObjectId*) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbCorridor>, A_0: bool) """
        pass

    def GetDirectionAtStation(self, station):
        """ GetDirectionAtStation(self: BaseBaseline, station: float) -> Vector3d """
        pass

    def getEndStation(self, *args): #cannot find CLR method
        """ getEndStation(self: BaseBaseline) -> float """
        pass

    def getStartStation(self, *args): #cannot find CLR method
        """ getStartStation(self: BaseBaseline) -> float """
        pass

    def IsFeatureLineBased(self):
        """ IsFeatureLineBased(self: BaseBaseline) -> bool """
        pass

    def SetAlignmentAndProfile(self, alignmentId, profileId):
        """ SetAlignmentAndProfile(self: BaseBaseline, alignmentId: ObjectId, profileId: ObjectId) """
        pass

    def setAlignmentProfile(self, *args): #cannot find CLR method
        """ setAlignmentProfile(self: BaseBaseline, oidAlignment: AcDbObjectId*, oidProfile: AcDbObjectId*) """
        pass

    def SortedStations(self):
        """ SortedStations(self: BaseBaseline) -> Array[float] """
        pass

    def StationOffsetElevationToXYZ(self, soe):
        """ StationOffsetElevationToXYZ(self: BaseBaseline, soe: Point3d) -> Point3d """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: BaseBaseline) -> ObjectId

"""

    baselineGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: baselineGUID(self: BaseBaseline) -> Guid

"""

    BaselineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineType(self: BaseBaseline) -> CorridorBaselineType

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: BaseBaseline) -> ObjectId

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: BaseBaseline) -> float

"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: BaseBaseline) -> ObjectId

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: BaseBaseline) -> float

"""



class Baseline(BaseBaseline):
    # no doc
    def Dispose(self):
        """ Dispose(self: Baseline, A_0: bool) """
        pass

    def GetAppliedAssemblyAtIndex(self, index):
        """ GetAppliedAssemblyAtIndex(self: Baseline, index: int) -> AppliedAssembly """
        pass

    def GetAppliedAssemblyAtStation(self, station):
        """ GetAppliedAssemblyAtStation(self: Baseline, station: float) -> AppliedAssembly """
        pass

    def GetTargets(self):
        """ GetTargets(self: Baseline) -> SubassemblyTargetInfoCollection """
        pass

    def IsFeatureLineBased(self):
        """ IsFeatureLineBased(self: Baseline) -> bool """
        pass

    def SetTargets(self, updatedTargets):
        """ SetTargets(self: Baseline, updatedTargets: SubassemblyTargetInfoCollection) """
        pass

    def SortedStations(self):
        """ SortedStations(self: Baseline) -> Array[float] """
        pass

    def UpdateStation(self, station):
        """ UpdateStation(self: Baseline, station: float) """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: Baseline) -> ObjectId

"""

    baselineGUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: baselineGUID(self: Baseline) -> Guid

"""

    BaselineRegions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineRegions(self: Baseline) -> BaselineRegionCollection

"""

    BaselineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineType(self: Baseline) -> CorridorBaselineType

"""

    IsProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProcessed(self: Baseline) -> bool

"""

    MainBaselineFeatureLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MainBaselineFeatureLines(self: Baseline) -> BaselineFeatureLines

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Baseline) -> str

Set: Name(self: Baseline) = value
"""

    NeedsProcessing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedsProcessing(self: Baseline) -> bool

Set: NeedsProcessing(self: Baseline) = value
"""

    OffsetBaselineFeatureLinesCol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetBaselineFeatureLinesCol(self: Baseline) -> BaselineFeatureLinesCollection

"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: Baseline) -> ObjectId

"""



class BaselineCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, baselineName, *__args):
        """
        Add(self: BaselineCollection, baselineName: str, alignmentName: str, profileName: str) -> Baseline
        Add(self: BaselineCollection, baselineName: str, alignmentId: ObjectId, profileId: ObjectId) -> Baseline
        """
        pass

    def AddGUIDBaseline(self, baselineName, alignmentId, profileId):
        """ AddGUIDBaseline(self: BaselineCollection, baselineName: str, alignmentId: ObjectId, profileId: ObjectId) -> Baseline """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbCorridor>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BaselineCollection) -> IEnumerator[Baseline] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: BaselineCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """
        Remove(self: BaselineCollection, baselineName: str) -> bool
        Remove(self: BaselineCollection, baseline: Baseline) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: BaselineCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Baseline](enumerable: IEnumerable[Baseline], value: Baseline) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: BaselineCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BaselineCollection) -> int

"""



class BaselineFeatureLines(CivilWrapper<AeccDbCorridor>):
    # no doc
    def CodeNames(self):
        """ CodeNames(self: BaselineFeatureLines) -> Array[str] """
        pass

    def Dispose(self):
        """ Dispose(self: BaselineFeatureLines, A_0: bool) """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: BaselineFeatureLines) -> ObjectId

"""

    FeatureLineCollectionMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineCollectionMap(self: BaselineFeatureLines) -> FeatureLineCollectionMap

"""

    HardcodedOffsetBaselineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardcodedOffsetBaselineName(self: BaselineFeatureLines) -> str

"""

    IsMainBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMainBaseline(self: BaselineFeatureLines) -> bool

"""

    OffsetAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetAlignmentId(self: BaselineFeatureLines) -> ObjectId

"""



class BaselineFeatureLinesCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def CodeNames(self):
        """ CodeNames(self: BaselineFeatureLinesCollection) -> Array[str] """
        pass

    def Dispose(self):
        """ Dispose(self: BaselineFeatureLinesCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BaselineFeatureLinesCollection) -> IEnumerator[BaselineFeatureLines] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: BaselineFeatureLinesCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BaselineFeatureLines](enumerable: IEnumerable[BaselineFeatureLines], value: BaselineFeatureLines) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: BaselineFeatureLinesCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BaselineFeatureLinesCollection) -> int

"""



class BaseLineRange(object):
    # no doc
    def CheckStationRange(self):
        """ CheckStationRange(self: BaseLineRange) """
        pass

    BaseLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseLineId(self: BaseLineRange) -> ObjectId

Set: BaseLineId(self: BaseLineRange) = value
"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: BaseLineRange) -> float

Set: EndStation(self: BaseLineRange) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: BaseLineRange) -> float

Set: StartStation(self: BaseLineRange) = value
"""



class BaselineRegion(CivilWrapper<AeccDbCorridor>):
    # no doc
    def AdditionalStations(self):
        """ AdditionalStations(self: BaselineRegion) -> Array[float] """
        pass

    def AddStation(self, rawStation, description):
        """ AddStation(self: BaselineRegion, rawStation: float, description: str) """
        pass

    def ClearAdditionalStations(self):
        """ ClearAdditionalStations(self: BaselineRegion) """
        pass

    def DeleteStation(self, rawStation):
        """ DeleteStation(self: BaselineRegion, rawStation: float) """
        pass

    def Dispose(self):
        """ Dispose(self: BaselineRegion, A_0: bool) """
        pass

    def GetOverriddenStations(self):
        """ GetOverriddenStations(self: BaselineRegion) -> Array[OverriddenStationInfo] """
        pass

    def GetTargets(self):
        """ GetTargets(self: BaselineRegion) -> SubassemblyTargetInfoCollection """
        pass

    def Match(self, sourceRegion, matchOption):
        """ Match(self: BaselineRegion, sourceRegion: BaselineRegion, matchOption: RegionMatchType) """
        pass

    def Merge(self, firstRegion, lastRegion):
        """ Merge(self: BaselineRegion, firstRegion: BaselineRegion, lastRegion: BaselineRegion) """
        pass

    def RemoveOverriddenStation(self, station):
        """ RemoveOverriddenStation(self: BaselineRegion, station: float) -> bool """
        pass

    def SetTargets(self, updatedTargets):
        """ SetTargets(self: BaselineRegion, updatedTargets: SubassemblyTargetInfoCollection) """
        pass

    def SortedStations(self):
        """ SortedStations(self: BaselineRegion) -> Array[float] """
        pass

    def Split(self, splitStation):
        """ Split(self: BaselineRegion, splitStation: float) -> BaselineRegion """
        pass

    AppliedAssemblies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAssemblies(self: BaselineRegion) -> AppliedAssemblyCollection

"""

    AppliedAssemblySetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedAssemblySetting(self: BaselineRegion) -> AppliedAssemblySetting

"""

    AssemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyId(self: BaselineRegion) -> ObjectId

Set: AssemblyId(self: BaselineRegion) = value
"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: BaselineRegion) -> ObjectId

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: BaselineRegion) -> float

Set: EndStation(self: BaselineRegion) = value
"""

    IsProcessed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProcessed(self: BaselineRegion) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BaselineRegion) -> str

Set: Name(self: BaselineRegion) = value
"""

    NeedsProcessing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedsProcessing(self: BaselineRegion) -> bool

Set: NeedsProcessing(self: BaselineRegion) = value
"""

    OffsetBaselines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetBaselines(self: BaselineRegion) -> OffsetBaselineCollection

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: BaselineRegion) -> float

Set: StartStation(self: BaselineRegion) = value
"""



class BaselineRegionCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, regionName, *__args):
        """
        Add(self: BaselineRegionCollection, regionName: str, assemblyId: ObjectId) -> BaselineRegion
        Add(self: BaselineRegionCollection, regionName: str, assemblyName: str) -> BaselineRegion
        Add(self: BaselineRegionCollection, regionName: str, assemblyId: ObjectId, startStation: float, endStation: float) -> BaselineRegion
        Add(self: BaselineRegionCollection, regionName: str, assemblyName: str, startStation: float, endStation: float) -> BaselineRegion
        """
        pass

    def AddRegion(self, regionName, *__args):
        """
        AddRegion(self: BaselineRegionCollection, regionName: str, assemblyName: str) -> BaselineRegion
        AddRegion(self: BaselineRegionCollection, regionName: str, assemblyId: ObjectId) -> BaselineRegion
        """
        pass

    def Dispose(self):
        """ Dispose(self: BaselineRegionCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BaselineRegionCollection) -> IEnumerator[BaselineRegion] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: BaselineRegionCollection) -> IEnumerator """
        pass

    def IndexOf(self, region):
        """ IndexOf(self: BaselineRegionCollection, region: BaselineRegion) -> int """
        pass

    def Remove(self, *__args):
        """
        Remove(self: BaselineRegionCollection, regionName: str) -> bool
        Remove(self: BaselineRegionCollection, region: BaselineRegion) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: BaselineRegionCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BaselineRegion](enumerable: IEnumerable[BaselineRegion], value: BaselineRegion) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: BaselineRegionCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BaselineRegionCollection) -> int

"""



class BoundingShapeType(Enum):
    """ enum BoundingShapeType, values: Box (2), Cylinder (1), Sphere (3), Undefined (0) """
    Box = None
    Cylinder = None
    Sphere = None
    Undefined = None
    value__ = None


class CalculatedSubentity(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CalculatedSubentity, A_0: bool) """
        pass

    CorridorCodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorCodes(self: CalculatedSubentity) -> CorridorCodeCollection

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CalculatedSubentity) -> ObjectId

"""

    SubassemblyBelongedTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubassemblyBelongedTo(self: CalculatedSubentity) -> AppliedSubassembly

"""



class CalculatedLink(CalculatedSubentity):
    # no doc
    def Dispose(self):
        """ Dispose(self: CalculatedLink, A_0: bool) """
        pass

    CalculatedPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculatedPoints(self: CalculatedLink) -> CalculatedPointCollection

"""

    CorridorCodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorCodes(self: CalculatedLink) -> CorridorCodeCollection

"""

    DrawOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawOverride(self: CalculatedLink) -> CorridorLinkDrawOverride

"""



class CalculatedLinkCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, point1, point2, code):
        """ Add(self: CalculatedLinkCollection, point1: CalculatedPoint, point2: CalculatedPoint, code: str) -> CalculatedLink """
        pass

    def Dispose(self):
        """ Dispose(self: CalculatedLinkCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CalculatedLinkCollection) -> IEnumerator[CalculatedLink] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CalculatedLinkCollection) -> IEnumerator """
        pass

    def Remove(self, link):
        """ Remove(self: CalculatedLinkCollection, link: CalculatedLink) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CalculatedLinkCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CalculatedLink](enumerable: IEnumerable[CalculatedLink], value: CalculatedLink) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CalculatedLinkCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CalculatedLinkCollection) -> int

"""



class CalculatedPoint(CalculatedSubentity):
    # no doc
    def Dispose(self):
        """ Dispose(self: CalculatedPoint, A_0: bool) """
        pass

    CorridorCodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorCodes(self: CalculatedPoint) -> CorridorCodeCollection

"""

    NormalToBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalToBaseline(self: CalculatedPoint) -> Vector3d

"""

    NormalToSubassembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalToSubassembly(self: CalculatedPoint) -> Vector3d

"""

    StationOffsetElevationToBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationOffsetElevationToBaseline(self: CalculatedPoint) -> Point3d

"""

    StationOffsetElevationToSubassembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationOffsetElevationToSubassembly(self: CalculatedPoint) -> Point3d

"""



class CalculatedPointCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, link, code):
        """ Add(self: CalculatedPointCollection, link: CalculatedLink, code: str) -> CalculatedPoint """
        pass

    def Dispose(self):
        """ Dispose(self: CalculatedPointCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CalculatedPointCollection) -> IEnumerator[CalculatedPoint] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CalculatedPointCollection) -> IEnumerator """
        pass

    def Remove(self, point):
        """ Remove(self: CalculatedPointCollection, point: CalculatedPoint) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CalculatedPointCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CalculatedPoint](enumerable: IEnumerable[CalculatedPoint], value: CalculatedPoint) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CalculatedPointCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CalculatedPointCollection) -> int

"""



class CalculatedShape(CalculatedSubentity):
    # no doc
    def Dispose(self):
        """ Dispose(self: CalculatedShape, A_0: bool) """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: CalculatedShape) -> float

"""

    CalculatedLinks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculatedLinks(self: CalculatedShape) -> CalculatedLinkCollection

"""

    CorridorCodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorCodes(self: CalculatedShape) -> CorridorCodeCollection

"""



class CalculatedShapeCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CalculatedShapeCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CalculatedShapeCollection) -> IEnumerator[CalculatedShape] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CalculatedShapeCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CalculatedShape](enumerable: IEnumerable[CalculatedShape], value: CalculatedShape) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CalculatedShapeCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CalculatedShapeCollection) -> int

"""



class CANTCriticalStation(object):
    # no doc
    AppliedCANT = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedCANT(self: CANTCriticalStation) -> float

Set: AppliedCANT(self: CANTCriticalStation) = value
"""

    CANTCurveName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CANTCurveName(self: CANTCriticalStation) -> str

"""

    LeftRailElevationDifference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftRailElevationDifference(self: CANTCriticalStation) -> float

"""

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: CANTCriticalStation) -> ObjectId

"""

    RightRailElevationDifference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightRailElevationDifference(self: CANTCriticalStation) -> float

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: CANTCriticalStation) -> float

Set: Station(self: CANTCriticalStation) = value
"""

    StationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationType(self: CANTCriticalStation) -> SuperelevationCriticalStationType

"""

    TransitionDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionDescription(self: CANTCriticalStation) -> str

Set: TransitionDescription(self: CANTCriticalStation) = value
"""

    TransitionRegionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionRegionType(self: CANTCriticalStation) -> SuperelevationTransitionRegionType

"""



class CANTCriticalStationCollection(object):
    # no doc
    def Add(self, station, criticalStationType, attainmentRegionType=None):
        """ Add(self: CANTCriticalStationCollection, station: float, criticalStationType: SuperelevationCriticalStationType)Add(self: CANTCriticalStationCollection, station: float, criticalStationType: SuperelevationCriticalStationType, attainmentRegionType: SuperelevationAttainmentRegionType) """
        pass

    def GetCriticalStationAt(self, station, tolerance):
        """ GetCriticalStationAt(self: CANTCriticalStationCollection, station: float, tolerance: float) -> CANTCriticalStation """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CANTCriticalStationCollection) -> IEnumerator[CANTCriticalStation] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CANTCriticalStationCollection) -> IEnumerator """
        pass

    def IsCriticalStation(self, station, tolerance):
        """ IsCriticalStation(self: CANTCriticalStationCollection, station: float, tolerance: float) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CANTCriticalStationCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CANTCriticalStation](enumerable: IEnumerable[CANTCriticalStation], value: CANTCriticalStation) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CANTCriticalStationCollection) -> int

"""

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: CANTCriticalStationCollection) -> ObjectId

"""



class SECurve(object):
    # no doc
    CANTCriticalStations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CANTCriticalStations(self: SECurve) -> CANTCriticalStationCollection

"""

    CriticalStations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CriticalStations(self: SECurve) -> SuperelevationCriticalStationCollection

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: SECurve) -> float

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SECurve) -> str

Set: Name(self: SECurve) = value
"""

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: SECurve) -> ObjectId

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: SECurve) -> float

"""



class CANTCurve(SECurve):
    # no doc

class CANTCurveCollection(object):
    # no doc
    def AddUserDefinedCurve(self, startSubEntity, endSubEntity):
        """ AddUserDefinedCurve(self: CANTCurveCollection, startSubEntity: AlignmentSubEntity, endSubEntity: AlignmentSubEntity) -> CANTCurve """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CANTCurveCollection) -> IEnumerator[CANTCurve] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CANTCurveCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CANTCurve](enumerable: IEnumerable[CANTCurve], value: CANTCurve) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CANTCurveCollection) -> int

"""

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: CANTCurveCollection) -> ObjectId

"""



class Catchment(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAvailableCatchmentLabelIds(self):
        """ GetAvailableCatchmentLabelIds(self: Catchment) -> ObjectIdCollection """
        pass

    def GetAvailableFlowSegmentLabelIds(self):
        """ GetAvailableFlowSegmentLabelIds(self: Catchment) -> ObjectIdCollection """
        pass

    def GetFlowPath(self):
        """ GetFlowPath(self: Catchment) -> FlowPath """
        pass


class CatchmentLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(catchmentId, labelStyleId=None):
        """
        Create(catchmentId: ObjectId, labelStyleId: ObjectId) -> ObjectId
        Create(catchmentId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(catchmentId):
        """ GetAvailableLabelIds(catchmentId: ObjectId) -> ObjectIdCollection """
        pass

    m_SubData = None


class CodeCollection(CivilWrapper<AeccDbEntity>):
    # no doc
    def Add(self, *__args):
        """ Add(self: CodeCollection, code: str)Add(self: CodeCollection, codes: Array[str]) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbEntity>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CodeCollection) -> IEnumerator[str] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CodeCollection) -> IEnumerator """
        pass

    def Remove(self, code):
        """ Remove(self: CodeCollection, code: str) -> bool """
        pass

    def TryAdd(self, *__args):
        """
        TryAdd(self: CodeCollection, code: str) -> bool
        TryAdd(self: CodeCollection, codes: Array[str])
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[str](enumerable: IEnumerable[str], value: str) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CodeCollection) -> int

"""



class CogoPoint(Entity):
    # no doc
    def ApplyDescriptionKeys(self):
        """ ApplyDescriptionKeys(self: CogoPoint) """
        pass

    def ClearAllLabelTextComponentOverrides(self):
        """ ClearAllLabelTextComponentOverrides(self: CogoPoint) """
        pass

    def ClearLabelTextComponentOverrides(self, labelComponentId):
        """ ClearLabelTextComponentOverrides(self: CogoPoint, labelComponentId: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetLabelTextComponentIds(self):
        """ GetLabelTextComponentIds(self: CogoPoint) -> ObjectIdCollection """
        pass

    def GetLabelTextComponentJustificationOverride(self, labelComponentId):
        """ GetLabelTextComponentJustificationOverride(self: CogoPoint, labelComponentId: ObjectId) -> TextJustificationType """
        pass

    def GetLabelTextComponentOverride(self, labelComponentId):
        """ GetLabelTextComponentOverride(self: CogoPoint, labelComponentId: ObjectId) -> str """
        pass

    def GetUDPValue(self, udp):
        """
        GetUDPValue(self: CogoPoint, udp: UDPString) -> str
        GetUDPValue(self: CogoPoint, udp: UDPDouble) -> float
        GetUDPValue(self: CogoPoint, udp: UDPInteger) -> int
        GetUDPValue(self: CogoPoint, udp: UDPEnumeration) -> str
        GetUDPValue(self: CogoPoint, udp: UDPBoolean) -> bool
        """
        pass

    def IsLabelTextComponentOverriden(self, labelComponentId):
        """ IsLabelTextComponentOverriden(self: CogoPoint, labelComponentId: ObjectId) -> bool """
        pass

    def Renumber(self, newPointNumber, resolveType=None):
        """
        Renumber(self: CogoPoint, newPointNumber: UInt32) -> UInt32
        Renumber(self: CogoPoint, newPointNumber: UInt32, resolveType: PointNumberResolveType) -> UInt32
        """
        pass

    def ResetLabel(self):
        """ ResetLabel(self: CogoPoint) """
        pass

    def ResetLabelLocation(self):
        """ ResetLabelLocation(self: CogoPoint) """
        pass

    def ResetLabelRotation(self):
        """ ResetLabelRotation(self: CogoPoint) """
        pass

    def SetLabelTextComponentJustificationOverride(self, labelComponentId, textJustificationType):
        """ SetLabelTextComponentJustificationOverride(self: CogoPoint, labelComponentId: ObjectId, textJustificationType: TextJustificationType) """
        pass

    def SetLabelTextComponentOverride(self, labelComponentId, textOverride):
        """ SetLabelTextComponentOverride(self: CogoPoint, labelComponentId: ObjectId, textOverride: str) """
        pass

    def SetUDPValue(self, udp, value):
        """ SetUDPValue(self: CogoPoint, udp: UDPString, value: str)SetUDPValue(self: CogoPoint, udp: UDPDouble, value: float)SetUDPValue(self: CogoPoint, udp: UDPInteger, value: int)SetUDPValue(self: CogoPoint, udp: UDPEnumeration, value: str)SetUDPValue(self: CogoPoint, udp: UDPBoolean, value: bool) """
        pass

    Convergence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Convergence(self: CogoPoint) -> float

"""

    DescriptionFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DescriptionFormat(self: CogoPoint) -> str

Set: DescriptionFormat(self: CogoPoint) = value
"""

    Easting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Easting(self: CogoPoint) -> float

Set: Easting(self: CogoPoint) = value
"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: CogoPoint) -> float

Set: Elevation(self: CogoPoint) = value
"""

    ElevationOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationOverride(self: CogoPoint) -> float

"""

    FullDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullDescription(self: CogoPoint) -> str

"""

    FullDescriptionOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullDescriptionOverride(self: CogoPoint) -> str

"""

    GridEasting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridEasting(self: CogoPoint) -> float

Set: GridEasting(self: CogoPoint) = value
"""

    GridNorthing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridNorthing(self: CogoPoint) -> float

Set: GridNorthing(self: CogoPoint) = value
"""

    IsCheckedOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCheckedOut(self: CogoPoint) -> bool

"""

    IsLabelDragged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLabelDragged(self: CogoPoint) -> bool

"""

    IsLabelPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLabelPinned(self: CogoPoint) -> bool

Set: IsLabelPinned(self: CogoPoint) = value
"""

    IsLabelVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLabelVisible(self: CogoPoint) -> bool

Set: IsLabelVisible(self: CogoPoint) = value
"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLocked(self: CogoPoint) -> bool

Set: IsLocked(self: CogoPoint) = value
"""

    IsMovable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMovable(self: CogoPoint) -> bool

"""

    IsProjectPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsProjectPoint(self: CogoPoint) -> bool

"""

    IsSurveyPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSurveyPoint(self: CogoPoint) -> bool

"""

    LabelLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelLocation(self: CogoPoint) -> Point3d

Set: LabelLocation(self: CogoPoint) = value
"""

    LabelRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelRotation(self: CogoPoint) -> float

Set: LabelRotation(self: CogoPoint) = value
"""

    LabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleId(self: CogoPoint) -> ObjectId

Set: LabelStyleId(self: CogoPoint) = value
"""

    LabelStyleIdOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleIdOverride(self: CogoPoint) -> ObjectId

"""

    Latitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Latitude(self: CogoPoint) -> float

Set: Latitude(self: CogoPoint) = value
"""

    LeaderAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderAttachment(self: CogoPoint) -> LeaderAttachmentBehaviorType

Set: LeaderAttachment(self: CogoPoint) = value
"""

    LeaderTailVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderTailVisibility(self: CogoPoint) -> LeaderTailVisibilityType

Set: LeaderTailVisibility(self: CogoPoint) = value
"""

    LeaderVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderVisibility(self: CogoPoint) -> LeaderVisibilityType

Set: LeaderVisibility(self: CogoPoint) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: CogoPoint) -> Point3d

"""

    Longitude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Longitude(self: CogoPoint) -> float

Set: Longitude(self: CogoPoint) = value
"""

    MarkerRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerRotation(self: CogoPoint) -> float

Set: MarkerRotation(self: CogoPoint) = value
"""

    Northing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Northing(self: CogoPoint) -> float

Set: Northing(self: CogoPoint) = value
"""

    PointName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointName(self: CogoPoint) -> str

Set: PointName(self: CogoPoint) = value
"""

    PointNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointNumber(self: CogoPoint) -> UInt32

Set: PointNumber(self: CogoPoint) = value
"""

    PrimaryPointGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryPointGroupId(self: CogoPoint) -> ObjectId

"""

    ProjectVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectVersion(self: CogoPoint) -> int

"""

    RawDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawDescription(self: CogoPoint) -> str

Set: RawDescription(self: CogoPoint) = value
"""

    RawDescriptionOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawDescriptionOverride(self: CogoPoint) -> str

"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: CogoPoint) -> float

"""

    ScaleXY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleXY(self: CogoPoint) -> float

Set: ScaleXY(self: CogoPoint) = value
"""

    ScaleZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleZ(self: CogoPoint) -> float

Set: ScaleZ(self: CogoPoint) = value
"""

    ShowToolTip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowToolTip(self: CogoPoint) -> bool

Set: ShowToolTip(self: CogoPoint) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: CogoPoint) -> ObjectId

Set: StyleId(self: CogoPoint) = value
"""

    StyleIdOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleIdOverride(self: CogoPoint) -> ObjectId

"""



class CogoPointCollection(object):
    # no doc
    def Add(self, *__args):
        """
        Add(self: CogoPointCollection, location: Point3d, desc: str, useDescriptionKey: bool, matchOnParams: bool, useNextPointNumSetting: bool) -> ObjectId
        Add(self: CogoPointCollection, location: Point3d, desc: str, useNextPointNumSetting: bool) -> ObjectId
        Add(self: CogoPointCollection, location: Point3d, useNextPointNumSetting: bool) -> ObjectId
        Add(self: CogoPointCollection, locations: Point3dCollection, desc: str, useDescriptionKey: bool, matchOnParams: bool, useNextPointNumSetting: bool) -> ObjectIdCollection
        Add(self: CogoPointCollection, locations: Point3dCollection, desc: str, useNextPointNumSetting: bool) -> ObjectIdCollection
        Add(self: CogoPointCollection, locations: Point3dCollection, useNextPointNumSetting: bool) -> ObjectIdCollection
        """
        pass

    def Clear(self):
        """ Clear(self: CogoPointCollection) """
        pass

    def Contains(self, pointNumber):
        """ Contains(self: CogoPointCollection, pointNumber: UInt32) -> bool """
        pass

    @staticmethod
    def ExportPoints(pointFileFullName, fileFormat, *__args):
        """
        ExportPoints(pointFileFullName: str, fileFormat: PointFileFormat, pointGroupId: ObjectId) -> UInt32
        ExportPoints(pointFileFullName: str, fileFormat: PointFileFormat) -> UInt32
        ExportPoints(pointFileFullName: str, fileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformCoordinate: bool, shouldExpandCoordinateData: bool, pointGroupId: ObjectId) -> UInt32
        ExportPoints(pointFileFullName: str, fileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformCoordinate: bool, shouldExpandCoordinateData: bool) -> UInt32
        """
        pass

    @staticmethod
    def GetCogoPoints(pDatabase):
        """ GetCogoPoints(pDatabase: Database) -> CogoPointCollection """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CogoPointCollection) -> IEnumerator[ObjectId] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CogoPointCollection) -> IEnumerator """
        pass

    def GetPointByPointNumber(self, pointNumber):
        """ GetPointByPointNumber(self: CogoPointCollection, pointNumber: UInt32) -> ObjectId """
        pass

    @staticmethod
    def ImportPoints(pointFileFullName, fileFormat, *__args):
        """
        ImportPoints(pointFileFullName: str, fileFormat: PointFileFormat, pointGroupId: ObjectId) -> UInt32
        ImportPoints(pointFileFullName: str, fileFormat: PointFileFormat) -> UInt32
        ImportPoints(pointFileFullName: str, fileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformCoordinate: bool, shouldExpandCoordinateData: bool, pointGroupId: ObjectId) -> UInt32
        ImportPoints(pointFileFullName: str, fileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformCoordinate: bool, shouldExpandCoordinateData: bool) -> UInt32
        """
        pass

    def Remove(self, *__args):
        """ Remove(self: CogoPointCollection, pointNumber: UInt32)Remove(self: CogoPointCollection, pointId: ObjectId) """
        pass

    def SetDescriptionFormat(self, *__args):
        """
        SetDescriptionFormat(self: CogoPointCollection, pointId: ObjectId, descFormat: str) -> ObjectId
        SetDescriptionFormat(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], descFormat: str) -> ObjectIdCollection
        SetDescriptionFormat(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[str]) -> ObjectIdCollection
        """
        pass

    def SetEasting(self, *__args):
        """
        SetEasting(self: CogoPointCollection, pointId: ObjectId, easting: float) -> ObjectId
        SetEasting(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], easting: float) -> ObjectIdCollection
        SetEasting(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetElevation(self, *__args):
        """
        SetElevation(self: CogoPointCollection, pointId: ObjectId, elevation: float) -> ObjectId
        SetElevation(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], elevation: float) -> ObjectIdCollection
        SetElevation(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], elevations: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetElevationByOffset(self, *__args):
        """
        SetElevationByOffset(self: CogoPointCollection, pointId: ObjectId, offset: float) -> ObjectId
        SetElevationByOffset(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], offset: float) -> ObjectIdCollection
        SetElevationByOffset(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], offsets: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetElevationBySurface(self, *__args):
        """
        SetElevationBySurface(self: CogoPointCollection, pointId: ObjectId, surfaceId: ObjectId) -> ObjectId
        SetElevationBySurface(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], surfaceId: ObjectId) -> ObjectIdCollection
        """
        pass

    def SetIsLocked(self, *__args):
        """
        SetIsLocked(self: CogoPointCollection, pointId: ObjectId, isLocked: bool) -> ObjectId
        SetIsLocked(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], isLocked: bool) -> ObjectIdCollection
        SetIsLocked(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[bool]) -> ObjectIdCollection
        """
        pass

    def SetLabelRotation(self, *__args):
        """
        SetLabelRotation(self: CogoPointCollection, pointId: ObjectId, rotation: float) -> ObjectId
        SetLabelRotation(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], rotation: float) -> ObjectIdCollection
        SetLabelRotation(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetLabelStyleId(self, *__args):
        """
        SetLabelStyleId(self: CogoPointCollection, pointId: ObjectId, styleId: ObjectId) -> ObjectId
        SetLabelStyleId(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], styleId: ObjectId) -> ObjectIdCollection
        SetLabelStyleId(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], styleIds: IEnumerable[ObjectId]) -> ObjectIdCollection
        """
        pass

    def SetMarkerRotation(self, *__args):
        """
        SetMarkerRotation(self: CogoPointCollection, pointId: ObjectId, rotation: float) -> ObjectId
        SetMarkerRotation(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], rotation: float) -> ObjectIdCollection
        SetMarkerRotation(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetNorthing(self, *__args):
        """
        SetNorthing(self: CogoPointCollection, pointId: ObjectId, northing: float) -> ObjectId
        SetNorthing(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], northing: float) -> ObjectIdCollection
        SetNorthing(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetPointName(self, *__args):
        """
        SetPointName(self: CogoPointCollection, pointId: ObjectId, name: str) -> ObjectId
        SetPointName(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[str]) -> ObjectIdCollection
        """
        pass

    def SetPointNumber(self, *__args):
        """
        SetPointNumber(self: CogoPointCollection, pointId: ObjectId, pointNumber: UInt32) -> ObjectId
        SetPointNumber(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], additiveFactor: int) -> ObjectIdCollection
        """
        pass

    def SetRawDescription(self, *__args):
        """
        SetRawDescription(self: CogoPointCollection, pointId: ObjectId, rawDesc: str) -> ObjectId
        SetRawDescription(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], rawDesc: str) -> ObjectIdCollection
        SetRawDescription(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], rawDescs: IEnumerable[str]) -> ObjectIdCollection
        """
        pass

    def SetScaleXY(self, *__args):
        """
        SetScaleXY(self: CogoPointCollection, pointId: ObjectId, scale: float) -> ObjectId
        SetScaleXY(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], scale: float) -> ObjectIdCollection
        SetScaleXY(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetScaleZ(self, *__args):
        """
        SetScaleZ(self: CogoPointCollection, pointId: ObjectId, scale: float) -> ObjectId
        SetScaleZ(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], scale: float) -> ObjectIdCollection
        SetScaleZ(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[float]) -> ObjectIdCollection
        """
        pass

    def SetShowTooltips(self, *__args):
        """
        SetShowTooltips(self: CogoPointCollection, pointId: ObjectId, showTooltips: bool) -> ObjectId
        SetShowTooltips(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], showTooltips: bool) -> ObjectIdCollection
        SetShowTooltips(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], values: IEnumerable[bool]) -> ObjectIdCollection
        """
        pass

    def SetStyleId(self, *__args):
        """
        SetStyleId(self: CogoPointCollection, pointId: ObjectId, styleId: ObjectId) -> ObjectId
        SetStyleId(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], styleId: ObjectId) -> ObjectIdCollection
        SetStyleId(self: CogoPointCollection, pointIds: IEnumerable[ObjectId], styleIds: IEnumerable[ObjectId]) -> ObjectIdCollection
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerable: IEnumerable[ObjectId], value: ObjectId) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CogoPointCollection) -> UInt32

"""



class CogoPointEnumerator(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: CogoPointEnumerator) """
        pass

    def MoveNext(self):
        """ MoveNext(self: CogoPointEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: CogoPointEnumerator) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerator: IEnumerator[ObjectId], value: ObjectId) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: CogoPointEnumerator) -> ObjectId

"""

    CurrentObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentObject(self: CogoPointEnumerator) -> object

"""



class ConnectorPositionType(Enum):
    """ enum ConnectorPositionType, values: End (2), Start (1) """
    End = None
    Start = None
    value__ = None


class Corridor(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def ExportFeatureLinesAsCogoPoints(self, pointGroupName, codes, baseLineRange=None):
        """
        ExportFeatureLinesAsCogoPoints(self: Corridor, pointGroupName: str, codes: CorridorPointCodeSelector) -> ObjectId
        ExportFeatureLinesAsCogoPoints(self: Corridor, pointGroupName: str, codes: CorridorPointCodeSelector, baseLineRange: ValueType) -> ObjectId
        """
        pass

    def GetLinkCodes(self):
        """ GetLinkCodes(self: Corridor) -> Array[str] """
        pass

    def GetPointCodes(self):
        """ GetPointCodes(self: Corridor) -> Array[str] """
        pass

    def GetShapeCodes(self):
        """ GetShapeCodes(self: Corridor) -> Array[str] """
        pass

    def GetTargets(self):
        """ GetTargets(self: Corridor) -> SubassemblyTargetInfoCollection """
        pass

    def Rebuild(self):
        """ Rebuild(self: Corridor) """
        pass

    def SetTargets(self, updatedTargets):
        """ SetTargets(self: Corridor, updatedTargets: SubassemblyTargetInfoCollection) """
        pass

    Baselines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Baselines(self: Corridor) -> BaselineCollection

"""

    CodeSetStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeSetStyleId(self: Corridor) -> ObjectId

Set: CodeSetStyleId(self: Corridor) = value
"""

    CodeSetStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeSetStyleName(self: Corridor) -> str

Set: CodeSetStyleName(self: Corridor) = value
"""

    CorridorSurfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorSurfaces(self: Corridor) -> CorridorSurfaceCollection

"""

    FeatureLineCodeInfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineCodeInfos(self: Corridor) -> FeatureLineCodeInfoCollection

"""

    IsOutOfDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOutOfDate(self: Corridor) -> bool

"""

    MaximumTriangleSideLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumTriangleSideLength(self: Corridor) -> float

Set: MaximumTriangleSideLength(self: Corridor) = value
"""

    RebuildAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RebuildAutomatic(self: Corridor) -> bool

Set: RebuildAutomatic(self: Corridor) = value
"""

    RegionLockMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegionLockMode(self: Corridor) -> CorridorRegionLockType

Set: RegionLockMode(self: Corridor) = value
"""

    SlopePatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopePatterns(self: Corridor) -> CorridorSlopePatternCollection

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Corridor) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: Corridor) = value
"""



class CorridorBaselineType(Enum):
    """ enum CorridorBaselineType, values: HardcodedOffsetBaseline (3), MainBaseline (1), None (0), OffsetBaseline (2) """
    HardcodedOffsetBaseline = None
    MainBaseline = None
    None = None
    OffsetBaseline = None
    value__ = None


class CorridorCodeCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, code):
        """ Add(self: CorridorCodeCollection, code: str) """
        pass

    def Clear(self):
        """ Clear(self: CorridorCodeCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: CorridorCodeCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CorridorCodeCollection) -> IEnumerator[str] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CorridorCodeCollection) -> IEnumerator """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[str](enumerable: IEnumerable[str], value: str) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorCodeCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CorridorCodeCollection) -> int

"""



class CorridorCollection(CivilWrapper<AcDbDatabase>):
    # no doc
    def Add(self, corridorName, baselineName=None, alignmentId=None, profileId=None, baselineRegionName=None, assemblyId=None):
        """
        Add(self: CorridorCollection, corridorName: str) -> ObjectId
        Add(self: CorridorCollection, corridorName: str, baselineName: str, alignmentId: ObjectId, profileId: ObjectId) -> ObjectId
        Add(self: CorridorCollection, corridorName: str, baselineName: str, alignmentId: ObjectId, profileId: ObjectId, baselineRegionName: str, assemblyId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AcDbDatabase>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CorridorCollection) -> IEnumerator[ObjectId] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CorridorCollection) -> IEnumerator """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerable: IEnumerable[ObjectId], value: ObjectId) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CorridorCollection) -> int

"""



class CorridorFeatureLine(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CorridorFeatureLine, A_0: bool) """
        pass

    def ExportAsAlignment(self, alignmentName, siteId, layerId, styleId, labelSetId, alignmentType):
        """ ExportAsAlignment(self: CorridorFeatureLine, alignmentName: str, siteId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, alignmentType: AlignmentType) -> ObjectId """
        pass

    def ExportAsGradingFeatureLine(self, siteId, isDynamic, featureLineName=None, layerId=None, styleId=None, smoothOption=None):
        """
        ExportAsGradingFeatureLine(self: CorridorFeatureLine, siteId: ObjectId, isDynamic: bool) -> ObjectId
        ExportAsGradingFeatureLine(self: CorridorFeatureLine, siteId: ObjectId, isDynamic: bool, featureLineName: str, layerId: ObjectId, styleId: ObjectId, smoothOption: GradingSmoothOption) -> ObjectId
        """
        pass

    def ExportAsPolyline3d(self):
        """ ExportAsPolyline3d(self: CorridorFeatureLine) -> ObjectId """
        pass

    def ExportAsPolyline3dCollection(self):
        """ ExportAsPolyline3dCollection(self: CorridorFeatureLine) -> ObjectIdCollection """
        pass

    def ExportAsProfile(self, profileName, alignmentId, layerId, styleId, labelSetId):
        """ ExportAsProfile(self: CorridorFeatureLine, profileName: str, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId """
        pass

    CodeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeName(self: CorridorFeatureLine) -> str

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorFeatureLine) -> ObjectId

"""

    FeatureLinePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLinePoints(self: CorridorFeatureLine) -> FeatureLinePointCollection

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: CorridorFeatureLine) -> ObjectId

Set: StyleId(self: CorridorFeatureLine) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: CorridorFeatureLine) -> str

Set: StyleName(self: CorridorFeatureLine) = value
"""



class CorridorLinkDisplay(Enum):
    """ enum CorridorLinkDisplay, values: Dashed (2), DashedWithArrowhead (3), Normal (0), NormalWithArrowhead (1) """
    Dashed = None
    DashedWithArrowhead = None
    Normal = None
    NormalWithArrowhead = None
    value__ = None


class CorridorLinkDrawOverride(Enum):
    """ enum CorridorLinkDrawOverride, values: Dashed (1), Normal (0), WithArrowhead (2) """
    Dashed = None
    Normal = None
    value__ = None
    WithArrowhead = None


class CorridorPointCodeOption(object):
    """ CorridorPointCodeOption() """
    CodeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeName(self: CorridorPointCodeOption) -> str

Set: CodeName(self: CorridorPointCodeOption) = value
"""

    Selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selected(self: CorridorPointCodeOption) -> bool

Set: Selected(self: CorridorPointCodeOption) = value
"""



class CorridorPointCodeSelector(object):
    """ CorridorPointCodeSelector(corridor: Corridor) """
    def GetAllCodes(self):
        """ GetAllCodes(self: CorridorPointCodeSelector) -> Array[str] """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CorridorPointCodeSelector) -> IEnumerator[CorridorPointCodeOption] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CorridorPointCodeSelector) -> IEnumerator """
        pass

    def SelectAll(self):
        """ SelectAll(self: CorridorPointCodeSelector) """
        pass

    def UnSelectAll(self):
        """ UnSelectAll(self: CorridorPointCodeSelector) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CorridorPointCodeOption](enumerable: IEnumerable[CorridorPointCodeOption], value: CorridorPointCodeOption) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, corridor):
        """ __new__(cls: type, corridor: Corridor) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CorridorPointCodeSelector) -> int

"""



class Section(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    LeftOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftOffset(self: Section) -> float

"""

    LeftSwathWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftSwathWidth(self: Section) -> float

Set: LeftSwathWidth(self: Section) = value
"""

    MaximumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumElevation(self: Section) -> float

"""

    MinmumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinmumElevation(self: Section) -> float

"""

    ParentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentId(self: Section) -> ObjectId

"""

    RightOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightOffset(self: Section) -> float

"""

    RightSwathWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightSwathWidth(self: Section) -> float

Set: RightSwathWidth(self: Section) = value
"""

    SampleLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineId(self: Section) -> ObjectId

"""

    SectionPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionPoints(self: Section) -> SectionPointCollection

"""

    SourceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceName(self: Section) -> str

"""

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceType(self: Section) -> SectionSourceType

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: Section) -> float

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Section) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: Section) = value
"""

    UpdateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateMode(self: Section) -> SectionUpdateType

Set: UpdateMode(self: Section) = value
"""



class CorridorSection(Section):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetCorridor(self):
        """ GetCorridor(self: CorridorSection) -> ObjectId """
        pass

    def GetLinkCodes(self):
        """ GetLinkCodes(self: CorridorSection) -> Array[str] """
        pass

    def GetPointCodes(self):
        """ GetPointCodes(self: CorridorSection) -> Array[str] """
        pass

    def GetShapeCodes(self):
        """ GetShapeCodes(self: CorridorSection) -> Array[str] """
        pass

    def SetCorridor(self, *__args):
        """ SetCorridor(self: CorridorSection, corridorId: ObjectId)SetCorridor(self: CorridorSection, corridorName: str) """
        pass

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: CorridorSection) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: CorridorSection) = value
"""



class CorridorSlopePattern(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CorridorSlopePattern, A_0: bool) """
        pass

    BaselineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineId(self: CorridorSlopePattern) -> ObjectId

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorSlopePattern) -> ObjectId

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: CorridorSlopePattern) -> float

Set: EndStation(self: CorridorSlopePattern) = value
"""

    FeatureLine1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLine1(self: CorridorSlopePattern) -> CorridorFeatureLine

"""

    FeatureLine2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLine2(self: CorridorSlopePattern) -> CorridorFeatureLine

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: CorridorSlopePattern) -> float

Set: StartStation(self: CorridorSlopePattern) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: CorridorSlopePattern) -> ObjectId

Set: StyleId(self: CorridorSlopePattern) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: CorridorSlopePattern) -> str

Set: StyleName(self: CorridorSlopePattern) = value
"""



class CorridorSlopePatternCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, featureLine1, featureLine2, slopePatternStyleId):
        """ Add(self: CorridorSlopePatternCollection, featureLine1: CorridorFeatureLine, featureLine2: CorridorFeatureLine, slopePatternStyleId: ObjectId) -> CorridorSlopePattern """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbCorridor>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CorridorSlopePatternCollection) -> IEnumerator[CorridorSlopePattern] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CorridorSlopePatternCollection) -> IEnumerator """
        pass

    def Remove(self, slopePattern):
        """ Remove(self: CorridorSlopePatternCollection, slopePattern: CorridorSlopePattern) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CorridorSlopePatternCollection, index: int) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CorridorSlopePattern](enumerable: IEnumerable[CorridorSlopePattern], value: CorridorSlopePattern) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorSlopePatternCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CorridorSlopePatternCollection) -> int

"""



class CorridorSurface(CivilWrapper<AeccDbCorridor>):
    # no doc
    def AddFeatureLineCode(self, codeName):
        """ AddFeatureLineCode(self: CorridorSurface, codeName: str) """
        pass

    def AddLinkCode(self, codeName, addAsBreakLine):
        """ AddLinkCode(self: CorridorSurface, codeName: str, addAsBreakLine: bool) """
        pass

    def Dispose(self):
        """ Dispose(self: CorridorSurface, A_0: bool) """
        pass

    def FeatureLineCodeIsBreak(self, name):
        """ FeatureLineCodeIsBreak(self: CorridorSurface, name: str) -> bool """
        pass

    def FeatureLineCodes(self):
        """ FeatureLineCodes(self: CorridorSurface) -> Array[str] """
        pass

    def FindElevationAtXY(self, x, y):
        """ FindElevationAtXY(self: CorridorSurface, x: float, y: float) -> float """
        pass

    def GetSampleElevations(self, startX, startY, endX, endY):
        """ GetSampleElevations(self: CorridorSurface, startX: float, startY: float, endX: float, endY: float) -> Point3dCollection """
        pass

    def IsLinkCodeAsBreakLine(self, codeName):
        """ IsLinkCodeAsBreakLine(self: CorridorSurface, codeName: str) -> bool """
        pass

    def LinkCodes(self):
        """ LinkCodes(self: CorridorSurface) -> Array[str] """
        pass

    def PointCodes(self):
        """ PointCodes(self: CorridorSurface) -> Array[str] """
        pass

    def RemoveFeatureLineCode(self, codeName):
        """ RemoveFeatureLineCode(self: CorridorSurface, codeName: str) -> bool """
        pass

    def RemoveLinkCode(self, codeName):
        """ RemoveLinkCode(self: CorridorSurface, codeName: str) -> bool """
        pass

    def SetLinkCodeAsBreakLine(self, codeName, asBreakLine):
        """ SetLinkCodeAsBreakLine(self: CorridorSurface, codeName: str, asBreakLine: bool) """
        pass

    Boundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Boundaries(self: CorridorSurface) -> CorridorSurfaceBoundaryCollection

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorSurface) -> ObjectId

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: CorridorSurface) -> str

Set: Description(self: CorridorSurface) = value
"""

    IsBuild = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBuild(self: CorridorSurface) -> bool

Set: IsBuild(self: CorridorSurface) = value
"""

    IsDraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDraw(self: CorridorSurface) -> bool

"""

    Masks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Masks(self: CorridorSurface) -> CorridorSurfaceMaskCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CorridorSurface) -> str

Set: Name(self: CorridorSurface) = value
"""

    OverhangCorrection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverhangCorrection(self: CorridorSurface) -> OverhangCorrectionType

Set: OverhangCorrection(self: CorridorSurface) = value
"""

    RenderMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMaterialId(self: CorridorSurface) -> ObjectId

Set: RenderMaterialId(self: CorridorSurface) = value
"""

    SectionStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionStyleId(self: CorridorSurface) -> ObjectId

"""

    SurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceId(self: CorridorSurface) -> ObjectId

"""

    SurfaceStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceStyleId(self: CorridorSurface) -> ObjectId

Set: SurfaceStyleId(self: CorridorSurface) = value
"""



class CorridorSurfaceBaseMask(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CorridorSurfaceBaseMask, A_0: bool) """
        pass

    def PolygonPoints(self):
        """ PolygonPoints(self: CorridorSurfaceBaseMask) -> Array[Point3d] """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorSurfaceBaseMask) -> ObjectId

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: CorridorSurfaceBaseMask) -> str

Set: Description(self: CorridorSurfaceBaseMask) = value
"""

    FeatureLineComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineComponents(self: CorridorSurfaceBaseMask) -> FeatureLineComponentCollection

"""

    IsDefinedFromPolygon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefinedFromPolygon(self: CorridorSurfaceBaseMask) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CorridorSurfaceBaseMask) -> str

Set: Name(self: CorridorSurfaceBaseMask) = value
"""



class CorridorSurfaceBoundary(CorridorSurfaceBaseMask):
    # no doc
    def Dispose(self):
        """ Dispose(self: CorridorSurfaceBaseMask, A_0: bool) """
        pass

    BoundaryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryType(self: CorridorSurfaceBoundary) -> CorridorSurfaceBoundaryType

Set: BoundaryType(self: CorridorSurfaceBoundary) = value
"""

    IsCorridorExtents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCorridorExtents(self: CorridorSurfaceBoundary) -> bool

"""



class CorridorSurfaceBoundaryCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, boundaryName, *__args):
        """
        Add(self: CorridorSurfaceBoundaryCollection, boundaryName: str, featureLineCode: str) -> CorridorSurfaceBoundary
        Add(self: CorridorSurfaceBoundaryCollection, boundaryName: str) -> CorridorSurfaceBoundary
        Add(self: CorridorSurfaceBoundaryCollection, boundaryName: str, points: Point3dCollection) -> CorridorSurfaceBoundary
        Add(self: CorridorSurfaceBoundaryCollection, boundaryName: str, polylineId: ObjectId) -> CorridorSurfaceBoundary
        """
        pass

    def AddCorridorExtentsBoundary(self, boundaryName):
        """ AddCorridorExtentsBoundary(self: CorridorSurfaceBoundaryCollection, boundaryName: str) -> CorridorSurfaceBoundary """
        pass

    def BoundaryNames(self):
        """ BoundaryNames(self: CorridorSurfaceBoundaryCollection) -> Array[str] """
        pass

    def Dispose(self):
        """ Dispose(self: CorridorSurfaceBoundaryCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CorridorSurfaceBoundaryCollection) -> IEnumerator[CorridorSurfaceBoundary] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CorridorSurfaceBoundaryCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """
        Remove(self: CorridorSurfaceBoundaryCollection, boundaryName: str) -> bool
        Remove(self: CorridorSurfaceBoundaryCollection, boundary: CorridorSurfaceBoundary) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CorridorSurfaceBoundaryCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CorridorSurfaceBoundary](enumerable: IEnumerable[CorridorSurfaceBoundary], value: CorridorSurfaceBoundary) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorSurfaceBoundaryCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CorridorSurfaceBoundaryCollection) -> int

"""



class CorridorSurfaceBoundaryType(Enum):
    """ enum CorridorSurfaceBoundaryType, values: InsideBoundary (1), OutsideBoundary (2) """
    InsideBoundary = None
    OutsideBoundary = None
    value__ = None


class CorridorSurfaceCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, corridorSurfaceName, styleId=None):
        """
        Add(self: CorridorSurfaceCollection, corridorSurfaceName: str, styleId: ObjectId) -> CorridorSurface
        Add(self: CorridorSurfaceCollection, corridorSurfaceName: str) -> CorridorSurface
        """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbCorridor>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CorridorSurfaceCollection) -> IEnumerator[CorridorSurface] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CorridorSurfaceCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """
        Remove(self: CorridorSurfaceCollection, corridorSurfaceName: str) -> bool
        Remove(self: CorridorSurfaceCollection, corridorSurface: CorridorSurface) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CorridorSurfaceCollection, index: int) """
        pass

    def SurfaceNames(self):
        """ SurfaceNames(self: CorridorSurfaceCollection) -> Array[str] """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CorridorSurface](enumerable: IEnumerable[CorridorSurface], value: CorridorSurface) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorSurfaceCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CorridorSurfaceCollection) -> int

"""



class CorridorSurfaceMask(CorridorSurfaceBaseMask):
    # no doc
    def Dispose(self):
        """ Dispose(self: CorridorSurfaceBaseMask, A_0: bool) """
        pass

    RenderMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMaterialId(self: CorridorSurfaceMask) -> ObjectId

Set: RenderMaterialId(self: CorridorSurfaceMask) = value
"""



class CorridorSurfaceMaskCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, maskName, *__args):
        """
        Add(self: CorridorSurfaceMaskCollection, maskName: str, featureLineCode: str) -> CorridorSurfaceMask
        Add(self: CorridorSurfaceMaskCollection, maskName: str) -> CorridorSurfaceMask
        Add(self: CorridorSurfaceMaskCollection, maskName: str, points: Point3dCollection) -> CorridorSurfaceMask
        Add(self: CorridorSurfaceMaskCollection, maskName: str, polylineId: ObjectId) -> CorridorSurfaceMask
        """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbCorridor>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CorridorSurfaceMaskCollection) -> IEnumerator[CorridorSurfaceMask] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CorridorSurfaceMaskCollection) -> IEnumerator """
        pass

    def MaskNames(self):
        """ MaskNames(self: CorridorSurfaceMaskCollection) -> Array[str] """
        pass

    def Remove(self, *__args):
        """
        Remove(self: CorridorSurfaceMaskCollection, maskName: str) -> bool
        Remove(self: CorridorSurfaceMaskCollection, mask: CorridorSurfaceMask) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CorridorSurfaceMaskCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CorridorSurfaceMask](enumerable: IEnumerable[CorridorSurfaceMask], value: CorridorSurfaceMask) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: CorridorSurfaceMaskCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CorridorSurfaceMaskCollection) -> int

"""



class PressurePartProfileLabel(FeatureLabel):
    # no doc
    def checkProfileViewPartInProfileView(self, *args): #cannot find CLR method
        """ checkProfileViewPartInProfileView(oidProfileViewPart: AcDbObjectId, oidProfileView: AcDbObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PressurePartProfileLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PressurePartProfileLabel) = value
"""


    m_SubData = None


class CrossingPressurePipeProfileLabel(PressurePartProfileLabel):
    # no doc
    @staticmethod
    def Create(profileViewPartId, profileViewId, ratio, labelStyleId):
        """ Create(profileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectIdCollection """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(profileViewPartId, profileViewId):
        """ GetAvailableLabelIds(profileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: CrossingPressurePipeProfileLabel) -> float

Set: Ratio(self: CrossingPressurePipeProfileLabel) = value
"""


    m_SubData = None


class CurbReturnJoiningType(Enum):
    """ enum CurbReturnJoiningType, values: ExtendingEdge (1), JoiningTangent (0) """
    ExtendingEdge = None
    JoiningTangent = None
    value__ = None


class TransitionDescriptionBase(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: TransitionDescriptionBase, A_0: bool) """
        pass

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: TransitionDescriptionBase) -> float

Set: EndStation(self: TransitionDescriptionBase) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: TransitionDescriptionBase) -> float

Set: Length(self: TransitionDescriptionBase) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: TransitionDescriptionBase) -> float

Set: StartStation(self: TransitionDescriptionBase) = value
"""


    m_pTransitionParam = None


class CurveCurveReverseCurveTransitionDescription(TransitionDescriptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: TransitionDescriptionBase, A_0: bool) """
        pass

    FirstCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstCurveRadius(self: CurveCurveReverseCurveTransitionDescription) -> float

Set: FirstCurveRadius(self: CurveCurveReverseCurveTransitionDescription) = value
"""

    ReverseCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseCurveRadius(self: CurveCurveReverseCurveTransitionDescription) -> float

Set: ReverseCurveRadius(self: CurveCurveReverseCurveTransitionDescription) = value
"""

    SecondCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondCurveRadius(self: CurveCurveReverseCurveTransitionDescription) -> float

Set: SecondCurveRadius(self: CurveCurveReverseCurveTransitionDescription) = value
"""


    m_pTransitionParam = None


class CurveLineCurveTransitionDescription(TransitionDescriptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: TransitionDescriptionBase, A_0: bool) """
        pass

    EntryCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryCurveRadius(self: CurveLineCurveTransitionDescription) -> float

Set: EntryCurveRadius(self: CurveLineCurveTransitionDescription) = value
"""

    ExitCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExitCurveRadius(self: CurveLineCurveTransitionDescription) -> float

Set: ExitCurveRadius(self: CurveLineCurveTransitionDescription) = value
"""


    m_pTransitionParam = None


class CurveParamType(Enum):
    """ enum CurveParamType, values: ChordLength (3), CurveAngle (7), CurveLength (4), CurveThroughPoint (8), DegreeOfCurve (1), ExternalDist (5), MiddleOrdinate (6), Radius (0), TangentLength (2) """
    ChordLength = None
    CurveAngle = None
    CurveLength = None
    CurveThroughPoint = None
    DegreeOfCurve = None
    ExternalDist = None
    MiddleOrdinate = None
    Radius = None
    TangentLength = None
    value__ = None


class CurveReverseCurveTransitionDescription(TransitionDescriptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: TransitionDescriptionBase, A_0: bool) """
        pass

    EntryCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntryCurveRadius(self: CurveReverseCurveTransitionDescription) -> float

Set: EntryCurveRadius(self: CurveReverseCurveTransitionDescription) = value
"""

    ReverseCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseCurveRadius(self: CurveReverseCurveTransitionDescription) -> float

Set: ReverseCurveRadius(self: CurveReverseCurveTransitionDescription) = value
"""


    m_pTransitionParam = None


class CurveType(Enum):
    """ enum CurveType, values: Compound (0), Reverse (1) """
    Compound = None
    Reverse = None
    value__ = None


class PointGroupQuery(object):
    """ PointGroupQuery() """
    def getQueryString(self, *args): #cannot find CLR method
        """ getQueryString(self: PointGroupQuery) -> str """
        pass

    def isCurrentPointGroup(self, *args): #cannot find CLR method
        """ isCurrentPointGroup(self: PointGroupQuery, pvalue: AecRmCString*) -> bool """
        pass

    def isExistingPointGroup(self, *args): #cannot find CLR method
        """ isExistingPointGroup(self: PointGroupQuery, pvalue: AecRmCString*) -> bool """
        pass

    def loadQuery(self, *args): #cannot find CLR method
        """ loadQuery(self: PointGroupQuery) """
        pass

    def saveQuery(self, *args): #cannot find CLR method
        """ saveQuery(self: PointGroupQuery) """
        pass

    def setQueryString(self, *args): #cannot find CLR method
        """ setQueryString(self: PointGroupQuery, query: str) """
        pass

    def setQueryStringFromItems(self, *args): #cannot find CLR method
        """ setQueryStringFromItems(self: PointGroupQuery, items: list<AeccPointGroupQueryBuilder::DataItem\,std::allocator<AeccPointGroupQueryBuilder::DataItem> >*) """
        pass

    QueryString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QueryString(self: PointGroupQuery) -> str

"""

    UseCaseSensitiveMatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseCaseSensitiveMatch(self: PointGroupQuery) -> bool

Set: UseCaseSensitiveMatch(self: PointGroupQuery) = value
"""


    _curBuilder = None
    _curPG = None


class CustomPointGroupQuery(PointGroupQuery):
    """ CustomPointGroupQuery() """
    QueryString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QueryString(self: CustomPointGroupQuery) -> str

Set: QueryString(self: CustomPointGroupQuery) = value
"""


    _curBuilder = None
    _curPG = None


class DatumRoundingType(Enum):
    """ enum DatumRoundingType, values: ExactElevation (64), PreviousMajorGrid (16), PreviousMinorGrid (32) """
    ExactElevation = None
    PreviousMajorGrid = None
    PreviousMinorGrid = None
    value__ = None


class DBObject(DBObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: DBObject) -> object

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: DBObject) -> str

Set: Description(self: DBObject) = value
"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DBObject) -> object

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DBObject) -> str

Set: Name(self: DBObject) = value
"""



class DesignSpeed(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: DesignSpeed) -> str

Set: Comment(self: DesignSpeed) = value
"""

    SpeedNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpeedNumber(self: DesignSpeed) -> int

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: DesignSpeed) -> float

Set: Station(self: DesignSpeed) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DesignSpeed) -> float

Set: Value(self: DesignSpeed) = value
"""



class DesignSpeedCollection(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Add(self, station, speed):
        """ Add(self: DesignSpeedCollection, station: float, speed: float) -> DesignSpeed """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    def GetDesignSpeed(self, rawStation):
        """ GetDesignSpeed(self: DesignSpeedCollection, rawStation: float) -> DesignSpeed """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DesignSpeedCollection) -> IEnumerator[DesignSpeed] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: DesignSpeedCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """ Remove(self: DesignSpeedCollection, Index: int)Remove(self: DesignSpeedCollection, rawStation: float) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[DesignSpeed](enumerable: IEnumerable[DesignSpeed], value: DesignSpeed) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DesignSpeedCollection) -> int

"""



class DomainType(Enum):
    """ enum DomainType, values: Pipe (1), Structure (2) """
    Pipe = None
    Structure = None
    value__ = None


class ElevationRangeType(Enum):
    """ enum ElevationRangeType, values: Automatic (0), UserSpecified (1) """
    Automatic = None
    UserSpecified = None
    value__ = None


class EntityAttachType(Enum):
    """ enum EntityAttachType, values: Append (0), Prepend (1) """
    Append = None
    Prepend = None
    value__ = None


class EntityVerticalConstraintType(Enum):
    """ enum EntityVerticalConstraintType, values: BestFit (531), CurveLength (513), HighLowPoints (532), KValue (514), NextSubEntEndAndPassPt (527), NextSubEntPassPtAndParameter (523), NextSubEntPassPtWithGrade (525), NoConstraints (530), PassThroughPt (516), PassThroughPt1 (528), PassThroughPt1AndPt2 (517), PassThroughPt2 (529), PreviousSubEntEndAndPassPt (526), PreviousSubEntPassPtAndParameter (522), PreviousSubEntPassPtWithGrade (524), Radius (515), ThreePassPoints (519), TwoPassPointsAndGrade (520), TwoPassPointsAndParameter (521) """
    BestFit = None
    CurveLength = None
    HighLowPoints = None
    KValue = None
    NextSubEntEndAndPassPt = None
    NextSubEntPassPtAndParameter = None
    NextSubEntPassPtWithGrade = None
    NoConstraints = None
    PassThroughPt = None
    PassThroughPt1 = None
    PassThroughPt1AndPt2 = None
    PassThroughPt2 = None
    PreviousSubEntEndAndPassPt = None
    PreviousSubEntPassPtAndParameter = None
    PreviousSubEntPassPtWithGrade = None
    Radius = None
    ThreePassPoints = None
    TwoPassPointsAndGrade = None
    TwoPassPointsAndParameter = None
    value__ = None


class FeatureLine(Feature):
    # no doc
    def AssignElevationsFromSurface(self, surfaceId, bIncIntermediate):
        """ AssignElevationsFromSurface(self: FeatureLine, surfaceId: ObjectId, bIncIntermediate: bool) """
        pass

    @staticmethod
    def Create(featurelineName, idCreatedFrom, siteId=None):
        """
        Create(featurelineName: str, idCreatedFrom: ObjectId, siteId: ObjectId) -> ObjectId
        Create(featurelineName: str, idCreatedFrom: ObjectId) -> ObjectId
        """
        pass

    def DeleteElevationPoint(self, pt):
        """ DeleteElevationPoint(self: FeatureLine, pt: Point3d) """
        pass

    def DeletePIPoint(self, pt):
        """ DeletePIPoint(self: FeatureLine, pt: Point3d) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def Get3dDistanceAtPoint(self, pt):
        """ Get3dDistanceAtPoint(self: FeatureLine, pt: Point3d) -> float """
        pass

    def GetBulge(self, index):
        """ GetBulge(self: FeatureLine, index: int) -> float """
        pass

    def GetDeflectionAngleAtPoint(self, pt):
        """ GetDeflectionAngleAtPoint(self: FeatureLine, pt: Point3d) -> float """
        pass

    def GetGradeInAtPoint(self, pt):
        """ GetGradeInAtPoint(self: FeatureLine, pt: Point3d) -> float """
        pass

    def GetGradeOutAtPoint(self, pt):
        """ GetGradeOutAtPoint(self: FeatureLine, pt: Point3d) -> float """
        pass

    def GetPoints(self, type):
        """ GetPoints(self: FeatureLine, type: FeatureLinePointType) -> Point3dCollection """
        pass

    def InsertElevationPoint(self, pt):
        """ InsertElevationPoint(self: FeatureLine, pt: Point3d) """
        pass

    def InsertPIPoint(self, pt):
        """ InsertPIPoint(self: FeatureLine, pt: Point3d) """
        pass

    @staticmethod
    def MoveToNoneSite(featureLineId):
        """ MoveToNoneSite(featureLineId: ObjectId) """
        pass

    @staticmethod
    def MoveToSite(featureLineId, destinationSiteId):
        """ MoveToSite(featureLineId: ObjectId, destinationSiteId: ObjectId) """
        pass

    def SetBulge(self, index, bugle):
        """ SetBulge(self: FeatureLine, index: int, bugle: float) """
        pass

    def SetPointElevation(self, index, elevation):
        """ SetPointElevation(self: FeatureLine, index: int, elevation: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ElevationPointsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationPointsCount(self: FeatureLine) -> int

"""

    Length2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2D(self: FeatureLine) -> float

"""

    Length3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3D(self: FeatureLine) -> float

"""

    MaxElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxElevation(self: FeatureLine) -> float

"""

    MaxGrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxGrade(self: FeatureLine) -> float

"""

    MinElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinElevation(self: FeatureLine) -> float

"""

    MinGrade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinGrade(self: FeatureLine) -> float

"""

    PIPointsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PIPointsCount(self: FeatureLine) -> int

"""

    PointsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointsCount(self: FeatureLine) -> int

"""

    SiteId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SiteId(self: FeatureLine) -> ObjectId

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: FeatureLine) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: FeatureLine) -> str

Set: StyleName(self: FeatureLine) = value
"""



class FeatureLineCodeInfo(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: FeatureLineCodeInfo, A_0: bool) """
        pass

    CodeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeName(self: FeatureLineCodeInfo) -> str

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLineCodeInfo) -> ObjectId

"""

    IsConnect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnect(self: FeatureLineCodeInfo) -> bool

Set: IsConnect(self: FeatureLineCodeInfo) = value
"""

    IsConnected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnected(self: FeatureLineCodeInfo) -> bool

Set: IsConnected(self: FeatureLineCodeInfo) = value
"""

    IsDraw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDraw(self: FeatureLineCodeInfo) -> bool

"""

    PayItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PayItems(self: FeatureLineCodeInfo) -> Array[str]

Set: PayItems(self: FeatureLineCodeInfo) = value
"""



class FeatureLineCodeInfoCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def CodeNames(self):
        """ CodeNames(self: FeatureLineCodeInfoCollection) -> Array[str] """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbCorridor>, A_0: bool) """
        pass

    def GetConnectedFeatureLineCodeInfos(self):
        """ GetConnectedFeatureLineCodeInfos(self: FeatureLineCodeInfoCollection) -> Array[FeatureLineCodeInfo] """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: FeatureLineCodeInfoCollection) -> IEnumerator[FeatureLineCodeInfo] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: FeatureLineCodeInfoCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FeatureLineCodeInfo](enumerable: IEnumerable[FeatureLineCodeInfo], value: FeatureLineCodeInfo) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLineCodeInfoCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: FeatureLineCodeInfoCollection) -> int

"""



class FeatureLineCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: FeatureLineCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: FeatureLineCollection) -> IEnumerator[CorridorFeatureLine] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: FeatureLineCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CorridorFeatureLine](enumerable: IEnumerable[CorridorFeatureLine], value: CorridorFeatureLine) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    ConnectDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectDirection(self: FeatureLineCollection) -> FeatureLineConnectDirectionType

Set: ConnectDirection(self: FeatureLineCollection) = value
"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLineCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: FeatureLineCollection) -> int

"""

    FeatureLineCodeInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineCodeInfo(self: FeatureLineCollection) -> FeatureLineCodeInfo

"""

    IsConnectExtraPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsConnectExtraPoints(self: FeatureLineCollection) -> bool

Set: IsConnectExtraPoints(self: FeatureLineCollection) = value
"""



class FeatureLineCollectionMap(CivilWrapper<AeccDbCorridor>):
    # no doc
    def CodeNames(self):
        """ CodeNames(self: FeatureLineCollectionMap) -> Array[str] """
        pass

    def Dispose(self):
        """ Dispose(self: FeatureLineCollectionMap, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: FeatureLineCollectionMap) -> IEnumerator[FeatureLineCollection] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: FeatureLineCollectionMap) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FeatureLineCollection](enumerable: IEnumerable[FeatureLineCollection], value: FeatureLineCollection) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLineCollectionMap) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: FeatureLineCollectionMap) -> int

"""



class FeatureLineComponent(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: FeatureLineComponent, A_0: bool) """
        pass

    BaselineAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineAlignmentId(self: FeatureLineComponent) -> ObjectId

"""

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLineComponent) -> ObjectId

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: FeatureLineComponent) -> float

Set: EndStation(self: FeatureLineComponent) = value
"""

    FeatureLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLine(self: FeatureLineComponent) -> CorridorFeatureLine

"""

    IsReversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReversed(self: FeatureLineComponent) -> bool

Set: IsReversed(self: FeatureLineComponent) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: FeatureLineComponent) -> float

Set: StartStation(self: FeatureLineComponent) = value
"""

    UseEndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseEndStation(self: FeatureLineComponent) -> bool

"""

    UseStartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseStartStation(self: FeatureLineComponent) -> bool

"""



class FeatureLineComponentCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Add(self, featureLine):
        """ Add(self: FeatureLineComponentCollection, featureLine: CorridorFeatureLine) -> FeatureLineComponent """
        pass

    def Dispose(self):
        """ Dispose(self: FeatureLineComponentCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: FeatureLineComponentCollection) -> IEnumerator[FeatureLineComponent] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: FeatureLineComponentCollection) -> IEnumerator """
        pass

    def Remove(self, featureLineComponent):
        """ Remove(self: FeatureLineComponentCollection, featureLineComponent: FeatureLineComponent) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: FeatureLineComponentCollection, index: int) """
        pass

    def Swap(self, component1, component2):
        """ Swap(self: FeatureLineComponentCollection, component1: FeatureLineComponent, component2: FeatureLineComponent) """
        pass

    def SwapAt(self, index1, index2):
        """ SwapAt(self: FeatureLineComponentCollection, index1: int, index2: int) """
        pass

    def Validate(self):
        """ Validate(self: FeatureLineComponentCollection) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FeatureLineComponent](enumerable: IEnumerable[FeatureLineComponent], value: FeatureLineComponent) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLineComponentCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: FeatureLineComponentCollection) -> int

"""



class FeatureLinePoint(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: FeatureLinePoint, A_0: bool) """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLinePoint) -> ObjectId

"""

    IsBreak = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBreak(self: FeatureLinePoint) -> bool

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: FeatureLinePoint) -> float

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: FeatureLinePoint) -> float

"""

    XYZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XYZ(self: FeatureLinePoint) -> Point3d

"""



class FeatureLinePointCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: FeatureLinePointCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: FeatureLinePointCollection) -> IEnumerator[FeatureLinePoint] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: FeatureLinePointCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[FeatureLinePoint](enumerable: IEnumerable[FeatureLinePoint], value: FeatureLinePoint) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: FeatureLinePointCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: FeatureLinePointCollection) -> int

"""



class FlowDirectionMethodType(Enum):
    """ enum FlowDirectionMethodType, values: Bidirectional (0), BySlope (3), EndToStart (2), StartToEnd (1) """
    Bidirectional = None
    BySlope = None
    EndToStart = None
    StartToEnd = None
    value__ = None


class FlowDirectionType(Enum):
    """ enum FlowDirectionType, values: Bidirectional (0), EndToStart (2), StartToEnd (1) """
    Bidirectional = None
    EndToStart = None
    StartToEnd = None
    value__ = None


class FlowPath(object):
    # no doc
    def GetFlowSegmentAt(self, index):
        """ GetFlowSegmentAt(self: FlowPath, index: int) -> FlowSegment """
        pass

    FlowSegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowSegmentCount(self: FlowPath) -> int

"""



class FlowSegment(object):
    # no doc

class FlowSegmentLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(flowSegment, labelStyleId=None):
        """
        Create(flowSegment: FlowSegment, labelStyleId: ObjectId) -> ObjectId
        Create(flowSegment: FlowSegment) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(catchmentId):
        """ GetAvailableLabelIds(catchmentId: ObjectId) -> ObjectIdCollection """
        pass

    FlowSegmentIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowSegmentIndex(self: FlowSegmentLabel) -> int

Set: FlowSegmentIndex(self: FlowSegmentLabel) = value
"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: FlowSegmentLabel) -> float

Set: Ratio(self: FlowSegmentLabel) = value
"""


    m_SubData = None


class Folder(DBObject):
    # no doc
    def AddEntity(self, entityId):
        """ AddEntity(self: Folder, entityId: ObjectId) """
        pass

    def CreateFolder(self, name):
        """ CreateFolder(self: Folder, name: str) -> ObjectId """
        pass

    def DeleteFolder(self):
        """ DeleteFolder(self: Folder) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetFolder(self, nameOrPath):
        """ GetFolder(self: Folder, nameOrPath: str) -> ObjectId """
        pass

    def GetParent(self):
        """ GetParent(self: Folder) -> ObjectId """
        pass

    def GetPath(self):
        """ GetPath(self: Folder) -> str """
        pass

    def GetSubFolders(self):
        """ GetSubFolders(self: Folder) -> ObjectIdCollection """
        pass

    def RenameFolder(self, newName):
        """ RenameFolder(self: Folder, newName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class FolderUtil(object):
    """ FolderUtil() """
    @staticmethod
    def GetAlignmentRootFolder(aType, database):
        """ GetAlignmentRootFolder(aType: AlignmentType, database: Database) -> ObjectId """
        pass

    @staticmethod
    def GetNonAlignmentRootFolder(rxClass, database):
        """ GetNonAlignmentRootFolder(rxClass: RXClass, database: Database) -> ObjectId """
        pass


class GeneralSegmentLabel(Label):
    # no doc
    @staticmethod
    def Create(featureId, ratio, lineLabelStyleId=None, curveLabelStyleId=None):
        """
        Create(featureId: ObjectId, ratio: float, lineLabelStyleId: ObjectId, curveLabelStyleId: ObjectId) -> ObjectId
        Create(featureId: ObjectId, ratio: float) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(featureId):
        """ GetAvailableLabelIds(featureId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    CurveLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveLabelStyleId(self: GeneralSegmentLabel) -> ObjectId

Set: CurveLabelStyleId(self: GeneralSegmentLabel) = value
"""

    LineLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineLabelStyleId(self: GeneralSegmentLabel) -> ObjectId

Set: LineLabelStyleId(self: GeneralSegmentLabel) = value
"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: GeneralSegmentLabel) -> float

Set: Ratio(self: GeneralSegmentLabel) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: GeneralSegmentLabel) -> str

Set: StyleName(self: GeneralSegmentLabel) = value
"""


    m_SubData = None


class GeneralSurfaceProperties(object):
    # no doc
    MaximumCoordinateX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumCoordinateX(self: GeneralSurfaceProperties) -> float

"""

    MaximumCoordinateY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumCoordinateY(self: GeneralSurfaceProperties) -> float

"""

    MaximumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumElevation(self: GeneralSurfaceProperties) -> float

"""

    MeanElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeanElevation(self: GeneralSurfaceProperties) -> float

"""

    MinimumCoordinateX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumCoordinateX(self: GeneralSurfaceProperties) -> float

"""

    MinimumCoordinateY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumCoordinateY(self: GeneralSurfaceProperties) -> float

"""

    MinimumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumElevation(self: GeneralSurfaceProperties) -> float

"""

    NumberOfPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfPoints(self: GeneralSurfaceProperties) -> int

"""

    RevisionNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RevisionNumber(self: GeneralSurfaceProperties) -> int

"""



class Grading(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class GradingSmoothOption(object):
    """ GradingSmoothOption(isSoomth: bool, arcInclusionDistance: float, weedingDistance: float, horizDeviation: float) """
    @staticmethod # known case of __new__
    def __new__(self, isSoomth, arcInclusionDistance, weedingDistance, horizDeviation):
        """
        __new__[GradingSmoothOption]() -> GradingSmoothOption
        
        __new__(cls: type, isSoomth: bool, arcInclusionDistance: float, weedingDistance: float, horizDeviation: float)
        """
        pass

    ArcInclusionDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArcInclusionDistance(self: GradingSmoothOption) -> float

Set: ArcInclusionDistance(self: GradingSmoothOption) = value
"""

    HorizDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HorizDeviation(self: GradingSmoothOption) -> float

Set: HorizDeviation(self: GradingSmoothOption) = value
"""

    NeedSmooth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedSmooth(self: GradingSmoothOption) -> bool

Set: NeedSmooth(self: GradingSmoothOption) = value
"""

    WeedingDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeedingDistance(self: GradingSmoothOption) -> float

Set: WeedingDistance(self: GradingSmoothOption) = value
"""



class Graph(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Graph) -> Point3d

Set: Location(self: Graph) = value
"""



class GraphBandSet(object):
    # no doc
    def checkBandStyleSet(self, *args): #cannot find CLR method
        """ checkBandStyleSet(self: GraphBandSet, oidBandSetStyle: AcDbObjectId) -> bool """
        pass

    def createBandItemCollection(self, *args): #cannot find CLR method
        """ createBandItemCollection(self: GraphBandSet, pBandVector: vector<AeccDbBandStyleSetData \*\,std::allocator<AeccDbBandStyleSetData \*> >*, oidGraph: AcDbObjectId, location: BandLocationType) -> BandSetItemCollection """
        pass

    def createC3DGraphBandLabelGroups(self, *args): #cannot find CLR method
        """ createC3DGraphBandLabelGroups(self: GraphBandSet, pBandVector: vector<AeccDbBandStyleSetData \*\,std::allocator<AeccDbBandStyleSetData \*> >*) """
        pass

    def createNewBandStyleSetByName(self, *args): #cannot find CLR method
        """ createNewBandStyleSetByName(self: GraphBandSet, styleName: AecRmCString*) -> AeccDbGraphBandStyleSet* """
        pass

    def getBandSetStyleRoot(self, *args): #cannot find CLR method
        """ getBandSetStyleRoot(self: GraphBandSet, : AeccDbTreeOid*) -> AeccDbTreeOid* """
        pass

    def getBottomBandItems(self, *args): #cannot find CLR method
        """ getBottomBandItems(self: GraphBandSet) -> BandSetItemCollection """
        pass

    def getTopBandItems(self, *args): #cannot find CLR method
        """ getTopBandItems(self: GraphBandSet) -> BandSetItemCollection """
        pass

    def ImportBandSetStyle(self, bandSetId):
        """ ImportBandSetStyle(self: GraphBandSet, bandSetId: ObjectId) """
        pass

    def SaveAsBandSetStyle(self, name):
        """ SaveAsBandSetStyle(self: GraphBandSet, name: str) -> ObjectId """
        pass

    def setBottomBandItems(self, *args): #cannot find CLR method
        """ setBottomBandItems(self: GraphBandSet, bandItems: BandSetItemCollection) """
        pass

    def setTopBandItems(self, *args): #cannot find CLR method
        """ setTopBandItems(self: GraphBandSet, bandItems: BandSetItemCollection) """
        pass

    def updateBandItemByInterval(self, *args): #cannot find CLR method
        """ updateBandItemByInterval(self: GraphBandSet, pData: AeccDbBandStyleSetData*, majorInterval: float, minorInterval: float) """
        pass

    def updateBandStyleSetDatas(self, *args): #cannot find CLR method
        """ updateBandStyleSetDatas(self: GraphBandSet, pBandVector: vector<AeccDbBandStyleSetData \*\,std::allocator<AeccDbBandStyleSetData \*> >*) """
        pass

    MatchIncrementToGridIntervals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchIncrementToGridIntervals(self: GraphBandSet) -> bool

Set: MatchIncrementToGridIntervals(self: GraphBandSet) = value
"""


    m_pGraph = None


class GraphOverride(CivilWrapper<AeccDbGraph>):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverride, A_0: bool) """
        pass

    Draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Draw(self: GraphOverride) -> bool

Set: Draw(self: GraphOverride) = value
"""

    OverrideStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideStyleId(self: GraphOverride) -> ObjectId

Set: OverrideStyleId(self: GraphOverride) = value
"""

    OverrideStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideStyleName(self: GraphOverride) -> str

Set: OverrideStyleName(self: GraphOverride) = value
"""

    UseOverrideStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseOverrideStyle(self: GraphOverride) -> bool

Set: UseOverrideStyle(self: GraphOverride) = value
"""


    m_pDataLineId = None


class GraphOverrideCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverrideCollection[ItemType]) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: GraphOverrideCollection[ItemType]) -> IEnumerator[ItemType] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: GraphOverrideCollection[ItemType]) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
# Error generating skeleton for function __contains__: Method must be called on a Type for which Type.IsGenericParameter is false.

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

    ClipGridAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClipGridAt(self: GraphOverrideCollection[ItemType]) -> str

Set: ClipGridAt(self: GraphOverrideCollection[ItemType]) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GraphOverrideCollection[ItemType]) -> int

"""


    m_dataVector = None


class GridLocation(object):
    """ GridLocation(columnIndex: int, rowIndex: int) """
    def Equals(self, obj):
        """ Equals(self: GridLocation, obj: object) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, columnIndex, rowIndex):
        """
        __new__[GridLocation]() -> GridLocation
        
        __new__(cls: type, columnIndex: int, rowIndex: int)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    ColumnIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnIndex(self: GridLocation) -> int

Set: ColumnIndex(self: GridLocation) = value
"""

    RowIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowIndex(self: GridLocation) -> int

Set: RowIndex(self: GridLocation) = value
"""



class Surface(Entity):
    # no doc
    def CreateSnapshot(self):
        """ CreateSnapshot(self: Surface) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def ExportToDEM(self, fileName, coordinateSystemCode, gridSpacing, deteElevBy, useCustomNullElevationation=None, customNullElevation=None):
        """ ExportToDEM(self: Surface, fileName: str, coordinateSystemCode: str, gridSpacing: float, deteElevBy: ExportDetermineElevationType, useCustomNullElevationation: bool, customNullElevation: Single)ExportToDEM(self: Surface, fileName: str, coordinateSystemCode: str, gridSpacing: float, deteElevBy: ExportDetermineElevationType) """
        pass

    def FindDirectionAtXY(self, x, y):
        """ FindDirectionAtXY(self: Surface, x: float, y: float) -> float """
        pass

    def FindElevationAtXY(self, x, y):
        """ FindElevationAtXY(self: Surface, x: float, y: float) -> float """
        pass

    def FindPointsAlongLine(self, lineSeg3d):
        """ FindPointsAlongLine(self: Surface, lineSeg3d: LineSegment3d) -> Point3dCollection """
        pass

    def FindSlopeAtXY(self, x, y):
        """ FindSlopeAtXY(self: Surface, x: float, y: float) -> float """
        pass

    def GetBoundedVolumes(self, polygon, datumElevation=None):
        """
        GetBoundedVolumes(self: Surface, polygon: Point3dCollection) -> SurfaceVolumeInfo
        GetBoundedVolumes(self: Surface, polygon: Point3dCollection, datumElevation: float) -> SurfaceVolumeInfo
        """
        pass

    def GetGeneralProperties(self):
        """ GetGeneralProperties(self: Surface) -> GeneralSurfaceProperties """
        pass

    def GetIntersectionPoint(self, startPoint, dir):
        """ GetIntersectionPoint(self: Surface, startPoint: Point3d, dir: Vector3d) -> Point3d """
        pass

    def InternalAddCreationGeneralData(self, *args): #cannot find CLR method
        """ InternalAddCreationGeneralData(surfaceData: AeccSurfaceCreationData*, surfaceType: SurfaceType, surfaceName: str, styleId: ObjectId) """
        pass

    def InternalAddCreationGridData(self, *args): #cannot find CLR method
        """ InternalAddCreationGridData(surfaceData: AeccSurfaceCreationData*, xSpacing: float, ySpacing: float, orientation: float) """
        pass

    def InternalAddCreationVolumeData(self, *args): #cannot find CLR method
        """ InternalAddCreationVolumeData(surfaceData: AeccSurfaceCreationData*, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId) """
        pass

    def InternalCreateSurface(self, *args): #cannot find CLR method
        """ InternalCreateSurface(surfaceData: AeccSurfaceCreationData*) -> ObjectId """
        pass

    def InternalExtractBorder(self, *args): #cannot find CLR method
        """ InternalExtractBorder(self: Surface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def InternalExtractContours(self, *args): #cannot find CLR method
        """
        InternalExtractContours(self: Surface, lowElev: float, highElev: float, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        InternalExtractContours(self: Surface, lowElev: float, highElev: float, interval: float) -> ObjectIdCollection
        InternalExtractContours(self: Surface, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        InternalExtractContours(self: Surface, interval: float) -> ObjectIdCollection
        """
        pass

    def InternalExtractContoursAt(self, *args): #cannot find CLR method
        """
        InternalExtractContoursAt(self: Surface, elevation: float) -> ObjectIdCollection
        InternalExtractContoursAt(self: Surface, elevation: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def InternalExtractGridded(self, *args): #cannot find CLR method
        """ InternalExtractGridded(self: Surface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def InternalExtractMajorContours(self, *args): #cannot find CLR method
        """
        InternalExtractMajorContours(self: Surface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        InternalExtractMajorContours(self: Surface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def InternalExtractMinorContours(self, *args): #cannot find CLR method
        """
        InternalExtractMinorContours(self: Surface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        InternalExtractMinorContours(self: Surface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def InternalExtractWatershed(self, *args): #cannot find CLR method
        """ InternalExtractWatershed(self: Surface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def InternalSampleElevations(self, *args): #cannot find CLR method
        """
        InternalSampleElevations(self: Surface, curveId: ObjectId) -> Point3dCollection
        InternalSampleElevations(self: Surface, pt1: Point3d, pt2: Point3d) -> Point3dCollection
        """
        pass

    def Rebuild(self):
        """ Rebuild(self: Surface) """
        pass

    def RebuildSnapshot(self):
        """ RebuildSnapshot(self: Surface) """
        pass

    def RemoveSnapshot(self):
        """ RemoveSnapshot(self: Surface) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Analysis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Analysis(self: Surface) -> SurfaceAnalysis

"""

    BoundariesDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundariesDefinition(self: Surface) -> SurfaceDefinitionBoundaries

"""

    BuildOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BuildOptions(self: Surface) -> SurfaceBuildOptions

"""

    HasSnapshot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasSnapshot(self: Surface) -> bool

"""

    IsOutOfDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOutOfDate(self: Surface) -> bool

"""

    IsSnapshotOutOfDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSnapshotOutOfDate(self: Surface) -> bool

"""

    IsVolumeSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVolumeSurface(self: Surface) -> bool

"""

    Lock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lock(self: Surface) -> bool

Set: Lock(self: Surface) = value
"""

    Masks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Masks(self: Surface) -> SurfaceMaskCollection

"""

    Operations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Operations(self: Surface) -> SurfaceOperationCollection

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Surface) = value
"""



class GridSurface(Surface):
    # no doc
    def AddPoint(self, location, elevation):
        """ AddPoint(self: GridSurface, location: GridLocation, elevation: float) -> SurfaceOperationAddGridPoint """
        pass

    @staticmethod
    def Create(*__args):
        """
        Create(database: Database, surfaceName: str, spacingX: float, spacingY: float, orientation: float) -> ObjectId
        Create(surfaceName: str, spacingX: float, spacingY: float, orientation: float, styleId: ObjectId) -> ObjectId
        """
        pass

    @staticmethod
    def CreateFromDEM(*__args):
        """
        CreateFromDEM(database: Database, DEMFileName: str) -> ObjectId
        CreateFromDEM(DEMFileName: str, styleId: ObjectId) -> ObjectId
        """
        pass

    def DeleteLine(self, edge):
        """ DeleteLine(self: GridSurface, edge: GridSurfaceEdge) -> SurfaceOperationDeleteLine """
        pass

    def DeleteLines(self, edges):
        """ DeleteLines(self: GridSurface, edges: IEnumerable[GridSurfaceEdge]) -> SurfaceOperationDeleteMultipleLines """
        pass

    def DeletePoint(self, location):
        """ DeletePoint(self: GridSurface, location: GridLocation) -> SurfaceOperationDeleteGridPoint """
        pass

    def DeletePoints(self, locations):
        """ DeletePoints(self: GridSurface, locations: IEnumerable[GridLocation]) -> SurfaceOperationDeleteMultipleGridPoints """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def ExtractBorder(self, settingsType):
        """ ExtractBorder(self: GridSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def ExtractContours(self, *__args):
        """
        ExtractContours(self: GridSurface, lowElev: float, highElev: float, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        ExtractContours(self: GridSurface, lowElev: float, highElev: float, interval: float) -> ObjectIdCollection
        ExtractContours(self: GridSurface, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        ExtractContours(self: GridSurface, interval: float) -> ObjectIdCollection
        """
        pass

    def ExtractContoursAt(self, elevation, smoothType=None, smoothFactor=None):
        """
        ExtractContoursAt(self: GridSurface, elevation: float) -> ObjectIdCollection
        ExtractContoursAt(self: GridSurface, elevation: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractGridded(self, settingsType):
        """ ExtractGridded(self: GridSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def ExtractMajorContours(self, settingsType, smoothType=None, smoothFactor=None):
        """
        ExtractMajorContours(self: GridSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        ExtractMajorContours(self: GridSurface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractMinorContours(self, settingsType, smoothType=None, smoothFactor=None):
        """
        ExtractMinorContours(self: GridSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        ExtractMinorContours(self: GridSurface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractWatershed(self, settingsType):
        """ ExtractWatershed(self: GridSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def FindCellAtXY(self, x, y):
        """ FindCellAtXY(self: GridSurface, x: float, y: float) -> GridSurfaceCell """
        pass

    def FindEdgeAtXY(self, x, y):
        """ FindEdgeAtXY(self: GridSurface, x: float, y: float) -> GridSurfaceEdge """
        pass

    def FindVertexAtXY(self, x, y):
        """ FindVertexAtXY(self: GridSurface, x: float, y: float) -> GridSurfaceVertex """
        pass

    def GetCells(self, includeInvisible):
        """ GetCells(self: GridSurface, includeInvisible: bool) -> GridSurfaceCellCollection """
        pass

    def GetGridProperties(self):
        """ GetGridProperties(self: GridSurface) -> GridSurfaceProperties """
        pass

    def GetTerrainProperties(self):
        """ GetTerrainProperties(self: GridSurface) -> TerrainSurfaceProperties """
        pass

    def GetVertices(self, includeInvisible):
        """ GetVertices(self: GridSurface, includeInvisible: bool) -> GridSurfaceVertexCollection """
        pass

    def RaisePoints(self, locations, deltaElevation):
        """ RaisePoints(self: GridSurface, locations: IEnumerable[GridLocation], deltaElevation: float) -> SurfaceOperationModifyMultipleGridPointsElevation """
        pass

    def RaiseSurface(self, deltaElevation):
        """ RaiseSurface(self: GridSurface, deltaElevation: float) -> SurfaceOperationRaise """
        pass

    def SampleElevations(self, *__args):
        """
        SampleElevations(self: GridSurface, curveId: ObjectId) -> Point3dCollection
        SampleElevations(self: GridSurface, pt1: Point3d, pt2: Point3d) -> Point3dCollection
        """
        pass

    def SetPointElevation(self, location, newElevation):
        """ SetPointElevation(self: GridSurface, location: GridLocation, newElevation: float) -> SurfaceOperationModifyGridPointElevation """
        pass

    def SetPointsElevation(self, locations, newElevation):
        """ SetPointsElevation(self: GridSurface, locations: IEnumerable[GridLocation], newElevation: float) -> SurfaceOperationModifyMultipleGridPointsElevation """
        pass

    Cells = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cells(self: GridSurface) -> GridSurfaceCellCollection

"""

    DEMFilesDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DEMFilesDefinition(self: GridSurface) -> SurfaceDefinitionDEMFiles

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: GridSurface) -> GridSurfaceVertexCollection

"""



class GridSurfaceObject(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: GridSurfaceObject) """
        pass

    def getAeccSurfaceGrid(self, *args): #cannot find CLR method
        """ getAeccSurfaceGrid(self: GridSurfaceObject) -> AeccSurfaceGrid* """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GridSurfaceObject) -> bool

"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: GridSurfaceObject) -> GridSurface

"""


    m_pSurfaceAPIObject = None


class GridSurfaceCell(GridSurfaceObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: GridSurfaceObject, A_0: bool) """
        pass

    def Equals(self, rhs):
        """ Equals(self: GridSurfaceCell, rhs: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GridSurfaceCell) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    BottomEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomEdge(self: GridSurfaceCell) -> GridSurfaceEdge

"""

    BottomLeftVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomLeftVertex(self: GridSurfaceCell) -> GridSurfaceVertex

"""

    BottomRightVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomRightVertex(self: GridSurfaceCell) -> GridSurfaceVertex

"""

    GridLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridLocation(self: GridSurfaceCell) -> GridLocation

"""

    LeftEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftEdge(self: GridSurfaceCell) -> GridSurfaceEdge

"""

    RightEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightEdge(self: GridSurfaceCell) -> GridSurfaceEdge

"""

    TopEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopEdge(self: GridSurfaceCell) -> GridSurfaceEdge

"""

    TopLeftVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopLeftVertex(self: GridSurfaceCell) -> GridSurfaceVertex

"""

    TopRightVertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopRightVertex(self: GridSurfaceCell) -> GridSurfaceVertex

"""


    m_pSurfaceAPIObject = None


class GridSurfaceCellCollection(object):
    # no doc
    def Contains(self, location):
        """ Contains(self: GridSurfaceCellCollection, location: GridLocation) -> bool """
        pass

    def GetAt(self, location):
        """ GetAt(self: GridSurfaceCellCollection, location: GridLocation) -> GridSurfaceCell """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: GridSurfaceCellCollection) -> IEnumerator[GridSurfaceCell] """
        pass

    def GetIndexRange(self, minColIndex, minRowIndex, maxColIndex, maxRowIndex):
        """ GetIndexRange(self: GridSurfaceCellCollection, minColIndex: int, minRowIndex: int, maxColIndex: int, maxRowIndex: int) -> (int, int, int, int) """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: GridSurfaceCellCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GridSurfaceCell](enumerable: IEnumerable[GridSurfaceCell], value: GridSurfaceCell) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GridSurfaceCellCollection) -> int

"""



class GridSurfaceCellEnumerator(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: GridSurfaceCellEnumerator) """
        pass

    def MoveNext(self):
        """ MoveNext(self: GridSurfaceCellEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: GridSurfaceCellEnumerator) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GridSurfaceCell](enumerator: IEnumerator[GridSurfaceCell], value: GridSurfaceCell) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: GridSurfaceCellEnumerator) -> GridSurfaceCell

"""

    CurrentObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentObject(self: GridSurfaceCellEnumerator) -> object

"""



class GridSurfaceEdge(GridSurfaceObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: GridSurfaceEdge, A_0: bool) """
        pass

    def Equals(self, rhs):
        """ Equals(self: GridSurfaceEdge, rhs: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GridSurfaceEdge) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Cell1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cell1(self: GridSurfaceEdge) -> GridSurfaceCell

"""

    Cell2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cell2(self: GridSurfaceEdge) -> GridSurfaceCell

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GridSurfaceEdge) -> bool

"""

    Vertex1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex1(self: GridSurfaceEdge) -> GridSurfaceVertex

"""

    Vertex2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex2(self: GridSurfaceEdge) -> GridSurfaceVertex

"""


    m_pSurfaceAPIObject = None


class GridSurfaceProperties(object):
    # no doc
    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Orientation(self: GridSurfaceProperties) -> float

"""

    SpacingX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpacingX(self: GridSurfaceProperties) -> float

"""

    SpacingY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpacingY(self: GridSurfaceProperties) -> float

"""



class GridSurfaceVertex(GridSurfaceObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: GridSurfaceObject, A_0: bool) """
        pass

    def Equals(self, rhs):
        """ Equals(self: GridSurfaceVertex, rhs: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: GridSurfaceVertex) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    GridLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridLocation(self: GridSurfaceVertex) -> GridLocation

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: GridSurfaceVertex) -> Point3d

"""


    m_pSurfaceAPIObject = None


class GridSurfaceVertexCollection(object):
    # no doc
    def Contains(self, location):
        """ Contains(self: GridSurfaceVertexCollection, location: GridLocation) -> bool """
        pass

    def GetAt(self, location):
        """ GetAt(self: GridSurfaceVertexCollection, location: GridLocation) -> GridSurfaceVertex """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: GridSurfaceVertexCollection) -> IEnumerator[GridSurfaceVertex] """
        pass

    def GetIndexRange(self, minColIndex, minRowIndex, maxColIndex, maxRowIndex):
        """ GetIndexRange(self: GridSurfaceVertexCollection, minColIndex: int, minRowIndex: int, maxColIndex: int, maxRowIndex: int) -> (int, int, int, int) """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: GridSurfaceVertexCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GridSurfaceVertex](enumerable: IEnumerable[GridSurfaceVertex], value: GridSurfaceVertex) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GridSurfaceVertexCollection) -> int

"""



class GridSurfaceVertexEnumerator(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: GridSurfaceVertexEnumerator) """
        pass

    def MoveNext(self):
        """ MoveNext(self: GridSurfaceVertexEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: GridSurfaceVertexEnumerator) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[GridSurfaceVertex](enumerator: IEnumerator[GridSurfaceVertex], value: GridSurfaceVertex) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: GridSurfaceVertexEnumerator) -> GridSurfaceVertex

"""

    CurrentObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentObject(self: GridSurfaceVertexEnumerator) -> object

"""



class GridVolumeSurface(Surface):
    # no doc
    @staticmethod
    def Create(surfaceName, baseSurfaceId, comparisonSurfaceId, spacingX, spacingY, orientation, styleId=None):
        """
        Create(surfaceName: str, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, spacingX: float, spacingY: float, orientation: float) -> ObjectId
        Create(surfaceName: str, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, spacingX: float, spacingY: float, orientation: float, styleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetGridProperties(self):
        """ GetGridProperties(self: GridVolumeSurface) -> GridSurfaceProperties """
        pass

    def GetVolumeProperties(self):
        """ GetVolumeProperties(self: GridVolumeSurface) -> VolumeSurfaceProperties """
        pass

    CutFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutFactor(self: GridVolumeSurface) -> float

Set: CutFactor(self: GridVolumeSurface) = value
"""

    FillFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillFactor(self: GridVolumeSurface) -> float

Set: FillFactor(self: GridVolumeSurface) = value
"""



class HardcodedOffsetBaseline(BaseBaseline):
    # no doc
    def Dispose(self):
        """ Dispose(self: HardcodedOffsetBaseline, A_0: bool) """
        pass

    def IsFeatureLineBased(self):
        """ IsFeatureLineBased(self: HardcodedOffsetBaseline) -> bool """
        pass

    def SortedStations(self):
        """ SortedStations(self: HardcodedOffsetBaseline) -> Array[float] """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: HardcodedOffsetBaseline) -> ObjectId

"""

    BaselineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineType(self: HardcodedOffsetBaseline) -> CorridorBaselineType

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: HardcodedOffsetBaseline) -> str

"""

    OffsetElevationFromMainBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetElevationFromMainBaseline(self: HardcodedOffsetBaseline) -> Point2d

"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: HardcodedOffsetBaseline) -> ObjectId

"""

    RelatedOffsetBaselineFeatureLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelatedOffsetBaselineFeatureLines(self: HardcodedOffsetBaseline) -> BaselineFeatureLines

"""



class HatchCriteriaBoundaryType(Enum):
    """ enum HatchCriteriaBoundaryType, values: Lower (1), Upper (0) """
    Lower = None
    Upper = None
    value__ = None


class HoldOnResizeType(Enum):
    """ enum HoldOnResizeType, values: Centerline (2), Crown (1), Invert (0) """
    Centerline = None
    Crown = None
    Invert = None
    value__ = None


class ProfileBandLabelGroup(AutoFeatureLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(runtimeClass, profileViewId, includeDerived):
        """ GetAvailableLabelGroupIds(runtimeClass: RXClass, profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(runtimeClass, profileViewId, includeDerived):
        """ GetAvailableLabelGroups(runtimeClass: RXClass, profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: ProfileBandLabelGroup) -> ObjectId

Set: StyleId(self: ProfileBandLabelGroup) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: ProfileBandLabelGroup) -> str

Set: StyleName(self: ProfileBandLabelGroup) = value
"""


    m_SubData = None


class HorizontalGeometryBandLabelGroup(ProfileBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class IAppliedSubassemblyParam:
    # no doc
    def ClearOverride(self):
        """ ClearOverride(self: IAppliedSubassemblyParam) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Comment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Comment(self: IAppliedSubassemblyParam) -> str

Set: Comment(self: IAppliedSubassemblyParam) = value
"""

    DesignValueAsObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignValueAsObject(self: IAppliedSubassemblyParam) -> object

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: IAppliedSubassemblyParam) -> str

"""

    IsOverriden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverriden(self: IAppliedSubassemblyParam) -> bool

"""

    KeyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyName(self: IAppliedSubassemblyParam) -> str

"""

    ValueAsObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueAsObject(self: IAppliedSubassemblyParam) -> object

"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueType(self: IAppliedSubassemblyParam) -> Type

"""



class ICommonLabel:
    # no doc
    def ClearAllTextComponentOverrides(self):
        """ ClearAllTextComponentOverrides(self: ICommonLabel) """
        pass

    def GetReferenceTextTarget(self, referenceTextComponentId):
        """ GetReferenceTextTarget(self: ICommonLabel, referenceTextComponentId: ObjectId) -> ObjectId """
        pass

    def GetTextComponentIds(self):
        """ GetTextComponentIds(self: ICommonLabel) -> ObjectIdCollection """
        pass

    def GetTextComponentJustificationOverride(self, labelStyleComponentId):
        """ GetTextComponentJustificationOverride(self: ICommonLabel, labelStyleComponentId: ObjectId) -> TextJustificationType """
        pass

    def GetTextComponentOverride(self, labelStyleComponentId):
        """ GetTextComponentOverride(self: ICommonLabel, labelStyleComponentId: ObjectId) -> str """
        pass

    def IsTextComponentOverriden(self, labelStyleComponentId):
        """ IsTextComponentOverriden(self: ICommonLabel, labelStyleComponentId: ObjectId) -> bool """
        pass

    def Reset(self):
        """ Reset(self: ICommonLabel) """
        pass

    def ResetLocation(self):
        """ ResetLocation(self: ICommonLabel) """
        pass

    def ResetProperties(self):
        """ ResetProperties(self: ICommonLabel) """
        pass

    def SetReferenceTextTarget(self, referenceTextComponentId, referenceObjectId):
        """ SetReferenceTextTarget(self: ICommonLabel, referenceTextComponentId: ObjectId, referenceObjectId: ObjectId) """
        pass

    def SetTextComponentJustificationOverride(self, labelStyleComponentId, textJustificationType):
        """ SetTextComponentJustificationOverride(self: ICommonLabel, labelStyleComponentId: ObjectId, textJustificationType: TextJustificationType) """
        pass

    def SetTextComponentOverride(self, labelStyleComponentId, textOverride, textJustificationType=None):
        """ SetTextComponentOverride(self: ICommonLabel, labelStyleComponentId: ObjectId, textOverride: str)SetTextComponentOverride(self: ICommonLabel, labelStyleComponentId: ObjectId, textOverride: str, textJustificationType: TextJustificationType) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AnchorInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorInfo(self: ICommonLabel) -> AnchorInfo

"""

    AnchorMarkerRotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorMarkerRotationAngle(self: ICommonLabel) -> float

Set: AnchorMarkerRotationAngle(self: ICommonLabel) = value
"""

    AnchorMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorMarkerStyleId(self: ICommonLabel) -> ObjectId

Set: AnchorMarkerStyleId(self: ICommonLabel) = value
"""

    CanRotate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRotate(self: ICommonLabel) -> bool

"""

    DimensionAnchorInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorInfo(self: ICommonLabel) -> AnchorInfo

"""

    DimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorOption(self: ICommonLabel) -> DimensionAnchorOptionType

Set: DimensionAnchorOption(self: ICommonLabel) = value
"""

    DimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorValue(self: ICommonLabel) -> float

Set: DimensionAnchorValue(self: ICommonLabel) = value
"""

    Dragged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dragged(self: ICommonLabel) -> bool

"""

    DraggedOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DraggedOffset(self: ICommonLabel) -> Vector3d

Set: DraggedOffset(self: ICommonLabel) = value
"""

    Flipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flipped(self: ICommonLabel) -> bool

Set: Flipped(self: ICommonLabel) = value
"""

    LeaderAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderAttachment(self: ICommonLabel) -> LeaderAttachmentBehaviorType

Set: LeaderAttachment(self: ICommonLabel) = value
"""

    LeaderTailVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderTailVisibility(self: ICommonLabel) -> LeaderTailVisibilityType

Set: LeaderTailVisibility(self: ICommonLabel) = value
"""

    LeaderVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderVisibility(self: ICommonLabel) -> LeaderVisibilityType

Set: LeaderVisibility(self: ICommonLabel) = value
"""

    Pinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pinned(self: ICommonLabel) -> bool

Set: Pinned(self: ICommonLabel) = value
"""

    Reversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reversed(self: ICommonLabel) -> bool

Set: Reversed(self: ICommonLabel) = value
"""

    RotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationAngle(self: ICommonLabel) -> float

Set: RotationAngle(self: ICommonLabel) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: ICommonLabel) -> ObjectId

Set: StyleId(self: ICommonLabel) = value
"""



class ICommonLabelOptions:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AllowsAnchorMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsAnchorMarker(self: ICommonLabelOptions) -> bool

"""

    AllowsDimensionAnchors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsDimensionAnchors(self: ICommonLabelOptions) -> bool

"""

    AllowsDragging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsDragging(self: ICommonLabelOptions) -> bool

"""

    AllowsFlipping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsFlipping(self: ICommonLabelOptions) -> bool

"""

    AllowsLeaderAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsLeaderAttachment(self: ICommonLabelOptions) -> bool

"""

    AllowsPinning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsPinning(self: ICommonLabelOptions) -> bool

"""

    AllowsReversing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsReversing(self: ICommonLabelOptions) -> bool

"""

    DefaultDimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorOption(self: ICommonLabelOptions) -> DimensionAnchorOptionType

Set: DefaultDimensionAnchorOption(self: ICommonLabelOptions) = value
"""

    DefaultDimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorValue(self: ICommonLabelOptions) -> float

Set: DefaultDimensionAnchorValue(self: ICommonLabelOptions) = value
"""

    RotationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationType(self: ICommonLabelOptions) -> LabelRotationType

"""



class IGridSurface:
    # no doc
    def GetGridProperties(self):
        """ GetGridProperties(self: IGridSurface) -> GridSurfaceProperties """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class Interference(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    Network1Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Network1Id(self: Interference) -> ObjectId

"""

    Network2Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Network2Id(self: Interference) -> ObjectId

"""



class InterferenceCheck(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class Intersection(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetIntersectionLocaitonLabelIds(self):
        """ GetIntersectionLocaitonLabelIds(self: Intersection) -> ObjectIdCollection """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: Intersection) -> ObjectId

"""

    GradeRuleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeRuleType(self: Intersection) -> IntersectionCorridorType

"""

    IntersectionRegions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionRegions(self: Intersection) -> IntersectionRegionCollection

"""

    IntersectionRoads = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionRoads(self: Intersection) -> IntersectionRoadCollection

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Intersection) -> Point3d

"""

    RoadwayDrivingDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RoadwayDrivingDirection(self: Intersection) -> DrivingDirectionType

Set: RoadwayDrivingDirection(self: Intersection) = value
"""



class IntersectionCorridorType(Enum):
    """ enum IntersectionCorridorType, values: AllCrownsMaintained (2), PrimaryRoadCrownMaintained (1) """
    AllCrownsMaintained = None
    PrimaryRoadCrownMaintained = None
    value__ = None


class IntersectionLocationLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(intersectionId, labelStyleId=None):
        """
        Create(intersectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId
        Create(intersectionId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(intersectionId):
        """ GetAvailableLabelIds(intersectionId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class IntersectionRegion(CivilWrapper<AeccDbIntersection>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbIntersection>, A_0: bool) """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: IntersectionRegion) -> float

"""

    CurbReturnAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurbReturnAlignmentId(self: IntersectionRegion) -> ObjectId

"""

    CurbReturnProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurbReturnProfileId(self: IntersectionRegion) -> ObjectId

"""

    InAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InAlignmentId(self: IntersectionRegion) -> ObjectId

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IntersectionRegion) -> str

Set: Name(self: IntersectionRegion) = value
"""

    OutAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutAlignmentId(self: IntersectionRegion) -> ObjectId

"""



class IntersectionRegionCollection(CivilWrapper<AeccDbIntersection>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbIntersection>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IntersectionRegionCollection) -> IEnumerator[IntersectionRegion] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: IntersectionRegionCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IntersectionRegion](enumerable: IEnumerable[IntersectionRegion], value: IntersectionRegion) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IntersectionRegionCollection) -> int

"""



class IntersectionRoad(CivilWrapper<AeccDbIntersection>):
    # no doc
    def Dispose(self):
        """ Dispose(self: IntersectionRoad, A_0: bool) """
        pass

    CenterlineAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineAlignmentId(self: IntersectionRoad) -> ObjectId

"""

    CenterlineProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineProfileId(self: IntersectionRoad) -> ObjectId

"""

    OffsetLeftAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetLeftAlignmentId(self: IntersectionRoad) -> ObjectId

"""

    OffsetLeftProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetLeftProfileId(self: IntersectionRoad) -> ObjectId

"""

    OffsetRightAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetRightAlignmentId(self: IntersectionRoad) -> ObjectId

"""

    OffsetRightProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetRightProfileId(self: IntersectionRoad) -> ObjectId

"""



class IntersectionRoadCollection(CivilWrapper<AeccDbIntersection>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbIntersection>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IntersectionRoadCollection) -> IEnumerator[IntersectionRoad] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: IntersectionRoadCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[IntersectionRoad](enumerable: IEnumerable[IntersectionRoad], value: IntersectionRoad) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IntersectionRoadCollection) -> int

"""



class IPoint:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Codes(self: IPoint) -> CodeCollection

"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: IPoint) -> float

Set: Elevation(self: IPoint) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: IPoint) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: IPoint) -> float

Set: Offset(self: IPoint) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: IPoint) -> float

Set: Station(self: IPoint) = value
"""



class ITerrainSurface:
    # no doc
    def ExtractBorder(self, settingsType):
        """ ExtractBorder(self: ITerrainSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def ExtractContours(self, *__args):
        """
        ExtractContours(self: ITerrainSurface, lowElev: float, highElev: float, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        ExtractContours(self: ITerrainSurface, lowElev: float, highElev: float, interval: float) -> ObjectIdCollection
        ExtractContours(self: ITerrainSurface, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        ExtractContours(self: ITerrainSurface, interval: float) -> ObjectIdCollection
        """
        pass

    def ExtractContoursAt(self, elevation, smoothType=None, smoothFactor=None):
        """
        ExtractContoursAt(self: ITerrainSurface, elevation: float) -> ObjectIdCollection
        ExtractContoursAt(self: ITerrainSurface, elevation: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractGridded(self, settingsType):
        """ ExtractGridded(self: ITerrainSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def ExtractMajorContours(self, settingsType, smoothType=None, smoothFactor=None):
        """
        ExtractMajorContours(self: ITerrainSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        ExtractMajorContours(self: ITerrainSurface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractMinorContours(self, settingsType, smoothType=None, smoothFactor=None):
        """
        ExtractMinorContours(self: ITerrainSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        ExtractMinorContours(self: ITerrainSurface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractWatershed(self, settingsType):
        """ ExtractWatershed(self: ITerrainSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def GetTerrainProperties(self):
        """ GetTerrainProperties(self: ITerrainSurface) -> TerrainSurfaceProperties """
        pass

    def RaiseSurface(self, deltaElevation):
        """ RaiseSurface(self: ITerrainSurface, deltaElevation: float) -> SurfaceOperationRaise """
        pass

    def SampleElevations(self, curveId):
        """ SampleElevations(self: ITerrainSurface, curveId: ObjectId) -> Point3dCollection """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    DEMFilesDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DEMFilesDefinition(self: ITerrainSurface) -> SurfaceDefinitionDEMFiles

"""



class ITinSurface:
    # no doc
    def GetTinProperties(self):
        """ GetTinProperties(self: ITinSurface) -> TinSurfaceProperties """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IVolumeSurface:
    # no doc
    def GetVolumeProperties(self):
        """ GetVolumeProperties(self: IVolumeSurface) -> VolumeSurfaceProperties """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CutFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutFactor(self: IVolumeSurface) -> float

Set: CutFactor(self: IVolumeSurface) = value
"""

    FillFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillFactor(self: IVolumeSurface) -> float

Set: FillFactor(self: IVolumeSurface) = value
"""



class KrigingMethodOptions(object):
    """ KrigingMethodOptions() """
    NuggetEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NuggetEffect(self: KrigingMethodOptions) -> float

Set: NuggetEffect(self: KrigingMethodOptions) = value
"""

    SampleVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleVertices(self: KrigingMethodOptions) -> IEnumerable[TinSurfaceVertex]

Set: SampleVertices(self: KrigingMethodOptions) = value
"""

    SemivariogramModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SemivariogramModel(self: KrigingMethodOptions) -> KrigingSemivariogramType

Set: SemivariogramModel(self: KrigingMethodOptions) = value
"""

    VariogramParamA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VariogramParamA(self: KrigingMethodOptions) -> float

Set: VariogramParamA(self: KrigingMethodOptions) = value
"""

    VariogramParamC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VariogramParamC(self: KrigingMethodOptions) -> float

Set: VariogramParamC(self: KrigingMethodOptions) = value
"""



class LabelGroupSubEntity(object):
    # no doc
    def ClearAllTextComponentOverrides(self):
        """ ClearAllTextComponentOverrides(self: LabelGroupSubEntity) """
        pass

    def GetReferenceTextTarget(self, referenceTextComponentId):
        """ GetReferenceTextTarget(self: LabelGroupSubEntity, referenceTextComponentId: ObjectId) -> ObjectId """
        pass

    def GetTextComponentIds(self):
        """ GetTextComponentIds(self: LabelGroupSubEntity) -> ObjectIdCollection """
        pass

    def GetTextComponentJustificationOverride(self, labelStyleComponentId):
        """ GetTextComponentJustificationOverride(self: LabelGroupSubEntity, labelStyleComponentId: ObjectId) -> TextJustificationType """
        pass

    def GetTextComponentOverride(self, labelStyleComponentId):
        """ GetTextComponentOverride(self: LabelGroupSubEntity, labelStyleComponentId: ObjectId) -> str """
        pass

    def IsTextComponentOverriden(self, newVal):
        """ IsTextComponentOverriden(self: LabelGroupSubEntity, newVal: ObjectId) -> bool """
        pass

    def Reset(self):
        """ Reset(self: LabelGroupSubEntity) """
        pass

    def ResetLocation(self):
        """ ResetLocation(self: LabelGroupSubEntity) """
        pass

    def ResetProperties(self):
        """ ResetProperties(self: LabelGroupSubEntity) """
        pass

    def SetReferenceTextTarget(self, referenceTextComponentId, referenceObjectId):
        """ SetReferenceTextTarget(self: LabelGroupSubEntity, referenceTextComponentId: ObjectId, referenceObjectId: ObjectId) """
        pass

    def SetTextComponentJustificationOverride(self, labelStyleComponentId, textJustificationType):
        """ SetTextComponentJustificationOverride(self: LabelGroupSubEntity, labelStyleComponentId: ObjectId, textJustificationType: TextJustificationType) """
        pass

    def SetTextComponentOverride(self, labelStyleComponentId, textOverride, textJustificationType=None):
        """ SetTextComponentOverride(self: LabelGroupSubEntity, labelStyleComponentId: ObjectId, textOverride: str)SetTextComponentOverride(self: LabelGroupSubEntity, labelStyleComponentId: ObjectId, textOverride: str, textJustificationType: TextJustificationType) """
        pass

    AllowsAnchorMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsAnchorMarker(self: LabelGroupSubEntity) -> bool

"""

    AllowsDimensionAnchors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsDimensionAnchors(self: LabelGroupSubEntity) -> bool

"""

    AllowsDragging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsDragging(self: LabelGroupSubEntity) -> bool

"""

    AllowsFlipping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsFlipping(self: LabelGroupSubEntity) -> bool

"""

    AllowsLeaderAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsLeaderAttachment(self: LabelGroupSubEntity) -> bool

"""

    AllowsPinning = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsPinning(self: LabelGroupSubEntity) -> bool

"""

    AllowsReversing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowsReversing(self: LabelGroupSubEntity) -> bool

"""

    AnchorInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorInfo(self: LabelGroupSubEntity) -> AnchorInfo

"""

    AnchorMarkerRotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorMarkerRotationAngle(self: LabelGroupSubEntity) -> float

Set: AnchorMarkerRotationAngle(self: LabelGroupSubEntity) = value
"""

    AnchorMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorMarkerStyleId(self: LabelGroupSubEntity) -> ObjectId

Set: AnchorMarkerStyleId(self: LabelGroupSubEntity) = value
"""

    CanRotate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanRotate(self: LabelGroupSubEntity) -> bool

"""

    DefaultDimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorOption(self: LabelGroupSubEntity) -> DimensionAnchorOptionType

Set: DefaultDimensionAnchorOption(self: LabelGroupSubEntity) = value
"""

    DefaultDimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDimensionAnchorValue(self: LabelGroupSubEntity) -> float

Set: DefaultDimensionAnchorValue(self: LabelGroupSubEntity) = value
"""

    DimensionAnchorInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorInfo(self: LabelGroupSubEntity) -> AnchorInfo

"""

    DimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorOption(self: LabelGroupSubEntity) -> DimensionAnchorOptionType

Set: DimensionAnchorOption(self: LabelGroupSubEntity) = value
"""

    DimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorValue(self: LabelGroupSubEntity) -> float

Set: DimensionAnchorValue(self: LabelGroupSubEntity) = value
"""

    Dragged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dragged(self: LabelGroupSubEntity) -> bool

"""

    DraggedOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DraggedOffset(self: LabelGroupSubEntity) -> Vector3d

Set: DraggedOffset(self: LabelGroupSubEntity) = value
"""

    Flipped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flipped(self: LabelGroupSubEntity) -> bool

Set: Flipped(self: LabelGroupSubEntity) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: LabelGroupSubEntity) -> UInt32

"""

    LabelLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelLocation(self: LabelGroupSubEntity) -> Point3d

Set: LabelLocation(self: LabelGroupSubEntity) = value
"""

    LeaderAttachment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderAttachment(self: LabelGroupSubEntity) -> LeaderAttachmentBehaviorType

Set: LeaderAttachment(self: LabelGroupSubEntity) = value
"""

    LeaderTailVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderTailVisibility(self: LabelGroupSubEntity) -> LeaderTailVisibilityType

Set: LeaderTailVisibility(self: LabelGroupSubEntity) = value
"""

    LeaderVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderVisibility(self: LabelGroupSubEntity) -> LeaderVisibilityType

Set: LeaderVisibility(self: LabelGroupSubEntity) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: LabelGroupSubEntity) -> LabelGroup

"""

    Pinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pinned(self: LabelGroupSubEntity) -> bool

Set: Pinned(self: LabelGroupSubEntity) = value
"""

    Reversed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Reversed(self: LabelGroupSubEntity) -> bool

Set: Reversed(self: LabelGroupSubEntity) = value
"""

    RotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationAngle(self: LabelGroupSubEntity) -> float

Set: RotationAngle(self: LabelGroupSubEntity) = value
"""

    RotationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationType(self: LabelGroupSubEntity) -> LabelRotationType

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: LabelGroupSubEntity) -> ObjectId

Set: StyleId(self: LabelGroupSubEntity) = value
"""

    Visibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visibility(self: LabelGroupSubEntity) -> bool

Set: Visibility(self: LabelGroupSubEntity) = value
"""



class LabelSelectionProperties(object):
    """ LabelSelectionProperties(objIds: ObjectIdCollection) """
    def Dispose(self):
        """ Dispose(self: LabelSelectionProperties) """
        pass

    @staticmethod
    def Instance(objIds):
        """ Instance(objIds: ObjectIdCollection) -> LabelSelectionProperties """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, objIds):
        """ __new__(cls: type, objIds: ObjectIdCollection) """
        pass

    ClearLabelText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClearLabelText(self: LabelSelectionProperties) -> bool

"""

    ClearMultiLabelText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClearMultiLabelText(self: LabelSelectionProperties) -> bool

"""

    EditLabelText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditLabelText(self: LabelSelectionProperties) -> bool

"""

    FlipLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlipLabel(self: LabelSelectionProperties) -> bool

"""

    Leader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Leader(self: LabelSelectionProperties) -> bool

"""

    LeaderTail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeaderTail(self: LabelSelectionProperties) -> bool

"""

    ResetLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResetLabel(self: LabelSelectionProperties) -> bool

"""

    ReverseLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseLabel(self: LabelSelectionProperties) -> bool

"""

    TagLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagLabel(self: LabelSelectionProperties) -> bool

"""

    ToggleLabelPin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToggleLabelPin(self: LabelSelectionProperties) -> bool

"""



class LabelType(Enum):
    """ enum LabelType, values: AlignmentCANTCriticalPoints (13), AlignmentCurve (16), AlignmentDesignSpeed (11), AlignmentGeometryPoint (8), AlignmentMajorStation (6), AlignmentMinorStation (7), AlignmentPointOfIntersection (19), AlignmentProfileGeometryPoint (9), AlignmentSpiral (17), AlignmentStationEquation (10), AlignmentStationOffset (14), AlignmentSuperelevationCriticalPoints (12), AlignmentTangent (15), AlignmentTangentIntersection (18), General (2), HorizontalGeometryBand (32), MatchLine (52), Note (1), ParcelFace (4), ParcelSegment (5), Pipe (45), PipeNetworkBand (34), PipeProfile (46), PipeSection (47), ProfileCrestCurve (25), ProfileDataBand (30), ProfileGradeBreaks (23), ProfileHorizontalGeometryPoint (22), ProfileLine (24), ProfileMajorStation (20), ProfileMinorStation (21), ProfileProjection (29), ProfileSagCurve (26), ProfileStationElevation (27), ProfileViewDepth (28), SampleLine (44), SectionalDataBand (35), SectionCorridorPoint (53), SectionDataBand (43), SectionGradeBreak (41), SectionMajorOffset (39), SectionMinorOffset (40), SectionProjection (38), SectionSegment (42), SectionViewDepth (37), SectionViewOffsetElevation (36), StructureLabel (48), StructureProfile (49), StructureSection (50), SuperElevationBand (33), SurfaceContour (3), Unknown (0), VerticalGeometryBand (31), ViewFrame (51) """
    AlignmentCANTCriticalPoints = None
    AlignmentCurve = None
    AlignmentDesignSpeed = None
    AlignmentGeometryPoint = None
    AlignmentMajorStation = None
    AlignmentMinorStation = None
    AlignmentPointOfIntersection = None
    AlignmentProfileGeometryPoint = None
    AlignmentSpiral = None
    AlignmentStationEquation = None
    AlignmentStationOffset = None
    AlignmentSuperelevationCriticalPoints = None
    AlignmentTangent = None
    AlignmentTangentIntersection = None
    General = None
    HorizontalGeometryBand = None
    MatchLine = None
    Note = None
    ParcelFace = None
    ParcelSegment = None
    Pipe = None
    PipeNetworkBand = None
    PipeProfile = None
    PipeSection = None
    ProfileCrestCurve = None
    ProfileDataBand = None
    ProfileGradeBreaks = None
    ProfileHorizontalGeometryPoint = None
    ProfileLine = None
    ProfileMajorStation = None
    ProfileMinorStation = None
    ProfileProjection = None
    ProfileSagCurve = None
    ProfileStationElevation = None
    ProfileViewDepth = None
    SampleLine = None
    SectionalDataBand = None
    SectionCorridorPoint = None
    SectionDataBand = None
    SectionGradeBreak = None
    SectionMajorOffset = None
    SectionMinorOffset = None
    SectionProjection = None
    SectionSegment = None
    SectionViewDepth = None
    SectionViewOffsetElevation = None
    StructureLabel = None
    StructureProfile = None
    StructureSection = None
    SuperElevationBand = None
    SurfaceContour = None
    Unknown = None
    value__ = None
    VerticalGeometryBand = None
    ViewFrame = None


class LegendTable(Table):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class LinearTransitionDescription(TransitionDescriptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: TransitionDescriptionBase, A_0: bool) """
        pass

    TaperInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaperInput(self: LinearTransitionDescription) -> TaperInputType

Set: TaperInput(self: LinearTransitionDescription) = value
"""

    TaperRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TaperRatio(self: LinearTransitionDescription) -> float

Set: TaperRatio(self: LinearTransitionDescription) = value
"""


    m_pTransitionParam = None


class Link(CivilWrapper<AeccDbEntity>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbEntity>, A_0: bool) """
        pass

    Codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Codes(self: Link) -> CodeCollection

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: Link) -> int

"""

    IsHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHidden(self: Link) -> bool

Set: IsHidden(self: Link) = value
"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Link) -> PointCollection

"""



class LinkCollection(CivilWrapper<AeccDbEntity>):
    # no doc
    def Add(self, *__args):
        """
        Add(self: LinkCollection, point1: IPoint, point2: IPoint, code: str, displayMode: CorridorLinkDisplay) -> Link
        Add(self: LinkCollection, point1: IPoint, point2: IPoint, code: str) -> Link
        Add(self: LinkCollection, points: Array[IPoint], code: str, displayMode: CorridorLinkDisplay) -> Link
        Add(self: LinkCollection, points: Array[IPoint], code: str) -> Link
        Add(self: LinkCollection, point1: IPoint, point2: IPoint, codes: Array[str], displayMode: CorridorLinkDisplay) -> Link
        Add(self: LinkCollection, point1: IPoint, point2: IPoint, codes: Array[str]) -> Link
        Add(self: LinkCollection, points: Array[IPoint], codes: Array[str], displayMode: CorridorLinkDisplay) -> Link
        Add(self: LinkCollection, points: Array[IPoint], codes: Array[str]) -> Link
        """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbEntity>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LinkCollection) -> IEnumerator[Link] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: LinkCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """ Remove(self: LinkCollection, index: int)Remove(self: LinkCollection, link: Link) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Link](enumerable: IEnumerable[Link], value: Link) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: LinkCollection) -> int

"""



class MassHaulLine(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class MassHaulView(Graph):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    MassHaulLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MassHaulLineId(self: MassHaulView) -> ObjectId

"""



class MatchLine(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: MatchLine) -> ObjectId

"""

    GroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupId(self: MatchLine) -> ObjectId

"""

    IsLeftLabelVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLeftLabelVisible(self: MatchLine) -> bool

Set: IsLeftLabelVisible(self: MatchLine) = value
"""

    IsRightLabelVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRightLabelVisible(self: MatchLine) -> bool

Set: IsRightLabelVisible(self: MatchLine) = value
"""

    LeftLabelAnchorPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftLabelAnchorPosition(self: MatchLine) -> MatchLineLabelLocationType

Set: LeftLabelAnchorPosition(self: MatchLine) = value
"""

    LeftLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftLabelStyleId(self: MatchLine) -> ObjectId

Set: LeftLabelStyleId(self: MatchLine) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: MatchLine) -> int

"""

    RightLabelAnchorPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightLabelAnchorPosition(self: MatchLine) -> MatchLineLabelLocationType

Set: RightLabelAnchorPosition(self: MatchLine) = value
"""

    RightLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightLabelStyleId(self: MatchLine) -> ObjectId

Set: RightLabelStyleId(self: MatchLine) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: MatchLine) -> float

"""



class MatchLineLabelGroup(AutoFeatureLabelGroup):
    # no doc
    @staticmethod
    def Create(viewFrameGroupId, side, labelStyleId=None, anchorPosition=None):
        """
        Create(viewFrameGroupId: ObjectId, side: EntitySideType, labelStyleId: ObjectId, anchorPosition: MatchLineLabelLocationType) -> ObjectId
        Create(viewFrameGroupId: ObjectId, side: EntitySideType) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(viewFrameGroupId):
        """ GetAvailableLabelGroupIds(viewFrameGroupId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetLabelGroupIdBySide(viewFrameGroupId, side):
        """ GetLabelGroupIdBySide(viewFrameGroupId: ObjectId, side: EntitySideType) -> ObjectId """
        pass

    Side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Side(self: MatchLineLabelGroup) -> EntitySideType

"""


    m_SubData = None


class MaterialConditionType(Enum):
    """ enum MaterialConditionType, values: Above (0), Base (2), Below (1), Compare (3), Exclude (5), Include (4) """
    Above = None
    Base = None
    Below = None
    Compare = None
    Exclude = None
    Include = None
    value__ = None


class MaterialFactorType(Enum):
    """ enum MaterialFactorType, values: Cut (0), Fill (1), Refill (2) """
    Cut = None
    Fill = None
    Refill = None
    value__ = None


class MaterialItemType(Enum):
    """ enum MaterialItemType, values: CorridorShape (1), Surface (0) """
    CorridorShape = None
    Surface = None
    value__ = None


class MaterialQuantityType(Enum):
    """ enum MaterialQuantityType, values: Cut (0), CutFill (2), Earthwork (3), Fill (1), Structure (4) """
    Cut = None
    CutFill = None
    Earthwork = None
    Fill = None
    Structure = None
    value__ = None


class MaterialSection(Section):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: MaterialSection) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: MaterialSection) = value
"""



class MaterialSectionSource(object):
    # no doc
    def GetMaterialSectionIds(self):
        """ GetMaterialSectionIds(self: MaterialSectionSource) -> ObjectIdCollection """
        pass

    IsSampled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSampled(self: MaterialSectionSource) -> bool

"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: MaterialSectionSource) -> QTOMaterial

"""

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceType(self: MaterialSectionSource) -> SectionSourceType

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: MaterialSectionSource) -> ObjectId

Set: StyleId(self: MaterialSectionSource) = value
"""

    UpdateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateMode(self: MaterialSectionSource) -> SectionUpdateType

"""



class MaterialSectionSourceCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: MaterialSectionSourceCollection) -> IEnumerator[MaterialSectionSource] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: MaterialSectionSourceCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MaterialSectionSource](enumerable: IEnumerable[MaterialSectionSource], value: MaterialSectionSource) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MaterialSectionSourceCollection) -> int

"""



class MaterialVolumeCalculationMethodType(Enum):
    """ enum MaterialVolumeCalculationMethodType, values: AverageEndArea (0), CompositeVolume (2), Prismoidal (1) """
    AverageEndArea = None
    CompositeVolume = None
    Prismoidal = None
    value__ = None


class MultipleProfileViewsCreationOptions(object):
    """ MultipleProfileViewsCreationOptions() """
    DrawOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawOrder(self: MultipleProfileViewsCreationOptions) -> ProfileViewPlotType

Set: DrawOrder(self: MultipleProfileViewsCreationOptions) = value
"""

    GapBetweenViewsInColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GapBetweenViewsInColumn(self: MultipleProfileViewsCreationOptions) -> float

Set: GapBetweenViewsInColumn(self: MultipleProfileViewsCreationOptions) = value
"""

    GapBetweenViewsInRow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GapBetweenViewsInRow(self: MultipleProfileViewsCreationOptions) -> float

Set: GapBetweenViewsInRow(self: MultipleProfileViewsCreationOptions) = value
"""

    LengthOfEachView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthOfEachView(self: MultipleProfileViewsCreationOptions) -> float

Set: LengthOfEachView(self: MultipleProfileViewsCreationOptions) = value
"""

    MaxViewInRowOrColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxViewInRowOrColumn(self: MultipleProfileViewsCreationOptions) -> int

Set: MaxViewInRowOrColumn(self: MultipleProfileViewsCreationOptions) = value
"""

    StartCorner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCorner(self: MultipleProfileViewsCreationOptions) -> ProfileViewStartCornerType

Set: StartCorner(self: MultipleProfileViewsCreationOptions) = value
"""



class Network(GeoEntity):
    # no doc
    def AddCurvePipe(self, pipeFamilyId, pipeSizeId, curve, clockwise, newPipeId, applyRules):
        """ AddCurvePipe(self: Network, pipeFamilyId: ObjectId, pipeSizeId: ObjectId, curve: Curve3d, clockwise: bool, newPipeId: ObjectId, applyRules: bool) -> ObjectId """
        pass

    def AddLinePipe(self, pipeFamilyId, pipeSizeId, line, newPipeId, applyRules):
        """ AddLinePipe(self: Network, pipeFamilyId: ObjectId, pipeSizeId: ObjectId, line: LineSegment3d, newPipeId: ObjectId, applyRules: bool) -> ObjectId """
        pass

    def AddStructure(self, *__args):
        """ AddStructure(self: Network, structureId: ObjectId)AddStructure(self: Network, structureFamilyId: ObjectId, structureSizeId: ObjectId, location: Point3d, rotation: float, newStructureId: ObjectId, applyRules: bool) -> ObjectId """
        pass

    def BreakPipe(self, pipeIdToBreak, breakPoint, existingStructureId, newPipeId):
        """ BreakPipe(self: Network, pipeIdToBreak: ObjectId, breakPoint: Point3d, existingStructureId: ObjectId, newPipeId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def Create(document, networkName):
        """ Create(document: CivilDocument, networkName: str) -> (ObjectId, str) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def FindShortestNetworkPath(startPartId, endPartId, minLength):
        """ FindShortestNetworkPath(startPartId: ObjectId, endPartId: ObjectId, minLength: float) -> (ObjectIdCollection, float) """
        pass

    def GetPipeIds(self):
        """ GetPipeIds(self: Network) -> ObjectIdCollection """
        pass

    def GetSpanningPipePlanLabelIds(self):
        """ GetSpanningPipePlanLabelIds(self: Network) -> ObjectIdCollection """
        pass

    def GetSpanningPipeProfileLabelIds(self):
        """ GetSpanningPipeProfileLabelIds(self: Network) -> ObjectIdCollection """
        pass

    def GetStructureIds(self):
        """ GetStructureIds(self: Network) -> ObjectIdCollection """
        pass

    def MoveParts(self, partIds, dstNetworkId):
        """ MoveParts(self: Network, partIds: ObjectIdCollection, dstNetworkId: ObjectId) """
        pass

    PartsListId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartsListId(self: Network) -> ObjectId

Set: PartsListId(self: Network) = value
"""

    PartsListName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartsListName(self: Network) -> str

Set: PartsListName(self: Network) = value
"""

    PipeNameTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeNameTemplate(self: Network) -> str

Set: PipeNameTemplate(self: Network) = value
"""

    PipeNetworkSectionLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeNetworkSectionLayerId(self: Network) -> ObjectId

Set: PipeNetworkSectionLayerId(self: Network) = value
"""

    PipeNetworkSectionLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeNetworkSectionLayerName(self: Network) -> str

Set: PipeNetworkSectionLayerName(self: Network) = value
"""

    PipePlanLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLabelStyleId(self: Network) -> ObjectId

Set: PipePlanLabelStyleId(self: Network) = value
"""

    PipePlanLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLabelStyleName(self: Network) -> str

Set: PipePlanLabelStyleName(self: Network) = value
"""

    PipePlanLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLayerId(self: Network) -> ObjectId

Set: PipePlanLayerId(self: Network) = value
"""

    PipePlanLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLayerName(self: Network) -> str

Set: PipePlanLayerName(self: Network) = value
"""

    PipeProfileLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLabelStyleId(self: Network) -> ObjectId

Set: PipeProfileLabelStyleId(self: Network) = value
"""

    PipeProfileLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLabelStyleName(self: Network) -> str

Set: PipeProfileLabelStyleName(self: Network) = value
"""

    PipeProfileLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLayerId(self: Network) -> ObjectId

Set: PipeProfileLayerId(self: Network) = value
"""

    PipeProfileLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLayerName(self: Network) -> str

Set: PipeProfileLayerName(self: Network) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: Network) -> ObjectId

Set: ReferenceAlignmentId(self: Network) = value
"""

    ReferenceAlignmentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentName(self: Network) -> str

Set: ReferenceAlignmentName(self: Network) = value
"""

    ReferenceSurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceSurfaceId(self: Network) -> ObjectId

Set: ReferenceSurfaceId(self: Network) = value
"""

    ReferenceSurfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceSurfaceName(self: Network) -> str

Set: ReferenceSurfaceName(self: Network) = value
"""

    StructureNameTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureNameTemplate(self: Network) -> str

Set: StructureNameTemplate(self: Network) = value
"""

    StructurePlanLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructurePlanLabelStyleId(self: Network) -> ObjectId

Set: StructurePlanLabelStyleId(self: Network) = value
"""

    StructurePlanLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructurePlanLabelStyleName(self: Network) -> str

Set: StructurePlanLabelStyleName(self: Network) = value
"""

    StructurePlanLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructurePlanLayerId(self: Network) -> ObjectId

Set: StructurePlanLayerId(self: Network) = value
"""

    StructurePlanLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructurePlanLayerName(self: Network) -> str

Set: StructurePlanLayerName(self: Network) = value
"""

    StructureProfileLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureProfileLabelStyleId(self: Network) -> ObjectId

Set: StructureProfileLabelStyleId(self: Network) = value
"""

    StructureProfileLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureProfileLabelStyleName(self: Network) -> str

Set: StructureProfileLabelStyleName(self: Network) = value
"""

    StructureProfileLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureProfileLayerId(self: Network) -> ObjectId

Set: StructureProfileLayerId(self: Network) = value
"""

    StructureProfileLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureProfileLayerName(self: Network) -> str

Set: StructureProfileLayerName(self: Network) = value
"""



class NetworkCatalogDef(object):
    # no doc
    @staticmethod
    def DeclareNewParameter(globalContext, displayContext, paramName, paramDesc, dataType, usage, defaultUnits, singleton, catManagedList):
        """ DeclareNewParameter(globalContext: str, displayContext: str, paramName: str, paramDesc: str, dataType: PartCatalogDataType, usage: PartParamUsageType, defaultUnits: str, singleton: bool, catManagedList: bool) """
        pass

    @staticmethod
    def DeclarePartProperty(globalContext, domain, partType):
        """ DeclarePartProperty(globalContext: str, domain: DomainType, partType: PartType) """
        pass


class NetworkRule(DBObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    ParamsDouble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsDouble(self: NetworkRule) -> ParamDoubleCollection

"""

    ParamsLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsLong(self: NetworkRule) -> ParamLongCollection

"""



class NoteLabel(Label):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(location: Point3d, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId
        Create(database: Database, location: Point3d) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(database):
        """ GetAvailableLabelIds(database: Database) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class OffsetAlignmentInfo(CivilWrapper<AeccDbAlignment>):
    # no doc
    def AddAutoWidenings(self, *__args):
        """ AddAutoWidenings(self: OffsetAlignmentInfo, wideningInfo: AutoWideningInfo, curveGroups: Array[AlignmentSubEntityArc])AddAutoWidenings(self: OffsetAlignmentInfo, wideningInfo: AutoWideningInfo, location: SweptCurveLocation)AddAutoWidenings(self: OffsetAlignmentInfo, wideningCriteria: AutoWideningCriteriaInfo, curveGroups: Array[AlignmentSubEntityArc])AddAutoWidenings(self: OffsetAlignmentInfo, wideningCriteria: AutoWideningCriteriaInfo, location: SweptCurveLocation) """
        pass

    def AddWidening(self, startStation, endStation, offsetDistance):
        """ AddWidening(self: OffsetAlignmentInfo, startStation: float, endStation: float, offsetDistance: float) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    LockMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockMode(self: OffsetAlignmentInfo) -> AlignmentLockModeType

Set: LockMode(self: OffsetAlignmentInfo) = value
"""

    LockToEndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockToEndStation(self: OffsetAlignmentInfo) -> bool

Set: LockToEndStation(self: OffsetAlignmentInfo) = value
"""

    LockToStartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockToStartStation(self: OffsetAlignmentInfo) -> bool

Set: LockToStartStation(self: OffsetAlignmentInfo) = value
"""

    NominalOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NominalOffset(self: OffsetAlignmentInfo) -> float

Set: NominalOffset(self: OffsetAlignmentInfo) = value
"""

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: OffsetAlignmentInfo) -> ObjectId

"""

    Regions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Regions(self: OffsetAlignmentInfo) -> AlignmentRegionCollection

"""

    Side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Side(self: OffsetAlignmentInfo) -> EntitySideType

"""

    Transitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transitions(self: OffsetAlignmentInfo) -> AlignmentTransitionCollection

"""

    UpdateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateMode(self: OffsetAlignmentInfo) -> AlignmentUpdateModeType

Set: UpdateMode(self: OffsetAlignmentInfo) = value
"""



class OffsetAlignmentWideningCriteria(object):
    # no doc
    AttainmentMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttainmentMethod(self: OffsetAlignmentWideningCriteria) -> str

Set: AttainmentMethod(self: OffsetAlignmentWideningCriteria) = value
"""

    LaneWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LaneWidth(self: OffsetAlignmentWideningCriteria) -> float

Set: LaneWidth(self: OffsetAlignmentWideningCriteria) = value
"""

    LeftLanesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftLanesCount(self: OffsetAlignmentWideningCriteria) -> int

Set: LeftLanesCount(self: OffsetAlignmentWideningCriteria) = value
"""

    MinimumRadiusTableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumRadiusTableName(self: OffsetAlignmentWideningCriteria) -> str

Set: MinimumRadiusTableName(self: OffsetAlignmentWideningCriteria) = value
"""

    RightLanesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightLanesCount(self: OffsetAlignmentWideningCriteria) -> int

Set: RightLanesCount(self: OffsetAlignmentWideningCriteria) = value
"""

    SpiralPercentForSC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralPercentForSC(self: OffsetAlignmentWideningCriteria) -> float

Set: SpiralPercentForSC(self: OffsetAlignmentWideningCriteria) = value
"""

    TangentPercentForTC = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentPercentForTC(self: OffsetAlignmentWideningCriteria) -> float

Set: TangentPercentForTC(self: OffsetAlignmentWideningCriteria) = value
"""

    TransitionLengthTableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionLengthTableName(self: OffsetAlignmentWideningCriteria) -> str

Set: TransitionLengthTableName(self: OffsetAlignmentWideningCriteria) = value
"""

    WheelbaseLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WheelbaseLength(self: OffsetAlignmentWideningCriteria) -> float

Set: WheelbaseLength(self: OffsetAlignmentWideningCriteria) = value
"""

    WideningMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WideningMethod(self: OffsetAlignmentWideningCriteria) -> str

Set: WideningMethod(self: OffsetAlignmentWideningCriteria) = value
"""

    WideningSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WideningSide(self: OffsetAlignmentWideningCriteria) -> WideningSide

Set: WideningSide(self: OffsetAlignmentWideningCriteria) = value
"""



class OffsetAssembly(object):
    # no doc
    def AddSubassembly(self, subassemblyId, pointHookTo=None):
        """
        AddSubassembly(self: OffsetAssembly, subassemblyId: ObjectId) -> AssemblyGroup
        AddSubassembly(self: OffsetAssembly, subassemblyId: ObjectId, pointHookTo: Point)
        """
        pass

    def CopySubassembly(self, subassemblyIdFrom, pointHookTo=None):
        """
        CopySubassembly(self: OffsetAssembly, subassemblyIdFrom: ObjectId) -> AssemblyGroup
        CopySubassembly(self: OffsetAssembly, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: OffsetAssembly) """
        pass

    def InsertSubassemblyAfter(self, subassemblyId, pointHookTo):
        """ InsertSubassemblyAfter(self: OffsetAssembly, subassemblyId: ObjectId, pointHookTo: Point) """
        pass

    def InsertSubassemblyBefore(self, subassemblyId, targetSubassemblyId):
        """ InsertSubassemblyBefore(self: OffsetAssembly, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) """
        pass

    def MirrorSubassembly(self, subassemblyIdFrom, pointHookTo=None):
        """
        MirrorSubassembly(self: OffsetAssembly, subassemblyIdFrom: ObjectId) -> AssemblyGroup
        MirrorSubassembly(self: OffsetAssembly, subassemblyIdFrom: ObjectId, pointHookTo: Point) -> ObjectId
        """
        pass

    def ReplaceSubassembly(self, subassemblyId, targetSubassemblyId):
        """ ReplaceSubassembly(self: OffsetAssembly, subassemblyId: ObjectId, targetSubassemblyId: ObjectId) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    AssemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyId(self: OffsetAssembly) -> ObjectId

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Groups(self: OffsetAssembly) -> AssemblyGroupCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: OffsetAssembly) -> str

Set: Name(self: OffsetAssembly) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: OffsetAssembly) -> Vector2d

Set: Offset(self: OffsetAssembly) = value
"""



class OffsetAssemblyCollection(object):
    # no doc
    def Add(self, offsetAssemblyName, offset):
        """ Add(self: OffsetAssemblyCollection, offsetAssemblyName: str, offset: Vector2d) -> OffsetAssembly """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: OffsetAssemblyCollection) -> IEnumerator[OffsetAssembly] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: OffsetAssemblyCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """
        Remove(self: OffsetAssemblyCollection, offsetAssemblyName: str) -> bool
        Remove(self: OffsetAssemblyCollection, offsetAssembly: OffsetAssembly) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: OffsetAssemblyCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[OffsetAssembly](enumerable: IEnumerable[OffsetAssembly], value: OffsetAssembly) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: OffsetAssemblyCollection) -> int

"""



class OffsetBaseline(BaseBaseline):
    # no doc
    def Dispose(self):
        """ Dispose(self: OffsetBaseline, A_0: bool) """
        pass

    def GetOffsetElevationFromMainBaselineStation(self, mainBaselineStation):
        """ GetOffsetElevationFromMainBaselineStation(self: OffsetBaseline, mainBaselineStation: float) -> Point2d """
        pass

    def IsFeatureLineBased(self):
        """ IsFeatureLineBased(self: OffsetBaseline) -> bool """
        pass

    def MainBaselineStationToOffsetBaselineStation(self, mainBaselineStation):
        """ MainBaselineStationToOffsetBaselineStation(self: OffsetBaseline, mainBaselineStation: float) -> float """
        pass

    def OffsetBaselineStationToMainBaselineStation(self, offsetBaselineStation):
        """ OffsetBaselineStationToMainBaselineStation(self: OffsetBaseline, offsetBaselineStation: float) -> float """
        pass

    def SortedStations(self):
        """ SortedStations(self: OffsetBaseline) -> Array[float] """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: OffsetBaseline) -> ObjectId

"""

    BaselineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaselineType(self: OffsetBaseline) -> CorridorBaselineType

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: OffsetBaseline) -> float

Set: EndStation(self: OffsetBaseline) = value
"""

    EndStationOnMainBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStationOnMainBaseline(self: OffsetBaseline) -> float

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: OffsetBaseline) -> str

"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: OffsetBaseline) -> ObjectId

"""

    RelatedOffsetBaselineFeatureLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelatedOffsetBaselineFeatureLines(self: OffsetBaseline) -> BaselineFeatureLines

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: OffsetBaseline) -> float

Set: StartStation(self: OffsetBaseline) = value
"""

    StartStationOnMainBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStationOnMainBaseline(self: OffsetBaseline) -> float

"""



class OffsetBaselineCollection(CivilWrapper<AeccDbCorridor>):
    # no doc
    def Dispose(self):
        """ Dispose(self: OffsetBaselineCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: OffsetBaselineCollection) -> IEnumerator[OffsetBaseline] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: OffsetBaselineCollection) -> IEnumerator """
        pass

    def OffsetBaselineNames(self):
        """ OffsetBaselineNames(self: OffsetBaselineCollection) -> Array[str] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[OffsetBaseline](enumerable: IEnumerable[OffsetBaseline], value: OffsetBaseline) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: OffsetBaselineCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: OffsetBaselineCollection) -> int

"""



class OffsetLengthOption(Enum):
    """ enum OffsetLengthOption, values: AlignmentStartToEnd (2), IntersectionExtents (1) """
    AlignmentStartToEnd = None
    IntersectionExtents = None
    value__ = None


class OverhangCorrectionType(Enum):
    """ enum OverhangCorrectionType, values: BottomLinks (2), None (0), TopLinks (1) """
    BottomLinks = None
    None = None
    TopLinks = None
    value__ = None


class OverriddenStationInfo(object):
    # no doc
    IsGeometryOverridden = None
    IsParameterOverridden = None
    Station = None


class Parcel(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAvailableParcelAreaLabelIds(self):
        """ GetAvailableParcelAreaLabelIds(self: Parcel) -> ObjectIdCollection """
        pass

    def ResetAreaSelectionLabel(self):
        """ ResetAreaSelectionLabel(self: Parcel) """
        pass

    AreaLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaLocation(self: Parcel) -> Point3d

Set: AreaLocation(self: Parcel) = value
"""

    AreaSelectionLabelLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaSelectionLabelLocation(self: Parcel) -> Point3d

Set: AreaSelectionLabelLocation(self: Parcel) = value
"""

    AreaSelectionLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaSelectionLabelStyleId(self: Parcel) -> ObjectId

Set: AreaSelectionLabelStyleId(self: Parcel) = value
"""

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centroid(self: Parcel) -> Point3d

"""

    IsAreaSelectionLabelPinned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAreaSelectionLabelPinned(self: Parcel) -> bool

Set: IsAreaSelectionLabelPinned(self: Parcel) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: Parcel) -> int

Set: Number(self: Parcel) = value
"""



class ParcelAreaLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(parcelId, labelStyleId=None):
        """
        Create(parcelId: ObjectId, labelStyleId: ObjectId) -> ObjectId
        Create(parcelId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(parcelId):
        """ GetAvailableLabelIds(parcelId: ObjectId) -> ObjectIdCollection """
        pass

    m_SubData = None


class ParcelSegment(Feature):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class ParcelSegmentTable(Table):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class ParcelTable(Table):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class Part(GeoEntity):
    # no doc
    def AddToProfileView(self, profileViewId):
        """ AddToProfileView(self: Part, profileViewId: ObjectId) """
        pass

    def AddToSectionView(self, sectionViewId):
        """ AddToSectionView(self: Part, sectionViewId: ObjectId) """
        pass

    def ApplyResizing(self, *args): #cannot find CLR method
        """ ApplyResizing(self: Part, record: AeccDataRecord*) """
        pass

    def ApplyRules(self):
        """ ApplyRules(self: Part) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: Part, A_0: bool) """
        pass

    def GetOverriddenRuleIds(self):
        """ GetOverriddenRuleIds(self: Part) -> ObjectIdCollection """
        pass

    def GetProfileViewsDisplayingMe(self):
        """ GetProfileViewsDisplayingMe(self: Part) -> ObjectIdCollection """
        pass

    def GetRuleSetStylesRoot(self, *args): #cannot find CLR method
        """ GetRuleSetStylesRoot(self: Part, : AeccDbTreeOid*) -> AeccDbTreeOid* """
        pass

    def GetSectionViewsDisplayingMe(self):
        """ GetSectionViewsDisplayingMe(self: Part) -> ObjectIdCollection """
        pass

    def InnerGetPropertyDoubleValue(self, *args): #cannot find CLR method
        """
        InnerGetPropertyDoubleValue(self: Part, attributeId: UInt32, partType: PartType) -> float
        InnerGetPropertyDoubleValue(self: Part, networkEnum: Context, partType: PartType) -> float
        """
        pass

    def InnerGetPropertyStringValue(self, *args): #cannot find CLR method
        """
        InnerGetPropertyStringValue(self: Part, attributeId: UInt32) -> str
        InnerGetPropertyStringValue(self: Part, networkEnum: Context) -> str
        """
        pass

    def RemoveFromAllProfileViews(self):
        """ RemoveFromAllProfileViews(self: Part) """
        pass

    def RemoveFromAllSectionViews(self):
        """ RemoveFromAllSectionViews(self: Part) """
        pass

    def RemoveFromProfileView(self, profileViewId):
        """ RemoveFromProfileView(self: Part, profileViewId: ObjectId) """
        pass

    def RemoveFromSectionView(self, sectionViewId):
        """ RemoveFromSectionView(self: Part, sectionViewId: ObjectId) """
        pass

    def SwapPartFamilyAndSize(self, partFamilyId, partSizeId):
        """ SwapPartFamilyAndSize(self: Part, partFamilyId: ObjectId, partSizeId: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ConnectedPartCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectedPartCount(self: Part) -> int

"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Domain(self: Part) -> DomainType

"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: Part) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Part) -> str

"""

    NetworkId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetworkId(self: Part) -> ObjectId

"""

    NetworkName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetworkName(self: Part) -> str

"""

    OverrideRuleSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideRuleSet(self: Part) -> bool

Set: OverrideRuleSet(self: Part) = value
"""

    ParamsBool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsBool(self: Part) -> ParamBoolCollection

"""

    ParamsDouble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsDouble(self: Part) -> ParamDoubleCollection

"""

    ParamsLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsLong(self: Part) -> ParamLongCollection

"""

    ParamsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsString(self: Part) -> ParamStringCollection

"""

    PartData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartData(self: Part) -> PartDataRecord

Set: PartData(self: Part) = value
"""

    PartDefId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartDefId(self: Part) -> ObjectId

"""

    PartDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartDescription(self: Part) -> str

"""

    PartSizeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartSizeName(self: Part) -> str

"""

    PartSubType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartSubType(self: Part) -> str

"""

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartType(self: Part) -> PartType

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Part) -> Point3d

Set: Position(self: Part) = value
"""

    ProfileViewPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewPartId(self: Part) -> ObjectId

"""

    RefAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefAlignmentId(self: Part) -> ObjectId

Set: RefAlignmentId(self: Part) = value
"""

    RefAlignmentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefAlignmentName(self: Part) -> str

"""

    RefSurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefSurfaceId(self: Part) -> ObjectId

Set: RefSurfaceId(self: Part) = value
"""

    RefSurfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RefSurfaceName(self: Part) -> str

"""

    RuleSetStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RuleSetStyleId(self: Part) -> ObjectId

Set: RuleSetStyleId(self: Part) = value
"""

    RuleSetStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RuleSetStyleName(self: Part) -> str

Set: RuleSetStyleName(self: Part) = value
"""

    SectionViewPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewPartId(self: Part) -> ObjectId

"""

    Solid3dBody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Solid3dBody(self: Part) -> Solid3d

"""

    SurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceId(self: Part) -> ObjectId

Set: SurfaceId(self: Part) = value
"""

    WallThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallThickness(self: Part) -> float

"""



class PartCatalogDataType(Enum):
    """ enum PartCatalogDataType, values: Bool (3), Double (1), Int (2), String (4) """
    Bool = None
    Double = None
    Int = None
    String = None
    value__ = None


class PartContextType(Enum):
    """ enum PartContextType, values: ConnectionType (303), FloorThickness (302), FlowAnalysisDarcyWeisbach (408), FlowAnalysisHazenWilliams (407), FlowAnalysisManning (406), Material (300), MinCurveRadius (405), PipeInnerBottomToBasePoint (404), PipeInnerDiameter (401), PipeInnerHeight (402), PipeInnerWidth (403), StructApronBackThickness (525), StructApronFrontThickness (526), StructApronLength (527), StructApronWidth (528), StructBarrelHeight (506), StructBarrelPipeClearance (532), StructBoundingShape (500), StructConeHeight (533), StructCover (516), StructDiameter (502), StructFrame (514), StructFrameDiameter (512), StructFrameHeight (511), StructFrameLength (513), StructFrameWidth (529), StructGrate (515), StructHeadwallBaseThickness (518), StructHeadwallBaseWidth (517), StructHeadwallTopThickness (520), StructHeadwallTopWidth (519), StructHeight (501), StructHorizontalPipeClearance (531), StructInnerDiameter (508), StructInnerLength (509), StructInnerWidth (510), StructLength (503), StructPipeCenterElevation (603), StructPipeCrownElevation (604), StructPipeDirection (611), StructPipeFlowDirection (610), StructPipeInnerHeight (607), StructPipeInnerWidth (606), StructPipeInvertElevation (602), StructPipeMaterial (614), StructPipeOuterBottomElevation (601), StructPipeOuterHeight (609), StructPipeOuterTopElevation (605), StructPipeOuterWidth (608), StructPipeShape (612), StructPipeWallThickness (613), StructRimToSumpHeight (505), StructRiserHeight (507), StructSlabThickness (534), StructVerticalPipeClearance (530), StructWidth (504), StructWingBackHeight (521), StructWingFrontHeight (522), StructWingLength (523), StructWingThickness (524), SweptShape (400), WallThickness (301) """
    ConnectionType = None
    FloorThickness = None
    FlowAnalysisDarcyWeisbach = None
    FlowAnalysisHazenWilliams = None
    FlowAnalysisManning = None
    Material = None
    MinCurveRadius = None
    PipeInnerBottomToBasePoint = None
    PipeInnerDiameter = None
    PipeInnerHeight = None
    PipeInnerWidth = None
    StructApronBackThickness = None
    StructApronFrontThickness = None
    StructApronLength = None
    StructApronWidth = None
    StructBarrelHeight = None
    StructBarrelPipeClearance = None
    StructBoundingShape = None
    StructConeHeight = None
    StructCover = None
    StructDiameter = None
    StructFrame = None
    StructFrameDiameter = None
    StructFrameHeight = None
    StructFrameLength = None
    StructFrameWidth = None
    StructGrate = None
    StructHeadwallBaseThickness = None
    StructHeadwallBaseWidth = None
    StructHeadwallTopThickness = None
    StructHeadwallTopWidth = None
    StructHeight = None
    StructHorizontalPipeClearance = None
    StructInnerDiameter = None
    StructInnerLength = None
    StructInnerWidth = None
    StructLength = None
    StructPipeCenterElevation = None
    StructPipeCrownElevation = None
    StructPipeDirection = None
    StructPipeFlowDirection = None
    StructPipeInnerHeight = None
    StructPipeInnerWidth = None
    StructPipeInvertElevation = None
    StructPipeMaterial = None
    StructPipeOuterBottomElevation = None
    StructPipeOuterHeight = None
    StructPipeOuterTopElevation = None
    StructPipeOuterWidth = None
    StructPipeShape = None
    StructPipeWallThickness = None
    StructRimToSumpHeight = None
    StructRiserHeight = None
    StructSlabThickness = None
    StructVerticalPipeClearance = None
    StructWidth = None
    StructWingBackHeight = None
    StructWingFrontHeight = None
    StructWingLength = None
    StructWingThickness = None
    SweptShape = None
    value__ = None
    WallThickness = None


class PartDataField(object):
    # no doc
    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Context(self: PartDataField) -> PartContextType

"""

    ContextString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContextString(self: PartDataField) -> str

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: PartDataField) -> PartCatalogDataType

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PartDataField) -> str

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: PartDataField) -> int

"""

    IsFromList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFromList(self: PartDataField) -> bool

"""

    IsFromRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFromRange(self: PartDataField) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: PartDataField) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PartDataField) -> str

"""

    Units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Units(self: PartDataField) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: PartDataField) -> object

Set: Value(self: PartDataField) = value
"""

    ValueList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueList(self: PartDataField) -> PartDataList

"""

    ValueRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueRange(self: PartDataField) -> PartDataRange

"""


    m_dataField = None
    m_domain = None
    m_parentDataRecord = None
    m_rawTable = None


class PartDataList(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: PartDataList) """
        pass

    def IsValidValue(self, value):
        """ IsValidValue(self: PartDataList, value: object) -> bool """
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

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Context(self: PartDataList) -> PartContextType

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PartDataList) -> int

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: PartDataList) -> PartCatalogDataType

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: PartDataList) -> int

"""



class PartDataRange(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: PartDataRange) """
        pass

    def IsValidValue(self, value):
        """ IsValidValue(self: PartDataRange, value: object) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Context(self: PartDataRange) -> PartContextType

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: PartDataRange) -> PartCatalogDataType

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: PartDataRange) -> int

"""

    RangeDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeDefault(self: PartDataRange) -> object

"""

    RangeMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeMax(self: PartDataRange) -> object

"""

    RangeMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeMin(self: PartDataRange) -> object

"""



class PartDataRecord(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: PartDataRecord) """
        pass

    def GetAllDataFields(self):
        """ GetAllDataFields(self: PartDataRecord) -> Array[PartDataField] """
        pass

    def GetDataFieldBy(self, *__args):
        """
        GetDataFieldBy(self: PartDataRecord, context: PartContextType, index: int) -> PartDataField
        GetDataFieldBy(self: PartDataRecord, context: PartContextType) -> PartDataField
        GetDataFieldBy(self: PartDataRecord, name: str) -> PartDataField
        """
        pass

    def GetMaxIndex(self, context):
        """ GetMaxIndex(self: PartDataRecord, context: PartContextType) -> int """
        pass

    def GetSupportedContexts(self):
        """ GetSupportedContexts(self: PartDataRecord) -> Array[PartContextType] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class PartDef(DBObject):
    """ PartDef(unmanagedPointer: IntPtr, autoDelete: bool) """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def Get3dBody(self):
        """ Get3dBody(self: PartDef) -> Solid3d """
        pass

    def GetBoundingShapeBody(self):
        """ GetBoundingShapeBody(self: PartDef) -> Solid3d """
        pass

    def GetNetworkPartViewDef(self):
        """ GetNetworkPartViewDef(self: PartDef) -> PartViewDef """
        pass

    def GetProfileInFrontView(self):
        """ GetProfileInFrontView(self: PartDef) -> Profile """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedPointer, autoDelete):
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class PartParamUsageType(Enum):
    """ enum PartParamUsageType, values: BoolGeneral (401), DoubleAngle (106), DoubleArea (108), DoubleDistance (104), DoubleDistanceMinor (105), DoubleElevation (110), DoubleGeneral (101), DoubleNonZero (102), DoubleNonZeroNonNegative (103), DoublePercent (107), DoubleVolume (109), IntGeneral (201), IntNonZero (202), IntNonZeroNonNegative (203), MultipleValueDirection (502), MultipleValuePosition (501), StringEnumKey (304), StringGeneral (301), StringGuid (303), StringName (302) """
    BoolGeneral = None
    DoubleAngle = None
    DoubleArea = None
    DoubleDistance = None
    DoubleDistanceMinor = None
    DoubleElevation = None
    DoubleGeneral = None
    DoubleNonZero = None
    DoubleNonZeroNonNegative = None
    DoublePercent = None
    DoubleVolume = None
    IntGeneral = None
    IntNonZero = None
    IntNonZeroNonNegative = None
    MultipleValueDirection = None
    MultipleValuePosition = None
    StringEnumKey = None
    StringGeneral = None
    StringGuid = None
    StringName = None
    value__ = None


class PartProfileLabel(FeatureLabel):
    # no doc
    def checkProfileViewPartInProfileView(self, *args): #cannot find CLR method
        """ checkProfileViewPartInProfileView(oidProfileViewPart: AcDbObjectId, oidProfileView: AcDbObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PartProfileLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PartProfileLabel) = value
"""


    m_SubData = None


class PartSectionLabel(FeatureLabel):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def getIntersectionCount(self, *args): #cannot find CLR method
        """ getIntersectionCount(oidPart: AcDbObjectId, oidSectionPipeNetwork: AcDbObjectId) -> int """
        pass

    def isNetworkPartTheSourceOfSectionPipeNetwork(self, *args): #cannot find CLR method
        """ isNetworkPartTheSourceOfSectionPipeNetwork(oidPart: AcDbObjectId, oidSectionPipeNetwork: AcDbObjectId) -> bool """
        pass

    def isSectionViewContainSectionPipeNetowrk(self, *args): #cannot find CLR method
        """ isSectionViewContainSectionPipeNetowrk(oidPart: AcDbObjectId, oidSectionView: AcDbObjectId) -> bool """
        pass

    def isSectionViewDrawSectionPipeNetwork(self, *args): #cannot find CLR method
        """ isSectionViewDrawSectionPipeNetwork(oidPart: AcDbObjectId, oidSectionView: AcDbObjectId) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PartSectionLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PartSectionLabel) = value
"""


    m_SubData = None


class PartType(Enum):
    """ enum PartType, values: Channel (11), Conduit (13), Pipe (10), StructEquipment (105), StructGeneral (104), StructInletOutlet (103), StructJunction (102), StructNull (101), UndefinedPartType (0), Wire (12) """
    Channel = None
    Conduit = None
    Pipe = None
    StructEquipment = None
    StructGeneral = None
    StructInletOutlet = None
    StructJunction = None
    StructNull = None
    UndefinedPartType = None
    value__ = None
    Wire = None


class PartViewDef(ImpObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    BoundingBodyBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBodyBlockId(self: PartViewDef) -> ObjectId

"""

    BoundingBodyBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingBodyBlockName(self: PartViewDef) -> str

"""

    PartBodyGraphicsBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartBodyGraphicsBlockId(self: PartViewDef) -> ObjectId

"""

    PartBodyGraphicsBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartBodyGraphicsBlockName(self: PartViewDef) -> str

"""



class PayItemFileFormat(Enum):
    """ enum PayItemFileFormat, values: AutodeskTakeoffTemplate (4), CommaSeparated (3), FloridaDOT (2), NotSet (0), TransXml (1) """
    AutodeskTakeoffTemplate = None
    CommaSeparated = None
    FloridaDOT = None
    NotSet = None
    TransXml = None
    value__ = None


class Pipe(Part):
    # no doc
    def AdjustEndpoint(self, endpointToAdjust, targetLocation, dOffset):
        """ AdjustEndpoint(self: Pipe, endpointToAdjust: ConnectorPositionType, targetLocation: PipeEndLocation, dOffset: float) -> bool """
        pass

    def ConnectToPipe(self, sourceType, destinationPipeId, destinationType, structureFamilyId, structureSizeId, newStructureId, applyRules, force):
        """ ConnectToPipe(self: Pipe, sourceType: ConnectorPositionType, destinationPipeId: ObjectId, destinationType: ConnectorPositionType, structureFamilyId: ObjectId, structureSizeId: ObjectId, newStructureId: ObjectId, applyRules: bool, force: bool) -> ObjectId """
        pass

    def ConnectToStructure(self, sourcePosition, destinationStructureId, force):
        """ ConnectToStructure(self: Pipe, sourcePosition: ConnectorPositionType, destinationStructureId: ObjectId, force: bool) """
        pass

    def Disconnect(self, pos):
        """ Disconnect(self: Pipe, pos: ConnectorPositionType) """
        pass

    def Dispose(self):
        """ Dispose(self: Part, A_0: bool) """
        pass

    def GetAvailablePipeLabelIds(self):
        """ GetAvailablePipeLabelIds(self: Pipe) -> ObjectIdCollection """
        pass

    def GetAvailableSpanningPipeLabelIds(self):
        """ GetAvailableSpanningPipeLabelIds(self: Pipe) -> ObjectIdCollection """
        pass

    def GetClosestPointTo(self, *__args):
        """ GetClosestPointTo(self: Pipe, sourcePoint: Point3d) -> Point3d """
        pass

    def GetLabelIds(self):
        """ GetLabelIds(self: Pipe) -> ObjectIdCollection """
        pass

    def GetParamAtPoint(self, point):
        """ GetParamAtPoint(self: Pipe, point: Point3d) -> float """
        pass

    def GetPipeLabelIds(self):
        """ GetPipeLabelIds(self: Pipe) -> ObjectIdCollection """
        pass

    def GetPointAtParam(self, paramInterval):
        """ GetPointAtParam(self: Pipe, paramInterval: float) -> Point3d """
        pass

    def GetProject2dPointVertically(self, sourcePoint, projectPoint):
        """ GetProject2dPointVertically(self: Pipe, sourcePoint: Point2d, projectPoint: Point3d) -> (bool, Point3d) """
        pass

    def IsMaxCoverViolated(self, maxCover, pointsViolated, differences, params):
        """ IsMaxCoverViolated(self: Pipe, maxCover: float, pointsViolated: Array[Point3d], differences: Array[float], params: Array[float]) -> (bool, Array[Point3d], Array[float], Array[float]) """
        pass

    def IsMinCoverViolated(self, minCover, pointsViolated, differences, params):
        """ IsMinCoverViolated(self: Pipe, minCover: float, pointsViolated: Array[Point3d], differences: Array[float], params: Array[float]) -> (bool, Array[Point3d], Array[float], Array[float]) """
        pass

    def ResizeByInnerDiameterOrWidth(self, innerDiameterOrWidth, useClosestSize):
        """ ResizeByInnerDiameterOrWidth(self: Pipe, innerDiameterOrWidth: float, useClosestSize: bool) """
        pass

    def SetSlopeHoldEnd(self, endValue):
        """ SetSlopeHoldEnd(self: Pipe, endValue: float) """
        pass

    def SetSlopeHoldStart(self, startValue):
        """ SetSlopeHoldStart(self: Pipe, startValue: float) """
        pass

    Bearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bearing(self: Pipe) -> float

"""

    CoverOfEndpoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoverOfEndpoint(self: Pipe) -> float

"""

    CoverOfStartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoverOfStartPoint(self: Pipe) -> float

"""

    CrossSectionalShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionalShape(self: Pipe) -> SweptShapeType

"""

    Curve2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve2d(self: Pipe) -> CircularArc2d

"""

    EndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffset(self: Pipe) -> float

"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Pipe) -> Point3d

Set: EndPoint(self: Pipe) = value
"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: Pipe) -> float

"""

    EndStructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStructureId(self: Pipe) -> ObjectId

"""

    EnergyGradeLineDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnergyGradeLineDown(self: Pipe) -> float

Set: EnergyGradeLineDown(self: Pipe) = value
"""

    EnergyGradeLineUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnergyGradeLineUp(self: Pipe) -> float

Set: EnergyGradeLineUp(self: Pipe) = value
"""

    FlowDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowDirection(self: Pipe) -> FlowDirectionType

"""

    FlowDirectionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowDirectionMethod(self: Pipe) -> FlowDirectionMethodType

Set: FlowDirectionMethod(self: Pipe) = value
"""

    FlowRate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowRate(self: Pipe) -> float

Set: FlowRate(self: Pipe) = value
"""

    HoldOnResizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HoldOnResizeType(self: Pipe) -> HoldOnResizeType

Set: HoldOnResizeType(self: Pipe) = value
"""

    HydraulicGradeLineDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HydraulicGradeLineDown(self: Pipe) -> float

Set: HydraulicGradeLineDown(self: Pipe) = value
"""

    HydraulicGradeLineUp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HydraulicGradeLineUp(self: Pipe) -> float

Set: HydraulicGradeLineUp(self: Pipe) = value
"""

    InnerDiameterOrWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerDiameterOrWidth(self: Pipe) -> float

"""

    InnerHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerHeight(self: Pipe) -> float

"""

    JunctionLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JunctionLoss(self: Pipe) -> float

Set: JunctionLoss(self: Pipe) = value
"""

    Length2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2D(self: Pipe) -> float

"""

    Length2DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2DCenterToCenter(self: Pipe) -> float

"""

    Length2DToInsideEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2DToInsideEdge(self: Pipe) -> float

"""

    Length3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3D(self: Pipe) -> float

"""

    Length3DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3DCenterToCenter(self: Pipe) -> float

"""

    Length3DToInsideEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3DToInsideEdge(self: Pipe) -> float

"""

    MaximumCover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumCover(self: Pipe) -> float

"""

    MinimumCover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumCover(self: Pipe) -> float

"""

    OuterDiameterOrWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterDiameterOrWidth(self: Pipe) -> float

"""

    OuterHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterHeight(self: Pipe) -> float

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: Pipe) -> float

"""

    ReturnPeriod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReturnPeriod(self: Pipe) -> int

Set: ReturnPeriod(self: Pipe) = value
"""

    Slope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slope(self: Pipe) -> float

"""

    StartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffset(self: Pipe) -> float

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Pipe) -> Point3d

Set: StartPoint(self: Pipe) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: Pipe) -> float

"""

    StartStructureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStructureId(self: Pipe) -> ObjectId

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Pipe) = value
"""

    SubEntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubEntityType(self: Pipe) -> PipeSubEntityType

"""



class PipeEndLocation(Enum):
    """ enum PipeEndLocation, values: StructureCenter (0), StructureInnerWall (1), StructureOuterWall (2) """
    StructureCenter = None
    StructureInnerWall = None
    StructureOuterWall = None
    value__ = None


class PipeLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(pipeId, ratio, labelStyleId=None):
        """
        Create(pipeId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId
        Create(pipeId: ObjectId, ratio: float) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(pipeId):
        """ GetAvailableLabelIds(pipeId: ObjectId) -> ObjectIdCollection """
        pass

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PipeLabel) -> float

Set: Ratio(self: PipeLabel) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PipeLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PipeLabel) = value
"""


    m_SubData = None


class PipeNetworkBandLabelGroup(ProfileBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class PipeOverride(GraphOverride):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverride, A_0: bool) """
        pass

    Draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Draw(self: PipeOverride) = value
"""

    OverrideStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleId(self: PipeOverride) = value
"""

    OverrideStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleName(self: PipeOverride) = value
"""

    PipeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeId(self: PipeOverride) -> ObjectId

"""

    PipeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeName(self: PipeOverride) -> str

"""


    m_pDataLineId = None


class PipeOverrideCollection(GraphOverrideCollection[PipeOverride]):
    # no doc
    def Dispose(self):
        """ Dispose(self: PipeOverrideCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PipeOverrideCollection) -> IEnumerator[PipeOverride] """
        pass

    SplitAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitAt(self: PipeOverrideCollection) -> str

Set: SplitAt(self: PipeOverrideCollection) = value
"""


    m_dataVector = None


class PipeProfileLabel(PartProfileLabel):
    # no doc
    @staticmethod
    def Create(profileViewPartId, profileViewId, ratio=None, labelStyleId=None):
        """
        Create(profileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId
        Create(profileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(profileViewId):
        """ GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PipeProfileLabel) -> float

Set: Ratio(self: PipeProfileLabel) = value
"""


    m_SubData = None


class PipeSectionLabel(PartSectionLabel):
    # no doc
    @staticmethod
    def Create(sectionViewId, pipeId, sectionPipeNetworkId, partIndex, labelStyleId=None):
        """
        Create(sectionViewId: ObjectId, pipeId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: int, labelStyleId: ObjectId) -> ObjectId
        Create(sectionViewId: ObjectId, pipeId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: int) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(sectionViewId):
        """ GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection """
        pass

    m_SubData = None


class PipeSubEntityType(Enum):
    """ enum PipeSubEntityType, values: Curved (258), Flex (260), Segmented (259), Straight (257) """
    Curved = None
    Flex = None
    Segmented = None
    Straight = None
    value__ = None


class Point(CivilWrapper<AeccDbEntity>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbEntity>, A_0: bool) """
        pass

    def GetXYZ(self, x, y, z):
        """ GetXYZ(self: Point, x: float, y: float, z: float) -> (float, float, float) """
        pass

    Codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Codes(self: Point) -> CodeCollection

"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: Point) -> float

Set: Elevation(self: Point) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: Point) -> int

"""

    IsHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHidden(self: Point) -> bool

Set: IsHidden(self: Point) = value
"""

    IsLoopPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLoopPoint(self: Point) -> bool

Set: IsLoopPoint(self: Point) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: Point) -> float

Set: Offset(self: Point) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: Point) -> float

Set: Station(self: Point) = value
"""



class PointCloud(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class PointCloudUtility(object):
    # no doc
    @staticmethod
    def GetCivilPointCloudName(A_0):
        """ GetCivilPointCloudName(A_0: ObjectId) -> str """
        pass

    @staticmethod
    def IsCivilPointCloud(A_0):
        """ IsCivilPointCloud(A_0: ObjectId) -> bool """
        pass


class PointCollection(CivilWrapper<AeccDbEntity>):
    # no doc
    def Add(self, offset, elevation, *__args):
        """
        Add(self: PointCollection, offset: float, elevation: float, code: str) -> Point
        Add(self: PointCollection, offset: float, elevation: float, codes: Array[str]) -> Point
        """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbEntity>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PointCollection) -> IEnumerator[Point] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: PointCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """ Remove(self: PointCollection, index: int)Remove(self: PointCollection, point: Point) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Point](enumerable: IEnumerable[Point], value: Point) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PointCollection) -> int

"""



class PointDescriptionKey(DBObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    ApplyDrawingScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyDrawingScale(self: PointDescriptionKey) -> bool

Set: ApplyDrawingScale(self: PointDescriptionKey) = value
"""

    ApplyFixedLabelRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyFixedLabelRotation(self: PointDescriptionKey) -> bool

Set: ApplyFixedLabelRotation(self: PointDescriptionKey) = value
"""

    ApplyFixedMarkerRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyFixedMarkerRotation(self: PointDescriptionKey) -> bool

Set: ApplyFixedMarkerRotation(self: PointDescriptionKey) = value
"""

    ApplyFixedScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyFixedScaleFactor(self: PointDescriptionKey) -> bool

Set: ApplyFixedScaleFactor(self: PointDescriptionKey) = value
"""

    ApplyLabelRotationParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyLabelRotationParameter(self: PointDescriptionKey) -> bool

Set: ApplyLabelRotationParameter(self: PointDescriptionKey) = value
"""

    ApplyLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyLabelStyleId(self: PointDescriptionKey) -> bool

Set: ApplyLabelStyleId(self: PointDescriptionKey) = value
"""

    ApplyLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyLayerId(self: PointDescriptionKey) -> bool

Set: ApplyLayerId(self: PointDescriptionKey) = value
"""

    ApplyMarkerRotationParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyMarkerRotationParameter(self: PointDescriptionKey) -> bool

Set: ApplyMarkerRotationParameter(self: PointDescriptionKey) = value
"""

    ApplyScaleParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyScaleParameter(self: PointDescriptionKey) -> bool

Set: ApplyScaleParameter(self: PointDescriptionKey) = value
"""

    ApplyScaleXY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyScaleXY(self: PointDescriptionKey) -> bool

Set: ApplyScaleXY(self: PointDescriptionKey) = value
"""

    ApplyScaleZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyScaleZ(self: PointDescriptionKey) -> bool

Set: ApplyScaleZ(self: PointDescriptionKey) = value
"""

    ApplyStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyStyleId(self: PointDescriptionKey) -> bool

Set: ApplyStyleId(self: PointDescriptionKey) = value
"""

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: PointDescriptionKey) -> str

Set: Code(self: PointDescriptionKey) = value
"""

    FixedLabelRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedLabelRotation(self: PointDescriptionKey) -> float

Set: FixedLabelRotation(self: PointDescriptionKey) = value
"""

    FixedMarkerRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedMarkerRotation(self: PointDescriptionKey) -> float

Set: FixedMarkerRotation(self: PointDescriptionKey) = value
"""

    FixedScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedScaleFactor(self: PointDescriptionKey) -> float

Set: FixedScaleFactor(self: PointDescriptionKey) = value
"""

    Format = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Format(self: PointDescriptionKey) -> str

Set: Format(self: PointDescriptionKey) = value
"""

    LabelRotationParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelRotationParameter(self: PointDescriptionKey) -> int

Set: LabelRotationParameter(self: PointDescriptionKey) = value
"""

    LabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleId(self: PointDescriptionKey) -> ObjectId

Set: LabelStyleId(self: PointDescriptionKey) = value
"""

    LayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerId(self: PointDescriptionKey) -> ObjectId

Set: LayerId(self: PointDescriptionKey) = value
"""

    MarkerRotationParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerRotationParameter(self: PointDescriptionKey) -> int

Set: MarkerRotationParameter(self: PointDescriptionKey) = value
"""

    RotationDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationDirection(self: PointDescriptionKey) -> RotationDirType

Set: RotationDirection(self: PointDescriptionKey) = value
"""

    ScaleParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleParameter(self: PointDescriptionKey) -> int

Set: ScaleParameter(self: PointDescriptionKey) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: PointDescriptionKey) -> ObjectId

Set: StyleId(self: PointDescriptionKey) = value
"""



class PointDescriptionKeySet(DBObject):
    # no doc
    def Add(self, codeName):
        """ Add(self: PointDescriptionKeySet, codeName: str) -> ObjectId """
        pass

    def Clear(self):
        """ Clear(self: PointDescriptionKeySet) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: PointDescriptionKeySet, objectId: ObjectId) -> bool
        Contains(self: PointDescriptionKeySet, name: str) -> bool
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetPointDescriptionKeyIds(self):
        """ GetPointDescriptionKeyIds(self: PointDescriptionKeySet) -> ObjectIdCollection """
        pass

    def Remove(self, keyId):
        """ Remove(self: PointDescriptionKeySet, keyId: ObjectId) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PointDescriptionKeySet) -> int

"""



class PointDescriptionKeySetCollection(object):
    # no doc
    def Add(self, name):
        """ Add(self: PointDescriptionKeySetCollection, name: str) -> ObjectId """
        pass

    def Clear(self):
        """ Clear(self: PointDescriptionKeySetCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: PointDescriptionKeySetCollection, objectId: ObjectId) -> bool
        Contains(self: PointDescriptionKeySetCollection, name: str) -> bool
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PointDescriptionKeySetCollection) -> IEnumerator[ObjectId] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: PointDescriptionKeySetCollection) -> IEnumerator """
        pass

    @staticmethod
    def GetPointDescriptionKeySets(database):
        """ GetPointDescriptionKeySets(database: Database) -> PointDescriptionKeySetCollection """
        pass

    def Remove(self, *__args):
        """ Remove(self: PointDescriptionKeySetCollection, name: str)Remove(self: PointDescriptionKeySetCollection, objectId: ObjectId) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: PointDescriptionKeySetCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerable: IEnumerable[ObjectId], value: ObjectId) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PointDescriptionKeySetCollection) -> int

"""

    SearchOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchOrder(self: PointDescriptionKeySetCollection) -> ObjectIdCollection

Set: SearchOrder(self: PointDescriptionKeySetCollection) = value
"""



class PointFileFormat(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: PointFileFormat, obj: object) -> bool """
        pass

    CommentTag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommentTag(self: PointFileFormat) -> str

"""

    Delimiter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Delimiter(self: PointFileFormat) -> str

"""

    FileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileExtension(self: PointFileFormat) -> str

"""

    FileFormatType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileFormatType(self: PointFileFormat) -> PointFileFormatType

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PointFileFormat) -> str

"""



class PointFileFormatCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: PointFileFormatCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PointFileFormatCollection) -> IEnumerator[PointFileFormat] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: PointFileFormatCollection) -> IEnumerator """
        pass

    @staticmethod
    def GetPointFileFormats(pDatabase):
        """ GetPointFileFormats(pDatabase: Database) -> PointFileFormatCollection """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PointFileFormat](enumerable: IEnumerable[PointFileFormat], value: PointFileFormat) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PointFileFormatCollection) -> int

"""



class PointGroup(DBObject):
    # no doc
    def ApplyDescriptionKeys(self):
        """ ApplyDescriptionKeys(self: PointGroup) """
        pass

    def ContainsPoint(self, pointNumber):
        """ ContainsPoint(self: PointGroup, pointNumber: UInt32) -> bool """
        pass

    def DeletePoints(self):
        """ DeletePoints(self: PointGroup) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetPendingChanges(self):
        """ GetPendingChanges(self: PointGroup) -> PointGroupChangeInfo """
        pass

    def GetPointNumbers(self):
        """ GetPointNumbers(self: PointGroup) -> Array[UInt32] """
        pass

    def GetQuery(self):
        """ GetQuery(self: PointGroup) -> PointGroupQuery """
        pass

    def LockPoints(self):
        """ LockPoints(self: PointGroup) """
        pass

    def SetQuery(self, query):
        """ SetQuery(self: PointGroup, query: PointGroupQuery) """
        pass

    def UnlockPoints(self):
        """ UnlockPoints(self: PointGroup) """
        pass

    def Update(self):
        """ Update(self: PointGroup) """
        pass

    def UseAllClassifications(self):
        """ UseAllClassifications(self: PointGroup) """
        pass

    def UseCustomClassification(self, *__args):
        """ UseCustomClassification(self: PointGroup, name: str)UseCustomClassification(self: PointGroup, udpClassification: UDPClassification) """
        pass

    def UseNoneClassification(self):
        """ UseNoneClassification(self: PointGroup) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ElevationOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationOverride(self: PointGroup) -> PointGroupElevationOverrideInfo

"""

    IsElevationOverridden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsElevationOverridden(self: PointGroup) -> bool

Set: IsElevationOverridden(self: PointGroup) = value
"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLocked(self: PointGroup) -> bool

Set: IsLocked(self: PointGroup) = value
"""

    IsOutOfDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOutOfDate(self: PointGroup) -> bool

"""

    IsPointLabelStyleOverridden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPointLabelStyleOverridden(self: PointGroup) -> bool

Set: IsPointLabelStyleOverridden(self: PointGroup) = value
"""

    IsPointStyleOverridden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPointStyleOverridden(self: PointGroup) -> bool

Set: IsPointStyleOverridden(self: PointGroup) = value
"""

    IsRawDescriptionOverridden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRawDescriptionOverridden(self: PointGroup) -> bool

Set: IsRawDescriptionOverridden(self: PointGroup) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PointGroup) -> str

Set: Name(self: PointGroup) = value
"""

    PointLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointLabelStyleId(self: PointGroup) -> ObjectId

Set: PointLabelStyleId(self: PointGroup) = value
"""

    PointsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointsCount(self: PointGroup) -> UInt32

"""

    PointStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointStyleId(self: PointGroup) -> ObjectId

Set: PointStyleId(self: PointGroup) = value
"""

    RawDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawDescription(self: PointGroup) -> str

"""

    RawDescriptionOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawDescriptionOverride(self: PointGroup) -> PointGroupRawDescriptionOverrideInfo

"""

    UDPClassificationApplyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UDPClassificationApplyType(self: PointGroup) -> UDPClassificationApplyType

"""

    UDPClassificationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UDPClassificationName(self: PointGroup) -> str

"""


    AllPointsGroupName = '_All Points'


class PointGroupChangeInfo(object):
    # no doc
    PointsToAdd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointsToAdd(self: PointGroupChangeInfo) -> Array[UInt32]

"""

    PointsToRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointsToRemove(self: PointGroupChangeInfo) -> Array[UInt32]

"""



class PointGroupCollection(object):
    # no doc
    def Add(self, name):
        """ Add(self: PointGroupCollection, name: str) -> ObjectId """
        pass

    def Contains(self, *__args):
        """
        Contains(self: PointGroupCollection, pointGroupId: ObjectId) -> bool
        Contains(self: PointGroupCollection, name: str) -> bool
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PointGroupCollection) -> IEnumerator[ObjectId] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: PointGroupCollection) -> IEnumerator """
        pass

    def GetOutOfDatePointGroupIds(self):
        """ GetOutOfDatePointGroupIds(self: PointGroupCollection) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetPointGroups(pDatabase):
        """ GetPointGroups(pDatabase: Database) -> PointGroupCollection """
        pass

    def Remove(self, *__args):
        """ Remove(self: PointGroupCollection, name: str)Remove(self: PointGroupCollection, pointGroupId: ObjectId) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: PointGroupCollection, index: int) """
        pass

    def UpdateAllPointGroups(self):
        """ UpdateAllPointGroups(self: PointGroupCollection) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerable: IEnumerable[ObjectId], value: ObjectId) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    AllPointsPointGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllPointsPointGroupId(self: PointGroupCollection) -> ObjectId

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PointGroupCollection) -> int

"""

    DrawOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawOrder(self: PointGroupCollection) -> ObjectIdCollection

Set: DrawOrder(self: PointGroupCollection) = value
"""



class PointGroupOverrideInfo(object):
    # no doc
    ActiveOverrideType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveOverrideType(self: PointGroupOverrideInfo) -> PointGroupOverrideType

Set: ActiveOverrideType(self: PointGroupOverrideInfo) = value
"""

    XDRefId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XDRefId(self: PointGroupOverrideInfo) -> ObjectId

Set: XDRefId(self: PointGroupOverrideInfo) = value
"""



class PointGroupElevationOverrideInfo(PointGroupOverrideInfo):
    # no doc
    FixedElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedElevation(self: PointGroupElevationOverrideInfo) -> float

Set: FixedElevation(self: PointGroupElevationOverrideInfo) = value
"""

    UDP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UDP(self: PointGroupElevationOverrideInfo) -> UDPDouble

Set: UDP(self: PointGroupElevationOverrideInfo) = value
"""



class PointGroupOverrideType(Enum):
    """ enum PointGroupOverrideType, values: FixedValue (0), UserDefinedProperty (2), XDRef (1) """
    FixedValue = None
    UserDefinedProperty = None
    value__ = None
    XDRef = None


class PointGroupQueryInvalidPointGroupValueException(ArgumentException):
    # no doc
    InvalidPointGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InvalidPointGroup(self: PointGroupQueryInvalidPointGroupValueException) -> str

"""



class PointGroupQueryOperationFailedException(ArgumentException):
    # no doc

class PointGroupQueryParserException(ArgumentException):
    # no doc
    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: PointGroupQueryParserException) -> int

"""

    Query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Query(self: PointGroupQueryParserException) -> str

"""



class PointGroupQueryToken(object):
    """ PointGroupQueryToken() """
    AND = 'AND'
    ClosingParenthesis = ')'
    Equal = '='
    FullDescriptionField = 'FullDescription'
    GreaterThan = '>'
    GreaterThanOrEqual = '>='
    LessThan = '<'
    LessThanOrEqual = '<='
    NameField = 'Name'
    NOT = 'NOT'
    NotEqual = '!='
    OpeningParenthesis = '('
    OR = 'OR'
    PointElevationField = 'PointElevation'
    PointGroupField = 'PointGroup'
    PointNumberField = 'PointNumber'
    RawDescriptionField = 'RawDescription'
    SingleQuoteCode = '&squot;'
    ValueDelimiter = "'"


class PointGroupRawDescriptionOverrideInfo(PointGroupOverrideInfo):
    # no doc
    FixedRawDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedRawDescription(self: PointGroupRawDescriptionOverrideInfo) -> str

Set: FixedRawDescription(self: PointGroupRawDescriptionOverrideInfo) = value
"""

    UDP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UDP(self: PointGroupRawDescriptionOverrideInfo) -> UDP

Set: UDP(self: PointGroupRawDescriptionOverrideInfo) = value
"""



class PointInMem(object):
    """ PointInMem() """
    Codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Codes(self: PointInMem) -> CodeCollection

"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: PointInMem) -> float

Set: Elevation(self: PointInMem) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: PointInMem) -> int

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: PointInMem) -> float

Set: Offset(self: PointInMem) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: PointInMem) -> float

Set: Station(self: PointInMem) = value
"""



class PointNumberResolveType(Enum):
    """ enum PointNumberResolveType, values: Overwrite (1), UseNext (0) """
    Overwrite = None
    UseNext = None
    value__ = None


class PointTable(Table):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class PolylineOptions(object):
    # no doc
    def Equals(self, *__args):
        """
        Equals(self: PolylineOptions, obj: object) -> bool
        Equals(self: PolylineOptions, other: PolylineOptions) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PolylineOptions) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AddCurvesBetweenTangents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddCurvesBetweenTangents(self: PolylineOptions) -> bool

Set: AddCurvesBetweenTangents(self: PolylineOptions) = value
"""

    EraseExistingEntities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EraseExistingEntities(self: PolylineOptions) -> bool

Set: EraseExistingEntities(self: PolylineOptions) = value
"""

    PlineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlineId(self: PolylineOptions) -> ObjectId

Set: PlineId(self: PolylineOptions) = value
"""



class PressurePart(GeoEntity):
    # no doc
    def AddToProfileView(self, profileViewId):
        """ AddToProfileView(self: PressurePart, profileViewId: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: PressurePart, A_0: bool) """
        pass

    def GetProfileViewsDisplayingMe(self):
        """ GetProfileViewsDisplayingMe(self: PressurePart) -> ObjectIdCollection """
        pass

    def RemoveFromAllProfileViews(self):
        """ RemoveFromAllProfileViews(self: PressurePart) """
        pass

    def RemoveFromProfileView(self, profileViewId):
        """ RemoveFromProfileView(self: PressurePart, profileViewId: ObjectId) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PressurePart) -> str

"""

    NetworkId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetworkId(self: PressurePart) -> ObjectId

"""

    NetworkName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetworkName(self: PressurePart) -> str

"""

    ParamsBool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsBool(self: PressurePart) -> ParamBoolCollection

"""

    ParamsDouble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsDouble(self: PressurePart) -> ParamDoubleCollection

"""

    ParamsLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsLong(self: PressurePart) -> ParamLongCollection

"""

    ParamsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsString(self: PressurePart) -> ParamStringCollection

"""

    PartDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartDescription(self: PressurePart) -> str

Set: PartDescription(self: PressurePart) = value
"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: PressurePart) -> Point3d

Set: Position(self: PressurePart) = value
"""

    ProfileViewPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewPartId(self: PressurePart) -> ObjectId

"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PressurePart) -> ObjectId

Set: ReferenceAlignmentId(self: PressurePart) = value
"""

    ReferenceAlignmentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentName(self: PressurePart) -> str

"""

    ReferenceSurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceSurfaceId(self: PressurePart) -> ObjectId

Set: ReferenceSurfaceId(self: PressurePart) = value
"""

    ReferenceSurfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceSurfaceName(self: PressurePart) -> str

"""



class PressureAppurtenance(PressurePart):
    # no doc
    def Dispose(self):
        """ Dispose(self: PressurePart, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    InsertionPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPointOffset(self: PressureAppurtenance) -> float

"""

    InsertionPointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPointStation(self: PressureAppurtenance) -> float

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: PressureAppurtenance) -> Point3d

Set: Location(self: PressureAppurtenance) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: PressureAppurtenance) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: PressureAppurtenance) = value
"""



class PressureAppurtenanceLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(appurtenanceId, styleId, ratio, direction):
        """ Create(appurtenanceId: ObjectId, styleId: ObjectId, ratio: float, direction: Vector3d) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(appurtenanceId):
        """ GetAvailableLabelIds(appurtenanceId: ObjectId) -> ObjectIdCollection """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: PressureAppurtenanceLabel) -> Vector3d

Set: Direction(self: PressureAppurtenanceLabel) = value
"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PressureAppurtenanceLabel) -> float

Set: Ratio(self: PressureAppurtenanceLabel) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PressureAppurtenanceLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PressureAppurtenanceLabel) = value
"""


    m_SubData = None


class PressureAppurtenanceProfileLabel(PressurePartProfileLabel):
    # no doc
    @staticmethod
    def Create(profileViewPartId, profileViewId, ratio, direction, labelStyleId):
        """ Create(profileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, direction: Vector3d, labelStyleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(profileViewPartId, profileViewId):
        """ GetAvailableLabelIds(profileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: PressureAppurtenanceProfileLabel) -> Vector3d

Set: Direction(self: PressureAppurtenanceProfileLabel) = value
"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PressureAppurtenanceProfileLabel) -> float

Set: Ratio(self: PressureAppurtenanceProfileLabel) = value
"""


    m_SubData = None


class PressureFitting(PressurePart):
    # no doc
    def Dispose(self):
        """ Dispose(self: PressurePart, A_0: bool) """
        pass

    InsertionPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPointOffset(self: PressureFitting) -> float

"""

    InsertionPointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPointStation(self: PressureFitting) -> float

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: PressureFitting) -> Point3d

Set: Location(self: PressureFitting) = value
"""

    ResultantHorizontalAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultantHorizontalAngle(self: PressureFitting) -> float

"""

    ResultantVerticalAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultantVerticalAngle(self: PressureFitting) -> float

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: PressureFitting) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: PressureFitting) = value
"""



class PressureFittingLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(fittingId, styleId, ratio, direction):
        """ Create(fittingId: ObjectId, styleId: ObjectId, ratio: float, direction: Vector3d) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(fittingId):
        """ GetAvailableLabelIds(fittingId: ObjectId) -> ObjectIdCollection """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: PressureFittingLabel) -> Vector3d

Set: Direction(self: PressureFittingLabel) = value
"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PressureFittingLabel) -> float

Set: Ratio(self: PressureFittingLabel) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PressureFittingLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PressureFittingLabel) = value
"""


    m_SubData = None


class PressureFittingProfileLabel(PressurePartProfileLabel):
    # no doc
    @staticmethod
    def Create(profileViewPartId, profileViewId, ratio, direction, labelStyleId):
        """ Create(profileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, direction: Vector3d, labelStyleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(profileViewPartId, profileViewId):
        """ GetAvailableLabelIds(profileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: PressureFittingProfileLabel) -> Vector3d

Set: Direction(self: PressureFittingProfileLabel) = value
"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PressureFittingProfileLabel) -> float

Set: Ratio(self: PressureFittingProfileLabel) = value
"""


    m_SubData = None


class PressurePartContextType(Enum):
    """ enum PressurePartContextType, values: AppurtIdCoolingMethod (904), AppurtIdPowerRequirement (905), AppurtIdPrimingMethod (906), AppurtIdSize (900), AppurtOutCon1Dia (901), AppurtOutCon2Dia (902), AppurtOutCon3Dia (903), AppurtPrimingRequired (907), AppurtValveActuator (908), CatalogId (700), CompatibleStandard (707), ConnectionPointCount (708), ConnectionPointDeflection (724), ConnectionPointEngagementLength (725), ConnectionPointIdJointEndType (726), ConnectionPointNominalDiameter (727), ConnectionPointOuterDiameter (728), ConnectionPointWallThickness (729), Description (709), DiameterNominal (710), FidManufacturer (711), FittingAngle (850), FittingBranchAngle1 (851), FittingBranchAngle2 (852), FittingCurveRadius (853), FittingCutbackAngle (854), IdCoatingInside (712), IdCoatingOutside (713), IdMaterial (714), IdType (706), IdTypeDescription (730), ModelName (715), PartDomain (702), PartFamilyId (704), PartFamilyName (705), PartType (701), PID (703), PipeCutLength (800), PipeDiameterOutside (802), PipeDiamterInside (801), PipeMinFlexRadius (803), PipeThickness (804), PressureClass (716), PressureMax (717), Schedule (718), Sdr (719), Series (720), StrengthClass (721), ThicknessClass (722), Version (723) """
    AppurtIdCoolingMethod = None
    AppurtIdPowerRequirement = None
    AppurtIdPrimingMethod = None
    AppurtIdSize = None
    AppurtOutCon1Dia = None
    AppurtOutCon2Dia = None
    AppurtOutCon3Dia = None
    AppurtPrimingRequired = None
    AppurtValveActuator = None
    CatalogId = None
    CompatibleStandard = None
    ConnectionPointCount = None
    ConnectionPointDeflection = None
    ConnectionPointEngagementLength = None
    ConnectionPointIdJointEndType = None
    ConnectionPointNominalDiameter = None
    ConnectionPointOuterDiameter = None
    ConnectionPointWallThickness = None
    Description = None
    DiameterNominal = None
    FidManufacturer = None
    FittingAngle = None
    FittingBranchAngle1 = None
    FittingBranchAngle2 = None
    FittingCurveRadius = None
    FittingCutbackAngle = None
    IdCoatingInside = None
    IdCoatingOutside = None
    IdMaterial = None
    IdType = None
    IdTypeDescription = None
    ModelName = None
    PartDomain = None
    PartFamilyId = None
    PartFamilyName = None
    PartType = None
    PID = None
    PipeCutLength = None
    PipeDiameterOutside = None
    PipeDiamterInside = None
    PipeMinFlexRadius = None
    PipeThickness = None
    PressureClass = None
    PressureMax = None
    Schedule = None
    Sdr = None
    Series = None
    StrengthClass = None
    ThicknessClass = None
    value__ = None
    Version = None


class PressurePartDomainType(Enum):
    """ enum PressurePartDomainType, values: Appurtenance (5), Fitting (4), Pipe (1) """
    Appurtenance = None
    Fitting = None
    Pipe = None
    value__ = None


class PressurePartType(Enum):
    """ enum PressurePartType, values: Cap (154), Coupling (155), Cross (153), Elbow (150), Hydrant (202), Plug (156), PressurePipe (14), Pump (201), Reducer (157), Tee (151), Valve (200), Wye (152) """
    Cap = None
    Coupling = None
    Cross = None
    Elbow = None
    Hydrant = None
    Plug = None
    PressurePipe = None
    Pump = None
    Reducer = None
    Tee = None
    value__ = None
    Valve = None
    Wye = None


class PressurePipe(PressurePart):
    # no doc
    def Dispose(self):
        """ Dispose(self: PressurePart, A_0: bool) """
        pass

    Bearing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bearing(self: PressurePipe) -> float

"""

    Bulge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bulge(self: PressurePipe) -> float

"""

    EndElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndElevation(self: PressurePipe) -> float

"""

    EndFittingId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndFittingId(self: PressurePipe) -> ObjectId

"""

    EndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffset(self: PressurePipe) -> float

"""

    EndPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPartId(self: PressurePipe) -> ObjectId

"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: PressurePipe) -> Point3d

Set: EndPoint(self: PressurePipe) = value
"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: PressurePipe) -> float

"""

    InnerDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerDiameter(self: PressurePipe) -> float

"""

    Length2DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2DCenterToCenter(self: PressurePipe) -> float

"""

    Length3DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3DCenterToCenter(self: PressurePipe) -> float

"""

    MaximumCover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumCover(self: PressurePipe) -> float

"""

    MinimumCover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumCover(self: PressurePipe) -> float

"""

    OuterDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterDiameter(self: PressurePipe) -> float

"""

    Slope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slope(self: PressurePipe) -> float

"""

    StartElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartElevation(self: PressurePipe) -> float

"""

    StartFittingId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartFittingId(self: PressurePipe) -> ObjectId

"""

    StartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffset(self: PressurePipe) -> float

"""

    StartPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPartId(self: PressurePipe) -> ObjectId

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: PressurePipe) -> Point3d

Set: StartPoint(self: PressurePipe) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: PressurePipe) -> float

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: PressurePipe) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: PressurePipe) = value
"""

    WallThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallThickness(self: PressurePipe) -> float

"""



class PressurePipeLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(pipeId, ratio, labelStyleId):
        """ Create(pipeId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(pipeId):
        """ GetAvailableLabelIds(pipeId: ObjectId) -> ObjectIdCollection """
        pass

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PressurePipeLabel) -> float

Set: Ratio(self: PressurePipeLabel) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PressurePipeLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PressurePipeLabel) = value
"""


    m_SubData = None


class PressurePipeNetwork(GeoEntity):
    # no doc
    def AddAppurtenance(self, appurtenanceId):
        """ AddAppurtenance(self: PressurePipeNetwork, appurtenanceId: ObjectId) """
        pass

    def AddCurvePipe(self, startPoint, *__args):
        """
        AddCurvePipe(self: PressurePipeNetwork, startPoint: Point3d, startDir: Vector2d, endPoint: Point3d, partSize: PressurePartSize) -> ObjectId
        AddCurvePipe(self: PressurePipeNetwork, startPoint: Point3d, secondPoint: Point3d, endPoint: Point3d, partSize: PressurePartSize) -> ObjectId
        """
        pass

    def AddFitting(self, fittingId):
        """ AddFitting(self: PressurePipeNetwork, fittingId: ObjectId) """
        pass

    def AddLinePipe(self, line, partSize):
        """ AddLinePipe(self: PressurePipeNetwork, line: LineSegment3d, partSize: PressurePartSize) -> ObjectId """
        pass

    def AddPipe(self, pipeId):
        """ AddPipe(self: PressurePipeNetwork, pipeId: ObjectId) """
        pass

    @staticmethod
    def Create(database, networkName):
        """ Create(database: Database, networkName: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAppurtenanceIds(self):
        """ GetAppurtenanceIds(self: PressurePipeNetwork) -> ObjectIdCollection """
        pass

    def GetFittingIds(self):
        """ GetFittingIds(self: PressurePipeNetwork) -> ObjectIdCollection """
        pass

    def GetPipeIds(self):
        """ GetPipeIds(self: PressurePipeNetwork) -> ObjectIdCollection """
        pass

    AppurtenanceNameTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenanceNameTemplate(self: PressurePipeNetwork) -> str

Set: AppurtenanceNameTemplate(self: PressurePipeNetwork) = value
"""

    AppurtenancePlanLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenancePlanLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: AppurtenancePlanLabelStyleId(self: PressurePipeNetwork) = value
"""

    AppurtenancePlanLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenancePlanLabelStyleName(self: PressurePipeNetwork) -> str

Set: AppurtenancePlanLabelStyleName(self: PressurePipeNetwork) = value
"""

    AppurtenancePlanLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenancePlanLayerId(self: PressurePipeNetwork) -> ObjectId

Set: AppurtenancePlanLayerId(self: PressurePipeNetwork) = value
"""

    AppurtenancePlanLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenancePlanLayerName(self: PressurePipeNetwork) -> str

Set: AppurtenancePlanLayerName(self: PressurePipeNetwork) = value
"""

    AppurtenanceProfileLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenanceProfileLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: AppurtenanceProfileLabelStyleId(self: PressurePipeNetwork) = value
"""

    AppurtenanceProfileLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenanceProfileLabelStyleName(self: PressurePipeNetwork) -> str

Set: AppurtenanceProfileLabelStyleName(self: PressurePipeNetwork) = value
"""

    AppurtenanceProfileLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenanceProfileLayerId(self: PressurePipeNetwork) -> ObjectId

Set: AppurtenanceProfileLayerId(self: PressurePipeNetwork) = value
"""

    AppurtenanceProfileLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenanceProfileLayerName(self: PressurePipeNetwork) -> str

Set: AppurtenanceProfileLayerName(self: PressurePipeNetwork) = value
"""

    CrossingPressurePipeProfileLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingPressurePipeProfileLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: CrossingPressurePipeProfileLabelStyleId(self: PressurePipeNetwork) = value
"""

    CrossingPressurePipeProfileLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingPressurePipeProfileLabelStyleName(self: PressurePipeNetwork) -> str

Set: CrossingPressurePipeProfileLabelStyleName(self: PressurePipeNetwork) = value
"""

    CurrentPartListId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPartListId(self: PressurePipeNetwork) -> ObjectId

Set: CurrentPartListId(self: PressurePipeNetwork) = value
"""

    FittingNameTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingNameTemplate(self: PressurePipeNetwork) -> str

Set: FittingNameTemplate(self: PressurePipeNetwork) = value
"""

    FittingPlanLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingPlanLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: FittingPlanLabelStyleId(self: PressurePipeNetwork) = value
"""

    FittingPlanLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingPlanLabelStyleName(self: PressurePipeNetwork) -> str

Set: FittingPlanLabelStyleName(self: PressurePipeNetwork) = value
"""

    FittingPlanLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingPlanLayerId(self: PressurePipeNetwork) -> ObjectId

Set: FittingPlanLayerId(self: PressurePipeNetwork) = value
"""

    FittingPlanLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingPlanLayerName(self: PressurePipeNetwork) -> str

Set: FittingPlanLayerName(self: PressurePipeNetwork) = value
"""

    FittingProfileLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingProfileLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: FittingProfileLabelStyleId(self: PressurePipeNetwork) = value
"""

    FittingProfileLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingProfileLabelStyleName(self: PressurePipeNetwork) -> str

Set: FittingProfileLabelStyleName(self: PressurePipeNetwork) = value
"""

    FittingProfileLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingProfileLayerId(self: PressurePipeNetwork) -> ObjectId

Set: FittingProfileLayerId(self: PressurePipeNetwork) = value
"""

    FittingProfileLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingProfileLayerName(self: PressurePipeNetwork) -> str

Set: FittingProfileLayerName(self: PressurePipeNetwork) = value
"""

    HasPipeRun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPipeRun(self: PressurePipeNetwork) -> bool

"""

    IsEmpty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEmpty(self: PressurePipeNetwork) -> bool

"""

    MaximumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumElevation(self: PressurePipeNetwork) -> float

"""

    MinimumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumElevation(self: PressurePipeNetwork) -> float

"""

    PipeNameTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeNameTemplate(self: PressurePipeNetwork) -> str

Set: PipeNameTemplate(self: PressurePipeNetwork) = value
"""

    PipePlanLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: PipePlanLabelStyleId(self: PressurePipeNetwork) = value
"""

    PipePlanLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLabelStyleName(self: PressurePipeNetwork) -> str

Set: PipePlanLabelStyleName(self: PressurePipeNetwork) = value
"""

    PipePlanLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLayerId(self: PressurePipeNetwork) -> ObjectId

Set: PipePlanLayerId(self: PressurePipeNetwork) = value
"""

    PipePlanLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipePlanLayerName(self: PressurePipeNetwork) -> str

Set: PipePlanLayerName(self: PressurePipeNetwork) = value
"""

    PipeProfileLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: PipeProfileLabelStyleId(self: PressurePipeNetwork) = value
"""

    PipeProfileLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLabelStyleName(self: PressurePipeNetwork) -> str

Set: PipeProfileLabelStyleName(self: PressurePipeNetwork) = value
"""

    PipeProfileLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLayerId(self: PressurePipeNetwork) -> ObjectId

Set: PipeProfileLayerId(self: PressurePipeNetwork) = value
"""

    PipeProfileLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeProfileLayerName(self: PressurePipeNetwork) -> str

Set: PipeProfileLayerName(self: PressurePipeNetwork) = value
"""

    PipeRunNameTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeRunNameTemplate(self: PressurePipeNetwork) -> str

Set: PipeRunNameTemplate(self: PressurePipeNetwork) = value
"""

    PipeRuns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeRuns(self: PressurePipeNetwork) -> PressurePipeRunCollection

"""

    PipeSectionLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeSectionLabelStyleId(self: PressurePipeNetwork) -> ObjectId

Set: PipeSectionLabelStyleId(self: PressurePipeNetwork) = value
"""

    PipeSectionLabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeSectionLabelStyleName(self: PressurePipeNetwork) -> str

Set: PipeSectionLabelStyleName(self: PressurePipeNetwork) = value
"""

    PipeSectionLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeSectionLayerId(self: PressurePipeNetwork) -> ObjectId

Set: PipeSectionLayerId(self: PressurePipeNetwork) = value
"""

    PipeSectionLayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeSectionLayerName(self: PressurePipeNetwork) -> str

Set: PipeSectionLayerName(self: PressurePipeNetwork) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PressurePipeNetwork) -> ObjectId

Set: ReferenceAlignmentId(self: PressurePipeNetwork) = value
"""

    ReferenceAlignmentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentName(self: PressurePipeNetwork) -> str

Set: ReferenceAlignmentName(self: PressurePipeNetwork) = value
"""

    ReferenceSurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceSurfaceId(self: PressurePipeNetwork) -> ObjectId

Set: ReferenceSurfaceId(self: PressurePipeNetwork) = value
"""

    ReferenceSurfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceSurfaceName(self: PressurePipeNetwork) -> str

Set: ReferenceSurfaceName(self: PressurePipeNetwork) = value
"""



class PressurePipeProfileLabel(PressurePartProfileLabel):
    # no doc
    @staticmethod
    def Create(profileViewPartId, profileViewId, ratio, labelStyleId):
        """ Create(profileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(profileViewPartId, profileViewId):
        """ GetAvailableLabelIds(profileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PressurePipeProfileLabel) -> float

Set: Ratio(self: PressurePipeProfileLabel) = value
"""


    m_SubData = None


class PressurePipeRun(object):
    # no doc
    def GetPartIds(self):
        """ GetPartIds(self: PressurePipeRun) -> ObjectIdCollection """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: PressurePipeRun) -> ObjectId

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PressurePipeRun) -> str

Set: Name(self: PressurePipeRun) = value
"""



class PressurePipeRunCollection(object):
    # no doc
    def createPipeRun(self, name, path, partSize, depthOfCover, autoAddBends):
        """ createPipeRun(self: PressurePipeRunCollection, name: str, path: Polyline, partSize: PressurePartSize, depthOfCover: float, autoAddBends: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: PressurePipeRunCollection) -> IEnumerator[PressurePipeRun] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: PressurePipeRunCollection) -> IEnumerator """
        pass

    def Remove(self, pipeRun, includeParts):
        """ Remove(self: PressurePipeRunCollection, pipeRun: PressurePipeRun, includeParts: bool) """
        pass

    def RemoveAt(self, index, includeParts):
        """ RemoveAt(self: PressurePipeRunCollection, index: int, includeParts: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PressurePipeRun](enumerable: IEnumerable[PressurePipeRun], value: PressurePipeRun) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PressurePipeRunCollection) -> int

"""



class PressurePipeSectionLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(sectionViewId, pipeId, sectionNetworkId, partIndex, ratio, direction, *__args):
        """
        Create(sectionViewId: ObjectId, pipeId: ObjectId, sectionNetworkId: ObjectId, partIndex: int, ratio: float, direction: Vector3d, labelStyleId: ObjectId, dimOpt: DimensionAnchorOptionType, dimVal: float) -> ObjectId
        Create(sectionViewId: ObjectId, pipeId: ObjectId, sectionNetworkId: ObjectId, partIndex: int, ratio: float, direction: Vector3d, dimOpt: DimensionAnchorOptionType, dimVal: float) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(sectionViewId, pipeId, sectionNetworkId):
        """ GetAvailableLabelIds(sectionViewId: ObjectId, pipeId: ObjectId, sectionNetworkId: ObjectId) -> ObjectIdCollection """
        pass

    def getIntersectionCount(self, *args): #cannot find CLR method
        """ getIntersectionCount(oidPart: AcDbObjectId, oidSectionPipeNetwork: AcDbObjectId) -> int """
        pass

    def isNetworkPartTheSourceOfSectionPressurePipeNetwork(self, *args): #cannot find CLR method
        """ isNetworkPartTheSourceOfSectionPressurePipeNetwork(oidPart: AcDbObjectId, oidSectionPipeNetwork: AcDbObjectId) -> bool """
        pass

    def isSectionViewContainSectionPressurePipeNetowrk(self, *args): #cannot find CLR method
        """ isSectionViewContainSectionPressurePipeNetowrk(oidPart: AcDbObjectId, oidSectionView: AcDbObjectId) -> bool """
        pass

    def isSectionViewDrawSectionPressurePipeNetwork(self, *args): #cannot find CLR method
        """ isSectionViewDrawSectionPressurePipeNetwork(oidPart: AcDbObjectId, oidSectionView: AcDbObjectId) -> bool """
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: PressurePipeSectionLabel) -> Vector3d

Set: Direction(self: PressurePipeSectionLabel) = value
"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: PressurePipeSectionLabel) -> float

Set: Ratio(self: PressurePipeSectionLabel) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: PressurePipeSectionLabel) -> ObjectId

Set: ReferenceAlignmentId(self: PressurePipeSectionLabel) = value
"""


    m_SubData = None


class Profile(Feature):
    # no doc
    @staticmethod
    def CreateByLayout(profileName, *__args):
        """
        CreateByLayout(profileName: str, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId
        CreateByLayout(profileName: str, document: CivilDocument, alignmentName: str, layerName: str, styleName: str, labelSetName: str) -> ObjectId
        """
        pass

    @staticmethod
    def CreateFromFeatureLine(profileName, corridorFeatureLine, alignmentId, layerId, styleId, labelSetId):
        """ CreateFromFeatureLine(profileName: str, corridorFeatureLine: CorridorFeatureLine, alignmentId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def CreateFromSurface(profileName, *__args):
        """
        CreateFromSurface(profileName: str, alignmentId: ObjectId, surfaceId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId) -> ObjectId
        CreateFromSurface(profileName: str, alignmentId: ObjectId, surfaceId: ObjectId, layerId: ObjectId, styleId: ObjectId, labelSetId: ObjectId, offset: float, sampleStart: float, sampleEnd: float) -> ObjectId
        CreateFromSurface(profileName: str, document: CivilDocument, alignmentName: str, surfaceName: str, layerName: str, styleName: str, labelSetName: str) -> ObjectId
        CreateFromSurface(profileName: str, document: CivilDocument, alignmentName: str, surfaceName: str, layerName: str, styleName: str, labelSetName: str, offset: float, sampleStart: float, sampleEnd: float) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def ElevationAt(self, station):
        """ ElevationAt(self: Profile, station: float) -> float """
        pass

    def GradeAt(self, station):
        """ GradeAt(self: Profile, station: float) -> float """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: Profile) -> ObjectId

"""

    DataSourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataSourceId(self: Profile) -> ObjectId

"""

    DataSourceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataSourceName(self: Profile) -> str

"""

    DesignCheckSetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignCheckSetId(self: Profile) -> ObjectId

Set: DesignCheckSetId(self: Profile) = value
"""

    DesignCheckSetName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignCheckSetName(self: Profile) -> str

Set: DesignCheckSetName(self: Profile) = value
"""

    DesignSpeedBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignSpeedBased(self: Profile) -> bool

Set: DesignSpeedBased(self: Profile) = value
"""

    ElevationMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationMax(self: Profile) -> float

"""

    ElevationMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationMin(self: Profile) -> float

"""

    EndingStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndingStation(self: Profile) -> float

"""

    Entities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entities(self: Profile) -> ProfileEntityCollection

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Profile) -> float

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: Profile) -> float

"""

    Plinegen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plinegen(self: Profile) -> bool

Set: Plinegen(self: Profile) = value
"""

    ProfileType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileType(self: Profile) -> ProfileType

"""

    PVIs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIs(self: Profile) -> ProfilePVICollection

"""

    StartingStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartingStation(self: Profile) -> float

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Profile) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: Profile) = value
"""

    UpdateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateMode(self: Profile) -> ProfileUpdateType

Set: UpdateMode(self: Profile) = value
"""

    UseDesignCheckSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDesignCheckSet(self: Profile) -> bool

Set: UseDesignCheckSet(self: Profile) = value
"""

    UseDesignCriteriaFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDesignCriteriaFile(self: Profile) -> bool

Set: UseDesignCriteriaFile(self: Profile) = value
"""



class ProfileEntity(CivilWrapper<AeccDbVAlignment>):
    # no doc
    def DesignChecks(self):
        """ DesignChecks(self: ProfileEntity) -> Array[ProfileDesignCheck] """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    def InternalGetProfileEntityAttributeDouble(self, *args): #cannot find CLR method
        """ InternalGetProfileEntityAttributeDouble(self: ProfileEntity, attributeId: UInt32) -> float """
        pass

    def InternalPutProfileEntityAttributeDouble(self, *args): #cannot find CLR method
        """ InternalPutProfileEntityAttributeDouble(self: ProfileEntity, attributeId: UInt32, newValue: float) """
        pass

    def ValidateDesignCheck(self, designCheck, curveType):
        """ ValidateDesignCheck(self: ProfileEntity, designCheck: ProfileDesignCheck, curveType: ProfileApplyCurveType) -> bool """
        pass

    Constraint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint1(self: ProfileEntity) -> ProfileEntityConstraintType

"""

    Constraint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint2(self: ProfileEntity) -> EntityVerticalConstraintType

"""

    EndElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndElevation(self: ProfileEntity) -> float

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: ProfileEntity) -> float

"""

    EntityAfter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityAfter(self: ProfileEntity) -> UInt32

"""

    EntityBefore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityBefore(self: ProfileEntity) -> UInt32

"""

    EntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityId(self: ProfileEntity) -> UInt32

"""

    EntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityType(self: ProfileEntity) -> ProfileEntityType

"""

    HighestDesignSpeed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighestDesignSpeed(self: ProfileEntity) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: ProfileEntity) -> float

Set: Length(self: ProfileEntity) = value
"""

    MinimumKValueHSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumKValueHSD(self: ProfileEntity) -> float

"""

    MinimumKValuePSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumKValuePSD(self: ProfileEntity) -> float

"""

    MinimumKValueSSD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumKValueSSD(self: ProfileEntity) -> float

"""

    StartElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartElevation(self: ProfileEntity) -> float

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: ProfileEntity) -> float

"""



class ProfileCircular(ProfileEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    CurveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveType(self: ProfileCircular) -> VerticalCurveType

"""

    EntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityType(self: ProfileCircular) -> ProfileEntityType

"""

    GradeChange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeChange(self: ProfileCircular) -> float

"""

    GradeIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeIn(self: ProfileCircular) -> float

"""

    GradeOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeOut(self: ProfileCircular) -> float

"""

    HighLowPointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighLowPointElevation(self: ProfileCircular) -> float

"""

    HighLowPointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighLowPointStation(self: ProfileCircular) -> float

"""

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: K(self: ProfileCircular) -> float

Set: K(self: ProfileCircular) = value
"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: ProfileCircular) -> float

"""

    PVIElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIElevation(self: ProfileCircular) -> float

"""

    PVIStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIStation(self: ProfileCircular) -> float

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: ProfileCircular) -> float

Set: Radius(self: ProfileCircular) = value
"""

    TangentOffsetAtPVI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentOffsetAtPVI(self: ProfileCircular) -> float

"""



class ProfileLabelGroup(AutoFeatureLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(runtimeClass, profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroupIds(runtimeClass: RXClass, profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(runtimeClass, profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(runtimeClass: RXClass, profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    def IsProfileInProfileView(self, *args): #cannot find CLR method
        """ IsProfileInProfileView(profileId: ObjectId, profileViewId: ObjectId) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class ProfileCrestCurveLabelGroup(ProfileLabelGroup):
    # no doc
    @staticmethod
    def Create(profileViewId, profileId, styleId):
        """ Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId, profileId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class ProfileCriteria(CivilWrapper<AeccDbGraphProfile>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphProfile>, A_0: bool) """
        pass

    BoundaryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryType(self: ProfileCriteria) -> HatchCriteriaBoundaryType

"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: ProfileCriteria) -> ObjectId

Set: ProfileId(self: ProfileCriteria) = value
"""

    ProfileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileName(self: ProfileCriteria) -> str

Set: ProfileName(self: ProfileCriteria) = value
"""



class ProfileCriteriaCollection(CivilWrapper<AeccDbGraphProfile>):
    # no doc
    def Add(self, profileId, type):
        """ Add(self: ProfileCriteriaCollection, profileId: ObjectId, type: HatchCriteriaBoundaryType) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphProfile>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileCriteriaCollection) -> IEnumerator[ProfileCriteria] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfileCriteriaCollection) -> IEnumerator """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ProfileCriteriaCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfileCriteria](enumerable: IEnumerable[ProfileCriteria], value: ProfileCriteria) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ProfileCriteriaCollection) -> int

"""



class ProfileProjection(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class ProfileCrossing(ProfileProjection):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class ProfileDataBandLabelGroup(ProfileBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class ProfileEntityCollection(CivilWrapper<AeccDbVAlignment>):
    # no doc
    def AddFixedSymmetricParabolaByEntityEndAndThroughPoint(self, attachEntityId, passPoint):
        """
        AddFixedSymmetricParabolaByEntityEndAndThroughPoint(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point2d) -> ProfileParabolaSymmetric
        AddFixedSymmetricParabolaByEntityEndAndThroughPoint(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point3d) -> ProfileParabolaSymmetric
        """
        pass

    def AddFixedSymmetricParabolaByThreePoints(self, point, point2, point3):
        """
        AddFixedSymmetricParabolaByThreePoints(self: ProfileEntityCollection, point: Point2d, point2: Point2d, point3: Point2d) -> ProfileParabolaSymmetric
        AddFixedSymmetricParabolaByThreePoints(self: ProfileEntityCollection, point: Point3d, point2: Point3d, point3: Point3d) -> ProfileParabolaSymmetric
        """
        pass

    def AddFixedSymmetricParabolaByTwoPointsAndEndGrade(self, point1, point2, endGrade):
        """
        AddFixedSymmetricParabolaByTwoPointsAndEndGrade(self: ProfileEntityCollection, point1: Point2d, point2: Point2d, endGrade: float) -> ProfileParabolaSymmetric
        AddFixedSymmetricParabolaByTwoPointsAndEndGrade(self: ProfileEntityCollection, point1: Point3d, point2: Point3d, endGrade: float) -> ProfileParabolaSymmetric
        """
        pass

    def AddFixedSymmetricParabolaByTwoPointsAndK(self, point1, point2, curveType, k):
        """
        AddFixedSymmetricParabolaByTwoPointsAndK(self: ProfileEntityCollection, point1: Point2d, point2: Point2d, curveType: VerticalCurveType, k: float) -> ProfileParabolaSymmetric
        AddFixedSymmetricParabolaByTwoPointsAndK(self: ProfileEntityCollection, point1: Point3d, point2: Point3d, curveType: VerticalCurveType, k: float) -> ProfileParabolaSymmetric
        """
        pass

    def AddFixedSymmetricParabolaByTwoPointsAndRadius(self, point1, point2, curType, radius):
        """
        AddFixedSymmetricParabolaByTwoPointsAndRadius(self: ProfileEntityCollection, point1: Point2d, point2: Point2d, curType: VerticalCurveType, radius: float) -> ProfileParabolaSymmetric
        AddFixedSymmetricParabolaByTwoPointsAndRadius(self: ProfileEntityCollection, point1: Point3d, point2: Point3d, curType: VerticalCurveType, radius: float) -> ProfileParabolaSymmetric
        """
        pass

    def AddFixedSymmetricParabolaByTwoPointsAndStartGrade(self, point1, point2, startGrade):
        """
        AddFixedSymmetricParabolaByTwoPointsAndStartGrade(self: ProfileEntityCollection, point1: Point2d, point2: Point2d, startGrade: float) -> ProfileParabolaSymmetric
        AddFixedSymmetricParabolaByTwoPointsAndStartGrade(self: ProfileEntityCollection, point1: Point3d, point2: Point3d, startGrade: float) -> ProfileParabolaSymmetric
        """
        pass

    def AddFixedTangent(self, startPoint, endPoint):
        """
        AddFixedTangent(self: ProfileEntityCollection, startPoint: Point2d, endPoint: Point2d) -> ProfileTangent
        AddFixedTangent(self: ProfileEntityCollection, startPoint: Point3d, endPoint: Point3d) -> ProfileTangent
        """
        pass

    def AddFixedTangentWithPreviousEntity(self, previousEntityId, startPoint, endPoint):
        """
        AddFixedTangentWithPreviousEntity(self: ProfileEntityCollection, previousEntityId: UInt32, startPoint: Point2d, endPoint: Point2d) -> ProfileTangent
        AddFixedTangentWithPreviousEntity(self: ProfileEntityCollection, previousEntityId: UInt32, startPoint: Point3d, endPoint: Point3d) -> ProfileTangent
        """
        pass

    def AddFloatingSymmetricParabolaByThroughPointAndGrade(self, attachEntityId, passPoint, grade, attachType):
        """
        AddFloatingSymmetricParabolaByThroughPointAndGrade(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point2d, grade: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric
        AddFloatingSymmetricParabolaByThroughPointAndGrade(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point3d, grade: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric
        """
        pass

    def AddFloatingSymmetricParabolaByThroughPointAndK(self, attachEntityId, passPoint, k, attachType):
        """
        AddFloatingSymmetricParabolaByThroughPointAndK(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point2d, k: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric
        AddFloatingSymmetricParabolaByThroughPointAndK(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point3d, k: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric
        """
        pass

    def AddFloatingSymmetricParabolaByThroughPointAndRadius(self, attachEntityId, passPoint, radius, attachType):
        """
        AddFloatingSymmetricParabolaByThroughPointAndRadius(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point2d, radius: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric
        AddFloatingSymmetricParabolaByThroughPointAndRadius(self: ProfileEntityCollection, attachEntityId: UInt32, passPoint: Point3d, radius: float, attachType: EntityAttachType) -> ProfileParabolaSymmetric
        """
        pass

    def AddFloatingTangent(self, entityId, passPoint, attachType):
        """
        AddFloatingTangent(self: ProfileEntityCollection, entityId: UInt32, passPoint: Point2d, attachType: EntityAttachType) -> ProfileTangent
        AddFloatingTangent(self: ProfileEntityCollection, entityId: UInt32, passPoint: Point3d, attachType: EntityAttachType) -> ProfileTangent
        """
        pass

    def AddFreeAsymmetricParabolaByPVIAndLengths(self, attachProfilePVI, length1, length2):
        """ AddFreeAsymmetricParabolaByPVIAndLengths(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, length1: float, length2: float) -> ProfileParabolaAsymmetric """
        pass

    def AddFreeCircularCurveByPVIAndLength(self, attachProfilePVI, length):
        """ AddFreeCircularCurveByPVIAndLength(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, length: float) -> ProfileCircular """
        pass

    def AddFreeCircularCurveByPVIAndRadius(self, attachProfilePVI, radius):
        """ AddFreeCircularCurveByPVIAndRadius(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, radius: float) -> ProfileCircular """
        pass

    def AddFreeCircularCurveByPVIAndThroughPoint(self, attachProfilePVI, passPoint):
        """
        AddFreeCircularCurveByPVIAndThroughPoint(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, passPoint: Point2d) -> ProfileCircular
        AddFreeCircularCurveByPVIAndThroughPoint(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, passPoint: Point3d) -> ProfileCircular
        """
        pass

    def AddFreeSymmetricParabolaByK(self, previousEntityId, nextEntityId, curveType, k):
        """ AddFreeSymmetricParabolaByK(self: ProfileEntityCollection, previousEntityId: UInt32, nextEntityId: UInt32, curveType: VerticalCurveType, k: float) -> ProfileParabolaSymmetric """
        pass

    def AddFreeSymmetricParabolaByLength(self, previousEntityId, nextEntityId, curveType, length, preferFlat):
        """ AddFreeSymmetricParabolaByLength(self: ProfileEntityCollection, previousEntityId: UInt32, nextEntityId: UInt32, curveType: VerticalCurveType, length: float, preferFlat: bool) -> ProfileParabolaSymmetric """
        pass

    def AddFreeSymmetricParabolaByPVIAndCurveLength(self, attachProfilePVI, curveLength):
        """ AddFreeSymmetricParabolaByPVIAndCurveLength(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, curveLength: float) -> ProfileParabolaSymmetric """
        pass

    def AddFreeSymmetricParabolaByPVIAndK(self, attachProfilePVI, k):
        """ AddFreeSymmetricParabolaByPVIAndK(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, k: float) -> ProfileParabolaSymmetric """
        pass

    def AddFreeSymmetricParabolaByPVIAndThroughPoint(self, attachProfilePVI, passPoint):
        """
        AddFreeSymmetricParabolaByPVIAndThroughPoint(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, passPoint: Point2d) -> ProfileParabolaSymmetric
        AddFreeSymmetricParabolaByPVIAndThroughPoint(self: ProfileEntityCollection, attachProfilePVI: ProfilePVI, passPoint: Point3d) -> ProfileParabolaSymmetric
        """
        pass

    def AddFreeSymmetricParabolaByRadius(self, previousEntityId, nextEntityId, curveType, radius):
        """ AddFreeSymmetricParabolaByRadius(self: ProfileEntityCollection, previousEntityId: UInt32, nextEntityId: UInt32, curveType: VerticalCurveType, radius: float) -> ProfileParabolaSymmetric """
        pass

    def AddFreeTangent(self, previousEntityId, nextEntityId):
        """ AddFreeTangent(self: ProfileEntityCollection, previousEntityId: UInt32, nextEntityId: UInt32) -> ProfileTangent """
        pass

    def Clear(self):
        """ Clear(self: ProfileEntityCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    def EntityAtId(self, id):
        """ EntityAtId(self: ProfileEntityCollection, id: UInt32) -> ProfileEntity """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileEntityCollection) -> IEnumerator[ProfileEntity] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfileEntityCollection) -> IEnumerator """
        pass

    def Remove(self, entity):
        """ Remove(self: ProfileEntityCollection, entity: ProfileEntity) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ProfileEntityCollection, index: int) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfileEntity](enumerable: IEnumerable[ProfileEntity], value: ProfileEntity) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ProfileEntityCollection) -> int

"""

    FirstEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstEntity(self: ProfileEntityCollection) -> UInt32

"""

    LastEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastEntity(self: ProfileEntityCollection) -> UInt32

"""



class ProfileEntityConstraintType(Enum):
    """ enum ProfileEntityConstraintType, values: Fixed (289), FloatOnNext (291), FloatOnPrev (290), Free (292) """
    Fixed = None
    FloatOnNext = None
    FloatOnPrev = None
    Free = None
    value__ = None


class ProfileEntityType(Enum):
    """ enum ProfileEntityType, values: Circular (258), None (262), ParabolaAsymmetric (260), ParabolaSymmetric (259), Tangent (257) """
    Circular = None
    None = None
    ParabolaAsymmetric = None
    ParabolaSymmetric = None
    Tangent = None
    value__ = None


class ProfileHatchArea(CivilWrapper<AeccDbGraphProfile>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphProfile>, A_0: bool) """
        pass

    Criteria = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Criteria(self: ProfileHatchArea) -> ProfileCriteriaCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ProfileHatchArea) -> str

Set: Name(self: ProfileHatchArea) = value
"""

    ShapeStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeStyleId(self: ProfileHatchArea) -> ObjectId

Set: ShapeStyleId(self: ProfileHatchArea) = value
"""

    ShapeStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeStyleName(self: ProfileHatchArea) -> str

Set: ShapeStyleName(self: ProfileHatchArea) = value
"""



class ProfileHatchAreaCollection(CivilWrapper<AeccDbGraphProfile>):
    # no doc
    def Add(self, hatchAreaName, upperProfileId, lowerProfileId, shapeStyleId):
        """ Add(self: ProfileHatchAreaCollection, hatchAreaName: str, upperProfileId: ObjectId, lowerProfileId: ObjectId, shapeStyleId: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphProfile>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileHatchAreaCollection) -> IEnumerator[ProfileHatchArea] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfileHatchAreaCollection) -> IEnumerator """
        pass

    def Remove(self, hatchAreaName):
        """ Remove(self: ProfileHatchAreaCollection, hatchAreaName: str) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfileHatchArea](enumerable: IEnumerable[ProfileHatchArea], value: ProfileHatchArea) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ProfileHatchAreaCollection) -> int

"""



class ProfileHorizontalGeometryPointLabelGroup(ProfileLabelGroup):
    # no doc
    @staticmethod
    def Create(profileViewId, profileId, styleId):
        """ Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId, profileId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    def GetGeometryPointsOptions(self):
        """ GetGeometryPointsOptions(self: ProfileHorizontalGeometryPointLabelGroup) -> GeometryPointSelector[AlignmentPointType] """
        pass

    def SetGeometryPointsOptions(self, profileGeometryPoints):
        """ SetGeometryPointsOptions(self: ProfileHorizontalGeometryPointLabelGroup, profileGeometryPoints: GeometryPointSelector[AlignmentPointType]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    StaggerLineHeight1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight1(self: ProfileHorizontalGeometryPointLabelGroup) -> float

Set: StaggerLineHeight1(self: ProfileHorizontalGeometryPointLabelGroup) = value
"""

    StaggerLineHeight2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight2(self: ProfileHorizontalGeometryPointLabelGroup) -> float

Set: StaggerLineHeight2(self: ProfileHorizontalGeometryPointLabelGroup) = value
"""


    m_SubData = None


class ProfileLineLabelGroup(ProfileLabelGroup):
    # no doc
    @staticmethod
    def Create(profileViewId, profileId, styleId):
        """ Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId, profileId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Weeding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weeding(self: ProfileLineLabelGroup) -> float

Set: Weeding(self: ProfileLineLabelGroup) = value
"""


    m_SubData = None


class ProfileStationLabelGroup(ProfileLabelGroup):
    # no doc
    @staticmethod
    def Create(profileViewId, profileId, styleId, increment):
        """ Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId, increment: float) -> ObjectId """
        pass

    @staticmethod
    def CreateMajor(profileViewId, profileId, styleId, increment):
        """ CreateMajor(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId, increment: float) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: ProfileStationLabelGroup) -> float

Set: Increment(self: ProfileStationLabelGroup) = value
"""

    StaggerLineHeight1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight1(self: ProfileStationLabelGroup) -> float

Set: StaggerLineHeight1(self: ProfileStationLabelGroup) = value
"""

    StaggerLineHeight2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight2(self: ProfileStationLabelGroup) -> float

Set: StaggerLineHeight2(self: ProfileStationLabelGroup) = value
"""


    m_SubData = None


class ProfileMinorStationLabelGroup(ProfileStationLabelGroup):
    # no doc
    @staticmethod
    def Create(styleId, majorStationLabelGroupId, increment):
        """ Create(styleId: ObjectId, majorStationLabelGroupId: ObjectId, increment: float) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId, profileId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    MajorStationLabelGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorStationLabelGroup(self: ProfileMinorStationLabelGroup) -> ObjectId

Set: MajorStationLabelGroup(self: ProfileMinorStationLabelGroup) = value
"""


    m_SubData = None


class ProfileOverride(GraphOverride):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverride, A_0: bool) """
        pass

    def GetLabelGroupIds(self):
        """ GetLabelGroupIds(self: ProfileOverride) -> ObjectIdCollection """
        pass

    def GetProfileLabelGroupIds(self):
        """ GetProfileLabelGroupIds(self: ProfileOverride) -> ObjectIdCollection """
        pass

    OverrideStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleId(self: ProfileOverride) = value
"""

    OverrideStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleName(self: ProfileOverride) = value
"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: ProfileOverride) -> ObjectId

"""

    ProfileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileName(self: ProfileOverride) -> str

"""


    m_pDataLineId = None


class ProfileOverrideCollection(GraphOverrideCollection[ProfileOverride]):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverrideCollection[ProfileOverride], A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileOverrideCollection) -> IEnumerator[ProfileOverride] """
        pass

    SplitAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitAt(self: ProfileOverrideCollection) -> str

Set: SplitAt(self: ProfileOverrideCollection) = value
"""


    m_dataVector = None


class ProfileParabolaAsymmetric(ProfileEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    AsymmetricLength1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AsymmetricLength1(self: ProfileParabolaAsymmetric) -> float

Set: AsymmetricLength1(self: ProfileParabolaAsymmetric) = value
"""

    AsymmetricLength2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AsymmetricLength2(self: ProfileParabolaAsymmetric) -> float

Set: AsymmetricLength2(self: ProfileParabolaAsymmetric) = value
"""

    CurveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveType(self: ProfileParabolaAsymmetric) -> VerticalCurveType

"""

    EntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityType(self: ProfileParabolaAsymmetric) -> ProfileEntityType

"""

    GradeChange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeChange(self: ProfileParabolaAsymmetric) -> float

"""

    GradeIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeIn(self: ProfileParabolaAsymmetric) -> float

"""

    GradeOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeOut(self: ProfileParabolaAsymmetric) -> float

"""

    HighLowPointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighLowPointElevation(self: ProfileParabolaAsymmetric) -> float

"""

    HighLowPointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighLowPointStation(self: ProfileParabolaAsymmetric) -> float

"""

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: K(self: ProfileParabolaAsymmetric) -> float

Set: K(self: ProfileParabolaAsymmetric) = value
"""

    PVIElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIElevation(self: ProfileParabolaAsymmetric) -> float

"""

    PVIStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIStation(self: ProfileParabolaAsymmetric) -> float

"""

    TangentOffsetAtPVI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentOffsetAtPVI(self: ProfileParabolaAsymmetric) -> float

"""



class ProfileParabolaSymmetric(ProfileEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    def GetHeadlightSightDistance(self, maxAngle, headlightHeight):
        """ GetHeadlightSightDistance(self: ProfileParabolaSymmetric, maxAngle: float, headlightHeight: float) -> float """
        pass

    def GetPassingSightDistance(self, eyeHeight, objectHeight):
        """ GetPassingSightDistance(self: ProfileParabolaSymmetric, eyeHeight: float, objectHeight: float) -> float """
        pass

    def GetStoppingSightDistance(self, eyeHeight, objectHeight):
        """ GetStoppingSightDistance(self: ProfileParabolaSymmetric, eyeHeight: float, objectHeight: float) -> float """
        pass

    def SetHeadlightSightDistance(self, maxAngle, headlightHeight, distance):
        """ SetHeadlightSightDistance(self: ProfileParabolaSymmetric, maxAngle: float, headlightHeight: float, distance: float) """
        pass

    def SetPassingSightDistance(self, eyeHeight, objectHeight, distance):
        """ SetPassingSightDistance(self: ProfileParabolaSymmetric, eyeHeight: float, objectHeight: float, distance: float) """
        pass

    def SetStoppingSightDistance(self, eyeHeight, objectHeight, distance):
        """ SetStoppingSightDistance(self: ProfileParabolaSymmetric, eyeHeight: float, objectHeight: float, distance: float) """
        pass

    CurveType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveType(self: ProfileParabolaSymmetric) -> VerticalCurveType

"""

    EntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityType(self: ProfileParabolaSymmetric) -> ProfileEntityType

"""

    GradeAtThroughPoint1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeAtThroughPoint1(self: ProfileParabolaSymmetric) -> float

Set: GradeAtThroughPoint1(self: ProfileParabolaSymmetric) = value
"""

    GradeAtThroughPoint2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeAtThroughPoint2(self: ProfileParabolaSymmetric) -> float

Set: GradeAtThroughPoint2(self: ProfileParabolaSymmetric) = value
"""

    GradeChange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeChange(self: ProfileParabolaSymmetric) -> float

"""

    GradeIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeIn(self: ProfileParabolaSymmetric) -> float

"""

    GradeOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeOut(self: ProfileParabolaSymmetric) -> float

"""

    HighLowPointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighLowPointElevation(self: ProfileParabolaSymmetric) -> float

"""

    HighLowPointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighLowPointStation(self: ProfileParabolaSymmetric) -> float

"""

    K = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: K(self: ProfileParabolaSymmetric) -> float

Set: K(self: ProfileParabolaSymmetric) = value
"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: ProfileParabolaSymmetric) -> float

"""

    PVIElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIElevation(self: ProfileParabolaSymmetric) -> float

"""

    PVIStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIStation(self: ProfileParabolaSymmetric) -> float

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: ProfileParabolaSymmetric) -> float

Set: Radius(self: ProfileParabolaSymmetric) = value
"""

    TangentOffsetAtPVI = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentOffsetAtPVI(self: ProfileParabolaSymmetric) -> float

"""

    ThroughPoint1Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint1Elevation(self: ProfileParabolaSymmetric) -> float

Set: ThroughPoint1Elevation(self: ProfileParabolaSymmetric) = value
"""

    ThroughPoint1Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint1Station(self: ProfileParabolaSymmetric) -> float

Set: ThroughPoint1Station(self: ProfileParabolaSymmetric) = value
"""

    ThroughPoint2Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint2Elevation(self: ProfileParabolaSymmetric) -> float

Set: ThroughPoint2Elevation(self: ProfileParabolaSymmetric) = value
"""

    ThroughPoint2Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint2Station(self: ProfileParabolaSymmetric) -> float

Set: ThroughPoint2Station(self: ProfileParabolaSymmetric) = value
"""

    ThroughPoint3Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint3Elevation(self: ProfileParabolaSymmetric) -> float

Set: ThroughPoint3Elevation(self: ProfileParabolaSymmetric) = value
"""

    ThroughPoint3Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint3Station(self: ProfileParabolaSymmetric) -> float

Set: ThroughPoint3Station(self: ProfileParabolaSymmetric) = value
"""



class ProfileProjectionLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(profileViewId, profileProjectionId, labelStyleId):
        """ Create(profileViewId: ObjectId, profileProjectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ProjectionSourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionSourceId(self: ProfileProjectionLabel) -> ObjectId

"""


    m_SubData = None


class ProfilePVI(CivilWrapper<AeccDbVAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: ProfilePVI) -> float

Set: Elevation(self: ProfilePVI) = value
"""

    EntityAfter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityAfter(self: ProfilePVI) -> UInt32

"""

    EntityBefore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityBefore(self: ProfilePVI) -> UInt32

"""

    GradeIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeIn(self: ProfilePVI) -> float

Set: GradeIn(self: ProfilePVI) = value
"""

    GradeOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeOut(self: ProfilePVI) -> float

Set: GradeOut(self: ProfilePVI) = value
"""

    HeadlightSightDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadlightSightDistance(self: ProfilePVI) -> float

Set: HeadlightSightDistance(self: ProfilePVI) = value
"""

    PassingSightDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PassingSightDistance(self: ProfilePVI) -> float

Set: PassingSightDistance(self: ProfilePVI) = value
"""

    PVIType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PVIType(self: ProfilePVI) -> ProfileEntityType

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: ProfilePVI) -> float

Set: Station(self: ProfilePVI) = value
"""

    StoppingSightDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StoppingSightDistance(self: ProfilePVI) -> float

Set: StoppingSightDistance(self: ProfilePVI) = value
"""

    VerticalCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalCurve(self: ProfilePVI) -> ProfileEntity

"""



class ProfilePVICollection(CivilWrapper<AeccDbVAlignment>):
    # no doc
    def AddPVI(self, station, elevation):
        """ AddPVI(self: ProfilePVICollection, station: float, elevation: float) -> ProfilePVI """
        pass

    def AddPVIArc(self, station, elevation, radius):
        """ AddPVIArc(self: ProfilePVICollection, station: float, elevation: float, radius: float) -> ProfilePVI """
        pass

    def AddPVIAsymParabola(self, station, elevation, tangentLen1, tangentLen2):
        """ AddPVIAsymParabola(self: ProfilePVICollection, station: float, elevation: float, tangentLen1: float, tangentLen2: float) -> ProfilePVI """
        pass

    def AddPVISymParabola(self, station, elevation, curveLength):
        """ AddPVISymParabola(self: ProfilePVICollection, station: float, elevation: float, curveLength: float) -> ProfilePVI """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfilePVICollection) -> IEnumerator[ProfilePVI] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfilePVICollection) -> IEnumerator """
        pass

    def GetPVIAt(self, station, elevation):
        """ GetPVIAt(self: ProfilePVICollection, station: float, elevation: float) -> ProfilePVI """
        pass

    def Remove(self, profilePVI):
        """ Remove(self: ProfilePVICollection, profilePVI: ProfilePVI) """
        pass

    def RemoveAt(self, *__args):
        """ RemoveAt(self: ProfilePVICollection, index: int)RemoveAt(self: ProfilePVICollection, station: float, elevation: float) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfilePVI](enumerable: IEnumerable[ProfilePVI], value: ProfilePVI) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ProfilePVICollection) -> int

"""



class ProfilePVILabelGroup(ProfileLabelGroup):
    # no doc
    @staticmethod
    def Create(profileViewId, profileId, styleId):
        """ Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId, profileId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    StaggerLineHeight1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight1(self: ProfilePVILabelGroup) -> float

Set: StaggerLineHeight1(self: ProfilePVILabelGroup) = value
"""

    StaggerLineHeight2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight2(self: ProfilePVILabelGroup) -> float

Set: StaggerLineHeight2(self: ProfilePVILabelGroup) = value
"""

    Weeding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weeding(self: ProfilePVILabelGroup) -> float

Set: Weeding(self: ProfilePVILabelGroup) = value
"""


    m_SubData = None


class ProfileSagCurveLabelGroup(ProfileLabelGroup):
    # no doc
    @staticmethod
    def Create(profileViewId, profileId, styleId):
        """ Create(profileViewId: ObjectId, profileId: ObjectId, styleId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId, profileId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId, profileId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, profileId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, profileId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class ProfileTangent(ProfileEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbVAlignment>, A_0: bool) """
        pass

    EntityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityType(self: ProfileTangent) -> ProfileEntityType

"""

    Grade = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grade(self: ProfileTangent) -> float

"""

    ThroughPoint1Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint1Elevation(self: ProfileTangent) -> float

Set: ThroughPoint1Elevation(self: ProfileTangent) = value
"""

    ThroughPoint1Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint1Station(self: ProfileTangent) -> float

Set: ThroughPoint1Station(self: ProfileTangent) = value
"""

    ThroughPoint2Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint2Elevation(self: ProfileTangent) -> float

Set: ThroughPoint2Elevation(self: ProfileTangent) = value
"""

    ThroughPoint2Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPoint2Station(self: ProfileTangent) -> float

Set: ThroughPoint2Station(self: ProfileTangent) = value
"""



class ProfileType(Enum):
    """ enum ProfileType, values: CorridorFeature (4), CurbReturnProfile (7), EG (0), FG (1), File (3), OffsetProfile (6), Superimposed (2) """
    CorridorFeature = None
    CurbReturnProfile = None
    EG = None
    FG = None
    File = None
    OffsetProfile = None
    Superimposed = None
    value__ = None


class ProfileUpdateType(Enum):
    """ enum ProfileUpdateType, values: Dynamic (1), Static (0) """
    Dynamic = None
    Static = None
    value__ = None


class ProfileView(Graph):
    # no doc
    @staticmethod
    def Create(*__args):
        """
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId, splitOptions: SplitProfileViewCreationOptions) -> ObjectId
        Create(alignmentId: ObjectId, insertPosition: Point3d) -> ObjectId
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId) -> ObjectId
        Create(document: CivilDocument, profileViewName: str, profileViewBandSetName: str, alignmentName: str, insertPosition: Point3d) -> ObjectId
        Create(document: CivilDocument, profileViewName: str, profileViewBandSetId: ObjectId, alignmentId: ObjectId, insertPosition: Point3d) -> ObjectId
        Create(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: StackedProfileViewsCreationOptions) -> ObjectIdCollection
        Create(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: StackedProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions) -> ObjectIdCollection
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, stackedOptions: StackedProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions) -> ObjectIdCollection
        Create(alignmentId: ObjectId, insertPosition: Point3d, splitOptions: SplitProfileViewCreationOptions) -> ObjectId
        Create(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, stackedOptions: StackedProfileViewsCreationOptions) -> ObjectIdCollection
        """
        pass

    @staticmethod
    def CreateMultiple(alignmentId, insertPosition, *__args):
        """
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, multipleOptions: MultipleProfileViewsCreationOptions) -> ObjectIdCollection
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, multipleOptions: MultipleProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions, datumType: ProfileViewDatumType) -> ObjectIdCollection
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId, multipleOptions: MultipleProfileViewsCreationOptions) -> ObjectIdCollection
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, profileViewStyleId: ObjectId, multipleOptions: MultipleProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions, datumType: ProfileViewDatumType) -> ObjectIdCollection
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: StackedProfileViewsCreationOptions, multipleOptions: MultipleProfileViewsCreationOptions) -> ObjectIdCollection
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, stackedOptions: StackedProfileViewsCreationOptions, multipleOptions: MultipleProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions, datumType: ProfileViewDatumType) -> ObjectIdCollection
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, stackedOptions: StackedProfileViewsCreationOptions, multipleOptions: MultipleProfileViewsCreationOptions) -> ObjectIdCollection
        CreateMultiple(alignmentId: ObjectId, insertPosition: Point3d, profileViewName: str, profileViewBandSetId: ObjectId, stackedOptions: StackedProfileViewsCreationOptions, multipleOptions: MultipleProfileViewsCreationOptions, splitOptions: SplitProfileViewCreationOptions, datumType: ProfileViewDatumType) -> ObjectIdCollection
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def FindStationAndElevationAtXY(self, x, y, station, elevation):
        """ FindStationAndElevationAtXY(self: ProfileView, x: float, y: float, station: float, elevation: float) -> (bool, float, float) """
        pass

    def FindXYAtStationAndElevation(self, station, elevation, x, y):
        """ FindXYAtStationAndElevation(self: ProfileView, station: float, elevation: float, x: float, y: float) -> (bool, float, float) """
        pass

    def GetAvailablePipeProfileLabelIds(self):
        """ GetAvailablePipeProfileLabelIds(self: ProfileView) -> ObjectIdCollection """
        pass

    def GetAvailableSpanningPipeProfileLabelIds(self):
        """ GetAvailableSpanningPipeProfileLabelIds(self: ProfileView) -> ObjectIdCollection """
        pass

    def GetAvailableStructureProfileLabelIds(self):
        """ GetAvailableStructureProfileLabelIds(self: ProfileView) -> ObjectIdCollection """
        pass

    def GetLabelIds(self):
        """ GetLabelIds(self: ProfileView) -> ObjectIdCollection """
        pass

    def GetPressureNetworkPartsInGraph(self):
        """ GetPressureNetworkPartsInGraph(self: ProfileView) -> ObjectIdCollection """
        pass

    def GetProfileViewLabelIds(self):
        """ GetProfileViewLabelIds(self: ProfileView) -> ObjectIdCollection """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: ProfileView) -> ObjectId

"""

    AlignmentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentName(self: ProfileView) -> str

"""

    Bands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bands(self: ProfileView) -> ProfileViewBandSet

"""

    ElevationMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationMax(self: ProfileView) -> float

Set: ElevationMax(self: ProfileView) = value
"""

    ElevationMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationMin(self: ProfileView) -> float

Set: ElevationMin(self: ProfileView) = value
"""

    ElevationRangeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationRangeMode(self: ProfileView) -> ElevationRangeType

Set: ElevationRangeMode(self: ProfileView) = value
"""

    GraphOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphOverrides(self: ProfileView) -> ProfileOverrideCollection

"""

    HatchAreas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchAreas(self: ProfileView) -> ProfileHatchAreaCollection

"""

    PipeOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeOverrides(self: ProfileView) -> PipeOverrideCollection

"""

    SplitDataLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitDataLines(self: ProfileView) -> ProfileViewSplitDataCollection

"""

    SplitDatumRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitDatumRounding(self: ProfileView) -> DatumRoundingType

Set: SplitDatumRounding(self: ProfileView) = value
"""

    SplitHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitHeight(self: ProfileView) -> float

Set: SplitHeight(self: ProfileView) = value
"""

    SplitProfileView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitProfileView(self: ProfileView) -> bool

Set: SplitProfileView(self: ProfileView) = value
"""

    SplitStationMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitStationMode(self: ProfileView) -> SplitStationType

Set: SplitStationMode(self: ProfileView) = value
"""

    SplitStationRounding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitStationRounding(self: ProfileView) -> StationRoundingType

Set: SplitStationRounding(self: ProfileView) = value
"""

    StationEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationEnd(self: ProfileView) -> float

Set: StationEnd(self: ProfileView) = value
"""

    StationRangeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationRangeMode(self: ProfileView) -> StationRangeType

Set: StationRangeMode(self: ProfileView) = value
"""

    StationStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationStart(self: ProfileView) -> float

Set: StationStart(self: ProfileView) = value
"""

    StructureOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureOverrides(self: ProfileView) -> StructureOverrideCollection

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: ProfileView) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: ProfileView) = value
"""



class ProfileViewBandItem(ProfileViewBandSetItem):
    # no doc
    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: ProfileViewBandItem) -> ObjectId

"""

    DataSourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataSourceId(self: ProfileViewBandItem) -> ObjectId

Set: DataSourceId(self: ProfileViewBandItem) = value
"""

    MaterialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialName(self: ProfileViewBandItem) -> str

Set: MaterialName(self: ProfileViewBandItem) = value
"""

    Profile1Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile1Id(self: ProfileViewBandItem) -> ObjectId

Set: Profile1Id(self: ProfileViewBandItem) = value
"""

    Profile2Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile2Id(self: ProfileViewBandItem) -> ObjectId

Set: Profile2Id(self: ProfileViewBandItem) = value
"""

    SettingsNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ProfileViewBandItemCollection(BandSetItemCollection):
    """ ProfileViewBandItemCollection(profileViewId: ObjectId, location: BandLocationType) """
    def Add(self, *__args):
        """ Add(self: ProfileViewBandItemCollection, bandType: BandType, profileBandStyleName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: BandSetItemCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileViewBandItemCollection) -> IEnumerator[ProfileViewBandItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfileViewBandItemCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfileViewBandItem](enumerable: IEnumerable[ProfileViewBandItem], value: ProfileViewBandItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, profileViewId, location):
        """ __new__(cls: type, profileViewId: ObjectId, location: BandLocationType) """
        pass


class ProfileViewBandSet(GraphBandSet):
    # no doc
    def GetBottomBandItems(self):
        """ GetBottomBandItems(self: ProfileViewBandSet) -> ProfileViewBandItemCollection """
        pass

    def GetTopBandItems(self):
        """ GetTopBandItems(self: ProfileViewBandSet) -> ProfileViewBandItemCollection """
        pass

    def SetBottomBandItems(self, bandItems):
        """ SetBottomBandItems(self: ProfileViewBandSet, bandItems: ProfileViewBandItemCollection) """
        pass

    def SetTopBandItems(self, bandItems):
        """ SetTopBandItems(self: ProfileViewBandSet, bandItems: ProfileViewBandItemCollection) """
        pass

    m_pGraph = None


class ProfileViewDepthLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(profileViewId, labelStyleId, startPoint, endPoint):
        """ Create(profileViewId: ObjectId, labelStyleId: ObjectId, startPoint: Point2d, endPoint: Point2d) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: ProfileViewDepthLabel) -> Point2d

Set: EndPoint(self: ProfileViewDepthLabel) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: ProfileViewDepthLabel) -> Point2d

Set: StartPoint(self: ProfileViewDepthLabel) = value
"""


    m_SubData = None


class ProfileViewPart(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetLabelIds(self):
        """ GetLabelIds(self: ProfileViewPart) -> ObjectIdCollection """
        pass

    def GetPartProfileLabelIds(self):
        """ GetPartProfileLabelIds(self: ProfileViewPart) -> ObjectIdCollection """
        pass

    ModelPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelPartId(self: ProfileViewPart) -> ObjectId

"""



class ProfileViewPressurePart(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    ModelPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelPartId(self: ProfileViewPressurePart) -> ObjectId

"""



class ProfileViewSplitData(CivilWrapper<AeccDbGraphProfile>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphProfile>, A_0: bool) """
        pass

    AdjustedDatum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjustedDatum(self: ProfileViewSplitData) -> float

Set: AdjustedDatum(self: ProfileViewSplitData) = value
"""

    ProfileViewStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewStyleId(self: ProfileViewSplitData) -> ObjectId

Set: ProfileViewStyleId(self: ProfileViewSplitData) = value
"""

    ProfileViewStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewStyleName(self: ProfileViewSplitData) -> str

Set: ProfileViewStyleName(self: ProfileViewSplitData) = value
"""

    SplitStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitStation(self: ProfileViewSplitData) -> float

Set: SplitStation(self: ProfileViewSplitData) = value
"""



class ProfileViewSplitDataCollection(CivilWrapper<AeccDbGraphProfile>):
    # no doc
    def Add(self, rawStation, datum):
        """ Add(self: ProfileViewSplitDataCollection, rawStation: float, datum: float) -> ProfileViewSplitData """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphProfile>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileViewSplitDataCollection) -> IEnumerator[ProfileViewSplitData] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfileViewSplitDataCollection) -> IEnumerator """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ProfileViewSplitDataCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfileViewSplitData](enumerable: IEnumerable[ProfileViewSplitData], value: ProfileViewSplitData) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ProfileViewSplitDataCollection) -> int

"""



class QTOAreaResult(CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>, A_0: bool) """
        pass

    CutArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutArea(self: QTOAreaResult) -> float

"""

    FactoredCutArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FactoredCutArea(self: QTOAreaResult) -> float

"""

    FactoredFillArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FactoredFillArea(self: QTOAreaResult) -> float

"""

    FactoredUsableArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FactoredUsableArea(self: QTOAreaResult) -> float

"""

    FillArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillArea(self: QTOAreaResult) -> float

"""

    MomentOfCutArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MomentOfCutArea(self: QTOAreaResult) -> float

"""

    MomentOfFactoredCutArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MomentOfFactoredCutArea(self: QTOAreaResult) -> float

"""

    MomentOfFactoredFillArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MomentOfFactoredFillArea(self: QTOAreaResult) -> float

"""

    MomentOfFactoredUsableArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MomentOfFactoredUsableArea(self: QTOAreaResult) -> float

"""

    MomentOfFillArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MomentOfFillArea(self: QTOAreaResult) -> float

"""



class QTOCriteriaNameMapping(object):
    """ QTOCriteriaNameMapping(quantityTakeoffCriteriaId: ObjectId, sampleLineGroupId: ObjectId) """
    def Dispose(self):
        """ Dispose(self: QTOCriteriaNameMapping) """
        pass

    def GetMappedCorridorShape(self, materialName, shapeName, mappedCorridorId, mappedShapeName):
        """ GetMappedCorridorShape(self: QTOCriteriaNameMapping, materialName: str, shapeName: str, mappedCorridorId: ObjectId, mappedShapeName: str) -> (ObjectId, str) """
        pass

    def GetMappedSurfaceId(self, materialName, surfaceName):
        """ GetMappedSurfaceId(self: QTOCriteriaNameMapping, materialName: str, surfaceName: str) -> ObjectId """
        pass

    def MapCorridorShape(self, *__args):
        """ MapCorridorShape(self: QTOCriteriaNameMapping, materialName: str, shapeName: str, mappedCorridorId: ObjectId, mappedShapeName: str)MapCorridorShape(self: QTOCriteriaNameMapping, shapeName: str, mappedCorridorId: ObjectId, mappedShapeName: str) """
        pass

    def MapSurface(self, *__args):
        """ MapSurface(self: QTOCriteriaNameMapping, materialName: str, surfaceName: str, mappedSurfaceId: ObjectId)MapSurface(self: QTOCriteriaNameMapping, surfaceName: str, mappedSurfaceId: ObjectId) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, quantityTakeoffCriteriaId, sampleLineGroupId):
        """ __new__(cls: type, quantityTakeoffCriteriaId: ObjectId, sampleLineGroupId: ObjectId) """
        pass

    isMappingCompleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: isMappingCompleted(self: QTOCriteriaNameMapping) -> bool

"""



class QTOMaterial(object):
    # no doc
    def Add(self, *__args):
        """
        Add(self: QTOMaterial, surfaceId: ObjectId) -> QTOMaterialItem
        Add(self: QTOMaterial, corridorId: ObjectId, shapeCode: str) -> QTOMaterialItem
        """
        pass

    def Dispose(self):
        """ Dispose(self: QTOMaterial) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: QTOMaterial) -> IEnumerator[QTOMaterialItem] """
        pass

    def GetFactor(self, type):
        """ GetFactor(self: QTOMaterial, type: MaterialFactorType) -> float """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: QTOMaterial) -> IEnumerator """
        pass

    def IsFactorApplicable(self, type):
        """ IsFactorApplicable(self: QTOMaterial, type: MaterialFactorType) -> bool """
        pass

    def Remove(self, *__args):
        """
        Remove(self: QTOMaterial, name: str) -> bool
        Remove(self: QTOMaterial, materialItem: QTOMaterialItem) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: QTOMaterial, index: int) """
        pass

    def SetFactor(self, type, newValue):
        """ SetFactor(self: QTOMaterial, type: MaterialFactorType, newValue: float) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QTOMaterialItem](enumerable: IEnumerable[QTOMaterialItem], value: QTOMaterialItem) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QTOMaterial) -> int

"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guid(self: QTOMaterial) -> Guid

"""

    IsSubcriteriaSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSubcriteriaSupported(self: QTOMaterial) -> bool

"""

    MaterialGaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialGaps(self: QTOMaterial) -> QTOMaterialGapCollection

"""

    MaterialListGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialListGuid(self: QTOMaterial) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: QTOMaterial) -> str

Set: Name(self: QTOMaterial) = value
"""

    QuantityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityType(self: QTOMaterial) -> MaterialQuantityType

Set: QuantityType(self: QTOMaterial) = value
"""

    SampleLineGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineGroupId(self: QTOMaterial) -> ObjectId

"""

    ShapeStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeStyleId(self: QTOMaterial) -> ObjectId

Set: ShapeStyleId(self: QTOMaterial) = value
"""

    Subcriteria = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Subcriteria(self: QTOMaterial) -> QTOSubcriteriaCollection

"""



class QTOMaterialGap(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: QTOMaterialGap) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Applied = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Applied(self: QTOMaterialGap) -> bool

Set: Applied(self: QTOMaterialGap) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: QTOMaterialGap) -> str

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: QTOMaterialGap) -> float

"""

    RunInDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RunInDistance(self: QTOMaterialGap) -> float

Set: RunInDistance(self: QTOMaterialGap) = value
"""

    RunOutDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RunOutDistance(self: QTOMaterialGap) -> float

Set: RunOutDistance(self: QTOMaterialGap) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: QTOMaterialGap) -> float

"""



class QTOMaterialGapCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: QTOMaterialGapCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: QTOMaterialGapCollection) -> IEnumerator[QTOMaterialGap] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: QTOMaterialGapCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QTOMaterialGap](enumerable: IEnumerable[QTOMaterialGap], value: QTOMaterialGap) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QTOMaterialGapCollection) -> int

"""



class QTOMaterialItem(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: QTOMaterialItem) """
        pass

    def IsConditionApplicable(self, conditionType):
        """ IsConditionApplicable(self: QTOMaterialItem, conditionType: MaterialConditionType) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Condition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Condition(self: QTOMaterialItem) -> MaterialConditionType

Set: Condition(self: QTOMaterialItem) = value
"""

    MaterialGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialGuid(self: QTOMaterialItem) -> Guid

"""

    MaterialListGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialListGuid(self: QTOMaterialItem) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: QTOMaterialItem) -> str

"""

    SampleLineGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineGroupId(self: QTOMaterialItem) -> ObjectId

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: QTOMaterialItem) -> MaterialItemType

"""



class QTOMaterialList(object):
    # no doc
    def Add(self, materialName):
        """ Add(self: QTOMaterialList, materialName: str) -> QTOMaterial """
        pass

    def Dispose(self):
        """ Dispose(self: QTOMaterialList) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: QTOMaterialList) -> IEnumerator[QTOMaterial] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: QTOMaterialList) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """
        Remove(self: QTOMaterialList, guid: Guid) -> bool
        Remove(self: QTOMaterialList, name: str) -> bool
        Remove(self: QTOMaterialList, material: QTOMaterial) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: QTOMaterialList, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QTOMaterial](enumerable: IEnumerable[QTOMaterial], value: QTOMaterial) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QTOMaterialList) -> int

"""

    CurveCorrectionTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveCorrectionTolerance(self: QTOMaterialList) -> float

Set: CurveCorrectionTolerance(self: QTOMaterialList) = value
"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guid(self: QTOMaterialList) -> Guid

"""

    IsCurveCorrectionEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCurveCorrectionEnabled(self: QTOMaterialList) -> bool

Set: IsCurveCorrectionEnabled(self: QTOMaterialList) = value
"""

    MaterialListGaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialListGaps(self: QTOMaterialList) -> QTOMaterialListGapCollection

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: QTOMaterialList) -> str

Set: Name(self: QTOMaterialList) = value
"""

    SampleLineGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineGroupId(self: QTOMaterialList) -> ObjectId

"""



class QTOMaterialListCollection(object):
    # no doc
    def Add(self, materialListName):
        """ Add(self: QTOMaterialListCollection, materialListName: str) -> QTOMaterialList """
        pass

    def Fix(self, methodType):
        """ Fix(self: QTOMaterialListCollection, methodType: MaterialVolumeCalculationMethodType) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: QTOMaterialListCollection) -> IEnumerator[QTOMaterialList] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: QTOMaterialListCollection) -> IEnumerator """
        pass

    def ImportCriteria(self, criteriaNameMapping):
        """ ImportCriteria(self: QTOMaterialListCollection, criteriaNameMapping: QTOCriteriaNameMapping) -> QTOMaterialList """
        pass

    def Remove(self, *__args):
        """
        Remove(self: QTOMaterialListCollection, guid: Guid) -> bool
        Remove(self: QTOMaterialListCollection, name: str) -> bool
        Remove(self: QTOMaterialListCollection, materialList: QTOMaterialList) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: QTOMaterialListCollection, index: int) """
        pass

    def Validate(self, methodType):
        """ Validate(self: QTOMaterialListCollection, methodType: MaterialVolumeCalculationMethodType) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QTOMaterialList](enumerable: IEnumerable[QTOMaterialList], value: QTOMaterialList) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QTOMaterialListCollection) -> int

"""

    VolumeCalculationMethodType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeCalculationMethodType(self: QTOMaterialListCollection) -> MaterialVolumeCalculationMethodType

Set: VolumeCalculationMethodType(self: QTOMaterialListCollection) = value
"""



class QTOMaterialListGap(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: QTOMaterialListGap) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: QTOMaterialListGap) -> str

Set: Description(self: QTOMaterialListGap) = value
"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: QTOMaterialListGap) -> float

Set: EndStation(self: QTOMaterialListGap) = value
"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: QTOMaterialListGap) -> float

Set: StartStation(self: QTOMaterialListGap) = value
"""



class QTOMaterialListGapCollection(object):
    # no doc
    def Add(self, startStation, endStation):
        """ Add(self: QTOMaterialListGapCollection, startStation: float, endStation: float) -> QTOMaterialListGap """
        pass

    def Dispose(self):
        """ Dispose(self: QTOMaterialListGapCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: QTOMaterialListGapCollection) -> IEnumerator[QTOMaterialListGap] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: QTOMaterialListGapCollection) -> IEnumerator """
        pass

    def Remove(self, materialListGap):
        """ Remove(self: QTOMaterialListGapCollection, materialListGap: QTOMaterialListGap) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: QTOMaterialListGapCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QTOMaterialListGap](enumerable: IEnumerable[QTOMaterialListGap], value: QTOMaterialListGap) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QTOMaterialListGapCollection) -> int

"""



class QTOResultType(Enum):
    """ enum QTOResultType, values: MaterialCutFillVolume (3), MaterialCutVolume (1), MaterialEarthWorkVolume (4), MaterialFillVolume (2), MaterialStructureVolume (5), TotalVolume (0) """
    MaterialCutFillVolume = None
    MaterialCutVolume = None
    MaterialEarthWorkVolume = None
    MaterialFillVolume = None
    MaterialStructureVolume = None
    TotalVolume = None
    value__ = None


class QTOSectionalResult(CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>, A_0: bool) """
        pass

    AreaResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaResult(self: QTOSectionalResult) -> QTOAreaResult

"""

    SampleLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineId(self: QTOSectionalResult) -> ObjectId

"""

    SampleLineName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineName(self: QTOSectionalResult) -> str

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: QTOSectionalResult) -> float

"""

    VolumeResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeResult(self: QTOSectionalResult) -> QTOVolumeResult

"""



class QTOSubcriteria(object):
    # no doc
    def Add(self, surfaceId):
        """ Add(self: QTOSubcriteria, surfaceId: ObjectId) -> QTOMaterialItem """
        pass

    def Dispose(self):
        """ Dispose(self: QTOSubcriteria) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: QTOSubcriteria) -> IEnumerator[QTOMaterialItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: QTOSubcriteria) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """
        Remove(self: QTOSubcriteria, name: str) -> bool
        Remove(self: QTOSubcriteria, materialItem: QTOMaterialItem) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: QTOSubcriteria, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QTOMaterialItem](enumerable: IEnumerable[QTOMaterialItem], value: QTOMaterialItem) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QTOSubcriteria) -> int

"""

    MaterialGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialGuid(self: QTOSubcriteria) -> Guid

"""

    MaterialListGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialListGuid(self: QTOSubcriteria) -> Guid

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: QTOSubcriteria) -> str

Set: Name(self: QTOSubcriteria) = value
"""

    SampleLineGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineGroupId(self: QTOSubcriteria) -> ObjectId

"""



class QTOSubcriteriaCollection(object):
    # no doc
    def Add(self, subcriteriaName):
        """ Add(self: QTOSubcriteriaCollection, subcriteriaName: str) -> QTOSubcriteria """
        pass

    def Dispose(self):
        """ Dispose(self: QTOSubcriteriaCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: QTOSubcriteriaCollection) -> IEnumerator[QTOSubcriteria] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: QTOSubcriteriaCollection) -> IEnumerator """
        pass

    def Remove(self, subcriteria):
        """ Remove(self: QTOSubcriteriaCollection, subcriteria: QTOSubcriteria) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: QTOSubcriteriaCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[QTOSubcriteria](enumerable: IEnumerable[QTOSubcriteria], value: QTOSubcriteria) -> bool """
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

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QTOSubcriteriaCollection) -> int

"""



class QTOUtility(object):
    # no doc
    @staticmethod
    def AddPayItemId(oid, payItemID):
        """ AddPayItemId(oid: ObjectId, payItemID: str) """
        pass

    @staticmethod
    def DeleteAllPayItemsIds(oid):
        """ DeleteAllPayItemsIds(oid: ObjectId) """
        pass

    @staticmethod
    def DeletePayItemIds(oid, payItemIDs):
        """ DeletePayItemIds(oid: ObjectId, payItemIDs: StringCollection) """
        pass

    @staticmethod
    def GetPayItemIds(oid):
        """ GetPayItemIds(oid: ObjectId) -> StringCollection """
        pass

    @staticmethod
    def OpenPayItemFile(fileFormat, strPayItemFilePath, strPayItemCategorizationFilePath):
        """ OpenPayItemFile(fileFormat: PayItemFileFormat, strPayItemFilePath: str, strPayItemCategorizationFilePath: str) -> bool """
        pass


class QTOVolumeResult(CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccQuantityTakeoffResult::SECTIONAL_RESULT>, A_0: bool) """
        pass

    CumulativeCutVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CumulativeCutVolume(self: QTOVolumeResult) -> float

"""

    CumulativeFillVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CumulativeFillVolume(self: QTOVolumeResult) -> float

"""

    CumulativeUsableVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CumulativeUsableVolume(self: QTOVolumeResult) -> float

"""

    IncrementalCutVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalCutVolume(self: QTOVolumeResult) -> float

"""

    IncrementalFillVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalFillVolume(self: QTOVolumeResult) -> float

"""

    IncrementalUsableVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalUsableVolume(self: QTOVolumeResult) -> float

"""



class QuantityTakeoffResult(CivilWrapper<AeccQuantityTakeoffResult>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccQuantityTakeoffResult>, A_0: bool) """
        pass

    def GetResult(self, *__args):
        """
        GetResult(self: QuantityTakeoffResult, sampleLineName: str) -> QTOSectionalResult
        GetResult(self: QuantityTakeoffResult, sampleLineId: ObjectId) -> QTOSectionalResult
        GetResult(self: QuantityTakeoffResult, sampleLineStation: float) -> QTOSectionalResult
        GetResult(self: QuantityTakeoffResult, sampleLineStation: float, tolerance: float) -> QTOSectionalResult
        """
        pass

    def GetResultsAlongSampleLines(self):
        """ GetResultsAlongSampleLines(self: QuantityTakeoffResult) -> Array[QTOSectionalResult] """
        pass


class RailAlignmentInfo(object):
    # no doc
    def GetCantInfoAtStation(self, station):
        """ GetCantInfoAtStation(self: RailAlignmentInfo, station: float) -> RailCANTInfo """
        pass

    TrackWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrackWidth(self: RailAlignmentInfo) -> float

Set: TrackWidth(self: RailAlignmentInfo) = value
"""



class RailCANTInfo(object):
    # no doc
    AppliedCANT = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliedCANT(self: RailCANTInfo) -> float

"""

    LeftRailElevationDifference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftRailElevationDifference(self: RailCANTInfo) -> float

"""

    Pivot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pivot(self: RailCANTInfo) -> RailAlignmentPivotType

"""

    RightRailElevationDifference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightRailElevationDifference(self: RailCANTInfo) -> float

"""



class RegionMatchType(Enum):
    """ enum RegionMatchType, values: All (0), AssemblyAndTarget (1), Frequency (3) """
    All = None
    AssemblyAndTarget = None
    Frequency = None
    value__ = None


class SampledSectionLink(CivilWrapper<Autodesk::Civil::DatabaseServices::SampleSectionLinkData>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<Autodesk::Civil::DatabaseServices::SampleSectionLinkData>, A_0: bool) """
        pass

    EndPointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointElevation(self: SampledSectionLink) -> float

Set: EndPointElevation(self: SampledSectionLink) = value
"""

    EndPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointOffset(self: SampledSectionLink) -> float

Set: EndPointOffset(self: SampledSectionLink) = value
"""

    EndPointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointStation(self: SampledSectionLink) -> float

"""

    StartPointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointElevation(self: SampledSectionLink) -> float

"""

    StartPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointOffset(self: SampledSectionLink) -> float

"""

    StartPointStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointStation(self: SampledSectionLink) -> float

"""



class SampledSectionLinkCollection(CivilWrapper<std::vector<Autodesk::Civil::DatabaseServices::SampleSectionLinkData \*\,std::allocator<Autodesk::Civil::DatabaseServices::SampleSectionLinkData \*> > >):
    # no doc
    def Dispose(self):
        """ Dispose(self: SampledSectionLinkCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SampledSectionLinkCollection) -> IEnumerator[SampledSectionLink] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SampledSectionLinkCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SampledSectionLink](enumerable: IEnumerable[SampledSectionLink], value: SampledSectionLink) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class SampleLine(GeoEntity):
    # no doc
    @staticmethod
    def Create(sampleLineName, sampleLineGroupId, *__args):
        """
        Create(sampleLineName: str, sampleLineGroupId: ObjectId, station: float) -> ObjectId
        Create(sampleLineName: str, sampleLineGroupId: ObjectId, points: Point2dCollection) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetMaterialSectionId(self, materialListGuid, materialGuid):
        """ GetMaterialSectionId(self: SampleLine, materialListGuid: Guid, materialGuid: Guid) -> ObjectId """
        pass

    def GetSectionId(self, sampledSourceId):
        """ GetSectionId(self: SampleLine, sampledSourceId: ObjectId) -> ObjectId """
        pass

    def GetSectionIds(self):
        """ GetSectionIds(self: SampleLine) -> ObjectIdCollection """
        pass

    def GetSectionViewIds(self):
        """ GetSectionViewIds(self: SampleLine) -> ObjectIdCollection """
        pass

    GroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupId(self: SampleLine) -> ObjectId

"""

    LockToStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockToStation(self: SampleLine) -> bool

Set: LockToStation(self: SampleLine) = value
"""

    Number = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Number(self: SampleLine) -> int

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: SampleLine) -> float

Set: Station(self: SampleLine) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: SampleLine) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: SampleLine) = value
"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: SampleLine) -> SampleLineVertexCollection

"""



class SampleLineGroup(GeoEntity):
    # no doc
    @staticmethod
    def Create(groupName, alignmentId):
        """ Create(groupName: str, alignmentId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAvailableSampleLineLabelGroupIds(self):
        """ GetAvailableSampleLineLabelGroupIds(self: SampleLineGroup) -> ObjectIdCollection """
        pass

    def GetMappingGuid(self, mappingName):
        """ GetMappingGuid(self: SampleLineGroup, mappingName: str) -> Guid """
        pass

    def GetMassHaulViewIds(self):
        """ GetMassHaulViewIds(self: SampleLineGroup) -> ObjectIdCollection """
        pass

    def GetMaterialGuid(self, mappingGuid, materialName):
        """ GetMaterialGuid(self: SampleLineGroup, mappingGuid: Guid, materialName: str) -> Guid """
        pass

    def GetMaterialNamesInMapping(self, mappingGuid):
        """ GetMaterialNamesInMapping(self: SampleLineGroup, mappingGuid: Guid) -> Array[str] """
        pass

    def GetMaterialSectionSources(self):
        """ GetMaterialSectionSources(self: SampleLineGroup) -> MaterialSectionSourceCollection """
        pass

    def GetQTOMappingNames(self):
        """ GetQTOMappingNames(self: SampleLineGroup) -> Array[str] """
        pass

    def GetSampleLineIds(self, station=None, tolerance=None):
        """
        GetSampleLineIds(self: SampleLineGroup) -> ObjectIdCollection
        GetSampleLineIds(self: SampleLineGroup, station: float, tolerance: float) -> ObjectIdCollection
        """
        pass

    def GetSectionSources(self):
        """ GetSectionSources(self: SampleLineGroup) -> SectionSourceCollection """
        pass

    def GetTotalVolumeResultDataForMaterialList(self, mappingGuid):
        """ GetTotalVolumeResultDataForMaterialList(self: SampleLineGroup, mappingGuid: Guid) -> QuantityTakeoffResult """
        pass

    DefaultSamplineLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultSamplineLabelStyleId(self: SampleLineGroup) -> ObjectId

Set: DefaultSamplineLabelStyleId(self: SampleLineGroup) = value
"""

    DefaultSamplineStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultSamplineStyleId(self: SampleLineGroup) -> ObjectId

Set: DefaultSamplineStyleId(self: SampleLineGroup) = value
"""

    IndividualSectionViewGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndividualSectionViewGroup(self: SampleLineGroup) -> SectionViewGroup

"""

    MaterialLists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialLists(self: SampleLineGroup) -> QTOMaterialListCollection

"""

    SectionViewGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewGroups(self: SampleLineGroup) -> SectionViewGroupCollection

"""



class SampleLineLabelGroup(AutoFeatureLabelGroup):
    # no doc
    @staticmethod
    def Create(sampleLineGroupId, labelStyleId=None):
        """
        Create(sampleLineGroupId: ObjectId, labelStyleId: ObjectId) -> ObjectId
        Create(sampleLineGroupId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(sampleLineGroupId):
        """ GetAvailableLabelGroupIds(sampleLineGroupId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class SampleLineVertex(CivilWrapper<AeccDbSampleLine>):
    # no doc
    def Dispose(self):
        """ Dispose(self: SampleLineVertex, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SampleLineVertex) -> Point3d

Set: Location(self: SampleLineVertex) = value
"""

    OffsetIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetIndex(self: SampleLineVertex) -> int

"""

    Side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Side(self: SampleLineVertex) -> SampleLineVertexSideType

"""



class SampleLineVertexCollection(CivilWrapper<AeccDbSampleLine>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSampleLine>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SampleLineVertexCollection) -> IEnumerator[SampleLineVertex] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SampleLineVertexCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SampleLineVertex](enumerable: IEnumerable[SampleLineVertex], value: SampleLineVertex) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SampleLineVertexCollection) -> int

"""



class SampleLineVertexSideType(Enum):
    """ enum SampleLineVertexSideType, values: Center (2), Left (0), Right (1) """
    Center = None
    Left = None
    Right = None
    value__ = None


class SCSCSConstraints(CivilWrapper<AeccGeSCSCSConstraints>):
    # no doc
    @staticmethod
    def CreateByArc1Angle(arc1Angle, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByArc1Angle(arc1Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByArc1Length(arc1Len, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByArc1Length(arc1Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByArc1PassPt(ptArc1PassThru, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByArc1PassPt(ptArc1PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByArc2Angle(arc2Angle, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByArc2Angle(arc2Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByArc2Length(arc2Len, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByArc2Length(arc2Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByArc2PassPt(ptArc2PassThru, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByArc2PassPt(ptArc2PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByEndPoint(endPoint, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByEndPoint(endPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByStartPoint(startPoint, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByStartPoint(startPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByTan1Length(extTan1Len, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByTan1Length(extTan1Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    @staticmethod
    def CreateByTan2Length(extTan2Len, sp1Param, arc1Radius, sp2Param, arc2Radius, sp3Param, isParamAValue):
        """ CreateByTan2Length(extTan2Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, arc2Radius: float, sp3Param: float, isParamAValue: bool) -> SCSCSConstraints """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccGeSCSCSConstraints>, A_0: bool) """
        pass


class SCSSCSConstraints(CivilWrapper<AeccGeSCSSCSConstraints>):
    # no doc
    @staticmethod
    def CreateByArc1Angle(arc1Angle, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByArc1Angle(arc1Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    @staticmethod
    def CreateByArc1Length(arc1Len, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByArc1Length(arc1Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    @staticmethod
    def CreateByArc1PassPt(ptArc1PassThru, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByArc1PassPt(ptArc1PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    @staticmethod
    def CreateByArc2Angle(arc2Angle, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByArc2Angle(arc2Angle: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    @staticmethod
    def CreateByArc2Length(arc2Len, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByArc2Length(arc2Len: float, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    @staticmethod
    def CreateByArc2PassPt(ptArc2PassThru, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByArc2PassPt(ptArc2PassThru: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    @staticmethod
    def CreateByEndPoint(endPoint, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByEndPoint(endPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    @staticmethod
    def CreateByStartPoint(startPoint, sp1Param, arc1Radius, sp2Param, sp3Param, arc2Radius, sp4Param, isParamAValue):
        """ CreateByStartPoint(startPoint: Point2d, sp1Param: float, arc1Radius: float, sp2Param: float, sp3Param: float, arc2Radius: float, sp4Param: float, isParamAValue: bool) -> SCSSCSConstraints """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccGeSCSSCSConstraints>, A_0: bool) """
        pass


class SectionalDataBandLabelGroup(ProfileBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class SectionBandLabelGroup(AutoFeatureLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(bandLabelGroupClassType, sectionViewId, includeDerived):
        """ GetAvailableLabelGroupIds(bandLabelGroupClassType: Type, sectionViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: SectionBandLabelGroup) -> ObjectId

Set: StyleId(self: SectionBandLabelGroup) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: SectionBandLabelGroup) -> str

Set: StyleName(self: SectionBandLabelGroup) = value
"""


    m_SubData = None


class SectionDataBandLabelGroup(SectionBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId):
        """ GetAvailableLabelGroupIds(sectionViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class SectionLabelGroup(AutoFeatureLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def DoesSectionSupportSectionLabelGroup(self, *args): #cannot find CLR method
        """ DoesSectionSupportSectionLabelGroup(oidSection: AcDbObjectId) -> bool """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(labelGroupClassType, sectionViewId, sectionId, includeDerived):
        """ GetAvailableLabelGroupIds(labelGroupClassType: Type, sectionViewId: ObjectId, sectionId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    def IsSectionInSectionView(self, *args): #cannot find CLR method
        """ IsSectionInSectionView(oidSection: AcDbObjectId, oidSectionView: AcDbObjectId) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    RangeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeEnd(self: SectionLabelGroup) = value
"""

    RangeEndFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeEndFromFeature(self: SectionLabelGroup) = value
"""

    RangeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeStart(self: SectionLabelGroup) = value
"""

    RangeStartFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeStartFromFeature(self: SectionLabelGroup) = value
"""


    m_SubData = None


class SectionGradeBreakLabelGroup(SectionLabelGroup):
    # no doc
    @staticmethod
    def Create(sectionViewId, sectionId, labelStyleId=None):
        """
        Create(sectionViewId: ObjectId, sectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId
        Create(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId, sectionId):
        """ GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    StaggerLineHeight1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight1(self: SectionGradeBreakLabelGroup) -> float

Set: StaggerLineHeight1(self: SectionGradeBreakLabelGroup) = value
"""

    StaggerLineHeight2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight2(self: SectionGradeBreakLabelGroup) -> float

Set: StaggerLineHeight2(self: SectionGradeBreakLabelGroup) = value
"""

    Weeding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weeding(self: SectionGradeBreakLabelGroup) -> float

Set: Weeding(self: SectionGradeBreakLabelGroup) = value
"""


    m_SubData = None


class SectionOffsetLabelGroup(SectionLabelGroup):
    # no doc
    @staticmethod
    def CreateMajor(sectionViewId, sectionId, increment, labelStyleId=None):
        """
        CreateMajor(sectionViewId: ObjectId, sectionId: ObjectId, increment: float, labelStyleId: ObjectId) -> ObjectId
        CreateMajor(sectionViewId: ObjectId, sectionId: ObjectId, increment: float) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId, sectionId, includeDerived):
        """ GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: SectionOffsetLabelGroup) -> float

Set: Increment(self: SectionOffsetLabelGroup) = value
"""

    StaggerLineHeight1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight1(self: SectionOffsetLabelGroup) -> float

Set: StaggerLineHeight1(self: SectionOffsetLabelGroup) = value
"""

    StaggerLineHeight2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight2(self: SectionOffsetLabelGroup) -> float

Set: StaggerLineHeight2(self: SectionOffsetLabelGroup) = value
"""


    m_SubData = None


class SectionMinorOffsetLabelGroup(SectionOffsetLabelGroup):
    # no doc
    @staticmethod
    def Create(majorOffsetLabelGroupId, increment, labelGroupStyleId=None):
        """
        Create(majorOffsetLabelGroupId: ObjectId, increment: float, labelGroupStyleId: ObjectId) -> ObjectId
        Create(majorOffsetLabelGroupId: ObjectId, increment: float) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId, sectionId):
        """ GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    MajorOffsetLabelGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorOffsetLabelGroupId(self: SectionMinorOffsetLabelGroup) -> ObjectId

Set: MajorOffsetLabelGroupId(self: SectionMinorOffsetLabelGroup) = value
"""

    RangeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeEnd(self: SectionMinorOffsetLabelGroup) = value
"""

    RangeEndFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeEndFromFeature(self: SectionMinorOffsetLabelGroup) = value
"""

    RangeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeStart(self: SectionMinorOffsetLabelGroup) = value
"""

    RangeStartFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: RangeStartFromFeature(self: SectionMinorOffsetLabelGroup) = value
"""


    m_SubData = None


class SectionOverride(GraphOverride):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverride, A_0: bool) """
        pass

    def GetSectionLabelGroupIds(self):
        """ GetSectionLabelGroupIds(self: SectionOverride) -> ObjectIdCollection """
        pass

    OverrideStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleId(self: SectionOverride) = value
"""

    OverrideStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleName(self: SectionOverride) = value
"""

    SectionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionId(self: SectionOverride) -> ObjectId

"""

    SectionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionName(self: SectionOverride) -> str

"""


    m_pDataLineId = None


class SectionOverrideCollection(GraphOverrideCollection[SectionOverride]):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverrideCollection[SectionOverride], A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionOverrideCollection) -> IEnumerator[SectionOverride] """
        pass

    m_dataVector = None


class SectionPipeNetwork(Section):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: SectionPipeNetwork) -> ObjectId

Set: StyleId(self: SectionPipeNetwork) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: SectionPipeNetwork) -> str

Set: StyleName(self: SectionPipeNetwork) = value
"""



class SectionPoint(CivilWrapper<AeccDbSection>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSection>, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SectionPoint) -> Point3d

"""



class SectionPointCollection(CivilWrapper<AeccDbSection>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSection>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionPointCollection) -> IEnumerator[SectionPoint] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SectionPointCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SectionPoint](enumerable: IEnumerable[SectionPoint], value: SectionPoint) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SectionPointCollection) -> int

"""



class SectionPressurePipeNetwork(Section):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    SourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceId(self: SectionPressurePipeNetwork) -> ObjectId

"""



class SectionProjection(Section):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: SectionProjection) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleName(self: SectionProjection) = value
"""



class SectionProjectionLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(sectionViewId, sectionProjectionId, labelStyleId=None):
        """
        Create(sectionViewId: ObjectId, sectionProjectionId: ObjectId, labelStyleId: ObjectId) -> ObjectId
        Create(sectionViewId: ObjectId, sectionProjectionId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(sectionViewId):
        """ GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ProjectionSourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionSourceId(self: SectionProjectionLabel) -> ObjectId

"""


    m_SubData = None


class SectionSegmentBandLabelGroup(SectionBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId):
        """ GetAvailableLabelGroupIds(sectionViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class SectionSegmentLabelGroup(SectionLabelGroup):
    # no doc
    @staticmethod
    def Create(sectionViewId, sectionId, labelGroupStyleId=None):
        """
        Create(sectionViewId: ObjectId, sectionId: ObjectId, labelGroupStyleId: ObjectId) -> ObjectId
        Create(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(sectionViewId, sectionId):
        """ GetAvailableLabelGroupIds(sectionViewId: ObjectId, sectionId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class SectionSource(object):
    # no doc
    def GetSectionIds(self):
        """ GetSectionIds(self: SectionSource) -> ObjectIdCollection """
        pass

    IsSampled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSampled(self: SectionSource) -> bool

Set: IsSampled(self: SectionSource) = value
"""

    SourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceId(self: SectionSource) -> ObjectId

"""

    SourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceType(self: SectionSource) -> SectionSourceType

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: SectionSource) -> ObjectId

Set: StyleId(self: SectionSource) = value
"""

    UpdateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateMode(self: SectionSource) -> SectionUpdateType

Set: UpdateMode(self: SectionSource) = value
"""



class SectionSourceCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: SectionSourceCollection) -> IEnumerator[SectionSource] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SectionSourceCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SectionSource](enumerable: IEnumerable[SectionSource], value: SectionSource) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SectionSourceCollection) -> int

"""



class SectionSourceType(Enum):
    """ enum SectionSourceType, values: Corridor (2), CorridorSurface (3), Grading (1), GridSurface (6), Material (5), PipeNetwork (4), TinSurface (0) """
    Corridor = None
    CorridorSurface = None
    Grading = None
    GridSurface = None
    Material = None
    PipeNetwork = None
    TinSurface = None
    value__ = None


class SectionUpdateType(Enum):
    """ enum SectionUpdateType, values: Dynamic (1), Static (0) """
    Dynamic = None
    Static = None
    value__ = None


class SectionView(Graph):
    # no doc
    @staticmethod
    def Create(sectionViewName, sampleLineId, location):
        """ Create(sectionViewName: str, sampleLineId: ObjectId, location: Point3d) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def FindOffsetAndElevationAtXY(self, x, y, offset, elevation):
        """ FindOffsetAndElevationAtXY(self: SectionView, x: float, y: float, offset: float, elevation: float) -> (bool, float, float) """
        pass

    def FindXYAtOffsetAndElevation(self, offset, elevation, x, y):
        """ FindXYAtOffsetAndElevation(self: SectionView, offset: float, elevation: float, x: float, y: float) -> (bool, float, float) """
        pass

    def GetPipeSectionLabelIds(self):
        """ GetPipeSectionLabelIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetSectionGradeBreakLabelGroupIds(self):
        """ GetSectionGradeBreakLabelGroupIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetSectionMinorOffsetLabelGroupIds(self):
        """ GetSectionMinorOffsetLabelGroupIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetSectionOffsetLabelGroupIds(self):
        """ GetSectionOffsetLabelGroupIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetSectionProjectionLabelIds(self):
        """ GetSectionProjectionLabelIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetSectionSegmentLabelGroupIds(self):
        """ GetSectionSegmentLabelGroupIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetSectionViewDepthLabelIds(self):
        """ GetSectionViewDepthLabelIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetSectionViewOffsetElevationLabelIds(self):
        """ GetSectionViewOffsetElevationLabelIds(self: SectionView) -> ObjectIdCollection """
        pass

    def GetStructureSectionLabelIds(self):
        """ GetStructureSectionLabelIds(self: SectionView) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Bands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bands(self: SectionView) -> SectionViewBandSet

"""

    ElevationMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationMax(self: SectionView) -> float

Set: ElevationMax(self: SectionView) = value
"""

    ElevationMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationMin(self: SectionView) -> float

Set: ElevationMin(self: SectionView) = value
"""

    GraphOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphOverrides(self: SectionView) -> SectionOverrideCollection

"""

    IsElevationRangeAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsElevationRangeAutomatic(self: SectionView) -> bool

Set: IsElevationRangeAutomatic(self: SectionView) = value
"""

    IsOffsetRangeAutomatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOffsetRangeAutomatic(self: SectionView) -> bool

Set: IsOffsetRangeAutomatic(self: SectionView) = value
"""

    OffsetLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetLeft(self: SectionView) -> float

Set: OffsetLeft(self: SectionView) = value
"""

    OffsetRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetRight(self: SectionView) -> float

Set: OffsetRight(self: SectionView) = value
"""

    ParentEntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentEntityId(self: SectionView) -> ObjectId

"""

    ProfileGradePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileGradePoints(self: SectionView) -> SectionViewProfileGradePointCollection

"""

    VolumeTables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeTables(self: SectionView) -> SectionViewVolumeTableGroup

"""



class SectionViewBandItem(SectionViewBandSetItem):
    # no doc
    SampleLineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineId(self: SectionViewBandItem) -> ObjectId

"""

    Section1Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Section1Id(self: SectionViewBandItem) -> ObjectId

Set: Section1Id(self: SectionViewBandItem) = value
"""

    Section2Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Section2Id(self: SectionViewBandItem) -> ObjectId

Set: Section2Id(self: SectionViewBandItem) = value
"""

    SettingsNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SectionViewBandItemCollection(BandSetItemCollection):
    """ SectionViewBandItemCollection(sectionViewId: ObjectId, location: BandLocationType) """
    def Dispose(self):
        """ Dispose(self: BandSetItemCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionViewBandItemCollection) -> IEnumerator[SectionViewBandItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SectionViewBandItemCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SectionViewBandItem](enumerable: IEnumerable[SectionViewBandItem], value: SectionViewBandItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sectionViewId, location):
        """ __new__(cls: type, sectionViewId: ObjectId, location: BandLocationType) """
        pass


class SectionViewBandSet(GraphBandSet):
    # no doc
    def GetBottomBandItems(self):
        """ GetBottomBandItems(self: SectionViewBandSet) -> SectionViewBandItemCollection """
        pass

    def GetTopBandItems(self):
        """ GetTopBandItems(self: SectionViewBandSet) -> SectionViewBandItemCollection """
        pass

    def SetBottomBandItems(self, bandItems):
        """ SetBottomBandItems(self: SectionViewBandSet, bandItems: SectionViewBandItemCollection) """
        pass

    def SetTopBandItems(self, bandItems):
        """ SetTopBandItems(self: SectionViewBandSet, bandItems: SectionViewBandItemCollection) """
        pass

    m_pGraph = None


class SectionViewDepthLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(sectionViewId, startPoint, endPoint, labelStyleId=None):
        """
        Create(sectionViewId: ObjectId, startPoint: Point2d, endPoint: Point2d, labelStyleId: ObjectId) -> ObjectId
        Create(sectionViewId: ObjectId, startPoint: Point2d, endPoint: Point2d) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(sectionViewId):
        """ GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: SectionViewDepthLabel) -> Point2d

Set: EndPoint(self: SectionViewDepthLabel) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: SectionViewDepthLabel) -> Point2d

Set: StartPoint(self: SectionViewDepthLabel) = value
"""


    m_SubData = None


class SectionViewGroup(object):
    # no doc
    def GetSectionViewIds(self):
        """ GetSectionViewIds(self: SectionViewGroup) -> ObjectIdCollection """
        pass

    IsIndividual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIndividual(self: SectionViewGroup) -> bool

"""

    LayoutName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutName(self: SectionViewGroup) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SectionViewGroup) -> str

"""

    PlotStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotStyleId(self: SectionViewGroup) -> ObjectId

Set: PlotStyleId(self: SectionViewGroup) = value
"""

    SampleLineGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineGroupId(self: SectionViewGroup) -> ObjectId

"""

    TemplateFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemplateFilePath(self: SectionViewGroup) -> str

"""



class SectionViewGroupCollection(object):
    # no doc
    def Add(self, insertPosition, startStation=None, endStation=None, rangeOptions=None, placementOptions=None):
        """
        Add(self: SectionViewGroupCollection, insertPosition: Point3d) -> SectionViewGroup
        Add(self: SectionViewGroupCollection, insertPosition: Point3d, startStation: float, endStation: float, rangeOptions: SectionViewGroupCreationRangeOptions, placementOptions: SectionViewGroupCreationPlacementOptions) -> SectionViewGroup
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionViewGroupCollection) -> IEnumerator[SectionViewGroup] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SectionViewGroupCollection) -> IEnumerator """
        pass

    def Remove(self, sectionViewGroup):
        """ Remove(self: SectionViewGroupCollection, sectionViewGroup: SectionViewGroup) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SectionViewGroupCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SectionViewGroup](enumerable: IEnumerable[SectionViewGroup], value: SectionViewGroup) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SectionViewGroupCollection) -> int

"""



class SectionViewGroupCreationPlacementOptions(object):
    """ SectionViewGroupCreationPlacementOptions() """
    def GetAvailableLayoutNames(self, templateFilePath):
        """ GetAvailableLayoutNames(self: SectionViewGroupCreationPlacementOptions, templateFilePath: str) -> Array[str] """
        pass

    def UseDraftPlacement(self):
        """ UseDraftPlacement(self: SectionViewGroupCreationPlacementOptions) """
        pass

    def UseProductionPlacement(self, templateFilePath, layoutName):
        """ UseProductionPlacement(self: SectionViewGroupCreationPlacementOptions, templateFilePath: str, layoutName: str) """
        pass

    LayoutName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutName(self: SectionViewGroupCreationPlacementOptions) -> str

"""

    PlacementOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlacementOption(self: SectionViewGroupCreationPlacementOptions) -> PlacementOptionType

"""

    TemplateFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemplateFilePath(self: SectionViewGroupCreationPlacementOptions) -> str

"""



class SectionViewGroupCreationRangeOptions(object):
    """ SectionViewGroupCreationRangeOptions(sampleLineGroupId: ObjectId) """
    def Dispose(self):
        """ Dispose(self: SectionViewGroupCreationRangeOptions) """
        pass

    def FollowSection(self, sectionSource):
        """ FollowSection(self: SectionViewGroupCreationRangeOptions, sectionSource: SectionSource) """
        pass

    def SetOffsetRange(self, leftOffset, rightOffset):
        """ SetOffsetRange(self: SectionViewGroupCreationRangeOptions, leftOffset: float, rightOffset: float) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, sampleLineGroupId):
        """ __new__(cls: type, sampleLineGroupId: ObjectId) """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: SectionViewGroupCreationRangeOptions) -> float

Set: Elevation(self: SectionViewGroupCreationRangeOptions) = value
"""

    ElevationRangeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationRangeType(self: SectionViewGroupCreationRangeOptions) -> SectionViewElevationRangeType

Set: ElevationRangeType(self: SectionViewGroupCreationRangeOptions) = value
"""

    LeftOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftOffset(self: SectionViewGroupCreationRangeOptions) -> float

"""

    RightOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightOffset(self: SectionViewGroupCreationRangeOptions) -> float

"""

    UseUserSpecifiedElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseUserSpecifiedElevation(self: SectionViewGroupCreationRangeOptions) -> bool

Set: UseUserSpecifiedElevation(self: SectionViewGroupCreationRangeOptions) = value
"""

    UseUserSpecifiedOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseUserSpecifiedOffset(self: SectionViewGroupCreationRangeOptions) -> bool

Set: UseUserSpecifiedOffset(self: SectionViewGroupCreationRangeOptions) = value
"""



class SectionViewOffsetElevationLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(sectionViewId, offset, elevation, labelStyleId=None, markerStyleId=None):
        """
        Create(sectionViewId: ObjectId, offset: float, elevation: float, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId
        Create(sectionViewId: ObjectId, offset: float, elevation: float) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(sectionViewId):
        """ GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: SectionViewOffsetElevationLabel) -> float

Set: Elevation(self: SectionViewOffsetElevationLabel) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: SectionViewOffsetElevationLabel) -> float

Set: Offset(self: SectionViewOffsetElevationLabel) = value
"""

    Section1Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Section1Id(self: SectionViewOffsetElevationLabel) -> ObjectId

Set: Section1Id(self: SectionViewOffsetElevationLabel) = value
"""

    Section2Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Section2Id(self: SectionViewOffsetElevationLabel) -> ObjectId

Set: Section2Id(self: SectionViewOffsetElevationLabel) = value
"""


    m_SubData = None


class SectionViewProfileGradePoint(object):
    # no doc
    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: SectionViewProfileGradePoint) -> ObjectId

"""

    IsShow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsShow(self: SectionViewProfileGradePoint) -> bool

Set: IsShow(self: SectionViewProfileGradePoint) = value
"""

    MarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleId(self: SectionViewProfileGradePoint) -> ObjectId

Set: MarkerStyleId(self: SectionViewProfileGradePoint) = value
"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: SectionViewProfileGradePoint) -> ObjectId

Set: ProfileId(self: SectionViewProfileGradePoint) = value
"""



class SectionViewProfileGradePointCollection(object):
    # no doc
    def Add(self, alignmentId):
        """ Add(self: SectionViewProfileGradePointCollection, alignmentId: ObjectId) -> SectionViewProfileGradePoint """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionViewProfileGradePointCollection) -> IEnumerator[SectionViewProfileGradePoint] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SectionViewProfileGradePointCollection) -> IEnumerator """
        pass

    def Remove(self, pgPoint):
        """ Remove(self: SectionViewProfileGradePointCollection, pgPoint: SectionViewProfileGradePoint) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SectionViewProfileGradePointCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SectionViewProfileGradePoint](enumerable: IEnumerable[SectionViewProfileGradePoint], value: SectionViewProfileGradePoint) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SectionViewProfileGradePointCollection) -> int

"""



class SectionViewQuantityTakeoffTable(Table):
    # no doc
    def AddSelectedMaterial(self, materialGuid):
        """ AddSelectedMaterial(self: SectionViewQuantityTakeoffTable, materialGuid: Guid) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetSelectedMaterials(self):
        """ GetSelectedMaterials(self: SectionViewQuantityTakeoffTable) -> Array[Guid] """
        pass

    def RemoveSelectedMaterial(self, materialGuid):
        """ RemoveSelectedMaterial(self: SectionViewQuantityTakeoffTable, materialGuid: Guid) -> bool """
        pass

    MaterialListGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialListGuid(self: SectionViewQuantityTakeoffTable) -> Guid

Set: MaterialListGuid(self: SectionViewQuantityTakeoffTable) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SectionViewQuantityTakeoffTable) -> VolumeTableType

"""



class SectionViewVolumeTableAnchorType(Enum):
    """ enum SectionViewVolumeTableAnchorType, values: BottomCenter (7), BottomLeft (6), BottomRight (8), MiddleCenter (4), MiddleLeft (3), MiddleRight (5), TopCenter (1), TopLeft (0), TopRight (2) """
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


class SectionViewVolumeTableGroup(object):
    # no doc
    def CreateVolumeTable(self, type, materialListGuid):
        """ CreateVolumeTable(self: SectionViewVolumeTableGroup, type: VolumeTableType, materialListGuid: Guid) -> ObjectId """
        pass

    def GetVolumeTableIds(self):
        """ GetVolumeTableIds(self: SectionViewVolumeTableGroup) -> ObjectIdCollection """
        pass

    def Swap(self, tableId1, tableId2):
        """ Swap(self: SectionViewVolumeTableGroup, tableId1: ObjectId, tableId2: ObjectId) """
        pass

    def SwapAt(self, index1, index2):
        """ SwapAt(self: SectionViewVolumeTableGroup, index1: int, index2: int) """
        pass

    OffsetX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetX(self: SectionViewVolumeTableGroup) -> float

Set: OffsetX(self: SectionViewVolumeTableGroup) = value
"""

    OffsetY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetY(self: SectionViewVolumeTableGroup) -> float

Set: OffsetY(self: SectionViewVolumeTableGroup) = value
"""

    SectionViewAnchorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewAnchorType(self: SectionViewVolumeTableGroup) -> SectionViewVolumeTableAnchorType

Set: SectionViewAnchorType(self: SectionViewVolumeTableGroup) = value
"""

    TableAnchorType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableAnchorType(self: SectionViewVolumeTableGroup) -> SectionViewVolumeTableAnchorType

Set: TableAnchorType(self: SectionViewVolumeTableGroup) = value
"""

    TableLayoutType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableLayoutType(self: SectionViewVolumeTableGroup) -> SectionViewVolumeTableLayoutType

Set: TableLayoutType(self: SectionViewVolumeTableGroup) = value
"""



class SectionViewVolumeTableLayoutType(Enum):
    """ enum SectionViewVolumeTableLayoutType, values: Horizontal (0), Vertical (1) """
    Horizontal = None
    value__ = None
    Vertical = None


class Shape(CivilWrapper<AeccDbEntity>):
    # no doc
    def AddHole(self, links):
        """ AddHole(self: Shape, links: Array[Link]) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbEntity>, A_0: bool) """
        pass

    Codes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Codes(self: Shape) -> CodeCollection

"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: Shape) -> int

"""

    IsHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHidden(self: Shape) -> bool

Set: IsHidden(self: Shape) = value
"""

    Links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Links(self: Shape) -> LinkCollection

"""



class ShapeCollection(CivilWrapper<AeccDbEntity>):
    # no doc
    def Add(self, *__args):
        """
        Add(self: ShapeCollection, link1: Link, link2: Link, link3: Link, link4: Link, code: str) -> Shape
        Add(self: ShapeCollection, links: Array[Link], code: str) -> Shape
        Add(self: ShapeCollection, link1: Link, link2: Link, link3: Link, link4: Link, codes: Array[str]) -> Shape
        Add(self: ShapeCollection, links: Array[Link], codes: Array[str]) -> Shape
        """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbEntity>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ShapeCollection) -> IEnumerator[Shape] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ShapeCollection) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """ Remove(self: ShapeCollection, index: int)Remove(self: ShapeCollection, shape: Shape) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Shape](enumerable: IEnumerable[Shape], value: Shape) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ShapeCollection) -> int

"""



class Sheet(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class SideRoadProfileDistanceRuleType(Enum):
    """ enum SideRoadProfileDistanceRuleType, values: SpecifyDistance (2), ToIntersectionExtents (1) """
    SpecifyDistance = None
    ToIntersectionExtents = None
    value__ = None


class Site(Entity):
    # no doc
    @staticmethod
    def Create(document, siteName):
        """ Create(document: CivilDocument, siteName: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAlignmentIds(self):
        """ GetAlignmentIds(self: Site) -> ObjectIdCollection """
        pass

    def GetFeatureLineIds(self):
        """ GetFeatureLineIds(self: Site) -> ObjectIdCollection """
        pass

    def GetParcelIds(self):
        """ GetParcelIds(self: Site) -> ObjectIdCollection """
        pass


class SlopeElevationTarget(CivilWrapper<AeccSlopeElevationTarget>):
    """ SlopeElevationTarget(targetId: ObjectId) """
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccSlopeElevationTarget>, A_0: bool) """
        pass

    def GetElevation(self, alignmentId, stationOnAlignment, side=None):
        """
        GetElevation(self: SlopeElevationTarget, alignmentId: ObjectId, stationOnAlignment: float) -> float
        GetElevation(self: SlopeElevationTarget, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide) -> float
        """
        pass

    def GetNearestPipeOfNetworkToAlignment(self, alignmentId, stationOnAlignment, *__args):
        """
        GetNearestPipeOfNetworkToAlignment(self: SlopeElevationTarget, alignmentId: ObjectId, stationOnAlignment: float, pipeId: ObjectId) -> ObjectId
        GetNearestPipeOfNetworkToAlignment(self: SlopeElevationTarget, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide, pipeId: ObjectId) -> ObjectId
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, targetId):
        """ __new__(cls: type, targetId: ObjectId) """
        pass

    TargetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetId(self: SlopeElevationTarget) -> ObjectId

"""



class SpanningPipeLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(partIds, anchorPipeId, ratio=None, labelStyleId=None):
        """
        Create(partIds: ObjectIdCollection, anchorPipeId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId
        Create(partIds: ObjectIdCollection, anchorPipeId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(pipeId):
        """ GetAvailableLabelIds(pipeId: ObjectId) -> ObjectIdCollection """
        pass

    AnchorPipeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorPipeId(self: SpanningPipeLabel) -> ObjectId

Set: AnchorPipeId(self: SpanningPipeLabel) = value
"""

    Length2DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2DCenterToCenter(self: SpanningPipeLabel) -> float

"""

    Length2DEdgeToEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2DEdgeToEdge(self: SpanningPipeLabel) -> float

"""

    Length3DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3DCenterToCenter(self: SpanningPipeLabel) -> float

"""

    Length3DEdgeToEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3DEdgeToEdge(self: SpanningPipeLabel) -> float

"""

    PipeIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeIds(self: SpanningPipeLabel) -> ObjectIdCollection

"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: SpanningPipeLabel) -> float

Set: Ratio(self: SpanningPipeLabel) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: SpanningPipeLabel) -> ObjectId

Set: ReferenceAlignmentId(self: SpanningPipeLabel) = value
"""

    ShowSpannedPipes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowSpannedPipes(self: SpanningPipeLabel) -> bool

Set: ShowSpannedPipes(self: SpanningPipeLabel) = value
"""

    StructureIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureIds(self: SpanningPipeLabel) -> ObjectIdCollection

"""


    m_SubData = None


class SpanningPipeProfileLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(profileViewPartIds, anchorProfileViewPartId, profileViewId, ratio=None, labelStyleId=None):
        """
        Create(profileViewPartIds: ObjectIdCollection, anchorProfileViewPartId: ObjectId, profileViewId: ObjectId, ratio: float, labelStyleId: ObjectId) -> ObjectId
        Create(profileViewPartIds: ObjectIdCollection, anchorProfileViewPartId: ObjectId, profileViewId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(profileViewId):
        """ GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    AnchorProfileViewPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorProfileViewPartId(self: SpanningPipeProfileLabel) -> ObjectId

Set: AnchorProfileViewPartId(self: SpanningPipeProfileLabel) = value
"""

    Length2DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2DCenterToCenter(self: SpanningPipeProfileLabel) -> float

"""

    Length2DEdgeToEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length2DEdgeToEdge(self: SpanningPipeProfileLabel) -> float

"""

    Length3DCenterToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3DCenterToCenter(self: SpanningPipeProfileLabel) -> float

"""

    Length3DEdgeToEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length3DEdgeToEdge(self: SpanningPipeProfileLabel) -> float

"""

    ProfileViewPipeIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewPipeIds(self: SpanningPipeProfileLabel) -> ObjectIdCollection

"""

    ProfileViewStructureIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewStructureIds(self: SpanningPipeProfileLabel) -> ObjectIdCollection

"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: SpanningPipeProfileLabel) -> float

Set: Ratio(self: SpanningPipeProfileLabel) = value
"""

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: SpanningPipeProfileLabel) -> ObjectId

Set: ReferenceAlignmentId(self: SpanningPipeProfileLabel) = value
"""

    ShowSpannedProfileViewPipes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowSpannedProfileViewPipes(self: SpanningPipeProfileLabel) -> bool

Set: ShowSpannedProfileViewPipes(self: SpanningPipeProfileLabel) = value
"""


    m_SubData = None


class SpiralCurveType(Enum):
    """ enum SpiralCurveType, values: InCurve (261), OutCurve (262) """
    InCurve = None
    OutCurve = None
    value__ = None


class SpiralDirectionType(Enum):
    """ enum SpiralDirectionType, values: DirectionLeft (1), DirectionRight (0) """
    DirectionLeft = None
    DirectionRight = None
    value__ = None


class SpiralParamType(Enum):
    """ enum SpiralParamType, values: AValue (0), Length (1) """
    AValue = None
    Length = None
    value__ = None


class SplitProfileViewCreationOptions(object):
    """ SplitProfileViewCreationOptions(viewHeight: float, firstViewStyleId: ObjectId, intermediateViewStyleId: ObjectId, lastViewStyleId: ObjectId) """
    @staticmethod # known case of __new__
    def __new__(self, viewHeight, firstViewStyleId, intermediateViewStyleId, lastViewStyleId):
        """ __new__(cls: type, viewHeight: float, firstViewStyleId: ObjectId, intermediateViewStyleId: ObjectId, lastViewStyleId: ObjectId) """
        pass

    FirstViewStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstViewStyleId(self: SplitProfileViewCreationOptions) -> ObjectId

Set: FirstViewStyleId(self: SplitProfileViewCreationOptions) = value
"""

    IntermediateViewStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntermediateViewStyleId(self: SplitProfileViewCreationOptions) -> ObjectId

Set: IntermediateViewStyleId(self: SplitProfileViewCreationOptions) = value
"""

    LastViewStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastViewStyleId(self: SplitProfileViewCreationOptions) -> ObjectId

Set: LastViewStyleId(self: SplitProfileViewCreationOptions) = value
"""

    SplitDatumOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitDatumOption(self: SplitProfileViewCreationOptions) -> ProfileViewSplitDatumType

Set: SplitDatumOption(self: SplitProfileViewCreationOptions) = value
"""

    SplitStationOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitStationOption(self: SplitProfileViewCreationOptions) -> ProfileViewSplitStationType

Set: SplitStationOption(self: SplitProfileViewCreationOptions) = value
"""

    ViewHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewHeight(self: SplitProfileViewCreationOptions) -> float

Set: ViewHeight(self: SplitProfileViewCreationOptions) = value
"""



class SplitStationType(Enum):
    """ enum SplitStationType, values: Automatic (0), Manual (1) """
    Automatic = None
    Manual = None
    value__ = None


class StackedProfileViewsCreationOptions(object):
    """ StackedProfileViewsCreationOptions(topViewStyleId: ObjectId, middleViewStyleId: ObjectId, bottomViewStyleId: ObjectId) """
    @staticmethod # known case of __new__
    def __new__(self, topViewStyleId, middleViewStyleId, bottomViewStyleId):
        """ __new__(cls: type, topViewStyleId: ObjectId, middleViewStyleId: ObjectId, bottomViewStyleId: ObjectId) """
        pass

    BottomViewStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomViewStyleId(self: StackedProfileViewsCreationOptions) -> ObjectId

Set: BottomViewStyleId(self: StackedProfileViewsCreationOptions) = value
"""

    GapBetweenViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GapBetweenViews(self: StackedProfileViewsCreationOptions) -> float

Set: GapBetweenViews(self: StackedProfileViewsCreationOptions) = value
"""

    MiddleViewStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiddleViewStyleId(self: StackedProfileViewsCreationOptions) -> ObjectId

Set: MiddleViewStyleId(self: StackedProfileViewsCreationOptions) = value
"""

    NumberOfViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfViews(self: StackedProfileViewsCreationOptions) -> int

Set: NumberOfViews(self: StackedProfileViewsCreationOptions) = value
"""

    TopViewStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopViewStyleId(self: StackedProfileViewsCreationOptions) -> ObjectId

Set: TopViewStyleId(self: StackedProfileViewsCreationOptions) = value
"""



class StandardPointGroupQuery(PointGroupQuery):
    """ StandardPointGroupQuery() """
    ExcludeElevations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeElevations(self: StandardPointGroupQuery) -> str

Set: ExcludeElevations(self: StandardPointGroupQuery) = value
"""

    ExcludeFullDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeFullDescriptions(self: StandardPointGroupQuery) -> str

Set: ExcludeFullDescriptions(self: StandardPointGroupQuery) = value
"""

    ExcludeNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeNames(self: StandardPointGroupQuery) -> str

Set: ExcludeNames(self: StandardPointGroupQuery) = value
"""

    ExcludeNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeNumbers(self: StandardPointGroupQuery) -> str

Set: ExcludeNumbers(self: StandardPointGroupQuery) = value
"""

    ExcludeRawDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeRawDescriptions(self: StandardPointGroupQuery) -> str

Set: ExcludeRawDescriptions(self: StandardPointGroupQuery) = value
"""

    IncludeAllPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeAllPoints(self: StandardPointGroupQuery) -> bool

Set: IncludeAllPoints(self: StandardPointGroupQuery) = value
"""

    IncludeElevations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeElevations(self: StandardPointGroupQuery) -> str

Set: IncludeElevations(self: StandardPointGroupQuery) = value
"""

    IncludeFullDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeFullDescriptions(self: StandardPointGroupQuery) -> str

Set: IncludeFullDescriptions(self: StandardPointGroupQuery) = value
"""

    IncludeNames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeNames(self: StandardPointGroupQuery) -> str

Set: IncludeNames(self: StandardPointGroupQuery) = value
"""

    IncludeNumbers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeNumbers(self: StandardPointGroupQuery) -> str

Set: IncludeNumbers(self: StandardPointGroupQuery) = value
"""

    IncludeRawDescriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludeRawDescriptions(self: StandardPointGroupQuery) -> str

Set: IncludeRawDescriptions(self: StandardPointGroupQuery) = value
"""

    PointGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointGroups(self: StandardPointGroupQuery) -> IList[str]

"""


    _curBuilder = None
    _curPG = None


class Station(object):
    """ Station() """
    GeometryStationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryStationType(self: Station) -> AlignmentGeometryPointStationType

Set: GeometryStationType(self: Station) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Station) -> Point2d

Set: Location(self: Station) = value
"""

    RawStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawStation(self: Station) -> float

Set: RawStation(self: Station) = value
"""

    StationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationType(self: Station) -> StationTypes

Set: StationType(self: Station) = value
"""



class StationElevationLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(profileViewId, labelStyleId, markerStyleId, station, elevation):
        """ Create(profileViewId: ObjectId, labelStyleId: ObjectId, markerStyleId: ObjectId, station: float, elevation: float) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: StationElevationLabel) -> float

"""

    Profile1Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile1Id(self: StationElevationLabel) -> ObjectId

Set: Profile1Id(self: StationElevationLabel) = value
"""

    Profile2Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile2Id(self: StationElevationLabel) -> ObjectId

Set: Profile2Id(self: StationElevationLabel) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: StationElevationLabel) -> float

"""


    m_SubData = None


class StationEquation(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    EquationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EquationType(self: StationEquation) -> StationEquationType

Set: EquationType(self: StationEquation) = value
"""

    RawStationBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawStationBack(self: StationEquation) -> float

Set: RawStationBack(self: StationEquation) = value
"""

    StationAhead = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationAhead(self: StationEquation) -> float

Set: StationAhead(self: StationEquation) = value
"""

    StationBack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationBack(self: StationEquation) -> float

"""



class StationEquationCollection(CivilWrapper<AeccDbAlignment>):
    # no doc
    def Add(self, rawStationBack, stationAhead, stationEquationType):
        """ Add(self: StationEquationCollection, rawStationBack: float, stationAhead: float, stationEquationType: StationEquationType) -> StationEquation """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignment>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: StationEquationCollection) -> IEnumerator[StationEquation] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: StationEquationCollection) -> IEnumerator """
        pass

    def GetStationEquation(self, rawStationBack):
        """ GetStationEquation(self: StationEquationCollection, rawStationBack: float) -> StationEquation """
        pass

    def Remove(self, *__args):
        """ Remove(self: StationEquationCollection, index: int)Remove(self: StationEquationCollection, rawStationBack: float) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[StationEquation](enumerable: IEnumerable[StationEquation], value: StationEquation) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: StationEquationCollection) -> int

"""



class StationEquationType(Enum):
    """ enum StationEquationType, values: Decreasing (0), Increasing (1) """
    Decreasing = None
    Increasing = None
    value__ = None


class StationOffsetLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(alignmentId, labelStyleId, markerStyleId, location):
        """ Create(alignmentId: ObjectId, labelStyleId: ObjectId, markerStyleId: ObjectId, location: Point2d) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    AnchorAtXY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorAtXY(self: StationOffsetLabel) -> bool

Set: AnchorAtXY(self: StationOffsetLabel) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: StationOffsetLabel) -> Point2d

Set: Location(self: StationOffsetLabel) = value
"""


    m_SubData = None


class StationRangeType(Enum):
    """ enum StationRangeType, values: Automatic (0), UserSpecified (1) """
    Automatic = None
    UserSpecified = None
    value__ = None


class StationRoundingType(Enum):
    """ enum StationRoundingType, values: ExactStation (8), PreviousMajorGrid (2), PreviousMinorGrid (4) """
    ExactStation = None
    PreviousMajorGrid = None
    PreviousMinorGrid = None
    value__ = None


class StationTypes(Enum):
    """ enum (flags) StationTypes, values: All (-1), CurveAtIncrement (4096), CurveByCurvature (1024), Equation (16), GeometryPoint (8), HorizontalMask (8191), Major (1), Minor (2), OffsetTargetCurveOnly (2048), PIPoint (65536), RangeEnd (64), RangeStart (32), SuperTransPoint (128) """
    All = None
    CurveAtIncrement = None
    CurveByCurvature = None
    Equation = None
    GeometryPoint = None
    HorizontalMask = None
    Major = None
    Minor = None
    OffsetTargetCurveOnly = None
    PIPoint = None
    RangeEnd = None
    RangeStart = None
    SuperTransPoint = None
    value__ = None


class Structure(Part):
    # no doc
    def ConnectToPipe(self, pipeId, positionType):
        """ ConnectToPipe(self: Structure, pipeId: ObjectId, positionType: ConnectorPositionType) """
        pass

    def Disconnect(self, pipeId):
        """ Disconnect(self: Structure, pipeId: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: Part, A_0: bool) """
        pass

    def GetAvailableStructureLabelIds(self):
        """ GetAvailableStructureLabelIds(self: Structure) -> ObjectIdCollection """
        pass

    def GetConnectedPipeNames(self):
        """ GetConnectedPipeNames(self: Structure) -> Array[str] """
        pass

    def GetLabelIds(self):
        """ GetLabelIds(self: Structure) -> ObjectIdCollection """
        pass

    def IsConnectedPipeFlowingIn(self, index):
        """ IsConnectedPipeFlowingIn(self: Structure, index: int) -> bool """
        pass

    def IsConnectedPipeFlowingOut(self, index):
        """ IsConnectedPipeFlowingOut(self: Structure, index: int) -> bool """
        pass

    def IsPointInsideStructureRegion(self, point):
        """ IsPointInsideStructureRegion(self: Structure, point: Point3d) -> bool """
        pass

    def ResizeByPipeDepths(self):
        """ ResizeByPipeDepths(self: Structure) -> bool """
        pass

    def ResizeJunctionStructure(self, partFamilyGuid, rimElevation, sumpElevation):
        """ ResizeJunctionStructure(self: Structure, partFamilyGuid: str, rimElevation: float, sumpElevation: float) """
        pass

    AutomaticRimSurfaceAdjustment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticRimSurfaceAdjustment(self: Structure) -> bool

Set: AutomaticRimSurfaceAdjustment(self: Structure) = value
"""

    BarrelPipeClearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BarrelPipeClearance(self: Structure) -> float

"""

    BoundingShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingShape(self: Structure) -> BoundingShapeType

"""

    ConeHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConeHeight(self: Structure) -> float

"""

    ConnectedPipesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectedPipesCount(self: Structure) -> int

"""

    ControlSumpBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlSumpBy(self: Structure) -> StructureControlSumpType

Set: ControlSumpBy(self: Structure) = value
"""

    Cover = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cover(self: Structure) -> str

"""

    DiameterOrWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiameterOrWidth(self: Structure) -> float

"""

    Easting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Easting(self: Structure) -> float

Set: Easting(self: Structure) = value
"""

    FloorThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FloorThickness(self: Structure) -> float

"""

    Frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Frame(self: Structure) -> str

"""

    FrameDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameDiameter(self: Structure) -> float

"""

    FrameHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameHeight(self: Structure) -> float

"""

    Grate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grate(self: Structure) -> str

"""

    HeadwallBaseThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadwallBaseThickness(self: Structure) -> float

"""

    HeadwallBaseWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeadwallBaseWidth(self: Structure) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: Structure) -> float

"""

    InnerDiameterOrWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerDiameterOrWidth(self: Structure) -> float

"""

    InnerLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerLength(self: Structure) -> float

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Structure) -> float

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Structure) -> Point3d

Set: Location(self: Structure) = value
"""

    Northing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Northing(self: Structure) -> float

Set: Northing(self: Structure) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: Structure) -> float

"""

    PipeLowestBottomDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeLowestBottomDepth(self: Structure) -> float

"""

    PipeUpperTopDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeUpperTopDepth(self: Structure) -> float

"""

    RimElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RimElevation(self: Structure) -> float

Set: RimElevation(self: Structure) = value
"""

    RimToSumpHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RimToSumpHeight(self: Structure) -> float

Set: RimToSumpHeight(self: Structure) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: Structure) -> float

Set: Rotation(self: Structure) = value
"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: Structure) -> float

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: StyleId(self: Structure) = value
"""

    SumpDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SumpDepth(self: Structure) -> float

Set: SumpDepth(self: Structure) = value
"""

    SumpElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SumpElevation(self: Structure) -> float

Set: SumpElevation(self: Structure) = value
"""

    SurfaceAdjustmentValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceAdjustmentValue(self: Structure) -> float

Set: SurfaceAdjustmentValue(self: Structure) = value
"""

    SurfaceElevationAtInsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceElevationAtInsertionPoint(self: Structure) -> float

"""

    VerticalPipeClearance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalPipeClearance(self: Structure) -> float

"""



class StructureControlSumpType(Enum):
    """ enum StructureControlSumpType, values: ByDepth (0), ByElevation (1) """
    ByDepth = None
    ByElevation = None
    value__ = None


class StructureLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(structureId, labelStyleId=None, labelLocation=None):
        """
        Create(structureId: ObjectId, labelStyleId: ObjectId, labelLocation: Point3d) -> ObjectId
        Create(structureId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(structureId):
        """ GetAvailableLabelIds(structureId: ObjectId) -> ObjectIdCollection """
        pass

    ReferenceAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceAlignmentId(self: StructureLabel) -> ObjectId

Set: ReferenceAlignmentId(self: StructureLabel) = value
"""


    m_SubData = None


class StructureOverride(GraphOverride):
    # no doc
    def Dispose(self):
        """ Dispose(self: GraphOverride, A_0: bool) """
        pass

    Draw = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Draw(self: StructureOverride) = value
"""

    OverrideStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleId(self: StructureOverride) = value
"""

    OverrideStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: OverrideStyleName(self: StructureOverride) = value
"""

    StructId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructId(self: StructureOverride) -> ObjectId

"""

    StructName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructName(self: StructureOverride) -> str

"""


    m_pDataLineId = None


class StructureOverrideCollection(GraphOverrideCollection[StructureOverride]):
    # no doc
    def Dispose(self):
        """ Dispose(self: StructureOverrideCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: StructureOverrideCollection) -> IEnumerator[StructureOverride] """
        pass

    SplitAt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SplitAt(self: StructureOverrideCollection) -> str

Set: SplitAt(self: StructureOverrideCollection) = value
"""


    m_dataVector = None


class StructureProfileLabel(PartProfileLabel):
    # no doc
    @staticmethod
    def Create(profileViewId, profileViewPartId, labelStyleId=None):
        """
        Create(profileViewId: ObjectId, profileViewPartId: ObjectId, labelStyleId: ObjectId) -> ObjectId
        Create(profileViewId: ObjectId, profileViewPartId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(profileViewId):
        """ GetAvailableLabelIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    m_SubData = None


class StructureSectionLabel(PartSectionLabel):
    # no doc
    @staticmethod
    def Create(sectionViewId, structureId, sectionPipeNetworkId, partIndex, labelStyleId=None):
        """
        Create(sectionViewId: ObjectId, structureId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: int, labelStyleId: ObjectId) -> ObjectId
        Create(sectionViewId: ObjectId, structureId: ObjectId, sectionPipeNetworkId: ObjectId, partIndex: int) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelIds(sectionViewId):
        """ GetAvailableLabelIds(sectionViewId: ObjectId) -> ObjectIdCollection """
        pass

    m_SubData = None


class Subassembly(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def EraseAllParams(self):
        """ EraseAllParams(self: Subassembly) """
        pass

    def GetResourceString(self, resourceId):
        """
        GetResourceString(self: Subassembly, resourceId: UInt32) -> str
        GetResourceString(self: Subassembly, resourceId: str) -> str
        """
        pass

    def Run(self):
        """ Run(self: Subassembly) """
        pass

    def ShowHelp(self):
        """ ShowHelp(self: Subassembly) """
        pass

    AssemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyId(self: Subassembly) -> ObjectId

"""

    AttachedToOffsetAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttachedToOffsetAssembly(self: Subassembly) -> bool

"""

    CodeSetStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeSetStyleName(self: Subassembly) -> str

Set: CodeSetStyleName(self: Subassembly) = value
"""

    DefaultLoopInLayoutMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultLoopInLayoutMode(self: Subassembly) -> bool

Set: DefaultLoopInLayoutMode(self: Subassembly) = value
"""

    DefaultLoopOffsetInLayoutMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultLoopOffsetInLayoutMode(self: Subassembly) -> float

Set: DefaultLoopOffsetInLayoutMode(self: Subassembly) = value
"""

    GeometryGenerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryGenerator(self: Subassembly) -> SubassemblyGenerator

Set: GeometryGenerator(self: Subassembly) = value
"""

    HasParentAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasParentAssembly(self: Subassembly) -> bool

"""

    HasSide = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasSide(self: Subassembly) -> bool

"""

    HelpCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpCommand(self: Subassembly) -> str

Set: HelpCommand(self: Subassembly) = value
"""

    HelpData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpData(self: Subassembly) -> str

Set: HelpData(self: Subassembly) = value
"""

    HelpFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpFile(self: Subassembly) -> str

Set: HelpFile(self: Subassembly) = value
"""

    IsDynamic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDynamic(self: Subassembly) -> bool

"""

    Links = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Links(self: Subassembly) -> LinkCollection

"""

    OffsetAssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetAssemblyName(self: Subassembly) -> str

"""

    OffsetToAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetToAssembly(self: Subassembly) -> Vector2d

Set: OffsetToAssembly(self: Subassembly) = value
"""

    OffsetToBaseline = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetToBaseline(self: Subassembly) -> Vector2d

"""

    OffsetToParentAssembly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetToParentAssembly(self: Subassembly) -> Vector2d

Set: OffsetToParentAssembly(self: Subassembly) = value
"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: Subassembly) -> Point3d

Set: Origin(self: Subassembly) = value
"""

    ParamsBool = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsBool(self: Subassembly) -> ParamBoolCollection

"""

    ParamsDouble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsDouble(self: Subassembly) -> ParamDoubleCollection

"""

    ParamsLong = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsLong(self: Subassembly) -> ParamLongCollection

"""

    ParamsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamsString(self: Subassembly) -> ParamStringCollection

"""

    PointIndexHookTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointIndexHookTo(self: Subassembly) -> int

Set: PointIndexHookTo(self: Subassembly) = value
"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: Subassembly) -> PointCollection

"""

    ResourceModule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResourceModule(self: Subassembly) -> str

Set: ResourceModule(self: Subassembly) = value
"""

    Shapes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shapes(self: Subassembly) -> ShapeCollection

"""

    Side = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Side(self: Subassembly) -> SubassemblySideType

Set: Side(self: Subassembly) = value
"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: Subassembly) -> str

"""

    SubassemblyHookTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubassemblyHookTo(self: Subassembly) -> ObjectId

"""

    UseEmbeddedProject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseEmbeddedProject(self: Subassembly) -> bool

Set: UseEmbeddedProject(self: Subassembly) = value
"""



class SubassemblyCollection(CivilWrapper<AcDbDatabase>):
    # no doc
    def Add(self, subassemblyName, entityId, midOrdinateDist, linkCreationOption):
        """ Add(self: SubassemblyCollection, subassemblyName: str, entityId: ObjectId, midOrdinateDist: float, linkCreationOption: LinkCreationType) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AcDbDatabase>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SubassemblyCollection) -> IEnumerator[ObjectId] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SubassemblyCollection) -> IEnumerator """
        pass

    def GetSubassemblyIdsByName(self, subassemblyName):
        """ GetSubassemblyIdsByName(self: SubassemblyCollection, subassemblyName: str) -> ObjectIdCollection """
        pass

    def ImportStockSubassembly(self, subassemblyName, className, location):
        """ ImportStockSubassembly(self: SubassemblyCollection, subassemblyName: str, className: str, location: Point3d) -> ObjectId """
        pass

    def ImportSubassembly(self, subassemblyName, atcFilePath, itemId, location):
        """ ImportSubassembly(self: SubassemblyCollection, subassemblyName: str, atcFilePath: str, itemId: str, location: Point3d) -> ObjectId """
        pass

    def Remove(self, subassemblyId):
        """ Remove(self: SubassemblyCollection, subassemblyId: ObjectId) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SubassemblyCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerable: IEnumerable[ObjectId], value: ObjectId) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SubassemblyCollection) -> int

"""



class SubassemblyGenerator(object):
    """ SubassemblyGenerator(mode: SubassemblyGeometryGenerateMode, projectOrAssemblyName: str, macroOrClassName: str) """
    @staticmethod # known case of __new__
    def __new__(self, mode, projectOrAssemblyName, macroOrClassName):
        """ __new__(cls: type, mode: SubassemblyGeometryGenerateMode, projectOrAssemblyName: str, macroOrClassName: str) """
        pass

    GeometryGenerateMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryGenerateMode(self: SubassemblyGenerator) -> SubassemblyGeometryGenerateMode

Set: GeometryGenerateMode(self: SubassemblyGenerator) = value
"""

    MacroOrClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MacroOrClassName(self: SubassemblyGenerator) -> str

Set: MacroOrClassName(self: SubassemblyGenerator) = value
"""

    ProjectOrAssemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectOrAssemblyName(self: SubassemblyGenerator) -> str

Set: ProjectOrAssemblyName(self: SubassemblyGenerator) = value
"""



class SubassemblyGeometryGenerateMode(Enum):
    """ enum SubassemblyGeometryGenerateMode, values: HardCoded (0), UseCOM (2), UseDotNet (3), UseVBA (1) """
    HardCoded = None
    UseCOM = None
    UseDotNet = None
    UseVBA = None
    value__ = None


class SubassemblyLogicalNameType(Enum):
    """ enum SubassemblyLogicalNameType, values: Alignment (2), Elevation (5), ElevationPipe (7), Offset (4), OffsetPipe (6), Profile (3), Surface (1) """
    Alignment = None
    Elevation = None
    ElevationPipe = None
    Offset = None
    OffsetPipe = None
    Profile = None
    Surface = None
    value__ = None


class SubassemblySideType(Enum):
    """ enum SubassemblySideType, values: Left (0), Right (1) """
    Left = None
    Right = None
    value__ = None


class SubassemblyTargetInfo(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AssemblyGroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyGroupName(self: SubassemblyTargetInfo) -> str

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: SubassemblyTargetInfo) -> str

"""

    LogicalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogicalName(self: SubassemblyTargetInfo) -> str

"""

    SubassemblyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubassemblyName(self: SubassemblyTargetInfo) -> str

"""

    TargetIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetIds(self: SubassemblyTargetInfo) -> ObjectIdCollection

Set: TargetIds(self: SubassemblyTargetInfo) = value
"""

    TargetToOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetToOption(self: SubassemblyTargetInfo) -> SubassemblyTargetToOption

Set: TargetToOption(self: SubassemblyTargetInfo) = value
"""

    TargetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetType(self: SubassemblyTargetInfo) -> SubassemblyLogicalNameType

"""



class SubassemblyTargetInfoCollection(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SubassemblyTargetInfoCollection) -> IEnumerator[SubassemblyTargetInfo] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SubassemblyTargetInfoCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SubassemblyTargetInfo](enumerable: IEnumerable[SubassemblyTargetInfo], value: SubassemblyTargetInfo) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SubassemblyTargetInfoCollection) -> int

"""



class SubassemblyTargetToOption(Enum):
    """ enum SubassemblyTargetToOption, values: Farthest (2), Flattest (3), Nearest (1), Steepest (4) """
    Farthest = None
    Flattest = None
    Nearest = None
    Steepest = None
    value__ = None


class SuperElevationBandLabelGroup(ProfileBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class SuperelevationCriticalStation(object):
    # no doc
    def BreakSegment(self, crossSegmentType):
        """ BreakSegment(self: SuperelevationCriticalStation, crossSegmentType: SuperelevationCrossSegmentType) """
        pass

    def GetSlope(self, crossSegmentType):
        """ GetSlope(self: SuperelevationCriticalStation, crossSegmentType: SuperelevationCrossSegmentType) -> float """
        pass

    def GetSmoothingLength(self, crossSegmentType):
        """ GetSmoothingLength(self: SuperelevationCriticalStation, crossSegmentType: SuperelevationCrossSegmentType) -> float """
        pass

    def IsGradeBreak(self, crossSegmentType):
        """ IsGradeBreak(self: SuperelevationCriticalStation, crossSegmentType: SuperelevationCrossSegmentType) -> bool """
        pass

    def RemoveGradeBreak(self, crossSegmentType):
        """ RemoveGradeBreak(self: SuperelevationCriticalStation, crossSegmentType: SuperelevationCrossSegmentType) """
        pass

    def SetSlope(self, crossSegmentType, slope):
        """ SetSlope(self: SuperelevationCriticalStation, crossSegmentType: SuperelevationCrossSegmentType, slope: float) """
        pass

    def SetSmoothingLength(self, crossSegmentType, length):
        """ SetSmoothingLength(self: SuperelevationCriticalStation, crossSegmentType: SuperelevationCrossSegmentType, length: float) """
        pass

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: SuperelevationCriticalStation) -> ObjectId

"""

    Station = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Station(self: SuperelevationCriticalStation) -> float

Set: Station(self: SuperelevationCriticalStation) = value
"""

    StationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationType(self: SuperelevationCriticalStation) -> SuperelevationCriticalStationType

"""

    SuperelevationCurveName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperelevationCurveName(self: SuperelevationCriticalStation) -> str

"""

    TransitionDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionDescription(self: SuperelevationCriticalStation) -> str

Set: TransitionDescription(self: SuperelevationCriticalStation) = value
"""

    TransitionRegionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransitionRegionType(self: SuperelevationCriticalStation) -> SuperelevationTransitionRegionType

"""



class SuperelevationCriticalStationCollection(object):
    # no doc
    def Add(self, station, criticalStationType, attainmentRegionType=None):
        """ Add(self: SuperelevationCriticalStationCollection, station: float, criticalStationType: SuperelevationCriticalStationType)Add(self: SuperelevationCriticalStationCollection, station: float, criticalStationType: SuperelevationCriticalStationType, attainmentRegionType: SuperelevationAttainmentRegionType) """
        pass

    def GetCriticalStationAt(self, station, tolerance):
        """ GetCriticalStationAt(self: SuperelevationCriticalStationCollection, station: float, tolerance: float) -> SuperelevationCriticalStation """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SuperelevationCriticalStationCollection) -> IEnumerator[SuperelevationCriticalStation] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SuperelevationCriticalStationCollection) -> IEnumerator """
        pass

    def IsCriticalStation(self, station, tolerance):
        """ IsCriticalStation(self: SuperelevationCriticalStationCollection, station: float, tolerance: float) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SuperelevationCriticalStationCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SuperelevationCriticalStation](enumerable: IEnumerable[SuperelevationCriticalStation], value: SuperelevationCriticalStation) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SuperelevationCriticalStationCollection) -> int

"""

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: SuperelevationCriticalStationCollection) -> ObjectId

"""



class SuperelevationCurve(SECurve):
    # no doc

class SuperelevationCurveCollection(object):
    # no doc
    def AddUserDefinedCurve(self, startSubEntity, endSubEntity):
        """ AddUserDefinedCurve(self: SuperelevationCurveCollection, startSubEntity: AlignmentSubEntity, endSubEntity: AlignmentSubEntity) -> SuperelevationCurve """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SuperelevationCurveCollection) -> IEnumerator[SuperelevationCurve] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SuperelevationCurveCollection) -> IEnumerator """
        pass

    @staticmethod
    def ImportSuperelevationDataFromFile(fileName, alignmentId, acceptGarbage):
        """ ImportSuperelevationDataFromFile(fileName: str, alignmentId: ObjectId, acceptGarbage: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SuperelevationCurve](enumerable: IEnumerable[SuperelevationCurve], value: SuperelevationCurve) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SuperelevationCurveCollection) -> int

"""

    ParentAlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentAlignmentId(self: SuperelevationCurveCollection) -> ObjectId

"""



class SuperelevationType(Enum):
    """ enum SuperelevationType, values: Cant (3), NotSupported (1), Superelevation (2) """
    Cant = None
    NotSupported = None
    Superelevation = None
    value__ = None


class SurfaceAnalysis(object):
    # no doc
    def CreateWaterdrop(self, location, objectType):
        """ CreateWaterdrop(self: SurfaceAnalysis, location: Point2d, objectType: WaterdropObjectType) -> ObjectIdCollection """
        pass

    def Dispose(self):
        """ Dispose(self: SurfaceAnalysis) """
        pass

    def GetContourData(self):
        """ GetContourData(self: SurfaceAnalysis) -> Array[SurfaceAnalysisContourData] """
        pass

    def GetDirectionData(self):
        """ GetDirectionData(self: SurfaceAnalysis) -> Array[SurfaceAnalysisDirectionData] """
        pass

    def GetElevationData(self):
        """ GetElevationData(self: SurfaceAnalysis) -> Array[SurfaceAnalysisElevationData] """
        pass

    def GetSlopeArrowData(self):
        """ GetSlopeArrowData(self: SurfaceAnalysis) -> Array[SurfaceAnalysisSlopeArrowData] """
        pass

    def GetSlopeData(self):
        """ GetSlopeData(self: SurfaceAnalysis) -> Array[SurfaceAnalysisSlopeData] """
        pass

    def GetUserDefinedContourData(self):
        """ GetUserDefinedContourData(self: SurfaceAnalysis) -> Array[SurfaceAnalysisUserDefinedContourData] """
        pass

    def GetWatershedData(self):
        """ GetWatershedData(self: SurfaceAnalysis) -> SurfaceAnalysisWatershedDataCollection """
        pass

    def SetContourData(self, analysisData):
        """ SetContourData(self: SurfaceAnalysis, analysisData: Array[SurfaceAnalysisContourData]) """
        pass

    def SetDirectionData(self, analysisData):
        """ SetDirectionData(self: SurfaceAnalysis, analysisData: Array[SurfaceAnalysisDirectionData]) """
        pass

    def SetElevationData(self, analysisData):
        """ SetElevationData(self: SurfaceAnalysis, analysisData: Array[SurfaceAnalysisElevationData]) """
        pass

    def SetSlopeArrowData(self, analysisData):
        """ SetSlopeArrowData(self: SurfaceAnalysis, analysisData: Array[SurfaceAnalysisSlopeArrowData]) """
        pass

    def SetSlopeData(self, analysisData):
        """ SetSlopeData(self: SurfaceAnalysis, analysisData: Array[SurfaceAnalysisSlopeData]) """
        pass

    def SetUserDefinedContourData(self, analysisData):
        """ SetUserDefinedContourData(self: SurfaceAnalysis, analysisData: Array[SurfaceAnalysisUserDefinedContourData]) """
        pass

    def SetWatershedData(self, analysisData):
        """ SetWatershedData(self: SurfaceAnalysis, analysisData: SurfaceAnalysisWatershedDataCollection) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class SurfaceAnalysisContourData(object):
    """
    SurfaceAnalysisContourData(minimumElevation: float, maximumElevation: float, contourValue: ContourValues)
    SurfaceAnalysisContourData()
    """
    def Initialize(self, codeValue):
        """ Initialize(self: SurfaceAnalysisContourData, codeValue: ColorValue*) """
        pass

    def Update(self, codeValue):
        """ Update(self: SurfaceAnalysisContourData, codeValue: ColorValue*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, minimumElevation=None, maximumElevation=None, contourValue=None):
        """
        __new__(cls: type, minimumElevation: float, maximumElevation: float, contourValue: ContourValues)
        __new__(cls: type)
        """
        pass

    ContourValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContourValue(self: SurfaceAnalysisContourData) -> ContourValues

Set: ContourValue(self: SurfaceAnalysisContourData) = value
"""

    MaximumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumElevation(self: SurfaceAnalysisContourData) -> float

Set: MaximumElevation(self: SurfaceAnalysisContourData) = value
"""

    MinimumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumElevation(self: SurfaceAnalysisContourData) -> float

Set: MinimumElevation(self: SurfaceAnalysisContourData) = value
"""



class SurfaceAnalysisDirectionData(object):
    """
    SurfaceAnalysisDirectionData(minimumDirection: float, maximumDirection: float, scheme: Color)
    SurfaceAnalysisDirectionData()
    """
    def Initialize(self, codeValue):
        """ Initialize(self: SurfaceAnalysisDirectionData, codeValue: ColorValue*) """
        pass

    def Update(self, A_0):
        """ Update(self: SurfaceAnalysisDirectionData, A_0: ColorValue*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, minimumDirection=None, maximumDirection=None, scheme=None):
        """
        __new__(cls: type, minimumDirection: float, maximumDirection: float, scheme: Color)
        __new__(cls: type)
        """
        pass

    MaximumDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumDirection(self: SurfaceAnalysisDirectionData) -> float

Set: MaximumDirection(self: SurfaceAnalysisDirectionData) = value
"""

    MinimumDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumDirection(self: SurfaceAnalysisDirectionData) -> float

Set: MinimumDirection(self: SurfaceAnalysisDirectionData) = value
"""

    Scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scheme(self: SurfaceAnalysisDirectionData) -> Color

Set: Scheme(self: SurfaceAnalysisDirectionData) = value
"""



class SurfaceAnalysisElevationData(object):
    """
    SurfaceAnalysisElevationData(minimumElevation: float, maximumElevation: float, scheme: Color)
    SurfaceAnalysisElevationData()
    """
    def Initialize(self, codeValue):
        """ Initialize(self: SurfaceAnalysisElevationData, codeValue: ColorValue*) """
        pass

    def Update(self, A_0):
        """ Update(self: SurfaceAnalysisElevationData, A_0: ColorValue*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, minimumElevation=None, maximumElevation=None, scheme=None):
        """
        __new__(cls: type, minimumElevation: float, maximumElevation: float, scheme: Color)
        __new__(cls: type)
        """
        pass

    MaximumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumElevation(self: SurfaceAnalysisElevationData) -> float

Set: MaximumElevation(self: SurfaceAnalysisElevationData) = value
"""

    MinimumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumElevation(self: SurfaceAnalysisElevationData) -> float

Set: MinimumElevation(self: SurfaceAnalysisElevationData) = value
"""

    Scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scheme(self: SurfaceAnalysisElevationData) -> Color

Set: Scheme(self: SurfaceAnalysisElevationData) = value
"""



class SurfaceAnalysisSlopeArrowData(object):
    """
    SurfaceAnalysisSlopeArrowData(minimumSlope: float, maximumSlope: float, scheme: Color)
    SurfaceAnalysisSlopeArrowData()
    """
    def Initialize(self, codeValue):
        """ Initialize(self: SurfaceAnalysisSlopeArrowData, codeValue: ColorValue*) """
        pass

    def Update(self, A_0):
        """ Update(self: SurfaceAnalysisSlopeArrowData, A_0: ColorValue*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, minimumSlope=None, maximumSlope=None, scheme=None):
        """
        __new__(cls: type, minimumSlope: float, maximumSlope: float, scheme: Color)
        __new__(cls: type)
        """
        pass

    MaximumSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumSlope(self: SurfaceAnalysisSlopeArrowData) -> float

Set: MaximumSlope(self: SurfaceAnalysisSlopeArrowData) = value
"""

    MinimumSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumSlope(self: SurfaceAnalysisSlopeArrowData) -> float

Set: MinimumSlope(self: SurfaceAnalysisSlopeArrowData) = value
"""

    Scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scheme(self: SurfaceAnalysisSlopeArrowData) -> Color

Set: Scheme(self: SurfaceAnalysisSlopeArrowData) = value
"""



class SurfaceAnalysisSlopeData(object):
    """
    SurfaceAnalysisSlopeData(minimumSlope: float, maximumSlope: float, scheme: Color)
    SurfaceAnalysisSlopeData()
    """
    def Initialize(self, codeValue):
        """ Initialize(self: SurfaceAnalysisSlopeData, codeValue: ColorValue*) """
        pass

    def Update(self, A_0):
        """ Update(self: SurfaceAnalysisSlopeData, A_0: ColorValue*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, minimumSlope=None, maximumSlope=None, scheme=None):
        """
        __new__(cls: type, minimumSlope: float, maximumSlope: float, scheme: Color)
        __new__(cls: type)
        """
        pass

    MaximumSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumSlope(self: SurfaceAnalysisSlopeData) -> float

Set: MaximumSlope(self: SurfaceAnalysisSlopeData) = value
"""

    MinimumSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumSlope(self: SurfaceAnalysisSlopeData) -> float

Set: MinimumSlope(self: SurfaceAnalysisSlopeData) = value
"""

    Scheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scheme(self: SurfaceAnalysisSlopeData) -> Color

Set: Scheme(self: SurfaceAnalysisSlopeData) = value
"""



class SurfaceAnalysisUserDefinedContourData(object):
    """
    SurfaceAnalysisUserDefinedContourData(elevation: float, color: Color, lineTypeId: ObjectId, lineWeight: LineWeight)
    SurfaceAnalysisUserDefinedContourData()
    """
    def Initialize(self, codeValue):
        """ Initialize(self: SurfaceAnalysisUserDefinedContourData, codeValue: ColorValue*) """
        pass

    def Update(self, A_0):
        """ Update(self: SurfaceAnalysisUserDefinedContourData, A_0: ColorValue*) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, elevation=None, color=None, lineTypeId=None, lineWeight=None):
        """
        __new__(cls: type, elevation: float, color: Color, lineTypeId: ObjectId, lineWeight: LineWeight)
        __new__(cls: type)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: SurfaceAnalysisUserDefinedContourData) -> Color

Set: Color(self: SurfaceAnalysisUserDefinedContourData) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceAnalysisUserDefinedContourData) -> str

Set: Description(self: SurfaceAnalysisUserDefinedContourData) = value
"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: SurfaceAnalysisUserDefinedContourData) -> float

Set: Elevation(self: SurfaceAnalysisUserDefinedContourData) = value
"""

    LineTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineTypeId(self: SurfaceAnalysisUserDefinedContourData) -> ObjectId

Set: LineTypeId(self: SurfaceAnalysisUserDefinedContourData) = value
"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWeight(self: SurfaceAnalysisUserDefinedContourData) -> LineWeight

Set: LineWeight(self: SurfaceAnalysisUserDefinedContourData) = value
"""



class SurfaceAnalysisWatershedData(object):
    """ SurfaceAnalysisWatershedData() """
    def Initialize(self, codeValue):
        """ Initialize(self: SurfaceAnalysisWatershedData, codeValue: ColorValue*) """
        pass

    def Update(self, A_0):
        """ Update(self: SurfaceAnalysisWatershedData, A_0: ColorValue*) """
        pass

    AreaColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaColor(self: SurfaceAnalysisWatershedData) -> Color

Set: AreaColor(self: SurfaceAnalysisWatershedData) = value
"""

    AreaHatchPatternName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaHatchPatternName(self: SurfaceAnalysisWatershedData) -> str

Set: AreaHatchPatternName(self: SurfaceAnalysisWatershedData) = value
"""

    AreaID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaID(self: SurfaceAnalysisWatershedData) -> int

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceAnalysisWatershedData) -> str

Set: Description(self: SurfaceAnalysisWatershedData) = value
"""

    DrainsInto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrainsInto(self: SurfaceAnalysisWatershedData) -> Array[int]

"""

    SegmentColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentColor(self: SurfaceAnalysisWatershedData) -> Color

Set: SegmentColor(self: SurfaceAnalysisWatershedData) = value
"""

    SegmentLineTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLineTypeId(self: SurfaceAnalysisWatershedData) -> ObjectId

Set: SegmentLineTypeId(self: SurfaceAnalysisWatershedData) = value
"""

    SegmentLineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLineWeight(self: SurfaceAnalysisWatershedData) -> LineWeight

Set: SegmentLineWeight(self: SurfaceAnalysisWatershedData) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SurfaceAnalysisWatershedData) -> WatershedType

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: SurfaceAnalysisWatershedData) -> bool

Set: Visible(self: SurfaceAnalysisWatershedData) = value
"""



class SurfaceAnalysisWatershedDataCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: SurfaceAnalysisWatershedDataCollection) -> IEnumerator[SurfaceAnalysisWatershedData] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SurfaceAnalysisWatershedDataCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SurfaceAnalysisWatershedData](enumerable: IEnumerable[SurfaceAnalysisWatershedData], value: SurfaceAnalysisWatershedData) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SurfaceAnalysisWatershedDataCollection) -> int

"""

    ParentSurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentSurfaceId(self: SurfaceAnalysisWatershedDataCollection) -> ObjectId

"""



class SurfaceBoundary(object):
    # no doc
    BoundaryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryType(self: SurfaceBoundary) -> SurfaceBoundaryType

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: SurfaceBoundary) -> Point3dCollection

"""



class SurfaceBreakline(object):
    # no doc
    def InsertIntoDrawing(self):
        """ InsertIntoDrawing(self: SurfaceBreakline) -> ObjectId """
        pass

    BreaklineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BreaklineType(self: SurfaceBreakline) -> SurfaceBreaklineType

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceBreakline) -> str

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: SurfaceBreakline) -> Point3dCollection

"""



class SurfaceBuildOptions(object):
    # no doc
    CopyDeletedDependentObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CopyDeletedDependentObjects(self: SurfaceBuildOptions) -> bool

Set: CopyDeletedDependentObjects(self: SurfaceBuildOptions) = value
"""

    CrossingBreaklinesElevationOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingBreaklinesElevationOption(self: SurfaceBuildOptions) -> CrossingBreaklinesElevationType

Set: CrossingBreaklinesElevationOption(self: SurfaceBuildOptions) = value
"""

    ExecludeMaximumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecludeMaximumElevation(self: SurfaceBuildOptions) -> bool

Set: ExecludeMaximumElevation(self: SurfaceBuildOptions) = value
"""

    ExecludeMinimumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExecludeMinimumElevation(self: SurfaceBuildOptions) -> bool

Set: ExecludeMinimumElevation(self: SurfaceBuildOptions) = value
"""

    MaximumAngleBetweenAdjacentTinLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumAngleBetweenAdjacentTinLines(self: SurfaceBuildOptions) -> float

Set: MaximumAngleBetweenAdjacentTinLines(self: SurfaceBuildOptions) = value
"""

    MaximumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumElevation(self: SurfaceBuildOptions) -> float

Set: MaximumElevation(self: SurfaceBuildOptions) = value
"""

    MaximumTriangleLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumTriangleLength(self: SurfaceBuildOptions) -> float

Set: MaximumTriangleLength(self: SurfaceBuildOptions) = value
"""

    MinimumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumElevation(self: SurfaceBuildOptions) -> float

Set: MinimumElevation(self: SurfaceBuildOptions) = value
"""

    NeedConvertBreaklines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedConvertBreaklines(self: SurfaceBuildOptions) -> bool

Set: NeedConvertBreaklines(self: SurfaceBuildOptions) = value
"""

    UseMaximumAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseMaximumAngle(self: SurfaceBuildOptions) -> bool

Set: UseMaximumAngle(self: SurfaceBuildOptions) = value
"""

    UseMaximumTriangleLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseMaximumTriangleLength(self: SurfaceBuildOptions) -> bool

Set: UseMaximumTriangleLength(self: SurfaceBuildOptions) = value
"""



class SurfaceContourLabelGroup(AutoFeatureLabelGroup):
    # no doc
    @staticmethod
    def Create(surfaceId, labelLinePoints, majorContourlabelStyleId=None, minorContourlabelStyleId=None, userContourlabelStyleId=None):
        """
        Create(surfaceId: ObjectId, labelLinePoints: Point2dCollection) -> ObjectId
        Create(surfaceId: ObjectId, labelLinePoints: Point2dCollection, majorContourlabelStyleId: ObjectId, minorContourlabelStyleId: ObjectId, userContourlabelStyleId: ObjectId) -> ObjectId
        """
        pass

    @staticmethod
    def CreateMultipleAtInterval(surfaceId, labelLineStartPoint, labelLineEndPoint, interval, options=None):
        """ CreateMultipleAtInterval(surfaceId: ObjectId, labelLineStartPoint: Point2d, labelLineEndPoint: Point2d, interval: float)CreateMultipleAtInterval(surfaceId: ObjectId, labelLineStartPoint: Point2d, labelLineEndPoint: Point2d, interval: float, options: SurfaceContourLabelGroupCreateOption) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(surfaceId):
        """ GetAvailableLabelGroupIds(surfaceId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(surfaceId):
        """ GetAvailableLabelGroups(surfaceId: ObjectId) -> ObjectIdCollection """
        pass

    def GetLabelLinePoint(self, index):
        """ GetLabelLinePoint(self: SurfaceContourLabelGroup, index: int) -> Point2d """
        pass

    def SetLabelLinePoint(self, index, __unnamed001):
        """ SetLabelLinePoint(self: SurfaceContourLabelGroup, index: int, __unnamed001: Point2d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    IsLabelLineVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLabelLineVisible(self: SurfaceContourLabelGroup) -> bool

Set: IsLabelLineVisible(self: SurfaceContourLabelGroup) = value
"""

    IsMajorContourLabelVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMajorContourLabelVisible(self: SurfaceContourLabelGroup) -> bool

Set: IsMajorContourLabelVisible(self: SurfaceContourLabelGroup) = value
"""

    IsMinorContourLabelVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMinorContourLabelVisible(self: SurfaceContourLabelGroup) -> bool

Set: IsMinorContourLabelVisible(self: SurfaceContourLabelGroup) = value
"""

    IsUserContourLabelVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserContourLabelVisible(self: SurfaceContourLabelGroup) -> bool

Set: IsUserContourLabelVisible(self: SurfaceContourLabelGroup) = value
"""

    LabelLinePoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelLinePoints(self: SurfaceContourLabelGroup) -> Point2dCollection

Set: LabelLinePoints(self: SurfaceContourLabelGroup) = value
"""

    MajorContourLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorContourLabelStyleId(self: SurfaceContourLabelGroup) -> ObjectId

Set: MajorContourLabelStyleId(self: SurfaceContourLabelGroup) = value
"""

    MinorContourLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorContourLabelStyleId(self: SurfaceContourLabelGroup) -> ObjectId

Set: MinorContourLabelStyleId(self: SurfaceContourLabelGroup) = value
"""

    RangeEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeEnd(self: SurfaceContourLabelGroup) -> float

Set: RangeEnd(self: SurfaceContourLabelGroup) = value
"""

    RangeEndFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeEndFromFeature(self: SurfaceContourLabelGroup) -> bool

Set: RangeEndFromFeature(self: SurfaceContourLabelGroup) = value
"""

    RangeStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeStart(self: SurfaceContourLabelGroup) -> float

Set: RangeStart(self: SurfaceContourLabelGroup) = value
"""

    RangeStartFromFeature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangeStartFromFeature(self: SurfaceContourLabelGroup) -> bool

Set: RangeStartFromFeature(self: SurfaceContourLabelGroup) = value
"""

    UserContourLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserContourLabelStyleId(self: SurfaceContourLabelGroup) -> ObjectId

Set: UserContourLabelStyleId(self: SurfaceContourLabelGroup) = value
"""


    m_SubData = None


class SurfaceContourLabelGroupCreateOption(object):
    """ SurfaceContourLabelGroupCreateOption() """
    MajorContourlabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorContourlabelStyleId(self: SurfaceContourLabelGroupCreateOption) -> ObjectId

Set: MajorContourlabelStyleId(self: SurfaceContourLabelGroupCreateOption) = value
"""

    MaskType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskType(self: SurfaceContourLabelGroupCreateOption) -> LabelMaskType

Set: MaskType(self: SurfaceContourLabelGroupCreateOption) = value
"""

    MinorContourlabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorContourlabelStyleId(self: SurfaceContourLabelGroupCreateOption) -> ObjectId

Set: MinorContourlabelStyleId(self: SurfaceContourLabelGroupCreateOption) = value
"""

    ShowLabelLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowLabelLine(self: SurfaceContourLabelGroupCreateOption) -> bool

Set: ShowLabelLine(self: SurfaceContourLabelGroupCreateOption) = value
"""

    ShowMajorContourlabelgroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowMajorContourlabelgroup(self: SurfaceContourLabelGroupCreateOption) -> bool

Set: ShowMajorContourlabelgroup(self: SurfaceContourLabelGroupCreateOption) = value
"""

    ShowMinorContourlabelgroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowMinorContourlabelgroup(self: SurfaceContourLabelGroupCreateOption) -> bool

Set: ShowMinorContourlabelgroup(self: SurfaceContourLabelGroupCreateOption) = value
"""

    ShowUserDefinedContourlabelgroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowUserDefinedContourlabelgroup(self: SurfaceContourLabelGroupCreateOption) -> bool

Set: ShowUserDefinedContourlabelgroup(self: SurfaceContourLabelGroupCreateOption) = value
"""

    UserDefinedContourlabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserDefinedContourlabelStyleId(self: SurfaceContourLabelGroupCreateOption) -> ObjectId

Set: UserDefinedContourlabelStyleId(self: SurfaceContourLabelGroupCreateOption) = value
"""



class SurfaceDefinitionAddFigureSurveyQueries(SurfaceDefinitionBase[SurfaceOperationAddFigureSurveyQuery]):
    # no doc
    def AddFigureSurveyQuery(self, surveyProjectGuid, surveyQueryGuid, queryChecksum, surfaceOpDescription, midOrdinateDis):
        """ AddFigureSurveyQuery(self: SurfaceDefinitionAddFigureSurveyQueries, surveyProjectGuid: Guid, surveyQueryGuid: Guid, queryChecksum: int, surfaceOpDescription: str, midOrdinateDis: float) -> SurfaceOperationAddFigureSurveyQuery """
        pass

    m_pSurface = None


class SurfaceDefinitionAddPointSurveyQueries(SurfaceDefinitionBase[SurfaceOperationAddPointSurveyQuery]):
    # no doc
    def AddPointSurveyQuery(self, surveyProjectGuid, surveyQueryGuid, queryChecksum, surfaceOpDescription, midOrdinateDis):
        """ AddPointSurveyQuery(self: SurfaceDefinitionAddPointSurveyQueries, surveyProjectGuid: Guid, surveyQueryGuid: Guid, queryChecksum: int, surfaceOpDescription: str, midOrdinateDis: float) -> SurfaceOperationAddPointSurveyQuery """
        pass

    m_pSurface = None


class SurfaceDefinitionBase(object):
    """ SurfaceDefinitionBase[T](surface: Surface) """
    def IsCorrectOperation(self, *args): #cannot find CLR method
        """ IsCorrectOperation(self: SurfaceDefinitionBase[T], pOp: AeccSurfaceOp*) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SurfaceDefinitionBase[T], index: int) """
        pass

    def ToAcGeVoidPointerArray(self, *args): #cannot find CLR method
        """ ToAcGeVoidPointerArray(: AcArray<void \*\,AcArrayMemCopyReallocator<void \*> >*, cliPoints: Point3dCollection) -> AcArray<void \*\,AcArrayMemCopyReallocator<void \*> >* """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, surface):
        """ __new__(cls: type, surface: Surface) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SurfaceDefinitionBase[T]) -> int

"""


    m_pSurface = None


class SurfaceDefinitionBoundaries(SurfaceDefinitionBase[SurfaceOperationAddBoundary]):
    # no doc
    def AddBoundaries(self, *__args):
        """
        AddBoundaries(self: SurfaceDefinitionBoundaries, boundaryEntities: ObjectIdCollection, midOrdinateDistance: float, boundaryType: SurfaceBoundaryType, useNonDestructiveBreakline: bool) -> SurfaceOperationAddBoundary
        AddBoundaries(self: SurfaceDefinitionBoundaries, points: Point2dCollection, midOrdinateDistance: float, boundaryType: SurfaceBoundaryType, useNonDestructiveBreakline: bool) -> SurfaceOperationAddBoundary
        AddBoundaries(self: SurfaceDefinitionBoundaries, points: Point3dCollection, midOrdinateDistance: float, boundaryType: SurfaceBoundaryType, useNonDestructiveBreakline: bool) -> SurfaceOperationAddBoundary
        """
        pass

    m_pSurface = None


class SurfaceDefinitionBreaklines(SurfaceDefinitionBase[SurfaceOperationAddBreakline]):
    # no doc
    def AddBreaklinesFromFile(self, filename):
        """ AddBreaklinesFromFile(self: SurfaceDefinitionBreaklines, filename: str) -> SurfaceOperationAddBreaklineFromFile """
        pass

    def AddNonDestructiveBreaklines(self, *__args):
        """
        AddNonDestructiveBreaklines(self: SurfaceDefinitionBreaklines, breaklineEntities: ObjectIdCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline
        AddNonDestructiveBreaklines(self: SurfaceDefinitionBreaklines, points: Point2dCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline
        AddNonDestructiveBreaklines(self: SurfaceDefinitionBreaklines, points: Point3dCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline
        """
        pass

    def AddProximityBreaklines(self, *__args):
        """
        AddProximityBreaklines(self: SurfaceDefinitionBreaklines, breaklineEntities: ObjectIdCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline
        AddProximityBreaklines(self: SurfaceDefinitionBreaklines, points: Point2dCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline
        AddProximityBreaklines(self: SurfaceDefinitionBreaklines, points: Point3dCollection, midOrdinateDistance: float) -> SurfaceOperationAddBreakline
        """
        pass

    def AddStandardBreaklines(self, *__args):
        """
        AddStandardBreaklines(self: SurfaceDefinitionBreaklines, breaklineEntities: ObjectIdCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddBreakline
        AddStandardBreaklines(self: SurfaceDefinitionBreaklines, points: Point2dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddBreakline
        AddStandardBreaklines(self: SurfaceDefinitionBreaklines, points: Point3dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddBreakline
        """
        pass

    def AddWallBreaklines(self, creationData, midOrdinateDistance, maximumDistance, weedingDistance, weedingAngle):
        """
        AddWallBreaklines(self: SurfaceDefinitionBreaklines, creationData: Array[WallBreaklineCreationDataEx], midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddBreakline
        AddWallBreaklines(self: SurfaceDefinitionBreaklines, creationData: Array[WallBreaklineCreationData], midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddBreakline
        """
        pass

    def ImportBreaklinesFromFile(self, filename):
        """ ImportBreaklinesFromFile(self: SurfaceDefinitionBreaklines, filename: str) -> Array[SurfaceOperationAddBreakline] """
        pass

    m_pSurface = None


class SurfaceDefinitionContours(SurfaceDefinitionBase[SurfaceOperationAddContour]):
    # no doc
    def AddContours(self, *__args):
        """
        AddContours(self: SurfaceDefinitionContours, points: Point3dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddContour
        AddContours(self: SurfaceDefinitionContours, points: Point2dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddContour
        AddContours(self: SurfaceDefinitionContours, boundaryEntities: ObjectIdCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float) -> SurfaceOperationAddContour
        AddContours(self: SurfaceDefinitionContours, points: Point3dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float, options: SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationAddContour
        AddContours(self: SurfaceDefinitionContours, points: Point2dCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float, options: SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationAddContour
        AddContours(self: SurfaceDefinitionContours, boundaryEntities: ObjectIdCollection, midOrdinateDistance: float, maximumDistance: float, weedingDistance: float, weedingAngle: float, options: SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationAddContour
        """
        pass

    m_pSurface = None


class SurfaceDefinitionDEMFiles(SurfaceDefinitionBase[SurfaceOperationAddDEMFile]):
    # no doc
    def AddDEMFile(self, filename, *__args):
        """
        AddDEMFile(self: SurfaceDefinitionDEMFiles, filename: str) -> SurfaceOperationAddDEMFile
        AddDEMFile(self: SurfaceDefinitionDEMFiles, filename: str, useCustomNullElevation: bool, customeNullElevation: float) -> SurfaceOperationAddDEMFile
        AddDEMFile(self: SurfaceDefinitionDEMFiles, filename: str, coordinateSystemCode: str, useCustomNullElevation: bool, customeNullElevation: float) -> SurfaceOperationAddDEMFile
        """
        pass

    m_pSurface = None


class SurfaceDefinitionDrawingObjects(SurfaceDefinitionBase[SurfaceOperationAddDrawingObject]):
    # no doc
    def AddFrom3DFaces(self, *__args):
        """
        AddFrom3DFaces(self: SurfaceDefinitionDrawingObjects, face3DIds: ObjectIdCollection, needMaintainEdge: bool, description: str) -> SurfaceOperationAdd3DFaces
        AddFrom3DFaces(self: SurfaceDefinitionDrawingObjects, points: Point3dCollection, edges: IEnumerable[KeyValuePair[int, int]], description: str) -> SurfaceOperationAdd3DFaces
        """
        pass

    def AddFromBlocks(self, blockIds, description):
        """ AddFromBlocks(self: SurfaceDefinitionDrawingObjects, blockIds: ObjectIdCollection, description: str) -> SurfaceOperationAddDrawingObject """
        pass

    def AddFromLines(self, lineIds, needMaintainEdge, description):
        """ AddFromLines(self: SurfaceDefinitionDrawingObjects, lineIds: ObjectIdCollection, needMaintainEdge: bool, description: str) -> SurfaceOperationAddDrawingObject """
        pass

    def AddFromPoints(self, pointIds, description):
        """ AddFromPoints(self: SurfaceDefinitionDrawingObjects, pointIds: ObjectIdCollection, description: str) -> SurfaceOperationAddDrawingObject """
        pass

    def AddFromPolyFaces(self, polyfaceIds, needMaintainEdge, description):
        """ AddFromPolyFaces(self: SurfaceDefinitionDrawingObjects, polyfaceIds: ObjectIdCollection, needMaintainEdge: bool, description: str) -> SurfaceOperationAddDrawingObject """
        pass

    def AddFromTexts(self, textIds, description):
        """ AddFromTexts(self: SurfaceDefinitionDrawingObjects, textIds: ObjectIdCollection, description: str) -> SurfaceOperationAddDrawingObject """
        pass

    m_pSurface = None


class SurfaceDefinitionPointFiles(SurfaceDefinitionBase[SurfaceOperationAddPointFile]):
    # no doc
    def AddPointFile(self, pointFilename, pointFileFormat, useAdjustedElevation=None, shouldTransformPointCoordinate=None, shouldExpandCoordinateData=None):
        """
        AddPointFile(self: SurfaceDefinitionPointFiles, pointFilename: str, pointFileFormat: PointFileFormat) -> SurfaceOperationAddPointFile
        AddPointFile(self: SurfaceDefinitionPointFiles, pointFilename: str, pointFileFormat: PointFileFormat, useAdjustedElevation: bool, shouldTransformPointCoordinate: bool, shouldExpandCoordinateData: bool) -> SurfaceOperationAddPointFile
        """
        pass

    m_pSurface = None


class SurfaceDefinitionPointGroups(SurfaceDefinitionBase[SurfaceOperationAddPointGroup]):
    # no doc
    def AddPointGroup(self, pointGroupId):
        """ AddPointGroup(self: SurfaceDefinitionPointGroups, pointGroupId: ObjectId) -> SurfaceOperationAddPointGroup """
        pass

    m_pSurface = None


class SurfaceElevationLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(surfaceId, location, labelStyleId=None, markerStyleId=None):
        """
        Create(surfaceId: ObjectId, location: Point2d) -> ObjectId
        Create(surfaceId: ObjectId, location: Point2d, labelStyleId: ObjectId, markerStyleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableSurfaceElevationLabelIds(surfaceId):
        """ GetAvailableSurfaceElevationLabelIds(surfaceId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableSurfaceElevationLabels(surfaceId):
        """ GetAvailableSurfaceElevationLabels(surfaceId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceElevationLabel) -> Point2d

Set: Location(self: SurfaceElevationLabel) = value
"""


    m_SubData = None


class SurfaceMask(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceMask) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceMask) -> str

Set: Description(self: SurfaceMask) = value
"""

    IsRenderOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRenderOnly(self: SurfaceMask) -> bool

Set: IsRenderOnly(self: SurfaceMask) = value
"""

    Linkages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linkages(self: SurfaceMask) -> ObjectIdCollection

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: SurfaceMask) -> ObjectId

Set: MaterialId(self: SurfaceMask) = value
"""

    MidOrdinateDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidOrdinateDistance(self: SurfaceMask) -> float

Set: MidOrdinateDistance(self: SurfaceMask) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SurfaceMask) -> str

Set: Name(self: SurfaceMask) = value
"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: SurfaceMask) -> ObjectId

"""

    SurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceId(self: SurfaceMask) -> ObjectId

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SurfaceMask) -> SurfaceMaskType

Set: Type(self: SurfaceMask) = value
"""



class SurfaceMaskCollection(object):
    """ SurfaceMaskCollection(pSurface: Surface) """
    def Add(self, creationData):
        """ Add(self: SurfaceMaskCollection, creationData: SurfaceMaskCreationData) -> SurfaceMask """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SurfaceMaskCollection) -> IEnumerator[SurfaceMask] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SurfaceMaskCollection) -> IEnumerator """
        pass

    def IndexOf(self, mask):
        """ IndexOf(self: SurfaceMaskCollection, mask: SurfaceMask) -> int """
        pass

    def MoveDown(self, mask):
        """ MoveDown(self: SurfaceMaskCollection, mask: SurfaceMask) """
        pass

    def MoveUp(self, mask):
        """ MoveUp(self: SurfaceMaskCollection, mask: SurfaceMask) """
        pass

    def Remove(self, mask):
        """ Remove(self: SurfaceMaskCollection, mask: SurfaceMask) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SurfaceMaskCollection, index: int) """
        pass

    def Swap(self, mask1, mask2):
        """ Swap(self: SurfaceMaskCollection, mask1: SurfaceMask, mask2: SurfaceMask) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SurfaceMask](enumerable: IEnumerable[SurfaceMask], value: SurfaceMask) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pSurface):
        """ __new__(cls: type, pSurface: Surface) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SurfaceMaskCollection) -> int

"""



class SurfaceMaskCreationData(object):
    """
    SurfaceMaskCreationData(name: str, desc: str, surfaceId: ObjectId, linkages: ObjectIdCollection, midOrdinateDistance: float, materialId: ObjectId, type: SurfaceMaskType, isRenderOnly: bool)
    SurfaceMaskCreationData()
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None, desc=None, surfaceId=None, linkages=None, midOrdinateDistance=None, materialId=None, type=None, isRenderOnly=None):
        """
        __new__(cls: type, name: str, desc: str, surfaceId: ObjectId, linkages: ObjectIdCollection, midOrdinateDistance: float, materialId: ObjectId, type: SurfaceMaskType, isRenderOnly: bool)
        __new__(cls: type)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceMaskCreationData) -> str

Set: Description(self: SurfaceMaskCreationData) = value
"""

    IsRenderOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRenderOnly(self: SurfaceMaskCreationData) -> bool

Set: IsRenderOnly(self: SurfaceMaskCreationData) = value
"""

    Linkages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linkages(self: SurfaceMaskCreationData) -> ObjectIdCollection

Set: Linkages(self: SurfaceMaskCreationData) = value
"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: SurfaceMaskCreationData) -> ObjectId

Set: MaterialId(self: SurfaceMaskCreationData) = value
"""

    MidOrdinateDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidOrdinateDistance(self: SurfaceMaskCreationData) -> float

Set: MidOrdinateDistance(self: SurfaceMaskCreationData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SurfaceMaskCreationData) -> str

Set: Name(self: SurfaceMaskCreationData) = value
"""

    SurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceId(self: SurfaceMaskCreationData) -> ObjectId

Set: SurfaceId(self: SurfaceMaskCreationData) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: SurfaceMaskCreationData) -> SurfaceMaskType

Set: Type(self: SurfaceMaskCreationData) = value
"""



class SurfaceMaskType(Enum):
    """ enum SurfaceMaskType, values: InSide (0), OutSide (1) """
    InSide = None
    OutSide = None
    value__ = None


class SurfaceMinimizeFlatAreaOptions(object):
    """ SurfaceMinimizeFlatAreaOptions(fillGaps: bool, swapEdges: bool, addPointsToTriangles: bool, addPointsToEdges: bool) """
    @staticmethod # known case of __new__
    def __new__(self, fillGaps, swapEdges, addPointsToTriangles, addPointsToEdges):
        """
        __new__[SurfaceMinimizeFlatAreaOptions]() -> SurfaceMinimizeFlatAreaOptions
        
        __new__(cls: type, fillGaps: bool, swapEdges: bool, addPointsToTriangles: bool, addPointsToEdges: bool)
        """
        pass

    AddPointsToEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddPointsToEdges(self: SurfaceMinimizeFlatAreaOptions) -> bool

Set: AddPointsToEdges(self: SurfaceMinimizeFlatAreaOptions) = value
"""

    AddPointsToTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddPointsToTriangles(self: SurfaceMinimizeFlatAreaOptions) -> bool

Set: AddPointsToTriangles(self: SurfaceMinimizeFlatAreaOptions) = value
"""

    FillGaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillGaps(self: SurfaceMinimizeFlatAreaOptions) -> bool

Set: FillGaps(self: SurfaceMinimizeFlatAreaOptions) = value
"""

    SwapEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SwapEdges(self: SurfaceMinimizeFlatAreaOptions) -> bool

Set: SwapEdges(self: SurfaceMinimizeFlatAreaOptions) = value
"""



class SurfaceOperation(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation) """
        pass

    def MoveDown(self):
        """ MoveDown(self: SurfaceOperation) """
        pass

    def MoveToBottom(self):
        """ MoveToBottom(self: SurfaceOperation) """
        pass

    def MoveToTop(self):
        """ MoveToTop(self: SurfaceOperation) """
        pass

    def MoveUp(self):
        """ MoveUp(self: SurfaceOperation) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: SurfaceOperation) -> bool

Set: Enabled(self: SurfaceOperation) = value
"""



class SurfaceOperationAddDrawingObject(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceOperationAddDrawingObject) -> str

"""

    MaintainEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaintainEdge(self: SurfaceOperationAddDrawingObject) -> bool

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectType(self: SurfaceOperationAddDrawingObject) -> SurfaceDrawObjectType

"""



class SurfaceOperationAdd3DFaces(SurfaceOperationAddDrawingObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass


class SurfaceOperationAddBoundary(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SurfaceOperationAddBoundary) -> IEnumerator[SurfaceBoundary] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SurfaceOperationAddBoundary) -> IEnumerator """
        pass

    def InsertIntoDrawing(self):
        """ InsertIntoDrawing(self: SurfaceOperationAddBoundary) -> ObjectIdCollection """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SurfaceBoundary](enumerable: IEnumerable[SurfaceBoundary], value: SurfaceBoundary) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    BoundaryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryType(self: SurfaceOperationAddBoundary) -> SurfaceBoundaryType

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SurfaceOperationAddBoundary) -> int

"""

    IsTrimmed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTrimmed(self: SurfaceOperationAddBoundary) -> bool

"""

    MidOrdinateDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidOrdinateDistance(self: SurfaceOperationAddBoundary) -> float

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SurfaceOperationAddBoundary) -> str

Set: Name(self: SurfaceOperationAddBoundary) = value
"""



class SurfaceOperationAddBreakline(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SurfaceOperationAddBreakline) -> IEnumerator[SurfaceBreakline] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SurfaceOperationAddBreakline) -> IEnumerator """
        pass

    def InsertIntoDrawing(self):
        """ InsertIntoDrawing(self: SurfaceOperationAddBreakline) -> ObjectIdCollection """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SurfaceBreakline](enumerable: IEnumerable[SurfaceBreakline], value: SurfaceBreakline) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    BreaklineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BreaklineType(self: SurfaceOperationAddBreakline) -> SurfaceBreaklineType

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SurfaceOperationAddBreakline) -> int

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceOperationAddBreakline) -> str

Set: Description(self: SurfaceOperationAddBreakline) = value
"""

    MaximumDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumDistance(self: SurfaceOperationAddBreakline) -> float

"""

    MidOrdinateDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidOrdinateDistance(self: SurfaceOperationAddBreakline) -> float

"""

    WeedingAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeedingAngle(self: SurfaceOperationAddBreakline) -> float

"""

    WeedingDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeedingDistance(self: SurfaceOperationAddBreakline) -> float

"""



class SurfaceOperationAddBreaklineFromFile(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    BreaklineFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BreaklineFileName(self: SurfaceOperationAddBreaklineFromFile) -> str

Set: BreaklineFileName(self: SurfaceOperationAddBreaklineFromFile) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceOperationAddBreaklineFromFile) -> str

"""



class SurfaceOperationAddContour(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    def InsertIntoDrawing(self):
        """ InsertIntoDrawing(self: SurfaceOperationAddContour) -> ObjectIdCollection """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceOperationAddContour) -> str

Set: Description(self: SurfaceOperationAddContour) = value
"""

    MaximumDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumDistance(self: SurfaceOperationAddContour) -> float

"""

    MidOrdinateDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidOrdinateDistance(self: SurfaceOperationAddContour) -> float

"""

    Summary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Summary(self: SurfaceOperationAddContour) -> str

"""

    WeedingAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeedingAngle(self: SurfaceOperationAddContour) -> float

"""

    WeedingDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeedingDistance(self: SurfaceOperationAddContour) -> float

"""



class SurfaceOperationAddDEMFile(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    CoordinateSystemCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystemCode(self: SurfaceOperationAddDEMFile) -> str

"""

    CustomeNullElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomeNullElevation(self: SurfaceOperationAddDEMFile) -> float

"""

    DEMFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DEMFileName(self: SurfaceOperationAddDEMFile) -> str

Set: DEMFileName(self: SurfaceOperationAddDEMFile) = value
"""

    FileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileSize(self: SurfaceOperationAddDEMFile) -> float

"""

    UseCustomNullElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseCustomNullElevation(self: SurfaceOperationAddDEMFile) -> bool

"""



class SurfaceOperationAddSurveyQuery(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SurfaceOperationAddSurveyQuery) -> str

"""

    ProjectGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectGuid(self: SurfaceOperationAddSurveyQuery) -> Guid

"""

    ProjectName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectName(self: SurfaceOperationAddSurveyQuery) -> str

"""

    QueryGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QueryGuid(self: SurfaceOperationAddSurveyQuery) -> Guid

"""

    QueryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QueryName(self: SurfaceOperationAddSurveyQuery) -> str

"""

    SurveyQueryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurveyQueryType(self: SurfaceOperationAddSurveyQuery) -> SurfaceSurveyQueryType

"""



class SurfaceOperationAddFigureSurveyQuery(SurfaceOperationAddSurveyQuery):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass


class SurfaceOperationAddGridPoint(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: SurfaceOperationAddGridPoint) -> float

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceOperationAddGridPoint) -> GridLocation

"""



class SurfaceOperationAddImxFile(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    DoCoordinateConversion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DoCoordinateConversion(self: SurfaceOperationAddImxFile) -> bool

Set: DoCoordinateConversion(self: SurfaceOperationAddImxFile) = value
"""

    FileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileSize(self: SurfaceOperationAddImxFile) -> float

"""

    GitHash = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GitHash(self: SurfaceOperationAddImxFile) -> str

Set: GitHash(self: SurfaceOperationAddImxFile) = value
"""

    ImxFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImxFileName(self: SurfaceOperationAddImxFile) -> str

Set: ImxFileName(self: SurfaceOperationAddImxFile) = value
"""

    Query = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Query(self: SurfaceOperationAddImxFile) -> str

Set: Query(self: SurfaceOperationAddImxFile) = value
"""

    SurfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceName(self: SurfaceOperationAddImxFile) -> str

Set: SurfaceName(self: SurfaceOperationAddImxFile) = value
"""



class SurfaceOperationAddLine(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    EndLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndLocation(self: SurfaceOperationAddLine) -> Point2d

"""

    StartLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartLocation(self: SurfaceOperationAddLine) -> Point2d

"""



class SurfaceOperationAddPointFile(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperationAddPointFile, A_0: bool) """
        pass

    FileFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileFormat(self: SurfaceOperationAddPointFile) -> PointFileFormat

"""

    PointFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointFileName(self: SurfaceOperationAddPointFile) -> str

Set: PointFileName(self: SurfaceOperationAddPointFile) = value
"""

    ShouldExpandCoordinateData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShouldExpandCoordinateData(self: SurfaceOperationAddPointFile) -> bool

"""

    ShouldTransformPointCoordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShouldTransformPointCoordinates(self: SurfaceOperationAddPointFile) -> bool

"""

    UseAdjustedElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseAdjustedElevation(self: SurfaceOperationAddPointFile) -> bool

"""



class SurfaceOperationAddPointGroup(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    PointGroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointGroupId(self: SurfaceOperationAddPointGroup) -> ObjectId

"""



class SurfaceOperationAddPointSurveyQuery(SurfaceOperationAddSurveyQuery):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass


class SurfaceOperationAddTinFile(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    FileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileSize(self: SurfaceOperationAddTinFile) -> float

"""

    TinFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TinFileName(self: SurfaceOperationAddTinFile) -> str

Set: TinFileName(self: SurfaceOperationAddTinFile) = value
"""



class SurfaceOperationAddTinMultipleVertices(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Locations(self: SurfaceOperationAddTinMultipleVertices) -> Point3dCollection

"""



class SurfaceOperationAddTinVertex(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceOperationAddTinVertex) -> Point3d

"""



class SurfaceOperationAddXmlFile(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    XmlFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XmlFileName(self: SurfaceOperationAddXmlFile) -> str

"""



class SurfaceOperationCollection(object):
    # no doc
    def DisableOperations(self, operationClassType):
        """ DisableOperations(self: SurfaceOperationCollection, operationClassType: Type) """
        pass

    def EnableOperations(self, operationClassType):
        """ EnableOperations(self: SurfaceOperationCollection, operationClassType: Type) """
        pass

    def GetOperationStatus(self, operationClassType):
        """ GetOperationStatus(self: SurfaceOperationCollection, operationClassType: Type) -> SurfaceOpeartionStatusType """
        pass

    def Remove(self, operation):
        """ Remove(self: SurfaceOperationCollection, operation: SurfaceOperation) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SurfaceOperationCollection, index: int) """
        pass

    def Swap(self, firstOperation, secondOperation):
        """ Swap(self: SurfaceOperationCollection, firstOperation: SurfaceOperation, secondOperation: SurfaceOperation) """
        pass

    def SwapAt(self, firstIndex, secondIndex):
        """ SwapAt(self: SurfaceOperationCollection, firstIndex: int, secondIndex: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SurfaceOperationCollection) -> int

"""



class SurfaceOperationCreateByCropping(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    CroppedBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CroppedBoundary(self: SurfaceOperationCreateByCropping) -> Point3dCollection

"""

    SourceFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceFileName(self: SurfaceOperationCreateByCropping) -> str

"""



class SurfaceOperationCreatedFromCorridor(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    CorridorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorId(self: SurfaceOperationCreatedFromCorridor) -> ObjectId

"""

    CorridorSurfaceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorSurfaceName(self: SurfaceOperationCreatedFromCorridor) -> str

"""



class SurfaceOperationDeleteGridPoint(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceOperationDeleteGridPoint) -> GridLocation

"""



class SurfaceOperationDeleteLine(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    MidLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidLocation(self: SurfaceOperationDeleteLine) -> Point2d

"""



class SurfaceOperationDeleteMultipleGridPoints(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Locations(self: SurfaceOperationDeleteMultipleGridPoints) -> Array[GridLocation]

"""



class SurfaceOperationDeleteMultipleLines(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    MidLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidLocations(self: SurfaceOperationDeleteMultipleLines) -> Point2dCollection

"""



class SurfaceOperationDeleteMultipleTinVertices(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Locations(self: SurfaceOperationDeleteMultipleTinVertices) -> Point2dCollection

"""



class SurfaceOperationDeleteTinVertex(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceOperationDeleteTinVertex) -> Point2d

"""



class SurfaceOperationMinimizeFlatAreas(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    CountOfAddedPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountOfAddedPoints(self: SurfaceOperationMinimizeFlatAreas) -> int

"""

    CountOfRemovedPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountOfRemovedPoints(self: SurfaceOperationMinimizeFlatAreas) -> int

"""

    MinimizeFlatAreaOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimizeFlatAreaOptions(self: SurfaceOperationMinimizeFlatAreas) -> SurfaceMinimizeFlatAreaOptions

"""



class SurfaceOperationModifyGridPointElevation(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceOperationModifyGridPointElevation) -> GridLocation

"""

    NewElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewElevation(self: SurfaceOperationModifyGridPointElevation) -> float

"""



class SurfaceOperationModifyMultipleGridPointsElevation(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: SurfaceOperationModifyMultipleGridPointsElevation) -> float

"""

    IsDeltaElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeltaElevation(self: SurfaceOperationModifyMultipleGridPointsElevation) -> bool

"""

    Locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Locations(self: SurfaceOperationModifyMultipleGridPointsElevation) -> Array[GridLocation]

"""



class SurfaceOperationModifyMultipleTinVerticesElevation(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: SurfaceOperationModifyMultipleTinVerticesElevation) -> float

"""

    IsDeltaElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDeltaElevation(self: SurfaceOperationModifyMultipleTinVerticesElevation) -> bool

"""

    Locations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Locations(self: SurfaceOperationModifyMultipleTinVerticesElevation) -> Point2dCollection

"""



class SurfaceOperationModifyTinVertexElevation(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceOperationModifyTinVertexElevation) -> Point2d

"""

    NewElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewElevation(self: SurfaceOperationModifyTinVertexElevation) -> float

"""



class SurfaceOperationMoveTinVertex(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    NewLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewLocation(self: SurfaceOperationMoveTinVertex) -> Point2d

"""

    OriginalLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginalLocation(self: SurfaceOperationMoveTinVertex) -> Point2d

"""



class SurfaceOperationPasteSurface(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    SurfaceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceId(self: SurfaceOperationPasteSurface) -> ObjectId

"""



class SurfaceOperationRaise(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    DeltaElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeltaElevation(self: SurfaceOperationRaise) -> float

"""



class SurfaceOperationSimplify(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    CountOfRemovedPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CountOfRemovedPoints(self: SurfaceOperationSimplify) -> int

"""

    SimplifyOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimplifyOptions(self: SurfaceOperationSimplify) -> SurfaceSimplifyOptions

"""



class SurfaceOperationSmooth(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    OutPutPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutPutPoints(self: SurfaceOperationSmooth) -> Point3dCollection

"""

    SurfaceSmoothMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceSmoothMethod(self: SurfaceOperationSmooth) -> SurfaceSmoothType

"""



class SurfaceOperationSwapEdge(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    MidLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidLocation(self: SurfaceOperationSwapEdge) -> Point2d

"""



class SurfaceOperationTransformBy(SurfaceOperation):
    # no doc
    def Dispose(self):
        """ Dispose(self: SurfaceOperation, A_0: bool) """
        pass

    TransformMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransformMatrix(self: SurfaceOperationTransformBy) -> Matrix3d

"""

    TransformType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransformType(self: SurfaceOperationTransformBy) -> SurfaceTransformOperationType

"""



class SurfacePointOutputOptions(object):
    """ SurfacePointOutputOptions() """
    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: SurfacePointOutputOptions) -> IEnumerable[TinSurfaceEdge]

Set: Edges(self: SurfacePointOutputOptions) = value
"""

    GridOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridOrientation(self: SurfacePointOutputOptions) -> float

Set: GridOrientation(self: SurfacePointOutputOptions) = value
"""

    GridSpacingX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridSpacingX(self: SurfacePointOutputOptions) -> float

Set: GridSpacingX(self: SurfacePointOutputOptions) = value
"""

    GridSpacingY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridSpacingY(self: SurfacePointOutputOptions) -> float

Set: GridSpacingY(self: SurfacePointOutputOptions) = value
"""

    OutputLocations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputLocations(self: SurfacePointOutputOptions) -> SurfacePointOutputLocationsType

Set: OutputLocations(self: SurfacePointOutputOptions) = value
"""

    OutputRegions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutputRegions(self: SurfacePointOutputOptions) -> IEnumerable[Point3dCollection]

Set: OutputRegions(self: SurfacePointOutputOptions) = value
"""

    RandomPointsNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RandomPointsNumber(self: SurfacePointOutputOptions) -> int

Set: RandomPointsNumber(self: SurfacePointOutputOptions) = value
"""



class SurfaceSimplifyOptions(object):
    """
    SurfaceSimplifyOptions(options: SurfaceSimplifyOptions)
    SurfaceSimplifyOptions(simplifyMethod: SurfaceSimplifyType)
    """
    def Equals(self, right):
        """ Equals(self: SurfaceSimplifyOptions, right: object) -> bool """
        pass

    def SetSurfaceBorderAsRegion(self):
        """ SetSurfaceBorderAsRegion(self: SurfaceSimplifyOptions) """
        pass

    def SetUserSpecifiedPolygonRegionByEntityId(self, entityId, midOrdinate):
        """ SetUserSpecifiedPolygonRegionByEntityId(self: SurfaceSimplifyOptions, entityId: ObjectId, midOrdinate: float) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, options: SurfaceSimplifyOptions)
        __new__(cls: type, simplifyMethod: SurfaceSimplifyType)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    MaximumChangeInElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumChangeInElevation(self: SurfaceSimplifyOptions) -> float

Set: MaximumChangeInElevation(self: SurfaceSimplifyOptions) = value
"""

    PercentageToRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentageToRemove(self: SurfaceSimplifyOptions) -> float

Set: PercentageToRemove(self: SurfaceSimplifyOptions) = value
"""

    RegionOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegionOption(self: SurfaceSimplifyOptions) -> SurfaceSimplifyRegionType

"""

    SimplifyMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimplifyMethod(self: SurfaceSimplifyOptions) -> SurfaceSimplifyType

Set: SimplifyMethod(self: SurfaceSimplifyOptions) = value
"""

    UseMaximumChangeInElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseMaximumChangeInElevation(self: SurfaceSimplifyOptions) -> bool

Set: UseMaximumChangeInElevation(self: SurfaceSimplifyOptions) = value
"""

    UsePercentageToRemove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsePercentageToRemove(self: SurfaceSimplifyOptions) -> bool

Set: UsePercentageToRemove(self: SurfaceSimplifyOptions) = value
"""

    UserSpecifiedPolygonRegion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserSpecifiedPolygonRegion(self: SurfaceSimplifyOptions) -> Point3dCollection

Set: UserSpecifiedPolygonRegion(self: SurfaceSimplifyOptions) = value
"""



class SurfaceSimplifyRegionType(Enum):
    """ enum SurfaceSimplifyRegionType, values: SurfaceBorder (0), UserSpecified (1) """
    SurfaceBorder = None
    UserSpecified = None
    value__ = None


class SurfaceSlopeLabel(FeatureLabel):
    # no doc
    @staticmethod
    def Create(surfaceId, *__args):
        """
        Create(surfaceId: ObjectId, location: Point2d, labelStyleId: ObjectId) -> ObjectId
        Create(surfaceId: ObjectId, location: Point2d) -> ObjectId
        Create(surfaceId: ObjectId, point1: Point2d, point2: Point2d, labelStyleId: ObjectId) -> ObjectId
        Create(surfaceId: ObjectId, point1: Point2d, point2: Point2d) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableSurfaceSlopeLabelIds(surfaceId):
        """ GetAvailableSurfaceSlopeLabelIds(surfaceId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableSurfaceSlopeLabels(surfaceId):
        """ GetAvailableSurfaceSlopeLabels(surfaceId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SurfaceSlopeLabel) -> Point2d

Set: Location(self: SurfaceSlopeLabel) = value
"""

    Location2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location2(self: SurfaceSlopeLabel) -> Point2d

Set: Location2(self: SurfaceSlopeLabel) = value
"""

    SlopeLabelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeLabelType(self: SurfaceSlopeLabel) -> SurfaceSlopeLabelType

"""


    m_SubData = None


class SurfaceSlopeLabelType(Enum):
    """ enum SurfaceSlopeLabelType, values: OnePoint (0), TwoPoint (1) """
    OnePoint = None
    TwoPoint = None
    value__ = None


class SurfaceTransformOperationType(Enum):
    """ enum SurfaceTransformOperationType, values: Move (3), Rotate (1), Scale (2) """
    Move = None
    Rotate = None
    Scale = None
    value__ = None


class SurfaceVolumeInfo(object):
    # no doc
    Cut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cut(self: SurfaceVolumeInfo) -> float

"""

    Fill = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fill(self: SurfaceVolumeInfo) -> float

"""

    Net = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Net(self: SurfaceVolumeInfo) -> float

"""



class SurveyFigure(FeatureLine):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class SurveyNetworkEntity(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class SweptShapeType(Enum):
    """ enum SweptShapeType, values: Arched (7), Circular (2), CustomShape (1), EggShaped (5), Elliptical (4), HorizontalElliptical (6), Rectangular (3), Undefined (0) """
    Arched = None
    Circular = None
    CustomShape = None
    EggShaped = None
    Elliptical = None
    HorizontalElliptical = None
    Rectangular = None
    Undefined = None
    value__ = None


class TerrainSurfaceProperties(object):
    # no doc
    MaximumGradeOrSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumGradeOrSlope(self: TerrainSurfaceProperties) -> float

"""

    MeanGradeOrSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeanGradeOrSlope(self: TerrainSurfaceProperties) -> float

"""

    MinimumGradeOrSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumGradeOrSlope(self: TerrainSurfaceProperties) -> float

"""

    SurfaceArea2D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceArea2D(self: TerrainSurfaceProperties) -> float

"""

    SurfaceArea3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceArea3D(self: TerrainSurfaceProperties) -> float

"""



class TinSurface(Surface):
    # no doc
    def AddLine(self, vertex1, vertex2):
        """ AddLine(self: TinSurface, vertex1: TinSurfaceVertex, vertex2: TinSurfaceVertex) -> SurfaceOperationAddLine """
        pass

    def AddVertex(self, location):
        """
        AddVertex(self: TinSurface, location: Point3d) -> SurfaceOperationAddTinVertex
        AddVertex(self: TinSurface, location: Point2d) -> SurfaceOperationAddTinVertex
        """
        pass

    def AddVertices(self, locations):
        """
        AddVertices(self: TinSurface, locations: Point3dCollection) -> SurfaceOperationAddTinMultipleVertices
        AddVertices(self: TinSurface, locations: Point2dCollection) -> SurfaceOperationAddTinMultipleVertices
        """
        pass

    @staticmethod
    def Create(*__args):
        """
        Create(database: Database, surfaceName: str) -> ObjectId
        Create(surfaceName: str, styleId: ObjectId) -> ObjectId
        """
        pass

    @staticmethod
    def CreateByCropping(destDatabase, surfaceName, srcSurfaceId, *__args):
        """
        CreateByCropping(destDatabase: Database, surfaceName: str, srcSurfaceId: ObjectId, points: Point2dCollection) -> ObjectId
        CreateByCropping(destDatabase: Database, surfaceName: str, srcSurfaceId: ObjectId, points: Point3dCollection) -> ObjectId
        CreateByCropping(destDatabase: Database, surfaceName: str, srcSurfaceId: ObjectId, objects: ObjectIdCollection, location: Point2d) -> ObjectId
        """
        pass

    @staticmethod
    def CreateFromCorridorSurface(surfaceName, corridorSurface):
        """ CreateFromCorridorSurface(surfaceName: str, corridorSurface: CorridorSurface) -> ObjectId """
        pass

    @staticmethod
    def CreateFromIMX(database, styleId, imxFileName, surfaceName, gitHash, query, doCoordSysConversion):
        """ CreateFromIMX(database: Database, styleId: ObjectId, imxFileName: str, surfaceName: str, gitHash: str, query: str, doCoordSysConversion: bool) -> ObjectId """
        pass

    @staticmethod
    def CreateFromTin(database, tinFileName):
        """ CreateFromTin(database: Database, tinFileName: str) -> ObjectId """
        pass

    def DeleteLine(self, tinTriangleEdge):
        """ DeleteLine(self: TinSurface, tinTriangleEdge: TinSurfaceEdge) -> SurfaceOperationDeleteLine """
        pass

    def DeleteLines(self, tinTriangleEdges):
        """ DeleteLines(self: TinSurface, tinTriangleEdges: IEnumerable[TinSurfaceEdge]) -> SurfaceOperationDeleteMultipleLines """
        pass

    def DeleteVertex(self, vertex):
        """ DeleteVertex(self: TinSurface, vertex: TinSurfaceVertex) -> SurfaceOperationDeleteTinVertex """
        pass

    def DeleteVertices(self, vertices):
        """ DeleteVertices(self: TinSurface, vertices: IEnumerable[TinSurfaceVertex]) -> SurfaceOperationDeleteMultipleTinVertices """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def ExtractBorder(self, settingsType):
        """ ExtractBorder(self: TinSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def ExtractContours(self, *__args):
        """
        ExtractContours(self: TinSurface, lowElev: float, highElev: float, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        ExtractContours(self: TinSurface, lowElev: float, highElev: float, interval: float) -> ObjectIdCollection
        ExtractContours(self: TinSurface, interval: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        ExtractContours(self: TinSurface, interval: float) -> ObjectIdCollection
        """
        pass

    def ExtractContoursAt(self, elevation, smoothType=None, smoothFactor=None):
        """
        ExtractContoursAt(self: TinSurface, elevation: float) -> ObjectIdCollection
        ExtractContoursAt(self: TinSurface, elevation: float, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractGridded(self, settingsType):
        """ ExtractGridded(self: TinSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def ExtractMajorContours(self, settingsType, smoothType=None, smoothFactor=None):
        """
        ExtractMajorContours(self: TinSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        ExtractMajorContours(self: TinSurface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractMinorContours(self, settingsType, smoothType=None, smoothFactor=None):
        """
        ExtractMinorContours(self: TinSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection
        ExtractMinorContours(self: TinSurface, settingsType: SurfaceExtractionSettingsType, smoothType: ContourSmoothingType, smoothFactor: int) -> ObjectIdCollection
        """
        pass

    def ExtractWatershed(self, settingsType):
        """ ExtractWatershed(self: TinSurface, settingsType: SurfaceExtractionSettingsType) -> ObjectIdCollection """
        pass

    def FindEdgeAtXY(self, x, y):
        """ FindEdgeAtXY(self: TinSurface, x: float, y: float) -> TinSurfaceEdge """
        pass

    def FindTriangleAtXY(self, x, y):
        """ FindTriangleAtXY(self: TinSurface, x: float, y: float) -> TinSurfaceTriangle """
        pass

    def FindVertexAtXY(self, x, y):
        """ FindVertexAtXY(self: TinSurface, x: float, y: float) -> TinSurfaceVertex """
        pass

    def GetTerrainProperties(self):
        """ GetTerrainProperties(self: TinSurface) -> TerrainSurfaceProperties """
        pass

    def GetTinProperties(self):
        """ GetTinProperties(self: TinSurface) -> TinSurfaceProperties """
        pass

    def GetTriangles(self, includeInvisible):
        """ GetTriangles(self: TinSurface, includeInvisible: bool) -> TinSurfaceTriangleCollection """
        pass

    def GetVerticesInsideBorder(self, border):
        """ GetVerticesInsideBorder(self: TinSurface, border: Point3dCollection) -> Array[TinSurfaceVertex] """
        pass

    def GetVerticesInsideBorderRandom(self, border, randomNumber):
        """ GetVerticesInsideBorderRandom(self: TinSurface, border: Point3dCollection, randomNumber: int) -> Array[TinSurfaceVertex] """
        pass

    def GetVerticesInsidePolylines(self, polylineIds):
        """ GetVerticesInsidePolylines(self: TinSurface, polylineIds: ObjectIdCollection) -> Array[TinSurfaceVertex] """
        pass

    def GetVerticesInsidePolylinesRandom(self, polylineIds, randomNumber):
        """ GetVerticesInsidePolylinesRandom(self: TinSurface, polylineIds: ObjectIdCollection, randomNumber: int) -> Array[TinSurfaceVertex] """
        pass

    def IdentifyFeatureTypeAtXY(self, x, y):
        """ IdentifyFeatureTypeAtXY(self: TinSurface, x: float, y: float) -> Type """
        pass

    def MinimizeFlatAreas(self, minimizeOptions):
        """ MinimizeFlatAreas(self: TinSurface, minimizeOptions: SurfaceMinimizeFlatAreaOptions) -> SurfaceOperationMinimizeFlatAreas """
        pass

    def MoveVertex(self, vertex, newLocation):
        """ MoveVertex(self: TinSurface, vertex: TinSurfaceVertex, newLocation: Point2d) -> SurfaceOperationMoveTinVertex """
        pass

    def PasteSurface(self, surfaceId):
        """ PasteSurface(self: TinSurface, surfaceId: ObjectId) -> SurfaceOperationPasteSurface """
        pass

    def RaiseSurface(self, deltaElevation):
        """ RaiseSurface(self: TinSurface, deltaElevation: float) -> SurfaceOperationRaise """
        pass

    def RaiseVertices(self, vertices, deltaElevation):
        """ RaiseVertices(self: TinSurface, vertices: IEnumerable[TinSurfaceVertex], deltaElevation: float) -> SurfaceOperationModifyMultipleTinVerticesElevation """
        pass

    def SampleElevations(self, *__args):
        """
        SampleElevations(self: TinSurface, curveId: ObjectId) -> Point3dCollection
        SampleElevations(self: TinSurface, pt1: Point3d, pt2: Point3d) -> Point3dCollection
        """
        pass

    def SetVertexElevation(self, vertex, newElevation):
        """ SetVertexElevation(self: TinSurface, vertex: TinSurfaceVertex, newElevation: float) -> SurfaceOperationModifyTinVertexElevation """
        pass

    def SetVerticesElevation(self, vertices, newElevation):
        """ SetVerticesElevation(self: TinSurface, vertices: IEnumerable[TinSurfaceVertex], newElevation: float) -> SurfaceOperationModifyMultipleTinVerticesElevation """
        pass

    def SimplifySurface(self, simplifyOptions):
        """ SimplifySurface(self: TinSurface, simplifyOptions: SurfaceSimplifyOptions) -> SurfaceOperationSimplify """
        pass

    def SmoothSurfaceByKriging(self, krigingOptions, pointOutputOptions):
        """ SmoothSurfaceByKriging(self: TinSurface, krigingOptions: KrigingMethodOptions, pointOutputOptions: SurfacePointOutputOptions) -> SurfaceOperationSmooth """
        pass

    def SmoothSurfaceByNNI(self, pointOutputOptions):
        """ SmoothSurfaceByNNI(self: TinSurface, pointOutputOptions: SurfacePointOutputOptions) -> SurfaceOperationSmooth """
        pass

    def SwapEdge(self, tinTriangleEdge):
        """ SwapEdge(self: TinSurface, tinTriangleEdge: TinSurfaceEdge) -> SurfaceOperationSwapEdge """
        pass

    BreaklinesDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BreaklinesDefinition(self: TinSurface) -> SurfaceDefinitionBreaklines

"""

    ContoursDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContoursDefinition(self: TinSurface) -> SurfaceDefinitionContours

"""

    DEMFilesDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DEMFilesDefinition(self: TinSurface) -> SurfaceDefinitionDEMFiles

"""

    DrawingObjectsDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawingObjectsDefinition(self: TinSurface) -> SurfaceDefinitionDrawingObjects

"""

    PointFilesDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointFilesDefinition(self: TinSurface) -> SurfaceDefinitionPointFiles

"""

    PointGroupsDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointGroupsDefinition(self: TinSurface) -> SurfaceDefinitionPointGroups

"""

    SurveyQueriesAddFigureDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurveyQueriesAddFigureDefinition(self: TinSurface) -> SurfaceDefinitionAddFigureSurveyQueries

"""

    SurveyQueriesAddPointDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurveyQueriesAddPointDefinition(self: TinSurface) -> SurfaceDefinitionAddPointSurveyQueries

"""

    Triangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Triangles(self: TinSurface) -> TinSurfaceTriangleCollection

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: TinSurface) -> TinSurfaceVertexCollection

"""



class TinSurfaceObject(object):
    # no doc
    def CheckValid(self, *args): #cannot find CLR method
        """ CheckValid(self: TinSurfaceObject) """
        pass

    def Dispose(self):
        """ Dispose(self: TinSurfaceObject) """
        pass

    def GetAeccSurfaceTin(self, *args): #cannot find CLR method
        """ GetAeccSurfaceTin(self: TinSurfaceObject) -> AeccSurfaceTin* """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: TinSurfaceObject) -> bool

"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: TinSurfaceObject) -> TinSurface

"""


    m_pSurfaceAPIObject = None


class TinSurfaceEdge(TinSurfaceObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceEdge, A_0: bool) """
        pass

    def Equals(self, rhs):
        """ Equals(self: TinSurfaceEdge, rhs: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TinSurfaceEdge) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: TinSurfaceEdge) -> bool

"""

    Triangle1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Triangle1(self: TinSurfaceEdge) -> TinSurfaceTriangle

"""

    Triangle2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Triangle2(self: TinSurfaceEdge) -> TinSurfaceTriangle

"""

    Vertex1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex1(self: TinSurfaceEdge) -> TinSurfaceVertex

"""

    Vertex2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex2(self: TinSurfaceEdge) -> TinSurfaceVertex

"""


    m_pSurfaceAPIObject = None


class TinSurfaceEdgeCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceEdgeCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: TinSurfaceEdgeCollection) -> IEnumerator[TinSurfaceEdge] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: TinSurfaceEdgeCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TinSurfaceEdge](enumerable: IEnumerable[TinSurfaceEdge], value: TinSurfaceEdge) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: TinSurfaceEdgeCollection) -> int

"""



class TinSurfaceEdgeEnumerator(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceEdgeEnumerator) """
        pass

    def MoveNext(self):
        """ MoveNext(self: TinSurfaceEdgeEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: TinSurfaceEdgeEnumerator) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TinSurfaceEdge](enumerator: IEnumerator[TinSurfaceEdge], value: TinSurfaceEdge) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: TinSurfaceEdgeEnumerator) -> TinSurfaceEdge

"""

    CurrentObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentObject(self: TinSurfaceEdgeEnumerator) -> object

"""



class TinSurfaceProperties(object):
    # no doc
    MaximumTriangleArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumTriangleArea(self: TinSurfaceProperties) -> float

"""

    MaximumTriangleLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumTriangleLength(self: TinSurfaceProperties) -> float

"""

    MinimumTriangleArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumTriangleArea(self: TinSurfaceProperties) -> float

"""

    MinimumTriangleLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumTriangleLength(self: TinSurfaceProperties) -> float

"""

    NumberOfTriangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfTriangles(self: TinSurfaceProperties) -> int

"""



class TinSurfaceTriangle(TinSurfaceObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceObject, A_0: bool) """
        pass

    def Equals(self, rhs):
        """ Equals(self: TinSurfaceTriangle, rhs: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TinSurfaceTriangle) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Edge1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge1(self: TinSurfaceTriangle) -> TinSurfaceEdge

"""

    Edge2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge2(self: TinSurfaceTriangle) -> TinSurfaceEdge

"""

    Edge3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edge3(self: TinSurfaceTriangle) -> TinSurfaceEdge

"""

    Vertex1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex1(self: TinSurfaceTriangle) -> TinSurfaceVertex

"""

    Vertex2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex2(self: TinSurfaceTriangle) -> TinSurfaceVertex

"""

    Vertex3 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex3(self: TinSurfaceTriangle) -> TinSurfaceVertex

"""


    m_pSurfaceAPIObject = None


class TinSurfaceTriangleCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceTriangleCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: TinSurfaceTriangleCollection) -> IEnumerator[TinSurfaceTriangle] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: TinSurfaceTriangleCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TinSurfaceTriangle](enumerable: IEnumerable[TinSurfaceTriangle], value: TinSurfaceTriangle) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: TinSurfaceTriangleCollection) -> int

"""



class TinSurfaceTriangleEnumerator(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceTriangleEnumerator) """
        pass

    def MoveNext(self):
        """ MoveNext(self: TinSurfaceTriangleEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: TinSurfaceTriangleEnumerator) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TinSurfaceTriangle](enumerator: IEnumerator[TinSurfaceTriangle], value: TinSurfaceTriangle) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: TinSurfaceTriangleEnumerator) -> TinSurfaceTriangle

"""

    CurrentObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentObject(self: TinSurfaceTriangleEnumerator) -> object

"""



class TinSurfaceVertex(TinSurfaceObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceObject, A_0: bool) """
        pass

    def Equals(self, rhs):
        """ Equals(self: TinSurfaceVertex, rhs: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: TinSurfaceVertex) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: TinSurfaceVertex) -> TinSurfaceEdgeCollection

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: TinSurfaceVertex) -> Point3d

"""

    Triangles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Triangles(self: TinSurfaceVertex) -> TinSurfaceTriangleCollection

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: TinSurfaceVertex) -> TinSurfaceVertexCollection

"""


    m_pSurfaceAPIObject = None


class TinSurfaceVertexCollection(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceVertexCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: TinSurfaceVertexCollection) -> IEnumerator[TinSurfaceVertex] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: TinSurfaceVertexCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TinSurfaceVertex](enumerable: IEnumerable[TinSurfaceVertex], value: TinSurfaceVertex) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: TinSurfaceVertexCollection) -> int

"""



class TinSurfaceVertexEnumerator(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: TinSurfaceVertexEnumerator) """
        pass

    def MoveNext(self):
        """ MoveNext(self: TinSurfaceVertexEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: TinSurfaceVertexEnumerator) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TinSurfaceVertex](enumerator: IEnumerator[TinSurfaceVertex], value: TinSurfaceVertex) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: TinSurfaceVertexEnumerator) -> TinSurfaceVertex

"""

    CurrentObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentObject(self: TinSurfaceVertexEnumerator) -> object

"""



class TinVolumeSurface(Surface):
    # no doc
    @staticmethod
    def Create(surfaceName, baseSurfaceId, comparisonSurfaceId, styleId=None):
        """
        Create(surfaceName: str, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId) -> ObjectId
        Create(surfaceName: str, baseSurfaceId: ObjectId, comparisonSurfaceId: ObjectId, styleId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetTinProperties(self):
        """ GetTinProperties(self: TinVolumeSurface) -> TinSurfaceProperties """
        pass

    def GetVolumeProperties(self):
        """ GetVolumeProperties(self: TinVolumeSurface) -> VolumeSurfaceProperties """
        pass

    CutFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutFactor(self: TinVolumeSurface) -> float

Set: CutFactor(self: TinVolumeSurface) = value
"""

    FillFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillFactor(self: TinVolumeSurface) -> float

Set: FillFactor(self: TinVolumeSurface) = value
"""



class UDP(object):
    # no doc
    ClassificationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassificationName(self: UDP) -> str

"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: UDP) -> object

Set: DefaultValue(self: UDP) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: UDP) -> str

Set: Description(self: UDP) = value
"""

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Guid(self: UDP) -> Guid

"""

    IsInUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInUsed(self: UDP) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: UDP) -> str

"""

    UseDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultValue(self: UDP) -> bool

Set: UseDefaultValue(self: UDP) = value
"""



class UDPBoolean(UDP):
    # no doc
    def InternalGetAttributeTypeInfo(self):
        """ InternalGetAttributeTypeInfo(self: UDPBoolean) -> AeccAttributeTypeInfoBool* """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: UDPBoolean) -> bool

Set: DefaultValue(self: UDPBoolean) = value
"""



class UDPClassification(object):
    # no doc
    def ContainsUDP(self, udp):
        """ ContainsUDP(self: UDPClassification, udp: UDP) -> bool """
        pass

    def CreateUDP(self, udpTypeInfo, guid=None):
        """
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoInt, guid: Guid) -> UDPInteger
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoBool) -> UDPBoolean
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoInt) -> UDPInteger
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoString) -> UDPString
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoString, guid: Guid) -> UDPString
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoDouble) -> UDPDouble
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoDouble, guid: Guid) -> UDPDouble
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoEnum, guid: Guid) -> UDPEnumeration
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoBool, guid: Guid) -> UDPBoolean
        CreateUDP(self: UDPClassification, udpTypeInfo: AttributeTypeInfoEnum) -> UDPEnumeration
        """
        pass

    def RemoveUDP(self, udp):
        """ RemoveUDP(self: UDPClassification, udp: UDP) -> bool """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: UDPClassification) -> str

"""

    UDPs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UDPs(self: UDPClassification) -> UDPCollection

"""



class UDPClassificationApplyType(Enum):
    """ enum UDPClassificationApplyType, values: All (0), Custom (2), None (1) """
    All = None
    Custom = None
    None = None
    value__ = None


class UDPClassificationCollection(object):
    # no doc
    def Add(self, name):
        """ Add(self: UDPClassificationCollection, name: str) -> UDPClassification """
        pass

    def Contains(self, *__args):
        """
        Contains(self: UDPClassificationCollection, udpClassification: UDPClassification) -> bool
        Contains(self: UDPClassificationCollection, name: str) -> bool
        """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: UDPClassificationCollection) -> IEnumerator[UDPClassification] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: UDPClassificationCollection) -> IEnumerator """
        pass

    @staticmethod
    def GetPointUDPClassifications(pDatabase):
        """ GetPointUDPClassifications(pDatabase: Database) -> UDPClassificationCollection """
        pass

    def Remove(self, *__args):
        """
        Remove(self: UDPClassificationCollection, name: str) -> bool
        Remove(self: UDPClassificationCollection, udpClassification: UDPClassification) -> bool
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UDPClassification](enumerable: IEnumerable[UDPClassification], value: UDPClassification) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: UDPClassificationCollection) -> int

"""



class UDPCollection(object):
    # no doc
    def Contains(self, udp):
        """ Contains(self: UDPCollection, udp: UDP) -> bool """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: UDPCollection) -> IEnumerator[UDP] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: UDPCollection) -> IEnumerator """
        pass

    def ToArray(self):
        """ ToArray(self: UDPCollection) -> Array[UDP] """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[UDP](enumerable: IEnumerable[UDP], value: UDP) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: UDPCollection) -> int

"""



class UDPDouble(UDP):
    # no doc
    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: UDPDouble) -> AttributeTypeInfoDoubleDataType

Set: DataType(self: UDPDouble) = value
"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: UDPDouble) -> float

Set: DefaultValue(self: UDPDouble) = value
"""

    LowerBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundInclusive(self: UDPDouble) -> bool

Set: LowerBoundInclusive(self: UDPDouble) = value
"""

    LowerBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundValue(self: UDPDouble) -> float

Set: LowerBoundValue(self: UDPDouble) = value
"""

    UpperBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundInclusive(self: UDPDouble) -> bool

Set: UpperBoundInclusive(self: UDPDouble) = value
"""

    UpperBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundValue(self: UDPDouble) -> float

Set: UpperBoundValue(self: UDPDouble) = value
"""



class UDPEnumeration(UDP):
    # no doc
    def GetEnumValues(self):
        """ GetEnumValues(self: UDPEnumeration) -> Array[str] """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: UDPEnumeration) -> str

Set: DefaultValue(self: UDPEnumeration) = value
"""



class UDPInteger(UDP):
    # no doc
    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: UDPInteger) -> int

Set: DefaultValue(self: UDPInteger) = value
"""

    LowerBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundInclusive(self: UDPInteger) -> bool

Set: LowerBoundInclusive(self: UDPInteger) = value
"""

    LowerBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerBoundValue(self: UDPInteger) -> int

Set: LowerBoundValue(self: UDPInteger) = value
"""

    UpperBoundInclusive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundInclusive(self: UDPInteger) -> bool

Set: UpperBoundInclusive(self: UDPInteger) = value
"""

    UpperBoundValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperBoundValue(self: UDPInteger) -> int

Set: UpperBoundValue(self: UDPInteger) = value
"""



class UDPString(UDP):
    # no doc
    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: UDPString) -> str

Set: DefaultValue(self: UDPString) = value
"""



class VerticalCurveType(Enum):
    """ enum VerticalCurveType, values: Crest (770), Sag (769) """
    Crest = None
    Sag = None
    value__ = None


class VerticalGeometryBandLabelGroup(ProfileBandLabelGroup):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(profileViewId):
        """ GetAvailableLabelGroupIds(profileViewId: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAvailableLabelGroups(profileViewId, includeDerived):
        """ GetAvailableLabelGroups(profileViewId: ObjectId, includeDerived: bool) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    m_SubData = None


class ViewFrame(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    AlignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentId(self: ViewFrame) -> ObjectId

"""

    EndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndStation(self: ViewFrame) -> float

"""

    GroupId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupId(self: ViewFrame) -> ObjectId

"""

    IsLabelVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLabelVisible(self: ViewFrame) -> bool

Set: IsLabelVisible(self: ViewFrame) = value
"""

    LabelAnchorPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelAnchorPosition(self: ViewFrame) -> ViewFrameLabelLocationType

Set: LabelAnchorPosition(self: ViewFrame) = value
"""

    LabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleId(self: ViewFrame) -> ObjectId

Set: LabelStyleId(self: ViewFrame) = value
"""

    Sheet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Sheet(self: ViewFrame) -> str

"""

    SheetSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetSet(self: ViewFrame) -> str

"""

    StartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartStation(self: ViewFrame) -> float

"""



class ViewFrameGroup(GeoEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAvailableMatchLineLabelGroupIds(self):
        """ GetAvailableMatchLineLabelGroupIds(self: ViewFrameGroup) -> ObjectIdCollection """
        pass

    def GetAvailableViewFrameLabelGroupIds(self):
        """ GetAvailableViewFrameLabelGroupIds(self: ViewFrameGroup) -> ObjectIdCollection """
        pass

    def GetMatchLineIds(self):
        """ GetMatchLineIds(self: ViewFrameGroup) -> ObjectIdCollection """
        pass

    def GetMatchLineLabelGroupIdBySide(self, side):
        """ GetMatchLineLabelGroupIdBySide(self: ViewFrameGroup, side: EntitySideType) -> ObjectId """
        pass

    def GetViewFrameIds(self):
        """ GetViewFrameIds(self: ViewFrameGroup) -> ObjectIdCollection """
        pass

    DefaultLeftMatchLineLabelAnchorPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultLeftMatchLineLabelAnchorPosition(self: ViewFrameGroup) -> MatchLineLabelLocationType

Set: DefaultLeftMatchLineLabelAnchorPosition(self: ViewFrameGroup) = value
"""

    DefaultLeftMatchLineLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultLeftMatchLineLabelStyleId(self: ViewFrameGroup) -> ObjectId

Set: DefaultLeftMatchLineLabelStyleId(self: ViewFrameGroup) = value
"""

    DefaultRightMatchLineLabelAnchorPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultRightMatchLineLabelAnchorPosition(self: ViewFrameGroup) -> MatchLineLabelLocationType

Set: DefaultRightMatchLineLabelAnchorPosition(self: ViewFrameGroup) = value
"""

    DefaultRightMatchLineLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultRightMatchLineLabelStyleId(self: ViewFrameGroup) -> ObjectId

Set: DefaultRightMatchLineLabelStyleId(self: ViewFrameGroup) = value
"""

    DefaultViewFrameLabelAnchorPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultViewFrameLabelAnchorPosition(self: ViewFrameGroup) -> ViewFrameLabelLocationType

Set: DefaultViewFrameLabelAnchorPosition(self: ViewFrameGroup) = value
"""

    DefaultViewFrameLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultViewFrameLabelStyleId(self: ViewFrameGroup) -> ObjectId

Set: DefaultViewFrameLabelStyleId(self: ViewFrameGroup) = value
"""



class ViewFrameLabelGroup(AutoFeatureLabelGroup):
    # no doc
    @staticmethod
    def Create(viewFrameGroupId, labelStyleId=None, anchorPosition=None):
        """
        Create(viewFrameGroupId: ObjectId, labelStyleId: ObjectId, anchorPosition: ViewFrameLabelLocationType) -> ObjectId
        Create(viewFrameGroupId: ObjectId) -> ObjectId
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailableLabelGroupIds(viewFrameGroupId):
        """ GetAvailableLabelGroupIds(viewFrameGroupId: ObjectId) -> ObjectIdCollection """
        pass

    m_SubData = None


class VolumeSurfaceProperties(object):
    # no doc
    AdjustedCutVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjustedCutVolume(self: VolumeSurfaceProperties) -> float

"""

    AdjustedFillVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjustedFillVolume(self: VolumeSurfaceProperties) -> float

"""

    AdjustedNetVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdjustedNetVolume(self: VolumeSurfaceProperties) -> float

"""

    BaseSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseSurface(self: VolumeSurfaceProperties) -> ObjectId

"""

    ComparisonSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComparisonSurface(self: VolumeSurfaceProperties) -> ObjectId

"""

    CutFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutFactor(self: VolumeSurfaceProperties) -> float

"""

    FillFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillFactor(self: VolumeSurfaceProperties) -> float

"""

    UnadjustedCutVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnadjustedCutVolume(self: VolumeSurfaceProperties) -> float

"""

    UnadjustedFillVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnadjustedFillVolume(self: VolumeSurfaceProperties) -> float

"""

    UnadjustedNetVolume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnadjustedNetVolume(self: VolumeSurfaceProperties) -> float

"""



class VolumeTableType(Enum):
    """ enum VolumeTableType, values: Material (1), TotalVolume (0) """
    Material = None
    TotalVolume = None
    value__ = None


class WallBreaklineCreationData(object):
    # no doc
    Elevation = None
    IsRightSideOffset = None
    SourceId = None


class WallBreaklineCreationDataEx(object):
    # no doc
    Elevations = None
    IsRightSideOffset = None
    SourceId = None


class WidthOffsetTarget(CivilWrapper<AeccWidthOffsetTarget>):
    """ WidthOffsetTarget(targetId: ObjectId) """
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccWidthOffsetTarget>, A_0: bool) """
        pass

    def GetDistanceToAlignment(self, alignmentId, stationOnAlignment, *__args):
        """
        GetDistanceToAlignment(self: WidthOffsetTarget, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide, xOnTarget: float, yOnTarget: float) -> (float, float, float)
        GetDistanceToAlignment(self: WidthOffsetTarget, alignmentId: ObjectId, stationOnAlignment: float, xOnTarget: float, yOnTarget: float) -> (float, float, float)
        """
        pass

    def GetNearestPipeOfNetworkToAlignment(self, alignmentId, stationOnAlignment, *__args):
        """
        GetNearestPipeOfNetworkToAlignment(self: WidthOffsetTarget, alignmentId: ObjectId, stationOnAlignment: float, pipeId: ObjectId) -> ObjectId
        GetNearestPipeOfNetworkToAlignment(self: WidthOffsetTarget, alignmentId: ObjectId, stationOnAlignment: float, side: AlignmentSide, pipeId: ObjectId) -> ObjectId
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, targetId):
        """ __new__(cls: type, targetId: ObjectId) """
        pass

    TargetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetId(self: WidthOffsetTarget) -> ObjectId

"""



# variables with complex values

