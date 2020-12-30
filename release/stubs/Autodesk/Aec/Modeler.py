# encoding: utf-8
# module Autodesk.Aec.Modeler calls itself Modeler
# from AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null, AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Entity(DisposableWrapper):
    # no doc
    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> Entity """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: Entity) -> UInt32

Set: Flags(self: Entity) = value
"""



class Body(Entity):
    """ Body() """
    @staticmethod
    def Add(body1, body2):
        """ Add(body1: Body, body2: Body) -> Body """
        pass

    def Align(self, source1, source2, *__args):
        """
        Align(self: Body, source1: Point3d, source2: Point3d, source3: Point3d, destination1: Point3d, destination2: Point3d, destination3: Point3d) -> Body
        Align(self: Body, source1: Point3d, source2: Vector3d, source3: Vector3d, destination1: Point3d, destination2: Vector3d, destination3: Vector3d) -> Body
        Align(self: Body, source1: Point3d, source2: Vector3d, destination1: Point3d, destination2: Vector3d) -> Body
        """
        pass

    @staticmethod
    def AxisRevolution(points, vertexData, numberOfVertices, polygonNormal, axis, revolutionAngle, approximation, scaleTwistFixedPoint=None, scaleFactor=None, twistAngle=None):
        """
        AxisRevolution(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, axis: LineSegment3d, revolutionAngle: float, approximation: int, scaleTwistFixedPoint: Point3d, scaleFactor: float, twistAngle: float) -> Body
        AxisRevolution(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, axis: LineSegment3d, revolutionAngle: float, approximation: int, scaleTwistFixedPoint: Point3d, scaleFactor: float) -> Body
        AxisRevolution(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, axis: LineSegment3d, revolutionAngle: float, approximation: int) -> Body
        """
        pass

    def BooleanOperation(self, body, type):
        """ BooleanOperation(self: Body, body: Body, type: BooleanOperatorType) -> Body """
        pass

    @staticmethod
    def Box(corner, sizes):
        """ Box(corner: Point3d, sizes: Vector3d) -> Body """
        pass

    def BreakEdge(self, *__args):
        """
        BreakEdge(self: Body, point: Point3d) -> Edge
        BreakEdge(self: Body, p1: Point3d, p2: Point3d) -> Edge
        """
        pass

    def ChangeVertexCoordinates(self, changedVertices, changedVertexCoordinates, checkPlanarity=None):
        """ ChangeVertexCoordinates(self: Body, changedVertices: Array[Vertex], changedVertexCoordinates: Point3dCollection, checkPlanarity: bool)ChangeVertexCoordinates(self: Body, changedVertices: Array[Vertex], changedVertexCoordinates: Point3dCollection) """
        pass

    def CleanUpNonManifoldEdgesAndCoincidentFaces(self):
        """ CleanUpNonManifoldEdgesAndCoincidentFaces(self: Body) """
        pass

    def ClosestDistanceOfRayIntersection(self, ray, tolerance):
        """ ClosestDistanceOfRayIntersection(self: Body, ray: LineSegment3d, tolerance: float) -> float """
        pass

    def ClosestEntityOfRayIntersection(self, ray, tolerance):
        """ ClosestEntityOfRayIntersection(self: Body, ray: LineSegment3d, tolerance: float) -> Entity """
        pass

    def Combine(self, body):
        """ Combine(self: Body, body: Body) -> Body """
        pass

    @staticmethod
    def Cone(axis, *__args):
        """
        Cone(axis: LineSegment3d, radius1: float, radius2: float, surfaceFacets: int) -> Body
        Cone(axis: LineSegment3d, baseNormal: Vector3d, radius1: float, radius2: float, surfaceFacets: int) -> Body
        """
        pass

    def Contains(self, point):
        """ Contains(self: Body, point: Point3d) -> PointInBodyLocation """
        pass

    def ConvertToTerrainBody(self, height, checkValidity):
        """ ConvertToTerrainBody(self: Body, height: float, checkValidity: bool) -> Array[Face] """
        pass

    @staticmethod
    def ConvexHull(points):
        """ ConvexHull(points: Point3dCollection) -> Body """
        pass

    def Copy(self):
        """ Copy(self: Body) -> Body """
        pass

    def CopyGeometryFrom(self, body, matrix=None):
        """ CopyGeometryFrom(self: Body, body: Body, matrix: Matrix3d)CopyGeometryFrom(self: Body, body: Body) """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> Body """
        pass

    @staticmethod
    def Cylinder(axis, *__args):
        """
        Cylinder(axis: LineSegment3d, radius: float, surfaceFacets: int) -> Body
        Cylinder(axis: LineSegment3d, baseNormal: Vector3d, radius: float, surfaceFacets: int) -> Body
        """
        pass

    def DecomposeIntoLumps(self):
        """ DecomposeIntoLumps(self: Body) -> BodyCollection """
        pass

    def DeleteEmptyFaces(self):
        """ DeleteEmptyFaces(self: Body) """
        pass

    def DeleteFaceIntervals(self):
        """ DeleteFaceIntervals(self: Body) """
        pass

    def DeleteFaceIntervalsAndPlanes(self):
        """ DeleteFaceIntervalsAndPlanes(self: Body) """
        pass

    def DeleteMarkedCurves(self, flag):
        """ DeleteMarkedCurves(self: Body, flag: UInt32) """
        pass

    def DeleteMarkedFaces(self, flag):
        """ DeleteMarkedFaces(self: Body, flag: UInt32) """
        pass

    def DeleteMarkedSurfaces(self, flag):
        """ DeleteMarkedSurfaces(self: Body, flag: UInt32) """
        pass

    def DeleteMarkedVertices(self, flag):
        """ DeleteMarkedVertices(self: Body, flag: UInt32) """
        pass

    def DeleteUnusedVerticesSurfacesCurves(self):
        """ DeleteUnusedVerticesSurfacesCurves(self: Body) """
        pass

    def DeleteVertexSurfaceData(self):
        """ DeleteVertexSurfaceData(self: Body) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def EndPointRevolution(points, vertexData, numberOfVertices, polygonNormal, revolutionAngle, approximation):
        """ EndPointRevolution(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, revolutionAngle: float, approximation: int) -> Body """
        pass

    @staticmethod
    def Equals(*__args):
        """ Equals(body1: Body, body2: Body) -> bool """
        pass

    def EvaluateVertexSurfaceData(self):
        """ EvaluateVertexSurfaceData(self: Body) """
        pass

    def ExtractFace(self, faceToExtract=None):
        """
        ExtractFace(self: Body, faceToExtract: Face) -> Body
        ExtractFace(self: Body) -> Body
        """
        pass

    def ExtractShell(self, faceInTheShell=None):
        """
        ExtractShell(self: Body, faceInTheShell: Face) -> Body
        ExtractShell(self: Body) -> Body
        """
        pass

    @staticmethod
    def Extrusion(points, vertexData, numberOfVertices, polygonNormal, extrusionVector, scaleTwistFixedPoint=None, scaleFactor=None, twistAngle=None):
        """
        Extrusion(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, extrusionVector: Vector3d, scaleTwistFixedPoint: Point3d, scaleFactor: float, twistAngle: float) -> Body
        Extrusion(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, extrusionVector: Vector3d, scaleTwistFixedPoint: Point3d, scaleFactor: float) -> Body
        Extrusion(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, extrusionVector: Vector3d) -> Body
        """
        pass

    @staticmethod
    def ExtrusionAlongPath(startProfile, endProfile, pathPolygon, pathVertexData, numberOfPathVertices, pathIsClosed, checkBodyValidity=None, scaleTwistFixedPoint=None, scaleFactor=None, twistAngle=None, morphingMap=None, calculateMorphingMapAutomatically=None, startProfileSignificantVertices=None, endProfileSignificantVertices=None):
        """
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool, scaleTwistFixedPoint: Point3d, scaleFactor: float, twistAngle: float, morphingMap: MorphingMap, calculateMorphingMapAutomatically: bool) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool, scaleTwistFixedPoint: Point3d, scaleFactor: float, twistAngle: float, morphingMap: MorphingMap) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool, scaleTwistFixedPoint: Point3d, scaleFactor: float, twistAngle: float, morphingMap: MorphingMap, calculateMorphingMapAutomatically: bool, startProfileSignificantVertices: IntegerCollection, endProfileSignificantVertices: IntegerCollection) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool, scaleTwistFixedPoint: Point3d, scaleFactor: float, twistAngle: float, morphingMap: MorphingMap, calculateMorphingMapAutomatically: bool, startProfileSignificantVertices: IntegerCollection) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool, scaleTwistFixedPoint: Point3d, scaleFactor: float, twistAngle: float) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool, scaleTwistFixedPoint: Point3d, scaleFactor: float) -> Body
        ExtrusionAlongPath(startProfile: Body, endProfile: Body, pathPolygon: Point3dCollection, pathVertexData: Array[PolygonVertexData], numberOfPathVertices: int, pathIsClosed: bool, checkBodyValidity: bool, scaleTwistFixedPoint: Point3d) -> Body
        """
        pass

    def FindEdge(self, p1, p2):
        """ FindEdge(self: Body, p1: Point3d, p2: Point3d) -> Edge """
        pass

    def FindFace(self, plane):
        """ FindFace(self: Body, plane: Plane) -> Array[Face] """
        pass

    def FindVertex(self, point):
        """ FindVertex(self: Body, point: Point3d) -> Vertex """
        pass

    def GenerateUnspecifiedSurfaces(self, angleTolerance, minNumberOfFacesInSurface=None):
        """ GenerateUnspecifiedSurfaces(self: Body, angleTolerance: float, minNumberOfFacesInSurface: int)GenerateUnspecifiedSurfaces(self: Body, angleTolerance: float) """
        pass

    def GenerateUnspecifiedSurfacesFromApproximationEdges(self, minNumberOfFacesInSurface=None):
        """ GenerateUnspecifiedSurfacesFromApproximationEdges(self: Body, minNumberOfFacesInSurface: int)GenerateUnspecifiedSurfacesFromApproximationEdges(self: Body) """
        pass

    def GetAllEdgesReferencingVertex(self, value):
        """ GetAllEdgesReferencingVertex(self: Body, value: Vertex) -> Array[Edge] """
        pass

    def GetIsValid(self, level):
        """ GetIsValid(self: Body, level: ValidityCheckingLevel) -> bool """
        pass

    def GetVertexMax(self, dir):
        """ GetVertexMax(self: Body, dir: Vector3d) -> Vertex """
        pass

    def GetVertexMin(self, dir):
        """ GetVertexMin(self: Body, dir: Vector3d) -> Vertex """
        pass

    def MakeArcTessellationsInExtrusionsCoincident(self, referenceExtrusion, extrusionVector):
        """ MakeArcTessellationsInExtrusionsCoincident(self: Body, referenceExtrusion: Body, extrusionVector: Vector3d) -> bool """
        pass

    def MergeCoincidentVertices(self):
        """ MergeCoincidentVertices(self: Body) -> bool """
        pass

    def MergeCoplanarFaces(self, edgeBetweenFaces):
        """ MergeCoplanarFaces(self: Body, edgeBetweenFaces: Edge) """
        pass

    def MergeEqualSurfaces(self):
        """ MergeEqualSurfaces(self: Body) """
        pass

    def Mirror(self, plane):
        """ Mirror(self: Body, plane: Plane) -> Body """
        pass

    def Modified(self):
        """ Modified(self: Body) """
        pass

    def MoveFace(self, faceToMove, vector, keepAdjacentFacePlanesFixed, keepFaceGeometryFixed):
        """ MoveFace(self: Body, faceToMove: Face, vector: Vector3d, keepAdjacentFacePlanesFixed: bool, keepFaceGeometryFixed: bool) -> Face """
        pass

    @staticmethod
    def Multiply(body1, body2):
        """ Multiply(body1: Body, body2: Body) -> Body """
        pass

    @staticmethod
    def Negate(body):
        """ Negate(body: Body) -> Body """
        pass

    @staticmethod
    def Pipe(axis, *__args):
        """
        Pipe(axis: LineSegment3d, outerRadius: float, innerRadius: float, surfaceFacets: int) -> Body
        Pipe(axis: LineSegment3d, baseNormal: Vector3d, outerRadius: float, innerRadius: float, surfaceFacets: int) -> Body
        """
        pass

    @staticmethod
    def PipeConic(axis, *__args):
        """
        PipeConic(axis: LineSegment3d, outerRadius1: float, innerRadius1: float, outerRadius2: float, innerRadius2: float, surfaceFacets: int) -> Body
        PipeConic(axis: LineSegment3d, baseNormal: Vector3d, outerRadius1: float, innerRadius1: float, outerRadius2: float, innerRadius2: float, surfaceFacets: int) -> Body
        """
        pass

    def PlaneIntersectsBody(self, plane):
        """ PlaneIntersectsBody(self: Body, plane: Plane) -> bool """
        pass

    def ProfilesOrdered(self, body):
        """ ProfilesOrdered(self: Body, body: Body) -> bool """
        pass

    @staticmethod
    def Pyramid(points, vertexData, numberOfVertices, polygonNormal, pyramidApex):
        """ Pyramid(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, pyramidApex: Point3d) -> Body """
        pass

    def RayIntersectionStatus(self, ray, tolerance):
        """ RayIntersectionStatus(self: Body, ray: LineSegment3d, tolerance: float) -> RayBodyIntersection """
        pass

    @staticmethod
    def RectangleToCircleReducer(baseCorner, baseSizes, topCircle, surfaceFacets):
        """ RectangleToCircleReducer(baseCorner: Point3d, baseSizes: Vector2d, topCircle: CircularArc3d, surfaceFacets: int) -> Body """
        pass

    @staticmethod
    def ReducingElbow(elbowCenter, endCenter1, endCenter2, endRadius1, endRadius2, majorSurfaceFacets, minorSurfaceFacets):
        """ ReducingElbow(elbowCenter: Point3d, endCenter1: Point3d, endCenter2: Point3d, endRadius1: float, endRadius2: float, majorSurfaceFacets: int, minorSurfaceFacets: int) -> Body """
        pass

    def Rotate(self, axis, angle):
        """ Rotate(self: Body, axis: LineSegment3d, angle: float) -> Body """
        pass

    def SaveToSAT(self, fileName, colorsAlso=None):
        """ SaveToSAT(self: Body, fileName: str, colorsAlso: bool)SaveToSAT(self: Body, fileName: str) """
        pass

    def Scale(self, fixedPoint, *__args):
        """
        Scale(self: Body, fixedPoint: Point3d, factor: float) -> Body
        Scale(self: Body, fixedPoint: Point3d, xyzFactors: Vector3d) -> Body
        """
        pass

    def Section(self, plane, keepInputBodyWhenFails):
        """ Section(self: Body, plane: Plane, keepInputBodyWhenFails: bool) """
        pass

    def SetApproximatingEdgeAndBridgeEdgeFlags(self, mark=None):
        """ SetApproximatingEdgeAndBridgeEdgeFlags(self: Body, mark: bool)SetApproximatingEdgeAndBridgeEdgeFlags(self: Body) """
        pass

    def SetColor(self, value):
        """ SetColor(self: Body, value: ColorType) """
        pass

    def SetCurveFlags(self, tag, flag):
        """ SetCurveFlags(self: Body, tag: OnOff, flag: UInt32) """
        pass

    def SetEdgeFlags(self, tag, flag):
        """ SetEdgeFlags(self: Body, tag: OnOff, flag: UInt32) """
        pass

    def SetFaceFlags(self, tag, flag):
        """ SetFaceFlags(self: Body, tag: OnOff, flag: UInt32) """
        pass

    def SetHiddenLineParameters(self, display=None, displayApproximationEdges=None, displayBridgeEdges=None):
        """ SetHiddenLineParameters(self: Body, display: HiddenLinesDisplay, displayApproximationEdges: bool)SetHiddenLineParameters(self: Body, display: HiddenLinesDisplay, displayApproximationEdges: bool, displayBridgeEdges: bool)SetHiddenLineParameters(self: Body)SetHiddenLineParameters(self: Body, display: HiddenLinesDisplay) """
        pass

    def SetSurfaceFlags(self, tag, flag):
        """ SetSurfaceFlags(self: Body, tag: OnOff, flag: UInt32) """
        pass

    def SetVertexFlags(self, tag, flag):
        """ SetVertexFlags(self: Body, tag: OnOff, flag: UInt32) """
        pass

    @staticmethod
    def Skin(profiles, numberOfProfiles, isClosed, checkPlanarity, morphingMaps, markInnerProfileEdgesAsApproximation, checkInputProfiles):
        """ Skin(profiles: BodyCollection, numberOfProfiles: int, isClosed: bool, checkPlanarity: bool, morphingMaps: Array[MorphingMap], markInnerProfileEdgesAsApproximation: bool, checkInputProfiles: bool) -> Body """
        pass

    @staticmethod
    def Sphere(center, radius, surfaceFacets):
        """ Sphere(center: Point3d, radius: float, surfaceFacets: int) -> Body """
        pass

    def StitchFaces(self, splitEdges=None, orientFaces=None, addMissingFaces=None):
        """ StitchFaces(self: Body, splitEdges: bool, orientFaces: bool)StitchFaces(self: Body, splitEdges: bool, orientFaces: bool, addMissingFaces: bool)StitchFaces(self: Body)StitchFaces(self: Body, splitEdges: bool) """
        pass

    def Stretch(self, line):
        """ Stretch(self: Body, line: LineSegment3d) -> Body """
        pass

    @staticmethod
    def Subtract(*__args):
        """
        Subtract(body1: Body, body2: Body) -> Body
        Subtract(body: Body, plane: Plane) -> Body
        """
        pass

    @staticmethod
    def Tetrahedron(points):
        """ Tetrahedron(points: Point3dCollection) -> Body """
        pass

    @staticmethod
    def Torus(axis, majorRadius, minorRadius, majorSurfaceFacets, minorSurfaceFacets):
        """ Torus(axis: LineSegment3d, majorRadius: float, minorRadius: float, majorSurfaceFacets: int, minorSurfaceFacets: int) -> Body """
        pass

    @staticmethod
    def TorusExtension(axis, majorRadius, minorRadius, majorSurfaceFacets, minorSurfaceFacets):
        """ TorusExtension(axis: LineSegment3d, majorRadius: float, minorRadius: float, majorSurfaceFacets: int, minorSurfaceFacets: int) -> Body """
        pass

    def Transform(self, matrix):
        """ Transform(self: Body, matrix: Matrix3d) -> Body """
        pass

    def Translate(self, vector):
        """ Translate(self: Body, vector: Vector3d) -> Body """
        pass

    def TriangulateAllFaces(self):
        """ TriangulateAllFaces(self: Body) """
        pass

    def TriangulateFace(self, face):
        """ TriangulateFace(self: Body, face: Face) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(body1: Body, body2: Body) -> Body """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(body1: Body, body2: Body) -> Body """
        pass

    def __rsub__(self, *args): #cannot find CLR method
        """ __rsub__(body1: Body, body2: Body) -> Body """
        pass

    def __sub__(self, *args): #cannot find CLR method
        """ x.__sub__(y) <==> x-yx.__sub__(y) <==> x-y """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Body) -> float

"""

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centroid(self: Body) -> Point3d

