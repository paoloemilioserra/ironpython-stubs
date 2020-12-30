# encoding: utf-8
# module Autodesk.AutoCAD.BoundaryRepresentation calls itself BoundaryRepresentation
# from acdbmgdbrep, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BrepEntity(RXObject):
    # no doc
    def CheckEntity(self):
        """ CheckEntity(self: BrepEntity) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: BrepEntity, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: BrepEntity) -> int """
        pass

    def GetLineContainment(self, line, numHitsWanted):
        """ GetLineContainment(self: BrepEntity, line: LinearEntity3d, numHitsWanted: int) -> Array[Hit] """
        pass

    def GetMassProperties(self, density=None, tolRequired=None, tolAchieved=None):
        """
        GetMassProperties(self: BrepEntity, density: float, tolRequired: float) -> MassProperties
        GetMassProperties(self: BrepEntity, density: float, tolRequired: float) -> (MassProperties, float)
        GetMassProperties(self: BrepEntity) -> MassProperties
        GetMassProperties(self: BrepEntity, density: float) -> MassProperties
        """
        pass

    def GetPerimeterLength(self, tolRequired=None, tolAchieved=None):
        """
        GetPerimeterLength(self: BrepEntity, tolRequired: float) -> (float, float)
        GetPerimeterLength(self: BrepEntity, tolRequired: float) -> float
        GetPerimeterLength(self: BrepEntity) -> float
        """
        pass

    def GetPointContainment(self, point, containment):
        """ GetPointContainment(self: BrepEntity, point: Point3d) -> (BrepEntity, PointContainment) """
        pass

    def GetSurfaceArea(self, tolRequired=None, tolAchieved=None):
        """
        GetSurfaceArea(self: BrepEntity, tolRequired: float) -> (float, float)
        GetSurfaceArea(self: BrepEntity, tolRequired: float) -> float
        GetSurfaceArea(self: BrepEntity) -> float
        """
        pass

    def GetVolume(self, tolRequired=None, tolAchieved=None):
        """
        GetVolume(self: BrepEntity, tolRequired: float) -> (float, float)
        GetVolume(self: BrepEntity, tolRequired: float) -> float
        GetVolume(self: BrepEntity) -> float
        """
        pass

    BoundBlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundBlock(self: BrepEntity) -> BoundBlock3d

"""

    Brep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Brep(self: BrepEntity) -> Brep

"""

    IsBrepChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBrepChanged(self: BrepEntity) -> bool

"""

    IsNull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNull(self: BrepEntity) -> bool

"""

    SubentityPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubentityPath(self: BrepEntity) -> FullSubentityPath

"""

    ValidationLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidationLevel(self: BrepEntity) -> ValidationLevel

Set: ValidationLevel(self: BrepEntity) = value
"""



class BoundaryLoop(BrepEntity):
    """ BoundaryLoop(fullPath: FullSubentityPath) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEdgesStartingFrom(self, startFrom):
        """ GetEdgesStartingFrom(self: BoundaryLoop, startFrom: Edge) -> LoopEdgeCollection """
        pass

    def GetVerticesStartingFrom(self, startFrom):
        """ GetVerticesStartingFrom(self: BoundaryLoop, startFrom: Vertex) -> LoopVertexCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fullPath):
        """ __new__(cls: type, fullPath: FullSubentityPath) """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: BoundaryLoop) -> LoopEdgeCollection

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: BoundaryLoop) -> Face

"""

    LoopType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoopType(self: BoundaryLoop) -> LoopType

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: BoundaryLoop) -> LoopVertexCollection

"""



class Brep(BrepEntity):
    """
    Brep(fullPath: FullSubentityPath)
    Brep(entity: Entity)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetComplexsStartingFrom(self, startFrom):
        """ GetComplexsStartingFrom(self: Brep, startFrom: Complex) -> BrepComplexCollection """
        pass

    def GetEdgesStartingFrom(self, startFrom):
        """ GetEdgesStartingFrom(self: Brep, startFrom: Edge) -> BrepEdgeCollection """
        pass

    def GetFacesStartingFrom(self, startFrom):
        """ GetFacesStartingFrom(self: Brep, startFrom: Face) -> BrepFaceCollection """
        pass

    def GetShellsStartingFrom(self, startFrom):
        """ GetShellsStartingFrom(self: Brep, startFrom: Shell) -> BrepShellCollection """
        pass

    def GetVerticesStartingFrom(self, startFrom):
        """ GetVerticesStartingFrom(self: Brep, startFrom: Vertex) -> BrepVertexCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, fullPath: FullSubentityPath)
        __new__(cls: type, entity: Entity)
        """
        pass

    Complexes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Complexes(self: Brep) -> BrepComplexCollection

"""

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Brep) -> BrepEdgeCollection

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Brep) -> BrepFaceCollection

