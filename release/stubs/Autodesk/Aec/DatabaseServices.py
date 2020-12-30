# encoding: utf-8
# module Autodesk.Aec.DatabaseServices calls itself DatabaseServices
# from AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null, AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ADTDwgVersion(Enum):
    """ enum ADTDwgVersion, values: Current (8), Future (32767), NoADTObjects (0), R1 (1), R2 (2), R3 (3), R4 (4), R5 (5), R6 (6) """
    Current = None
    Future = None
    NoADTObjects = None
    R1 = None
    R2 = None
    R3 = None
    R4 = None
    R5 = None
    R6 = None
    value__ = None


class AecXReferenceSubcommandActivities(Enum):
    """ enum AecXReferenceSubcommandActivities, values: Aborted (6), End (4), EndItem (3), Start (0), StartItem (2), StartXBindBlock (7), StartXBindSymbol (8), WillAbort (5) """
    Aborted = None
    End = None
    EndItem = None
    Start = None
    StartItem = None
    StartXBindBlock = None
    StartXBindSymbol = None
    value__ = None
    WillAbort = None


class DBObject(DBObject):
    """ DBObject() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetMaterialComponents(self, componentIds, componentNames, materialIds):
        """ GetMaterialComponents(self: DBObject) -> (IntegerCollection, StringCollection, ObjectIdCollection) """
        pass

    def SetMaterialComponents(self, componentIds, materialIds):
        """ SetMaterialComponents(self: DBObject, componentIds: IntegerCollection, materialIds: ObjectIdCollection) """
        pass

    def SetToStandard(self, db):
        """ SetToStandard(self: DBObject, db: Database) """
        pass

    def SubSetDatabaseDefaults(self, db):
        """ SubSetDatabaseDefaults(self: DBObject, db: Database) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: DBObject) -> str

Set: Description(self: DBObject) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: DBObject) -> str

"""

    Overrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Overrides(self: DBObject) -> OverrideCollection

"""

    SwappingReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SwappingReferences(self: DBObject) -> bool

Set: SwappingReferences(self: DBObject) = value
"""

    TypeIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeIcon(self: DBObject) -> Icon

"""



class Anchor(DBObject):
    """ Anchor() """
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


class AnchorContext(Enum):
    """ enum AnchorContext, values: AlreadyAttached (1), NewAttachment (0) """
    AlreadyAttached = None
    NewAttachment = None
    value__ = None


class AnchorToReference(Anchor):
    """ AnchorToReference() """
    def AppendNestedReferenceObject(self, id, db, relationType):
        """ AppendNestedReferenceObject(self: AnchorToReference, id: ObjectId, db: Database, relationType: RelationType) """
        pass

    def AppendReferenceObject(self, id, relationType):
        """ AppendReferenceObject(self: AnchorToReference, id: ObjectId, relationType: RelationType) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetNestedReferenceObjectAt(self, index, relationType):
        """ GetNestedReferenceObjectAt(self: AnchorToReference, index: int) -> (ObjectId, RelationType) """
        pass

    def GetNestedSingleReference(self, relationType):
        """ GetNestedSingleReference(self: AnchorToReference) -> (ObjectId, RelationType) """
        pass

    def GetReferenceObjectAt(self, index, relationType):
        """ GetReferenceObjectAt(self: AnchorToReference, index: int) -> (ObjectId, RelationType) """
        pass

    def GetSingleReference(self, relationType):
        """ GetSingleReference(self: AnchorToReference) -> (ObjectId, RelationType) """
        pass

    def IsReferenced(self, id, relationType):
        """ IsReferenced(self: AnchorToReference, id: ObjectId) -> (bool, RelationType) """
        pass

    def IsReferencedNested(self, aecId, db, relationType):
        """ IsReferencedNested(self: AnchorToReference, aecId: ObjectId, db: Database) -> (bool, RelationType) """
        pass

    def MirrorParameters(self, referenceWasMirrored, geo, transform):
        """ MirrorParameters(self: AnchorToReference, referenceWasMirrored: bool, geo: Geo, transform: Matrix3d) """
        pass

    def RemoveAllReferenceObjects(self):
        """ RemoveAllReferenceObjects(self: AnchorToReference) """
        pass

    def RemoveNestedReferenceObject(self, id, db):
        """ RemoveNestedReferenceObject(self: AnchorToReference, id: ObjectId, db: Database) """
        pass

    def RemoveReferenceObject(self, id):
        """ RemoveReferenceObject(self: AnchorToReference, id: ObjectId) """
        pass

    def SetNestedSingleReference(self, aecId, db, relationType):
        """ SetNestedSingleReference(self: AnchorToReference, aecId: ObjectId, db: Database, relationType: RelationType) """
        pass

    def SetSingleReference(self, id, relationType):
        """ SetSingleReference(self: AnchorToReference, id: ObjectId, relationType: RelationType) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ReferenceObjectCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceObjectCount(self: AnchorToReference) -> int

"""

    SingleReferenceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleReferenceId(self: AnchorToReference) -> ObjectId

"""



class AnchorEntityToCurve(AnchorToReference):
    """ AnchorEntityToCurve() """
    def CalculateCurveNormal(self, curve):
        """ CalculateCurveNormal(self: AnchorEntityToCurve, curve: Curve) -> Vector3d """
        pass

    def CalculateCurveThickness(self, curve):
        """ CalculateCurveThickness(self: AnchorEntityToCurve, curve: Curve) -> float """
        pass

    def CalculateCurveWidth(self, curve):
        """ CalculateCurveWidth(self: AnchorEntityToCurve, curve: Curve) -> float """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetEntityExtents(self, geo):
        """ GetEntityExtents(self: AnchorEntityToCurve, geo: Geo) -> BoundBlock3d """
        pass

    def ReverseParameters(self):
        """ ReverseParameters(self: AnchorEntityToCurve) """
        pass

    def SwitchAnchoredEnd(self, geo):
        """ SwitchAnchoredEnd(self: AnchorEntityToCurve, geo: Geo) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AnchorX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorX(self: AnchorEntityToCurve) -> AnchorToCurveX

"""

    AnchorY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorY(self: AnchorEntityToCurve) -> AnchorToCurveY

"""

    AnchorZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorZ(self: AnchorEntityToCurve) -> AnchorToCurveZ

"""

    CurveId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveId(self: AnchorEntityToCurve) -> ObjectId

Set: CurveId(self: AnchorEntityToCurve) = value
"""

    CurveNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveNormal(self: AnchorEntityToCurve) -> Vector3d

"""

    CurveThickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveThickness(self: AnchorEntityToCurve) -> float

"""

    CurveWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveWidth(self: AnchorEntityToCurve) -> float

"""

    FlipX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlipX(self: AnchorEntityToCurve) -> bool

Set: FlipX(self: AnchorEntityToCurve) = value
"""

    FlipY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlipY(self: AnchorEntityToCurve) -> bool

Set: FlipY(self: AnchorEntityToCurve) = value
"""

    FlipZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlipZ(self: AnchorEntityToCurve) -> bool

Set: FlipZ(self: AnchorEntityToCurve) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: AnchorEntityToCurve) -> float

Set: Rotation(self: AnchorEntityToCurve) = value
"""

    RotationAroundX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationAroundX(self: AnchorEntityToCurve) -> float

Set: RotationAroundX(self: AnchorEntityToCurve) = value
"""



class AnchorEntityToEntity(AnchorToReference):
    """ AnchorEntityToEntity() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def SetReferencedEntity(self, geo):
        """ SetReferencedEntity(self: AnchorEntityToEntity, geo: Geo) """
        pass

    def SetReferencedEntityOldEcs(self, mat):
        """ SetReferencedEntityOldEcs(self: AnchorEntityToEntity, mat: Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ReferencedEntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferencedEntityId(self: AnchorEntityToEntity) -> ObjectId

Set: ReferencedEntityId(self: AnchorEntityToEntity) = value
"""



class AnchorEntityToGridAssembly(AnchorToReference):
    """ AnchorEntityToGridAssembly() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetOrientation(self, flipX, flipY, flipZ):
        """ GetOrientation(self: AnchorEntityToGridAssembly) -> (bool, bool, bool) """
        pass

    def SetOrientation(self, flipX, flipY, flipZ):
        """ SetOrientation(self: AnchorEntityToGridAssembly, flipX: bool, flipY: bool, flipZ: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AllowVariesFromInfillDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowVariesFromInfillDefinition(self: AnchorEntityToGridAssembly) -> bool

Set: AllowVariesFromInfillDefinition(self: AnchorEntityToGridAssembly) = value
"""

    BottomOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomOffset(self: AnchorEntityToGridAssembly) -> float

Set: BottomOffset(self: AnchorEntityToGridAssembly) = value
"""

    GridAssemblyCellId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAssemblyCellId(self: AnchorEntityToGridAssembly) -> int

Set: GridAssemblyCellId(self: AnchorEntityToGridAssembly) = value
"""

    GridAssemblyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAssemblyId(self: AnchorEntityToGridAssembly) -> ObjectId

Set: GridAssemblyId(self: AnchorEntityToGridAssembly) = value
"""

    HasSizingOffsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasSizingOffsets(self: AnchorEntityToGridAssembly) -> bool

Set: HasSizingOffsets(self: AnchorEntityToGridAssembly) = value
"""

    LeftOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftOffset(self: AnchorEntityToGridAssembly) -> float

Set: LeftOffset(self: AnchorEntityToGridAssembly) = value
"""

    RightOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightOffset(self: AnchorEntityToGridAssembly) -> float

Set: RightOffset(self: AnchorEntityToGridAssembly) = value
"""

    TopOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopOffset(self: AnchorEntityToGridAssembly) -> float

Set: TopOffset(self: AnchorEntityToGridAssembly) = value
"""

    YAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAlignment(self: AnchorEntityToGridAssembly) -> YAlignment

Set: YAlignment(self: AnchorEntityToGridAssembly) = value
"""

    YOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YOffset(self: AnchorEntityToGridAssembly) -> float

Set: YOffset(self: AnchorEntityToGridAssembly) = value
"""



class AnchorEntityToLayoutNode(AnchorToReference):
    """ AnchorEntityToLayoutNode() """
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

    FlipX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlipX(self: AnchorEntityToLayoutNode) -> bool

Set: FlipX(self: AnchorEntityToLayoutNode) = value
"""

    FlipY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlipY(self: AnchorEntityToLayoutNode) -> bool

Set: FlipY(self: AnchorEntityToLayoutNode) = value
"""

    FlipZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlipZ(self: AnchorEntityToLayoutNode) -> bool

Set: FlipZ(self: AnchorEntityToLayoutNode) = value
"""

    LayoutNodeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutNodeId(self: AnchorEntityToLayoutNode) -> int

Set: LayoutNodeId(self: AnchorEntityToLayoutNode) = value
"""

    LayoutNodeIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutNodeIndex(self: AnchorEntityToLayoutNode) -> int

Set: LayoutNodeIndex(self: AnchorEntityToLayoutNode) = value
"""

    LayoutToolId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutToolId(self: AnchorEntityToLayoutNode) -> ObjectId

Set: LayoutToolId(self: AnchorEntityToLayoutNode) = value
"""

    NormalVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalVector(self: AnchorEntityToLayoutNode) -> Vector3d

Set: NormalVector(self: AnchorEntityToLayoutNode) = value
"""

    OffsetToCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetToCenter(self: AnchorEntityToLayoutNode) -> bool

Set: OffsetToCenter(self: AnchorEntityToLayoutNode) = value
"""

    OffsetVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetVector(self: AnchorEntityToLayoutNode) -> Vector3d

Set: OffsetVector(self: AnchorEntityToLayoutNode) = value
"""

    UseLocalCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseLocalCoordinateSystem(self: AnchorEntityToLayoutNode) -> bool

Set: UseLocalCoordinateSystem(self: AnchorEntityToLayoutNode) = value
"""

    XRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XRotation(self: AnchorEntityToLayoutNode) -> float

Set: XRotation(self: AnchorEntityToLayoutNode) = value
"""

    YRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YRotation(self: AnchorEntityToLayoutNode) -> float

Set: YRotation(self: AnchorEntityToLayoutNode) = value
"""

    ZRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZRotation(self: AnchorEntityToLayoutNode) -> float

Set: ZRotation(self: AnchorEntityToLayoutNode) = value
"""



class AnchorEntityToLayoutCell(AnchorEntityToLayoutNode):
    """ AnchorEntityToLayoutCell() """
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

    ApplyResize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplyResize(self: AnchorEntityToLayoutCell) -> bool

Set: ApplyResize(self: AnchorEntityToLayoutCell) = value
"""

    ResizeOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResizeOffset(self: AnchorEntityToLayoutCell) -> float

Set: ResizeOffset(self: AnchorEntityToLayoutCell) = value
"""



class AnchorEntityToLayoutVolume(AnchorEntityToLayoutCell):
    """ AnchorEntityToLayoutVolume() """
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


class AnchorLeaderToNode(AnchorEntityToLayoutNode):
    """ AnchorLeaderToNode() """
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

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: AnchorLeaderToNode) -> float

Set: Angle(self: AnchorLeaderToNode) = value
"""

    FirstExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstExtension(self: AnchorLeaderToNode) -> float

Set: FirstExtension(self: AnchorLeaderToNode) = value
"""

    SecondExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondExtension(self: AnchorLeaderToNode) -> float

Set: SecondExtension(self: AnchorLeaderToNode) = value
"""

    Vectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vectors(self: AnchorLeaderToNode) -> AnchorLeaderToNodeVectorCollection

"""



class AnchorLeaderToNodeVectorCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: AnchorLeaderToNodeVectorCollection, value: Vector2d) -> int """
        pass

    def Clear(self):
        """ Clear(self: AnchorLeaderToNodeVectorCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: AnchorLeaderToNodeVectorCollection, value: Vector2d) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: AnchorLeaderToNodeVectorCollection, array: Array[Vector2d], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AnchorLeaderToNodeVectorCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: AnchorLeaderToNodeVectorCollection, value: Vector2d) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: AnchorLeaderToNodeVectorCollection, index: int, value: Vector2d) """
        pass

    def Remove(self, value):
        """ Remove(self: AnchorLeaderToNodeVectorCollection, value: Vector2d) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: AnchorLeaderToNodeVectorCollection, index: int) """
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
    """Get: Count(self: AnchorLeaderToNodeVectorCollection) -> int

"""



class ImpObject(RXObject):
    """ ImpObject() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetToStandard(self, db):
        """ SetToStandard(self: ImpObject, db: Database) """
        pass

    def SubSetDatabaseDefaults(self, db):
        """ SubSetDatabaseDefaults(self: ImpObject, db: Database) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: ImpObject) -> Database

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: ImpObject) -> str

Set: Description(self: ImpObject) = value
"""



class AnchorToCurveX(ImpObject):
    """ AnchorToCurveX() """
    def CalculatePosition(self, curve, entityLength, insertionOffset, position, directionX, directionY, directionZ):
        """ CalculatePosition(self: AnchorToCurveX, curve: Curve, entityLength: float, insertionOffset: float) -> (Point3d, Vector3d, Vector3d, Vector3d) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def ReverseParameters(self):
        """ ReverseParameters(self: AnchorToCurveX) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    MeasureToType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeasureToType(self: AnchorToCurveX) -> CurveXMeasureToType

Set: MeasureToType(self: AnchorToCurveX) = value
"""

    OffsetDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetDistance(self: AnchorToCurveX) -> float

Set: OffsetDistance(self: AnchorToCurveX) = value
"""

    OffsetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetType(self: AnchorToCurveX) -> CurveXOffsetType

Set: OffsetType(self: AnchorToCurveX) = value
"""



class AnchorToCurveY(ImpObject):
    """ AnchorToCurveY() """
    def CalculateYOffset(self, curveThickness, entityThickness, insertionOffset):
        """ CalculateYOffset(self: AnchorToCurveY, curveThickness: float, entityThickness: float, insertionOffset: float) -> float """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    MeasureToType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MeasureToType(self: AnchorToCurveY) -> CurveYMeasureToType

Set: MeasureToType(self: AnchorToCurveY) = value
"""

    OffsetDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetDistance(self: AnchorToCurveY) -> float

Set: OffsetDistance(self: AnchorToCurveY) = value
"""

    OffsetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetType(self: AnchorToCurveY) -> CurveYOffsetType

Set: OffsetType(self: AnchorToCurveY) = value
"""



class AnchorToCurveZ(ImpObject):
    """ AnchorToCurveZ() """
    def CalculateZOffset(self, curveHeight, entityHeight, insertionOffset):
        """ CalculateZOffset(self: AnchorToCurveZ, curveHeight: float, entityHeight: float, insertionOffset: float) -> float """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    OffsetDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetDistance(self: AnchorToCurveZ) -> float

Set: OffsetDistance(self: AnchorToCurveZ) = value
"""

    OffsetFromType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetFromType(self: AnchorToCurveZ) -> CurveZOffsetFromType

Set: OffsetFromType(self: AnchorToCurveZ) = value
"""

    OffsetToType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetToType(self: AnchorToCurveZ) -> CurveZOffsetToType

Set: OffsetToType(self: AnchorToCurveZ) = value
"""



class AngularUnit(Enum):
    """ enum AngularUnit, values: CurrentAU (-1), DegMinSec (1), Degrees (0), Grads (2), Radians (3), Surveyor (4) """
    CurrentAU = None
    DegMinSec = None
    Degrees = None
    Grads = None
    Radians = None
    Surveyor = None
    value__ = None


class ApplyToFlags(Enum):
    """ enum (flags) ApplyToFlags, values: ApplyToBoundaryEdges (2), ApplyToInfill (1), ApplyToInteriorEdges (4) """
    ApplyToBoundaryEdges = None
    ApplyToInfill = None
    ApplyToInteriorEdges = None
    value__ = None


class Attribute(ImpObject):
    """ Attribute() """
    def Copy(self):
        """ Copy(self: Attribute) -> Attribute """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class AttributeId(Attribute):
    """
    AttributeId(aecObjectId: ObjectId)
    AttributeId()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, aecObjectId=None):
        """
        __new__(cls: type, aecObjectId: ObjectId)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: AttributeId) -> ObjectId

"""



class AutomaticSpaceBoundary(Enum):
    """ enum AutomaticSpaceBoundary, values: ByStyle (2), No (1), NotApplicableToThisObject (-1), Yes (0) """
    ByStyle = None
    No = None
    NotApplicableToThisObject = None
    value__ = None
    Yes = None


class AxisReference(Enum):
    """ enum AxisReference, values: End (2), Mid (1), Start (0) """
    End = None
    Mid = None
    Start = None
    value__ = None


class Entity(Curve):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAutomaticallyBoundSpaces(self, blockRefPath, boundSpaces):
        """ GetAutomaticallyBoundSpaces(self: Entity, blockRefPath: ObjectIdCollection) -> AutomaticSpaceBoundary """
        pass

    def GetBaseProfile(self, toWcs):
        """ GetBaseProfile(self: Entity) -> (Profile, Matrix3d) """
        pass

    def GetLocalExtents(self, extents):
        """ GetLocalExtents(self: Entity) -> BoundBlock3d """
        pass

    def GetLocalModelCachedExtents(self, ext):
        """ GetLocalModelCachedExtents(self: Entity) -> BoundBlock3d """
        pass

    def GetMaterialComponents(self, componentIds, componentNames, materialIds):
        """ GetMaterialComponents(self: Entity) -> (IntegerCollection, StringCollection, ObjectIdCollection) """
        pass

    def GetMaterialLocations(self, locationIds, styleIdArray):
        """ GetMaterialLocations(self: Entity) -> (IntegerCollection, ObjectIdCollection) """
        pass

    def GetProfile(self, cutPlane):
        """ GetProfile(self: Entity, cutPlane: Plane) -> Profile """
        pass

    def GetUsageArea(self, cutPlane):
        """ GetUsageArea(self: Entity, cutPlane: Plane) -> Profile """
        pass

    def GetWorldExtents(self, extents):
        """ GetWorldExtents(self: Entity) -> BoundBlock3d """
        pass

    def SetAutomaticallyBoundSpaces(self, blockRefPath, boundSpaces):
        """ SetAutomaticallyBoundSpaces(self: Entity, blockRefPath: ObjectIdCollection, boundSpaces: AutomaticSpaceBoundary) """
        pass

    def SetBaseProfile(self, profile, matrix):
        """ SetBaseProfile(self: Entity, profile: Profile, matrix: Matrix3d) """
        pass

    def SetDefaultLayer(self):
        """ SetDefaultLayer(self: Entity) """
        pass

    def SetLocalExtents(self, extents, flags):
        """ SetLocalExtents(self: Entity, extents: BoundBlock3d, flags: int) """
        pass

    def SetLocalModelExtentsDirty(self):
        """ SetLocalModelExtentsDirty(self: Entity) """
        pass

    def SetMaterialComponents(self, componentIds, materialIds):
        """ SetMaterialComponents(self: Entity, componentIds: IntegerCollection, materialIds: ObjectIdCollection) """
        pass

    def SetToStandard(self, db):
        """ SetToStandard(self: Entity, db: Database) """
        pass

    def SetWorldExtents(self, extents):
        """ SetWorldExtents(self: Entity, extents: BoundBlock3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    AutomaticallyBoundSpaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticallyBoundSpaces(self: Entity) -> AutomaticSpaceBoundary

Set: AutomaticallyBoundSpaces(self: Entity) = value
"""

    BaseCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseCurve(self: Entity) -> Curve

"""

    Classifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Classifications(self: Entity) -> ClassificationCollection

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Entity) -> str

Set: Description(self: Entity) = value
"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: Entity) -> str

"""

    IsHighlighting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsHighlighting(self: Entity) -> bool

"""

    LayerKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerKey(self: Entity) -> str

"""

    NeedsPromoting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedsPromoting(self: Entity) -> bool

Set: NeedsPromoting(self: Entity) = value
"""

    Overrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Overrides(self: Entity) -> OverrideCollection

"""

    ProjectState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectState(self: Entity) -> ProjectState

Set: ProjectState(self: Entity) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: Entity) -> ObjectId

Set: StyleId(self: Entity) = value
"""

    SupportsBaseCurveCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsBaseCurveCommands(self: Entity) -> bool

"""

    SupportsProfileCommands = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsProfileCommands(self: Entity) -> bool

"""

    SwappingReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SwappingReferences(self: Entity) -> bool

Set: SwappingReferences(self: Entity) = value
"""

    TypeIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeIcon(self: Entity) -> Icon

"""



class Geo(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def MoveInXY(self, offset):
        """ MoveInXY(self: Geo, offset: Vector3d) """
        pass

    def MoveInZ(self, dist):
        """ MoveInZ(self: Geo, dist: float) """
        pass

    def OnGeoEcsModified(self, previousEcs):
        """ OnGeoEcsModified(self: Geo, previousEcs: Matrix3d) """
        pass

    def ReleaseAnchor(self):
        """ ReleaseAnchor(self: Geo) """
        pass

    def SetAnchor(self, newAnchor):
        """ SetAnchor(self: Geo, newAnchor: Anchor) """
        pass

    def TranslateBy(self, offset):
        """ TranslateBy(self: Geo, offset: Vector3d) """
        pass

    def UpdateFromAnchor(self, anchor):
        """ UpdateFromAnchor(self: Geo, anchor: Anchor) """
        pass

    def UpdateGeoEcs(self, forceUpdate):
        """ UpdateGeoEcs(self: Geo, forceUpdate: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    AnchorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnchorId(self: Geo) -> ObjectId

"""

    CanBeAnchored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanBeAnchored(self: Geo) -> bool

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: Geo) -> Vector3d

Set: Direction(self: Geo) = value
"""

    GeoEcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeoEcs(self: Geo) -> Matrix3d

Set: GeoEcs(self: Geo) = value
"""

    GeoEcsIsDirty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeoEcsIsDirty(self: Geo) -> bool

Set: GeoEcsIsDirty(self: Geo) = value
"""

    IsAnchored = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAnchored(self: Geo) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Geo) -> Point3d

Set: Location(self: Geo) = value
"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Geo) -> Vector3d

Set: Normal(self: Geo) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: Geo) -> float

Set: Rotation(self: Geo) = value
"""

    XDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XDir(self: Geo) -> Vector3d

"""

    YDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YDir(self: Geo) -> Vector3d

"""

    ZDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZDir(self: Geo) -> Vector3d

"""



class BlockReference(Geo):
    """ BlockReference() """
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

    BlockDefId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockDefId(self: BlockReference) -> ObjectId

Set: BlockDefId(self: BlockReference) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: BlockReference) -> Scale3d

Set: Scale(self: BlockReference) = value
"""



class BoundaryFlags(Enum):
    """ enum (flags) BoundaryFlags, values: Bottom (4), Left (2), Right (8), Top (1) """
    Bottom = None
    Left = None
    Right = None
    Top = None
    value__ = None


class ByMaterialDisplayComponentType(Enum):
    """ enum ByMaterialDisplayComponentType, values: Body (3), Elevation2dSection (2), Linework (1), None (0), PlanHatch (4), SectionBoundary (7), SectionedBody (8), SectionHatch (6), SurfaceHatch (5) """
    Body = None
    Elevation2dSection = None
    Linework = None
    None = None
    PlanHatch = None
    SectionBoundary = None
    SectionedBody = None
    SectionHatch = None
    SurfaceHatch = None
    value__ = None


class LayoutTool(Geo):
    """ LayoutTool() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetClosestLayoutNode(self, location):
        """ GetClosestLayoutNode(self: LayoutTool, location: Point3d) -> int """
        pass

    def GetLayoutNodeCoordinateSystem(self, nodeId):
        """ GetLayoutNodeCoordinateSystem(self: LayoutTool, nodeId: int) -> Matrix3d """
        pass

    def GetLayoutNodeLocation(self, nodeId):
        """ GetLayoutNodeLocation(self: LayoutTool, nodeId: int) -> Point3d """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    LayoutNodeIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutNodeIds(self: LayoutTool) -> IntegerCollection

"""



class CellLayoutTool(LayoutTool):
    """ CellLayoutTool() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetClosestLayoutCell(self, location):
        """ GetClosestLayoutCell(self: CellLayoutTool, location: Point3d) -> int """
        pass

    def GetLayoutCellCentroid(self, cellId):
        """ GetLayoutCellCentroid(self: CellLayoutTool, cellId: int) -> Matrix3d """
        pass

    def GetLayoutCellProfile(self, cellId, toWcs):
        """ GetLayoutCellProfile(self: CellLayoutTool, cellId: int) -> (Profile, Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    LayoutCellIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCellIds(self: CellLayoutTool) -> IntegerCollection

"""



class DictionaryRecord(DBObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    AlternateName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlternateName(self: DictionaryRecord) -> str

Set: AlternateName(self: DictionaryRecord) = value
"""

    AutomaticallyBoundSpaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticallyBoundSpaces(self: DictionaryRecord) -> AutomaticSpaceBoundary

Set: AutomaticallyBoundSpaces(self: DictionaryRecord) = value
"""

    Classifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Classifications(self: DictionaryRecord) -> ClassificationCollection

"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLocked(self: DictionaryRecord) -> bool

Set: IsLocked(self: DictionaryRecord) = value
"""

    Keynote = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keynote(self: DictionaryRecord) -> str

Set: Keynote(self: DictionaryRecord) = value
"""

    KeynoteValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeynoteValue(self: DictionaryRecord) -> str

"""

    LocalizedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalizedName(self: DictionaryRecord) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DictionaryRecord) -> str

"""

    Translator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Translator(self: DictionaryRecord) -> DictionaryRecordNameTranslator

Set: Translator(self: DictionaryRecord) = value
"""



class Classification(DictionaryRecord):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    NameAndDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameAndDescription(self: Classification) -> str

"""

    OwningSystemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OwningSystemId(self: Classification) -> ObjectId

"""

    OwningSystemName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OwningSystemName(self: Classification) -> str

"""



class ClassificationCollection(ImpObject):
    """ ClassificationCollection() """
    def Add(self, item):
        """ Add(self: ClassificationCollection, item: ObjectId) -> int """
        pass

    @staticmethod
    def AreDifferent(a, b):
        """ AreDifferent(a: ClassificationCollection, b: ClassificationCollection) -> bool """
        pass

    def Clear(self):
        """ Clear(self: ClassificationCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: ClassificationCollection, item: ObjectId) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: ClassificationCollection, array: Array[ObjectId], start: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ClassificationCollection) -> IEnumerator """
        pass

    def GetIdForDefinition(self, idOwningSystemDefinition):
        """ GetIdForDefinition(self: ClassificationCollection, idOwningSystemDefinition: ObjectId) -> ObjectId """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: ClassificationCollection, item: ObjectId) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: ClassificationCollection, index: int, item: ObjectId) """
        pass

    def Remove(self, item):
        """ Remove(self: ClassificationCollection, item: ObjectId) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ClassificationCollection, index: int) """
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    AllowDuplicateDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowDuplicateDefinitions(self: ClassificationCollection) -> bool

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ClassificationCollection) -> int

"""



class ClassificationDefinition(DictionaryRecord):
    """ ClassificationDefinition() """
    def AppliesTo(self, className):
        """ AppliesTo(self: ClassificationDefinition, className: str) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def FilterEntitySet(entityIds, classificationIds, runToCompletion):
        """ FilterEntitySet(classificationIds: ClassificationCollection, runToCompletion: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetClassification(*__args):
        """
        GetClassification(self: ClassificationDefinition, classificationName: str) -> ObjectId
        GetClassification(entity: Entity, classificationDefinitionId: ObjectId) -> ObjectId
        GetClassification(dictionaryRecord: DictionaryRecord, classificationDefinitionId: ObjectId) -> ObjectId
        """
        pass

    @staticmethod
    def IsAClassifiedAsB(a, b, exclusive):
        """ IsAClassifiedAsB(a: ClassificationCollection, b: ClassificationCollection, exclusive: bool) -> bool """
        pass

    @staticmethod
    def IsClassified(*__args):
        """
        IsClassified(entity: Entity, classificationIds: ClassificationCollection) -> bool
        IsClassified(dictionaryRecord: DictionaryRecord, classificationIds: ClassificationCollection) -> bool
        IsClassified(id: ObjectId, classificationIds: ClassificationCollection) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AppliesToAll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToAll(self: ClassificationDefinition) -> bool

Set: AppliesToAll(self: ClassificationDefinition) = value
"""

    AppliesToFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToFilter(self: ClassificationDefinition) -> StringCollection

Set: AppliesToFilter(self: ClassificationDefinition) = value
"""

    ClassificationTree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassificationTree(self: ClassificationDefinition) -> ClassificationTree

"""



class ImpTree(ImpObject):
    """ ImpTree() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AllowChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowChildren(self: ImpTree) -> bool

Set: AllowChildren(self: ImpTree) = value
"""

    AllowNullObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNullObjects(self: ImpTree) -> bool

Set: AllowNullObjects(self: ImpTree) = value
"""

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Children(self: ImpTree) -> ImpTreeCollection

"""

    IsRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRoot(self: ImpTree) -> bool

"""

    ParentTree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentTree(self: ImpTree) -> ImpTree

"""

    Root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Root(self: ImpTree) -> ImpTree

"""

    SubObjectsMightHaveReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubObjectsMightHaveReferences(self: ImpTree) -> bool

Set: SubObjectsMightHaveReferences(self: ImpTree) = value
"""



class ClassificationTree(ImpTree):
    """ ClassificationTree() """
    def AddBranch(self, *__args):
        """ AddBranch(self: ClassificationTree, branch: ClassificationTree)AddBranch(self: ClassificationTree, idParent: ObjectId, branch: ClassificationTree) """
        pass

    def AddNode(self, *__args):
        """ AddNode(self: ClassificationTree, idClassification: ObjectId)AddNode(self: ClassificationTree, name: str) -> ObjectId """
        pass

    def AddNodeToParent(self, idParent, name):
        """ AddNodeToParent(self: ClassificationTree, idParent: ObjectId, name: str) -> ObjectId """
        pass

    def Contains(self, idClassification):
        """ Contains(self: ClassificationTree, idClassification: ObjectId) -> bool """
        pass

    def CopyBranch(self, from, to):
        """ CopyBranch(self: ClassificationTree, from: ObjectId, to: ObjectId) """
        pass

    def DeleteBranch(self, idClassification):
        """ DeleteBranch(self: ClassificationTree, idClassification: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetBranch(self, *__args):
        """
        GetBranch(self: ClassificationTree, idClassification: ObjectId) -> ClassificationTree
        GetBranch(self: ClassificationTree, name: str) -> ClassificationTree
        """
        pass

    def GetIdAt(self, index):
        """ GetIdAt(self: ClassificationTree, index: int) -> ObjectId """
        pass

    def IsInDictionary(self, *__args):
        """
        IsInDictionary(self: ClassificationTree, dbObject: DBObject) -> bool
        IsInDictionary(self: ClassificationTree, dbDictionary: DBDictionary) -> bool
        """
        pass

    def MoveBranch(self, from, to):
        """ MoveBranch(self: ClassificationTree, from: ObjectId, to: ObjectId) """
        pass

    def RemoveBranch(self, idClassification):
        """ RemoveBranch(self: ClassificationTree, idClassification: ObjectId) -> ClassificationTree """
        pass

    def RemoveFromDictionary(self):
        """ RemoveFromDictionary(self: ClassificationTree) """
        pass

    def Rename(self, idClassification, newName):
        """ Rename(self: ClassificationTree, idClassification: ObjectId, newName: str) """
        pass

    def SetClass(self, rxClass):
        """ SetClass(self: ClassificationTree, rxClass: RXClass) """
        pass

    def SynchDictionary(self):
        """ SynchDictionary(self: ClassificationTree) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ClassificationTree) -> ObjectId

Set: Id(self: ClassificationTree) = value
"""



class ClippingRectangleInfo(object):
    """ ClippingRectangleInfo(x: float, y: float, endX: float, endY: float) """
    @staticmethod # known case of __new__
    def __new__(self, x, y, endX, endY):
        """ __new__(cls: type, x: float, y: float, endX: float, endY: float) """
        pass

    ClipEndX = None
    ClipEndY = None
    ClipX = None
    ClipY = None


class ClipVolume(LayoutTool):
    """ ClipVolume() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetBody(self, id):
        """ GetBody(self: ClipVolume, id: ObjectId) -> Body """
        pass

    def Reverse(self):
        """ Reverse(self: ClipVolume) """
        pass

    def SetVertices(self, points, sectionPlane):
        """ SetVertices(self: ClipVolume, points: Point3dCollection, sectionPlane: Plane) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AngleA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleA(self: ClipVolume) -> float

Set: AngleA(self: ClipVolume) = value
"""

    AngleB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleB(self: ClipVolume) -> float

Set: AngleB(self: ClipVolume) = value
"""

    EcsVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EcsVertices(self: ClipVolume) -> Point2dCollection

Set: EcsVertices(self: ClipVolume) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: ClipVolume) -> float

Set: Height(self: ClipVolume) = value
"""

    IncludedEntities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncludedEntities(self: ClipVolume) -> ObjectIdCollection

Set: IncludedEntities(self: ClipVolume) = value
"""

    LengthA = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthA(self: ClipVolume) -> float

Set: LengthA(self: ClipVolume) = value
"""

    LengthB = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthB(self: ClipVolume) -> float

Set: LengthB(self: ClipVolume) = value
"""

    LowerExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerExtension(self: ClipVolume) -> float

Set: LowerExtension(self: ClipVolume) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: ClipVolume) -> str

Set: Name(self: ClipVolume) = value
"""

    Subdivisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Subdivisions(self: ClipVolume) -> DoubleCollection

Set: Subdivisions(self: ClipVolume) = value
"""

    UseModelExtentsForHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseModelExtentsForHeight(self: ClipVolume) -> bool

Set: UseModelExtentsForHeight(self: ClipVolume) = value
"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: ClipVolume) -> Point3dCollection

"""

    ViewSetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewSetId(self: ClipVolume) -> ObjectId

Set: ViewSetId(self: ClipVolume) = value
"""



class ClipVolumeResult(Geo):
    """ ClipVolumeResult() """
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

    ClipVolumeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClipVolumeId(self: ClipVolumeResult) -> ObjectId

Set: ClipVolumeId(self: ClipVolumeResult) = value
"""



class CommandStatus(Enum):
    """ enum CommandStatus, values: CommandAllowedAlways (0), CommandAllowedOnlyOnPickFirstSet (2), CommandNotAllowed (1) """
    CommandAllowedAlways = None
    CommandAllowedOnlyOnPickFirstSet = None
    CommandNotAllowed = None
    value__ = None


class ComponentType(Enum):
    """ enum ComponentType, values: DefiningLine (0), Erased (2), Hidden (1), InnerShrinkwrap (14), OuterShrinkwrap (13), SubDivision1 (3), SubDivision10 (12), SubDivision2 (4), SubDivision3 (5), SubDivision4 (6), SubDivision5 (7), SubDivision6 (8), SubDivision7 (9), SubDivision8 (10), SubDivision9 (11), UserDefined (15) """
    DefiningLine = None
    Erased = None
    Hidden = None
    InnerShrinkwrap = None
    OuterShrinkwrap = None
    SubDivision1 = None
    SubDivision10 = None
    SubDivision2 = None
    SubDivision3 = None
    SubDivision4 = None
    SubDivision5 = None
    SubDivision6 = None
    SubDivision7 = None
    SubDivision8 = None
    SubDivision9 = None
    UserDefined = None
    value__ = None


class ConnectionComponent(ImpObject):
    # no doc
    def ConnectsWith(self, component):
        """ ConnectsWith(self: ConnectionComponent, component: ConnectionComponent) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    BoundBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundBox(self: ConnectionComponent) -> BoundBox3d

"""

    MaxSimultaneousConnections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxSimultaneousConnections(self: ConnectionComponent) -> int

"""



class ConstraintUtility(object):
    """ ConstraintUtility() """
    @staticmethod
    def AddConstraintGeometry(subentityPath):
        """ AddConstraintGeometry(subentityPath: FullSubentityPath) -> ConstrainedGeometry """
        pass

    @staticmethod
    def AddDistanceConstraint(*__args):
        """ AddDistanceConstraint(subentity1: FullSubentityPath, subentity2: FullSubentityPath, valueDependencyId: ObjectId)AddDistanceConstraint(subentity: FullSubentityPath, valueDependencyId: ObjectId)AddDistanceConstraint(entity: Entity, subEntityId1: SubentityId, subEntityId2: SubentityId, valueDependencyId: ObjectId)AddDistanceConstraint(entity: Entity, subEntityId: SubentityId, valueDependencyId: ObjectId) """
        pass

    @staticmethod
    def AddFixConstraintOnSubent(path, newlyAddedConstraintGeometry):
        """ AddFixConstraintOnSubent(path: FullSubentityPath) -> (Array[GeometricalConstraint], Array[ConstrainedGeometry]) """
        pass

    @staticmethod
    def AddGeomConstraintToSubents(entity, *__args):
        """ AddGeomConstraintToSubents(entity: Entity, subEntityId: SubentityId, constraintType: ConstraintType, setToImplied: bool)AddGeomConstraintToSubents(entity: Entity, subEntityId1: SubentityId, subEntityId2: SubentityId, constraintType: ConstraintType, setToImplied: bool) """
        pass

    @staticmethod
    def AddInternalConstraint(entity, subEntityId):
        """ AddInternalConstraint(entity: Entity, subEntityId: SubentityId) """
        pass

    @staticmethod
    def AutoCoincidentConstraint(fullSubentityPaths, newlyAddedGeometries):
        """ AutoCoincidentConstraint(fullSubentityPaths: Array[FullSubentityPath]) -> (Array[GeometricalConstraint], Array[ConstrainedGeometry]) """
        pass

    @staticmethod
    def CreateAllEdgeVerticesSubentIds(entity):
        """ CreateAllEdgeVerticesSubentIds(entity: Entity) -> Array[SubentityId] """
        pass

    @staticmethod
    def CreateEdgeVertexSubentId(edgeSubentityId, vertexType):
        """ CreateEdgeVertexSubentId(edgeSubentityId: SubentityId, vertexType: EdgeVertexType) -> SubentityId """
        pass

    @staticmethod
    def DeleteConstraint(constraint):
        """ DeleteConstraint(constraint: GeometricalConstraint) """
        pass

    @staticmethod
    def DeleteGeometryDependencyOnSubentity(entity, subEntityId):
        """ DeleteGeometryDependencyOnSubentity(entity: Entity, subEntityId: SubentityId) """
        pass

    @staticmethod
    def DeleteGeometryNodeInConstraintGroup(*__args):
        """ DeleteGeometryNodeInConstraintGroup(ids: ObjectIdCollection)DeleteGeometryNodeInConstraintGroup(geometryDependencyId: ObjectId)DeleteGeometryNodeInConstraintGroup(constrainedGeometry: ConstrainedGeometry)DeleteGeometryNodeInConstraintGroup(constrainedGeometries: Array[ConstrainedGeometry]) """
        pass

    @staticmethod
    def Get2dConstraintsOnConstrainedGeometry(constraintGeometry, constraints, includeExplicitConstraints):
        """ Get2dConstraintsOnConstrainedGeometry(constraintGeometry: ConstrainedGeometry, includeExplicitConstraints: bool) -> (bool, Array[GeometricalConstraint]) """
        pass

    @staticmethod
    def Get2dConstraintsOnImplicitPoint(implicitPoint, constraints, includeExplicitConstraints):
        """ Get2dConstraintsOnImplicitPoint(implicitPoint: ConstrainedImplicitPoint, includeExplicitConstraints: bool) -> (bool, Array[GeometricalConstraint]) """
        pass

    @staticmethod
    def Get2dConstraintsOnImplicitPoints(points, constraints, includeExplicitConstraints):
        """ Get2dConstraintsOnImplicitPoints(points: Array[ConstrainedImplicitPoint], includeExplicitConstraints: bool) -> (bool, Array[GeometricalConstraint]) """
        pass

    @staticmethod
    def Get2dConstraintsOnObject(entityId, constraints, includeExplicitConstraints=None):
        """
        Get2dConstraintsOnObject(entityId: ObjectId, includeExplicitConstraints: bool) -> (bool, Array[GeometricalConstraint])
        Get2dConstraintsOnObject(entityId: ObjectId) -> (bool, Array[GeometricalConstraint])
        """
        pass

    @staticmethod
    def Get2dConstraintsOnSubent(subentityPath, constraints, includeExplicitConstraints):
        """ Get2dConstraintsOnSubent(subentityPath: FullSubentityPath, includeExplicitConstraints: bool) -> (bool, Array[GeometricalConstraint]) """
        pass

    @staticmethod
    def GetAcDbAssocValueDependencyIds(entity):
        """ GetAcDbAssocValueDependencyIds(entity: Entity) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetAllConstraintedGeometryOnEntity(entity, geometries):
        """ GetAllConstraintedGeometryOnEntity(entity: Entity) -> (bool, Array[ConstrainedGeometry]) """
        pass

    @staticmethod
    def GetAllImplicitPointsOnObject(entity, implicitPoints):
        """ GetAllImplicitPointsOnObject(entity: Entity) -> (bool, Array[ConstrainedImplicitPoint]) """
        pass

    @staticmethod
    def GetAllStartEndImplicitPointsOnObject(entity, implicitPoints):
        """ GetAllStartEndImplicitPointsOnObject(entity: Entity) -> (bool, Array[ConstrainedImplicitPoint]) """
        pass

    @staticmethod
    def GetAllSubEntitiesInEntity(entityId):
        """ GetAllSubEntitiesInEntity(entityId: ObjectId) -> Array[SubentityId] """
        pass

    @staticmethod
    def GetAssocPersSubentityIdPE(object):
        """ GetAssocPersSubentityIdPE(object: RXObject) -> AssocPersSubentityIdPE """
        pass

    @staticmethod
    def GetClosestEdgeSubentity(entity, fullPathObjectIds, inputPoint, subentityType):
        """ GetClosestEdgeSubentity(entity: Entity, fullPathObjectIds: ObjectIdCollection, inputPoint: Point3d, subentityType: SubentityType) -> SubentityId """
        pass

    @staticmethod
    def GetClosetVertexSubentityId(entity, objectIds, pickPoint, edgeSubentityId, closestVertexSubentityId):
        """ GetClosetVertexSubentityId(entity: Entity, objectIds: ObjectIdCollection, pickPoint: Point3d, edgeSubentityId: SubentityId) -> (bool, SubentityId) """
        pass

    @staticmethod
    def GetConstraintedGeometryOnSubent(subentityPath):
        """ GetConstraintedGeometryOnSubent(subentityPath: FullSubentityPath) -> ConstrainedGeometry """
        pass

    @staticmethod
    def GetCurrentSpaceNetwork(createIfNotExist):
        """ GetCurrentSpaceNetwork(createIfNotExist: bool) -> ObjectId """
        pass

    @staticmethod
    def GetEdgeBasedFullSubentityPath(path):
        """ GetEdgeBasedFullSubentityPath(path: FullSubentityPath) -> FullSubentityPath """
        pass

    @staticmethod
    def GetEdgeBasedSubentity(subEntityId):
        """ GetEdgeBasedSubentity(subEntityId: SubentityId) -> SubentityId """
        pass

    @staticmethod
    def GetEdgeSubentIdFromEdgeVertexSubentId(vertexSubentity):
        """ GetEdgeSubentIdFromEdgeVertexSubentId(vertexSubentity: SubentityId) -> SubentityId """
        pass

    @staticmethod
    def GetEdgeVertexSubentities(entity, edgeSubentityId, startVertexSubentityId, endVertexSubentityId, middleSubentityId=None, centerSubentityId=None):
        """
        GetEdgeVertexSubentities(entity: Entity, edgeSubentityId: SubentityId) -> (SubentityId, SubentityId)
        GetEdgeVertexSubentities(entity: Entity, edgeSubentityId: SubentityId) -> (SubentityId, SubentityId, SubentityId)
        GetEdgeVertexSubentities(entity: Entity, edgeSubentityId: SubentityId) -> (SubentityId, SubentityId, SubentityId, SubentityId)
        """
        pass

    @staticmethod
    def GetEdgeVertexSubentType(vertexSubentityId):
        """ GetEdgeVertexSubentType(vertexSubentityId: SubentityId) -> EdgeVertexType """
        pass

    @staticmethod
    def GetGeometryDependencyIdsOnEntity(entity):
        """ GetGeometryDependencyIdsOnEntity(entity: Entity) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetSpaceModelConstraintGroup(database, createIfDoesNotExist, plane):
        """ GetSpaceModelConstraintGroup(database: Database, createIfDoesNotExist: bool, plane: Plane) -> ObjectId """
        pass

    @staticmethod
    def GetSubentGeomDependency(entity, subEntityId):
        """ GetSubentGeomDependency(entity: Entity, subEntityId: SubentityId) -> ObjectId """
        pass

    @staticmethod
    def GetSubentGeometryXform(objectIds):
        """ GetSubentGeometryXform(objectIds: ObjectIdCollection) -> Matrix3d """
        pass

    @staticmethod
    def GetValueDependencyByName(entity, valueName):
        """ GetValueDependencyByName(entity: Entity, valueName: str) -> ObjectId """
        pass

    @staticmethod
    def GetVertexSubentityFullPathOfImplicitPoint(implicitPoint):
        """ GetVertexSubentityFullPathOfImplicitPoint(implicitPoint: ConstrainedImplicitPoint) -> FullSubentityPath """
        pass

    @staticmethod
    def IsAecDbEntityConstrBarVisible(geometricalConstraint):
        """ IsAecDbEntityConstrBarVisible(geometricalConstraint: GeometricalConstraint) -> bool """
        pass

    @staticmethod
    def IsEntityHasEdgeSubent(entityId):
        """ IsEntityHasEdgeSubent(entityId: ObjectId) -> bool """
        pass

    @staticmethod
    def IsSubentityFixed(path):
        """ IsSubentityFixed(path: FullSubentityPath) -> bool """
        pass

    @staticmethod
    def IsValidSubentity(entity, subEntityId):
        """ IsValidSubentity(entity: Entity, subEntityId: SubentityId) -> bool """
        pass

    @staticmethod
    def ObjectHasConstraint(entityId):
        """ ObjectHasConstraint(entityId: ObjectId) -> bool """
        pass

    @staticmethod
    def ObjectHasFixConstraint(entityId):
        """ ObjectHasFixConstraint(entityId: ObjectId) -> bool """
        pass

    @staticmethod
    def ObjectHasGeomDependency(*__args):
        """
        ObjectHasGeomDependency(entity: Entity) -> bool
        ObjectHasGeomDependency(id: ObjectId) -> bool
        """
        pass

    @staticmethod
    def OnAcDbAssocGeometryDependencyAppended(dependencyObjectId):
        """ OnAcDbAssocGeometryDependencyAppended(dependencyObjectId: ObjectId) """
        pass

    @staticmethod
    def ProjectToXYPlanCurve(curve3d):
        """ ProjectToXYPlanCurve(curve3d: Curve3d) -> Curve3d """
        pass

    @staticmethod
    def RecordForDelayRegen(id):
        """ RecordForDelayRegen(id: ObjectId) """
        pass

    @staticmethod
    def RecordForDelayRegen2ndRound(id):
        """ RecordForDelayRegen2ndRound(id: ObjectId) """
        pass

    @staticmethod
    def RelaxConstraintEvaluation():
        """ RelaxConstraintEvaluation() """
        pass

    @staticmethod
    def RemoveEntityRedundantInternalConstraints(entity):
        """ RemoveEntityRedundantInternalConstraints(entity: Entity) """
        pass

    @staticmethod
    def RemoveGeometryConstraintsOnObjects(object):
        """ RemoveGeometryConstraintsOnObjects(object: DBObject) """
        pass

    @staticmethod
    def RestoreConstraintEvaluation():
        """ RestoreConstraintEvaluation() """
        pass

    @staticmethod
    def SetDelayUpdateSpaceEnabledForCurDwg(value):
        """ SetDelayUpdateSpaceEnabledForCurDwg(value: bool) """
        pass

    @staticmethod
    def SubentHasGeomDependency(entity, subEntityId):
        """ SubentHasGeomDependency(entity: Entity, subEntityId: SubentityId) -> bool """
        pass

    @staticmethod
    def SubentityHasConstraint(entity, subEntityId):
        """ SubentityHasConstraint(entity: Entity, subEntityId: SubentityId) -> bool """
        pass

    DraggingState = None
    EdgeVertexType = None
    HideInternalConstraint = True
    IsActionEvaluationInProgress = False
    IsConstraintEvaluationRelaxed = False
    IsDragging = False


class CurveXMeasureToType(Enum):
    """ enum CurveXMeasureToType, values: ToCenter (0), ToEndEdge (2), ToStartEdge (1) """
    ToCenter = None
    ToEndEdge = None
    ToStartEdge = None
    value__ = None


class CurveXOffsetType(Enum):
    """ enum CurveXOffsetType, values: FromEndOfCurve (1), FromMidpointOfCurve (2), FromStartOfCurve (0) """
    FromEndOfCurve = None
    FromMidpointOfCurve = None
    FromStartOfCurve = None
    value__ = None


class CurveYMeasureToType(Enum):
    """ enum CurveYMeasureToType, values: ToBackEdge (2), ToCenter (0), ToFrontEdge (1) """
    ToBackEdge = None
    ToCenter = None
    ToFrontEdge = None
    value__ = None


class CurveYOffsetType(Enum):
    """ enum CurveYOffsetType, values: FromCenterCurve (0), FromLeftEdge (1), FromRightEdge (2) """
    FromCenterCurve = None
    FromLeftEdge = None
    FromRightEdge = None
    value__ = None


class CurveZOffsetFromType(Enum):
    """ enum CurveZOffsetFromType, values: FromBottom (0), FromCenter (2), FromTop (1) """
    FromBottom = None
    FromCenter = None
    FromTop = None
    value__ = None


class CurveZOffsetToType(Enum):
    """ enum CurveZOffsetToType, values: ToBottom (2), ToCenter (1), ToTop (0) """
    ToBottom = None
    ToCenter = None
    ToTop = None
    value__ = None


class DatabaseData(RXObject):
    """ DatabaseData() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: DatabaseData) -> Database

"""

    DrawingInitializedAndPromoted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawingInitializedAndPromoted(self: DatabaseData) -> bool

Set: DrawingInitializedAndPromoted(self: DatabaseData) = value
"""



class DatabaseDataAecBase(DatabaseData):
    """ DatabaseDataAecBase() """
    def AddNestedWblockCloneDictionary(self, mainLevelDictionary, destinationDictionary):
        """ AddNestedWblockCloneDictionary(self: DatabaseDataAecBase, mainLevelDictionary: str, destinationDictionary: DBDictionary) """
        pass

    def AddToEndDeepCloneMvBlockProcessingArray(self, idMvBlockReference):
        """ AddToEndDeepCloneMvBlockProcessingArray(self: DatabaseDataAecBase, idMvBlockReference: ObjectId) """
        pass

    def AddToEndDeepCloneUpdateViewBlockArray(self, idMvBlockReference):
        """ AddToEndDeepCloneUpdateViewBlockArray(self: DatabaseDataAecBase, idMvBlockReference: ObjectId) """
        pass

    def AppendCopiedObject(self, sourceId, destinationId):
        """ AppendCopiedObject(self: DatabaseDataAecBase, sourceId: ObjectId, destinationId: ObjectId) """
        pass

    def AppendPreKyotoSectionElevationLinesRequiringUpdate(self, id):
        """ AppendPreKyotoSectionElevationLinesRequiringUpdate(self: DatabaseDataAecBase, id: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def DoDictionaryAuditHack(self, info):
        """ DoDictionaryAuditHack(self: DatabaseDataAecBase, info: AuditInfo) """
        pass

    def GetNestedWblockCloneDictionary(self, mainLevelDictionary):
        """ GetNestedWblockCloneDictionary(self: DatabaseDataAecBase, mainLevelDictionary: str) -> DBDictionary """
        pass

    def LayoutCopyDoPostPurge(self):
        """ LayoutCopyDoPostPurge(self: DatabaseDataAecBase) """
        pass

    def NotifySpatialTreeMessageObject(self):
        """ NotifySpatialTreeMessageObject(self: DatabaseDataAecBase) """
        pass

    def PopAnnotationScaleFromStream(self):
        """ PopAnnotationScaleFromStream(self: DatabaseDataAecBase) """
        pass

    def RemoveAllKyotoSectionElevationLinesRequiringUpdate(self):
        """ RemoveAllKyotoSectionElevationLinesRequiringUpdate(self: DatabaseDataAecBase) """
        pass

    def RemoveFromKyotoSectionElevationLinesRequiringUpdate(self, id):
        """ RemoveFromKyotoSectionElevationLinesRequiringUpdate(self: DatabaseDataAecBase, id: ObjectId) """
        pass

    def RemoveNestedWblockCloneDictionary(self, mainLevelDictionary):
        """ RemoveNestedWblockCloneDictionary(self: DatabaseDataAecBase, mainLevelDictionary: str) """
        pass

    def ResetAuditFlags(self):
        """ ResetAuditFlags(self: DatabaseDataAecBase) """
        pass

    def ResetEndDeepCloneMvBlockProcessingArray(self):
        """ ResetEndDeepCloneMvBlockProcessingArray(self: DatabaseDataAecBase) """
        pass

    def ResetEndDeepCloneUpdateViewBlockArray(self):
        """ ResetEndDeepCloneUpdateViewBlockArray(self: DatabaseDataAecBase) """
        pass

    def ResetPostProcessDictionaryMergeInfo(self):
        """ ResetPostProcessDictionaryMergeInfo(self: DatabaseDataAecBase) """
        pass

    def SetGsMarkerComponentSelectionActive(self, componentSelectionActive):
        """ SetGsMarkerComponentSelectionActive(self: DatabaseDataAecBase, componentSelectionActive: bool) """
        pass

    def SetGsMarkerHighlightingEnabled(self, enableHighlighting):
        """ SetGsMarkerHighlightingEnabled(self: DatabaseDataAecBase, enableHighlighting: bool) """
        pass

    def SetGsMarkerUnhighlightingEnabled(self, enableUnhighlighting):
        """ SetGsMarkerUnhighlightingEnabled(self: DatabaseDataAecBase, enableUnhighlighting: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CachedLayerZeroId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CachedLayerZeroId(self: DatabaseDataAecBase) -> ObjectId

"""

    CachedVariableId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CachedVariableId(self: DatabaseDataAecBase) -> ObjectId

Set: CachedVariableId(self: DatabaseDataAecBase) = value
"""

    CloneToSameDatabaseActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloneToSameDatabaseActive(self: DatabaseDataAecBase) -> bool

"""

    CloningMixedVersionOfObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CloningMixedVersionOfObjects(self: DatabaseDataAecBase) -> bool

"""

    DeepClonedSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeepClonedSet(self: DatabaseDataAecBase) -> ObjectIdCollection

"""

    DeepCloneIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeepCloneIsActive(self: DatabaseDataAecBase) -> bool

"""

    DelaySpaceUpdateEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DelaySpaceUpdateEnabled(self: DatabaseDataAecBase) -> bool

Set: DelaySpaceUpdateEnabled(self: DatabaseDataAecBase) = value
"""

    DetectedMunichStairDisplayProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DetectedMunichStairDisplayProperties(self: DatabaseDataAecBase) -> int

Set: DetectedMunichStairDisplayProperties(self: DatabaseDataAecBase) = value
"""

    DidDictionaryAuditPass1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DidDictionaryAuditPass1(self: DatabaseDataAecBase) -> bool

"""

    DidDictionaryAuditPass2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DidDictionaryAuditPass2(self: DatabaseDataAecBase) -> bool

"""

    DisableObjectUpdateDuringModify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisableObjectUpdateDuringModify(self: DatabaseDataAecBase) -> bool

Set: DisableObjectUpdateDuringModify(self: DatabaseDataAecBase) = value
"""

    DisplayRepresentationManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationManager(self: DatabaseDataAecBase) -> DisplayRepresentationManager

"""

    DwgInFieldsTriggered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwgInFieldsTriggered(self: DatabaseDataAecBase) -> bool

"""

    DwgReadIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwgReadIsActive(self: DatabaseDataAecBase) -> bool

"""

    DwgSaveIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwgSaveIsActive(self: DatabaseDataAecBase) -> bool

"""

    DxfInFieldsTriggered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DxfInFieldsTriggered(self: DatabaseDataAecBase) -> bool

"""

    DxfInIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DxfInIsActive(self: DatabaseDataAecBase) -> bool

"""

    DxfOutIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DxfOutIsActive(self: DatabaseDataAecBase) -> bool

"""

    FastWblockIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FastWblockIsActive(self: DatabaseDataAecBase) -> bool

"""

    HidingObjectsIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HidingObjectsIsActive(self: DatabaseDataAecBase) -> bool

Set: HidingObjectsIsActive(self: DatabaseDataAecBase) = value
"""

    InitDwgCalled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitDwgCalled(self: DatabaseDataAecBase) -> bool

"""

    InplaceEditorMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InplaceEditorMap(self: DatabaseDataAecBase) -> InplaceEditorMap

"""

    InsertedBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertedBlockName(self: DatabaseDataAecBase) -> str

Set: InsertedBlockName(self: DatabaseDataAecBase) = value
"""

    InsertIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertIsActive(self: DatabaseDataAecBase) -> bool

"""

    IsGsMarkerComponentSelectionActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGsMarkerComponentSelectionActive(self: DatabaseDataAecBase) -> bool

"""

    IsGsMarkerHighlightingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGsMarkerHighlightingEnabled(self: DatabaseDataAecBase) -> bool

"""

    IsGsMarkerUnhighlightingEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGsMarkerUnhighlightingEnabled(self: DatabaseDataAecBase) -> bool

"""

    LastXrefSubcommandActivity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastXrefSubcommandActivity(self: DatabaseDataAecBase) -> AecXReferenceSubcommandActivities

Set: LastXrefSubcommandActivity(self: DatabaseDataAecBase) = value
"""

    LayoutCopyHandPurgeDictionaryIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCopyHandPurgeDictionaryIds(self: DatabaseDataAecBase) -> ObjectIdCollection

"""

    LayoutCopyIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCopyIsActive(self: DatabaseDataAecBase) -> bool

"""

    LongTransactionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongTransactionSet(self: DatabaseDataAecBase) -> ObjectIdCollection

"""

    ObjectRelationGraph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectRelationGraph(self: DatabaseDataAecBase) -> DBObjectRelationshipManager

"""

    PartialOpenVetoed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartialOpenVetoed(self: DatabaseDataAecBase) -> bool

"""

    PostProcessDictionaryMergeInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PostProcessDictionaryMergeInfo(self: DatabaseDataAecBase) -> DBObjectCollection

"""

    PreKyotoSectionElevationLinesRequiringUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreKyotoSectionElevationLinesRequiringUpdate(self: DatabaseDataAecBase) -> ObjectIdCollection

"""

    ProgressiveUpdateCondition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgressiveUpdateCondition(self: DatabaseDataAecBase) -> int

Set: ProgressiveUpdateCondition(self: DatabaseDataAecBase) = value
"""

    RecoverActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecoverActive(self: DatabaseDataAecBase) -> bool

"""

    ReferenceCloseCommandActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceCloseCommandActive(self: DatabaseDataAecBase) -> bool

Set: ReferenceCloseCommandActive(self: DatabaseDataAecBase) = value
"""

    ReferenceEditCommandActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceEditCommandActive(self: DatabaseDataAecBase) -> bool

Set: ReferenceEditCommandActive(self: DatabaseDataAecBase) = value
"""

    ReferenceEditPostUpdateEcsSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferenceEditPostUpdateEcsSet(self: DatabaseDataAecBase) -> ObjectIdCollection

"""

    RestoreInsUnitsOnBTRAfterInsert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RestoreInsUnitsOnBTRAfterInsert(self: DatabaseDataAecBase) -> bool

Set: RestoreInsUnitsOnBTRAfterInsert(self: DatabaseDataAecBase) = value
"""

    StyleManagerCloningActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleManagerCloningActive(self: DatabaseDataAecBase) -> bool

Set: StyleManagerCloningActive(self: DatabaseDataAecBase) = value
"""

    UnhidingObjectsIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnhidingObjectsIsActive(self: DatabaseDataAecBase) -> bool

Set: UnhidingObjectsIsActive(self: DatabaseDataAecBase) = value
"""

    WblockIsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WblockIsActive(self: DatabaseDataAecBase) -> bool

"""

    XreferenceIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XreferenceIds(self: DatabaseDataAecBase) -> ObjectIdCollection

"""

    XrefSubcommandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XrefSubcommandType(self: DatabaseDataAecBase) -> XReferenceSubCommandType

Set: XrefSubcommandType(self: DatabaseDataAecBase) = value
"""



class DBObjectRelationship(object):
    # no doc
    Id = None
    RelationshipType = None


class DBObjectRelationshipCollection(List[DBObjectRelationship]):
    """ DBObjectRelationshipCollection() """

class DBObjectRelationshipManager(object):
    """
    DBObjectRelationshipManager(db: Database)
    DBObjectRelationshipManager()
    """
    def ForceUpdate(self, ids=None):
        """ ForceUpdate(self: DBObjectRelationshipManager)ForceUpdate(self: DBObjectRelationshipManager, ids: ObjectIdCollection) """
        pass

    def GetAllReferences(self, object):
        """ GetAllReferences(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetAllReferencesIncludingErased(self, object):
        """ GetAllReferencesIncludingErased(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetClassReferencesToThisObject(self, object):
        """ GetClassReferencesToThisObject(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetClassReferencesToThisObjectIncludErased(self, object):
        """ GetClassReferencesToThisObjectIncludErased(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetObjectsOfType(self, type, verifyObject):
        """ GetObjectsOfType(self: DBObjectRelationshipManager, type: RXClass, verifyObject: bool) -> ObjectIdCollection """
        pass

    def GetObjectsOfTypeIncludingErased(self, type, verifyObject):
        """ GetObjectsOfTypeIncludingErased(self: DBObjectRelationshipManager, type: RXClass, verifyObject: bool) -> ObjectIdCollection """
        pass

    def GetReferencesFromThisObject(self, object):
        """ GetReferencesFromThisObject(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetReferencesFromThisObjectIncludeErased(self, object):
        """ GetReferencesFromThisObjectIncludeErased(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetReferencesToThisObject(self, object):
        """ GetReferencesToThisObject(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetReferencesToThisObjectIncludeErased(self, object):
        """ GetReferencesToThisObjectIncludeErased(self: DBObjectRelationshipManager, object: DBObject) -> DBObjectRelationshipCollection """
        pass

    def GetReferencesToThisObjectRecursive(self, object, relationshipTypeFilter, includeFilter):
        """ GetReferencesToThisObjectRecursive(self: DBObjectRelationshipManager, object: DBObject, relationshipTypeFilter: int, includeFilter: bool) -> DBObjectRelationshipCollection """
        pass

    def GetReferencesToThisObjectRecursiveIncludeErased(self, object, relationshipTypeFilter, includeFilter):
        """ GetReferencesToThisObjectRecursiveIncludeErased(self: DBObjectRelationshipManager, object: DBObject, relationshipTypeFilter: int, includeFilter: bool) -> DBObjectRelationshipCollection """
        pass

    def ObjectContainsEnhancedReferences(self, id):
        """ ObjectContainsEnhancedReferences(self: DBObjectRelationshipManager, id: ObjectId) -> bool """
        pass

    def SupressNotificationOff(self):
        """ SupressNotificationOff(self: DBObjectRelationshipManager) """
        pass

    def SupressNotificationOn(self):
        """ SupressNotificationOn(self: DBObjectRelationshipManager) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db=None):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type)
        """
        pass

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: DBObjectRelationshipManager) -> Database

"""

    IsNotificationSuppressed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNotificationSuppressed(self: DBObjectRelationshipManager) -> bool

"""

    ObjectsWithEnhancedReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectsWithEnhancedReferences(self: DBObjectRelationshipManager) -> ObjectIdCollection

"""

    ObjectsWithEnhancedReferencesIncludingErased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectsWithEnhancedReferencesIncludingErased(self: DBObjectRelationshipManager) -> ObjectIdCollection

"""



class Dictionary(RXObject):
    """ Dictionary(dictionaryName: str, recordType: RXClass, objectType: RXClass, hasStandardEntries: bool, db: Database) """
    def AddNewRecord(self, name, newRecord):
        """ AddNewRecord(self: Dictionary, name: str, newRecord: DictionaryRecord) """
        pass

    def CloneEntry(self, copyFromRecord, newName):
        """ CloneEntry(self: Dictionary, copyFromRecord: DictionaryRecord, newName: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def ExtraPurgeCheck(self, idsToPurge):
        """ ExtraPurgeCheck(self: Dictionary, idsToPurge: ObjectIdCollection) """
        pass

    def GetAlternateAt(self, name):
        """ GetAlternateAt(self: Dictionary, name: str) -> ObjectId """
        pass

    def GetAt(self, name):
        """ GetAt(self: Dictionary, name: str) -> ObjectId """
        pass

    def Has(self, name, trans):
        """ Has(self: Dictionary, name: str, trans: Transaction) -> bool """
        pass

    def NameAlternateAt(self, id):
        """ NameAlternateAt(self: Dictionary, id: ObjectId) -> str """
        pass

    def NameAt(self, id):
        """ NameAt(self: Dictionary, id: ObjectId) -> str """
        pass

    def NewEntry(self):
        """ NewEntry(self: Dictionary) -> DictionaryRecord """
        pass

    def Rename(self, oldName, newName, trans):
        """ Rename(self: Dictionary, oldName: str, newName: str, trans: Transaction) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, dictionaryName, recordType, objectType, hasStandardEntries, db):
        """
        __new__(cls: type, dictionaryName: str, recordType: RXClass, objectType: RXClass, hasStandardEntries: bool, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: Dictionary) -> Database

"""

    DictionaryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DictionaryId(self: Dictionary) -> ObjectId

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: Dictionary) -> str

"""

    HasStandardEntries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasStandardEntries(self: Dictionary) -> bool

"""

    InternalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalName(self: Dictionary) -> str

"""

    NamesInUse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamesInUse(self: Dictionary) -> StringCollection

"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectType(self: Dictionary) -> RXClass

"""

    Records = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Records(self: Dictionary) -> ObjectIdCollection

"""

    RecordType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RecordType(self: Dictionary) -> RXClass

"""



class DictionaryClassificationDefinition(Dictionary):
    """ DictionaryClassificationDefinition(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryDisplayConfiguration(Dictionary):
    """ DictionaryDisplayConfiguration(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardDisplayConfiguration(db):
        """ GetStandardDisplayConfiguration(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryDisplaySet(Dictionary):
    """ DictionaryDisplaySet(db: Database, doInitialization: bool) """
    @staticmethod
    def CheckForMatchingEntries(db, displaySetType):
        """ CheckForMatchingEntries(db: Database, displaySetType: StandardDisplaySetType) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def Exists(db):
        """ Exists(db: Database) -> bool """
        pass

    @staticmethod
    def GetStandardDisplaySetName(untranslatedName, db):
        """ GetStandardDisplaySetName(untranslatedName: str, db: Database) -> str """
        pass

    @staticmethod
    def GetStandardModelHighDetailId(db):
        """ GetStandardModelHighDetailId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardModelHighDetailName(db):
        """ GetStandardModelHighDetailName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardModelId(db):
        """ GetStandardModelId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardModelLowDetailId(db):
        """ GetStandardModelLowDetailId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardModelLowDetailName(db):
        """ GetStandardModelLowDetailName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardModelName(db):
        """ GetStandardModelName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardPlanHighDetailId(db):
        """ GetStandardPlanHighDetailId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardPlanHighDetailName(db):
        """ GetStandardPlanHighDetailName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardPlanId(db):
        """ GetStandardPlanId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardPlanLowDetailId(db):
        """ GetStandardPlanLowDetailId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardPlanLowDetailName(db):
        """ GetStandardPlanLowDetailName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardPlanName(db):
        """ GetStandardPlanName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardReflectedId(db):
        """ GetStandardReflectedId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardReflectedName(db):
        """ GetStandardReflectedName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardSectionElevId(db):
        """ GetStandardSectionElevId(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetStandardSectionElevName(db):
        """ GetStandardSectionElevName(db: Database) -> str """
        pass

    @staticmethod
    def GetStandardSet(name, db):
        """ GetStandardSet(name: str, db: Database) -> ObjectId """
        pass

    @staticmethod
    def ScanAndRemoveDuplicateStandardSets(db):
        """ ScanAndRemoveDuplicateStandardSets(db: Database) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db, doInitialization):
        """
        __new__(cls: type, db: Database, doInitialization: bool)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DictionaryName = 'AEC_DISP_REP_SETS'
    StandardModelHighDetailName = 'Model High Detail'
    StandardModelLowDetailName = 'Model Low Detail'
    StandardModelName = 'Model'
    StandardPlanHighDetailName = 'Plan High Detail'
    StandardPlanLowDetailName = 'Plan Low Detail'
    StandardPlanName = 'Plan'
    StandardReflectedName = 'Reflected'
    StandardSectionElevName = 'Section_Elev'


class DictionaryDisplayThemeStyle(Dictionary):
    """ DictionaryDisplayThemeStyle(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardStyle(db):
        """ GetStandardStyle(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryEntryInformation(object):
    # no doc
    Dictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dictionary(self: DictionaryEntryInformation) -> Dictionary

Set: Dictionary(self: DictionaryEntryInformation) = value
"""

    DictionaryEntryClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DictionaryEntryClass(self: DictionaryEntryInformation) -> RXClass

Set: DictionaryEntryClass(self: DictionaryEntryInformation) = value
"""



class DictionaryLayerKeyStyle(Dictionary):
    """ DictionaryLayerKeyStyle(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GenerateLayer(self, layerKey):
        """ GenerateLayer(self: DictionaryLayerKeyStyle, layerKey: str) -> ObjectId """
        pass

    @staticmethod
    def GetStandardStyle(db):
        """ GetStandardStyle(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryListDefinition(Dictionary):
    """ DictionaryListDefinition(database: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardDefinition(database):
        """ GetStandardDefinition(database: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, database):
        """
        __new__(cls: type, database: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryMaskBlockDefinition(Dictionary):
    """ DictionaryMaskBlockDefinition(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardDefinition(db):
        """ GetStandardDefinition(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryMassElementStyle(Dictionary):
    """ DictionaryMassElementStyle(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardStyle(db):
        """ GetStandardStyle(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryMaterialDefinition(Dictionary):
    """ DictionaryMaterialDefinition(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardDefinition(db):
        """ GetStandardDefinition(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryMultiViewBlockDefinition(Dictionary):
    """ DictionaryMultiViewBlockDefinition(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardDefinition(db):
        """ GetStandardDefinition(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryPolygonStyle(Dictionary):
    """ DictionaryPolygonStyle(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardStyle(db):
        """ GetStandardStyle(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryProfileDefinition(Dictionary):
    """ DictionaryProfileDefinition(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardDefinition(db):
        """ GetStandardDefinition(db: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class NameTranslator(DisposableWrapper):
    """ NameTranslator() """
    def Add(self, globalName, localName):
        """ Add(self: NameTranslator, globalName: str, localName: str) -> bool """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> NameTranslator """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Get(self, globalName):
        """ Get(self: NameTranslator, globalName: str) -> str """
        pass

    @staticmethod
    def IsTranslatorManaged(translator):
        """ IsTranslatorManaged(translator: NameTranslator) -> bool """
        pass

    @staticmethod
    def ManageTranslator(translator):
        """ ManageTranslator(translator: NameTranslator) -> bool """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        __new__(cls: type)
        """
        pass


class DictionaryRecordNameTranslator(NameTranslator):
    """ DictionaryRecordNameTranslator() """
    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> DictionaryRecordNameTranslator """
        pass

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


class DictionaryRecordAlternateNameTranslator(DictionaryRecordNameTranslator):
    """ DictionaryRecordAlternateNameTranslator() """
    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> DictionaryRecordAlternateNameTranslator """
        pass

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


class DictionarySection2dStyle(Dictionary):
    """ DictionarySection2dStyle(database: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardStyle(database):
        """ GetStandardStyle(database: Database) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, database):
        """
        __new__(cls: type, database: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DisplayComponent(ImpObject):
    """ DisplayComponent() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Reset(self):
        """ Reset(self: DisplayComponent) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    IsApplicable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsApplicable(self: DisplayComponent) -> bool

Set: IsApplicable(self: DisplayComponent) = value
"""

    IsInherited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInherited(self: DisplayComponent) -> bool

Set: IsInherited(self: DisplayComponent) = value
"""



class DisplayComponentEntity(DisplayComponent):
    """ DisplayComponentEntity() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetPlotStyleNameId(self):
        """ GetPlotStyleNameId(self: DisplayComponentEntity) -> ObjectId """
        pass

    def GetPlotStyleNameType(self):
        """ GetPlotStyleNameType(self: DisplayComponentEntity) -> PlotStyleNameType """
        pass

    def ResetEnt(self):
        """ ResetEnt(self: DisplayComponentEntity) """
        pass

    def SetPlotStyleName(self, type, id=None):
        """ SetPlotStyleName(self: DisplayComponentEntity, type: PlotStyleNameType, id: ObjectId)SetPlotStyleName(self: DisplayComponentEntity, type: PlotStyleNameType) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AllowByMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowByMaterial(self: DisplayComponentEntity) -> bool

Set: AllowByMaterial(self: DisplayComponentEntity) = value
"""

    ByMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ByMaterial(self: DisplayComponentEntity) -> bool

Set: ByMaterial(self: DisplayComponentEntity) = value
"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: DisplayComponentEntity) -> Color

Set: Color(self: DisplayComponentEntity) = value
"""

    ColorIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorIndex(self: DisplayComponentEntity) -> Int16

Set: ColorIndex(self: DisplayComponentEntity) = value
"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: DisplayComponentEntity) -> bool

Set: IsVisible(self: DisplayComponentEntity) = value
"""

    LayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerId(self: DisplayComponentEntity) -> ObjectId

Set: LayerId(self: DisplayComponentEntity) = value
"""

    LinetypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeId(self: DisplayComponentEntity) -> ObjectId

Set: LinetypeId(self: DisplayComponentEntity) = value
"""

    LinetypeScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeScale(self: DisplayComponentEntity) -> float

Set: LinetypeScale(self: DisplayComponentEntity) = value
"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWeight(self: DisplayComponentEntity) -> LineWeight

Set: LineWeight(self: DisplayComponentEntity) = value
"""



class DisplayComponentHatch(DisplayComponentEntity):
    """ DisplayComponentHatch() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def ResetHatch(self):
        """ ResetHatch(self: DisplayComponentHatch) """
        pass

    def SetHatchParams(self, hatch, angleOfObject, ucsXAngleOffset):
        """ SetHatchParams(self: DisplayComponentHatch, hatch: Hatch, angleOfObject: float, ucsXAngleOffset: float) """
        pass

    @staticmethod
    def SetHatchParamsToAcadSettings(hatch):
        """ SetHatchParamsToAcadSettings(hatch: Hatch) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: DisplayComponentHatch) -> float

Set: Angle(self: DisplayComponentHatch) = value
"""

    HatchType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchType(self: DisplayComponentHatch) -> HatchType

Set: HatchType(self: DisplayComponentHatch) = value
"""

    IsDoubleHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDoubleHatch(self: DisplayComponentHatch) -> bool

Set: IsDoubleHatch(self: DisplayComponentHatch) = value
"""

    PatternName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternName(self: DisplayComponentHatch) -> str

Set: PatternName(self: DisplayComponentHatch) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: DisplayComponentHatch) -> float

Set: Scale(self: DisplayComponentHatch) = value
"""

    Spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spacing(self: DisplayComponentHatch) -> float

Set: Spacing(self: DisplayComponentHatch) = value
"""

    UOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UOffset(self: DisplayComponentHatch) -> float

Set: UOffset(self: DisplayComponentHatch) = value
"""

    UseAngleOfObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseAngleOfObject(self: DisplayComponentHatch) -> bool

Set: UseAngleOfObject(self: DisplayComponentHatch) = value
"""

    VOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VOffset(self: DisplayComponentHatch) -> float

Set: VOffset(self: DisplayComponentHatch) = value
"""



class DisplayComponentPushPopData(DisposableWrapper):
    """
    DisplayComponentPushPopData(entity: DisplayComponentEntity, componentName: str)
    DisplayComponentPushPopData(entity: DisplayComponentEntity)
    DisplayComponentPushPopData()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetDisplayComponentData(self, entity, name):
        """ SetDisplayComponentData(self: DisplayComponentPushPopData, entity: DisplayComponentEntity, name: str) """
        pass

    def SetMaterialDisplayComponentData(self, entity, name):
        """ SetMaterialDisplayComponentData(self: DisplayComponentPushPopData, entity: DisplayComponentEntity, name: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, entity=None, componentName=None):
        """
        __new__(cls: type, entity: DisplayComponentEntity, componentName: str)
        __new__(cls: type, entity: DisplayComponentEntity)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayComponentEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayComponentEntity(self: DisplayComponentPushPopData) -> DisplayComponentEntity

Set: DisplayComponentEntity(self: DisplayComponentPushPopData) = value
"""

    DisplayComponentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayComponentName(self: DisplayComponentPushPopData) -> str

Set: DisplayComponentName(self: DisplayComponentPushPopData) = value
"""

    HasMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasMaterial(self: DisplayComponentPushPopData) -> bool

"""

    HasName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasName(self: DisplayComponentPushPopData) -> bool

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: DisplayComponentPushPopData) -> ObjectId

Set: MaterialId(self: DisplayComponentPushPopData) = value
"""

    MaterialInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialInformation(self: DisplayComponentPushPopData) -> DisplayMaterialInformation

Set: MaterialInformation(self: DisplayComponentPushPopData) = value
"""



class DisplayConfiguration(DictionaryRecord):
    """ DisplayConfiguration() """
    def AttachDisplayTheme(self, themeId):
        """ AttachDisplayTheme(self: DisplayConfiguration, themeId: ObjectId) """
        pass

    def DetachDisplayTheme(self):
        """ DetachDisplayTheme(self: DisplayConfiguration) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def FindViewDependentViewSet(self, direction):
        """ FindViewDependentViewSet(self: DisplayConfiguration, direction: Vector3d) -> int """
        pass

    def GetStateIcon(self, index):
        """ GetStateIcon(self: DisplayConfiguration, index: DisplayConfigurationImageIndex) -> Icon """
        pass

    def ResolveViewSet(self, viewportDirection):
        """ ResolveViewSet(self: DisplayConfiguration, viewportDirection: Vector3d) -> ViewDependentCombination """
        pass

    @staticmethod
    def VectorToViewDirectionType(direction):
        """ VectorToViewDirectionType(direction: Vector3d) -> ViewDirection """
        pass

    @staticmethod
    def ViewDirectionTypeToVector(type):
        """ ViewDirectionTypeToVector(type: ViewDirection) -> Vector3d """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CutPlaneAboveRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutPlaneAboveRange(self: DisplayConfiguration) -> float

Set: CutPlaneAboveRange(self: DisplayConfiguration) = value
"""

    CutPlaneBelowRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutPlaneBelowRange(self: DisplayConfiguration) -> float

Set: CutPlaneBelowRange(self: DisplayConfiguration) = value
"""

    CutPlaneOffsetFromWcsZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutPlaneOffsetFromWcsZero(self: DisplayConfiguration) -> float

Set: CutPlaneOffsetFromWcsZero(self: DisplayConfiguration) = value
"""

    DefaultViewDependentViewSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultViewDependentViewSet(self: DisplayConfiguration) -> ObjectId

Set: DefaultViewDependentViewSet(self: DisplayConfiguration) = value
"""

    DisplayTheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayTheme(self: DisplayConfiguration) -> ObjectId

"""

    HardViewDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardViewDirection(self: DisplayConfiguration) -> Vector3d

Set: HardViewDirection(self: DisplayConfiguration) = value
"""

    HardViewDirectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardViewDirectionType(self: DisplayConfiguration) -> ViewDirection

Set: HardViewDirectionType(self: DisplayConfiguration) = value
"""

    HardViewSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HardViewSet(self: DisplayConfiguration) -> ObjectId

Set: HardViewSet(self: DisplayConfiguration) = value
"""

    IsViewDependent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsViewDependent(self: DisplayConfiguration) -> bool

Set: IsViewDependent(self: DisplayConfiguration) = value
"""

    StateIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateIcon(self: DisplayConfiguration) -> Icon

"""

    StateImageIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateImageIndex(self: DisplayConfiguration) -> DisplayConfigurationImageIndex

"""

    UseViewportViewDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseViewportViewDirection(self: DisplayConfiguration) -> bool

Set: UseViewportViewDirection(self: DisplayConfiguration) = value
"""

    ViewDependentCombinations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewDependentCombinations(self: DisplayConfiguration) -> ViewDependentCombinationCollection

"""



class DisplayConfigurationImageIndex(Enum):
    """ enum DisplayConfigurationImageIndex, values: FirstImage (0), FixedView (2), FixedViewDefault (3), LastImage (3), MultiView (0), MultiViewDefault (1) """
    FirstImage = None
    FixedView = None
    FixedViewDefault = None
    LastImage = None
    MultiView = None
    MultiViewDefault = None
    value__ = None


class DisplayConfigurationParameter(Enum):
    """ enum DisplayConfigurationParameter, values: CutPlaneAbove (7), CutPlaneBelow (8), CutPlaneOffset (6), DefaultViewDependentSet (0), HardSet (1), HardViewDirection (4), HardViewDirectionType (5), UseViewportViewDirection (3), ViewDependentSet (2) """
    CutPlaneAbove = None
    CutPlaneBelow = None
    CutPlaneOffset = None
    DefaultViewDependentSet = None
    HardSet = None
    HardViewDirection = None
    HardViewDirectionType = None
    UseViewportViewDirection = None
    value__ = None
    ViewDependentSet = None


class DisplayMaterialInformation(DisposableWrapper):
    """
    DisplayMaterialInformation(locationId: UInt32, locationStyleId: ObjectId, componentId: UInt16, isFromObjectOverride: bool)
    DisplayMaterialInformation()
    """
    def Clone(self):
        """ Clone(self: DisplayMaterialInformation) -> object """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> DisplayMaterialInformation """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, locationId=None, locationStyleId=None, componentId=None, isFromObjectOverride=None):
        """
        __new__(cls: type, locationId: UInt32, locationStyleId: ObjectId, componentId: UInt16, isFromObjectOverride: bool)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ComponentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentId(self: DisplayMaterialInformation) -> UInt16

Set: ComponentId(self: DisplayMaterialInformation) = value
"""

    IsFromObjectOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFromObjectOverride(self: DisplayMaterialInformation) -> bool

Set: IsFromObjectOverride(self: DisplayMaterialInformation) = value
"""

    LocationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationId(self: DisplayMaterialInformation) -> UInt32

Set: LocationId(self: DisplayMaterialInformation) = value
"""

    LocationStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationStyleId(self: DisplayMaterialInformation) -> ObjectId

Set: LocationStyleId(self: DisplayMaterialInformation) = value
"""

    MaterialLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialLocation(self: DisplayMaterialInformation) -> MaterialInformationLocation

"""



class DisplayProperties(DictionaryRecord):
    """ DisplayProperties() """
    def DeprecateOverride(self, newObject, deprecatedDisplayRepId, oldDisplayRepId):
        """ DeprecateOverride(self: DisplayProperties, newObject: DBObject, deprecatedDisplayRepId: ObjectId, oldDisplayRepId: ObjectId) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetApplicableDisplayComponents(self, componentNames):
        """ GetApplicableDisplayComponents(self: DisplayProperties) -> (Array[DisplayComponent], StringCollection) """
        pass

    def GetDisplayComponents(self, componentNames):
        """ GetDisplayComponents(self: DisplayProperties) -> (Array[DisplayComponent], StringCollection) """
        pass

    @staticmethod
    def GetDisplayPropertiesFromOverride(id):
        """ GetDisplayPropertiesFromOverride(id: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetDisplayPropertiesOverrideClassType(id):
        """ GetDisplayPropertiesOverrideClassType(id: ObjectId) -> RXClass """
        pass

    @staticmethod
    def GetDisplayPropsExistsInDrawingDefaultDictionary(dispPropsClass, db):
        """ GetDisplayPropsExistsInDrawingDefaultDictionary(dispPropsClass: RXClass, db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetDisplayRepsForOverride(id):
        """ GetDisplayRepsForOverride(id: ObjectId) -> ObjectIdCollection """
        pass

    def GetDisplayRepsWhichWorksWithThisDisplayProps(self, ignoreOwnerDisplayRep):
        """ GetDisplayRepsWhichWorksWithThisDisplayProps(self: DisplayProperties, ignoreOwnerDisplayRep: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetDisplayRepsWhichWorksWithThisDisplayPropsClass(db, displayPropsClass, ignoreDerivedDispProps):
        """ GetDisplayRepsWhichWorksWithThisDisplayPropsClass(db: Database, displayPropsClass: RXClass, ignoreDerivedDispProps: bool) -> ObjectIdCollection """
        pass

    @staticmethod
    def RemoveDisplayPropsFromDrawingDefaultDictionary(objectId):
        """ RemoveDisplayPropsFromDrawingDefaultDictionary(objectId: ObjectId) -> bool """
        pass

    def SetDisplayRepDefaults(self, displayRep):
        """ SetDisplayRepDefaults(self: DisplayProperties, displayRep: DisplayRepresentation) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    IsDrawingDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDrawingDefault(self: DisplayProperties) -> bool

"""

    IsStyleOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStyleOverride(self: DisplayProperties) -> bool

"""

    OwnerObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OwnerObjectId(self: DisplayProperties) -> ObjectId

"""

    OwningDisplayRep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OwningDisplayRep(self: DisplayProperties) -> ObjectId

"""

    OwningDisplayRepClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OwningDisplayRepClass(self: DisplayProperties) -> RXClass

"""



class DisplayPropertiesMaterial(DisplayProperties):
    """ DisplayPropertiesMaterial() """
    def DisplayComponentForDisplayComponentType(self, materialDisplayComponentType):
        """ DisplayComponentForDisplayComponentType(self: DisplayPropertiesMaterial, materialDisplayComponentType: ByMaterialDisplayComponentType) -> DisplayComponentEntity """
        pass

    def DisplayComponentTypeForDisplayComponent(self, component):
        """ DisplayComponentTypeForDisplayComponent(self: DisplayPropertiesMaterial, component: DisplayComponentEntity) -> ByMaterialDisplayComponentType """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetDisplayPropertiesForMaterial(materialDisplayRepresentId, materialId):
        """ GetDisplayPropertiesForMaterial(materialDisplayRepresentId: ObjectId, materialId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def MaterialComponentType(componentName):
        """ MaterialComponentType(componentName: str) -> ByMaterialDisplayComponentType """
        pass

    @staticmethod
    def MaterialDisplayComponentName(materialDisplayComponentType):
        """ MaterialDisplayComponentName(materialDisplayComponentType: ByMaterialDisplayComponentType) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BodyProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BodyProperties(self: DisplayPropertiesMaterial) -> DisplayComponentEntity

"""

    ExcludeFrom2dSectionShrinkwrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExcludeFrom2dSectionShrinkwrap(self: DisplayPropertiesMaterial) -> bool

Set: ExcludeFrom2dSectionShrinkwrap(self: DisplayPropertiesMaterial) = value
"""

    KeepAllHiddenLinework = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeepAllHiddenLinework(self: DisplayPropertiesMaterial) -> bool

Set: KeepAllHiddenLinework(self: DisplayPropertiesMaterial) = value
"""

    LineworkProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineworkProperties(self: DisplayPropertiesMaterial) -> DisplayComponentEntity

"""

    MergeCommonMaterials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MergeCommonMaterials(self: DisplayPropertiesMaterial) -> bool

Set: MergeCommonMaterials(self: DisplayPropertiesMaterial) = value
"""

    OutsideBodyProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OutsideBodyProperties(self: DisplayPropertiesMaterial) -> DisplayComponentEntity

"""

    PlanHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanHatch(self: DisplayPropertiesMaterial) -> DisplayComponentHatch

"""

    SectionedBodyRenderingMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionedBodyRenderingMaterialId(self: DisplayPropertiesMaterial) -> ObjectId

Set: SectionedBodyRenderingMaterialId(self: DisplayPropertiesMaterial) = value
"""

    SectionedBoundaryProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionedBoundaryProperties(self: DisplayPropertiesMaterial) -> DisplayComponentEntity

"""

    SectionElevationLineworkProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionElevationLineworkProperties(self: DisplayPropertiesMaterial) -> DisplayComponentEntity

"""

    SectionHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionHatch(self: DisplayPropertiesMaterial) -> DisplayComponentHatch

"""

    SectionRenderingMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionRenderingMaterialId(self: DisplayPropertiesMaterial) -> ObjectId

Set: SectionRenderingMaterialId(self: DisplayPropertiesMaterial) = value
"""

    SurfaceHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceHatch(self: DisplayPropertiesMaterial) -> DisplayComponentHatch

"""

    SurfaceHatchLocationFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceHatchLocationFlags(self: DisplayPropertiesMaterial) -> SurfaceHatchFlags

Set: SurfaceHatchLocationFlags(self: DisplayPropertiesMaterial) = value
"""

    SurfaceRenderingMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceRenderingMaterialId(self: DisplayPropertiesMaterial) -> ObjectId

Set: SurfaceRenderingMaterialId(self: DisplayPropertiesMaterial) = value
"""

    SurfaceRenderMaterialMapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceRenderMaterialMapping(self: DisplayPropertiesMaterial) -> SurfaceMappingType

Set: SurfaceRenderMaterialMapping(self: DisplayPropertiesMaterial) = value
"""



class DisplayRepresentation(DictionaryRecord):
    """ DisplayRepresentation() """
    def CreateNewDisplayProperties(self):
        """ CreateNewDisplayProperties(self: DisplayRepresentation) -> DisplayProperties """
        pass

    def CreateRecordName(self, symbolName):
        """ CreateRecordName(self: DisplayRepresentation, symbolName: str) -> str """
        pass

    def CreateUniqueRecordName(self, db):
        """ CreateUniqueRecordName(self: DisplayRepresentation, db: Database) -> str """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def FindDisplayPropertiesOverride(self, object):
        """ FindDisplayPropertiesOverride(self: DisplayRepresentation, object: DBObject) -> ObjectId """
        pass

    def GetDisplayPropertiesId(self, *__args):
        """
        GetDisplayPropertiesId(self: DisplayRepresentation, object: DBObject) -> ObjectId
        GetDisplayPropertiesId(self: DisplayRepresentation, objects: DBObjectCollection) -> ObjectId
        """
        pass

    def GetDisplayPropertiesLocationIds(self, object):
        """ GetDisplayPropertiesLocationIds(self: DisplayRepresentation, object: DBObject) -> ObjectIdCollection """
        pass

    def GetDisplayPropertiesLocationLabels(self, object):
        """ GetDisplayPropertiesLocationLabels(self: DisplayRepresentation, object: DBObject) -> StringCollection """
        pass

    def GetGripGeometryIds(self, entity):
        """ GetGripGeometryIds(self: DisplayRepresentation, entity: Entity) -> IntegerCollection """
        pass

    def GetGripOnapModes(self, entity):
        """ GetGripOnapModes(self: DisplayRepresentation, entity: Entity) -> IntegerCollection """
        pass

    def GetGripPoints(self, entity):
        """ GetGripPoints(self: DisplayRepresentation, entity: Entity) -> Point3dCollection """
        pass

    def GetStateIcon(self, value):
        """ GetStateIcon(self: DisplayRepresentation, value: DisplayRepresentationImageIndex) -> Icon """
        pass

    def GetStretchPoints(self, entity):
        """ GetStretchPoints(self: DisplayRepresentation, entity: Entity) -> Point3dCollection """
        pass

    @staticmethod
    def IsVisible(representation, id):
        """ IsVisible(representation: RXClass, id: ObjectId) -> bool """
        pass

    def MoveGripPointsAt(self, entity, indices, offset):
        """ MoveGripPointsAt(self: DisplayRepresentation, entity: Entity, indices: IntegerCollection, offset: Vector3d) """
        pass

    def MoveStretchPointsAt(self, entity, indices, offset):
        """ MoveStretchPointsAt(self: DisplayRepresentation, entity: Entity, indices: IntegerCollection, offset: Vector3d) """
        pass

    def SetEnforcedOverridenDisplayPropertiesValues(self, properties):
        """ SetEnforcedOverridenDisplayPropertiesValues(self: DisplayRepresentation, properties: DisplayProperties) """
        pass

    def SetOverriddenDisplayPropertiesDefaults(self, properties):
        """ SetOverriddenDisplayPropertiesDefaults(self: DisplayRepresentation, properties: DisplayProperties) """
        pass

    @staticmethod
    def StandardDisplayRepresentationTypeName(type):
        """ StandardDisplayRepresentationTypeName(type: DisplayRepresentationTypeName) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BaseGsMarkerValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseGsMarkerValue(self: DisplayRepresentation) -> int

"""

    CanBeDeleted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanBeDeleted(self: DisplayRepresentation) -> bool

"""

    CurrentMaterialComponentDisplayInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentMaterialComponentDisplayInformation(self: DisplayRepresentation) -> DisplayMaterialInformation

Set: CurrentMaterialComponentDisplayInformation(self: DisplayRepresentation) = value
"""

    DefaultDisplayPropertiesId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDisplayPropertiesId(self: DisplayRepresentation) -> ObjectId

Set: DefaultDisplayPropertiesId(self: DisplayRepresentation) = value
"""

    DefaultRecordName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultRecordName(self: DisplayRepresentation) -> str

"""

    DefaultVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultVisibility(self: DisplayRepresentation) -> bool

Set: DefaultVisibility(self: DisplayRepresentation) = value
"""

    DisplayPropertiesClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayPropertiesClass(self: DisplayRepresentation) -> RXClass

"""

    DisplayRepresentationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationName(self: DisplayRepresentation) -> str

"""

    HasReliableGsMarkers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasReliableGsMarkers(self: DisplayRepresentation) -> bool

"""

    IsNewToThisDrawing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNewToThisDrawing(self: DisplayRepresentation) -> bool

"""

    IsSimilarTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSimilarTo(self: DisplayRepresentation) -> str

"""

    IsUserDisplayRepresentation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUserDisplayRepresentation(self: DisplayRepresentation) -> bool

"""

    StateIcon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateIcon(self: DisplayRepresentation) -> Icon

"""

    StateImageIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StateImageIndex(self: DisplayRepresentation) -> DisplayRepresentationImageIndex

"""

    SymbolName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolName(self: DisplayRepresentation) -> str

Set: SymbolName(self: DisplayRepresentation) = value
"""

    UseObjectSnapCache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseObjectSnapCache(self: DisplayRepresentation) -> bool

"""

    ViewTypeDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewTypeDisplayName(self: DisplayRepresentation) -> str

"""

    WorksWith = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorksWith(self: DisplayRepresentation) -> RXClass

"""



class DisplayRepresentationIdCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: DisplayRepresentationIdCollection, item: ObjectId) -> int """
        pass

    def Clear(self):
        """ Clear(self: DisplayRepresentationIdCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: DisplayRepresentationIdCollection, item: ObjectId) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: DisplayRepresentationIdCollection, array: Array[ObjectId], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DisplayRepresentationIdCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: DisplayRepresentationIdCollection, item: ObjectId) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: DisplayRepresentationIdCollection, index: int, item: ObjectId) """
        pass

    def Remove(self, item):
        """ Remove(self: DisplayRepresentationIdCollection, item: ObjectId) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: DisplayRepresentationIdCollection, index: int) """
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
    """Get: Count(self: DisplayRepresentationIdCollection) -> int

"""



class DisplayRepresentationImageIndex(Enum):
    """ enum DisplayRepresentationImageIndex, values: FirstImage (0), LastImage (2), Normal (0), UserDefined (2), WithoutProperties (1) """
    FirstImage = None
    LastImage = None
    Normal = None
    UserDefined = None
    value__ = None
    WithoutProperties = None


class DisplayRepresentationManager(object):
    """
    DisplayRepresentationManager(viewportId: ObjectId, viewDirection: Vector3d, entityDatabase: Database, contextDatabase: Database)
    DisplayRepresentationManager(viewportId: ObjectId, viewDirection: Vector3d, entityDatabase: Database, contextDatabase: Database, viewportDraw: ViewportDraw)
    DisplayRepresentationManager(db: Database)
    DisplayRepresentationManager()
    """
    def ActualDisplayRepresentationDirection(self, viewportId, viewDirection):
        """ ActualDisplayRepresentationDirection(self: DisplayRepresentationManager, viewportId: ObjectId, viewDirection: Vector3d) -> Vector3d """
        pass

    def CopyOverridenDisplayProperties(self, sourceId, userId):
        """ CopyOverridenDisplayProperties(self: DisplayRepresentationManager, sourceId: ObjectId, userId: ObjectId) -> ObjectIdCollection """
        pass

    def CreateUserDefaultDisplayProperty(self, id, name, flags=None):
        """
        CreateUserDefaultDisplayProperty(self: DisplayRepresentationManager, id: ObjectId, name: str, flags: int) -> ObjectId
        CreateUserDefaultDisplayProperty(self: DisplayRepresentationManager, id: ObjectId, name: str) -> ObjectId
        """
        pass

    def CreateUserDisplayRepresentation(self, id, name, flags=None):
        """
        CreateUserDisplayRepresentation(self: DisplayRepresentationManager, id: ObjectId, name: str, flags: int) -> ObjectId
        CreateUserDisplayRepresentation(self: DisplayRepresentationManager, id: ObjectId, name: str) -> ObjectId
        """
        pass

    def DisplayConfigurationId(self, viewportId, viewDirection):
        """ DisplayConfigurationId(self: DisplayRepresentationManager, viewportId: ObjectId, viewDirection: Vector3d) -> ObjectId """
        pass

    def DisplayRepresentationSet(self, viewportId, viewDirection):
        """ DisplayRepresentationSet(self: DisplayRepresentationManager, viewportId: ObjectId, viewDirection: Vector3d) -> ObjectId """
        pass

    def EnsureDisplayRepresentaionsHaveUniqueDictionaryNames(self):
        """ EnsureDisplayRepresentaionsHaveUniqueDictionaryNames(self: DisplayRepresentationManager) """
        pass

    @staticmethod
    def GetActiveDisplayRepresentationSets(db):
        """ GetActiveDisplayRepresentationSets(db: Database) -> ObjectIdCollection """
        pass

    def GetAllDisplayRepresentationsWorkForSpecifiedClass(self, worksWithClass):
        """ GetAllDisplayRepresentationsWorkForSpecifiedClass(self: DisplayRepresentationManager, worksWithClass: RXClass) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetConfigurationOverrideFromInsertPath(blockStack):
        """ GetConfigurationOverrideFromInsertPath(blockStack: ObjectIdCollection) -> ObjectId """
        pass

    def GetDisplayConfigurationId(self, id):
        """ GetDisplayConfigurationId(self: DisplayRepresentationManager, id: ObjectId) -> ObjectId """
        pass

    def GetDisplayRepresentationId(self, viewClass):
        """ GetDisplayRepresentationId(self: DisplayRepresentationManager, viewClass: RXClass) -> ObjectId """
        pass

    def GetDisplayRepresentationIdFromXref(self, view, db):
        """ GetDisplayRepresentationIdFromXref(self: DisplayRepresentationManager, view: DisplayRepresentation, db: Database) -> ObjectId """
        pass

    def GetDisplayRepresentationIdsFromCurrentViewport(self, classType, anchorType=None):
        """
        GetDisplayRepresentationIdsFromCurrentViewport(self: DisplayRepresentationManager, classType: RXClass) -> ObjectIdCollection
        GetDisplayRepresentationIdsFromCurrentViewport(self: DisplayRepresentationManager, classType: RXClass, anchorType: RXClass) -> ObjectIdCollection
        """
        pass

    @staticmethod
    def GetDisplayRepresentationsDictionary(db):
        """ GetDisplayRepresentationsDictionary(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetXrefInsertConfigurationOverride(reference):
        """ GetXrefInsertConfigurationOverride(reference: BlockReference) -> ObjectId """
        pass

    @staticmethod
    def GetXrefInsertOverlayDabase(blockRef):
        """ GetXrefInsertOverlayDabase(blockRef: BlockReference) -> Database """
        pass

    @staticmethod
    def IsGSViewportDraw(draw):
        """ IsGSViewportDraw(draw: ViewportDraw) -> bool """
        pass

    def PopInitialization(self):
        """ PopInitialization(self: DisplayRepresentationManager) """
        pass

    def PushInitialization(self, doInitialization=None):
        """ PushInitialization(self: DisplayRepresentationManager, doInitialization: bool)PushInitialization(self: DisplayRepresentationManager) """
        pass

    @staticmethod
    def RegisterDisplayRepresentation(viewClass, *__args):
        """ RegisterDisplayRepresentation(viewClass: RXClass, viewSetName: str)RegisterDisplayRepresentation(viewClass: RXClass)RegisterDisplayRepresentation(viewClass: RXClass, viewSetNames: StringCollection) """
        pass

    @staticmethod
    def RemoveXrefInsertConfigurationOverride(blockReference):
        """ RemoveXrefInsertConfigurationOverride(blockReference: BlockReference) """
        pass

    def SetDisplayConfigurationId(self, id, configurationId):
        """ SetDisplayConfigurationId(self: DisplayRepresentationManager, id: ObjectId, configurationId: ObjectId) """
        pass

    @staticmethod
    def SetXrefInsertConfigurationOverride(blockReference, configurationId, inverseOverlayOverride):
        """ SetXrefInsertConfigurationOverride(blockReference: BlockReference, configurationId: ObjectId, inverseOverlayOverride: bool) """
        pass

    @staticmethod
    def UnregisterDisplayRepresentation(viewClass):
        """ UnregisterDisplayRepresentation(viewClass: RXClass) """
        pass

    def UpdateMaskBlockDisplayRepresentations(self, sourceId, userId):
        """ UpdateMaskBlockDisplayRepresentations(self: DisplayRepresentationManager, sourceId: ObjectId, userId: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, viewportId: ObjectId, viewDirection: Vector3d, entityDatabase: Database, contextDatabase: Database)
        __new__(cls: type, viewportId: ObjectId, viewDirection: Vector3d, entityDatabase: Database, contextDatabase: Database, viewportDraw: ViewportDraw)
        __new__(cls: type, db: Database)
        __new__(cls: type)
        """
        pass

    DefaultDisplayConfigurationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultDisplayConfigurationId(self: DisplayRepresentationManager) -> ObjectId

Set: DefaultDisplayConfigurationId(self: DisplayRepresentationManager) = value
"""

    DisplayConfigurationIdForCurrentViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayConfigurationIdForCurrentViewport(self: DisplayRepresentationManager) -> ObjectId

"""

    DisplayRepresentaionToObjectTypeMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentaionToObjectTypeMap(self: DisplayRepresentationManager) -> RXClassToObjectIdCollection

"""

    DisplayRepresentationsDictionaryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationsDictionaryId(self: DisplayRepresentationManager) -> ObjectId

"""

    Initialization = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Initialization(self: DisplayRepresentationManager) -> bool

"""


    DisplayDxfName = False


class DisplayRepresentationSetParameter(Enum):
    """ enum DisplayRepresentationSetParameter, values: Classification (4), ClippedMaterials (1), DisplayRepresentation (0), LiveSectionClipVolumes (6), SectionBodyDisplay (3), SectionByDisplayRange (5), SurfaceHatching (2) """
    Classification = None
    ClippedMaterials = None
    DisplayRepresentation = None
    LiveSectionClipVolumes = None
    SectionBodyDisplay = None
    SectionByDisplayRange = None
    SurfaceHatching = None
    value__ = None


class DisplayRepresentationTData(RXObject):
    """ DisplayRepresentationTData() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    MaskProfilePushCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskProfilePushCount(self: DisplayRepresentationTData) -> int

Set: MaskProfilePushCount(self: DisplayRepresentationTData) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: DisplayRepresentationTData) -> DisplayProperties

Set: Properties(self: DisplayRepresentationTData) = value
"""



class DisplayRepresentationTypeName(Enum):
    """ enum DisplayRepresentationTypeName, values: Elevation (5), General (0), Model (2), ModelHighDetail (9), ModelLowDetail (8), Nominal (10), Plan (1), PlanHighDetail (7), PlanLowDetail (6), Reflected (4), Sketch (3) """
    Elevation = None
    General = None
    Model = None
    ModelHighDetail = None
    ModelLowDetail = None
    Nominal = None
    Plan = None
    PlanHighDetail = None
    PlanLowDetail = None
    Reflected = None
    Sketch = None
    value__ = None


class DisplaySet(DictionaryRecord):
    """ DisplaySet() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetCombinedDisplayRangeAndLiveSectionBody(self, configuration):
        """ GetCombinedDisplayRangeAndLiveSectionBody(self: DisplaySet, configuration: DisplayConfiguration) -> Body """
        pass

    def GetDisplayRangeSectionBody(self, configuration):
        """ GetDisplayRangeSectionBody(self: DisplaySet, configuration: DisplayConfiguration) -> Body """
        pass

    def GetStandardType(self):
        """ GetStandardType(self: DisplaySet) -> StandardDisplaySetType """
        pass

    def SetStandardType(self, type, db):
        """ SetStandardType(self: DisplaySet, type: StandardDisplaySetType, db: Database) """
        pass

    def SetTransientLiveSectionBody(self, body):
        """ SetTransientLiveSectionBody(self: DisplaySet, body: Body) """
        pass

    def UpdateMergedClassifications(self, oldSystemDefinition, oldClassId, newSystemDefinition, newClassId):
        """ UpdateMergedClassifications(self: DisplaySet, oldSystemDefinition: ObjectId, oldClassId: ObjectId, newSystemDefinition: ObjectId, newClassId: ObjectId) """
        pass

    def WorksWith(self, type):
        """ WorksWith(self: DisplaySet, type: RXClass) -> ObjectIdCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ClassificationFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassificationFilter(self: DisplaySet) -> ClassificationCollection

"""

    ClipModelGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClipModelGeometry(self: DisplaySet) -> bool

Set: ClipModelGeometry(self: DisplaySet) = value
"""

    DisableSectionedBodyDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisableSectionedBodyDisplay(self: DisplaySet) -> bool

Set: DisableSectionedBodyDisplay(self: DisplaySet) = value
"""

    DisableSurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisableSurfaceHatching(self: DisplaySet) -> bool

Set: DisableSurfaceHatching(self: DisplaySet) = value
"""

    DisplayRepresentationIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationIds(self: DisplaySet) -> DisplayRepresentationIdCollection

"""

    HasLiveClippingBody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasLiveClippingBody(self: DisplaySet) -> bool

"""

    HasTransientLiveSectionBody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasTransientLiveSectionBody(self: DisplaySet) -> bool

"""

    IsStandardSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStandardSet(self: DisplaySet) -> bool

"""

    LiveSectionBody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveSectionBody(self: DisplaySet) -> Body

"""

    LiveSectionClipVolumes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveSectionClipVolumes(self: DisplaySet) -> ObjectIdCollection

Set: LiveSectionClipVolumes(self: DisplaySet) = value
"""

    ShowClippedMaterials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowClippedMaterials(self: DisplaySet) -> bool

Set: ShowClippedMaterials(self: DisplaySet) = value
"""



class DisplayTheme(Geo):
    """ DisplayTheme() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDimensionHeight(self, style):
        """ GetDimensionHeight(self: DisplayTheme, style: DisplayThemeStyle) -> float """
        pass

    def GetDimensionRowHeight(self, style):
        """ GetDimensionRowHeight(self: DisplayTheme, style: DisplayThemeStyle) -> float """
        pass

    def GetDimensionWidth(self, style):
        """ GetDimensionWidth(self: DisplayTheme, style: DisplayThemeStyle) -> float """
        pass

    def GetExtentBoundBox(self):
        """ GetExtentBoundBox(self: DisplayTheme) -> BoundBox3d """
        pass

    def GetTransformMatrix(self):
        """ GetTransformMatrix(self: DisplayTheme) -> Matrix3d """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: DisplayTheme) -> bool

"""

    ParticipatesInDynamicUCS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParticipatesInDynamicUCS(self: DisplayTheme) -> bool

"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: DisplayTheme) -> float

Set: Scale(self: DisplayTheme) = value
"""

    SupportsVisualStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsVisualStyle(self: DisplayTheme) -> bool

"""



class DisplayThemeCellFormat(ImpObject):
    """ DisplayThemeCellFormat() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetActualTextHeight(self, text, textHeightScale):
        """ GetActualTextHeight(self: DisplayThemeCellFormat, text: str, textHeightScale: float) -> float """
        pass

    def GetCellHeight(self, text):
        """ GetCellHeight(self: DisplayThemeCellFormat, text: str) -> float """
        pass

    def GetCellHeightWithFixedWidth(self, text, fixedWidth):
        """ GetCellHeightWithFixedWidth(self: DisplayThemeCellFormat, text: str, fixedWidth: float) -> float """
        pass

    def GetCellWidth(self, text):
        """ GetCellWidth(self: DisplayThemeCellFormat, text: str) -> float """
        pass

    def GetHeight(self, text):
        """ GetHeight(self: DisplayThemeCellFormat, text: str) -> float """
        pass

    def GetRotatedTextCellWidth(self, text, fixedWidth):
        """ GetRotatedTextCellWidth(self: DisplayThemeCellFormat, text: str, fixedWidth: float) -> float """
        pass

    def GetSymbolHeight(self, count):
        """ GetSymbolHeight(self: DisplayThemeCellFormat, count: int) -> float """
        pass

    def GetSymbolWidth(self, count):
        """ GetSymbolWidth(self: DisplayThemeCellFormat, count: int) -> float """
        pass

    def GetWidth(self, text):
        """ GetWidth(self: DisplayThemeCellFormat, text: str) -> float """
        pass

    def ScaleBy(self, dScale):
        """ ScaleBy(self: DisplayThemeCellFormat, dScale: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gap(self: DisplayThemeCellFormat) -> float

Set: Gap(self: DisplayThemeCellFormat) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: DisplayThemeCellFormat) -> float

Set: Height(self: DisplayThemeCellFormat) = value
"""

    RotationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RotationType(self: DisplayThemeCellFormat) -> RotationType

Set: RotationType(self: DisplayThemeCellFormat) = value
"""

    TextStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyleId(self: DisplayThemeCellFormat) -> ObjectId

Set: TextStyleId(self: DisplayThemeCellFormat) = value
"""

    TextStyleIdString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyleIdString(self: DisplayThemeCellFormat) -> str

"""

    ThemeSymbolType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThemeSymbolType(self: DisplayThemeCellFormat) -> ThemeSymbolType

Set: ThemeSymbolType(self: DisplayThemeCellFormat) = value
"""



class DisplayThemeComponentBase(ImpObject):
    """ DisplayThemeComponentBase() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetDisplayString(self):
        """ GetDisplayString(self: DisplayThemeComponentBase) -> str """
        pass

    def SupportsEntity(self, entity):
        """ SupportsEntity(self: DisplayThemeComponentBase, entity: Entity) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayProperties(self: DisplayThemeComponentBase) -> DisplayComponentHatch

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: DisplayThemeComponentBase) -> str

Set: Name(self: DisplayThemeComponentBase) = value
"""

    Rules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rules(self: DisplayThemeComponentBase) -> DisplayThemeRuleBase

Set: Rules(self: DisplayThemeComponentBase) = value
"""



class DisplayThemeComponentCollection(object):
    """ DisplayThemeComponentCollection(pOp: IDisplayThemeComponentOperation) """
    def Add(self, value):
        """ Add(self: DisplayThemeComponentCollection, value: DisplayThemeComponentBase) -> int """
        pass

    def Clear(self):
        """ Clear(self: DisplayThemeComponentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: DisplayThemeComponentCollection, value: DisplayThemeComponentBase) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: DisplayThemeComponentCollection, array: Array[DisplayThemeComponentBase], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DisplayThemeComponentCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: DisplayThemeComponentCollection, value: DisplayThemeComponentBase) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: DisplayThemeComponentCollection, index: int, value: DisplayThemeComponentBase) """
        pass

    def Remove(self, value):
        """ Remove(self: DisplayThemeComponentCollection, value: DisplayThemeComponentBase) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: DisplayThemeComponentCollection, index: int) """
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IDisplayThemeComponentOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DisplayThemeComponentCollection) -> int

"""



class DisplayThemeNextNodeOperator(Enum):
    """ enum DisplayThemeNextNodeOperator, values: NextNodeOperatorAnd (0), NextNodeOperatorOr (1) """
    NextNodeOperatorAnd = None
    NextNodeOperatorOr = None
    value__ = None


class DisplayThemeRuleBase(ImpObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetCollectProperties(self):
        """ GetCollectProperties(self: DisplayThemeRuleBase) -> StringCollection """
        pass

    def GetCollectPropertiesDefaultIndex(self):
        """ GetCollectPropertiesDefaultIndex(self: DisplayThemeRuleBase) -> int """
        pass

    def GetCollectPropertyOwners(self):
        """ GetCollectPropertyOwners(self: DisplayThemeRuleBase) -> StringCollection """
        pass

    def GetCollectPropertyOwnersDefaultIndex(self):
        """ GetCollectPropertyOwnersDefaultIndex(self: DisplayThemeRuleBase) -> int """
        pass

    def GetTrueFalseText(self, isFormatted):
        """ GetTrueFalseText(self: DisplayThemeRuleBase, isFormatted: bool) -> StringCollection """
        pass

    def SupportsEntity(self, entity):
        """ SupportsEntity(self: DisplayThemeRuleBase, entity: Entity) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    ComparisonOperator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComparisonOperator(self: DisplayThemeRuleBase) -> DisplayThemeRuleComparisonOperator

Set: ComparisonOperator(self: DisplayThemeRuleBase) = value
"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: DisplayThemeRuleBase) -> PropertyDataType

Set: DataType(self: DisplayThemeRuleBase) = value
"""

    DisplayString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayString(self: DisplayThemeRuleBase) -> str

"""

    DisplayThemeRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayThemeRules(self: DisplayThemeRuleBase) -> DisplayThemeRuleCollection

"""

    FormattedValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormattedValue(self: DisplayThemeRuleBase) -> str

"""

    NextNodeOperator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextNodeOperator(self: DisplayThemeRuleBase) -> DisplayThemeNextNodeOperator

Set: NextNodeOperator(self: DisplayThemeRuleBase) = value
"""

    Precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Precision(self: DisplayThemeRuleBase) -> int

"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyName(self: DisplayThemeRuleBase) -> str

Set: PropertyName(self: DisplayThemeRuleBase) = value
"""

    PropertyOwnerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyOwnerName(self: DisplayThemeRuleBase) -> str

Set: PropertyOwnerName(self: DisplayThemeRuleBase) = value
"""

    PropertyOwnerTypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyOwnerTypeName(self: DisplayThemeRuleBase) -> str

"""

    Units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Units(self: DisplayThemeRuleBase) -> int

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: DisplayThemeRuleBase) -> object

Set: Value(self: DisplayThemeRuleBase) = value
"""

    ValueAsString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueAsString(self: DisplayThemeRuleBase) -> str

"""



class DisplayThemeRuleCollection(object):
    """ DisplayThemeRuleCollection(pOp: IDisplayThemeRuleOperation) """
    def Add(self, value):
        """ Add(self: DisplayThemeRuleCollection, value: DisplayThemeRuleBase) -> int """
        pass

    def Clear(self):
        """ Clear(self: DisplayThemeRuleCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: DisplayThemeRuleCollection, value: DisplayThemeRuleBase) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: DisplayThemeRuleCollection, array: Array[DisplayThemeRuleBase], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: DisplayThemeRuleCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: DisplayThemeRuleCollection, value: DisplayThemeRuleBase) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: DisplayThemeRuleCollection, index: int, value: DisplayThemeRuleBase) """
        pass

    def Remove(self, value):
        """ Remove(self: DisplayThemeRuleCollection, value: DisplayThemeRuleBase) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: DisplayThemeRuleCollection, index: int) """
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IDisplayThemeRuleOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: DisplayThemeRuleCollection) -> int

"""



class DisplayThemeRuleComparisonOperator(Enum):
    """ enum DisplayThemeRuleComparisonOperator, values: RuleComparisonOperatorEqualTo (1), RuleComparisonOperatorGreaterThan (5), RuleComparisonOperatorGreaterThanEqualTo (6), RuleComparisonOperatorInRange (7), RuleComparisonOperatorIsNone (0), RuleComparisonOperatorLessThan (3), RuleComparisonOperatorLessThanEqualTo (4), RuleComparisonOperatorNotEqualTo (2) """
    RuleComparisonOperatorEqualTo = None
    RuleComparisonOperatorGreaterThan = None
    RuleComparisonOperatorGreaterThanEqualTo = None
    RuleComparisonOperatorInRange = None
    RuleComparisonOperatorIsNone = None
    RuleComparisonOperatorLessThan = None
    RuleComparisonOperatorLessThanEqualTo = None
    RuleComparisonOperatorNotEqualTo = None
    value__ = None


class DisplayThemeStyle(DictionaryRecord):
    """ DisplayThemeStyle() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayThemeDisplayPropsForEntity(self, entity, componentIndex=None):
        """
        GetDisplayThemeDisplayPropsForEntity(self: DisplayThemeStyle, entity: Entity) -> DisplayComponentHatch
        GetDisplayThemeDisplayPropsForEntity(self: DisplayThemeStyle, entity: Entity) -> (DisplayComponentHatch, int)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellFormat(self: DisplayThemeStyle) -> DisplayThemeCellFormat

"""

    DisplayThemeComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayThemeComponents(self: DisplayThemeStyle) -> DisplayThemeComponentCollection

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: DisplayThemeStyle) -> str

Set: Title(self: DisplayThemeStyle) = value
"""



class DistributionFlags(Enum):
    """ enum (flags) DistributionFlags, values: DistributeEvenlyToAll (0), DistributeToFirst (1), DistributeToLast (2), DistributeToMiddle (4), MaintainAtLeastHalfCellSize (16), NeverExceedCellSize (8) """
    DistributeEvenlyToAll = None
    DistributeToFirst = None
    DistributeToLast = None
    DistributeToMiddle = None
    MaintainAtLeastHalfCellSize = None
    NeverExceedCellSize = None
    value__ = None


class DivisionDirection(Enum):
    """ enum DivisionDirection, values: AlongXAxis (0), AlongYAxis (1) """
    AlongXAxis = None
    AlongYAxis = None
    value__ = None


class EditingConstraint(Enum):
    """ enum EditingConstraint, values: DepthFixed (2), None (0), RectangularShape (4), WidthDepthFixed (3), WidthFixed (1) """
    DepthFixed = None
    None = None
    RectangularShape = None
    value__ = None
    WidthDepthFixed = None
    WidthFixed = None


class EditingContext(Enum):
    """ enum EditingContext, values: ClosedShape (0), OpenShape (1) """
    ClosedShape = None
    OpenShape = None
    value__ = None


class EditInPlaceProfile(Geo):
    """ EditInPlaceProfile() """
    def AddEcsVertex(self, ecsVertex):
        """ AddEcsVertex(self: EditInPlaceProfile, ecsVertex: Point2d) """
        pass

    def AddVertex(self, vertex):
        """ AddVertex(self: EditInPlaceProfile, vertex: Point3d) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def RemoveEcsVertex(self, ecsVertex):
        """ RemoveEcsVertex(self: EditInPlaceProfile, ecsVertex: Point2d) """
        pass

    def RemoveVertex(self, vertex):
        """ RemoveVertex(self: EditInPlaceProfile, vertex: Point3d) """
        pass

    def SetEcsVertices(self, ecsPoints):
        """ SetEcsVertices(self: EditInPlaceProfile, ecsPoints: Point2dCollection) """
        pass

    def SetVertices(self, ecsPoints, plane):
        """ SetVertices(self: EditInPlaceProfile, ecsPoints: Point3dCollection, plane: Plane) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BaseProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseProfile(self: EditInPlaceProfile) -> Profile

Set: BaseProfile(self: EditInPlaceProfile) = value
"""

    DrawDefaultGraphics = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawDefaultGraphics(self: EditInPlaceProfile) -> bool

Set: DrawDefaultGraphics(self: EditInPlaceProfile) = value
"""

    EcsInsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EcsInsertionPoint(self: EditInPlaceProfile) -> Point2d

Set: EcsInsertionPoint(self: EditInPlaceProfile) = value
"""

    EditingConstraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditingConstraint(self: EditInPlaceProfile) -> EditingConstraint

Set: EditingConstraint(self: EditInPlaceProfile) = value
"""

    EditingContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditingContext(self: EditInPlaceProfile) -> EditingContext

Set: EditingContext(self: EditInPlaceProfile) = value
"""

    InsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPoint(self: EditInPlaceProfile) -> Point3d

Set: InsertionPoint(self: EditInPlaceProfile) = value
"""

    InvalidProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InvalidProfile(self: EditInPlaceProfile) -> Profile

Set: InvalidProfile(self: EditInPlaceProfile) = value
"""

    UseDefaultGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultGrips(self: EditInPlaceProfile) -> bool

Set: UseDefaultGrips(self: EditInPlaceProfile) = value
"""

    UseDefaultMenus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultMenus(self: EditInPlaceProfile) -> bool

Set: UseDefaultMenus(self: EditInPlaceProfile) = value
"""

    UseMoveGrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseMoveGrip(self: EditInPlaceProfile) -> bool

Set: UseMoveGrip(self: EditInPlaceProfile) = value
"""

    UsesInsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsesInsertionPoint(self: EditInPlaceProfile) -> bool

Set: UsesInsertionPoint(self: EditInPlaceProfile) = value
"""



class EditState(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def RegisterState(self, id):
        """ RegisterState(self: EditState, id: ObjectId) """
        pass

    def UnregisterState(self, id):
        """ UnregisterState(self: EditState, id: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class EditStateManager(RXObject):
    # no doc
    @staticmethod
    def CurrentState(id):
        """ CurrentState(id: ObjectId) -> EditState """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GripStatus(self, entity, status):
        """ GripStatus(self: EditStateManager, entity: Entity, status: GripStatus) """
        pass

    def UnregisterState(self, id):
        """ UnregisterState(self: EditStateManager, id: ObjectId) """
        pass

    def UnregisterStateForEntitiesInDatabase(self, database):
        """ UnregisterStateForEntitiesInDatabase(self: EditStateManager, database: Database) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Instance = None


class EntityBodyModifier(ImpObject):
    """
    EntityBodyModifier()
    EntityBodyModifier(unmanagedPointer: IntPtr, autoDelete: bool)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetBodyAsMassElement(self):
        """ GetBodyAsMassElement(self: EntityBodyModifier) -> MassElement """
        pass

    def SetBodyFromMassElement(self, massElement, wcsToEcs):
        """ SetBodyFromMassElement(self: EntityBodyModifier, massElement: MassElement, wcsToEcs: Matrix3d) """
        pass

    def TransformBy(self, matrix):
        """ TransformBy(self: EntityBodyModifier, matrix: Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedPointer=None, autoDelete=None):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: EntityBodyModifier) -> Body

Set: Body(self: EntityBodyModifier) = value
"""

    ComponentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentId(self: EntityBodyModifier) -> Int16

Set: ComponentId(self: EntityBodyModifier) = value
"""

    OperationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OperationType(self: EntityBodyModifier) -> EntityBodyModifierOperationType

Set: OperationType(self: EntityBodyModifier) = value
"""



class EntityBodyModifierOperationType(Enum):
    """ enum EntityBodyModifierOperationType, values: Additive (0), Replace (2), Subtractive (1) """
    Additive = None
    Replace = None
    Subtractive = None
    value__ = None


class EntityCollectorData(DisposableWrapper):
    """ EntityCollectorData() """
    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> EntityCollectorData """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class EntityCollectorFilter(DisposableWrapper):
    """ EntityCollectorFilter() """
    def AllowEntity(self, entity, *__args):
        """
        AllowEntity(self: EntityCollectorFilter, entity: Entity) -> (bool, EntityCollectorData)
        AllowEntity(self: EntityCollectorFilter, entity: Entity, idArrayBlockReferencePath: ObjectIdCollection) -> (bool, EntityCollectorData)
        """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> EntityCollectorFilter """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def RecurseBlock(self, blockReference, idArrayBlockReferencePath):
        """ RecurseBlock(self: EntityCollectorFilter, blockReference: BlockReference, idArrayBlockReferencePath: ObjectIdCollection) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CheckRecurseBlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CheckRecurseBlock(self: EntityCollectorFilter) -> bool

Set: CheckRecurseBlock(self: EntityCollectorFilter) = value
"""



class EntityInterference(ImpObject):
    """
    EntityInterference()
    EntityInterference(unmanagedPointer: IntPtr, autoDelete: bool)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEntityBlockRefPath(self):
        """ GetEntityBlockRefPath(self: EntityInterference) -> ObjectIdCollection """
        pass

    def SetEntityBlockRefPath(self, id, blockRefPath, pDb):
        """ SetEntityBlockRefPath(self: EntityInterference, id: ObjectId, blockRefPath: ObjectIdCollection, pDb: Database) """
        pass

    def UpdateBody(self):
        """ UpdateBody(self: EntityInterference) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedPointer=None, autoDelete=None):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BlockReferenceBroken = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockReferenceBroken(self: EntityInterference) -> bool

Set: BlockReferenceBroken(self: EntityInterference) = value
"""

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: EntityInterference) -> Body

"""

    EntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityId(self: EntityInterference) -> ObjectId

Set: EntityId(self: EntityInterference) = value
"""

    FromBlockReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FromBlockReference(self: EntityInterference) -> bool

Set: FromBlockReference(self: EntityInterference) = value
"""

    ShrinkWrapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShrinkWrapEffect(self: EntityInterference) -> EntityInterferenceShrinkWrapEffect

Set: ShrinkWrapEffect(self: EntityInterference) = value
"""



class EntityInterferenceShrinkWrapEffect(Enum):
    """ enum EntityInterferenceShrinkWrapEffect, values: Additive (1), Ignore (0), Subtractive (2) """
    Additive = None
    Ignore = None
    Subtractive = None
    value__ = None


class EntityReference(BlockReference):
    """
    EntityReference(referenceEntity: ObjectId)
    EntityReference()
    """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, referenceEntity=None):
        """
        __new__(cls: type, referenceEntity: ObjectId)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    InsertionPointOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPointOffset(self: EntityReference) -> Vector3d

Set: InsertionPointOffset(self: EntityReference) = value
"""

    InsertionPointOfReferredEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPointOfReferredEntity(self: EntityReference) -> Point3d

Set: InsertionPointOfReferredEntity(self: EntityReference) = value
"""

    ReferredEntityEcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferredEntityEcs(self: EntityReference) -> Matrix3d

"""

    ReferredEntityEcsInverse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReferredEntityEcsInverse(self: EntityReference) -> Matrix3d

"""

    UseOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseOffset(self: EntityReference) -> bool

Set: UseOffset(self: EntityReference) = value
"""



class EntitySelectedComponentInformation(RXObject):
    """
    EntitySelectedComponentInformation(displayComponentName: str, displayPropertiesId: ObjectId, displayRepresentationId: ObjectId, viewportId: ObjectId, viewportNumber: int, materialDisplayPropertiesId: ObjectId, materialDisplayRepresentationId: ObjectId, materialInformation: MaterialInformation)
    EntitySelectedComponentInformation()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, displayComponentName=None, displayPropertiesId=None, displayRepresentationId=None, viewportId=None, viewportNumber=None, materialDisplayPropertiesId=None, materialDisplayRepresentationId=None, materialInformation=None):
        """
        __new__(cls: type, displayComponentName: str, displayPropertiesId: ObjectId, displayRepresentationId: ObjectId, viewportId: ObjectId, viewportNumber: int, materialDisplayPropertiesId: ObjectId, materialDisplayRepresentationId: ObjectId, materialInformation: MaterialInformation)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ComponentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentName(self: EntitySelectedComponentInformation) -> str

"""

    CurrentByMaterialStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentByMaterialStatus(self: EntitySelectedComponentInformation) -> bool

Set: CurrentByMaterialStatus(self: EntitySelectedComponentInformation) = value
"""

    DisplayComponentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayComponentName(self: EntitySelectedComponentInformation) -> str

Set: DisplayComponentName(self: EntitySelectedComponentInformation) = value
"""

    DisplayedDrawingDefaultWarningMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayedDrawingDefaultWarningMessage(self: EntitySelectedComponentInformation) -> bool

Set: DisplayedDrawingDefaultWarningMessage(self: EntitySelectedComponentInformation) = value
"""

    DisplayedMaterialWarningMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayedMaterialWarningMessage(self: EntitySelectedComponentInformation) -> bool

Set: DisplayedMaterialWarningMessage(self: EntitySelectedComponentInformation) = value
"""

    DisplayedStyleOverrideWarningMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayedStyleOverrideWarningMessage(self: EntitySelectedComponentInformation) -> bool

Set: DisplayedStyleOverrideWarningMessage(self: EntitySelectedComponentInformation) = value
"""

    DisplayedSystemOverrideWarningMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayedSystemOverrideWarningMessage(self: EntitySelectedComponentInformation) -> bool

Set: DisplayedSystemOverrideWarningMessage(self: EntitySelectedComponentInformation) = value
"""

    DisplayProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayProperties(self: EntitySelectedComponentInformation) -> ObjectId

"""

    DisplayPropertiesId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayPropertiesId(self: EntitySelectedComponentInformation) -> ObjectId

Set: DisplayPropertiesId(self: EntitySelectedComponentInformation) = value
"""

    DisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationId(self: EntitySelectedComponentInformation) -> ObjectId

Set: DisplayRepresentationId(self: EntitySelectedComponentInformation) = value
"""

    HasMaterialInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasMaterialInformation(self: EntitySelectedComponentInformation) -> bool

Set: HasMaterialInformation(self: EntitySelectedComponentInformation) = value
"""

    MaterialDisplayPropertiesId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialDisplayPropertiesId(self: EntitySelectedComponentInformation) -> ObjectId

Set: MaterialDisplayPropertiesId(self: EntitySelectedComponentInformation) = value
"""

    MaterialDisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialDisplayRepresentationId(self: EntitySelectedComponentInformation) -> ObjectId

Set: MaterialDisplayRepresentationId(self: EntitySelectedComponentInformation) = value
"""

    MaterialInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialInformation(self: EntitySelectedComponentInformation) -> MaterialInformation

Set: MaterialInformation(self: EntitySelectedComponentInformation) = value
"""

    ViewportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportId(self: EntitySelectedComponentInformation) -> ObjectId

Set: ViewportId(self: EntitySelectedComponentInformation) = value
"""

    ViewportNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportNumber(self: EntitySelectedComponentInformation) -> int

Set: ViewportNumber(self: EntitySelectedComponentInformation) = value
"""



class ExtendedStringCollection(object):
    """ ExtendedStringCollection(pOp: IStringOperation) """
    def Add(self, value):
        """ Add(self: ExtendedStringCollection, value: str) -> int """
        pass

    def AddBatch(self, stringList):
        """ AddBatch(self: ExtendedStringCollection, stringList: StringCollection) """
        pass

    def Clear(self):
        """ Clear(self: ExtendedStringCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: ExtendedStringCollection, value: str) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: ExtendedStringCollection, array: Array[str], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ExtendedStringCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: ExtendedStringCollection, value: str) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: ExtendedStringCollection, index: int, value: str) """
        pass

    def Remove(self, value):
        """ Remove(self: ExtendedStringCollection, value: str) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ExtendedStringCollection, index: int) """
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IStringOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ExtendedStringCollection) -> int

"""



class FaceScanResults(object):
    # no doc
    ExactHit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExactHit(self: FaceScanResults) -> bool

"""

    FaceCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceCoordinateSystem(self: FaceScanResults) -> Matrix3d

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: FaceScanResults) -> ObjectId

"""

    PickedFace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickedFace(self: FaceScanResults) -> Face

"""



class GraphicsStorage(ImpObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: GraphicsStorage) -> Color

"""

    ColorIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorIndex(self: GraphicsStorage) -> int

"""

    GeometryExtents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryExtents(self: GraphicsStorage) -> Extents3d

"""

    GsMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GsMarker(self: GraphicsStorage) -> IntPtr

"""

    LayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerId(self: GraphicsStorage) -> ObjectId

"""

    LinetypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeId(self: GraphicsStorage) -> ObjectId

"""

    LineTypeScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineTypeScale(self: GraphicsStorage) -> float

"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWeight(self: GraphicsStorage) -> LineWeight

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: GraphicsStorage) -> ObjectId

"""

    PlotStyleNameId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotStyleNameId(self: GraphicsStorage) -> ObjectId

"""

    PlotStyleNameType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotStyleNameType(self: GraphicsStorage) -> PlotStyleNameType

"""



class GraphicsStorageArc(GraphicsStorage):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Arc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc(self: GraphicsStorageArc) -> CircularArc3d

"""



class GraphicsStorageBody(GraphicsStorage):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: GraphicsStorageBody) -> Body

"""

    DiscardedEdgeFaceMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DiscardedEdgeFaceMask(self: GraphicsStorageBody) -> UInt16

"""



class GraphicsStorageFace(GraphicsStorage):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    EdgeVisibility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeVisibility(self: GraphicsStorageFace) -> Array[GraphicsStorageVisibility]

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: GraphicsStorageFace) -> Point3dCollection

"""



class GraphicsStorageHatch(GraphicsStorage):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    HatchType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchType(self: GraphicsStorageHatch) -> GraphicsStorageHatchType

"""

    Vectors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vectors(self: GraphicsStorageHatch) -> Array[LineSegment3d]

"""



class GraphicsStorageHatchType(Enum):
    """ enum GraphicsStorageHatchType, values: None (0), SectionHatch (2), SurfaceHatch (1) """
    None = None
    SectionHatch = None
    SurfaceHatch = None
    value__ = None


class GraphicsStoragePolyline(GraphicsStorage):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: GraphicsStoragePolyline) -> Point3dCollection

"""



class GraphicsStorageShell(GraphicsStorage):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    EdgeData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeData(self: GraphicsStorageShell) -> EdgeData

"""

    FaceData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceData(self: GraphicsStorageShell) -> FaceData

"""

    FaceList = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceList(self: GraphicsStorageShell) -> Array[int]

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: GraphicsStorageShell) -> Point3dCollection

"""



class GraphicsStorageVisibility(Enum):
    """ enum GraphicsStorageVisibility, values: Invisible (0), Silhouette (2), Visible (1) """
    Invisible = None
    Silhouette = None
    value__ = None
    Visible = None


class GraphicsSystemEntityDrawData(DisposableWrapper):
    """ GraphicsSystemEntityDrawData() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def FreeDrawData(self):
        """ FreeDrawData(self: GraphicsSystemEntityDrawData) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DbObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DbObject(self: GraphicsSystemEntityDrawData) -> DBObject

Set: DbObject(self: GraphicsSystemEntityDrawData) = value
"""

    GsMarkerInformationTree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GsMarkerInformationTree(self: GraphicsSystemEntityDrawData) -> GsMarkerInformationTree

Set: GsMarkerInformationTree(self: GraphicsSystemEntityDrawData) = value
"""

    IsBusy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBusy(self: GraphicsSystemEntityDrawData) -> bool

Set: IsBusy(self: GraphicsSystemEntityDrawData) = value
"""



class GridAssembly(CellLayoutTool):
    """ GridAssembly() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAnchoredObjectsFor(self, collectRecursive):
        """ GetAnchoredObjectsFor(self: GridAssembly, collectRecursive: bool) -> ObjectIdCollection """
        pass

    def GetCell(self, cellId):
        """ GetCell(self: GridAssembly, cellId: int) -> GridAssemblyCell """
        pass

    def GetCellAt(self, index):
        """ GetCellAt(self: GridAssembly, index: int) -> GridAssemblyCell """
        pass

    def GetEdge(self, *__args):
        """
        GetEdge(self: GridAssembly, edgeId: int) -> (GridAssemblyEdge, int)
        GetEdge(self: GridAssembly, edgeId: int) -> GridAssemblyEdge
        GetEdge(self: GridAssembly, path: IntegerCollection) -> (GridAssemblyEdge, int)
        GetEdge(self: GridAssembly, path: IntegerCollection) -> GridAssemblyEdge
        """
        pass

    def GetEdgeAt(self, index):
        """ GetEdgeAt(self: GridAssembly, index: int) -> GridAssemblyEdge """
        pass

    def GetMaterialIds(self, component, materialIdsCollection):
        """ GetMaterialIds(self: GridAssembly, component: GridAssemblyComponentType) -> ObjectIdCollection """
        pass

    def GetMinAndMaxElevation(self, minElevation, maxElevation, componentSet):
        """ GetMinAndMaxElevation(self: GridAssembly, componentSet: GridAssemblyComponentSet) -> (float, float) """
        pass

    def GetRightAndLeftExtents(self, leftOffset, rightOffset, componentSet):
        """ GetRightAndLeftExtents(self: GridAssembly, componentSet: GridAssemblyComponentSet) -> (float, float) """
        pass

    def HasEndMiterAngle(self, angle):
        """ HasEndMiterAngle(self: GridAssembly) -> (bool, float) """
        pass

    def HasStartMiterAngle(self, angle):
        """ HasStartMiterAngle(self: GridAssembly) -> (bool, float) """
        pass

    def IncrementCellAssignmentId(self):
        """ IncrementCellAssignmentId(self: GridAssembly) -> Int16 """
        pass

    def IncrementEdgeAssignmentId(self):
        """ IncrementEdgeAssignmentId(self: GridAssembly) -> Int16 """
        pass

    def RemoveClippingBoundary(self):
        """ RemoveClippingBoundary(self: GridAssembly) """
        pass

    def SetGridDirty(self, value):
        """ SetGridDirty(self: GridAssembly, value: bool) """
        pass

    def SetHasEndMiterAngle(self, value, angle):
        """ SetHasEndMiterAngle(self: GridAssembly, value: bool, angle: float) """
        pass

    def SetHasStartMiterAngle(self, value, angle):
        """ SetHasStartMiterAngle(self: GridAssembly, value: bool, angle: float) """
        pass

    def UpdateGridContents(self):
        """ UpdateGridContents(self: GridAssembly) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BaseCurveRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseCurveRadius(self: GridAssembly) -> float

"""

    CellCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellCount(self: GridAssembly) -> int

"""

    ClippingProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingProfile(self: GridAssembly) -> Profile

Set: ClippingProfile(self: GridAssembly) = value
"""

    ClippingRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClippingRectangle(self: GridAssembly) -> ClippingRectangleInfo

Set: ClippingRectangle(self: GridAssembly) = value
"""

    ComponentSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSet(self: GridAssembly) -> GridAssemblyComponentSet

Set: ComponentSet(self: GridAssembly) = value
"""

    CustomLineworkProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomLineworkProfile(self: GridAssembly) -> Profile

"""

    EdgeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeCount(self: GridAssembly) -> int

"""

    EditDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditDepth(self: GridAssembly) -> Int16

Set: EditDepth(self: GridAssembly) = value
"""

    EndMiterAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndMiterAngle(self: GridAssembly) -> float

"""

    GridAssemblyDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAssemblyDefinition(self: GridAssembly) -> GridAssemblyDefinition

Set: GridAssemblyDefinition(self: GridAssembly) = value
"""

    GridDefinitionLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridDefinitionLocation(self: GridAssembly) -> GridDefinitionLocationType

Set: GridDefinitionLocation(self: GridAssembly) = value
"""

    HasClippingBoundary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasClippingBoundary(self: GridAssembly) -> bool

"""

    HasClippingProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasClippingProfile(self: GridAssembly) -> bool

"""

    HasClippingRectangle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasClippingRectangle(self: GridAssembly) -> bool

"""

    HasEdgeProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasEdgeProfile(self: GridAssembly) -> bool

"""

    Interferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interferences(self: GridAssembly) -> GridAssemblyInterferenceCollection

"""

    InterferencesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterferencesCount(self: GridAssembly) -> int

"""

    IsManualGridDivision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsManualGridDivision(self: GridAssembly) -> bool

"""

    IsStyleBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStyleBased(self: GridAssembly) -> bool

"""

    NestedGridCellMergeData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridCellMergeData(self: GridAssembly) -> NestedGridCellMergeDataCollection

"""

    NestedGridCellOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridCellOverrides(self: GridAssembly) -> NestedGridCellOverrideCollection

"""

    NestedGridDivisionOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridDivisionOverrides(self: GridAssembly) -> NestedGridDivisionOverrideCollection

"""

    NestedGridEdgeOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridEdgeOverrides(self: GridAssembly) -> NestedGridEdgeOverrideCollection

"""

    NestedGridEdgeProfileOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridEdgeProfileOverrides(self: GridAssembly) -> NestedGridEdgeProfileOverrideCollection

"""

    StartMiterAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartMiterAngle(self: GridAssembly) -> float

"""

    SupportsInstanceBasedGridDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsInstanceBasedGridDefinition(self: GridAssembly) -> bool

"""

    SupportsInterference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsInterference(self: GridAssembly) -> bool

"""

    SupportsStyleBasedGridDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsStyleBasedGridDefinition(self: GridAssembly) -> bool

"""

    XAxisLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XAxisLength(self: GridAssembly) -> float

"""

    YAxisLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxisLength(self: GridAssembly) -> float

"""

    YAxisOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAxisOffset(self: GridAssembly) -> float

"""



class LayoutCell(ImpObject):
    """ LayoutCell() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellId(self: LayoutCell) -> int

Set: CellId(self: LayoutCell) = value
"""



class GridAssemblyCell(LayoutCell):
    """ GridAssemblyCell() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetInfillDefinition(self, componentSet, gridDefinition):
        """ GetInfillDefinition(self: GridAssemblyCell, componentSet: GridAssemblyComponentSet, gridDefinition: GridAssemblyDefinition) -> NestedGridInfillDefinition """
        pass

    def IntersectsCutPlane(self, elevation):
        """ IntersectsCutPlane(self: GridAssemblyCell, elevation: float) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AtEntityEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AtEntityEnd(self: GridAssemblyCell) -> bool

Set: AtEntityEnd(self: GridAssemblyCell) = value
"""

    AtEntityStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AtEntityStart(self: GridAssemblyCell) -> bool

Set: AtEntityStart(self: GridAssemblyCell) = value
"""

    CellAssignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellAssignmentId(self: GridAssemblyCell) -> Int16

Set: CellAssignmentId(self: GridAssemblyCell) = value
"""

    ContainedEntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainedEntityId(self: GridAssemblyCell) -> ObjectId

Set: ContainedEntityId(self: GridAssemblyCell) = value
"""

    GrossEndX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossEndX(self: GridAssemblyCell) -> float

Set: GrossEndX(self: GridAssemblyCell) = value
"""

    GrossEndY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossEndY(self: GridAssemblyCell) -> float

Set: GrossEndY(self: GridAssemblyCell) = value
"""

    GrossStartX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossStartX(self: GridAssemblyCell) -> float

Set: GrossStartX(self: GridAssemblyCell) = value
"""

    GrossStartY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossStartY(self: GridAssemblyCell) -> float

Set: GrossStartY(self: GridAssemblyCell) = value
"""

    HasNetProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasNetProfile(self: GridAssemblyCell) -> bool

"""

    InfillOverrideId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InfillOverrideId(self: GridAssemblyCell) -> Int16

Set: InfillOverrideId(self: GridAssemblyCell) = value
"""

    IsLeafCell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLeafCell(self: GridAssemblyCell) -> bool

Set: IsLeafCell(self: GridAssemblyCell) = value
"""

    IsOverridden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverridden(self: GridAssemblyCell) -> bool

Set: IsOverridden(self: GridAssemblyCell) = value
"""

    IsVoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVoid(self: GridAssemblyCell) -> bool

Set: IsVoid(self: GridAssemblyCell) = value
"""

    NestingPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestingPath(self: GridAssemblyCell) -> IntegerCollection

"""

    NetCellProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetCellProfile(self: GridAssemblyCell) -> Profile

Set: NetCellProfile(self: GridAssemblyCell) = value
"""

    NetEndX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetEndX(self: GridAssemblyCell) -> float

Set: NetEndX(self: GridAssemblyCell) = value
"""

    NetEndY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetEndY(self: GridAssemblyCell) -> float

Set: NetEndY(self: GridAssemblyCell) = value
"""

    NetStartX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetStartX(self: GridAssemblyCell) -> float

Set: NetStartX(self: GridAssemblyCell) = value
"""

    NetStartY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetStartY(self: GridAssemblyCell) -> float

Set: NetStartY(self: GridAssemblyCell) = value
"""

    WasTransfered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WasTransfered(self: GridAssemblyCell) -> bool

Set: WasTransfered(self: GridAssemblyCell) = value
"""



class GridAssemblyComponentSet(ImpObject):
    """ GridAssemblyComponentSet() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IncrementComponentDefinitionId(self):
        """ IncrementComponentDefinitionId(self: GridAssemblyComponentSet) -> Int16 """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BoundaryEdgeComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryEdgeComponents(self: GridAssemblyComponentSet) -> NestedGridBoundaryEdgeComponentCollection

"""

    DivisionComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DivisionComponents(self: GridAssemblyComponentSet) -> NestedGridDivisionComponentCollection

"""

    InfillComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InfillComponents(self: GridAssemblyComponentSet) -> NestedGridInfillComponentCollection

"""

    InteriorEdgeComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InteriorEdgeComponents(self: GridAssemblyComponentSet) -> NestedGridInteriorEdgeComponentCollection

"""



class GridAssemblyComponentType(Enum):
    """ enum GridAssemblyComponentType, values: Frame (1), Infill (3), Mullion (2) """
    Frame = None
    Infill = None
    Mullion = None
    value__ = None


class GridAssemblyDefinition(ImpObject):
    """ GridAssemblyDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def MaxCellAssignmentId(self, maxId):
        """ MaxCellAssignmentId(self: GridAssemblyDefinition, maxId: Int16) -> Int16 """
        pass

    def MaxEdgeAssignmentId(self, maxId):
        """ MaxEdgeAssignmentId(self: GridAssemblyDefinition, maxId: Int16) -> Int16 """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GridAssemblyDefinition) -> str

Set: Name(self: GridAssemblyDefinition) = value
"""

    SpecificBoundaryEdgeAssignments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificBoundaryEdgeAssignments(self: GridAssemblyDefinition) -> NestedGridBoundaryEdgeAssignmentCollection

"""

    SpecificCellAssignments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificCellAssignments(self: GridAssemblyDefinition) -> NestedGridCellAssignmentCollection

"""

    SpecificInteriorEdgeAssignments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificInteriorEdgeAssignments(self: GridAssemblyDefinition) -> NestedGridInteriorEdgeAssignmentCollection

"""



class GridAssemblyCustomDefinition(GridAssemblyDefinition):
    """ GridAssemblyCustomDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CustomGridDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomGridDefinition(self: GridAssemblyCustomDefinition) -> GridCustom

Set: CustomGridDefinition(self: GridAssemblyCustomDefinition) = value
"""



class GridAssemblyEdge(ImpObject):
    """ GridAssemblyEdge() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEdgeDefinition(self, componentSet, gridDef):
        """ GetEdgeDefinition(self: GridAssemblyEdge, componentSet: GridAssemblyComponentSet, gridDef: GridAssemblyDefinition) -> NestedGridEdgeDefinition """
        pass

    def IntersectsCutPlane(self, elevation, edgeDefinition):
        """ IntersectsCutPlane(self: GridAssemblyEdge, elevation: float, edgeDefinition: NestedGridEdgeDefinition) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    EdgeAssignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeAssignmentId(self: GridAssemblyEdge) -> Int16

Set: EdgeAssignmentId(self: GridAssemblyEdge) = value
"""

    EdgeCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeCurve(self: GridAssemblyEdge) -> Curve2d

Set: EdgeCurve(self: GridAssemblyEdge) = value
"""

    EdgeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeId(self: GridAssemblyEdge) -> int

Set: EdgeId(self: GridAssemblyEdge) = value
"""

    EdgeOverrideId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeOverrideId(self: GridAssemblyEdge) -> Int16

Set: EdgeOverrideId(self: GridAssemblyEdge) = value
"""

    EndAtEntityEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndAtEntityEnd(self: GridAssemblyEdge) -> bool

Set: EndAtEntityEnd(self: GridAssemblyEdge) = value
"""

    EndAtEntityStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndAtEntityStart(self: GridAssemblyEdge) -> bool

Set: EndAtEntityStart(self: GridAssemblyEdge) = value
"""

    HasProfileOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasProfileOverride(self: GridAssemblyEdge) -> bool

Set: HasProfileOverride(self: GridAssemblyEdge) = value
"""

    IsInternalEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInternalEdge(self: GridAssemblyEdge) -> bool

Set: IsInternalEdge(self: GridAssemblyEdge) = value
"""

    IsOverridden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverridden(self: GridAssemblyEdge) -> bool

Set: IsOverridden(self: GridAssemblyEdge) = value
"""

    IsVoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVoid(self: GridAssemblyEdge) -> bool

Set: IsVoid(self: GridAssemblyEdge) = value
"""

    NestingPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestingPath(self: GridAssemblyEdge) -> IntegerCollection

"""

    ProfileOverrideId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileOverrideId(self: GridAssemblyEdge) -> ObjectId

Set: ProfileOverrideId(self: GridAssemblyEdge) = value
"""

    StartAtEntityEnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAtEntityEnd(self: GridAssemblyEdge) -> bool

Set: StartAtEntityEnd(self: GridAssemblyEdge) = value
"""

    StartAtEntityStart = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartAtEntityStart(self: GridAssemblyEdge) -> bool

Set: StartAtEntityStart(self: GridAssemblyEdge) = value
"""



class GridAssemblyInterference(ImpObject):
    """ GridAssemblyInterference() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AppliesToFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToFlags(self: GridAssemblyInterference) -> ApplyToFlags

Set: AppliesToFlags(self: GridAssemblyInterference) = value
"""

    EntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityId(self: GridAssemblyInterference) -> ObjectId

Set: EntityId(self: GridAssemblyInterference) = value
"""



class GridAssemblyInterferenceCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: GridAssemblyInterferenceCollection, value: GridAssemblyInterference) -> int """
        pass

    def Clear(self):
        """ Clear(self: GridAssemblyInterferenceCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: GridAssemblyInterferenceCollection, value: GridAssemblyInterference) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: GridAssemblyInterferenceCollection, array: Array[GridAssemblyInterference], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: GridAssemblyInterferenceCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: GridAssemblyInterferenceCollection, value: GridAssemblyInterference) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: GridAssemblyInterferenceCollection, index: int, value: GridAssemblyInterference) """
        pass

    def Remove(self, value):
        """ Remove(self: GridAssemblyInterferenceCollection, value: GridAssemblyInterference) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: GridAssemblyInterferenceCollection, index: int) """
        pass

    def RemoveId(self, id):
        """ RemoveId(self: GridAssemblyInterferenceCollection, id: ObjectId) """
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
    """Get: Count(self: GridAssemblyInterferenceCollection) -> int

"""



class GridAssemblyStyle(DictionaryRecord):
    """ GridAssemblyStyle() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetMaterialIds(self, component, componentIds, materialIdsCollection):
        """ GetMaterialIds(self: GridAssemblyStyle, component: GridAssemblyComponentType) -> (IntegerCollection, ObjectIdCollection) """
        pass

    def IncrementCellAssignmentId(self):
        """ IncrementCellAssignmentId(self: GridAssemblyStyle) -> Int16 """
        pass

    def IncrementEdgeAssignmentId(self):
        """ IncrementEdgeAssignmentId(self: GridAssemblyStyle) -> Int16 """
        pass

    def SetFromGridAssemblyEntity(self, gridAssembly, copyMergers, copyCellOverrides, copyEdgeOverrides, copyProfileOverrides, copyDivisionOverrides):
        """ SetFromGridAssemblyEntity(self: GridAssemblyStyle, copyMergers: bool, copyCellOverrides: bool, copyEdgeOverrides: bool, copyProfileOverrides: bool, copyDivisionOverrides: bool) -> GridAssembly """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ComponentSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentSet(self: GridAssemblyStyle) -> GridAssemblyComponentSet

Set: ComponentSet(self: GridAssemblyStyle) = value
"""

    GridAssemblyDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAssemblyDefinition(self: GridAssemblyStyle) -> GridAssemblyDefinition

Set: GridAssemblyDefinition(self: GridAssemblyStyle) = value
"""

    NestedGridCellMergeData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridCellMergeData(self: GridAssemblyStyle) -> NestedGridCellMergeDataCollection

"""

    NestedGridCellOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridCellOverrides(self: GridAssemblyStyle) -> NestedGridCellOverrideCollection

"""

    NestedGridDivisionOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridDivisionOverrides(self: GridAssemblyStyle) -> NestedGridDivisionOverrideCollection

"""

    NestedGridEdgeOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridEdgeOverrides(self: GridAssemblyStyle) -> NestedGridEdgeOverrideCollection

"""

    NestedGridEdgeProfileOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridEdgeProfileOverrides(self: GridAssemblyStyle) -> NestedGridEdgeProfileOverrideCollection

"""



class GridCustom(GridAssemblyDefinition):
    """ GridCustom() """
    def CustomGridCell(self, id):
        """ CustomGridCell(self: GridCustom, id: int) -> GridCustomCell """
        pass

    def CustomGridCellAt(self, index):
        """ CustomGridCellAt(self: GridCustom, index: int) -> GridCustomCell """
        pass

    def CustomGridNode(self, id):
        """ CustomGridNode(self: GridCustom, id: int) -> GridCustomNode """
        pass

    def CustomGridNodeAt(self, index):
        """ CustomGridNodeAt(self: GridCustom, index: int) -> GridCustomNode """
        pass

    def DeleteTransientData(self):
        """ DeleteTransientData(self: GridCustom) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetLayoutCellProfile(self, cellId, profileToWcs):
        """ GetLayoutCellProfile(self: GridCustom, cellId: int) -> (Profile, Matrix3d) """
        pass

    def GetLayoutNodeCoordinateSystem(self, nodeId):
        """ GetLayoutNodeCoordinateSystem(self: GridCustom, nodeId: int) -> Matrix3d """
        pass

    def GetLayoutNodeLocation(self, nodeId):
        """ GetLayoutNodeLocation(self: GridCustom, nodeId: int) -> Point3d """
        pass

    def UpdateParameters(self):
        """ UpdateParameters(self: GridCustom) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellCount(self: GridCustom) -> int

"""

    LayoutCellIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCellIds(self: GridCustom) -> IntegerCollection

"""

    LayoutNodeIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutNodeIds(self: GridCustom) -> IntegerCollection

"""

    NodeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeCount(self: GridCustom) -> int

"""

    PersistentSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PersistentSolution(self: GridCustom) -> bool

Set: PersistentSolution(self: GridCustom) = value
"""

    RequiresUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RequiresUpdate(self: GridCustom) -> bool

Set: RequiresUpdate(self: GridCustom) = value
"""

    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: GridCustom) -> GridCustomSegmentCollection

"""

    TransientExteriorCell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransientExteriorCell(self: GridCustom) -> GridCustomCell

"""



class GridCustomCell(LayoutCell):
    """ GridCustomCell() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CalculateCellProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculateCellProfile(self: GridCustomCell) -> Profile

"""

    ExtractNodeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtractNodeCount(self: GridCustomCell) -> int

"""

    NodeInformationCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeInformationCollection(self: GridCustomCell) -> Array[NodeInformation]

"""



class LayoutNode(ImpObject):
    """ LayoutNode() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    NodeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeId(self: LayoutNode) -> int

Set: NodeId(self: LayoutNode) = value
"""



class GridCustomNode(LayoutNode):
    """ GridCustomNode() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetIntersectionIds(self, segmentIds, segmentParameters):
        """ GetIntersectionIds(self: GridCustomNode) -> (IntegerCollection, DoubleCollection) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    NodeLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeLocation(self: GridCustomNode) -> NodeLocationType

"""

    SegmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentId(self: GridCustomNode) -> int

"""



class GridCustomSegment(Segment2d):
    """
    GridCustomSegment(curve: Curve2d)
    GridCustomSegment()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, curve=None):
        """
        __new__(cls: type, curve: Curve2d)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: GridCustomSegment) -> int

Set: Id(self: GridCustomSegment) = value
"""



class GridCustomSegmentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: GridCustomSegmentCollection, value: GridCustomSegment) -> int """
        pass

    def Clear(self):
        """ Clear(self: GridCustomSegmentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: GridCustomSegmentCollection, value: GridCustomSegment) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: GridCustomSegmentCollection, array: Array[GridCustomSegment], index: int) """
        pass

    def FindById(self, id):
        """ FindById(self: GridCustomSegmentCollection, id: int) -> GridCustomSegment """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: GridCustomSegmentCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: GridCustomSegmentCollection, value: GridCustomSegment) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: GridCustomSegmentCollection, index: int, value: GridCustomSegment) """
        pass

    def Remove(self, value):
        """ Remove(self: GridCustomSegmentCollection, value: GridCustomSegment) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: GridCustomSegmentCollection, index: int) """
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
    """Get: Count(self: GridCustomSegmentCollection) -> int

"""



class GridDefinitionLocationType(Enum):
    """ enum GridDefinitionLocationType, values: InstanceBased (0), StyleBased (1) """
    InstanceBased = None
    StyleBased = None
    value__ = None


class GridType(Enum):
    """ enum GridType, values: UVCustom (3), UVRadial (1), UVRectangular (0), UVWRectangular (2) """
    UVCustom = None
    UVRadial = None
    UVRectangular = None
    UVWRectangular = None
    value__ = None


class GridUv(ImpObject):
    """ GridUv() """
    def AddNode(self, parameterU, parameterV):
        """ AddNode(self: GridUv, parameterU: float, parameterV: float) """
        pass

    def AppendGridColumn(self, parameterU):
        """ AppendGridColumn(self: GridUv, parameterU: float) """
        pass

    def AppendGridRow(self, parameterV):
        """ AppendGridRow(self: GridUv, parameterV: float) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetLayoutCellProfile(self, cellId, toWcs):
        """ GetLayoutCellProfile(self: GridUv, cellId: int) -> (Profile, Matrix3d) """
        pass

    def GetLayoutGrid2dCell(self, id):
        """ GetLayoutGrid2dCell(self: GridUv, id: int) -> LayoutGrid2dCell """
        pass

    def GetLayoutGrid2dCellAt(self, index):
        """ GetLayoutGrid2dCellAt(self: GridUv, index: int) -> LayoutGrid2dCell """
        pass

    def GetLayoutGrid2dNode(self, id):
        """ GetLayoutGrid2dNode(self: GridUv, id: int) -> LayoutGrid2dNode """
        pass

    def GetLayoutGrid2dNodeAt(self, index):
        """ GetLayoutGrid2dNodeAt(self: GridUv, index: int) -> LayoutGrid2dNode """
        pass

    def GetLayoutNodeCoordinateSystem(self, nodeId):
        """ GetLayoutNodeCoordinateSystem(self: GridUv, nodeId: int) -> Matrix3d """
        pass

    def GetLayoutNodeLocation(self, nodeId):
        """ GetLayoutNodeLocation(self: GridUv, nodeId: int) -> Point3d """
        pass

    def MoveGridColumn(self, oldParameter, newParameter):
        """ MoveGridColumn(self: GridUv, oldParameter: float, newParameter: float) """
        pass

    def MoveGridRow(self, oldParameter, newParameter):
        """ MoveGridRow(self: GridUv, oldParameter: float, newParameter: float) """
        pass

    def RemoveGridColumn(self, parameterU):
        """ RemoveGridColumn(self: GridUv, parameterU: float) """
        pass

    def RemoveGridRow(self, parameterV):
        """ RemoveGridRow(self: GridUv, parameterV: float) """
        pass

    def UpdateParameters(self):
        """ UpdateParameters(self: GridUv) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellCount(self: GridUv) -> int

"""

    GridType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridType(self: GridUv) -> GridType

"""

    LayoutCellIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCellIds(self: GridUv) -> IntegerCollection

"""

    LayoutNodeIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutNodeIds(self: GridUv) -> IntegerCollection

"""

    NodeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeCount(self: GridUv) -> int

"""

    UAxisLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UAxisLength(self: GridUv) -> float

Set: UAxisLength(self: GridUv) = value
"""

    UEndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UEndOffset(self: GridUv) -> float

Set: UEndOffset(self: GridUv) = value
"""

    ULayoutMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ULayoutMode(self: GridUv) -> UVLayoutModeType

Set: ULayoutMode(self: GridUv) = value
"""

    UParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UParameters(self: GridUv) -> DoubleCollection

"""

    USpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: USpacing(self: GridUv) -> float

Set: USpacing(self: GridUv) = value
"""

    UStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UStartOffset(self: GridUv) -> float

Set: UStartOffset(self: GridUv) = value
"""

    VAxisLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VAxisLength(self: GridUv) -> float

Set: VAxisLength(self: GridUv) = value
"""

    VEndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VEndOffset(self: GridUv) -> float

Set: VEndOffset(self: GridUv) = value
"""

    VLayoutMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VLayoutMode(self: GridUv) -> UVLayoutModeType

Set: VLayoutMode(self: GridUv) = value
"""

    VParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VParameters(self: GridUv) -> DoubleCollection

"""

    VSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VSpacing(self: GridUv) -> float

Set: VSpacing(self: GridUv) = value
"""

    VStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VStartOffset(self: GridUv) -> float

Set: VStartOffset(self: GridUv) = value
"""



class GridUvRadial(GridUv):
    """ GridUvRadial() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    UInsideRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UInsideRadius(self: GridUvRadial) -> float

Set: UInsideRadius(self: GridUvRadial) = value
"""

    VAngleSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VAngleSpacing(self: GridUvRadial) -> float

Set: VAngleSpacing(self: GridUvRadial) = value
"""

    VAxisAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VAxisAngle(self: GridUvRadial) -> float

Set: VAxisAngle(self: GridUvRadial) = value
"""

    VEndAngleOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VEndAngleOffset(self: GridUvRadial) -> float

Set: VEndAngleOffset(self: GridUvRadial) = value
"""

    VStartAngleOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VStartAngleOffset(self: GridUvRadial) -> float

Set: VStartAngleOffset(self: GridUvRadial) = value
"""



class GridUvRectangular(GridUv):
    """ GridUvRectangular() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class GridUvw(GridUv):
    """ GridUvw() """
    def AddNode(self, parameterU, parameterV, parameterW=None):
        """ AddNode(self: GridUvw, parameterU: float, parameterV: float, parameterW: float) """
        pass

    def AppendGridLevel(self, parameterW):
        """ AppendGridLevel(self: GridUvw, parameterW: float) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetLayoutGrid3dCell(self, id):
        """ GetLayoutGrid3dCell(self: GridUvw, id: int) -> LayoutGrid3dCell """
        pass

    def GetLayoutGrid3dCellAt(self, index):
        """ GetLayoutGrid3dCellAt(self: GridUvw, index: int) -> LayoutGrid3dCell """
        pass

    def GetLayoutGrid3dNode(self, id):
        """ GetLayoutGrid3dNode(self: GridUvw, id: int) -> LayoutGrid3dNode """
        pass

    def GetLayoutGrid3dNodeAt(self, index):
        """ GetLayoutGrid3dNodeAt(self: GridUvw, index: int) -> LayoutGrid3dNode """
        pass

    def GetLayoutGrid3dVolume(self, id):
        """ GetLayoutGrid3dVolume(self: GridUvw, id: int) -> LayoutGrid3dVolume """
        pass

    def GetLayoutGrid3dVolumeAt(self, index):
        """ GetLayoutGrid3dVolumeAt(self: GridUvw, index: int) -> LayoutGrid3dVolume """
        pass

    def GetLayoutVolumeBody(self, volumeId, toWcs):
        """ GetLayoutVolumeBody(self: GridUvw, volumeId: int) -> (Body, Matrix3d) """
        pass

    def GetLayoutVolumeCentroid(self, volumeId):
        """ GetLayoutVolumeCentroid(self: GridUvw, volumeId: int) -> Matrix3d """
        pass

    def GetLayoutVolumeExtent(self, volumeId, length, width, height, toWcs):
        """ GetLayoutVolumeExtent(self: GridUvw, volumeId: int) -> (float, float, float, Matrix3d) """
        pass

    def MoveGridLevel(self, oldParameter, newParameter):
        """ MoveGridLevel(self: GridUvw, oldParameter: float, newParameter: float) """
        pass

    def RemoveGridLevel(self, parameterW):
        """ RemoveGridLevel(self: GridUvw, parameterW: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    LayoutVolumeIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutVolumeIds(self: GridUvw) -> IntegerCollection

"""

    VolumeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeCount(self: GridUvw) -> int

"""

    WAxisLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WAxisLength(self: GridUvw) -> float

Set: WAxisLength(self: GridUvw) = value
"""

    WEndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WEndOffset(self: GridUvw) -> float

Set: WEndOffset(self: GridUvw) = value
"""

    WLayoutMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WLayoutMode(self: GridUvw) -> UVLayoutModeType

Set: WLayoutMode(self: GridUvw) = value
"""

    WParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WParameters(self: GridUvw) -> DoubleCollection

"""

    WSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WSpacing(self: GridUvw) -> float

Set: WSpacing(self: GridUvw) = value
"""

    WStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WStartOffset(self: GridUvw) -> float

Set: WStartOffset(self: GridUvw) = value
"""



class GsMarkerInformationNode(RXObject):
    """ GsMarkerInformationNode(parentTree: GsMarkerInformationTree, parentNode: GsMarkerInformationNode) """
    def Add(self, node):
        """ Add(self: GsMarkerInformationNode, node: GsMarkerInformationNode) """
        pass

    def Clear(self):
        """ Clear(self: GsMarkerInformationNode) """
        pass

    def CollectInformationNodes(self, nodeClass=None, recursive=None):
        """
        CollectInformationNodes(self: GsMarkerInformationNode) -> Array[GsMarkerInformationNode]
        CollectInformationNodes(self: GsMarkerInformationNode, nodeClass: RXClass, recursive: bool) -> Array[GsMarkerInformationNode]
        """
        pass

    def CollectLeafNodeGsMarkers(self, collectAll3DBodyGsMarkers=None):
        """
        CollectLeafNodeGsMarkers(self: GsMarkerInformationNode) -> Array[IntPtr]
        CollectLeafNodeGsMarkers(self: GsMarkerInformationNode, collectAll3DBodyGsMarkers: bool) -> Array[IntPtr]
        """
        pass

    def ContentToString(self, getName, continueWithNextLevelNodes):
        """ ContentToString(self: GsMarkerInformationNode, getName: bool, continueWithNextLevelNodes: bool) -> StringCollection """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def InformationNodeForGsMarker(self, value):
        """ InformationNodeForGsMarker(self: GsMarkerInformationNode, value: IntPtr) -> GsMarkerInformationNode """
        pass

    def InformationNodesForGsMarker(self, value):
        """ InformationNodesForGsMarker(self: GsMarkerInformationNode, value: IntPtr) -> Array[GsMarkerInformationNode] """
        pass

    @staticmethod
    def ObjectIdFromOldId(oldId):
        """ ObjectIdFromOldId(oldId: Int64) -> ObjectId """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parentTree, parentNode):
        """
        __new__(cls: type, parentTree: GsMarkerInformationTree, parentNode: GsMarkerInformationNode)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    GsMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GsMarker(self: GsMarkerInformationNode) -> IntPtr

Set: GsMarker(self: GsMarkerInformationNode) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GsMarkerInformationNode) -> str

"""

    ParentNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentNode(self: GsMarkerInformationNode) -> GsMarkerInformationNode

Set: ParentNode(self: GsMarkerInformationNode) = value
"""

    ParentTree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentTree(self: GsMarkerInformationNode) -> GsMarkerInformationTree

Set: ParentTree(self: GsMarkerInformationNode) = value
"""



class GsMarkerDisplayComponentInformationNode(GsMarkerInformationNode):
    """
    GsMarkerDisplayComponentInformationNode(name: str, parentTree: GsMarkerInformationTree, parentNode: GsMarkerInformationNode)
    GsMarkerDisplayComponentInformationNode()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, parentTree=None, parentNode=None):
        """
        __new__(cls: type, name: str, parentTree: GsMarkerInformationTree, parentNode: GsMarkerInformationNode)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayComponentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayComponentName(self: GsMarkerDisplayComponentInformationNode) -> str

Set: DisplayComponentName(self: GsMarkerDisplayComponentInformationNode) = value
"""

    DisplayPropertiesId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayPropertiesId(self: GsMarkerDisplayComponentInformationNode) -> ObjectId

"""

    DisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationId(self: GsMarkerDisplayComponentInformationNode) -> ObjectId

"""

    ParentDisplayRepresentationInformationNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentDisplayRepresentationInformationNode(self: GsMarkerDisplayComponentInformationNode) -> GsMarkerDisplayRepresentationInformationNode

Set: ParentDisplayRepresentationInformationNode(self: GsMarkerDisplayComponentInformationNode) = value
"""



class GsMarkerDisplayRepresentationInformationNode(GsMarkerInformationNode):
    """
    GsMarkerDisplayRepresentationInformationNode(displayRepresentationId: ObjectId, parentTree: GsMarkerInformationTree, parentNode: GsMarkerInformationNode)
    GsMarkerDisplayRepresentationInformationNode()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetDisplayComponentId(self, component):
        """ GetDisplayComponentId(self: GsMarkerDisplayRepresentationInformationNode, component: DisplayComponentEntity) -> int """
        pass

    def GetDisplayComponentName(self, component):
        """ GetDisplayComponentName(self: GsMarkerDisplayRepresentationInformationNode, component: DisplayComponentEntity) -> str """
        pass

    def ResetTransientDisplayPropertiesInformation(self):
        """ ResetTransientDisplayPropertiesInformation(self: GsMarkerDisplayRepresentationInformationNode) """
        pass

    def SetDisplayPropertiesInformation(self, properties):
        """ SetDisplayPropertiesInformation(self: GsMarkerDisplayRepresentationInformationNode, properties: DisplayProperties) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, displayRepresentationId=None, parentTree=None, parentNode=None):
        """
        __new__(cls: type, displayRepresentationId: ObjectId, parentTree: GsMarkerInformationTree, parentNode: GsMarkerInformationNode)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayPropertiesId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayPropertiesId(self: GsMarkerDisplayRepresentationInformationNode) -> ObjectId

Set: DisplayPropertiesId(self: GsMarkerDisplayRepresentationInformationNode) = value
"""

    DisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationId(self: GsMarkerDisplayRepresentationInformationNode) -> ObjectId

Set: DisplayRepresentationId(self: GsMarkerDisplayRepresentationInformationNode) = value
"""



class GsMarkerInformationTree(GsMarkerInformationNode):
    """
    GsMarkerInformationTree(id: ObjectId, dbReferencePath: ObjectIdCollection)
    GsMarkerInformationTree(id: ObjectId)
    GsMarkerInformationTree()
    """
    def AddBranchInformationNode(self, pushIntoCurrentNodeStack):
        """ AddBranchInformationNode(self: GsMarkerInformationTree, pushIntoCurrentNodeStack: bool) """
        pass

    def AddCustomBlockInformationNode(self, pushIntoCurrentNodeStack):
        """ AddCustomBlockInformationNode(self: GsMarkerInformationTree, pushIntoCurrentNodeStack: bool) """
        pass

    def AddCustomInformationNode(self, nGsMarker, pushIntoCurrentNodeStack):
        """ AddCustomInformationNode(self: GsMarkerInformationTree, nGsMarker: IntPtr, pushIntoCurrentNodeStack: bool) """
        pass

    def AddDisplayComponentInformationNode(self, *__args):
        """ AddDisplayComponentInformationNode(self: GsMarkerInformationTree, componentEntity: DisplayComponentEntity, pushIntoCurrentNodeStack: bool)AddDisplayComponentInformationNode(self: GsMarkerInformationTree, componentName: str, pushIntoCurrentNodeStack: bool) """
        pass

    def AddDisplayRepresentationInformationNode(self, id, pushIntoCurrentNodeStack):
        """ AddDisplayRepresentationInformationNode(self: GsMarkerInformationTree, id: ObjectId, pushIntoCurrentNodeStack: bool) """
        pass

    def AddDisplayThemeInformationNode(self, id, componentIndex, pushIntoCurrentNodeStack):
        """ AddDisplayThemeInformationNode(self: GsMarkerInformationTree, id: ObjectId, componentIndex: int, pushIntoCurrentNodeStack: bool) """
        pass

    def AddGsMarkerInformationNode(self, node, pushIntoCurrentNodeStack):
        """ AddGsMarkerInformationNode(self: GsMarkerInformationTree, node: GsMarkerInformationNode, pushIntoCurrentNodeStack: bool) """
        pass

    def AddSelectedComponentInformation(self, *__args):
        """ AddSelectedComponentInformation(self: GsMarkerInformationTree, gsMarkers: IntPtrCollection)AddSelectedComponentInformation(self: GsMarkerInformationTree, information: EntitySelectedComponentInformation) """
        pass

    def AddUnsupportedGraphicsInformationNode(self, pushIntoCurrentNodeStack):
        """ AddUnsupportedGraphicsInformationNode(self: GsMarkerInformationTree, pushIntoCurrentNodeStack: bool) """
        pass

    def CleanupGsMarkersForHoverHighliting(self):
        """ CleanupGsMarkersForHoverHighliting(self: GsMarkerInformationTree) """
        pass

    def ClearSelectedComponentsGsMarkers(self):
        """ ClearSelectedComponentsGsMarkers(self: GsMarkerInformationTree) """
        pass

    def ClearSelectedObjectDisplayRepresentationInformation(self):
        """ ClearSelectedObjectDisplayRepresentationInformation(self: GsMarkerInformationTree) """
        pass

    def CollectNonViewportInformationNodesInViewport(self, id, viewportIndex, nodeClass=None, recursive=None):
        """
        CollectNonViewportInformationNodesInViewport(self: GsMarkerInformationTree, id: ObjectId, viewportIndex: int, nodeClass: RXClass, recursive: bool) -> Array[GsMarkerInformationNode]
        CollectNonViewportInformationNodesInViewport(self: GsMarkerInformationTree, id: ObjectId, viewportIndex: int) -> Array[GsMarkerInformationNode]
        """
        pass

    def CustomBlockInformationToString(self):
        """ CustomBlockInformationToString(self: GsMarkerInformationTree) -> StringCollection """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetDisplayComponentNodesInCurrentViewport(self, gsMarkers, id, viewportNumber):
        """ GetDisplayComponentNodesInCurrentViewport(self: GsMarkerInformationTree, gsMarkers: IntPtrCollection, id: ObjectId, viewportNumber: int) -> Array[GsMarkerDisplayComponentInformationNode] """
        pass

    def GetSelectedComponentGsMarkersForHighligting(self):
        """ GetSelectedComponentGsMarkersForHighligting(self: GsMarkerInformationTree) -> IntPtrCollection """
        pass

    def GetSelectedComponentGsMarkersOnByMaterialChange(self, information):
        """ GetSelectedComponentGsMarkersOnByMaterialChange(self: GsMarkerInformationTree, information: EntitySelectedComponentInformation) -> IntPtrCollection """
        pass

    def GetSelectedComponentsInformation(self):
        """ GetSelectedComponentsInformation(self: GsMarkerInformationTree) -> Array[EntitySelectedComponentInformation] """
        pass

    def GetViewportIdFromViewportNode(self, gsMarker):
        """ GetViewportIdFromViewportNode(self: GsMarkerInformationTree, gsMarker: IntPtr) -> ObjectId """
        pass

    def GetViewportNumberFromViewportNode(self, gsMarker):
        """ GetViewportNumberFromViewportNode(self: GsMarkerInformationTree, gsMarker: IntPtr) -> int """
        pass

    def HasDatabaseReferencePath(self, path):
        """ HasDatabaseReferencePath(self: GsMarkerInformationTree, path: ObjectIdCollection) -> bool """
        pass

    def InformationNodeForGsMarkerAndInformationType(self, value, nodeType, doIsKindOfTest):
        """ InformationNodeForGsMarkerAndInformationType(self: GsMarkerInformationTree, value: IntPtr, nodeType: RXClass, doIsKindOfTest: bool) -> GsMarkerInformationNode """
        pass

    def PopCurrentGsMarkerInformationNode(self, nodeClass=None, checkForDerivedTypes=None):
        """ PopCurrentGsMarkerInformationNode(self: GsMarkerInformationTree, nodeClass: RXClass, checkForDerivedTypes: bool)PopCurrentGsMarkerInformationNode(self: GsMarkerInformationTree) """
        pass

    def PopViewportInformationNode(self):
        """ PopViewportInformationNode(self: GsMarkerInformationTree) """
        pass

    def PushCurrentGsMarkerInformationNode(self, node):
        """ PushCurrentGsMarkerInformationNode(self: GsMarkerInformationTree, node: GsMarkerInformationNode) """
        pass

    def ResetCurrentNodeStack(self):
        """ ResetCurrentNodeStack(self: GsMarkerInformationTree) """
        pass

    def ResetTransientDisplayPropertiesInformationForCurrentDisplayInformationNode(self):
        """ ResetTransientDisplayPropertiesInformationForCurrentDisplayInformationNode(self: GsMarkerInformationTree) """
        pass

    def SetDisplayPropertiesForCurrentDisplayInformationNode(self, properties):
        """ SetDisplayPropertiesForCurrentDisplayInformationNode(self: GsMarkerInformationTree, properties: DisplayProperties) """
        pass

    def SetParentCustomBlockOwnerInformation(self, id, customBlockGsMarker):
        """ SetParentCustomBlockOwnerInformation(self: GsMarkerInformationTree, id: ObjectId, customBlockGsMarker: IntPtr) """
        pass

    def UpdateSelectedComponentInformation(self, id, index):
        """ UpdateSelectedComponentInformation(self: GsMarkerInformationTree, id: ObjectId, index: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id=None, dbReferencePath=None):
        """
        __new__(cls: type, id: ObjectId, dbReferencePath: ObjectIdCollection)
        __new__(cls: type, id: ObjectId)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AreComponentsSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreComponentsSelected(self: GsMarkerInformationTree) -> bool

"""

    CurrentGsMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentGsMarker(self: GsMarkerInformationTree) -> IntPtr

"""

    CurrentGsMarkerInformationNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentGsMarkerInformationNode(self: GsMarkerInformationTree) -> GsMarkerInformationNode

"""

    CustomBlockGsMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomBlockGsMarker(self: GsMarkerInformationTree) -> IntPtr

"""

    CustomBlockOwnerEntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomBlockOwnerEntityId(self: GsMarkerInformationTree) -> ObjectId

"""

    EntityIsFromCustomBlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityIsFromCustomBlock(self: GsMarkerInformationTree) -> bool

"""

    GsMarkersForHoverHighlighting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GsMarkersForHoverHighlighting(self: GsMarkerInformationTree) -> Array[IntPtr]

Set: GsMarkersForHoverHighlighting(self: GsMarkerInformationTree) = value
"""

    HasGsMarkersForHoverHighlighting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasGsMarkersForHoverHighlighting(self: GsMarkerInformationTree) -> bool

"""

    IsDrawingCustomBlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDrawingCustomBlock(self: GsMarkerInformationTree) -> bool

Set: IsDrawingCustomBlock(self: GsMarkerInformationTree) = value
"""

    IsDrawingWithDisplayTheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDrawingWithDisplayTheme(self: GsMarkerInformationTree) -> bool

"""

    IsEntity2dSectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEntity2dSectionType(self: GsMarkerInformationTree) -> bool

Set: IsEntity2dSectionType(self: GsMarkerInformationTree) = value
"""

    NextGsMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextGsMarker(self: GsMarkerInformationTree) -> IntPtr

"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: GsMarkerInformationTree) -> ObjectId

"""

    PopulateTree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PopulateTree(self: GsMarkerInformationTree) -> bool

Set: PopulateTree(self: GsMarkerInformationTree) = value
"""

    PushCustomOverrideNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PushCustomOverrideNode(self: GsMarkerInformationTree) -> bool

Set: PushCustomOverrideNode(self: GsMarkerInformationTree) = value
"""

    SelectedObjectDisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedObjectDisplayRepresentationId(self: GsMarkerInformationTree) -> ObjectId

Set: SelectedObjectDisplayRepresentationId(self: GsMarkerInformationTree) = value
"""

    StartGsMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartGsMarker(self: GsMarkerInformationTree) -> IntPtr

Set: StartGsMarker(self: GsMarkerInformationTree) = value
"""



class HatchType(Enum):
    """ enum HatchType, values: CustomDefined (2), PreDefined (1), SolidFill (3), UserDefined (0) """
    CustomDefined = None
    PreDefined = None
    SolidFill = None
    UserDefined = None
    value__ = None


class IDisplayThemeComponentOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IDisplayThemeComponentOperation, A_0: DisplayThemeComponentBase) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IDisplayThemeComponentOperation, A_0: int) -> DisplayThemeComponentBase """
        pass

    def GetCount(self):
        """ GetCount(self: IDisplayThemeComponentOperation) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: IDisplayThemeComponentOperation, A_0: int, A_1: DisplayThemeComponentBase) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IDisplayThemeComponentOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IDisplayThemeComponentOperation, A_0: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IDisplayThemeRuleOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IDisplayThemeRuleOperation, A_0: DisplayThemeRuleBase) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IDisplayThemeRuleOperation, A_0: int) -> DisplayThemeRuleBase """
        pass

    def GetCount(self):
        """ GetCount(self: IDisplayThemeRuleOperation) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: IDisplayThemeRuleOperation, A_0: int, A_1: DisplayThemeRuleBase) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IDisplayThemeRuleOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IDisplayThemeRuleOperation, A_0: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IImpTreeOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IImpTreeOperation, A_0: ImpTree) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IImpTreeOperation, A_0: int) -> ImpTree """
        pass

    def GetCount(self):
        """ GetCount(self: IImpTreeOperation) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: IImpTreeOperation, A_0: int, A_1: ImpTree) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IImpTreeOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IImpTreeOperation, A_0: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ILayerKeyDefinitionOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: ILayerKeyDefinitionOperation, A_0: LayerKeyDefinition) -> int """
        pass

    def GetAt(self, A_0):
        """
        GetAt(self: ILayerKeyDefinitionOperation, A_0: int) -> LayerKeyDefinition
        GetAt(self: ILayerKeyDefinitionOperation, A_0: str) -> LayerKeyDefinition
        """
        pass

    def GetCount(self):
        """ GetCount(self: ILayerKeyDefinitionOperation) -> int """
        pass

    def IndexOf(self, A_0):
        """ IndexOf(self: ILayerKeyDefinitionOperation, A_0: LayerKeyDefinition) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: ILayerKeyDefinitionOperation, A_0: int, A_1: LayerKeyDefinition) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: ILayerKeyDefinitionOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: ILayerKeyDefinitionOperation, A_0: int) """
        pass

    def SetAt(self, A_0, A_1):
        """ SetAt(self: ILayerKeyDefinitionOperation, A_0: int, A_1: LayerKeyDefinition) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ImpArray(ImpObject):
    """ ImpArray[T]() """
    def Add(self, item):
# Error generating skeleton for function Add: Method must be called on a Type for which Type.IsGenericParameter is false.

    def Clear(self):
        """ Clear(self: ImpArray[T]) """
        pass

    def Contains(self, item):
# Error generating skeleton for function Contains: Method must be called on a Type for which Type.IsGenericParameter is false.

    def CopyTo(self, array, index):
        """ CopyTo(self: ImpArray[T], array: Array[T], index: int) """
        pass

    def DeleteAt(self, index):
        """ DeleteAt(self: ImpArray[T], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ImpArray[T]) -> IEnumerator[T] """
        pass

    def IndexOf(self, item):
# Error generating skeleton for function IndexOf: Method must be called on a Type for which Type.IsGenericParameter is false.

    def Insert(self, index, item):
# Error generating skeleton for function Insert: Method must be called on a Type for which Type.IsGenericParameter is false.

    def Remove(self, item):
# Error generating skeleton for function Remove: Method must be called on a Type for which Type.IsGenericParameter is false.

    def RemoveAll(self):
        """ RemoveAll(self: ImpArray[T]) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ImpArray[T], index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
# Error generating skeleton for function __contains__: Method must be called on a Type for which Type.IsGenericParameter is false.

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
    def __new__(self):
        """
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        __new__(cls: type)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    AllowNullObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNullObjects(self: ImpArray[T]) -> bool

Set: AllowNullObjects(self: ImpArray[T]) = value
"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ImpArray[T]) -> int

"""



class ImpObjectCollection(DisposableWrapper):
    """ ImpObjectCollection() """
    def Add(self, value):
        """ Add(self: ImpObjectCollection, value: ImpObject) -> int """
        pass

    def Clear(self):
        """ Clear(self: ImpObjectCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: ImpObjectCollection, value: ImpObject) -> bool """
        pass

    def CopyTo(self, arr, index):
        """ CopyTo(self: ImpObjectCollection, arr: Array[ImpObject], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ImpObjectCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: ImpObjectCollection, value: ImpObject) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: ImpObjectCollection, index: int, value: ImpObject) """
        pass

    def Remove(self, value):
        """ Remove(self: ImpObjectCollection, value: ImpObject) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ImpObjectCollection, index: int) """
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
    """Get: Count(self: ImpObjectCollection) -> int

"""



class ImpTreeCollection(object):
    """ ImpTreeCollection(pOp: IImpTreeOperation) """
    def Add(self, value):
        """ Add(self: ImpTreeCollection, value: ImpTree) -> int """
        pass

    def Clear(self):
        """ Clear(self: ImpTreeCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: ImpTreeCollection, value: ImpTree) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: ImpTreeCollection, array: Array[ImpTree], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ImpTreeCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: ImpTreeCollection, value: ImpTree) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: ImpTreeCollection, index: int, value: ImpTree) """
        pass

    def Remove(self, value):
        """ Remove(self: ImpTreeCollection, value: ImpTree) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ImpTreeCollection, index: int) """
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IImpTreeOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ImpTreeCollection) -> int

"""



class IndexSpecifier(ImpObject):
    """ IndexSpecifier() """
    def AppliesToIndex(self, index, startIndex, endIndex):
        """ AppliesToIndex(self: IndexSpecifier, index: int, startIndex: int, endIndex: int) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class IndexSpecifierBoundaryEdge(IndexSpecifier):
    """ IndexSpecifierBoundaryEdge() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BoundaryFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryFlags(self: IndexSpecifierBoundaryEdge) -> BoundaryFlags

Set: BoundaryFlags(self: IndexSpecifierBoundaryEdge) = value
"""

    OnBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnBottom(self: IndexSpecifierBoundaryEdge) -> bool

"""

    OnLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnLeft(self: IndexSpecifierBoundaryEdge) -> bool

"""

    OnRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnRight(self: IndexSpecifierBoundaryEdge) -> bool

"""

    OnTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnTop(self: IndexSpecifierBoundaryEdge) -> bool

"""



class IndexSpecifierExplicit(IndexSpecifier):
    """ IndexSpecifierExplicit() """
    def AppendToIndexArray(self, index):
        """ AppendToIndexArray(self: IndexSpecifierExplicit, index: int) """
        pass

    def ClearIndexArray(self):
        """ ClearIndexArray(self: IndexSpecifierExplicit) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def RemoveFromIndexArray(self, index):
        """ RemoveFromIndexArray(self: IndexSpecifierExplicit, index: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    IndexArray = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndexArray(self: IndexSpecifierExplicit) -> IntegerCollection

"""



class IndexSpecifierLocation(IndexSpecifier):
    """ IndexSpecifierLocation() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AppliesToEndIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToEndIndex(self: IndexSpecifierLocation) -> bool

Set: AppliesToEndIndex(self: IndexSpecifierLocation) = value
"""

    AppliesToMiddleIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToMiddleIndex(self: IndexSpecifierLocation) -> bool

Set: AppliesToMiddleIndex(self: IndexSpecifierLocation) = value
"""

    AppliesToStartIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToStartIndex(self: IndexSpecifierLocation) -> bool

Set: AppliesToStartIndex(self: IndexSpecifierLocation) = value
"""



class InplaceEditor(DictionaryRecord):
    """ InplaceEditor() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetInplaceEditEntities(self):
        """ GetInplaceEditEntities(self: InplaceEditor) -> ObjectIdCollection """
        pass

    def InvalidCommandInInPlaceEditMode(self, commandName, status):
        """ InvalidCommandInInPlaceEditMode(self: InplaceEditor, commandName: str) -> (bool, CommandStatus) """
        pass

    def IsCurrentEditorInplaceEditEntity(self, id):
        """ IsCurrentEditorInplaceEditEntity(self: InplaceEditor, id: ObjectId) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ActiveInplaceEditorComponentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveInplaceEditorComponentCount(self: InplaceEditor) -> int

"""

    Entity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entity(self: InplaceEditor) -> Entity

Set: Entity(self: InplaceEditor) = value
"""

    EntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityId(self: InplaceEditor) -> ObjectId

Set: EntityId(self: InplaceEditor) = value
"""

    InplaceEditorComponentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InplaceEditorComponentCount(self: InplaceEditor) -> int

"""

    IsSingleComponentEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSingleComponentEditor(self: InplaceEditor) -> bool

"""

    LongTransactionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LongTransactionId(self: InplaceEditor) -> ObjectId

Set: LongTransactionId(self: InplaceEditor) = value
"""

    OldEntityEcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldEntityEcs(self: InplaceEditor) -> Matrix3d

Set: OldEntityEcs(self: InplaceEditor) = value
"""

    OldUcsMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldUcsMatrix(self: InplaceEditor) -> Matrix3d

Set: OldUcsMatrix(self: InplaceEditor) = value
"""



class InplaceEditorClassInformation(object):
    # no doc
    InplaceEditorClassType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InplaceEditorClassType(self: InplaceEditorClassInformation) -> RXClass

Set: InplaceEditorClassType(self: InplaceEditorClassInformation) = value
"""

    InplaceEditorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InplaceEditorId(self: InplaceEditorClassInformation) -> ObjectId

Set: InplaceEditorId(self: InplaceEditorClassInformation) = value
"""



class InplaceEditorMap(DisposableWrapper):
    """ InplaceEditorMap() """
    def AddInplaceEditor(self, oldId, editorDataId):
        """ AddInplaceEditor(self: InplaceEditorMap, oldId: IntPtr, editorDataId: ObjectId) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def FindInplaceEditor(self, oldId):
        """ FindInplaceEditor(self: InplaceEditorMap, oldId: IntPtr) -> ObjectId """
        pass

    def FindInplaceEditorIdForInplaceEditEntityId(self, inplaceEditEntityId):
        """ FindInplaceEditorIdForInplaceEditEntityId(self: InplaceEditorMap, inplaceEditEntityId: ObjectId) -> ObjectId """
        pass

    def FindParentEntityIdForInplaceEditEntityId(self, inplaceEditEntityId):
        """ FindParentEntityIdForInplaceEditEntityId(self: InplaceEditorMap, inplaceEditEntityId: ObjectId) -> ObjectId """
        pass

    def FindParentEntityIdForInplaceEditorId(self, inplaceEditorId):
        """ FindParentEntityIdForInplaceEditorId(self: InplaceEditorMap, inplaceEditorId: ObjectId) -> ObjectId """
        pass

    def GetEntityIdsInInplaceEditMode(self):
        """ GetEntityIdsInInplaceEditMode(self: InplaceEditorMap) -> ObjectIdCollection """
        pass

    def GetObjectIdsInInplaceEditMode(self):
        """ GetObjectIdsInInplaceEditMode(self: InplaceEditorMap) -> ObjectIdCollection """
        pass

    def RemoveInplaceEditor(self, id):
        """ RemoveInplaceEditor(self: InplaceEditorMap, id: IntPtr) -> bool """
        pass

    def RemoveInplaceEditorAll(self):
        """ RemoveInplaceEditorAll(self: InplaceEditorMap) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    FirstInplaceEditorId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstInplaceEditorId(self: InplaceEditorMap) -> ObjectId

"""

    FirstParentEntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FirstParentEntityId(self: InplaceEditorMap) -> ObjectId

"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: InplaceEditorMap) -> UInt32

"""



class InplaceEditorUtilities(object):
    """ InplaceEditorUtilities() """
    @staticmethod
    def AddEditorToExtentionDictionaryAndClose(objectToSegOn, newEditorToAdd):
        """ AddEditorToExtentionDictionaryAndClose(objectToSegOn: DBObject, newEditorToAdd: InplaceEditor) -> ObjectId """
        pass

    @staticmethod
    def AddInplaceEditorToEntity(entity, inplaceEditorId):
        """ AddInplaceEditorToEntity(entity: Entity, inplaceEditorId: ObjectId) """
        pass

    @staticmethod
    def CreateNewDictionaryEntryFromOldDictionaryEntry(oldDictionaryId, dictionary):
        """ CreateNewDictionaryEntryFromOldDictionaryEntry(oldDictionaryId: ObjectId, dictionary: Dictionary) -> ObjectId """
        pass

    @staticmethod
    def CreateNewInplaceEditDictionaryEntryFromOldDictionaryEntry(oldDictionaryId, dictionary):
        """ CreateNewInplaceEditDictionaryEntryFromOldDictionaryEntry(oldDictionaryId: ObjectId, dictionary: Dictionary) -> ObjectId """
        pass

    @staticmethod
    def CreateNewInplaceEditProfileDefinitionFromOldProfileDefinition(oldProfileId):
        """ CreateNewInplaceEditProfileDefinitionFromOldProfileDefinition(oldProfileId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def CreateNewProfileDefinitionFromOldProfileDefinition(oldProfileDefinition):
        """ CreateNewProfileDefinitionFromOldProfileDefinition(oldProfileDefinition: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def CurrentInplaceEditLongTransactionId(selectedObjectIds):
        """ CurrentInplaceEditLongTransactionId(selectedObjectIds: ObjectIdCollection) -> ObjectId """
        pass

    @staticmethod
    def CurrentInplaceEditorId(selectedEntityId):
        """ CurrentInplaceEditorId(selectedEntityId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def DeleteInplaceEditorFromEntity(entity, inplaceEditorId):
        """ DeleteInplaceEditorFromEntity(entity: Entity, inplaceEditorId: ObjectId) """
        pass

    @staticmethod
    def EntityIdInInPlaceEditMode(db):
        """ EntityIdInInPlaceEditMode(db: Database) -> ObjectId """
        pass

    @staticmethod
    def FindParentEntityIdForInplaceEditEntityId(inplaceEditEntityId):
        """ FindParentEntityIdForInplaceEditEntityId(inplaceEditEntityId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def GetInplaceEditEntitiesInInPlaceEditMode(db):
        """ GetInplaceEditEntitiesInInPlaceEditMode(db: Database) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetInplaceEditorMap(db):
        """ GetInplaceEditorMap(db: Database) -> InplaceEditorMap """
        pass

    @staticmethod
    def HandledModifiedMessageFromInplaceEditEntity(fromObj, toEntity, messageId, allowedFromClass):
        """ HandledModifiedMessageFromInplaceEditEntity(fromObj: DBObject, toEntity: Entity, messageId: int, allowedFromClass: RXClass) """
        pass

    @staticmethod
    def HandleInplaceEditorMapOperation(entityId, inplaceEditorId, add):
        """ HandleInplaceEditorMapOperation(entityId: ObjectId, inplaceEditorId: ObjectId, add: bool) """
        pass

    @staticmethod
    def InplaceEditorIdInInPlaceEditMode(db):
        """ InplaceEditorIdInInPlaceEditMode(db: Database) -> ObjectId """
        pass

    @staticmethod
    def InvalidCommandInInPlaceEditMode(db, command, status):
        """ InvalidCommandInInPlaceEditMode(db: Database, command: str) -> (bool, CommandStatus) """
        pass

    @staticmethod
    def IsInplaceEditSessionInProgress(*__args):
        """
        IsInplaceEditSessionInProgress(selectedEntityId: ObjectId) -> bool
        IsInplaceEditSessionInProgress(db: Database) -> bool
        """
        pass

    @staticmethod
    def PurgeInplaceEditProfiles(db, profileIds):
        """ PurgeInplaceEditProfiles(db: Database, profileIds: ObjectIdCollection) """
        pass

    @staticmethod
    def RemoveEditorFromExtentionDictionary(objectToRemoveFrom, entryId):
        """ RemoveEditorFromExtentionDictionary(objectToRemoveFrom: DBObject, entryId: ObjectId) """
        pass

    @staticmethod
    def SelectionSetHasEntitiesFromInPlaceEditSession(selectedObjIds, inplaceEditEntities):
        """ SelectionSetHasEntitiesFromInPlaceEditSession(selectedObjIds: ObjectIdCollection, inplaceEditEntities: ObjectIdCollection) -> bool """
        pass

    @staticmethod
    def UpdateAnchoredObjectsForInplaceEditOperation(db, commandName):
        """ UpdateAnchoredObjectsForInplaceEditOperation(db: Database, commandName: str) -> bool """
        pass


class IOverrideOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IOverrideOperation, A_0: Override) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IOverrideOperation, A_0: int) -> Override """
        pass

    def GetCount(self):
        """ GetCount(self: IOverrideOperation) -> int """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IOverrideOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IOverrideOperation, A_0: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStringOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IStringOperation, A_0: str) -> int """
        pass

    def AddBatch(self, A_0):
        """ AddBatch(self: IStringOperation, A_0: StringCollection) """
        pass

    def Contains(self, A_0):
        """ Contains(self: IStringOperation, A_0: str) -> bool """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IStringOperation, A_0: int) -> str """
        pass

    def GetCount(self):
        """ GetCount(self: IStringOperation) -> int """
        pass

    def IndexOf(self, A_0):
        """ IndexOf(self: IStringOperation, A_0: str) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: IStringOperation, A_0: int, A_1: str) """
        pass

    def Remove(self, value):
        """ Remove(self: IStringOperation, value: str) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IStringOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IStringOperation, A_0: int) """
        pass

    def SetAt(self, A_0, A_1):
        """ SetAt(self: IStringOperation, A_0: int, A_1: str) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IStringPairOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IStringPairOperation, A_0: StringPair) -> int """
        pass

    def Contains(self, strLeft):
        """ Contains(self: IStringPairOperation, strLeft: str) -> bool """
        pass

    def Get(self, strLeft):
        """ Get(self: IStringPairOperation, strLeft: str) -> str """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IStringPairOperation, A_0: int) -> StringPair """
        pass

    def GetCount(self):
        """ GetCount(self: IStringPairOperation) -> int """
        pass

    def IndexOf(self, A_0):
        """ IndexOf(self: IStringPairOperation, A_0: StringPair) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: IStringPairOperation, A_0: int, A_1: StringPair) """
        pass

    def Remove(self, strLeft):
        """ Remove(self: IStringPairOperation, strLeft: str) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IStringPairOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IStringPairOperation, A_0: int) """
        pass

    def SetAt(self, A_0, A_1):
        """ SetAt(self: IStringPairOperation, A_0: int, A_1: StringPair) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LayerKeyDefinition(ImpObject):
    """ LayerKeyDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: LayerKeyDefinition) -> Color

Set: Color(self: LayerKeyDefinition) = value
"""

    IsPlottable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPlottable(self: LayerKeyDefinition) -> bool

Set: IsPlottable(self: LayerKeyDefinition) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Key(self: LayerKeyDefinition) -> str

Set: Key(self: LayerKeyDefinition) = value
"""

    LayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerName(self: LayerKeyDefinition) -> str

Set: LayerName(self: LayerKeyDefinition) = value
"""

    Linetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetype(self: LayerKeyDefinition) -> str

Set: Linetype(self: LayerKeyDefinition) = value
"""

    Lineweight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lineweight(self: LayerKeyDefinition) -> LineWeight

Set: Lineweight(self: LayerKeyDefinition) = value
"""

    Overrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Overrides(self: LayerKeyDefinition) -> ExtendedStringCollection

"""

    Plotstyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plotstyle(self: LayerKeyDefinition) -> str

Set: Plotstyle(self: LayerKeyDefinition) = value
"""

    Removable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Removable(self: LayerKeyDefinition) -> bool

"""



class LayerKeyDefinitionCollection(object):
    """ LayerKeyDefinitionCollection(pOp: ILayerKeyDefinitionOperation) """
    def Add(self, value):
        """ Add(self: LayerKeyDefinitionCollection, value: LayerKeyDefinition) -> int """
        pass

    def Clear(self):
        """ Clear(self: LayerKeyDefinitionCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: LayerKeyDefinitionCollection, value: LayerKeyDefinition) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: LayerKeyDefinitionCollection, array: Array[LayerKeyDefinition], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LayerKeyDefinitionCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: LayerKeyDefinitionCollection, value: LayerKeyDefinition) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: LayerKeyDefinitionCollection, index: int, value: LayerKeyDefinition) """
        pass

    def Remove(self, value):
        """ Remove(self: LayerKeyDefinitionCollection, value: LayerKeyDefinition) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: LayerKeyDefinitionCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: ILayerKeyDefinitionOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: LayerKeyDefinitionCollection) -> int

"""



class LayerKeyStyle(DictionaryRecord):
    """ LayerKeyStyle() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetOverrideAt(self, *__args):
        """
        GetOverrideAt(self: LayerKeyStyle, name: str, value: str) -> str
        GetOverrideAt(self: LayerKeyStyle, index: int, name: str, value: str) -> str
        """
        pass

    def OverrideExists(self, name):
        """ OverrideExists(self: LayerKeyStyle, name: str) -> bool """
        pass

    def SetOverrideAt(self, *__args):
        """ SetOverrideAt(self: LayerKeyStyle, name: str, value: str)SetOverrideAt(self: LayerKeyStyle, index: int, value: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    KeyDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyDefinitions(self: LayerKeyStyle) -> LayerKeyDefinitionCollection

"""

    OverrideCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverrideCount(self: LayerKeyStyle) -> int

"""

    OverridesEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OverridesEnabled(self: LayerKeyStyle) -> bool

Set: OverridesEnabled(self: LayerKeyStyle) = value
"""

    Standard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Standard(self: LayerKeyStyle) -> str

Set: Standard(self: LayerKeyStyle) = value
"""



class LayoutCurve(LayoutTool):
    """ LayoutCurve() """
    def AppendLayoutNode(self, position):
        """ AppendLayoutNode(self: LayoutCurve, position: float) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetLayoutCurveNode(self, id):
        """ GetLayoutCurveNode(self: LayoutCurve, id: int) -> LayoutCurveNode """
        pass

    def GetLayoutCurveNodeAt(self, index):
        """ GetLayoutCurveNodeAt(self: LayoutCurve, index: int) -> LayoutCurveNode """
        pass

    def GetNodePositionAt(self, index):
        """ GetNodePositionAt(self: LayoutCurve, index: int) -> float """
        pass

    def MoveLayoutNode(self, oldParameter, newParameter):
        """ MoveLayoutNode(self: LayoutCurve, oldParameter: float, newParameter: float) """
        pass

    def RemoveLayoutNode(self, id):
        """ RemoveLayoutNode(self: LayoutCurve, id: int) """
        pass

    def RemoveLayoutNodeAt(self, index):
        """ RemoveLayoutNodeAt(self: LayoutCurve, index: int) """
        pass

    def SetLayoutNodeLocation(self, node, location):
        """ SetLayoutNodeLocation(self: LayoutCurve, node: LayoutCurveNode, location: Point3d) """
        pass

    def UpdateParameters(self):
        """ UpdateParameters(self: LayoutCurve) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CurveId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveId(self: LayoutCurve) -> ObjectId

Set: CurveId(self: LayoutCurve) = value
"""

    EndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffset(self: LayoutCurve) -> float

Set: EndOffset(self: LayoutCurve) = value
"""

    LayoutMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutMode(self: LayoutCurve) -> LayoutModeType

Set: LayoutMode(self: LayoutCurve) = value
"""

    NodeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeCount(self: LayoutCurve) -> int

"""

    NodePositions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodePositions(self: LayoutCurve) -> DoubleCollection

"""

    Spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spacing(self: LayoutCurve) -> float

Set: Spacing(self: LayoutCurve) = value
"""

    StartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffset(self: LayoutCurve) -> float

Set: StartOffset(self: LayoutCurve) = value
"""



class LayoutCurveNode(LayoutNode):
    """ LayoutCurveNode() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    UPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UPosition(self: LayoutCurveNode) -> float

Set: UPosition(self: LayoutCurveNode) = value
"""



class LayoutGrid2d(CellLayoutTool):
    """ LayoutGrid2d() """
    def AppendBoundaryHole(self, id):
        """ AppendBoundaryHole(self: LayoutGrid2d, id: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def OppositeLayoutNode(self, nodeId, angleOffset, oppositeNodeId, oppositeAngleOffset):
        """ OppositeLayoutNode(self: LayoutGrid2d, nodeId: int, angleOffset: float) -> (bool, int, float) """
        pass

    def RemoveBoundaryHole(self, id):
        """ RemoveBoundaryHole(self: LayoutGrid2d, id: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BaseGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseGrid(self: LayoutGrid2d) -> GridUv

"""

    BoundaryHoles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryHoles(self: LayoutGrid2d) -> ObjectIdCollection

"""

    BoundaryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryId(self: LayoutGrid2d) -> ObjectId

Set: BoundaryId(self: LayoutGrid2d) = value
"""

    BoundaryProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryProfile(self: LayoutGrid2d) -> Profile

"""

    CustomGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomGrid(self: LayoutGrid2d) -> GridCustom

"""

    GridType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridType(self: LayoutGrid2d) -> GridType

Set: GridType(self: LayoutGrid2d) = value
"""



class LayoutGrid2dCell(LayoutCell):
    """ LayoutGrid2dCell() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    UIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UIndex(self: LayoutGrid2dCell) -> int

Set: UIndex(self: LayoutGrid2dCell) = value
"""

    VIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VIndex(self: LayoutGrid2dCell) -> int

Set: VIndex(self: LayoutGrid2dCell) = value
"""



class LayoutGrid2dNode(LayoutCurveNode):
    """ LayoutGrid2dNode() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    VPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VPosition(self: LayoutGrid2dNode) -> float

Set: VPosition(self: LayoutGrid2dNode) = value
"""



class VolumeLayoutTool(CellLayoutTool):
    """ VolumeLayoutTool() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetClosestLayoutVolume(self, location):
        """ GetClosestLayoutVolume(self: VolumeLayoutTool, location: Point3d) -> int """
        pass

    def GetLayoutVolumeBody(self, volumeId, toWcs):
        """ GetLayoutVolumeBody(self: VolumeLayoutTool, volumeId: int) -> (Body, Matrix3d) """
        pass

    def GetLayoutVolumeCentroid(self, volumeId):
        """ GetLayoutVolumeCentroid(self: VolumeLayoutTool, volumeId: int) -> Matrix3d """
        pass

    def GetLayoutVolumeExtent(self, volumeId, length, width, height, toWcs):
        """ GetLayoutVolumeExtent(self: VolumeLayoutTool, volumeId: int) -> (float, float, float, Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    LayoutVolumeIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutVolumeIds(self: VolumeLayoutTool) -> IntegerCollection

"""



class LayoutGrid3d(VolumeLayoutTool):
    """ LayoutGrid3d() """
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

    BaseGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseGrid(self: LayoutGrid3d) -> GridUvw

"""

    GridType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridType(self: LayoutGrid3d) -> GridType

Set: GridType(self: LayoutGrid3d) = value
"""



class LayoutGrid3dCell(LayoutGrid2dCell):
    """ LayoutGrid3dCell() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: LayoutGrid3dCell) -> PlaneType

Set: Plane(self: LayoutGrid3dCell) = value
"""

    WIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WIndex(self: LayoutGrid3dCell) -> int

Set: WIndex(self: LayoutGrid3dCell) = value
"""



class LayoutGrid3dNode(LayoutGrid2dNode):
    """ LayoutGrid3dNode() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    WPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WPosition(self: LayoutGrid3dNode) -> float

Set: WPosition(self: LayoutGrid3dNode) = value
"""



class LayoutVolume(ImpObject):
    """ LayoutVolume() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    VolumeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VolumeId(self: LayoutVolume) -> int

Set: VolumeId(self: LayoutVolume) = value
"""



class LayoutGrid3dVolume(LayoutVolume):
    """ LayoutGrid3dVolume() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    UIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UIndex(self: LayoutGrid3dVolume) -> int

Set: UIndex(self: LayoutGrid3dVolume) = value
"""

    VIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VIndex(self: LayoutGrid3dVolume) -> int

Set: VIndex(self: LayoutGrid3dVolume) = value
"""

    WIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WIndex(self: LayoutGrid3dVolume) -> int

Set: WIndex(self: LayoutGrid3dVolume) = value
"""



class LayoutModeType(Enum):
    """ enum LayoutModeType, values: Manual (0), Repeat (1), SpaceOut (2) """
    Manual = None
    Repeat = None
    SpaceOut = None
    value__ = None


class LinearUnit(Enum):
    """ enum LinearUnit, values: Architectural (4), CurrentLU (-1), Decimal (2), Engineering (3), Fractional (5), Scientific (1) """
    Architectural = None
    CurrentLU = None
    Decimal = None
    Engineering = None
    Fractional = None
    Scientific = None
    value__ = None


class LineWorkComponent(ImpObject):
    """ LineWorkComponent() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: LineWorkComponent) -> str

Set: Description(self: LineWorkComponent) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: LineWorkComponent) -> Int16

Set: Id(self: LineWorkComponent) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: LineWorkComponent) -> str

Set: Name(self: LineWorkComponent) = value
"""



class LineWorkComponentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: LineWorkComponentCollection, value: LineWorkComponent) -> int """
        pass

    def Clear(self):
        """ Clear(self: LineWorkComponentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: LineWorkComponentCollection, value: LineWorkComponent) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: LineWorkComponentCollection, array: Array[LineWorkComponent], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LineWorkComponentCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: LineWorkComponentCollection, value: LineWorkComponent) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: LineWorkComponentCollection, index: int, value: LineWorkComponent) """
        pass

    def Remove(self, value):
        """ Remove(self: LineWorkComponentCollection, value: LineWorkComponent) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: LineWorkComponentCollection, index: int) """
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
    """Get: Count(self: LineWorkComponentCollection) -> int

"""



class LineWorkRule(ImpObject):
    """ LineWorkRule() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: LineWorkRule) -> Color

Set: Color(self: LineWorkRule) = value
"""

    ComponentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentId(self: LineWorkRule) -> Int16

Set: ComponentId(self: LineWorkRule) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: LineWorkRule) -> str

Set: Description(self: LineWorkRule) = value
"""

    FilterFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterFlags(self: LineWorkRule) -> int

Set: FilterFlags(self: LineWorkRule) = value
"""



class LineWorkRuleCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: LineWorkRuleCollection, value: LineWorkRule) -> int """
        pass

    def Clear(self):
        """ Clear(self: LineWorkRuleCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: LineWorkRuleCollection, value: LineWorkRule) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: LineWorkRuleCollection, array: Array[LineWorkRule], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LineWorkRuleCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: LineWorkRuleCollection, value: LineWorkRule) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: LineWorkRuleCollection, index: int, value: LineWorkRule) """
        pass

    def Remove(self, value):
        """ Remove(self: LineWorkRuleCollection, value: LineWorkRule) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: LineWorkRuleCollection, index: int) """
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
    """Get: Count(self: LineWorkRuleCollection) -> int

"""



class LineWorkType(Enum):
    """ enum LineWorkType, values: LineWork (0), SectionHatching (2), SurfaceHatching (1) """
    LineWork = None
    SectionHatching = None
    SurfaceHatching = None
    value__ = None


class ListDefinition(ClassificationDefinition):
    """ ListDefinition() """
    def AddListItem(self, name):
        """ AddListItem(self: ListDefinition, name: str) -> ObjectId """
        pass

    def DeleteListItem(self, id):
        """ DeleteListItem(self: ListDefinition, id: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetListItem(self, name):
        """ GetListItem(self: ListDefinition, name: str) -> ObjectId """
        pass

    def GetListItems(self):
        """ GetListItems(self: ListDefinition) -> ObjectIdCollection """
        pass

    def RenameList(self, listId, newName):
        """ RenameList(self: ListDefinition, listId: ObjectId, newName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AllowToVary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowToVary(self: ListDefinition) -> bool

Set: AllowToVary(self: ListDefinition) = value
"""



class Listener(DisposableWrapper):
    # no doc
    def addClassNotToNotify(self, type):
        """ addClassNotToNotify(self: Listener, type: RXClass) """
        pass

    def addClassParam(self, *__args):
        """ addClassParam(self: Listener, type: RXClass, paramId: int)addClassParam(self: Listener, paramId: int, type: RXClass) """
        pass

    def addClassToNotify(self, type):
        """ addClassToNotify(self: Listener, type: RXClass) """
        pass

    def allowByClass(self, type):
        """ allowByClass(self: Listener, type: RXClass) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def objectAppended(self, pObjAppended):
        """ objectAppended(self: Listener, pObjAppended: DBObject) """
        pass

    def objectErased(self, pObjErased):
        """ objectErased(self: Listener, pObjErased: DBObject) """
        pass

    def objectModified(self, pObj):
        """ objectModified(self: Listener, pObj: DBObject) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, sendObjectAppendedAndErasedNotifications: bool)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: Listener) -> bool

Set: Enabled(self: Listener) = value
"""



class ListItem(Classification):
    """ ListItem() """
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


class MaskBlockDefinition(DictionaryRecord):
    """ MaskBlockDefinition() """
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

    CutProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutProfile(self: MaskBlockDefinition) -> Profile

Set: CutProfile(self: MaskBlockDefinition) = value
"""

    ExtraGraphicsBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtraGraphicsBlockId(self: MaskBlockDefinition) -> ObjectId

Set: ExtraGraphicsBlockId(self: MaskBlockDefinition) = value
"""



class MaskBlockReference(BlockReference):
    """ MaskBlockReference() """
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

    CutProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutProfile(self: MaskBlockReference) -> Profile

"""



class MassElement(Geo):
    """ MassElement() """
    def ChangeTo(self, type, *__args):
        """ ChangeTo(self: MassElement, type: ShapeType)ChangeTo(self: MassElement, type: ShapeType, profileId: ObjectId)ChangeTo(self: MassElement, type: ShapeType, profile: Profile) """
        pass

    @staticmethod
    def Create(type, *__args):
        """
        Create(type: ShapeType) -> MassElement
        Create(type: ShapeType, profileId: ObjectId) -> MassElement
        Create(type: ShapeType, profile: Profile) -> MassElement
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetMaterialId(self, component, wasOverridden):
        """ GetMaterialId(self: MassElement, component: int) -> (ObjectId, bool) """
        pass

    def ParentMassing(self, id, operation):
        """ ParentMassing(self: MassElement) -> (ObjectId, Operation) """
        pass

    def SetBody(self, body, centerToLcs):
        """ SetBody(self: MassElement, body: Body, centerToLcs: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: MassElement) -> Body

"""

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: MassElement) -> float

Set: Depth(self: MassElement) = value
"""

    Deviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Deviation(self: MassElement) -> float

Set: Deviation(self: MassElement) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: MassElement) -> float

Set: Height(self: MassElement) = value
"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile(self: MassElement) -> Profile

Set: Profile(self: MassElement) = value
"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: MassElement) -> ObjectId

Set: ProfileId(self: MassElement) = value
"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: MassElement) -> float

Set: Radius(self: MassElement) = value
"""

    Rise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rise(self: MassElement) -> float

Set: Rise(self: MassElement) = value
"""

    ShapeSubType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeSubType(self: MassElement) -> ShapeSubType

"""

    ShapeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeType(self: MassElement) -> ShapeType

"""

    SubType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubType(self: MassElement) -> str

Set: SubType(self: MassElement) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: MassElement) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: MassElement) -> float

Set: Width(self: MassElement) = value
"""



class MassElementStyle(DictionaryRecord):
    """ MassElementStyle() """
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

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: MassElementStyle) -> ObjectId

Set: MaterialId(self: MassElementStyle) = value
"""



class MassGroup(Geo):
    """ MassGroup() """
    def AddNode(self, entity, operation):
        """ AddNode(self: MassGroup, entity: Entity, operation: Operation) """
        pass

    def Contains(self, id, operation, recursive):
        """ Contains(self: MassGroup, id: ObjectId, recursive: bool) -> (bool, Operation) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetMaterialId(self, componentId):
        """ GetMaterialId(self: MassGroup, componentId: int) -> ObjectId """
        pass

    def GetOperation(self, id):
        """ GetOperation(self: MassGroup, id: ObjectId) -> Operation """
        pass

    @staticmethod
    def GetSupportsAnchoring(massGroupId):
        """ GetSupportsAnchoring(massGroupId: ObjectId) -> bool """
        pass

    def MoveNodeToAfter(self, id, afterId):
        """ MoveNodeToAfter(self: MassGroup, id: ObjectId, afterId: ObjectId) """
        pass

    def MoveNodeToBefore(self, id, beforeId):
        """ MoveNodeToBefore(self: MassGroup, id: ObjectId, beforeId: ObjectId) """
        pass

    def MoveNodeToBeginning(self, id):
        """ MoveNodeToBeginning(self: MassGroup, id: ObjectId) """
        pass

    def MoveNodeToEnd(self, id):
        """ MoveNodeToEnd(self: MassGroup, id: ObjectId) """
        pass

    def ParentMassing(self, operation):
        """ ParentMassing(self: MassGroup) -> (ObjectId, Operation) """
        pass

    def RemoveAllNodes(self):
        """ RemoveAllNodes(self: MassGroup) """
        pass

    def RemoveNode(self, entity):
        """ RemoveNode(self: MassGroup, entity: Entity) """
        pass

    def SaveBody(self, filename):
        """ SaveBody(self: MassGroup, filename: str) """
        pass

    def SetOperation(self, id, operation):
        """ SetOperation(self: MassGroup, id: ObjectId, operation: Operation) """
        pass

    @staticmethod
    def SetSupportsAnchoring(massGroupId, supports):
        """ SetSupportsAnchoring(massGroupId: ObjectId, supports: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Body(self: MassGroup) -> Body

"""

    Entities = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entities(self: MassGroup) -> ObjectIdCollection

"""

    NodeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeCount(self: MassGroup) -> int

"""

    Nodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nodes(self: MassGroup) -> ObjectIdCollection

"""

    RootNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RootNode(self: MassGroup) -> ObjectId

"""

    SubType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubType(self: MassGroup) -> str

Set: SubType(self: MassGroup) = value
"""

    SupportsAnchoring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsAnchoring(self: MassGroup) -> bool

Set: SupportsAnchoring(self: MassGroup) = value
"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: MassGroup) -> float

"""



class MaterialDefinition(DictionaryRecord):
    """ MaterialDefinition() """
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


class MaterialInformation(DisplayMaterialInformation):
    """
    MaterialInformation(materialId: ObjectId, componentName: str, locationId: int, locationStyleId: ObjectId, componentId: Int16, isFromObjectOverride: bool)
    MaterialInformation()
    """
    def CopyTo(self, information):
        """ CopyTo(self: MaterialInformation, information: MaterialInformation) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, materialId=None, componentName=None, locationId=None, locationStyleId=None, componentId=None, isFromObjectOverride=None):
        """
        __new__(cls: type, materialId: ObjectId, componentName: str, locationId: int, locationStyleId: ObjectId, componentId: Int16, isFromObjectOverride: bool)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ComponentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentName(self: MaterialInformation) -> str

Set: ComponentName(self: MaterialInformation) = value
"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: MaterialInformation) -> ObjectId

Set: MaterialId(self: MaterialInformation) = value
"""



class MaterialInformationLocation(Enum):
    """ enum MaterialInformationLocation, values: MaterialFromObject (0), MaterialFromObjectOverride (2), MaterialFromStyle (1) """
    MaterialFromObject = None
    MaterialFromObjectOverride = None
    MaterialFromStyle = None
    value__ = None


class MaterialUtility(object):
    # no doc
    @staticmethod
    def GetMaterialOverrides(entity, locationIds, materialIdArray):
        """ GetMaterialOverrides(entity: Entity) -> (IntegerCollection, ObjectIdCollection) """
        pass

    @staticmethod
    def GetResolvedMaterials(entity):
        """ GetResolvedMaterials(entity: Entity) -> ResolvedMaterialCollection """
        pass


class MultiViewBlockAttributeReference(ImpObject):
    """
    MultiViewBlockAttributeReference(prompt: str, att: AttributeReference)
    MultiViewBlockAttributeReference()
    """
    def CopyToMText(self):
        """ CopyToMText(self: MultiViewBlockAttributeReference) """
        pass

    def DeleteMText(self):
        """ DeleteMText(self: MultiViewBlockAttributeReference) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, prompt=None, att=None):
        """
        __new__(cls: type, prompt: str, att: AttributeReference)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attribute(self: MultiViewBlockAttributeReference) -> AttributeReference

Set: Attribute(self: MultiViewBlockAttributeReference) = value
"""

    MText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MText(self: MultiViewBlockAttributeReference) -> MText

"""

    NeedsUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedsUpdate(self: MultiViewBlockAttributeReference) -> bool

Set: NeedsUpdate(self: MultiViewBlockAttributeReference) = value
"""

    Prompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prompt(self: MultiViewBlockAttributeReference) -> str

Set: Prompt(self: MultiViewBlockAttributeReference) = value
"""



class MultiViewBlockAttributeReferenceCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: MultiViewBlockAttributeReferenceCollection, item: MultiViewBlockAttributeReference) -> int """
        pass

    def Clear(self):
        """ Clear(self: MultiViewBlockAttributeReferenceCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: MultiViewBlockAttributeReferenceCollection, item: MultiViewBlockAttributeReference) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: MultiViewBlockAttributeReferenceCollection, array: Array[MultiViewBlockAttributeReference], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MultiViewBlockAttributeReferenceCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: MultiViewBlockAttributeReferenceCollection, item: MultiViewBlockAttributeReference) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: MultiViewBlockAttributeReferenceCollection, index: int, item: MultiViewBlockAttributeReference) """
        pass

    def Remove(self, item):
        """ Remove(self: MultiViewBlockAttributeReferenceCollection, item: MultiViewBlockAttributeReference) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MultiViewBlockAttributeReferenceCollection, index: int) """
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
    """Get: Count(self: MultiViewBlockAttributeReferenceCollection) -> int

"""



class MultiViewBlockDefinition(DictionaryRecord):
    """ MultiViewBlockDefinition() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAllBlocksReferenced(self):
        """ GetAllBlocksReferenced(self: MultiViewBlockDefinition) -> ObjectIdCollection """
        pass

    def SetAttributeGripsDisabled(self, disable):
        """ SetAttributeGripsDisabled(self: MultiViewBlockDefinition, disable: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayRepresentationDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationDefinitions(self: MultiViewBlockDefinition) -> MultiViewBlockDisplayRepresentationDefinitionCollection

"""

    InterferenceBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterferenceBlockId(self: MultiViewBlockDefinition) -> ObjectId

Set: InterferenceBlockId(self: MultiViewBlockDefinition) = value
"""



class MultiViewBlockDisplayRepresentationDefinition(ImpObject):
    """ MultiViewBlockDisplayRepresentationDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetAttributeGripsDisabled(self, disable):
        """ SetAttributeGripsDisabled(self: MultiViewBlockDisplayRepresentationDefinition, disable: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayRepresentationId(self: MultiViewBlockDisplayRepresentationDefinition) -> ObjectId

Set: DisplayRepresentationId(self: MultiViewBlockDisplayRepresentationDefinition) = value
"""

    ViewDefinitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewDefinitions(self: MultiViewBlockDisplayRepresentationDefinition) -> MultiViewBlockViewDefinitionCollection

"""



class MultiViewBlockDisplayRepresentationDefinitionCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: MultiViewBlockDisplayRepresentationDefinitionCollection, item: MultiViewBlockDisplayRepresentationDefinition) -> int """
        pass

    def Clear(self):
        """ Clear(self: MultiViewBlockDisplayRepresentationDefinitionCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: MultiViewBlockDisplayRepresentationDefinitionCollection, item: MultiViewBlockDisplayRepresentationDefinition) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: MultiViewBlockDisplayRepresentationDefinitionCollection, array: Array[MultiViewBlockDisplayRepresentationDefinition], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MultiViewBlockDisplayRepresentationDefinitionCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: MultiViewBlockDisplayRepresentationDefinitionCollection, item: MultiViewBlockDisplayRepresentationDefinition) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: MultiViewBlockDisplayRepresentationDefinitionCollection, index: int, item: MultiViewBlockDisplayRepresentationDefinition) """
        pass

    def Remove(self, item):
        """ Remove(self: MultiViewBlockDisplayRepresentationDefinitionCollection, item: MultiViewBlockDisplayRepresentationDefinition) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MultiViewBlockDisplayRepresentationDefinitionCollection, index: int) """
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
    """Get: Count(self: MultiViewBlockDisplayRepresentationDefinitionCollection) -> int

"""



class MultiViewBlockReference(BlockReference):
    """ MultiViewBlockReference() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def UpdateAnnotative(self):
        """ UpdateAnnotative(self: MultiViewBlockReference) -> bool """
        pass

    def UpdateViewInstances(self):
        """ UpdateViewInstances(self: MultiViewBlockReference) """
        pass

    def UpdateViewInstancesAttributes(self, includeTextStyle):
        """ UpdateViewInstancesAttributes(self: MultiViewBlockReference, includeTextStyle: bool) """
        pass

    def UpdateViewInstancesAttributesIncludeWidth(self, includeTextStyle):
        """ UpdateViewInstancesAttributesIncludeWidth(self: MultiViewBlockReference, includeTextStyle: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AnnotationScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnnotationScale(self: MultiViewBlockReference) -> AnnotationScale

"""

    AnnotationScaleUniqueIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnnotationScaleUniqueIdentifier(self: MultiViewBlockReference) -> IntPtr

"""

    HasAttributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasAttributes(self: MultiViewBlockReference) -> bool

"""

    NumberOfAnnotationScaleContexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfAnnotationScaleContexts(self: MultiViewBlockReference) -> int

"""

    ScaleDependentOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleDependentOffset(self: MultiViewBlockReference) -> Vector3d

Set: ScaleDependentOffset(self: MultiViewBlockReference) = value
"""

    ViewInstances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewInstances(self: MultiViewBlockReference) -> MultiViewBlockViewInstanceCollection

"""



class MultiViewBlockViewDefinition(ImpObject):
    """ MultiViewBlockViewDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IsViewOn(self, viewDirectionType):
        """ IsViewOn(self: MultiViewBlockViewDefinition, viewDirectionType: ViewDirection) -> bool """
        pass

    def SetAllViews(self, isOn):
        """ SetAllViews(self: MultiViewBlockViewDefinition, isOn: bool) """
        pass

    def SetViewOn(self, viewDirectionType, isOn):
        """ SetViewOn(self: MultiViewBlockViewDefinition, viewDirectionType: ViewDirection, isOn: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AttributeGripsDisabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeGripsDisabled(self: MultiViewBlockViewDefinition) -> bool

Set: AttributeGripsDisabled(self: MultiViewBlockViewDefinition) = value
"""

    BlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockId(self: MultiViewBlockViewDefinition) -> ObjectId

Set: BlockId(self: MultiViewBlockViewDefinition) = value
"""



class MultiViewBlockViewDefinitionCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: MultiViewBlockViewDefinitionCollection, item: MultiViewBlockViewDefinition) -> int """
        pass

    def Clear(self):
        """ Clear(self: MultiViewBlockViewDefinitionCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: MultiViewBlockViewDefinitionCollection, item: MultiViewBlockViewDefinition) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: MultiViewBlockViewDefinitionCollection, array: Array[MultiViewBlockViewDefinition], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MultiViewBlockViewDefinitionCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: MultiViewBlockViewDefinitionCollection, item: MultiViewBlockViewDefinition) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: MultiViewBlockViewDefinitionCollection, index: int, item: MultiViewBlockViewDefinition) """
        pass

    def Remove(self, item):
        """ Remove(self: MultiViewBlockViewDefinitionCollection, item: MultiViewBlockViewDefinition) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MultiViewBlockViewDefinitionCollection, index: int) """
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
    """Get: Count(self: MultiViewBlockViewDefinitionCollection) -> int

"""



class MultiViewBlockViewInstance(ImpObject):
    """ MultiViewBlockViewInstance() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EnsureConsistentAttributes(self):
        """ EnsureConsistentAttributes(self: MultiViewBlockViewInstance) """
        pass

    def EnsureConsistentAttributesAndUpdateExisting(self, includeTextStyle):
        """ EnsureConsistentAttributesAndUpdateExisting(self: MultiViewBlockViewInstance, includeTextStyle: bool) """
        pass

    def EnsureConsistentAttributesAndUpdateExistingIncludeWidth(self, includeTextStyle):
        """ EnsureConsistentAttributesAndUpdateExistingIncludeWidth(self: MultiViewBlockViewInstance, includeTextStyle: bool) """
        pass

    def NeedsAttributeUpdateFullCheck(self, includeTextStyle):
        """ NeedsAttributeUpdateFullCheck(self: MultiViewBlockViewInstance, includeTextStyle: bool) -> bool """
        pass

    def NeedsAttributeUpdateFullCheckIncludeWidth(self, includeTextStyle):
        """ NeedsAttributeUpdateFullCheckIncludeWidth(self: MultiViewBlockViewInstance, includeTextStyle: bool) -> bool """
        pass

    def ResetAttributes(self, blockId):
        """ ResetAttributes(self: MultiViewBlockViewInstance, blockId: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AttributeReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeReferences(self: MultiViewBlockViewInstance) -> MultiViewBlockAttributeReferenceCollection

"""

    BlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockId(self: MultiViewBlockViewInstance) -> ObjectId

Set: BlockId(self: MultiViewBlockViewInstance) = value
"""

    NeedsAttributeUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NeedsAttributeUpdate(self: MultiViewBlockViewInstance) -> bool

"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: MultiViewBlockViewInstance) -> Vector3d

Set: Offset(self: MultiViewBlockViewInstance) = value
"""



class MultiViewBlockViewInstanceCollection(object):
    # no doc
    def CopyTo(self, array, start):
        """ CopyTo(self: MultiViewBlockViewInstanceCollection, array: Array[MultiViewBlockViewInstance], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MultiViewBlockViewInstanceCollection) -> IEnumerator """
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
    """Get: Count(self: MultiViewBlockViewInstanceCollection) -> int

"""



class NameObjectIdPair(object):
    """
    NameObjectIdPair(name: str, objectId: ObjectId)
    NameObjectIdPair()
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None, objectId=None):
        """
        __new__(cls: type, name: str, objectId: ObjectId)
        __new__(cls: type)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NameObjectIdPair) -> str

Set: Name(self: NameObjectIdPair) = value
"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: NameObjectIdPair) -> ObjectId

Set: ObjectId(self: NameObjectIdPair) = value
"""



class NameObjectIdPairCollection(DisposableWrapper):
    """
    NameObjectIdPairCollection(caseSensitive: bool)
    NameObjectIdPairCollection()
    """
    def Add(self, value):
        """ Add(self: NameObjectIdPairCollection, value: NameObjectIdPair) -> int """
        pass

    def AddAlpha(self, value):
        """ AddAlpha(self: NameObjectIdPairCollection, value: NameObjectIdPair) -> int """
        pass

    def AddHead(self, value):
        """ AddHead(self: NameObjectIdPairCollection, value: NameObjectIdPair) -> int """
        pass

    def Clear(self):
        """ Clear(self: NameObjectIdPairCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NameObjectIdPairCollection, value: NameObjectIdPair) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NameObjectIdPairCollection, array: Array[NameObjectIdPair], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NameObjectIdPairCollection) -> IEnumerator """
        pass

    def GetMatchFor(self, objectId):
        """ GetMatchFor(self: NameObjectIdPairCollection, objectId: ObjectId) -> str """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: NameObjectIdPairCollection, value: NameObjectIdPair) -> int
        IndexOf(self: NameObjectIdPairCollection, name: str) -> int
        IndexOf(self: NameObjectIdPairCollection, objectId: ObjectId) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: NameObjectIdPairCollection, index: int, value: NameObjectIdPair) """
        pass

    def Remove(self, value):
        """ Remove(self: NameObjectIdPairCollection, value: NameObjectIdPair) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NameObjectIdPairCollection, index: int) """
        pass

    def RemoveHead(self):
        """ RemoveHead(self: NameObjectIdPairCollection) """
        pass

    def RemoveTail(self):
        """ RemoveTail(self: NameObjectIdPairCollection) """
        pass

    def Rename(self, oldName, newName):
        """ Rename(self: NameObjectIdPairCollection, oldName: str, newName: str) -> bool """
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
    def __new__(self, caseSensitive=None):
        """
        __new__(cls: type, caseSensitive: bool)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: NameObjectIdPairCollection) -> int

"""



class NestedGridBoundaryEdgeAssignmentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridBoundaryEdgeAssignmentCollection, value: NestedGridEdgeAssignment) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridBoundaryEdgeAssignmentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridBoundaryEdgeAssignmentCollection, value: NestedGridEdgeAssignment) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridBoundaryEdgeAssignmentCollection, array: Array[NestedGridEdgeAssignment], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridBoundaryEdgeAssignmentCollection) -> IEnumerator """
        pass

    def GetId(self, id):
        """ GetId(self: NestedGridBoundaryEdgeAssignmentCollection, id: Int16) -> NestedGridEdgeAssignment """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridBoundaryEdgeAssignmentCollection, value: NestedGridEdgeAssignment) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridBoundaryEdgeAssignmentCollection, index: int, value: NestedGridEdgeAssignment) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridBoundaryEdgeAssignmentCollection, value: NestedGridEdgeAssignment) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridBoundaryEdgeAssignmentCollection, index: int) """
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
    """Get: Count(self: NestedGridBoundaryEdgeAssignmentCollection) -> int

"""

    Default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Default(self: NestedGridBoundaryEdgeAssignmentCollection) -> NestedGridEdgeAssignment

Set: Default(self: NestedGridBoundaryEdgeAssignmentCollection) = value
"""



class NestedGridBoundaryEdgeComponentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridBoundaryEdgeComponentCollection, value: NestedGridEdgeDefinition) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridBoundaryEdgeComponentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridBoundaryEdgeComponentCollection, value: NestedGridEdgeDefinition) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridBoundaryEdgeComponentCollection, array: Array[NestedGridEdgeDefinition], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridBoundaryEdgeComponentCollection) -> IEnumerator """
        pass

    def GetId(self, id):
        """ GetId(self: NestedGridBoundaryEdgeComponentCollection, id: Int16) -> NestedGridEdgeDefinition """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridBoundaryEdgeComponentCollection, value: NestedGridEdgeDefinition) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridBoundaryEdgeComponentCollection, index: int, value: NestedGridEdgeDefinition) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridBoundaryEdgeComponentCollection, value: NestedGridEdgeDefinition) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridBoundaryEdgeComponentCollection, index: int) """
        pass

    def RemoveId(self, id):
        """ RemoveId(self: NestedGridBoundaryEdgeComponentCollection, id: Int16) """
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
    """Get: Count(self: NestedGridBoundaryEdgeComponentCollection) -> int

"""



class NestedGridCellAssignment(ImpObject):
    """ NestedGridCellAssignment() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetVoid(self):
        """ SetVoid(self: NestedGridCellAssignment) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellSpecifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellSpecifier(self: NestedGridCellAssignment) -> IndexSpecifier

Set: CellSpecifier(self: NestedGridCellAssignment) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: NestedGridCellAssignment) -> Int16

Set: Id(self: NestedGridCellAssignment) = value
"""

    InfillDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InfillDefinitionId(self: NestedGridCellAssignment) -> Int16

Set: InfillDefinitionId(self: NestedGridCellAssignment) = value
"""

    IsVoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVoid(self: NestedGridCellAssignment) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NestedGridCellAssignment) -> str

Set: Name(self: NestedGridCellAssignment) = value
"""

    NestedGridDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedGridDefinition(self: NestedGridCellAssignment) -> NestedGridDefinition

Set: NestedGridDefinition(self: NestedGridCellAssignment) = value
"""

    ParentGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentGrid(self: NestedGridCellAssignment) -> GridAssemblyDefinition

"""



class NestedGridCellAssignmentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridCellAssignmentCollection, value: NestedGridCellAssignment) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridCellAssignmentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridCellAssignmentCollection, value: NestedGridCellAssignment) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridCellAssignmentCollection, array: Array[NestedGridCellAssignment], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridCellAssignmentCollection) -> IEnumerator """
        pass

    def GetId(self, id):
        """ GetId(self: NestedGridCellAssignmentCollection, id: Int16) -> NestedGridCellAssignment """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridCellAssignmentCollection, value: NestedGridCellAssignment) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridCellAssignmentCollection, index: int, value: NestedGridCellAssignment) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridCellAssignmentCollection, value: NestedGridCellAssignment) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridCellAssignmentCollection, index: int) """
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
    """Get: Count(self: NestedGridCellAssignmentCollection) -> int

"""

    Default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Default(self: NestedGridCellAssignmentCollection) -> NestedGridCellAssignment

Set: Default(self: NestedGridCellAssignmentCollection) = value
"""



class NestedGridCellMergeData(ImpObject):
    """ NestedGridCellMergeData() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    IsStyleBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStyleBased(self: NestedGridCellMergeData) -> bool

Set: IsStyleBased(self: NestedGridCellMergeData) = value
"""

    PrimaryCellPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryCellPath(self: NestedGridCellMergeData) -> IntegerCollection

Set: PrimaryCellPath(self: NestedGridCellMergeData) = value
"""

    SecondaryCellPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryCellPath(self: NestedGridCellMergeData) -> IntegerCollection

Set: SecondaryCellPath(self: NestedGridCellMergeData) = value
"""



class NestedGridCellMergeDataCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridCellMergeDataCollection, value: NestedGridCellMergeData) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridCellMergeDataCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridCellMergeDataCollection, value: NestedGridCellMergeData) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridCellMergeDataCollection, array: Array[NestedGridCellMergeData], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridCellMergeDataCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridCellMergeDataCollection, value: NestedGridCellMergeData) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridCellMergeDataCollection, index: int, value: NestedGridCellMergeData) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridCellMergeDataCollection, value: NestedGridCellMergeData) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridCellMergeDataCollection, index: int) """
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
    """Get: Count(self: NestedGridCellMergeDataCollection) -> int

"""



class NestedGridCellOverride(ImpObject):
    """ NestedGridCellOverride() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetVoid(self):
        """ SetVoid(self: NestedGridCellOverride) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellPath(self: NestedGridCellOverride) -> IntegerCollection

Set: CellPath(self: NestedGridCellOverride) = value
"""

    FrameRemovedBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRemovedBottom(self: NestedGridCellOverride) -> bool

Set: FrameRemovedBottom(self: NestedGridCellOverride) = value
"""

    FrameRemovedLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRemovedLeft(self: NestedGridCellOverride) -> bool

Set: FrameRemovedLeft(self: NestedGridCellOverride) = value
"""

    FrameRemovedRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRemovedRight(self: NestedGridCellOverride) -> bool

Set: FrameRemovedRight(self: NestedGridCellOverride) = value
"""

    FrameRemovedTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrameRemovedTop(self: NestedGridCellOverride) -> bool

Set: FrameRemovedTop(self: NestedGridCellOverride) = value
"""

    InfillDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InfillDefinitionId(self: NestedGridCellOverride) -> Int16

Set: InfillDefinitionId(self: NestedGridCellOverride) = value
"""

    IsStyleBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStyleBased(self: NestedGridCellOverride) -> bool

Set: IsStyleBased(self: NestedGridCellOverride) = value
"""

    IsVoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVoid(self: NestedGridCellOverride) -> bool

"""



class NestedGridCellOverrideCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridCellOverrideCollection, value: NestedGridCellOverride) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridCellOverrideCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridCellOverrideCollection, value: NestedGridCellOverride) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridCellOverrideCollection, array: Array[NestedGridCellOverride], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridCellOverrideCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridCellOverrideCollection, value: NestedGridCellOverride) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridCellOverrideCollection, index: int, value: NestedGridCellOverride) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridCellOverrideCollection, value: NestedGridCellOverride) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridCellOverrideCollection, index: int) """
        pass

    def RemoveEntity(self, objectId):
        """ RemoveEntity(self: NestedGridCellOverrideCollection, objectId: ObjectId) """
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
    """Get: Count(self: NestedGridCellOverrideCollection) -> int

"""



class NestedGridDefinition(GridAssemblyDefinition):
    """ NestedGridDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    GridDivisionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridDivisionId(self: NestedGridDefinition) -> Int16

Set: GridDivisionId(self: NestedGridDefinition) = value
"""



class NestedGridDivision(ImpObject):
    """ NestedGridDivision() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEdgePositions(self, startPosition, endPosition, edgePositions, baseCurveRadius, gridAssembly):
        """ GetEdgePositions(self: NestedGridDivision, startPosition: float, endPosition: float, baseCurveRadius: float, gridAssembly: GridAssembly) -> DoubleCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DivisionDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DivisionDirection(self: NestedGridDivision) -> DivisionDirection

Set: DivisionDirection(self: NestedGridDivision) = value
"""

    EndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffset(self: NestedGridDivision) -> float

Set: EndOffset(self: NestedGridDivision) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: NestedGridDivision) -> Int16

Set: Id(self: NestedGridDivision) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NestedGridDivision) -> str

Set: Name(self: NestedGridDivision) = value
"""

    StartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffset(self: NestedGridDivision) -> float

Set: StartOffset(self: NestedGridDivision) = value
"""



class NestedGridDivisionComponentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridDivisionComponentCollection, value: NestedGridDivision) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridDivisionComponentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridDivisionComponentCollection, value: NestedGridDivision) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridDivisionComponentCollection, array: Array[NestedGridDivision], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridDivisionComponentCollection) -> IEnumerator """
        pass

    def GetId(self, id):
        """ GetId(self: NestedGridDivisionComponentCollection, id: Int16) -> NestedGridDivision """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridDivisionComponentCollection, value: NestedGridDivision) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridDivisionComponentCollection, index: int, value: NestedGridDivision) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridDivisionComponentCollection, value: NestedGridDivision) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridDivisionComponentCollection, index: int) """
        pass

    def RemoveId(self, id):
        """ RemoveId(self: NestedGridDivisionComponentCollection, id: Int16) """
        pass

    def ReplaceAt(self, index, value):
        """ ReplaceAt(self: NestedGridDivisionComponentCollection, index: int, value: NestedGridDivision) """
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
    """Get: Count(self: NestedGridDivisionComponentCollection) -> int

"""



class NestedGridDivisionDivideBy(NestedGridDivision):
    """ NestedGridDivisionDivideBy() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DivideByCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DivideByCount(self: NestedGridDivisionDivideBy) -> Int16

Set: DivideByCount(self: NestedGridDivisionDivideBy) = value
"""



class NestedGridDivisionManual(NestedGridDivision):
    """ NestedGridDivisionManual() """
    def AddManualEdgeDefinition(self, edgeDefinition):
        """ AddManualEdgeDefinition(self: NestedGridDivisionManual, edgeDefinition: NestedGridDivisionManualEdgeDefinition) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def ManualEdgeDefinitionAt(self, index):
        """ ManualEdgeDefinitionAt(self: NestedGridDivisionManual, index: int) -> NestedGridDivisionManualEdgeDefinition """
        pass

    def RemoveManualEdgeDefinitionAt(self, index):
        """ RemoveManualEdgeDefinitionAt(self: NestedGridDivisionManual, index: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ManualEdgeDefinitionCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManualEdgeDefinitionCount(self: NestedGridDivisionManual) -> int

"""



class NestedGridDivisionManualEdgeDefinition(ImpObject):
    """ NestedGridDivisionManualEdgeDefinition() """
    def CopyFrom(self, other):
        """ CopyFrom(self: NestedGridDivisionManualEdgeDefinition, other: RXObject) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AxisReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisReference(self: NestedGridDivisionManualEdgeDefinition) -> AxisReference

Set: AxisReference(self: NestedGridDivisionManualEdgeDefinition) = value
"""

    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: NestedGridDivisionManualEdgeDefinition) -> float

Set: Offset(self: NestedGridDivisionManualEdgeDefinition) = value
"""



class NestedGridDivisionOverride(ImpObject):
    """ NestedGridDivisionOverride() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DivisionDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DivisionDefinitionId(self: NestedGridDivisionOverride) -> Int16

Set: DivisionDefinitionId(self: NestedGridDivisionOverride) = value
"""

    GridAssignmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridAssignmentId(self: NestedGridDivisionOverride) -> Int16

Set: GridAssignmentId(self: NestedGridDivisionOverride) = value
"""

    IsStyleBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStyleBased(self: NestedGridDivisionOverride) -> bool

Set: IsStyleBased(self: NestedGridDivisionOverride) = value
"""



class NestedGridDivisionOverrideCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridDivisionOverrideCollection, value: NestedGridDivisionOverride) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridDivisionOverrideCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridDivisionOverrideCollection, value: NestedGridDivisionOverride) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridDivisionOverrideCollection, array: Array[NestedGridDivisionOverride], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridDivisionOverrideCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridDivisionOverrideCollection, value: NestedGridDivisionOverride) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridDivisionOverrideCollection, index: int, value: NestedGridDivisionOverride) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridDivisionOverrideCollection, value: NestedGridDivisionOverride) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridDivisionOverrideCollection, index: int) """
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
    """Get: Count(self: NestedGridDivisionOverrideCollection) -> int

"""



class NestedGridDivisionRepeat(NestedGridDivision):
    """ NestedGridDivisionRepeat() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellSize(self: NestedGridDivisionRepeat) -> float

Set: CellSize(self: NestedGridDivisionRepeat) = value
"""

    DistributeSlack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributeSlack(self: NestedGridDivisionRepeat) -> bool

Set: DistributeSlack(self: NestedGridDivisionRepeat) = value
"""

    DistributionFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistributionFlags(self: NestedGridDivisionRepeat) -> DistributionFlags

Set: DistributionFlags(self: NestedGridDivisionRepeat) = value
"""



class NestedGridEdgeAssignment(ImpObject):
    """ NestedGridEdgeAssignment() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetVoid(self):
        """ SetVoid(self: NestedGridEdgeAssignment) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    EdgeDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeDefinitionId(self: NestedGridEdgeAssignment) -> Int16

Set: EdgeDefinitionId(self: NestedGridEdgeAssignment) = value
"""

    EdgeSpecifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeSpecifier(self: NestedGridEdgeAssignment) -> IndexSpecifier

Set: EdgeSpecifier(self: NestedGridEdgeAssignment) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: NestedGridEdgeAssignment) -> Int16

Set: Id(self: NestedGridEdgeAssignment) = value
"""

    IsVoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVoid(self: NestedGridEdgeAssignment) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NestedGridEdgeAssignment) -> str

Set: Name(self: NestedGridEdgeAssignment) = value
"""

    ParentGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentGrid(self: NestedGridEdgeAssignment) -> GridAssemblyDefinition

"""



class NestedGridEdgeDefinition(ImpObject):
    """ NestedGridEdgeDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CleanupInternalEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CleanupInternalEdges(self: NestedGridEdgeDefinition) -> bool

Set: CleanupInternalEdges(self: NestedGridEdgeDefinition) = value
"""

    DepthOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthOffset(self: NestedGridEdgeDefinition) -> float

Set: DepthOffset(self: NestedGridEdgeDefinition) = value
"""

    EdgeDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeDepth(self: NestedGridEdgeDefinition) -> float

Set: EdgeDepth(self: NestedGridEdgeDefinition) = value
"""

    EdgeOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeOffset(self: NestedGridEdgeDefinition) -> float

Set: EdgeOffset(self: NestedGridEdgeDefinition) = value
"""

    EdgeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeWidth(self: NestedGridEdgeDefinition) -> float

Set: EdgeWidth(self: NestedGridEdgeDefinition) = value
"""

    EndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndOffset(self: NestedGridEdgeDefinition) -> float

Set: EndOffset(self: NestedGridEdgeDefinition) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: NestedGridEdgeDefinition) -> Int16

Set: Id(self: NestedGridEdgeDefinition) = value
"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: NestedGridEdgeDefinition) -> ObjectId

Set: MaterialId(self: NestedGridEdgeDefinition) = value
"""

    MirrorProfileX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MirrorProfileX(self: NestedGridEdgeDefinition) -> bool

Set: MirrorProfileX(self: NestedGridEdgeDefinition) = value
"""

    MirrorProfileY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MirrorProfileY(self: NestedGridEdgeDefinition) -> bool

Set: MirrorProfileY(self: NestedGridEdgeDefinition) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NestedGridEdgeDefinition) -> str

Set: Name(self: NestedGridEdgeDefinition) = value
"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: NestedGridEdgeDefinition) -> ObjectId

Set: ProfileId(self: NestedGridEdgeDefinition) = value
"""

    ProfileRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileRotation(self: NestedGridEdgeDefinition) -> float

Set: ProfileRotation(self: NestedGridEdgeDefinition) = value
"""

    ScaleProfileX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleProfileX(self: NestedGridEdgeDefinition) -> bool

Set: ScaleProfileX(self: NestedGridEdgeDefinition) = value
"""

    ScaleProfileY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleProfileY(self: NestedGridEdgeDefinition) -> bool

Set: ScaleProfileY(self: NestedGridEdgeDefinition) = value
"""

    StartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartOffset(self: NestedGridEdgeDefinition) -> float

Set: StartOffset(self: NestedGridEdgeDefinition) = value
"""



class NestedGridEdgeOverride(ImpObject):
    """ NestedGridEdgeOverride() """
    def CopyFrom(self, other):
        """ CopyFrom(self: NestedGridEdgeOverride, other: RXObject) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetVoid(self):
        """ SetVoid(self: NestedGridEdgeOverride) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    EdgeDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeDefinitionId(self: NestedGridEdgeOverride) -> Int16

Set: EdgeDefinitionId(self: NestedGridEdgeOverride) = value
"""

    EdgePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgePath(self: NestedGridEdgeOverride) -> IntegerCollection

Set: EdgePath(self: NestedGridEdgeOverride) = value
"""

    IsStyleBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStyleBased(self: NestedGridEdgeOverride) -> bool

Set: IsStyleBased(self: NestedGridEdgeOverride) = value
"""

    IsVoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVoid(self: NestedGridEdgeOverride) -> bool

"""



class NestedGridEdgeOverrideCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridEdgeOverrideCollection, value: NestedGridEdgeOverride) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridEdgeOverrideCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridEdgeOverrideCollection, value: NestedGridEdgeOverride) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridEdgeOverrideCollection, array: Array[NestedGridEdgeOverride], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridEdgeOverrideCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridEdgeOverrideCollection, value: NestedGridEdgeOverride) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridEdgeOverrideCollection, index: int, value: NestedGridEdgeOverride) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridEdgeOverrideCollection, value: NestedGridEdgeOverride) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridEdgeOverrideCollection, index: int) """
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
    """Get: Count(self: NestedGridEdgeOverrideCollection) -> int

"""



class NestedGridEdgeProfileOverride(ImpObject):
    """ NestedGridEdgeProfileOverride() """
    def CopyFrom(self, other):
        """ CopyFrom(self: NestedGridEdgeProfileOverride, other: RXObject) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    EdgePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgePath(self: NestedGridEdgeProfileOverride) -> IntegerCollection

Set: EdgePath(self: NestedGridEdgeProfileOverride) = value
"""

    IsStyleBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsStyleBased(self: NestedGridEdgeProfileOverride) -> bool

Set: IsStyleBased(self: NestedGridEdgeProfileOverride) = value
"""

    ProfileId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileId(self: NestedGridEdgeProfileOverride) -> ObjectId

Set: ProfileId(self: NestedGridEdgeProfileOverride) = value
"""



class NestedGridEdgeProfileOverrideCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridEdgeProfileOverrideCollection, value: NestedGridEdgeProfileOverride) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridEdgeProfileOverrideCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridEdgeProfileOverrideCollection, value: NestedGridEdgeProfileOverride) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridEdgeProfileOverrideCollection, array: Array[NestedGridEdgeProfileOverride], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridEdgeProfileOverrideCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridEdgeProfileOverrideCollection, value: NestedGridEdgeProfileOverride) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridEdgeProfileOverrideCollection, index: int, value: NestedGridEdgeProfileOverride) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridEdgeProfileOverrideCollection, value: NestedGridEdgeProfileOverride) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridEdgeProfileOverrideCollection, index: int) """
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
    """Get: Count(self: NestedGridEdgeProfileOverrideCollection) -> int

"""



class NestedGridInfillComponentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridInfillComponentCollection, value: NestedGridInfillDefinition) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridInfillComponentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridInfillComponentCollection, value: NestedGridInfillDefinition) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridInfillComponentCollection, array: Array[NestedGridInfillDefinition], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridInfillComponentCollection) -> IEnumerator """
        pass

    def GetId(self, id):
        """ GetId(self: NestedGridInfillComponentCollection, id: Int16) -> NestedGridInfillDefinition """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridInfillComponentCollection, value: NestedGridInfillDefinition) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridInfillComponentCollection, index: int, value: NestedGridInfillDefinition) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridInfillComponentCollection, value: NestedGridInfillDefinition) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridInfillComponentCollection, index: int) """
        pass

    def RemoveId(self, id):
        """ RemoveId(self: NestedGridInfillComponentCollection, id: Int16) """
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
    """Get: Count(self: NestedGridInfillComponentCollection) -> int

"""



class NestedGridInfillDefinition(ImpObject):
    """ NestedGridInfillDefinition() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetOrientation(self, flipX, flipY, flipZ):
        """ GetOrientation(self: NestedGridInfillDefinition) -> (bool, bool, bool) """
        pass

    def ManageAnchoredEntity(self, entity, cell, context, styleWasChanged):
        """ ManageAnchoredEntity(self: NestedGridInfillDefinition, entity: ObjectId, cell: GridAssemblyCell, context: AnchorContext, styleWasChanged: bool) """
        pass

    def SetOrientation(self, flipX, flipY, flipZ):
        """ SetOrientation(self: NestedGridInfillDefinition, flipX: bool, flipY: bool, flipZ: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: NestedGridInfillDefinition) -> Int16

Set: Id(self: NestedGridInfillDefinition) = value
"""

    LeftOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftOffset(self: NestedGridInfillDefinition) -> float

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: NestedGridInfillDefinition) -> ObjectId

Set: MaterialId(self: NestedGridInfillDefinition) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: NestedGridInfillDefinition) -> str

Set: Name(self: NestedGridInfillDefinition) = value
"""

    RightOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightOffset(self: NestedGridInfillDefinition) -> float

"""

    SupportsMaterials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsMaterials(self: NestedGridInfillDefinition) -> bool

"""

    SupportsMitre = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportsMitre(self: NestedGridInfillDefinition) -> bool

"""

    YAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YAlignment(self: NestedGridInfillDefinition) -> YAlignment

Set: YAlignment(self: NestedGridInfillDefinition) = value
"""

    YOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YOffset(self: NestedGridInfillDefinition) -> float

Set: YOffset(self: NestedGridInfillDefinition) = value
"""



class NestedGridInteriorEdgeAssignmentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridInteriorEdgeAssignmentCollection, value: NestedGridEdgeAssignment) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridInteriorEdgeAssignmentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridInteriorEdgeAssignmentCollection, value: NestedGridEdgeAssignment) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridInteriorEdgeAssignmentCollection, array: Array[NestedGridEdgeAssignment], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridInteriorEdgeAssignmentCollection) -> IEnumerator """
        pass

    def GetId(self, id):
        """ GetId(self: NestedGridInteriorEdgeAssignmentCollection, id: Int16) -> NestedGridEdgeAssignment """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridInteriorEdgeAssignmentCollection, value: NestedGridEdgeAssignment) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridInteriorEdgeAssignmentCollection, index: int, value: NestedGridEdgeAssignment) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridInteriorEdgeAssignmentCollection, value: NestedGridEdgeAssignment) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridInteriorEdgeAssignmentCollection, index: int) """
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
    """Get: Count(self: NestedGridInteriorEdgeAssignmentCollection) -> int

"""

    Default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Default(self: NestedGridInteriorEdgeAssignmentCollection) -> NestedGridEdgeAssignment

Set: Default(self: NestedGridInteriorEdgeAssignmentCollection) = value
"""



class NestedGridInteriorEdgeComponentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: NestedGridInteriorEdgeComponentCollection, value: NestedGridEdgeDefinition) -> int """
        pass

    def Clear(self):
        """ Clear(self: NestedGridInteriorEdgeComponentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: NestedGridInteriorEdgeComponentCollection, value: NestedGridEdgeDefinition) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: NestedGridInteriorEdgeComponentCollection, array: Array[NestedGridEdgeDefinition], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: NestedGridInteriorEdgeComponentCollection) -> IEnumerator """
        pass

    def GetId(self, id):
        """ GetId(self: NestedGridInteriorEdgeComponentCollection, id: Int16) -> NestedGridEdgeDefinition """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: NestedGridInteriorEdgeComponentCollection, value: NestedGridEdgeDefinition) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: NestedGridInteriorEdgeComponentCollection, index: int, value: NestedGridEdgeDefinition) """
        pass

    def Remove(self, value):
        """ Remove(self: NestedGridInteriorEdgeComponentCollection, value: NestedGridEdgeDefinition) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: NestedGridInteriorEdgeComponentCollection, index: int) """
        pass

    def RemoveId(self, id):
        """ RemoveId(self: NestedGridInteriorEdgeComponentCollection, id: Int16) """
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
    """Get: Count(self: NestedGridInteriorEdgeComponentCollection) -> int

"""



class NodeInformation(object):
    """ NodeInformation() """
    ids = None
    type = None


class NodeLocationType(Enum):
    """ enum NodeLocationType, values: End (1), Intersection (2), Start (0) """
    End = None
    Intersection = None
    Start = None
    value__ = None


class NodeLoopType(Enum):
    """ enum NodeLoopType, values: NonVoid (1), Void (0) """
    NonVoid = None
    value__ = None
    Void = None


class ObjectId(DisposableWrapper):
    """
    ObjectId(id: ObjectId, blockRefPath: ObjectIdCollection)
    ObjectId(id: ObjectId)
    ObjectId()
    """
    def Clone(self):
        """ Clone(self: ObjectId) -> object """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def Equals(*__args):
        """ Equals(objId1: ObjectId, objId2: ObjectId) -> bool """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: ObjectId, provider: IFormatProvider) -> str
        ToString(self: ObjectId) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id=None, blockRefPath=None):
        """
        __new__(cls: type, id: ObjectId, blockRefPath: ObjectIdCollection)
        __new__(cls: type, id: ObjectId)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BlockRefPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockRefPath(self: ObjectId) -> ObjectIdCollection

Set: BlockRefPath(self: ObjectId) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ObjectId) -> ObjectId

Set: Id(self: ObjectId) = value
"""

    ModelToWorldTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelToWorldTransform(self: ObjectId) -> Matrix3d

"""

    WorldToModelTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorldToModelTransform(self: ObjectId) -> Matrix3d

"""



class ObjectIdAndBlockReferencePath(object):
    """
    ObjectIdAndBlockReferencePath(id: ObjectId)
    ObjectIdAndBlockReferencePath(id: ObjectId, blockReferencePath: ObjectIdCollection)
    """
    @staticmethod # known case of __new__
    def __new__(self, id, blockReferencePath=None):
        """
        __new__(cls: type, id: ObjectId)
        __new__(cls: type, id: ObjectId, blockReferencePath: ObjectIdCollection)
        """
        pass

    BlockReferencePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockReferencePath(self: ObjectIdAndBlockReferencePath) -> ObjectIdCollection

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: ObjectIdAndBlockReferencePath) -> ObjectId

"""



class ObjectIdAndBlockReferencePathCollection(DisposableWrapper):
    """ ObjectIdAndBlockReferencePathCollection() """
    def Add(self, ObjectIdAndBlockReferencePath, bypassCheck=None):
        """
        Add(self: ObjectIdAndBlockReferencePathCollection, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath) -> int
        Add(self: ObjectIdAndBlockReferencePathCollection, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath, bypassCheck: bool) -> int
        """
        pass

    def Append(self, containerToAppend, bypassCheck=None):
        """ Append(self: ObjectIdAndBlockReferencePathCollection, containerToAppend: ObjectIdAndBlockReferencePathCollection, bypassCheck: bool)Append(self: ObjectIdAndBlockReferencePathCollection, containerToAppend: ObjectIdAndBlockReferencePathCollection) """
        pass

    def Clear(self):
        """ Clear(self: ObjectIdAndBlockReferencePathCollection) """
        pass

    def Contains(self, ObjectIdAndBlockReferencePath):
        """ Contains(self: ObjectIdAndBlockReferencePathCollection, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath) -> bool """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> ObjectIdAndBlockReferencePathCollection """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ObjectIdAndBlockReferencePathCollection) -> IEnumerator """
        pass

    def IndexOf(self, ObjectIdAndBlockReferencePath):
        """ IndexOf(self: ObjectIdAndBlockReferencePathCollection, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath) -> int """
        pass

    def Remove(self, ObjectIdAndBlockReferencePath):
        """ Remove(self: ObjectIdAndBlockReferencePathCollection, ObjectIdAndBlockReferencePath: ObjectIdAndBlockReferencePath) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ObjectIdAndBlockReferencePathCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
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
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ObjectIdAndBlockReferencePathCollection) -> int

"""



class ObjectIdCollection(DisposableWrapper):
    """ ObjectIdCollection() """
    def Add(self, value):
        """ Add(self: ObjectIdCollection, value: ObjectId) -> int """
        pass

    def Clear(self):
        """ Clear(self: ObjectIdCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: ObjectIdCollection, value: ObjectId) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: ObjectIdCollection, array: Array[ObjectId], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ObjectIdCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: ObjectIdCollection, value: ObjectId) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: ObjectIdCollection, index: int, value: ObjectId) """
        pass

    def Remove(self, value):
        """ Remove(self: ObjectIdCollection, value: ObjectId) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ObjectIdCollection, index: int) """
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
    """Get: Count(self: ObjectIdCollection) -> int

"""



class Operation(Enum):
    """ enum Operation, values: Additive (0), Combine (3), Intersect (2), Subtractive (1), Unknown (-1) """
    Additive = None
    Combine = None
    Intersect = None
    Subtractive = None
    Unknown = None
    value__ = None


class Override(ImpObject):
    """ Override() """
    @staticmethod
    def AddToOverrideExtensionDictionaryAndClose(objectToSetOn, newObjectToAdd):
        """ AddToOverrideExtensionDictionaryAndClose(objectToSetOn: DBObject, newObjectToAdd: DBObject) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ExtensionDictionaryName = 'AEC_OVERRIDES'


class OverrideCollection(object):
    """ OverrideCollection(pOp: IOverrideOperation) """
    def Add(self, value):
        """ Add(self: OverrideCollection, value: Override) -> int """
        pass

    def Clear(self):
        """ Clear(self: OverrideCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: OverrideCollection) -> IEnumerator """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: OverrideCollection, index: int) """
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IOverrideOperation) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: OverrideCollection) -> int

"""



class OverrideDisplayProperties(Override):
    """ OverrideDisplayProperties() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def VerifyReferences(self, fullCheck):
        """ VerifyReferences(self: OverrideDisplayProperties, fullCheck: bool) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayPropertyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayPropertyId(self: OverrideDisplayProperties) -> ObjectId

Set: DisplayPropertyId(self: OverrideDisplayProperties) = value
"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewId(self: OverrideDisplayProperties) -> ObjectId

Set: ViewId(self: OverrideDisplayProperties) = value
"""



class OverrideMask(Override):
    """ OverrideMask() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    MaskId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskId(self: OverrideMask) -> ObjectId

Set: MaskId(self: OverrideMask) = value
"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewId(self: OverrideMask) -> ObjectId

Set: ViewId(self: OverrideMask) = value
"""



class OverrideMaterialAssignment(Override):
    """ OverrideMaterialAssignment() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ComponentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentId(self: OverrideMaterialAssignment) -> Int16

Set: ComponentId(self: OverrideMaterialAssignment) = value
"""

    LocationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationId(self: OverrideMaterialAssignment) -> int

Set: LocationId(self: OverrideMaterialAssignment) = value
"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: OverrideMaterialAssignment) -> ObjectId

Set: MaterialId(self: OverrideMaterialAssignment) = value
"""



class ParameterChangeListenerManager(object):
    # no doc
    @staticmethod
    def RegisterListener(pListener):
        """ RegisterListener(pListener: Listener) """
        pass

    @staticmethod
    def UnRegisterListener(pListener):
        """ UnRegisterListener(pListener: Listener) """
        pass


class PlaneType(Enum):
    """ enum PlaneType, values: UV (0), UW (1), VW (2) """
    UV = None
    UW = None
    value__ = None
    VW = None


class Polygon(CellLayoutTool):
    """ Polygon() """
    def AddEcsVertex(self, point2d):
        """ AddEcsVertex(self: Polygon, point2d: Point2d) """
        pass

    def AddVertex(self, point3d):
        """ AddVertex(self: Polygon, point3d: Point3d) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def RemoveEcsVertex(self, point2d):
        """ RemoveEcsVertex(self: Polygon, point2d: Point2d) """
        pass

    def RemoveVertex(self, point3d):
        """ RemoveVertex(self: Polygon, point3d: Point3d) """
        pass

    def SetEcsVertices(self, points):
        """ SetEcsVertices(self: Polygon, points: Point2dCollection) """
        pass

    def SetVertices(self, points, plane):
        """ SetVertices(self: Polygon, points: Point3dCollection, plane: Plane) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    EdgePerimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgePerimeter(self: Polygon) -> float

"""

    GrossArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrossArea(self: Polygon) -> float

"""

    HasHiddenEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasHiddenEdge(self: Polygon) -> bool

"""

    InfillArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InfillArea(self: Polygon) -> float

"""

    InfillPerimeter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InfillPerimeter(self: Polygon) -> float

"""



class PolygonStyle(DictionaryRecord):
    """ PolygonStyle() """
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

    EdgeWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeWidth(self: PolygonStyle) -> float

Set: EdgeWidth(self: PolygonStyle) = value
"""

    EdgeWidthJustifyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EdgeWidthJustifyType(self: PolygonStyle) -> PolygonStyleEdgeWidthJustify

Set: EdgeWidthJustifyType(self: PolygonStyle) = value
"""



class PolygonStyleEdgeWidthJustify(Enum):
    """ enum PolygonStyleEdgeWidthJustify, values: Center (1), In (0), Out (2) """
    Center = None
    In = None
    Out = None
    value__ = None


class ProfileDefinition(DictionaryRecord):
    """ ProfileDefinition() """
    def CalculateSegmentPositions(self, direction):
        """ CalculateSegmentPositions(self: ProfileDefinition, direction: ProfileExtrusionDirection) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def ModifySegmentPositions(self, *__args):
        """ ModifySegmentPositions(self: ProfileDefinition, oldPosition: SegmentPosition, newPosition: SegmentPosition)ModifySegmentPositions(self: ProfileDefinition, oldDirection: ProfileExtrusionDirection, newDirection: ProfileExtrusionDirection) """
        pass

    def SetProfile(self, profileToCopy, translateInsertion, insertionPoint):
        """ SetProfile(self: ProfileDefinition, profileToCopy: Profile, translateInsertion: bool, insertionPoint: Point2d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ExtrusionDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtrusionDirection(self: ProfileDefinition) -> ProfileExtrusionDirection

Set: ExtrusionDirection(self: ProfileDefinition) = value
"""

    InsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InsertionPoint(self: ProfileDefinition) -> Point2d

Set: InsertionPoint(self: ProfileDefinition) = value
"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile(self: ProfileDefinition) -> Profile

"""



class ProjectState(Enum):
    """ enum ProjectState, values: Demolition (2), Existing (1), New (0) """
    Demolition = None
    Existing = None
    New = None
    value__ = None


class PropertyBase(RXObject):
    """ PropertyBase() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: PropertyBase) -> PropertyDataType

Set: DataType(self: PropertyBase) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PropertyBase) -> str

Set: Name(self: PropertyBase) = value
"""



class PropertyDataType(Enum):
    """ enum PropertyDataType, values: kAngle (6), kArea (5), kBoolean (0), kDistance (4), kInteger (1), kReal (2), kString (3), kSymbolId (8), kVolume (7) """
    kAngle = None
    kArea = None
    kBoolean = None
    kDistance = None
    kInteger = None
    kReal = None
    kString = None
    kSymbolId = None
    kVolume = None
    value__ = None


class ReferenceDocument(DBObject):
    """ ReferenceDocument() """
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

    FileFullPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileFullPath(self: ReferenceDocument) -> str

"""

    FilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilePath(self: ReferenceDocument) -> str

Set: FilePath(self: ReferenceDocument) = value
"""


    ExtensionDictionaryName = 'AEC_REF_DOCS'


class RelationType(Enum):
    """ enum RelationType, values: DisplayReferenceFor (1), DisplayReferenceOf (0), LocationReferenceFor (3), LocationReferenceOf (2), NotApplicable (-1), OwnedBy (5), OwnerOf (4), TwoWayReference (6) """
    DisplayReferenceFor = None
    DisplayReferenceOf = None
    LocationReferenceFor = None
    LocationReferenceOf = None
    NotApplicable = None
    OwnedBy = None
    OwnerOf = None
    TwoWayReference = None
    value__ = None


class RenderModeType(Enum):
    """ enum RenderModeType, values: Explode (2), Shade (1), WireFrame (0) """
    Explode = None
    Shade = None
    value__ = None
    WireFrame = None


class ResolvedMaterial(object):
    """
    ResolvedMaterial(componentId: Int16, componentName: str, materialId: ObjectId, entityClassName: str, styleClassName: str, styleName: str, isOverride: bool)
    ResolvedMaterial(componentId: Int16, componentName: str, materialId: ObjectId, entityClassName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, componentId, componentName, materialId, entityClassName, styleClassName=None, styleName=None, isOverride=None):
        """
        __new__(cls: type)
        __new__(cls: type, componentId: Int16, componentName: str, materialId: ObjectId, entityClassName: str, styleClassName: str, styleName: str, isOverride: bool)
        __new__(cls: type, componentId: Int16, componentName: str, materialId: ObjectId, entityClassName: str)
        """
        pass

    ComponentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentId(self: ResolvedMaterial) -> Int16

"""

    ComponentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentName(self: ResolvedMaterial) -> str

"""

    EntityClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityClassName(self: ResolvedMaterial) -> str

"""

    IsOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOverride(self: ResolvedMaterial) -> bool

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: ResolvedMaterial) -> ObjectId

"""

    StyleClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleClassName(self: ResolvedMaterial) -> str

"""

    StyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleName(self: ResolvedMaterial) -> str

"""



class ResolvedMaterialCollection(List[ResolvedMaterial]):
    """ ResolvedMaterialCollection() """

class RotationType(Enum):
    """ enum RotationType, values: CellRotationHorizontal (0), CellRotationVertical (1) """
    CellRotationHorizontal = None
    CellRotationVertical = None
    value__ = None


class RXClassToObjectId(object):
    """ RXClassToObjectId(type: RXClass, ids: ObjectIdCollection) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, ids):
        """
        __new__[RXClassToObjectId]() -> RXClassToObjectId
        
        __new__(cls: type, type: RXClass, ids: ObjectIdCollection)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Ids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ids(self: RXClassToObjectId) -> ObjectIdCollection

Set: Ids(self: RXClassToObjectId) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: RXClassToObjectId) -> RXClass

Set: Type(self: RXClassToObjectId) = value
"""



class RXClassToObjectIdCollection(DisposableWrapper):
    # no doc
    def Add(self, item):
        """ Add(self: RXClassToObjectIdCollection, item: RXClassToObjectId) -> int """
        pass

    def Clear(self):
        """ Clear(self: RXClassToObjectIdCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: RXClassToObjectIdCollection, item: RXClassToObjectId) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: RXClassToObjectIdCollection, array: Array[RXClassToObjectId], start: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: RXClassToObjectIdCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: RXClassToObjectIdCollection, item: RXClassToObjectId) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: RXClassToObjectIdCollection, index: int, item: RXClassToObjectId) """
        pass

    def Lookup(self, type):
        """ Lookup(self: RXClassToObjectIdCollection, type: RXClass) -> ObjectIdCollection """
        pass

    def Remove(self, item):
        """ Remove(self: RXClassToObjectIdCollection, item: RXClassToObjectId) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: RXClassToObjectIdCollection, index: int) """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: RXClassToObjectIdCollection) -> int

"""



class Section2d(Geo):
    """ Section2d() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def HasAssociatedModelSpaceView(self, viewTableRecordId):
        """ HasAssociatedModelSpaceView(self: Section2d, viewTableRecordId: ObjectId) -> bool """
        pass

    def IntegrateLineWork(self, startPoint, endPoint, materialId, componentType, userComponentId, lineWorkType, isManual, isEdit):
        """ IntegrateLineWork(self: Section2d, startPoint: Point2d, endPoint: Point2d, materialId: ObjectId, componentType: ComponentType, userComponentId: Int16, lineWorkType: LineWorkType, isManual: bool, isEdit: bool) """
        pass

    def MergeLineWork(self, startPoint, endPoint, componentId, materialId, lineWorkType, mergeExactOnly):
        """ MergeLineWork(self: Section2d, startPoint: Point2d, endPoint: Point2d, componentId: Int16, materialId: ObjectId, lineWorkType: LineWorkType, mergeExactOnly: bool) """
        pass

    def MergeSection2d(self, section, doComponentEdits, doMergeEdits, removeSegments):
        """ MergeSection2d(self: Section2d, section: Section2d, doComponentEdits: bool, doMergeEdits: bool, removeSegments: bool) """
        pass

    def RemoveAllButUserEdits(self):
        """ RemoveAllButUserEdits(self: Section2d) """
        pass

    def RemoveAllLineWork(self):
        """ RemoveAllLineWork(self: Section2d) """
        pass

    def RemoveObjectPropertyDependencies(self):
        """ RemoveObjectPropertyDependencies(self: Section2d) """
        pass

    def SaveEditInPlaceChanges(self):
        """ SaveEditInPlaceChanges(self: Section2d) """
        pass

    def SetAssociatedModelSpaceView(self, viewTableRecord):
        """ SetAssociatedModelSpaceView(self: Section2d, viewTableRecord: ViewTableRecord) """
        pass

    def SetIsSingleSegment(self, value, segmentId):
        """ SetIsSingleSegment(self: Section2d, value: bool, segmentId: UInt32) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ClipVolumeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClipVolumeId(self: Section2d) -> ObjectId

Set: ClipVolumeId(self: Section2d) = value
"""

    HasObjectDisplayPropertyInformation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasObjectDisplayPropertyInformation(self: Section2d) -> bool

"""

    HasUserEdits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasUserEdits(self: Section2d) -> bool

"""

    HatchRegions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchRegions(self: Section2d) -> Section2dHatchRegionCollection

"""

    HatchRegionsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchRegionsCount(self: Section2d) -> int

"""

    IsSavedEdits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSavedEdits(self: Section2d) -> bool

Set: IsSavedEdits(self: Section2d) = value
"""

    IsSingleSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSingleSegment(self: Section2d) -> bool

"""

    MainSectionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MainSectionId(self: Section2d) -> ObjectId

Set: MainSectionId(self: Section2d) = value
"""

    SegmentGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentGroups(self: Section2d) -> Section2dSegmentGroupCollection

"""

    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: Section2d) -> SectionSegmentCollection

"""

    ShrinkWrapProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShrinkWrapProfile(self: Section2d) -> Profile

Set: ShrinkWrapProfile(self: Section2d) = value
"""

    ShrinkWrapSegmentGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShrinkWrapSegmentGroup(self: Section2d) -> Section2dSegmentGroup

"""

    SingleSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleSegment(self: Section2d) -> SectionSegment

"""

    SingleSegmentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleSegmentId(self: Section2d) -> int

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Section2d) -> SectionVertexCollection

"""



class Section2dHatchRegion(ImpObject):
    """ Section2dHatchRegion() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AppliesToMaterialLineWork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToMaterialLineWork(self: Section2dHatchRegion) -> bool

Set: AppliesToMaterialLineWork(self: Section2dHatchRegion) = value
"""

    AppliesToSectionHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToSectionHatch(self: Section2dHatchRegion) -> bool

Set: AppliesToSectionHatch(self: Section2dHatchRegion) = value
"""

    AppliesToShrinkWrapHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToShrinkWrapHatch(self: Section2dHatchRegion) -> bool

Set: AppliesToShrinkWrapHatch(self: Section2dHatchRegion) = value
"""

    AppliesToShrinkWrapLineWork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToShrinkWrapLineWork(self: Section2dHatchRegion) -> bool

Set: AppliesToShrinkWrapLineWork(self: Section2dHatchRegion) = value
"""

    AppliesToSurfaceHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppliesToSurfaceHatch(self: Section2dHatchRegion) -> bool

Set: AppliesToSurfaceHatch(self: Section2dHatchRegion) = value
"""

    HasMaterialFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasMaterialFilter(self: Section2dHatchRegion) -> bool

"""

    HatchProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchProfile(self: Section2dHatchRegion) -> Profile

Set: HatchProfile(self: Section2dHatchRegion) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Section2dHatchRegion) -> UInt16

"""

    IsSubtractive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSubtractive(self: Section2dHatchRegion) -> bool

Set: IsSubtractive(self: Section2dHatchRegion) = value
"""

    MaterialFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialFilter(self: Section2dHatchRegion) -> ObjectIdCollection

Set: MaterialFilter(self: Section2dHatchRegion) = value
"""



class Section2dHatchRegionCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: Section2dHatchRegionCollection, value: Section2dHatchRegion) -> int """
        pass

    def Clear(self):
        """ Clear(self: Section2dHatchRegionCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: Section2dHatchRegionCollection, value: Section2dHatchRegion) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: Section2dHatchRegionCollection, array: Array[Section2dHatchRegion], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Section2dHatchRegionCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: Section2dHatchRegionCollection, value: Section2dHatchRegion) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: Section2dHatchRegionCollection, index: int, value: Section2dHatchRegion) """
        pass

    def Remove(self, value):
        """ Remove(self: Section2dHatchRegionCollection, value: Section2dHatchRegion) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: Section2dHatchRegionCollection, index: int) """
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
    """Get: Count(self: Section2dHatchRegionCollection) -> int

"""



class Section2dSegmentGroup(ImpObject):
    """ Section2dSegmentGroup() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def RemoveAllButUserEdits(self):
        """ RemoveAllButUserEdits(self: Section2dSegmentGroup) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    HasUserEdits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasUserEdits(self: Section2dSegmentGroup) -> bool

"""

    LineWorkSegments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWorkSegments(self: Section2dSegmentGroup) -> SectionSegmentCollection

"""

    MaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialId(self: Section2dSegmentGroup) -> ObjectId

Set: MaterialId(self: Section2dSegmentGroup) = value
"""

    SectionHatchingSegments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionHatchingSegments(self: Section2dSegmentGroup) -> SectionSegmentCollection

"""

    SurfaceHatchingSegments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceHatchingSegments(self: Section2dSegmentGroup) -> SectionSegmentCollection

"""



class Section2dSegmentGroupCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: Section2dSegmentGroupCollection, value: Section2dSegmentGroup) -> int """
        pass

    def Clear(self):
        """ Clear(self: Section2dSegmentGroupCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: Section2dSegmentGroupCollection, value: Section2dSegmentGroup) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: Section2dSegmentGroupCollection, array: Array[Section2dSegmentGroup], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Section2dSegmentGroupCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: Section2dSegmentGroupCollection, value: Section2dSegmentGroup) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: Section2dSegmentGroupCollection, index: int, value: Section2dSegmentGroup) """
        pass

    def Remove(self, value):
        """ Remove(self: Section2dSegmentGroupCollection, value: Section2dSegmentGroup) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: Section2dSegmentGroupCollection, index: int) """
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
    """Get: Count(self: Section2dSegmentGroupCollection) -> int

"""



class Section2dStyle(DictionaryRecord):
    """ Section2dStyle() """
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

    KeepAllHiddenLineWork = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeepAllHiddenLineWork(self: Section2dStyle) -> bool

Set: KeepAllHiddenLineWork(self: Section2dStyle) = value
"""

    LineWorkComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWorkComponents(self: Section2dStyle) -> LineWorkComponentCollection

"""

    LineWorkRules = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWorkRules(self: Section2dStyle) -> LineWorkRuleCollection

"""

    UseObjectDisplayProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseObjectDisplayProperty(self: Section2dStyle) -> bool

Set: UseObjectDisplayProperty(self: Section2dStyle) = value
"""



class Section2dStyleParameter(Enum):
    """ enum Section2dStyleParameter, values: Component (0), KeepHiddenLineWork (2), LineWorkRule (1), UseObjectDisplayProperties (3) """
    Component = None
    KeepHiddenLineWork = None
    LineWorkRule = None
    UseObjectDisplayProperties = None
    value__ = None


class SectionSegment(ImpObject):
    """ SectionSegment() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ComponentId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentId(self: SectionSegment) -> Int16

Set: ComponentId(self: SectionSegment) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: SectionSegment) -> Point2d

Set: EndPoint(self: SectionSegment) = value
"""

    IsAPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAPoint(self: SectionSegment) -> bool

Set: IsAPoint(self: SectionSegment) = value
"""

    IsMergedSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMergedSegment(self: SectionSegment) -> bool

Set: IsMergedSegment(self: SectionSegment) = value
"""

    LineWorkType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWorkType(self: SectionSegment) -> LineWorkType

"""

    MarkedFromEdit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkedFromEdit(self: SectionSegment) -> bool

Set: MarkedFromEdit(self: SectionSegment) = value
"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: SectionSegment) -> Point2d

Set: StartPoint(self: SectionSegment) = value
"""



class SectionSegmentCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: SectionSegmentCollection, value: SectionSegment) -> int """
        pass

    def Clear(self):
        """ Clear(self: SectionSegmentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: SectionSegmentCollection, value: SectionSegment) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: SectionSegmentCollection, array: Array[SectionSegment], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionSegmentCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: SectionSegmentCollection, value: SectionSegment) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: SectionSegmentCollection, index: int, value: SectionSegment) """
        pass

    def Remove(self, value):
        """ Remove(self: SectionSegmentCollection, value: SectionSegment) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SectionSegmentCollection, index: int) """
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
    """Get: Count(self: SectionSegmentCollection) -> int

"""



class SectionVertex(ImpObject):
    """ SectionVertex() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: SectionVertex) -> Point2d

Set: Location(self: SectionVertex) = value
"""



class SectionVertexCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: SectionVertexCollection, value: SectionVertex) -> int """
        pass

    def Clear(self):
        """ Clear(self: SectionVertexCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: SectionVertexCollection, value: SectionVertex) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: SectionVertexCollection, array: Array[SectionVertex], index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionVertexCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: SectionVertexCollection, value: SectionVertex) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: SectionVertexCollection, index: int, value: SectionVertex) """
        pass

    def Remove(self, value):
        """ Remove(self: SectionVertexCollection, value: SectionVertex) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SectionVertexCollection, index: int) """
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
    """Get: Count(self: SectionVertexCollection) -> int

"""



class ShapeSubType(Enum):
    """ enum ShapeSubType, values: ProfileExternal (1), ProfileInternal (0), Unspecified (-1) """
    ProfileExternal = None
    ProfileInternal = None
    Unspecified = None
    value__ = None


class ShapeType(Enum):
    """ enum ShapeType, values: Arch (1), BarrelVault (2), BoundaryRepresentation (14), Box (0), Cone (4), Cylinder (5), Dome (6), Doric (3), Error (-1), Extrusion (12), Gable (7), IsoscelesTriangle (8), Pyramid (10), Revolution (13), RightTriangle (9), Sphere (11), Unknown (-2) """
    Arch = None
    BarrelVault = None
    BoundaryRepresentation = None
    Box = None
    Cone = None
    Cylinder = None
    Dome = None
    Doric = None
    Error = None
    Extrusion = None
    Gable = None
    IsoscelesTriangle = None
    Pyramid = None
    Revolution = None
    RightTriangle = None
    Sphere = None
    Unknown = None
    value__ = None


class SkipPushPopDisplayPropertiesType(Enum):
    """ enum SkipPushPopDisplayPropertiesType, values: AutoCADRenderMaterial (128), Color (1), Layer (2), LineType (4), LineTypeScale (16), LineWeight (8), None (0), PlotStyle (32), VisualStyle (64) """
    AutoCADRenderMaterial = None
    Color = None
    Layer = None
    LineType = None
    LineTypeScale = None
    LineWeight = None
    None = None
    PlotStyle = None
    value__ = None
    VisualStyle = None


class Slice(LayoutTool):
    """ Slice() """
    def AppendObject(self, objectId):
        """ AppendObject(self: Slice, objectId: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetEntities(self):
        """ GetEntities(self: Slice) -> ObjectIdCollection """
        pass

    def RemoveObject(self, objectId):
        """ RemoveObject(self: Slice, objectId: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    PlaneDepth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaneDepth(self: Slice) -> float

Set: PlaneDepth(self: Slice) = value
"""

    PlaneWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaneWidth(self: Slice) -> float

Set: PlaneWidth(self: Slice) = value
"""

    Profile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profile(self: Slice) -> Profile

"""



class StandardDisplaySetType(Enum):
    """ enum StandardDisplaySetType, values: Model (3), ModelHighDetail (131), ModelLowDetail (129), NotStandard (0), NumberOfStandardSets (9), Plan (5), PlanHighDetail (65), PlanLowDetail (33), Reflected (9), Section (17), Standard (1) """
    Model = None
    ModelHighDetail = None
    ModelLowDetail = None
    NotStandard = None
    NumberOfStandardSets = None
    Plan = None
    PlanHighDetail = None
    PlanLowDetail = None
    Reflected = None
    Section = None
    Standard = None
    value__ = None


class StreamAcad(RXObject):
    # no doc
    def AddToSkipPushPopDisplayPropertiesFlags(self, newDisplayPropertiesToSkipFlagsToAdd):
        """ AddToSkipPushPopDisplayPropertiesFlags(self: StreamAcad, newDisplayPropertiesToSkipFlagsToAdd: int) """
        pass

    def AlreadyDrawing(self, object):
        """ AlreadyDrawing(self: StreamAcad, object: DBObject) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetPlotStyleId(self):
        """ GetPlotStyleId(self: StreamAcad) -> ObjectId """
        pass

    def GetPlotStyleNameType(self):
        """ GetPlotStyleNameType(self: StreamAcad) -> PlotStyleNameType """
        pass

    def IsVisible(self, properties):
        """ IsVisible(self: StreamAcad, properties: DisplayComponentEntity) -> bool """
        pass

    def PopAutoCADRenderMaterial(self):
        """ PopAutoCADRenderMaterial(self: StreamAcad) """
        pass

    def PopBodyEdgeColorMode(self):
        """ PopBodyEdgeColorMode(self: StreamAcad) """
        pass

    def PopBodyFaceColorMode(self):
        """ PopBodyFaceColorMode(self: StreamAcad) """
        pass

    def PopColor(self):
        """ PopColor(self: StreamAcad) """
        pass

    def PopDisplayDirection(self):
        """ PopDisplayDirection(self: StreamAcad) """
        pass

    def PopDisplayParameters(self):
        """ PopDisplayParameters(self: StreamAcad) """
        pass

    def PopEntity(self):
        """ PopEntity(self: StreamAcad) """
        pass

    def PopFillType(self):
        """ PopFillType(self: StreamAcad) """
        pass

    def PopGsMarker(self):
        """ PopGsMarker(self: StreamAcad) """
        pass

    def PopInsertXform(self):
        """ PopInsertXform(self: StreamAcad) """
        pass

    def PopLayer(self):
        """ PopLayer(self: StreamAcad) """
        pass

    def PopLinetype(self):
        """ PopLinetype(self: StreamAcad) """
        pass

    def PopLineTypeScale(self):
        """ PopLineTypeScale(self: StreamAcad) """
        pass

    def PopLineWeight(self):
        """ PopLineWeight(self: StreamAcad) """
        pass

    def PopMaterial(self, closeIt):
        """ PopMaterial(self: StreamAcad, closeIt: bool) """
        pass

    def PopPlotStyle(self):
        """ PopPlotStyle(self: StreamAcad) """
        pass

    def PopProperties(self):
        """ PopProperties(self: StreamAcad) """
        pass

    def PopRenderMode(self):
        """ PopRenderMode(self: StreamAcad) """
        pass

    def PopSubObjectCoordinateSystem(self):
        """ PopSubObjectCoordinateSystem(self: StreamAcad) """
        pass

    def PopVisualStyle(self):
        """ PopVisualStyle(self: StreamAcad) """
        pass

    def PopXform(self):
        """ PopXform(self: StreamAcad) """
        pass

    def PushAutoCADRenderMaterial(self, id):
        """ PushAutoCADRenderMaterial(self: StreamAcad, id: ObjectId) """
        pass

    def PushBodyEdgeColorMode(self, mode):
        """ PushBodyEdgeColorMode(self: StreamAcad, mode: StreamBodyColorModeType) """
        pass

    def PushBodyFaceColorMode(self, mode):
        """ PushBodyFaceColorMode(self: StreamAcad, mode: StreamBodyColorModeType) """
        pass

    def PushColor(self, *__args):
        """ PushColor(self: StreamAcad, colorIndex: int)PushColor(self: StreamAcad, trueColor: Color) """
        pass

    def PushDisplayDirection(self, displayDirection):
        """ PushDisplayDirection(self: StreamAcad, displayDirection: Vector3d) """
        pass

    def PushDisplayParameters(self, displayConfigurationId, transaction):
        """ PushDisplayParameters(self: StreamAcad, displayConfigurationId: ObjectId, transaction: Transaction) """
        pass

    def PushEntity(self, object):
        """ PushEntity(self: StreamAcad, object: DBObject) """
        pass

    def PushFillType(self, fillType):
        """ PushFillType(self: StreamAcad, fillType: FillType) """
        pass

    def PushGsMarker(self, id):
        """ PushGsMarker(self: StreamAcad, id: IntPtr) """
        pass

    def PushInsertXform(self, matrix):
        """ PushInsertXform(self: StreamAcad, matrix: Matrix3d) """
        pass

    def PushLayer(self, id):
        """ PushLayer(self: StreamAcad, id: ObjectId) """
        pass

    def PushLinetype(self, lineTypeId):
        """ PushLinetype(self: StreamAcad, lineTypeId: ObjectId) """
        pass

    def PushLineTypeScale(self, thickness):
        """ PushLineTypeScale(self: StreamAcad, thickness: float) """
        pass

    def PushLineWeight(self, lineWeight):
        """ PushLineWeight(self: StreamAcad, lineWeight: LineWeight) """
        pass

    def PushMaterial(self, *__args):
        """
        PushMaterial(self: StreamAcad, materialId: ObjectId) -> MaterialDefinition
        PushMaterial(self: StreamAcad, materialDefinition: MaterialDefinition)
        """
        pass

    def PushPlotStyle(self, type, id):
        """ PushPlotStyle(self: StreamAcad, type: PlotStyleNameType, id: ObjectId) """
        pass

    def PushProperties(self, *__args):
        """ PushProperties(self: StreamAcad, entity: Entity)PushProperties(self: StreamAcad, properties: DisplayComponentEntity) """
        pass

    def PushRenderMode(self, mode):
        """ PushRenderMode(self: StreamAcad, mode: RenderModeType) """
        pass

    def PushSubObjectCoordinateSystem(self, matrix):
        """ PushSubObjectCoordinateSystem(self: StreamAcad, matrix: Matrix3d) """
        pass

    def PushVisualStyle(self, id):
        """ PushVisualStyle(self: StreamAcad, id: ObjectId) """
        pass

    def PushXform(self, matrix):
        """ PushXform(self: StreamAcad, matrix: Matrix3d) """
        pass

    def RemoveFromSkipPushPopDisplayPropertiesFlags(self, newDisplayPropertiesToSkipFlagsToRemove):
        """ RemoveFromSkipPushPopDisplayPropertiesFlags(self: StreamAcad, newDisplayPropertiesToSkipFlagsToRemove: int) """
        pass

    def SetSkipPushPopDisplayProperties(self, skip):
        """ SetSkipPushPopDisplayProperties(self: StreamAcad, skip: bool) """
        pass

    def Stream(self, *__args):
        """ Stream(self: StreamAcad, arc: EllipticalArc3d)Stream(self: StreamAcad, arc: CircularArc3d)Stream(self: StreamAcad, line: LineSegment3d)Stream(self: StreamAcad, points: Point3dCollection, closed: bool, intendedType: StreamEntityType)Stream(self: StreamAcad, line: LineSegment3d, parameters: DoubleCollection)Stream(self: StreamAcad, entity: Entity, pushEntityProperties: bool)Stream(self: StreamAcad, entity: Entity)Stream(self: StreamAcad, block: BoundBlock3d)Stream(self: StreamAcad, body: Body, colorToPropertiesMap: StreamColorToPropertiesMap)Stream(self: StreamAcad, body: Body)Stream(self: StreamAcad, points: Array[Point3d], closed: bool, intendedType: StreamEntityType)Stream(self: StreamAcad, line: LineSegment2d, parameters: DoubleCollection)Stream(self: StreamAcad, line: LineSegment2d)Stream(self: StreamAcad, begin: Point2d, end: Point2d)Stream(self: StreamAcad, curve: Curve2d)Stream(self: StreamAcad, curve: Curve3d)Stream(self: StreamAcad, begin: Point3d, end: Point3d)Stream(self: StreamAcad, points: Array[Point3d], closed: bool, intendedType: StreamEntityType, normal: Vector3d)Stream(self: StreamAcad, points: Array[Point3d], visibility: IntegerCollection)Stream(self: StreamAcad, arc: EllipticalArc2d)Stream(self: StreamAcad, arc: CircularArc2d) """
        pass

    def StreamBlock(self, blockRecord, *__args):
        """ StreamBlock(self: StreamAcad, blockRecord: BlockTableRecord)StreamBlock(self: StreamAcad, blockRecord: BlockTableRecord, showAttributedefinitions: bool)StreamBlock(self: StreamAcad, blockRecord: BlockTableRecord, nonDbAttributes: DBObjectCollection) """
        pass

    def StreamByMaterialHatch(self, *__args):
        """ StreamByMaterialHatch(self: StreamAcad, ecsToWcs: Matrix3d, hatchInformation: DisplayComponentHatch, materialId: ObjectId, points: Array[Point3d], bulges: Array[float])StreamByMaterialHatch(self: StreamAcad, fromEntity: Geo, hatchProperties: DisplayComponentHatch, materialId: ObjectId, points: Array[Point3d], bulges: Array[float])StreamByMaterialHatch(self: StreamAcad, fromEntity: Geo, hatchProperties: DisplayComponentHatch, materialId: ObjectId, profile: Profile)StreamByMaterialHatch(self: StreamAcad, ecsToWcs: Matrix3d, hatchInformation: DisplayComponentHatch, materialId: ObjectId, profile: Profile)StreamByMaterialHatch(self: StreamAcad, ecsToWcs: Matrix3d, profile: Profile, data: DisplayComponentPushPopData)StreamByMaterialHatch(self: StreamAcad, fromEntity: Geo, points: Array[Point3d], bulges: Array[float], data: DisplayComponentPushPopData)StreamByMaterialHatch(self: StreamAcad, fromEntity: Geo, profile: Profile, data: DisplayComponentPushPopData) """
        pass

    def StreamDrawable(self, drawable):
        """ StreamDrawable(self: StreamAcad, drawable: Drawable) """
        pass

    def StreamHatch(self, *__args):
        """ StreamHatch(self: StreamAcad, fromEntity: Geo, hatchInformation: DisplayComponentHatch, profile: Profile)StreamHatch(self: StreamAcad, ecsToWcs: Matrix3d, hatchInformation: DisplayComponentHatch, points: Array[Point3d], bulges: Array[float])StreamHatch(self: StreamAcad, fromEntity: Geo, hatchInformation: DisplayComponentHatch, points: Array[Point3d], bulges: Array[float])StreamHatch(self: StreamAcad, hatch: Hatch, pushEntityProperties: bool)StreamHatch(self: StreamAcad, hatch: Hatch)StreamHatch(self: StreamAcad, ecsToWcs: Matrix3d, hatchInformation: DisplayComponentHatch, profile: Profile) """
        pass

    def StreamWcs(self, *__args):
        """ StreamWcs(self: StreamAcad, points: Array[Point3d], closed: bool, intendedType: StreamEntityType, normal: Vector3d)StreamWcs(self: StreamAcad, points: Array[Point3d], visibility: IntegerCollection)StreamWcs(self: StreamAcad, begin: Point3d, end: Point3d)StreamWcs(self: StreamAcad, points: Array[Point3d], closed: bool, intendedType: StreamEntityType)StreamWcs(self: StreamAcad, body: Body)StreamWcs(self: StreamAcad, body: Body, colorToPropertiesMap: StreamColorToPropertiesMap)StreamWcs(self: StreamAcad, arc: CircularArc3d)StreamWcs(self: StreamAcad, arc: EllipticalArc3d) """
        pass

    def StreamWireframeBodyWcs(self, body):
        """ StreamWireframeBodyWcs(self: StreamAcad, body: Body) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    AlwaysResolveByLayerPlotStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlwaysResolveByLayerPlotStyles(self: StreamAcad) -> bool

"""

    AnnotationScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AnnotationScale(self: StreamAcad) -> AnnotationScale

"""

    ApplySurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplySurfaceHatching(self: StreamAcad) -> bool

"""

    AttenuateColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttenuateColor(self: StreamAcad) -> bool

Set: AttenuateColor(self: StreamAcad) = value
"""

    AutoCADRenderMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADRenderMaterial(self: StreamAcad) -> ObjectId

"""

    BackfaceCullSurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackfaceCullSurfaceHatching(self: StreamAcad) -> bool

"""

    BodyEdgeColorMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BodyEdgeColorMode(self: StreamAcad) -> StreamBodyColorModeType

"""

    BodyFaceColorMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BodyFaceColorMode(self: StreamAcad) -> StreamBodyColorModeType

"""

    ColorIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorIndex(self: StreamAcad) -> int

"""

    CurrentEntityDrawData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentEntityDrawData(self: StreamAcad) -> GraphicsSystemEntityDrawData

"""

    CurrentGsMarkerInfoTree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentGsMarkerInfoTree(self: StreamAcad) -> GsMarkerInformationTree

"""

    CurrentInsertXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentInsertXform(self: StreamAcad) -> Matrix3d

"""

    CurrentSubObjectXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSubObjectXform(self: StreamAcad) -> Matrix3d

"""

    CurrentXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentXform(self: StreamAcad) -> Matrix3d

"""

    DisplayDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayDirection(self: StreamAcad) -> Vector3d

"""

    DisplaySetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplaySetId(self: StreamAcad) -> ObjectId

"""

    EnablePushPopXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnablePushPopXform(self: StreamAcad) -> bool

Set: EnablePushPopXform(self: StreamAcad) = value
"""

    Entity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entity(self: StreamAcad) -> DBObject

"""

    FillType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillType(self: StreamAcad) -> FillType

"""

    FilterFrozenLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterFrozenLayers(self: StreamAcad) -> bool

Set: FilterFrozenLayers(self: StreamAcad) = value
"""

    FilterOffLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterOffLayers(self: StreamAcad) -> bool

Set: FilterOffLayers(self: StreamAcad) = value
"""

    GsMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GsMarker(self: StreamAcad) -> IntPtr

"""

    GsMarkersValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GsMarkersValid(self: StreamAcad) -> bool

Set: GsMarkersValid(self: StreamAcad) = value
"""

    IgnoreLiveSections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreLiveSections(self: StreamAcad) -> bool

Set: IgnoreLiveSections(self: StreamAcad) = value
"""

    IndependentLayerOffControl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IndependentLayerOffControl(self: StreamAcad) -> bool

Set: IndependentLayerOffControl(self: StreamAcad) = value
"""

    InverseInsertXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InverseInsertXform(self: StreamAcad) -> Matrix3d

"""

    InverseSubObjectXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InverseSubObjectXform(self: StreamAcad) -> Matrix3d

"""

    InverseXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InverseXform(self: StreamAcad) -> Matrix3d

"""

    IsPerspectiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPerspectiveView(self: StreamAcad) -> bool

"""

    IsScaled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsScaled(self: StreamAcad) -> bool

"""

    IsUniScaled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUniScaled(self: StreamAcad) -> bool

"""

    IsXform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsXform(self: StreamAcad) -> bool

"""

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: StreamAcad) -> ObjectId

"""

    Linetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetype(self: StreamAcad) -> ObjectId

"""

    LineTypeScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineTypeScale(self: StreamAcad) -> float

"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWeight(self: StreamAcad) -> LineWeight

"""

    LiveSectionRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LiveSectionRequired(self: StreamAcad) -> bool

"""

    MaskingRequired = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskingRequired(self: StreamAcad) -> bool

"""

    Material = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Material(self: StreamAcad) -> MaterialDefinition

"""

    RenderMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMode(self: StreamAcad) -> RenderModeType

"""

    ResolveByBlockTraits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResolveByBlockTraits(self: StreamAcad) -> bool

Set: ResolveByBlockTraits(self: StreamAcad) = value
"""

    ResolveByLayerTraits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResolveByLayerTraits(self: StreamAcad) -> bool

Set: ResolveByLayerTraits(self: StreamAcad) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: StreamAcad) -> Scale3d

"""

    SkipPushPopDisplayPropertiesFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SkipPushPopDisplayPropertiesFlags(self: StreamAcad) -> int

Set: SkipPushPopDisplayPropertiesFlags(self: StreamAcad) = value
"""

    SuppressShellAndMeshExtendedData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuppressShellAndMeshExtendedData(self: StreamAcad) -> bool

Set: SuppressShellAndMeshExtendedData(self: StreamAcad) = value
"""

    TrueColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrueColor(self: StreamAcad) -> Color

"""

    UseBodyInternalDeviation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseBodyInternalDeviation(self: StreamAcad) -> bool

Set: UseBodyInternalDeviation(self: StreamAcad) = value
"""

    UseLayerPropertyOverridePerViewportIfExists = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseLayerPropertyOverridePerViewportIfExists(self: StreamAcad) -> bool

Set: UseLayerPropertyOverridePerViewportIfExists(self: StreamAcad) = value
"""

    ViewportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportId(self: StreamAcad) -> ObjectId

"""

    VisualStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VisualStyle(self: StreamAcad) -> ObjectId

"""



class StreamBodyColorModeType(Enum):
    """ enum StreamBodyColorModeType, values: Ignore (0), UseAsColor (1), UseAsGsMarker (2), UseAsMapIndex (3) """
    Ignore = None
    UseAsColor = None
    UseAsGsMarker = None
    UseAsMapIndex = None
    value__ = None


class StreamCollectBodies(StreamAcad):
    """ StreamCollectBodies(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetBody(self):
        """ GetBody(self: StreamCollectBodies) -> Body """
        pass

    def GetBodyCopy(self):
        """ GetBodyCopy(self: StreamCollectBodies) -> Body """
        pass

    def InitializeBody(self):
        """ InitializeBody(self: StreamCollectBodies) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class StreamCollectClipBodies(StreamAcad):
    """ StreamCollectClipBodies(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetCollectedGraphics(self):
        """ GetCollectedGraphics(self: StreamCollectClipBodies) -> Array[GraphicsStorage] """
        pass

    def SetBodyClipVolume(self, bodyFilter):
        """ SetBodyClipVolume(self: StreamCollectClipBodies, bodyFilter: Body) """
        pass

    def SetCalculateShrinkwrap(self, value, toShrinkwrapPlane, continueExistingShrinkwrap=None):
        """ SetCalculateShrinkwrap(self: StreamCollectClipBodies, value: bool, toShrinkwrapPlane: Matrix3d, continueExistingShrinkwrap: bool)SetCalculateShrinkwrap(self: StreamCollectClipBodies, value: bool, toShrinkwrapPlane: Matrix3d) """
        pass

    def SetRetainBodies(self, value):
        """ SetRetainBodies(self: StreamCollectClipBodies, value: bool) """
        pass

    def SetSkipAnnotationObjects(self, value):
        """ SetSkipAnnotationObjects(self: StreamCollectClipBodies, value: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BackfaceCullSurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackfaceCullSurfaceHatching(self: StreamCollectClipBodies) -> bool

Set: BackfaceCullSurfaceHatching(self: StreamCollectClipBodies) = value
"""

    CalculateShrinkwrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CalculateShrinkwrap(self: StreamCollectClipBodies) -> bool

"""

    ShrinkwrapProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShrinkwrapProfile(self: StreamCollectClipBodies) -> Profile

"""



class StreamCollectMaterials(StreamAcad):
    """ StreamCollectMaterials(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetBody(self, materialId):
        """ GetBody(self: StreamCollectMaterials, materialId: ObjectId) -> Body """
        pass

    def GetFaceOnPoint(self, wcsPickPoint, materialId=None, flags=None):
        """
        GetFaceOnPoint(self: StreamCollectMaterials, wcsPickPoint: Point3d) -> FaceScanResults
        GetFaceOnPoint(self: StreamCollectMaterials, wcsPickPoint: Point3d, materialId: ObjectId, flags: SurfaceHatchFlags) -> FaceScanResults
        """
        pass

    def GetFaceScanResults(self):
        """ GetFaceScanResults(self: StreamCollectMaterials) -> FaceScanResults """
        pass

    def GetLineworkScanResult(self):
        """ GetLineworkScanResult(self: StreamCollectMaterials) -> ObjectId """
        pass

    def GetVolume(self, materialId):
        """ GetVolume(self: StreamCollectMaterials, materialId: ObjectId) -> float """
        pass

    def ResetBodies(self):
        """ ResetBodies(self: StreamCollectMaterials) """
        pass

    def SetupFaceScan(self, point):
        """ SetupFaceScan(self: StreamCollectMaterials, point: Point3d) """
        pass

    def SetupLineworkScan(self, point):
        """ SetupLineworkScan(self: StreamCollectMaterials, point: Point3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CombineBodies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CombineBodies(self: StreamCollectMaterials) -> bool

Set: CombineBodies(self: StreamCollectMaterials) = value
"""

    MaterialFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialFilter(self: StreamCollectMaterials) -> ObjectIdCollection

Set: MaterialFilter(self: StreamCollectMaterials) = value
"""

    MaterialIds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialIds(self: StreamCollectMaterials) -> ObjectIdCollection

"""



class StreamColorToPropertiesMap(DisposableWrapper):
    """ StreamColorToPropertiesMap() """
    def DeleteAll(self):
        """ DeleteAll(self: StreamColorToPropertiesMap) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Lookup(self, key):
        """ Lookup(self: StreamColorToPropertiesMap, key: int) -> DisplayComponentEntity """
        pass

    def SetAt(self, key, value, deleteExisting):
        """ SetAt(self: StreamColorToPropertiesMap, key: int, value: DisplayComponentEntity, deleteExisting: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class StreamCurves(StreamAcad):
    """ StreamCurves(db: Database) """
    def CollectDisplayPropertiesForCurves(self, curveIsALine):
        """ CollectDisplayPropertiesForCurves(self: StreamCurves, curveIsALine: bool) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ApplySurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplySurfaceHatching(self: StreamCurves) -> bool

Set: ApplySurfaceHatching(self: StreamCurves) = value
"""

    Arcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arcs(self: StreamCurves) -> Array[CircularArc3d]

"""

    BackfaceCullSurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackfaceCullSurfaceHatching(self: StreamCurves) -> bool

Set: BackfaceCullSurfaceHatching(self: StreamCurves) = value
"""

    CollectArcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectArcs(self: StreamCurves) -> bool

Set: CollectArcs(self: StreamCurves) = value
"""

    CollectDisplayPropertiesInfomationFor2dSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectDisplayPropertiesInfomationFor2dSection(self: StreamCurves) -> bool

Set: CollectDisplayPropertiesInfomationFor2dSection(self: StreamCurves) = value
"""

    DisplayComponentEntityArcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayComponentEntityArcs(self: StreamCurves) -> Array[DisplayComponentEntity]

"""

    DisplayComponentEntityLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayComponentEntityLines(self: StreamCurves) -> Array[DisplayComponentEntity]

"""

    IgnoreHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreHatch(self: StreamCurves) -> bool

Set: IgnoreHatch(self: StreamCurves) = value
"""

    IgnoreText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IgnoreText(self: StreamCurves) -> bool

Set: IgnoreText(self: StreamCurves) = value
"""

    Lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lines(self: StreamCurves) -> Array[LineSegment3d]

"""

    NestedEntityFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NestedEntityFilter(self: StreamCurves) -> ObjectIdCollection

Set: NestedEntityFilter(self: StreamCurves) = value
"""



class StreamEntityType(Enum):
    """ enum StreamEntityType, values: CircularArc (2), EllipticalArc (3), Face (4), Line (1), Pline (0) """
    CircularArc = None
    EllipticalArc = None
    Face = None
    Line = None
    Pline = None
    value__ = None


class StreamExplode(StreamAcad):
    """ StreamExplode(db: Database, entitySet: DBObjectCollection) """
    def AddExplodedEntitiesToCurrentSpace(self):
        """ AddExplodedEntitiesToCurrentSpace(self: StreamExplode) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def PackageExplodedEntities(self):
        """ PackageExplodedEntities(self: StreamExplode) """
        pass

    def PackageExplodedEntitiesAndReturnBlockId(self):
        """ PackageExplodedEntitiesAndReturnBlockId(self: StreamExplode) -> ObjectId """
        pass

    def ResetEntityArrays(self):
        """ ResetEntityArrays(self: StreamExplode) """
        pass

    def SetForBoundarySearch(self, value):
        """ SetForBoundarySearch(self: StreamExplode, value: bool) """
        pass

    def SetLocalTransform(self, matrix):
        """ SetLocalTransform(self: StreamExplode, matrix: Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db, entitySet):
        """
        __new__(cls: type, db: Database, entitySet: DBObjectCollection)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    IsVisualExplode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisualExplode(self: StreamExplode) -> bool

Set: IsVisualExplode(self: StreamExplode) = value
"""

    UseFaceAndEdgeParamsWhileDrawingMesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseFaceAndEdgeParamsWhileDrawingMesh(self: StreamExplode) -> bool

Set: UseFaceAndEdgeParamsWhileDrawingMesh(self: StreamExplode) = value
"""



class StreamExtent(StreamAcad):
    """ StreamExtent(db: Database) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def PopTextStrokingStatus(self):
        """ PopTextStrokingStatus(self: StreamExtent) """
        pass

    def PushTextStrokingStatus(self, isTextStrokingOn):
        """ PushTextStrokingStatus(self: StreamExtent, isTextStrokingOn: bool) """
        pass

    def SetIncludeLiveSectionInExtent(self, isInclude):
        """ SetIncludeLiveSectionInExtent(self: StreamExtent, isInclude: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AllowMText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowMText(self: StreamExtent) -> bool

Set: AllowMText(self: StreamExtent) = value
"""

    Extents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extents(self: StreamExtent) -> BoundBox3d

"""

    TextStrokingStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStrokingStatus(self: StreamExtent) -> bool

"""



class StreamIntersect(StreamAcad):
    """ StreamIntersect(db: Database, gsMarker: IntPtr) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IntersectWith(self, otherPipe, points):
        """ IntersectWith(self: StreamIntersect, otherPipe: StreamIntersect, points: Point3dCollection) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db, gsMarker):
        """
        __new__(cls: type, db: Database, gsMarker: IntPtr)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    GsSelectionMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GsSelectionMarker(self: StreamIntersect) -> IntPtr

"""



class StreamSlice(StreamCollectBodies):
    """
    StreamSlice(db: Database, plane: Plane)
    StreamSlice(db: Database, origin: Point3d, uDirection: Vector3d, vDirection: Vector3d)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetProfile(self):
        """ GetProfile(self: StreamSlice) -> Profile """
        pass

    def SetCopyAttributes(self, yesNo):
        """ SetCopyAttributes(self: StreamSlice, yesNo: bool) """
        pass

    def SetPlane(self, plane):
        """ SetPlane(self: StreamSlice, plane: Plane) """
        pass

    def SetReconstructArcs(self, yesNo):
        """ SetReconstructArcs(self: StreamSlice, yesNo: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db, *__args):
        """
        __new__(cls: type, db: Database, plane: Plane)
        __new__(cls: type, db: Database, origin: Point3d, uDirection: Vector3d, vDirection: Vector3d)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class StreamVector(StreamAcad):
    """
    StreamVector(db: Database, blockRecord: BlockTableRecord)
    StreamVector(db: Database)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db, blockRecord=None):
        """
        __new__(cls: type, db: Database, blockRecord: BlockTableRecord)
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ApplySurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ApplySurfaceHatching(self: StreamVector) -> bool

Set: ApplySurfaceHatching(self: StreamVector) = value
"""

    BackfaceCullSurfaceHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackfaceCullSurfaceHatching(self: StreamVector) -> bool

Set: BackfaceCullSurfaceHatching(self: StreamVector) = value
"""

    Lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lines(self: StreamVector) -> Array[LineSegment3d]

"""



class StringPair(object):
    """
    StringPair(str1: str, str2: str)
    StringPair()
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, str1=None, str2=None):
        """
        __new__(cls: type, str1: str, str2: str)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Left(self: StringPair) -> str

"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Right(self: StringPair) -> str

"""



class StringPairCollection(object):
    """ StringPairCollection(pOp: IStringPairOperation) """
    def Add(self, value):
        """ Add(self: StringPairCollection, value: StringPair) -> int """
        pass

    def Clear(self):
        """ Clear(self: StringPairCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: StringPairCollection, value: StringPair) -> bool
        Contains(self: StringPairCollection, strLeft: str) -> bool
        """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: StringPairCollection, array: Array[StringPair], start: int) """
        pass

    def Get(self, strLeft):
        """ Get(self: StringPairCollection, strLeft: str) -> str """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: StringPairCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: StringPairCollection, value: StringPair) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: StringPairCollection, index: int, value: StringPair) """
        pass

    def Remove(self, *__args):
        """ Remove(self: StringPairCollection, value: StringPair)Remove(self: StringPairCollection, strLeft: str) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: StringPairCollection, index: int) """
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IStringPairOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: StringPairCollection) -> int

"""



class SurfaceHatchFlags(Enum):
    """ enum SurfaceHatchFlags, values: Back (32), Bottom (2), Discard (128), Front (16), Left (8), NoHatch (0), Right (4), Section (64), Top (1) """
    Back = None
    Bottom = None
    Discard = None
    Front = None
    Left = None
    NoHatch = None
    Right = None
    Section = None
    Top = None
    value__ = None


class SurfaceMappingType(Enum):
    """ enum SurfaceMappingType, values: AsSurfaceHatch (2), DefaultMapping (0), FaceMapping (1) """
    AsSurfaceHatch = None
    DefaultMapping = None
    FaceMapping = None
    value__ = None


class TextNote(DBObject):
    """ TextNote() """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetStandardNote(instance):
        """ GetStandardNote(instance: DBObject) -> str """
        pass

    @staticmethod
    def SetStandardNote(instance, note):
        """ SetStandardNote(instance: DBObject, note: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Note = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Note(self: TextNote) -> str

Set: Note(self: TextNote) = value
"""


    ExtensionDictionaryName = 'AEC_TEXT_NOTE'


class ThemeSymbolType(Enum):
    """ enum ThemeSymbolType, values: ThemeSymbolCircle (1), ThemeSymbolSquare (0) """
    ThemeSymbolCircle = None
    ThemeSymbolSquare = None
    value__ = None


class UnitType(ImpObject):
    """
    UnitType(value: UnitType)
    UnitType(type: BuiltInUnit, exponent: int)
    UnitType()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetTypeDisplayName(self, getLocalized):
        """ GetTypeDisplayName(self: UnitType, getLocalized: bool) -> str """
        pass

    def IsCompatible(self, value):
        """ IsCompatible(self: UnitType, value: UnitType) -> bool """
        pass

    def IsSimpleUnit(self, unit):
        """ IsSimpleUnit(self: UnitType, unit: BuiltInUnit) -> bool """
        pass

    def PluralName(self, getLocalized):
        """ PluralName(self: UnitType, getLocalized: bool) -> str """
        pass

    def SingularName(self, getLocalized):
        """ SingularName(self: UnitType, getLocalized: bool) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, value: UnitType)
        __new__(cls: type, type: BuiltInUnit, exponent: int)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    InternalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalName(self: UnitType) -> str

"""

    IsImperial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsImperial(self: UnitType) -> bool

"""

    IsMetric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMetric(self: UnitType) -> bool

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: UnitType) -> UnitStatus

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: UnitType) -> BuiltInType

"""



class UnitVariable(ImpObject):
    """
    UnitVariable(unitVariable: UnitVariable)
    UnitVariable(value: float, type: UnitType, exponent: int)
    UnitVariable()
    """
    @staticmethod
    def Convert(from, toUnit):
        """ Convert(from: UnitVariable, toUnit: UnitType) -> UnitVariable """
        pass

    def ConvertTo(self, toUnit):
        """ ConvertTo(self: UnitVariable, toUnit: UnitType) -> UnitStatus """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IsCompatible(self, *__args):
        """
        IsCompatible(self: UnitVariable, other: UnitVariable) -> bool
        IsCompatible(self: UnitVariable, type: UnitType) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, unitVariable: UnitVariable)
        __new__(cls: type, value: float, type: UnitType, exponent: int)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: UnitVariable) -> UnitStatus

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: UnitVariable) -> UnitType

Set: Type(self: UnitVariable) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: UnitVariable) -> float

Set: Value(self: UnitVariable) = value
"""



class Utility(object):
    """ Utility() """
    @staticmethod
    def CanDeleteCurrentAnnotationScale(A_0):
        """ CanDeleteCurrentAnnotationScale(A_0: ObjectId) -> bool """
        pass

    @staticmethod
    def FindAnonymousBlockLastCreated(db):
        """ FindAnonymousBlockLastCreated(db: Database) -> ObjectId """
        pass

    @staticmethod
    def GetAutomaticallyBoundSpaces(object, blockRefPath, boundSpaces):
        """ GetAutomaticallyBoundSpaces(object: DBObject, blockRefPath: ObjectIdCollection) -> AutomaticSpaceBoundary """
        pass

    @staticmethod
    def GetCurrentSupportedAnnotationScales(A_0):
        """ GetCurrentSupportedAnnotationScales(A_0: ObjectId) -> ObjectIdCollection """
        pass

    @staticmethod
    def IsSectionedBodyDisplayDisabled(db):
        """ IsSectionedBodyDisplayDisabled(db: Database) -> bool """
        pass

    @staticmethod
    def MassElementHasFacesToJoin(massElementId):
        """ MassElementHasFacesToJoin(massElementId: ObjectId) -> bool """
        pass

    @staticmethod
    def SetAutomaticallyBoundSpaces(object, blockRefPath, boundSpaces):
        """ SetAutomaticallyBoundSpaces(object: DBObject, blockRefPath: ObjectIdCollection, boundSpaces: AutomaticSpaceBoundary) """
        pass

    @staticmethod
    def SetLayer(entity, layerKey):
        """ SetLayer(entity: Entity, layerKey: str) """
        pass


class UVLayoutModeType(Enum):
    """ enum UVLayoutModeType, values: Manual (0), Repeat (1), SpaceEvenly (2) """
    Manual = None
    Repeat = None
    SpaceEvenly = None
    value__ = None


class ViewDependentCombination(object):
    """ ViewDependentCombination(direction: Vector3d, setId: ObjectId) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, direction, setId):
        """
        __new__[ViewDependentCombination]() -> ViewDependentCombination
        
        __new__(cls: type, direction: Vector3d, setId: ObjectId)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: ViewDependentCombination) -> Vector3d

Set: Direction(self: ViewDependentCombination) = value
"""

    SetId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SetId(self: ViewDependentCombination) -> ObjectId

Set: SetId(self: ViewDependentCombination) = value
"""



class ViewDependentCombinationCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: ViewDependentCombinationCollection, item: ViewDependentCombination) -> int """
        pass

    def Clear(self):
        """ Clear(self: ViewDependentCombinationCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: ViewDependentCombinationCollection, item: ViewDependentCombination) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: ViewDependentCombinationCollection, array: Array[ViewDependentCombination], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ViewDependentCombinationCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: ViewDependentCombinationCollection, item: ViewDependentCombination) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: ViewDependentCombinationCollection, index: int, item: ViewDependentCombination) """
        pass

    def Remove(self, item):
        """ Remove(self: ViewDependentCombinationCollection, item: ViewDependentCombination) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ViewDependentCombinationCollection, index: int) """
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
    """Get: Count(self: ViewDependentCombinationCollection) -> int

"""



class ViewDirection(Enum):
    """ enum ViewDirection, values: Back (3), Bottom (1), Front (2), Left (4), Other (6), Right (5), Top (0) """
    Back = None
    Bottom = None
    Front = None
    Left = None
    Other = None
    Right = None
    Top = None
    value__ = None


class XReferenceSubCommandType(Enum):
    """ enum XReferenceSubCommandType, values: Attach (0), Bind (1), Detach (3), NoSubCommand (7), Overlay (4), Path (2), Reload (5), Unload (6) """
    Attach = None
    Bind = None
    Detach = None
    NoSubCommand = None
    Overlay = None
    Path = None
    Reload = None
    Unload = None
    value__ = None


class YAlignment(Enum):
    """ enum YAlignment, values: BackFlush (2), Centered (0), FrontFlush (1) """
    BackFlush = None
    Centered = None
    FrontFlush = None
    value__ = None