"""

    ContainsNonManifoldEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContainsNonManifoldEdges(self: Body) -> bool

"""

    Curves = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curves(self: Body) -> CurveCollection

"""

    Faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Faces(self: Body) -> FaceCollection

"""

    Interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interval(self: Body) -> Point3dCollection

"""

    IsNegated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNegated(self: Body) -> bool

"""

    IsNull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNull(self: Body) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Body) -> bool

"""

    Moments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Moments(self: Body) -> Point3d

"""

    Next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Next(self: Body) -> Body

Set: Next(self: Body) = value
"""

    PhysicalEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhysicalEdges(self: Body) -> Array[Edge]

"""

    PhysicalVertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PhysicalVertices(self: Body) -> Array[Vertex]

"""

    Products = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Products(self: Body) -> Point3d

"""

    Surfaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surfaces(self: Body) -> SurfaceCollection

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Body) -> VertexCollection

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: Body) -> float

"""



class BodyCollection(DisposableWrapper):
    """ BodyCollection() """
    def Add(self, value):
        """ Add(self: BodyCollection, value: Body) -> int """
        pass

    def Clear(self):
        """ Clear(self: BodyCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: BodyCollection, value: Body) -> bool """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: BodyCollection, array: Array[Body], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BodyCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: BodyCollection, value: Body) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: BodyCollection, index: int, value: Body) """
        pass

    def Remove(self, value):
        """ Remove(self: BodyCollection, value: Body) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: BodyCollection, index: int) """
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
    """Get: Count(self: BodyCollection) -> int

"""