"""

    Shells = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shells(self: Brep) -> BrepShellCollection

"""

    Solid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Solid(self: Brep) -> Solid3d

"""

    Surf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surf(self: Brep) -> Surface

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Brep) -> BrepVertexCollection

"""



class BrepComplexCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: BrepComplexCollection) -> BrepComplexEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Complex](enumerable: IEnumerable[Complex], value: Complex) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class EnumeratorBase(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def MoveNext(self):
        """ MoveNext(self: EnumeratorBase) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: EnumeratorBase) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    BrepChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BrepChanged(self: EnumeratorBase) -> bool

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsNull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNull(self: EnumeratorBase) -> bool

"""

    ValidationLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidationLevel(self: EnumeratorBase) -> ValidationLevel

Set: ValidationLevel(self: EnumeratorBase) = value
"""



class BrepComplexEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Complex](enumerator: IEnumerator[Complex], value: Complex) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: BrepComplexEnumerator) -> Complex

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BrepEdgeCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: BrepEdgeCollection) -> BrepEdgeEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Edge](enumerable: IEnumerable[Edge], value: Edge) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class BrepEdgeEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Edge](enumerator: IEnumerator[Edge], value: Edge) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: BrepEdgeEnumerator) -> Edge

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BrepFaceCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: BrepFaceCollection) -> BrepFaceEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Face](enumerable: IEnumerable[Face], value: Face) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class BrepFaceEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Face](enumerator: IEnumerator[Face], value: Face) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: BrepFaceEnumerator) -> Face

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BrepShellCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: BrepShellCollection) -> BrepShellEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Shell](enumerable: IEnumerable[Shell], value: Shell) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class BrepShellEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Shell](enumerator: IEnumerator[Shell], value: Shell) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: BrepShellEnumerator) -> Shell

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class BrepVertexCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: BrepVertexCollection) -> BrepVertexEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vertex](enumerable: IEnumerable[Vertex], value: Vertex) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class BrepVertexEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vertex](enumerator: IEnumerator[Vertex], value: Vertex) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: BrepVertexEnumerator) -> Vertex

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Complex(BrepEntity):
    """ Complex(fullPath: FullSubentityPath) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetShellsStartingFrom(self, startFrom):
        """ GetShellsStartingFrom(self: Complex, startFrom: Shell) -> ComplexShellCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fullPath):
        """ __new__(cls: type, fullPath: FullSubentityPath) """
        pass

    Shells = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shells(self: Complex) -> ComplexShellCollection

"""



class ComplexShellCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ComplexShellCollection) -> ComplexShellEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Shell](enumerable: IEnumerable[Shell], value: Shell) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ComplexShellEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Shell](enumerator: IEnumerator[Shell], value: Shell) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: ComplexShellEnumerator) -> Shell

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Edge(BrepEntity):
    """ Edge(fullPath: FullSubentityPath) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetCurveAsNurb(self, fitTolRequired=None, fitTolAchieved=None):
        """
        GetCurveAsNurb(self: Edge, fitTolRequired: float) -> (NurbCurve3d, float)
        GetCurveAsNurb(self: Edge, fitTolRequired: float) -> NurbCurve3d
        GetCurveAsNurb(self: Edge) -> NurbCurve3d
        """
        pass

    def GetLoopsStartingFrom(self, startFrom):
        """ GetLoopsStartingFrom(self: Edge, startFrom: BoundaryLoop) -> EdgeLoopCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fullPath):
        """ __new__(cls: type, fullPath: FullSubentityPath) """
        pass

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: Edge) -> Curve3d

"""

    IsOrientToCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOrientToCurve(self: Edge) -> bool

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: Edge) -> EdgeLoopCollection

"""

    Vertex1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex1(self: Edge) -> Vertex