class BooleanOperatorType(Enum):
    """ enum BooleanOperatorType, values: Intersect (2), Subtract (1), Unite (0) """
    Intersect = None
    Subtract = None
    Unite = None
    value__ = None


class Curve(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Transform(self, matrix, transfType=None, stretchVector=None):
        """
        Transform(self: Curve, matrix: Matrix3d, transfType: TransfType, stretchVector: Vector3d) -> bool
        Transform(self: Curve, matrix: Matrix3d, transfType: TransfType) -> bool
        Transform(self: Curve, matrix: Matrix3d) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Copy(self: Curve) -> Curve

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Curve) -> CurveType

"""



class CircleCurve(Curve):
    """
    CircleCurve(circle: CircularArc3d, approx: int, body: Body)
    CircleCurve()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, circle=None, approx=None, body=None):
        """
        __new__(cls: type, circle: CircularArc3d, approx: int, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Approx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Approx(self: CircleCurve) -> int

"""

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis(self: CircleCurve) -> LineSegment3d

"""

    Circle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circle(self: CircleCurve) -> CircularArc3d

"""

    Origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Origin(self: CircleCurve) -> Point3d

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: CircleCurve) -> float

"""

    Transf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transf(self: CircleCurve) -> Matrix3d

"""



class ColorType(Enum):
    """ enum ColorType, values: Color1 (1), Color2 (2), Color3 (3), Color4 (4), ColorInvisible (-1) """
    Color1 = None
    Color2 = None
    Color3 = None
    Color4 = None
    ColorInvisible = None
    value__ = None


class Surface(Entity):
    # no doc
    def Circle(self, plane, line):
        """ Circle(self: Surface, plane: Plane, line: LineSegment3d) -> CircularArc3d """
        pass

    def ContainsPoint(self, point):
        """ ContainsPoint(self: Surface, point: Point3d) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IsEqual(self, surface):
        """ IsEqual(self: Surface, surface: Surface) -> bool """
        pass

    def Normal(self, point):
        """ Normal(self: Surface, point: Point3d) -> Vector3d """
        pass

    def Transform(self, matrix, transfType=None, stretchVector=None):
        """
        Transform(self: Surface, matrix: Matrix3d, transfType: TransfType, stretchVector: Vector3d) -> bool
        Transform(self: Surface, matrix: Matrix3d, transfType: TransfType) -> bool
        Transform(self: Surface, matrix: Matrix3d) -> bool
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Copy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Copy(self: Surface) -> Surface

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Surface) -> SurfaceType

"""



class RevolutionSurface(Surface):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Axis(self: RevolutionSurface) -> LineSegment3d

"""

    StartDir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartDir(self: RevolutionSurface) -> Vector3d

"""



class ConeSurface(RevolutionSurface):
    """
    ConeSurface(axis: LineSegment3d, radius1: float, radius2: float, approx: int, body: Body)
    ConeSurface()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, axis=None, radius1=None, radius2=None, approx=None, body=None):
        """
        __new__(cls: type, axis: LineSegment3d, radius1: float, radius2: float, approx: int, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Apex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Apex(self: ConeSurface) -> Point3d

"""

    Approximation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Approximation(self: ConeSurface) -> int

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: ConeSurface) -> float

"""

    TanAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TanAngle(self: ConeSurface) -> float

"""



class CurveCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: CurveCollection, value: Curve) -> int """
        pass

    def Clear(self):
        """ Clear(self: CurveCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: CurveCollection, value: Curve) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: CurveCollection, array: Array[Curve], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CurveCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: CurveCollection, value: Curve) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: CurveCollection, index: int, value: Curve) """
        pass

    def Remove(self, value):
        """ Remove(self: CurveCollection, value: Curve) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CurveCollection, index: int) """
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
    """Get: Count(self: CurveCollection) -> int

"""



class CurveType(Enum):
    """ enum CurveType, values: CircleCurve (1), UnspecifiedCurve (0) """
    CircleCurve = None
    UnspecifiedCurve = None
    value__ = None


class CylinderSurface(RevolutionSurface):
    """
    CylinderSurface(axis: LineSegment3d, startDirection: Vector3d, radius: float, approx: int, body: Body)
    CylinderSurface(axis: LineSegment3d, radius: float, approx: int, body: Body)
    CylinderSurface()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, axis=None, *__args):
        """
        __new__(cls: type, axis: LineSegment3d, startDirection: Vector3d, radius: float, approx: int, body: Body)
        __new__(cls: type, axis: LineSegment3d, radius: float, approx: int, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Approx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Approx(self: CylinderSurface) -> int

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: CylinderSurface) -> float

"""



class DirectionType(Enum):
    """ enum DirectionType, values: Both (2), Forward (0), Reverse (1) """
    Both = None
    Forward = None
    Reverse = None
    value__ = None


class Edge(Entity):
    """
    Edge(vertex: Vertex, face: Face, previousEdge: Edge, partner: Edge)
    Edge(vertex: Vertex, face: Face, previousEdge: Edge, partner: Edge, curve: Curve)
    Edge()
    """
    def AddPartner(self, partnerEdge):
        """ AddPartner(self: Edge, partnerEdge: Edge) """
        pass

    def CanMergeWithPrevious(self, sameColorOnly):
        """ CanMergeWithPrevious(self: Edge, sameColorOnly: bool) -> bool """
        pass

    def Collapse(self):
        """ Collapse(self: Edge) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetAllConnectedEdgesSharingVertex(self):
        """ GetAllConnectedEdgesSharingVertex(self: Edge) -> Array[Edge] """
        pass

    def GetAllEdgesEndingInVertex(self):
        """ GetAllEdgesEndingInVertex(self: Edge) -> Array[Edge] """
        pass

    def GetAllEdgesSharingSameFaces(self, connectedSequenceOnly):
        """ GetAllEdgesSharingSameFaces(self: Edge, connectedSequenceOnly: bool) -> Array[Edge] """
        pass

    def GetAllEdgesStartingFromVertex(self):
        """ GetAllEdgesStartingFromVertex(self: Edge) -> Array[Edge] """
        pass

    def HasPartner(self, edge):
        """ HasPartner(self: Edge, edge: Edge) -> bool """
        pass

    def Merge(self):
        """ Merge(self: Edge) """
        pass

    def MergeLoopsAddBridgeEdge(self, innerEdge):
        """ MergeLoopsAddBridgeEdge(self: Edge, innerEdge: Edge) """
        pass

    def MergeLoopsSharingEdge(self):
        """ MergeLoopsSharingEdge(self: Edge) """
        pass

    def OrderPartnerEdgesAroundEulerEdge(self):
        """ OrderPartnerEdgesAroundEulerEdge(self: Edge) """
        pass

    def RemovePartner(self):
        """ RemovePartner(self: Edge) """
        pass

    def SetColor(self, colorType, partnersAlso):
        """ SetColor(self: Edge, colorType: ColorType, partnersAlso: bool) """
        pass

    def SetCurve(self, curve, partnersAlso):
        """ SetCurve(self: Edge, curve: Curve, partnersAlso: bool) """
        pass

    def Split(self, vertex):
        """ Split(self: Edge, vertex: Vertex) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, vertex=None, face=None, previousEdge=None, partner=None, curve=None):
        """
        __new__(cls: type, vertex: Vertex, face: Face, previousEdge: Edge, partner: Edge)
        __new__(cls: type, vertex: Vertex, face: Face, previousEdge: Edge, partner: Edge, curve: Curve)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AngleBetweenEdges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleBetweenEdges(self: Edge) -> float

"""

    AngleBetweenFaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleBetweenFaces(self: Edge) -> float

"""

    AngleBetweenFacesIsConcave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleBetweenFacesIsConcave(self: Edge) -> bool

"""

    AngleBetweenFacesIsConvex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleBetweenFacesIsConvex(self: Edge) -> bool

"""

    AngleBetweenFacesIsStraight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleBetweenFacesIsStraight(self: Edge) -> bool

"""

    Circle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circle(self: Edge) -> CircularArc3d

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: Edge) -> ColorType

"""

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: Edge) -> Curve

"""

    EulerEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EulerEdge(self: Edge) -> Edge

"""

    Face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Face(self: Edge) -> Face

Set: Face(self: Edge) = value
"""

    IsApprox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsApprox(self: Edge) -> bool

Set: IsApprox(self: Edge) = value
"""

    IsBridge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBridge(self: Edge) -> bool

Set: IsBridge(self: Edge) = value
"""

    IsEulerEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsEulerEdge(self: Edge) -> bool

"""

    IsManifold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsManifold(self: Edge) -> bool

"""

    IsOnCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOnCircle(self: Edge) -> bool

"""

    IsOnFullCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOnFullCircle(self: Edge) -> bool

"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Line(self: Edge) -> LineSegment3d

"""

    NextSkipBridge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextSkipBridge(self: Edge) -> Edge

"""

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Edge) -> Vector3d

"""

    Partner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Partner(self: Edge) -> Edge

Set: Partner(self: Edge) = value
"""

    PartnerBridgeEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartnerBridgeEdge(self: Edge) -> Edge

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Edge) -> Plane

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: Edge) -> Point3d

"""

    PrevSkipBridge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrevSkipBridge(self: Edge) -> Edge

"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: Edge) -> Surface

"""

    UnitVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitVector(self: Edge) -> Vector3d

"""

    Vector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vector(self: Edge) -> Vector3d

"""

    Vertex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertex(self: Edge) -> Vertex

Set: Vertex(self: Edge) = value
"""

    VertexNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexNormal(self: Edge) -> Vector3d

"""



class EdgeCollection(object):
    """ EdgeCollection(pOp: IEdgeOperation) """
    def Add(self, value):
        """ Add(self: EdgeCollection, value: Edge) -> int """
        pass

    def Clear(self):
        """ Clear(self: EdgeCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: EdgeCollection, value: Edge) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: EdgeCollection, array: Array[Edge], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: EdgeCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: EdgeCollection, value: Edge) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: EdgeCollection, index: int, value: Edge) """
        pass

    def Remove(self, value):
        """ Remove(self: EdgeCollection, value: Edge) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: EdgeCollection, index: int) """
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
        """ __new__(cls: type, pOp: IEdgeOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: EdgeCollection) -> int

"""



class ErrorCode(Enum):
    """ enum ErrorCode, values: _3dPolylineOrMeshNotAllowed (69), AngleMustBePositive (148), AngleMustNotBeZero (20), ApexMustNotLieInPolygon (51), ApproximationMustBeAtLeastFour (18), Arc3dTypeExpected (102), ArcBetweenLastAndFirstVertexNotAllowedForEndpointRevolution (65), ArcByBulgeNotAllowedForPathPolygons_UseArc3d (129), ArcByRadiusNotAllowedForPathPolygons_UseArc3d (128), ArcByRadiusTypeExpected (101), AtLeast4NonCoplanarPointsRequired (49), AtLeastOneEdgeExpected (79), AtLeastTwoProfilesExpected (93), AxisOfRevolutionIntersectsPolygon (54), AxisOfRevolutionMustLieInPolygonPlane (53), BadArcCenter (60), BadAxis (11), BadBodyGeometry (3), BadCurveType (5), BadDataRestored (39), BadDxfFile (70), BadFile (31), BadIndexInMorphingMap (155), BadInput (6), BadLine (10), BadMorphingMap (96), BadNormal (55), BadPath (108), BadPlane (9), BadPolygon (56), BadProfileAndPathOrientation (109), BadRelativePolygonPosition (58), BadSurfaceType (4), BadTransform (12), BaseNormalPerpendicularToAxisVector (87), BaseSizesMustBePositive (98), BodyCannotBeClosed (133), BodyIsNegative (28), BodyPointerIsNull (21), BodyProfileMustContainExactlyOneFace (94), BoxSizesMustNotBeZero (41), CallbackObjectPointerIsNull (47), CannotCreateFillet (59), CannotCreateLoopOfEdges (153), CannotCreateTouchingCircle (103), CannotFilletEdge (82), CannotFilletVerticesBelongingToArcs (63), CannotMitreEdgesOfDifferentConvexity (83), ChamferDistanceTooLarge (81), ChamferingDistanceMustBePositive (75), CircleIsNotValid (86), CoplanarFacesExpected (146), DestinationArgumentsAreColinearOrCoincident (73), EdgePointerIsNull (23), EdgeSharedByTwoDifferentFacesExpected (145), EdgesOfFirstProfileCannotBeMarkedApproximating (97), EndCentersMustHaveEqualDistance (88), EndProfileIsParallelWithLastPathSegment (126), EndProfileIsWrong (157), EndProfileMustHaveOnlySingleLoop (160), EndProfileNormalHasOppositeDirectionThanLastPathSegment (124), EndProfileNotAllowedWhenPathIsClosed (114), EntitiesSectionNotFoundInDxfFile (66), EpsilonMustBePositive (46), ExtrusionBodyLooksSelfIntersecting (118), ExtrusionPathIsWrong (158), ExtrusionVectorMustNotBeParallelToPolygon (52), FaceCanNotBeMoved (143), FaceHasNoEdges (90), FaceMustHaveAtLeastThreeEdges (106), FaceMustHaveManifoldEdgesOnly (141), FaceMustNotBelongToABody (89), FacePointerIsNull (22), Fail (1), FileIsNewerThanCurrentVersionOfModeler (40), FileNameIsNull (30), FileOpenError (34), FilePointerIsNull (33), FileReadError (35), FileWriteError (36), FilletByRadiusOrArcByBulgeTypeExpected (100), FilletRadiusMustBePositive (62), FilletRadiusTooLarge (80), FirstAndLastVertexInEndpointRevolutionMustNotBeFilleted (64), FirstPathPointMustLieInStartProfilePlane (110), FixedPointMustLieInPolygonPlane (121), FixedPointMustLieInStartProfilePlane (132), HeightMustBePositive (152), HeightTooSmall (113), IncorrectFile (32), InnerRadiusCanBeZeroOnlyIfOuterRadiusIsZero (44), InnerRadiusMustBeSmallerThanOuterRadius (43), InputBodiesMustNotBeNegated (14), InternalError (1000), IntervalIsNull (29), InvalidTerrainBody (151), InvalidVector (147), LastPathPointMustLieInEndProfilePlane (111), MajorRadiusMustBeGreaterThanMinorRadius (42), ManifoldEdgeExpected (144), MinNumberOfFacesInSurfaceMustBeAtLeastTwo (149), MorphingMapRequiresEndProfile (119), MorphingMustBeIdentityWhenPathIsClosed (117), NegativeIndexInMorphingMap (120), NonManifoldEdgesMustHaveEvenNumberOfPartners (140), NonPlanarPolygon (104), NonPlanarProfileFace (105), NotYetImplemented (85), NullNormalVector (8), NullVector (7), NumberOfLinearSegmentsMustBeAtLeastOne (130), OK (0), OneSidedFaceExpected (91), OnlyManifoldEdgesCanBeFilletedAndChamfered (76), OnlyStraightAndCircularEdgesCanBeFilletedAndChamfered (77), PartnerEdgesOfNonManifoldEdgeCannotBeOrdered (139), PathPolygonPointerIsNull (27), PickingNotPossible (48), PlanarEdgesCannotBeFilletedAndChamfered (78), PointerIsNull (136), PointLiesInPlane (13), PointsAreColinearOrCoincident (71), PointsAreCoplanar (74), PointsDoNotDefineConvexPolyhedron (50), PolygonIsSelfIntersectingOrTouching (57), PolygonNormalNotPerpendicularToPolygonPlane (134), PolygonPointerIsNull (25), PolygonPointsCoincide (107), PolylineEntityNotFoundInDxfFile (67), PolylineMustBeClosed (68), ProfileFaceHasNoEdges (95), ProfileFacesMustHaveTheSameNumberOfEdges (92), ProfilePolygonMustContainAtLeastOnePoint (127), ProfilePolygonPointerIsNull (26), RadiusMustBeNonNegative (16), RadiusMustBePositive (15), RadiusMustNotBeZero (17), RadiusTooSmall (61), RestoreError (38), SaveError (37), ScaleFactorMustBePositive (19), ScaleFactorNotAllowedWhenPathIsClosed (115), SizeMustBePositive (135), SourceArgumentsAreColinearOrCoincident (72), StartProfileIsParallelWithFirstPathSegment (125), StartProfileIsWrong (156), StartProfileMustHaveOnlySingleLoop (159), StartProfileNormalHasOppositeDirectionThanFirstPathSegment (123), StitchingFacesDidNotProduceAValidBody (142), TerrainSurfaceContainsHole (154), ToleranceMustBePositive (137), TooComplexMixedConvexityCap (84), TopCircleMustLieAboveBaseRectangle (99), TriStripsMayBeGeneratedOnlyWhenCachingTriangles (122), TwistAngleNotAllowedWhenPathIsClosed (116), UnspecifiedCurveTypeExpected (150), ValueMustBePositive (138), VertexPointerIsNull (24), ViewPointCoincidesWithTargetPoint (45), ViewPointLiesInsideScene (2), WidthTooSmall (112), ZeroBulgeNotAllowed (131) """
    AngleMustBePositive = None
    AngleMustNotBeZero = None
    ApexMustNotLieInPolygon = None
    ApproximationMustBeAtLeastFour = None
    Arc3dTypeExpected = None
    ArcBetweenLastAndFirstVertexNotAllowedForEndpointRevolution = None
    ArcByBulgeNotAllowedForPathPolygons_UseArc3d = None
    ArcByRadiusNotAllowedForPathPolygons_UseArc3d = None
    ArcByRadiusTypeExpected = None
    AtLeast4NonCoplanarPointsRequired = None
    AtLeastOneEdgeExpected = None
    AtLeastTwoProfilesExpected = None
    AxisOfRevolutionIntersectsPolygon = None
    AxisOfRevolutionMustLieInPolygonPlane = None
    BadArcCenter = None
    BadAxis = None
    BadBodyGeometry = None
    BadCurveType = None
    BadDataRestored = None
    BadDxfFile = None
    BadFile = None
    BadIndexInMorphingMap = None
    BadInput = None
    BadLine = None
    BadMorphingMap = None
    BadNormal = None
    BadPath = None
    BadPlane = None
    BadPolygon = None
    BadProfileAndPathOrientation = None
    BadRelativePolygonPosition = None
    BadSurfaceType = None
    BadTransform = None
    BaseNormalPerpendicularToAxisVector = None
    BaseSizesMustBePositive = None
    BodyCannotBeClosed = None
    BodyIsNegative = None
    BodyPointerIsNull = None
    BodyProfileMustContainExactlyOneFace = None
    BoxSizesMustNotBeZero = None
    CallbackObjectPointerIsNull = None
    CannotCreateFillet = None
    CannotCreateLoopOfEdges = None
    CannotCreateTouchingCircle = None
    CannotFilletEdge = None
    CannotFilletVerticesBelongingToArcs = None
    CannotMitreEdgesOfDifferentConvexity = None
    ChamferDistanceTooLarge = None
    ChamferingDistanceMustBePositive = None
    CircleIsNotValid = None
    CoplanarFacesExpected = None
    DestinationArgumentsAreColinearOrCoincident = None
    EdgePointerIsNull = None
    EdgeSharedByTwoDifferentFacesExpected = None
    EdgesOfFirstProfileCannotBeMarkedApproximating = None
    EndCentersMustHaveEqualDistance = None
    EndProfileIsParallelWithLastPathSegment = None
    EndProfileIsWrong = None
    EndProfileMustHaveOnlySingleLoop = None
    EndProfileNormalHasOppositeDirectionThanLastPathSegment = None
    EndProfileNotAllowedWhenPathIsClosed = None
    EntitiesSectionNotFoundInDxfFile = None
    EpsilonMustBePositive = None
    ExtrusionBodyLooksSelfIntersecting = None
    ExtrusionPathIsWrong = None
    ExtrusionVectorMustNotBeParallelToPolygon = None
    FaceCanNotBeMoved = None
    FaceHasNoEdges = None
    FaceMustHaveAtLeastThreeEdges = None
    FaceMustHaveManifoldEdgesOnly = None
    FaceMustNotBelongToABody = None
    FacePointerIsNull = None
    Fail = None
    FileIsNewerThanCurrentVersionOfModeler = None
    FileNameIsNull = None
    FileOpenError = None
    FilePointerIsNull = None
    FileReadError = None
    FileWriteError = None
    FilletByRadiusOrArcByBulgeTypeExpected = None
    FilletRadiusMustBePositive = None
    FilletRadiusTooLarge = None
    FirstAndLastVertexInEndpointRevolutionMustNotBeFilleted = None
    FirstPathPointMustLieInStartProfilePlane = None
    FixedPointMustLieInPolygonPlane = None
    FixedPointMustLieInStartProfilePlane = None
    HeightMustBePositive = None
    HeightTooSmall = None
    IncorrectFile = None
    InnerRadiusCanBeZeroOnlyIfOuterRadiusIsZero = None
    InnerRadiusMustBeSmallerThanOuterRadius = None
    InputBodiesMustNotBeNegated = None
    InternalError = None
    IntervalIsNull = None
    InvalidTerrainBody = None
    InvalidVector = None
    LastPathPointMustLieInEndProfilePlane = None
    MajorRadiusMustBeGreaterThanMinorRadius = None
    ManifoldEdgeExpected = None
    MinNumberOfFacesInSurfaceMustBeAtLeastTwo = None
    MorphingMapRequiresEndProfile = None
    MorphingMustBeIdentityWhenPathIsClosed = None
    NegativeIndexInMorphingMap = None
    NonManifoldEdgesMustHaveEvenNumberOfPartners = None
    NonPlanarPolygon = None
    NonPlanarProfileFace = None
    NotYetImplemented = None
    NullNormalVector = None
    NullVector = None
    NumberOfLinearSegmentsMustBeAtLeastOne = None
    OK = None
    OneSidedFaceExpected = None
    OnlyManifoldEdgesCanBeFilletedAndChamfered = None
    OnlyStraightAndCircularEdgesCanBeFilletedAndChamfered = None
    PartnerEdgesOfNonManifoldEdgeCannotBeOrdered = None
    PathPolygonPointerIsNull = None
    PickingNotPossible = None
    PlanarEdgesCannotBeFilletedAndChamfered = None
    PointerIsNull = None
    PointLiesInPlane = None
    PointsAreColinearOrCoincident = None
    PointsAreCoplanar = None
    PointsDoNotDefineConvexPolyhedron = None
    PolygonIsSelfIntersectingOrTouching = None
    PolygonNormalNotPerpendicularToPolygonPlane = None
    PolygonPointerIsNull = None
    PolygonPointsCoincide = None
    PolylineEntityNotFoundInDxfFile = None
    PolylineMustBeClosed = None
    ProfileFaceHasNoEdges = None
    ProfileFacesMustHaveTheSameNumberOfEdges = None
    ProfilePolygonMustContainAtLeastOnePoint = None
    ProfilePolygonPointerIsNull = None
    RadiusMustBeNonNegative = None
    RadiusMustBePositive = None
    RadiusMustNotBeZero = None
    RadiusTooSmall = None
    RestoreError = None
    SaveError = None
    ScaleFactorMustBePositive = None
    ScaleFactorNotAllowedWhenPathIsClosed = None
    SizeMustBePositive = None
    SourceArgumentsAreColinearOrCoincident = None
    StartProfileIsParallelWithFirstPathSegment = None
    StartProfileIsWrong = None
    StartProfileMustHaveOnlySingleLoop = None
    StartProfileNormalHasOppositeDirectionThanFirstPathSegment = None
    StitchingFacesDidNotProduceAValidBody = None
    TerrainSurfaceContainsHole = None
    ToleranceMustBePositive = None
    TooComplexMixedConvexityCap = None
    TopCircleMustLieAboveBaseRectangle = None
    TriStripsMayBeGeneratedOnlyWhenCachingTriangles = None
    TwistAngleNotAllowedWhenPathIsClosed = None
    UnspecifiedCurveTypeExpected = None
    ValueMustBePositive = None
    value__ = None
    VertexPointerIsNull = None
    ViewPointCoincidesWithTargetPoint = None
    ViewPointLiesInsideScene = None
    WidthTooSmall = None
    ZeroBulgeNotAllowed = None
    _3dPolylineOrMeshNotAllowed = None