"""

    Vertex2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex2(self: Edge) -> Vertex

"""



class EdgeLoopCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: EdgeLoopCollection) -> EdgeLoopEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BoundaryLoop](enumerable: IEnumerable[BoundaryLoop], value: BoundaryLoop) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class EdgeLoopEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BoundaryLoop](enumerator: IEnumerator[BoundaryLoop], value: BoundaryLoop) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: EdgeLoopEnumerator) -> BoundaryLoop

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MeshEntity(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: MeshEntity, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MeshEntity) -> int """
        pass

    EntityAssociated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityAssociated(self: MeshEntity) -> BrepEntity

"""

    IsBrepChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBrepChanged(self: MeshEntity) -> bool

"""

    IsNull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNull(self: MeshEntity) -> bool

"""

    ValidationLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidationLevel(self: MeshEntity) -> ValidationLevel

Set: ValidationLevel(self: MeshEntity) = value
"""



class Element(MeshEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class Element2d(Element):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetNodesStartingFrom(self, startFrom):
        """ GetNodesStartingFrom(self: Element2d, startFrom: Node) -> Element2dNodeCollection """
        pass

    Nodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nodes(self: Element2d) -> Element2dNodeCollection

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Element2d) -> Vector3d

"""



class Element2dNodeCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: Element2dNodeCollection) -> Element2dNodeEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Node](enumerable: IEnumerable[Node], value: Node) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class Element2dNodeEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Node](enumerator: IEnumerator[Node], value: Node) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: Element2dNodeEnumerator) -> Node

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Element2dShape(Enum):
    """ enum Element2dShape, values: AllPolygons (1), AllQuadrilaterals (2), AllTriangles (3), Default (0) """
    AllPolygons = None
    AllQuadrilaterals = None
    AllTriangles = None
    Default = None
    value__ = None


class ErrorStatus(Enum):
    """ enum ErrorStatus, values: AmbiguousOutput (5), BrepChanged (3008), DegenerateTopology (3020), InvalidInput (3), InvalidObject (123), MissingGeometry (153), MissingSubentity (137), NotApplicable (2), NotImplementedYet (1), NullObjectId (16), NullObjectPointer (123), NullSubentityId (24), ObjectIdMismatch (35), Ok (0), OutOfMemory (6), TopologyMismatch (35), UninitialisedObject (3021), UnsuitableGeometry (5), UnsuitableTopology (3013), WrongObjectType (34), WrongSubentityType (230) """
    AmbiguousOutput = None
    BrepChanged = None
    DegenerateTopology = None
    InvalidInput = None
    InvalidObject = None
    MissingGeometry = None
    MissingSubentity = None
    NotApplicable = None
    NotImplementedYet = None
    NullObjectId = None
    NullObjectPointer = None
    NullSubentityId = None
    ObjectIdMismatch = None
    Ok = None
    OutOfMemory = None
    TopologyMismatch = None
    UninitialisedObject = None
    UnsuitableGeometry = None
    UnsuitableTopology = None
    value__ = None
    WrongObjectType = None
    WrongSubentityType = None


class Exception(Exception):
    """
    Exception(es: ErrorStatus, message: str, innerException: Exception)
    Exception(es: ErrorStatus, message: str)
    Exception(es: ErrorStatus)
    Exception()
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: Exception, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, es=None, message=None, innerException=None):
        """
        __new__(cls: type, es: ErrorStatus, message: str, innerException: Exception)
        __new__(cls: type, es: ErrorStatus, message: str)
        __new__(cls: type, es: ErrorStatus)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    ErrorStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorStatus(self: Exception) -> ErrorStatus