class Face(Entity):
    """
    Face(points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, type: int, checkPlanarity: bool, body: Body)
    Face(circle: CircularArc3d, type: DirectionType, approximation: int, body: Body)
    Face(edge: Edge, surface: Surface, body: Body)
    Face(surface: Surface, body: Body)
    Face(body: Body)
    Face()
    """
    def AreaOfMass(self, body, dae, dbe):
        """ AreaOfMass(self: Face, body: Body, dae: bool, dbe: bool) -> float """
        pass

    def CentroidOfMass(self, body, dae, dbe):
        """ CentroidOfMass(self: Face, body: Body, dae: bool, dbe: bool) -> Point3d """
        pass

    def DecomposeIntoContiguousFaces(self, body):
        """ DecomposeIntoContiguousFaces(self: Face, body: Body) -> Array[Face] """
        pass

    def DeleteInterval(self):
        """ DeleteInterval(self: Face) """
        pass

    def DeletePlane(self):
        """ DeletePlane(self: Face) """
        pass

    def DeleteProjectionInterval(self):
        """ DeleteProjectionInterval(self: Face) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def ExtractAllLoops(self):
        """ ExtractAllLoops(self: Face) -> ArrayList """
        pass

    def InsertHoles(self, holeFaces, body):
        """ InsertHoles(self: Face, holeFaces: Array[Face], body: Body) -> Array[Face] """
        pass

    def IsPlanar(self, epsilon):
        """ IsPlanar(self: Face, epsilon: float) -> bool """
        pass

    def IsPointInside(self, point):
        """ IsPointInside(self: Face, point: Point3d) -> bool """
        pass

    def Lift(self, transform, checkPlanarity, owningBody):
        """ Lift(self: Face, transform: Matrix3d, checkPlanarity: bool, owningBody: Body) """
        pass

    def Modified(self):
        """ Modified(self: Face) """
        pass

    def Negate(self):
        """ Negate(self: Face) """
        pass

    def Paint(self, body, color, dae=None, dbe=None):
        """ Paint(self: Face, body: Body, color: ColorType, dae: bool, dbe: bool)Paint(self: Face, body: Body, color: ColorType, dae: bool)Paint(self: Face, body: Body, color: ColorType) """
        pass

    def PerimeterOfMass(self, body, dae, dbe):
        """ PerimeterOfMass(self: Face, body: Body, dae: bool, dbe: bool) -> float """
        pass

    def SetSpecifiedColor(self, value, edgesAlso, partnerEdgesAlso=None):
        """ SetSpecifiedColor(self: Face, value: ColorType, edgesAlso: bool, partnerEdgesAlso: bool)SetSpecifiedColor(self: Face, value: ColorType, edgesAlso: bool) """
        pass

    def Split(self, edgeA, edgeB, body):
        """ Split(self: Face, edgeA: Edge, edgeB: Edge, body: Body) -> Face """
        pass

    def __neg__(self, *args): #cannot find CLR method
        """ x.__neg__() <==> -x """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, points: Point3dCollection, vertexData: Array[PolygonVertexData], numberOfVertices: int, polygonNormal: Vector3d, type: int, checkPlanarity: bool, body: Body)
        __new__(cls: type, circle: CircularArc3d, type: DirectionType, approximation: int, body: Body)
        __new__(cls: type, edge: Edge, surface: Surface, body: Body)
        __new__(cls: type, surface: Surface, body: Body)
        __new__(cls: type, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Face) -> float

"""

    Attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attribute(self: Face) -> Void*