Set: ErrorStatus(self: Exception) = value
"""



class Face(BrepEntity):
    """ Face(fullPath: FullSubentityPath) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetArea(self, tolRequired=None, tolAchieved=None):
        """
        GetArea(self: Face, tolRequired: float) -> (float, float)
        GetArea(self: Face, tolRequired: float) -> float
        GetArea(self: Face) -> float
        """
        pass

    def GetLoopsStartingFrom(self, startFrom):
        """ GetLoopsStartingFrom(self: Face, startFrom: BoundaryLoop) -> FaceLoopCollection """
        pass

    def GetSurfaceAsNurb(self, fitTolRequired=None, fitTolAchieved=None):
        """
        GetSurfaceAsNurb(self: Face, fitTolRequired: float) -> (NurbSurface, float)
        GetSurfaceAsNurb(self: Face, fitTolRequired: float) -> NurbSurface
        GetSurfaceAsNurb(self: Face) -> NurbSurface
        """
        pass

    def GetSurfaceAsTrimmedNurbs(self):
        """ GetSurfaceAsTrimmedNurbs(self: Face) -> Array[ExternalBoundedSurface] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fullPath):
        """ __new__(cls: type, fullPath: FullSubentityPath) """
        pass

    IsOrientToSurface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOrientToSurface(self: Face) -> bool

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: Face) -> FaceLoopCollection

"""

    Shell = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Shell(self: Face) -> Shell

"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: Face) -> Surface

"""



class FaceLoopCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: FaceLoopCollection) -> FaceLoopEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BoundaryLoop](enumerable: IEnumerable[BoundaryLoop], value: BoundaryLoop) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class FaceLoopEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BoundaryLoop](enumerator: IEnumerator[BoundaryLoop], value: BoundaryLoop) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: FaceLoopEnumerator) -> BoundaryLoop

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Hit(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: Hit, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: Hit) -> int """
        pass

    EntityAssociated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityAssociated(self: Hit) -> BrepEntity

"""

    EntityEntered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityEntered(self: Hit) -> BrepEntity

"""

    EntityHit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EntityHit(self: Hit) -> BrepEntity

"""

    IsBrepChanged = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBrepChanged(self: Hit) -> bool

"""

    IsNull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNull(self: Hit) -> bool

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: Hit) -> Point3d

"""

    ValidationLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValidationLevel(self: Hit) -> ValidationLevel

Set: ValidationLevel(self: Hit) = value
"""



class LoopEdgeCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: LoopEdgeCollection) -> LoopEdgeEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Edge](enumerable: IEnumerable[Edge], value: Edge) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class LoopEdgeEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Edge](enumerator: IEnumerator[Edge], value: Edge) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: LoopEdgeEnumerator) -> Edge

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class LoopType(Enum):
    """ enum LoopType, values: LoopExterior (1), LoopInterior (2), LoopUnclassified (0), LoopWinding (3) """
    LoopExterior = None
    LoopInterior = None
    LoopUnclassified = None
    LoopWinding = None
    value__ = None


class LoopVertexCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: LoopVertexCollection) -> LoopVertexEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vertex](enumerable: IEnumerable[Vertex], value: Vertex) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class LoopVertexEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Vertex](enumerator: IEnumerator[Vertex], value: Vertex) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: LoopVertexEnumerator) -> Vertex

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class MassProperties(object):
    # no doc
    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centroid(self: MassProperties) -> Point3d

"""

    Mass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mass(self: MassProperties) -> float

"""

    MomentsOfIntertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MomentsOfIntertia(self: MassProperties) -> Vector3d

"""

    PrincipalMoments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrincipalMoments(self: MassProperties) -> Vector3d

"""

    ProductsOfIntertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProductsOfIntertia(self: MassProperties) -> Vector3d

"""

    RadiiOfGyration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiiOfGyration(self: MassProperties) -> Vector3d

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: MassProperties) -> float

"""



class Mesh(MeshEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class Mesh2d(Mesh):
    """ Mesh2d(meshFilter: Mesh2dFilter) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetElement2dsStartingFrom(self, startFrom):
        """ GetElement2dsStartingFrom(self: Mesh2d, startFrom: Element2d) -> Mesh2dElement2dCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, meshFilter):
        """ __new__(cls: type, meshFilter: Mesh2dFilter) """
        pass

    Element2ds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Element2ds(self: Mesh2d) -> Mesh2dElement2dCollection

"""



class MeshControl(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, obj):
        """ Equals(self: MeshControl, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MeshControl) -> int """
        pass

    AngleTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleTolerance(self: MeshControl) -> float

Set: AngleTolerance(self: MeshControl) = value
"""

    DistanceTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceTolerance(self: MeshControl) -> float