Set: Attribute(self: Face) = value
"""

    Edges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Edges(self: Face) -> EdgeCollection

"""

    FaceColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FaceColor(self: Face) -> ColorType

Set: FaceColor(self: Face) = value
"""

    IsSelfIntersecting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSelfIntersecting(self: Face) -> bool

"""

    Plane = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plane(self: Face) -> Plane

"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: Face) -> Surface

Set: Surface(self: Face) = value
"""



class FaceCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: FaceCollection, item: Face) -> int """
        pass

    def Clear(self):
        """ Clear(self: FaceCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: FaceCollection, item: Face) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: FaceCollection, array: Array[Face], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: FaceCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: FaceCollection, item: Face) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: FaceCollection, index: int, item: Face) """
        pass

    def Remove(self, item):
        """ Remove(self: FaceCollection, item: Face) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: FaceCollection, index: int) """
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
    """Get: Count(self: FaceCollection) -> int

"""



class HiddenLineDrawingImprove(Enum):
    """ enum HiddenLineDrawingImprove, values: ArcReconstructDrawingImprove (2), ConnectDrawingImprove (1), NoDrawingImprove (0) """
    ArcReconstructDrawingImprove = None
    ConnectDrawingImprove = None
    NoDrawingImprove = None
    value__ = None


class HiddenLinesDisplay(Enum):
    """ enum HiddenLinesDisplay, values: HiddenLinesDashed (1), HiddenLinesInvisible (0), HiddenLinesVisible (2) """
    HiddenLinesDashed = None
    HiddenLinesInvisible = None
    HiddenLinesVisible = None
    value__ = None


class IEdgeOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IEdgeOperation, A_0: Edge) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IEdgeOperation, A_0: int) -> Edge """
        pass

    def GetCount(self):
        """ GetCount(self: IEdgeOperation) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: IEdgeOperation, A_0: int, A_1: Edge) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IEdgeOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IEdgeOperation, A_0: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class ListFlags(Enum):
    """ enum ListFlags, values: Edge (8), Face (4), General (0), Surface (1), Vertex (2) """
    Edge = None
    Face = None
    General = None
    Surface = None
    value__ = None
    Vertex = None


class MorphingMap(DisposableWrapper):
    """ MorphingMap() """
    def Clone(self):
        """ Clone(self: MorphingMap) -> object """
        pass

    def CreateFromTwoPointLoops(self, pointLoopA, pointLoopB):
        """ CreateFromTwoPointLoops(self: MorphingMap, pointLoopA: Point2dCollection, pointLoopB: Point2dCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Initialize(self):
        """ Initialize(self: MorphingMap) """
        pass

    def Normalize(self, numberOfEdgesA, numberOfEdgesB):
        """ Normalize(self: MorphingMap, numberOfEdgesA: int, numberOfEdgesB: int) """
        pass

    def Print(self):
        """ Print(self: MorphingMap) """
        pass

    def RemapIndices(self, fromIndexMap, toIndexMap):
        """ RemapIndices(self: MorphingMap, fromIndexMap: IntegerCollection, toIndexMap: IntegerCollection) """
        pass

    def SetToExplicitIdentityMap(self, numberOfEdges):
        """ SetToExplicitIdentityMap(self: MorphingMap, numberOfEdges: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elements(self: MorphingMap) -> MorphingMapElementCollection

"""

    IsIdentity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsIdentity(self: MorphingMap) -> bool

"""

    IsNull = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsNull(self: MorphingMap) -> bool

"""


    Null = None


class MorphingMapElement(object):
    """
    MorphingMapElement(from: int, to: int, visibility: int)
    MorphingMapElement()
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, from=None, to=None, visibility=None):
        """
        __new__(cls: type, from: int, to: int, visibility: int)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    FromIndex = None
    ToIndex = None
    Visibility = None


class MorphingMapElementCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: MorphingMapElementCollection, item: MorphingMapElement) -> int """
        pass

    def Clear(self):
        """ Clear(self: MorphingMapElementCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: MorphingMapElementCollection, item: MorphingMapElement) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: MorphingMapElementCollection, array: Array[MorphingMapElement], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MorphingMapElementCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: MorphingMapElementCollection, item: MorphingMapElement) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: MorphingMapElementCollection, index: int, item: MorphingMapElement) """
        pass

    def Remove(self, item):
        """ Remove(self: MorphingMapElementCollection, item: MorphingMapElement) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MorphingMapElementCollection, index: int) """
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
    """Get: Count(self: MorphingMapElementCollection) -> int

"""



class OnOff(Enum):
    """ enum OnOff, values: Off (0), On (1) """
    Off = None
    On = None
    value__ = None


class PointInBodyLocation(Enum):
    """ enum PointInBodyLocation, values: PointAtVertex (1), PointInFace (3), PointInsideBody (4), PointOnEdge (2), PointOutsideBody (0) """
    PointAtVertex = None
    PointInFace = None
    PointInsideBody = None
    PointOnEdge = None
    PointOutsideBody = None
    value__ = None


class PolygonVertexData(DisposableWrapper):
    """
    PolygonVertexData(type: PolygonVertexDataType, bulgeOrRadius: float, approximation: int)
    PolygonVertexData(type: PolygonVertexDataType, radius: float, isCenterLeft: bool, approximation: int)
    PolygonVertexData(type: PolygonVertexDataType, circle: CircularArc3d, approximation: int)
    PolygonVertexData(type: PolygonVertexDataType)
    """
    def Clone(self):
        """ Clone(self: PolygonVertexData) -> object """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, *__args):
        """
        __new__(cls: type, type: PolygonVertexDataType, bulgeOrRadius: float, approximation: int)
        __new__(cls: type, type: PolygonVertexDataType, radius: float, isCenterLeft: bool, approximation: int)
        __new__(cls: type, type: PolygonVertexDataType, circle: CircularArc3d, approximation: int)
        __new__(cls: type, type: PolygonVertexDataType)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Approximation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Approximation(self: PolygonVertexData) -> int

Set: Approximation(self: PolygonVertexData) = value
"""

    Bulge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bulge(self: PolygonVertexData) -> float

Set: Bulge(self: PolygonVertexData) = value
"""

    Circle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Circle(self: PolygonVertexData) -> CircularArc3d

Set: Circle(self: PolygonVertexData) = value
"""

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: PolygonVertexData) -> Curve

Set: Curve(self: PolygonVertexData) = value
"""

    IsArc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArc(self: PolygonVertexData) -> bool

"""

    IsCenterLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCenterLeft(self: PolygonVertexData) -> bool

Set: IsCenterLeft(self: PolygonVertexData) = value
"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: PolygonVertexData) -> Surface

Set: Surface(self: PolygonVertexData) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: PolygonVertexData) -> PolygonVertexDataType

Set: Type(self: PolygonVertexData) = value
"""



class PolygonVertexDataType(Enum):
    """ enum PolygonVertexDataType, values: Arc3d (0), ArcByBulge (2), ArcByRadius (1), FilletByRadius (3), UnspecifiedCurve (4) """
    Arc3d = None
    ArcByBulge = None
    ArcByRadius = None
    FilletByRadius = None
    UnspecifiedCurve = None
    value__ = None


class RayBodyIntersection(Enum):
    """ enum RayBodyIntersection, values: RayDoesNotIntersect (0), RayIntersectsEdge (5), RayIntersectsFace (6), RayIntersectsVertex (4), RayPointAtVertex (1), RayPointInFace (3), RayPointOnEdge (2) """
    RayDoesNotIntersect = None
    RayIntersectsEdge = None
    RayIntersectsFace = None
    RayIntersectsVertex = None
    RayPointAtVertex = None
    RayPointInFace = None
    RayPointOnEdge = None
    value__ = None


class SphereSurface(RevolutionSurface):
    """
    SphereSurface(origin: Point3d, radius: float, approx: int, body: Body)
    SphereSurface()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, origin=None, radius=None, approx=None, body=None):
        """
        __new__(cls: type, origin: Point3d, radius: float, approx: int, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Approx = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Approx(self: SphereSurface) -> int

"""

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: SphereSurface) -> Point3d

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: SphereSurface) -> float

"""



class StateFlags(Enum):
    """ enum StateFlags, values: CircArcEdge (262144), IsVoidEdge (524288) """
    CircArcEdge = None
    IsVoidEdge = None
    value__ = None


class SurfaceCollection(object):
    # no doc
    def Add(self, item):
        """ Add(self: SurfaceCollection, item: Surface) -> int """
        pass

    def Clear(self):
        """ Clear(self: SurfaceCollection) """
        pass

    def Contains(self, item):
        """ Contains(self: SurfaceCollection, item: Surface) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: SurfaceCollection, array: Array[Surface], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SurfaceCollection) -> IEnumerator """
        pass

    def IndexOf(self, item):
        """ IndexOf(self: SurfaceCollection, item: Surface) -> int """
        pass

    def Insert(self, index, item):
        """ Insert(self: SurfaceCollection, index: int, item: Surface) """
        pass

    def Remove(self, item):
        """ Remove(self: SurfaceCollection, item: Surface) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SurfaceCollection, index: int) """
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
    """Get: Count(self: SurfaceCollection) -> int

"""



class SurfaceType(Enum):
    """ enum SurfaceType, values: Cone (2), Cylinder (1), Sphere (3), Torus (4), Unspecified (0) """
    Cone = None
    Cylinder = None
    Sphere = None
    Torus = None
    Unspecified = None
    value__ = None


class TorusSurface(RevolutionSurface):
    """
    TorusSurface(axis: LineSegment3d, majRadius: float, minRadius: float, majApprox: int, minApprox: int, body: Body)
    TorusSurface()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, axis=None, majRadius=None, minRadius=None, majApprox=None, minApprox=None, body=None):
        """
        __new__(cls: type, axis: LineSegment3d, majRadius: float, minRadius: float, majApprox: int, minApprox: int, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Center = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Center(self: TorusSurface) -> Point3d

"""

    MajorApprox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorApprox(self: TorusSurface) -> int

"""

    MajorRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorRadius(self: TorusSurface) -> float

"""

    MinorApprox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorApprox(self: TorusSurface) -> int

"""

    MinorRadius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorRadius(self: TorusSurface) -> float

"""



class TransfType(Enum):
    """ enum TransfType, values: EqualScalingOrthoTransf (1), NonOrthoTransf (2), ProjectionTransf (3), RigidMotionTransf (0), UnknownTransf (4) """
    EqualScalingOrthoTransf = None
    NonOrthoTransf = None
    ProjectionTransf = None
    RigidMotionTransf = None
    UnknownTransf = None
    value__ = None