Set: DistanceTolerance(self: MeshControl) = value
"""

    MaxNodeSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxNodeSpacing(self: MeshControl) -> float

Set: MaxNodeSpacing(self: MeshControl) = value
"""

    MaxSubdivisions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxSubdivisions(self: MeshControl) -> UInt32

Set: MaxSubdivisions(self: MeshControl) = value
"""



class Mesh2dControl(MeshControl):
    """ Mesh2dControl() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    ElementShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementShape(self: Mesh2dControl) -> Element2dShape

Set: ElementShape(self: Mesh2dControl) = value
"""

    MaxAspectRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxAspectRatio(self: Mesh2dControl) -> float

Set: MaxAspectRatio(self: Mesh2dControl) = value
"""



class Mesh2dElement2dCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: Mesh2dElement2dCollection) -> Mesh2dElement2dEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Element2d](enumerable: IEnumerable[Element2d], value: Element2d) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class Mesh2dElement2dEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Element2d](enumerator: IEnumerator[Element2d], value: Element2d) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: Mesh2dElement2dEnumerator) -> Element2d

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Mesh2dFilter(DisposableWrapper):
    """ Mesh2dFilter() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Insert(self, brepEntity, meshControl):
        """ Insert(self: Mesh2dFilter, brepEntity: BrepEntity, meshControl: Mesh2dControl) """
        pass


class Node(MeshEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: Node) -> Point3d

"""



class PointContainment(Enum):
    """ enum PointContainment, values: Inside (0), OnBoundary (2), Outside (1) """
    Inside = None
    OnBoundary = None
    Outside = None
    value__ = None


class Shell(BrepEntity):
    """ Shell(fullPath: FullSubentityPath) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetFacesStartingFrom(self, startFrom):
        """ GetFacesStartingFrom(self: Shell, startFrom: Face) -> ShellFaceCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fullPath):
        """ __new__(cls: type, fullPath: FullSubentityPath) """
        pass

    Complex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Complex(self: Shell) -> Complex

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Shell) -> ShellFaceCollection

"""

    ShellType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShellType(self: Shell) -> ShellType

"""



class ShellFaceCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: ShellFaceCollection) -> ShellFaceEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Face](enumerable: IEnumerable[Face], value: Face) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ShellFaceEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Face](enumerator: IEnumerator[Face], value: Face) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: ShellFaceEnumerator) -> Face

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ShellType(Enum):
    """ enum ShellType, values: ShellExterior (1), ShellInterior (2), ShellUnclassified (0) """
    ShellExterior = None
    ShellInterior = None
    ShellUnclassified = None
    value__ = None


class ValidationLevel(Enum):
    """ enum ValidationLevel, values: FullValidation (0), NoValidation (1) """
    FullValidation = None
    NoValidation = None
    value__ = None


class Vertex(BrepEntity):
    """ Vertex(fullPath: FullSubentityPath) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEdgesStartingFrom(self, startFrom):
        """ GetEdgesStartingFrom(self: Vertex, startFrom: Edge) -> VertexEdgeCollection """
        pass

    def GetLoopsStartingFrom(self, startFrom):
        """ GetLoopsStartingFrom(self: Vertex, startFrom: BoundaryLoop) -> VertexLoopCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, fullPath):
        """ __new__(cls: type, fullPath: FullSubentityPath) """
        pass

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Vertex) -> VertexEdgeCollection

"""

    Loops = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Loops(self: Vertex) -> VertexLoopCollection

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: Vertex) -> Point3d

"""



class VertexEdgeCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: VertexEdgeCollection) -> VertexEdgeEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Edge](enumerable: IEnumerable[Edge], value: Edge) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class VertexEdgeEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Edge](enumerator: IEnumerator[Edge], value: Edge) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: VertexEdgeEnumerator) -> Edge

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class VertexLoopCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: VertexLoopCollection) -> VertexLoopEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BoundaryLoop](enumerable: IEnumerable[BoundaryLoop], value: BoundaryLoop) -> bool """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class VertexLoopEnumerator(EnumeratorBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BoundaryLoop](enumerator: IEnumerator[BoundaryLoop], value: BoundaryLoop) -> bool """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: VertexLoopEnumerator) -> BoundaryLoop

"""

    IEnumeratorCurrent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