class UnspecifiedCurve(Curve):
    """
    UnspecifiedCurve(body: Body)
    UnspecifiedCurve()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, body=None):
        """
        __new__(cls: type, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class UnspecifiedSurface(Surface):
    """
    UnspecifiedSurface(body: Body)
    UnspecifiedSurface()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, body=None):
        """
        __new__(cls: type, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class Utility(object):
    """ Utility() """
    @staticmethod
    def ArcToBulge(point1, point2, pointOnArc, pointCenter):
        """ ArcToBulge(point1: Point2d, point2: Point2d, pointOnArc: Point2d, pointCenter: Point2d) -> float """
        pass

    @staticmethod
    def BodiesEqual(body1, body2):
        """ BodiesEqual(body1: Body, body2: Body) -> bool """
        pass

    @staticmethod
    def BodyFromObject(*__args):
        """
        BodyFromObject(id: ObjectId, blockReferencePath: ObjectIdCollection) -> Body
        BodyFromObject(entity: Entity, blockReferencePath: ObjectIdCollection) -> Body
        """
        pass

    @staticmethod
    def BottomLeftMostEdge(face):
        """ BottomLeftMostEdge(face: Face) -> Edge """
        pass

    @staticmethod
    def BulgeToCircle(point1, point2, bulge):
        """ BulgeToCircle(point1: Point2d, point2: Point2d, bulge: float) -> CircularArc2d """
        pass

    @staticmethod
    def CreateUnspecifiedSurface(body, vertexCount, vertexList, faceListSize, faceList):
        """ CreateUnspecifiedSurface(body: Body, vertexCount: int, vertexList: Point3dCollection, faceListSize: int, faceList: IntegerCollection) -> UnspecifiedSurface """
        pass

    @staticmethod
    def DisplayFailedBodyMsg(*__args):
        """ DisplayFailedBodyMsg(err: ErrorCode, operation: Operation)DisplayFailedBodyMsg(err: ErrorCode)DisplayFailedBodyMsg(message: str) """
        pass

    @staticmethod
    def EntityBodiesInterfere(*__args):
        """
        EntityBodiesInterfere(firstObjectId: ObjectId, firstObjectBlockReferencePath: ObjectIdCollection, secondObjectId: ObjectId, secondObjectBlockReferencePath: ObjectIdCollection) -> bool
        EntityBodiesInterfere(firstEntity: Entity, firstObjectBlockReferencePath: ObjectIdCollection, secondObjectId: ObjectId, secondObjectBlockReferencePath: ObjectIdCollection) -> bool
        EntityBodiesInterfere(firstEntity: Entity, firstObjectBlockReferencePath: ObjectIdCollection, secondEntity: Entity, secondObjectBlockReferencePath: ObjectIdCollection) -> bool
        """
        pass

    @staticmethod
    def FaceToProfile(face, toXY):
        """ FaceToProfile(face: Face, toXY: Matrix3d) -> Profile """
        pass

    @staticmethod
    def GetBodyExtrusionFromProfilesLineSeg(baseCurve, ecs, profile, *__args):
        """
        GetBodyExtrusionFromProfilesLineSeg(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, profileRotation: float, deviation: float) -> Body
        GetBodyExtrusionFromProfilesLineSeg(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, profileRotation: float, deviation: float, maxFacetsOnCircle: int) -> Body
        GetBodyExtrusionFromProfilesLineSeg(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, profileRotation: float) -> Body
        GetBodyExtrusionFromProfilesLineSeg(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile) -> Body
        GetBodyExtrusionFromProfilesLineSeg(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, deviation: float, maxFacetsOnCircle: int) -> Body
        """
        pass

    @staticmethod
    def GetBodyFromCutPlane(baseCurve, ecs, profile, cutPlaneNormal, *__args):
        """
        GetBodyFromCutPlane(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, cutPlaneNormal: Vector3d, originalPoint: Point3d, isFromEnd: bool) -> Body
        GetBodyFromCutPlane(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, cutPlaneNormal: Vector3d) -> Body
        GetBodyFromCutPlane(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, cutPlaneNormal: Vector3d, isFromEnd: bool) -> Body
        GetBodyFromCutPlane(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, cutPlaneNormal: Vector3d, startOffset: float) -> Body
        GetBodyFromCutPlane(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, cutPlaneNormal: Vector3d, startOffset: float, isFromEnd: bool) -> Body
        GetBodyFromCutPlane(baseCurve: Curve3d, ecs: Matrix3d, profile: Profile, cutPlaneNormal: Vector3d, originalPoint: Point3d) -> Body
        """
        pass

    @staticmethod
    def GetBodyFromCutPlanes(baseCurve, ecs, startProfile, startCutPlaneNormal, startOffset, endProfile, endCutPlaneNormal, endOffset):
        """ GetBodyFromCutPlanes(baseCurve: Curve3d, ecs: Matrix3d, startProfile: Profile, startCutPlaneNormal: Vector3d, startOffset: float, endProfile: Profile, endCutPlaneNormal: Vector3d, endOffset: float) -> Body """
        pass

    @staticmethod
    def GetBodyFromProfileAndTranslate(*__args):
        """
        GetBodyFromProfileAndTranslate(baseCurve: Curve3d, param: float, point: Point3d, ring: Ring, profileRotation: float, deviation: float, maxFacetsOnCircle: int) -> Body
        GetBodyFromProfileAndTranslate(ecsMat: Matrix3d, ring: Ring, profileRotation: float, profilePoints: Point3dCollection, hints: IntegerCollection, deviation: float) -> Body
        GetBodyFromProfileAndTranslate(ecsMat: Matrix3d, ring: Ring, profileRotation: float, profilePoints: Point3dCollection, hints: IntegerCollection, deviation: float, maxFacetsOnCircle: int) -> Body
        GetBodyFromProfileAndTranslate(baseCurve: Curve3d, param: float, ring: Ring, profileRotation: float, deviation: float) -> Body
        GetBodyFromProfileAndTranslate(baseCurve: Curve3d, param: float, ring: Ring, profileRotation: float, deviation: float, maxFacetsOnCircle: int) -> Body
        GetBodyFromProfileAndTranslate(baseCurve: Curve3d, param: float, point: Point3d, ring: Ring, profileRotation: float, deviation: float) -> Body
        """
        pass

    @staticmethod
    def GetBodyFromProfilesCurveSweep(db, *__args):
        """
        GetBodyFromProfilesCurveSweep(db: Database, curves: Curve3dCollection, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile, endRotation: float, deviation: float) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, curves: Curve3dCollection, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile, endRotation: float, deviation: float, maxFacetsOnCircle: int) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, curves: Curve3dCollection, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, curves: Curve3dCollection, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile, endRotation: float) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, startProfile: Profile, endProfile: Profile, extrusionDirection: ProfileExtrusionDirection, deviation: float, maxFacetsOnCircle: int) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, points: Point3dCollection, pathVertexData: Array[PolygonVertexData], startProfileEcs: Matrix3d, endProfileEcs: Matrix3d, ecs: Matrix3d, startProfile: Profile, startRotation: float, endProfile: Profile, endRotation: float, extrusionDirection: ProfileExtrusionDirection) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, startProfile: Profile, endProfile: Profile, extrusionDirection: ProfileExtrusionDirection) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, startProfile: Profile, endProfile: Profile, extrusionDirection: ProfileExtrusionDirection, deviation: float) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile, endRotation: float) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, curves: Curve3dCollection, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, curves: Curve3dCollection, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile, endRotation: float, deviation: float) -> Body
        GetBodyFromProfilesCurveSweep(db: Database, baseCurve: Curve3d, ecs: Matrix3d, extrusionDirection: ProfileExtrusionDirection, startProfile: Profile, startRotation: float, endProfile: Profile, endRotation: float, deviation: float, maxFacetsOnCircle: int) -> Body
        """
        pass

    @staticmethod
    def GetBodyFromRingCurveSweep(points, pathVertexData, startProfileEcs, endProfileEcs, ecs, startRing, startRotation, endRing, endRotation, extrusionDirection, deviation=None, maxFacetsOnCircle=None):
        """
        GetBodyFromRingCurveSweep(points: Point3dCollection, pathVertexData: Array[PolygonVertexData], startProfileEcs: Matrix3d, endProfileEcs: Matrix3d, ecs: Matrix3d, startRing: Ring, startRotation: float, endRing: Ring, endRotation: float, extrusionDirection: ProfileExtrusionDirection, deviation: float, maxFacetsOnCircle: int) -> Body
        GetBodyFromRingCurveSweep(points: Point3dCollection, pathVertexData: Array[PolygonVertexData], startProfileEcs: Matrix3d, endProfileEcs: Matrix3d, ecs: Matrix3d, startRing: Ring, startRotation: float, endRing: Ring, endRotation: float, extrusionDirection: ProfileExtrusionDirection, deviation: float) -> Body
        GetBodyFromRingCurveSweep(points: Point3dCollection, pathVertexData: Array[PolygonVertexData], startProfileEcs: Matrix3d, endProfileEcs: Matrix3d, ecs: Matrix3d, startRing: Ring, startRotation: float, endRing: Ring, endRotation: float, extrusionDirection: ProfileExtrusionDirection) -> Body
        """
        pass

    @staticmethod
    def GetBodySlice(body, *__args):
        """
        GetBodySlice(body: Body, polyPlane: Plane, to2dPlane: Matrix3d) -> Profile
        GetBodySlice(body: Body, height: float, copyAttributes: bool) -> Profile
        """
        pass

    @staticmethod
    def GetConnectedFaces(originalBody, selectedFace, otherFaces=None):
        """
        GetConnectedFaces(originalBody: Body, selectedFace: Face) -> (Body, Body)
        GetConnectedFaces(originalBody: Body, selectedFace: Face) -> Body
        """
        pass

    @staticmethod
    def GetDisconnectedBodies(originalBody):
        """ GetDisconnectedBodies(originalBody: Body) -> BodyCollection """
        pass

    @staticmethod
    def GetHolesInFace(holeEdgeArrays, startEdge):
        """ GetHolesInFace(startEdge: Edge) -> (Edge, ArrayList) """
        pass

    @staticmethod
    def GetPointOnFace(face, point):
        """ GetPointOnFace(face: Face) -> (bool, Point3d) """
        pass

    @staticmethod
    def InitFlagAndCount(body, flag=None):
        """
        InitFlagAndCount(body: Body, flag: int) -> int
        InitFlagAndCount(body: Body) -> int
        """
        pass

    @staticmethod
    def ListBody(body, flags=None):
        """ ListBody(body: Body, flags: ListFlags)ListBody(body: Body) """
        pass

    @staticmethod
    def ModelerError(err):
        """ ModelerError(err: ErrorCode) -> str """
        pass

    @staticmethod
    def NumberOfEdges(edge):
        """ NumberOfEdges(edge: Edge) -> int """
        pass

    @staticmethod
    def NumberOfFaces(body):
        """ NumberOfFaces(body: Body) -> int """
        pass

    @staticmethod
    def NumberOfVertices(body):
        """ NumberOfVertices(body: Body) -> int """
        pass

    @staticmethod
    def SetParamOnBaseCurve(baseCurve, offset, isFromEnd=None):
        """ SetParamOnBaseCurve(baseCurve: Curve3d, offset: float, isFromEnd: bool)SetParamOnBaseCurve(baseCurve: Curve3d, offset: float) """
        pass

    @staticmethod
    def SetParamsOnBaseCurve(baseCurve, startOffset, endOffset):
        """ SetParamsOnBaseCurve(baseCurve: Curve3d, startOffset: float, endOffset: float) """
        pass

    @staticmethod
    def SliceBody(body, bottom, top):
        """ SliceBody(body: Body, bottom: float, top: float) """
        pass


class ValidityCheckingLevel(Enum):
    """ enum ValidityCheckingLevel, values: ExtensiveChecking (2), NoChecking (0), SimpleChecking (1) """
    ExtensiveChecking = None
    NoChecking = None
    SimpleChecking = None
    value__ = None


class Vertex(Entity):
    """
    Vertex(point: Point3d, body: Body)
    Vertex()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetVertexSurfaceDataList(self, *args): #cannot find CLR method
        """ GetVertexSurfaceDataList(self: Vertex) -> VertexSurfaceData* """
        pass

    def Modified(self):
        """ Modified(self: Vertex) """
        pass

    def SetVertexSurfaceDataList(self, *args): #cannot find CLR method
        """ SetVertexSurfaceDataList(self: Vertex, head: VertexSurfaceData*) """
        pass

    def Transform(self, matrix):
        """ Transform(self: Vertex, matrix: Matrix3d) """
        pass

    def VertexSurfaceData(self, edge):
        """ VertexSurfaceData(self: Vertex, edge: Edge) -> VertexSurfaceData """
        pass

    @staticmethod # known case of __new__
    def __new__(self, point=None, body=None):
        """
        __new__(cls: type, point: Point3d, body: Body)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: Vertex) -> Point3d

Set: Point(self: Vertex) = value
"""

    VertexSurfaceDataCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexSurfaceDataCollection(self: Vertex) -> VertexSurfaceDataCollection

"""



class VertexCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: VertexCollection, value: Vertex) -> int """
        pass

    def Clear(self):
        """ Clear(self: VertexCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: VertexCollection, value: Vertex) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: VertexCollection, array: Array[Vertex], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: VertexCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: VertexCollection, value: Vertex) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: VertexCollection, index: int, value: Vertex) """
        pass

    def Remove(self, value):
        """ Remove(self: VertexCollection, value: Vertex) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: VertexCollection, index: int) """
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
    """Get: Count(self: VertexCollection) -> int

"""



class VertexSurfaceData(Entity):
    """
    VertexSurfaceData(edge: Edge)
    VertexSurfaceData()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Transform(self, matrix):
        """ Transform(self: VertexSurfaceData, matrix: Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, edge=None):
        """
        __new__(cls: type, edge: Edge)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: VertexSurfaceData) -> Vector3d

"""

    Surface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Surface(self: VertexSurfaceData) -> Surface

Set: Surface(self: VertexSurfaceData) = value
"""



class VertexSurfaceDataCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: VertexSurfaceDataCollection, value: VertexSurfaceData) -> int """
        pass

    def Clear(self):
        """ Clear(self: VertexSurfaceDataCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: VertexSurfaceDataCollection, value: VertexSurfaceData) -> bool """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: VertexSurfaceDataCollection, array: Array[VertexSurfaceData], start: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: VertexSurfaceDataCollection) -> IEnumerator """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: VertexSurfaceDataCollection, value: VertexSurfaceData) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: VertexSurfaceDataCollection, index: int, value: VertexSurfaceData) """
        pass

    def Remove(self, value):
        """ Remove(self: VertexSurfaceDataCollection, value: VertexSurfaceData) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: VertexSurfaceDataCollection, index: int) """
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
    """Get: Count(self: VertexSurfaceDataCollection) -> int

"""



