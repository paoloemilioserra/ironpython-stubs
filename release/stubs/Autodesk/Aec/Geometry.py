# encoding: utf-8
# module Autodesk.Aec.Geometry calls itself Geometry
# from AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null, AecBaseMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class BoundBox2d(DisposableWrapper):
    """
    BoundBox2d(minPoint: Point2d, maxPoint: Point2d)
    BoundBox2d()
    """
    def Clone(self):
        """ Clone(self: BoundBox2d) -> object """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: BoundBox2d, testPoint: Point2d) -> Point2d """
        pass

    def ContainsPoint(self, point):
        """ ContainsPoint(self: BoundBox2d, point: Point2d) -> bool """
        pass

    @staticmethod
    def Create(unmanagedPointer, bAutoDelete):
        """ Create(unmanagedPointer: IntPtr, bAutoDelete: bool) -> BoundBox2d """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Enlarge(self, amount):
        """ Enlarge(self: BoundBox2d, amount: float) """
        pass

    def FurthestPoint(self, testPoint):
        """ FurthestPoint(self: BoundBox2d, testPoint: Point2d) -> Point2d """
        pass

    def Init(self):
        """ Init(self: BoundBox2d) """
        pass

    def IntersectWith(self, boundBox):
        """ IntersectWith(self: BoundBox2d, boundBox: BoundBox2d) -> bool """
        pass

    def Set(self, *__args):
        """ Set(self: BoundBox2d, minPoint: Point2d, maxPoint: Point2d)Set(self: BoundBox2d, minX: float, minY: float, maxX: float, maxY: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, minPoint=None, maxPoint=None):
        """
        __new__(cls: type, minPoint: Point2d, maxPoint: Point2d)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: BoundBox2d) -> float

"""

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: BoundBox2d) -> float

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: BoundBox2d) -> bool

"""

    MaxPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxPoint(self: BoundBox2d) -> Point2d

"""

    MinPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinPoint(self: BoundBox2d) -> Point2d

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: BoundBox2d) -> float

"""



class BoundBox3d(DisposableWrapper):
    """
    BoundBox3d(minPoint: Point3d, maxPoint: Point3d)
    BoundBox3d()
    """
    def Clone(self):
        """ Clone(self: BoundBox3d) -> object """
        pass

    def ClosestPoint(self, testPoint):
        """ ClosestPoint(self: BoundBox3d, testPoint: Point3d) -> Point3d """
        pass

    @staticmethod
    def Create(unmanagedPointer, bAutoDelete):
        """ Create(unmanagedPointer: IntPtr, bAutoDelete: bool) -> BoundBox3d """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def FurthestPoint(self, testPoint):
        """ FurthestPoint(self: BoundBox3d, testPoint: Point3d) -> Point3d """
        pass

    def Init(self):
        """ Init(self: BoundBox3d) """
        pass

    def IntersectWith(self, boundBox):
        """ IntersectWith(self: BoundBox3d, boundBox: BoundBox3d) -> bool """
        pass

    def Set(self, *__args):
        """ Set(self: BoundBox3d, minPoint: Point3d, maxPoint: Point3d)Set(self: BoundBox3d, minX: float, minY: float, minZ: float, maxX: float, maxY: float, maxZ: float) """
        pass

    def TransformBy(self, xform):
        """ TransformBy(self: BoundBox3d, xform: Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, minPoint=None, maxPoint=None):
        """
        __new__(cls: type, minPoint: Point3d, maxPoint: Point3d)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: BoundBox3d) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: BoundBox3d) -> float

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: BoundBox3d) -> bool

"""

    MaxPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxPoint(self: BoundBox3d) -> Point3d

"""

    MinPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinPoint(self: BoundBox3d) -> Point3d

"""

    Volume = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Volume(self: BoundBox3d) -> float

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: BoundBox3d) -> float

"""



class CompoundCurve2d(ImpObject):
    """ CompoundCurve2d() """
    def AddSegment(self, segment, appendAtEnd):
        """ AddSegment(self: CompoundCurve2d, segment: Segment2d, appendAtEnd: bool) """
        pass

    def AddSegmentAt(self, index, segment):
        """ AddSegmentAt(self: CompoundCurve2d, index: int, segment: Segment2d) """
        pass

    def AddSegmentsFrom(self, *__args):
        """ AddSegmentsFrom(self: CompoundCurve2d, compoundCurve: CompoundCurve2d, appendAtEnd: bool)AddSegmentsFrom(self: CompoundCurve2d, polyline: Polyline, appendAtEnd: bool)AddSegmentsFrom(self: CompoundCurve2d, points: Point2dCollection, appendAtEnd: bool) """
        pass

    def CleanupVertices(self, doChange):
        """ CleanupVertices(self: CompoundCurve2d, doChange: bool) -> int """
        pass

    def DirectionAtParameter(self, segmentIndex, segmentParameter):
        """ DirectionAtParameter(self: CompoundCurve2d, segmentIndex: int, segmentParameter: float) -> Vector2d """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EvaluatePointAtParameter(self, segmentIndex, segmentParameter):
        """ EvaluatePointAtParameter(self: CompoundCurve2d, segmentIndex: int, segmentParameter: float) -> Point2d """
        pass

    def Extent(self, topLeft, bottomRight):
        """ Extent(self: CompoundCurve2d) -> (Point2d, Point2d) """
        pass

    def GetBetween(self, *__args):
        """
        GetBetween(self: CompoundCurve2d, startPoint: Point2d, endPoint: Point2d) -> CompoundCurve2d
        GetBetween(self: CompoundCurve2d, startDistanceAlong: float, endDistanceAlong: float) -> CompoundCurve2d
        GetBetween(self: CompoundCurve2d, startIndex: int, startParameter: float, endIndex: int, endParameter: float) -> CompoundCurve2d
        GetBetween(self: CompoundCurve2d, startClip: Curve2d, endClip: Curve2d) -> CompoundCurve2d
        """
        pass

    def GetClosestParameterTo(self, point, segmentIndex, segmentParameter):
        """ GetClosestParameterTo(self: CompoundCurve2d, point: Point2d) -> (int, float) """
        pass

    def GetParameterAtLength(self, distance, segmentIndex, segmentParameter, useStartParameterAtJoints, fromStart):
        """ GetParameterAtLength(self: CompoundCurve2d, distance: float, useStartParameterAtJoints: bool, fromStart: bool) -> (bool, int, float) """
        pass

    def GetParameterAtPoint(self, point, segmentIndex, segmentParameter, useStartParameterAtJoints):
        """ GetParameterAtPoint(self: CompoundCurve2d, point: Point2d, useStartParameterAtJoints: bool) -> (bool, int, float) """
        pass

    def InsertVertex(self, newPoint):
        """ InsertVertex(self: CompoundCurve2d, newPoint: Point2d) """
        pass

    def IntersectionParameter(self, curve, point, segmentIndex, segmentParameter, closestToStart):
        """ IntersectionParameter(self: CompoundCurve2d, curve: Curve2d, closestToStart: bool) -> (bool, Point2d, int, float) """
        pass

    def IntersectWith(self, curve, points, *__args):
        """
        IntersectWith(self: CompoundCurve2d, curve: CompoundCurve2d) -> (bool, Point2dCollection, IntegerCollection, DoubleCollection, IntegerCollection, DoubleCollection)
        IntersectWith(self: CompoundCurve2d, curve: CompoundCurve2d) -> (bool, Point2dCollection)
        IntersectWith(self: CompoundCurve2d, curve: Curve2d) -> (bool, Point2dCollection, IntegerCollection, DoubleCollection)
        IntersectWith(self: CompoundCurve2d, curve: Curve2d) -> (bool, Point2dCollection)
        """
        pass

    def IsEqualTo(self, otherCompCurve):
        """ IsEqualTo(self: CompoundCurve2d, otherCompCurve: CompoundCurve2d) -> bool """
        pass

    def JoinColinearPossible(self, segment, nextSegment):
        """ JoinColinearPossible(self: CompoundCurve2d, segment: Segment2d, nextSegment: Segment2d) -> bool """
        pass

    def JoinColinearSegments(self):
        """ JoinColinearSegments(self: CompoundCurve2d) """
        pass

    def LengthToParameter(self, segmentIndex, segmentParameter, fromStart):
        """ LengthToParameter(self: CompoundCurve2d, segmentIndex: int, segmentParameter: float, fromStart: bool) -> float """
        pass

    def LengthToPoint(self, pointOnCurve, fromStart):
        """ LengthToPoint(self: CompoundCurve2d, pointOnCurve: Point2d, fromStart: bool) -> float """
        pass

    def MoveVertex(self, vertex, offset):
        """ MoveVertex(self: CompoundCurve2d, vertex: CompoundCurve2dVertex, offset: Vector2d) """
        pass

    def OrientAboutPoint(self, point):
        """ OrientAboutPoint(self: CompoundCurve2d, point: Point2d) """
        pass

    def OrientAboutTopLeftCorner(self):
        """ OrientAboutTopLeftCorner(self: CompoundCurve2d) """
        pass

    def PopSegment(self, removeFromEnd):
        """ PopSegment(self: CompoundCurve2d, removeFromEnd: bool) -> Segment2d """
        pass

    def PopSegmentAt(self, index):
        """ PopSegmentAt(self: CompoundCurve2d, index: int) -> Segment2d """
        pass

    def RemoveAllSegments(self):
        """ RemoveAllSegments(self: CompoundCurve2d) """
        pass

    def RemoveSegment(self, removeFromEnd):
        """ RemoveSegment(self: CompoundCurve2d, removeFromEnd: bool) """
        pass

    def RemoveSegmentAt(self, index):
        """ RemoveSegmentAt(self: CompoundCurve2d, index: int) """
        pass

    def ReplaceSegmentAt(self, index, withThis):
        """ ReplaceSegmentAt(self: CompoundCurve2d, index: int, withThis: Segment2d) -> Segment2d """
        pass

    def Reverse(self, reverseInPlace):
        """ Reverse(self: CompoundCurve2d, reverseInPlace: bool) """
        pass

    def Scale(self, x, y):
        """ Scale(self: CompoundCurve2d, x: float, y: float) """
        pass

    def Segment(self, index):
        """ Segment(self: CompoundCurve2d, index: int) -> Segment2d """
        pass

    def TransferSegmentDataForJoin(self, segmentToKeep, segmentToDelete):
        """ TransferSegmentDataForJoin(self: CompoundCurve2d, segmentToKeep: Segment2d, segmentToDelete: Segment2d) """
        pass

    def TransferSegmentsFrom(self, compoundCurve, appendAtEnd):
        """ TransferSegmentsFrom(self: CompoundCurve2d, compoundCurve: CompoundCurve2d, appendAtEnd: bool) """
        pass

    def TransformBy(self, matrix):
        """ TransformBy(self: CompoundCurve2d, matrix: Matrix3d)TransformBy(self: CompoundCurve2d, matrix: Matrix2d) """
        pass

    def TranslateBy(self, vector):
        """ TranslateBy(self: CompoundCurve2d, vector: Vector2d) """
        pass

    def UpdateTransientData(self):
        """ UpdateTransientData(self: CompoundCurve2d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attribute(self: CompoundCurve2d) -> Attribute

Set: Attribute(self: CompoundCurve2d) = value
"""

    DirtyFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirtyFlag(self: CompoundCurve2d) -> bool

Set: DirtyFlag(self: CompoundCurve2d) = value
"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: CompoundCurve2d) -> Point2d

"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: CompoundCurve2d) -> bool

"""

    IsContinuous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsContinuous(self: CompoundCurve2d) -> bool

"""

    IsSelfIntersecting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSelfIntersecting(self: CompoundCurve2d) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: CompoundCurve2d) -> float

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentCount(self: CompoundCurve2d) -> int

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: CompoundCurve2d) -> Point2d

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: CompoundCurve2d) -> CompoundCurve2dVertexCollection

"""



class CompoundCurve2dVertex(DisposableWrapper):
    """ CompoundCurve2dVertex() """
    def Clone(self):
        """ Clone(self: CompoundCurve2dVertex) -> object """
        pass

    @staticmethod
    def Create(unmanagedPointer, bAutoDelete):
        """ Create(unmanagedPointer: IntPtr, bAutoDelete: bool) -> CompoundCurve2dVertex """
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

    CompoundCurve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompoundCurve(self: CompoundCurve2dVertex) -> CompoundCurve2d

"""

    NextSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NextSegment(self: CompoundCurve2dVertex) -> Segment2d

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: CompoundCurve2dVertex) -> Point2d

"""

    PreviousSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviousSegment(self: CompoundCurve2dVertex) -> Segment2d

"""



class CompoundCurve2dVertexCollection(DisposableWrapper):
    # no doc
    def CopyTo(self, array, start):
        """ CopyTo(self: CompoundCurve2dVertexCollection, array: Array[CompoundCurve2dVertex], start: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CompoundCurve2dVertexCollection) -> IEnumerator """
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
    """Get: Count(self: CompoundCurve2dVertexCollection) -> int

"""



class Segment2d(ImpObject):
    """
    Segment2d(startPoint: Point2d, endPoint: Point2d)
    Segment2d(curve: Curve2d, segmentPosition: SegmentPosition)
    Segment2d(curve: Curve2d)
    """
    def CanMoveStartEndPoint(self, oldStartEndPoint, newStartEndPoint):
        """ CanMoveStartEndPoint(self: Segment2d, oldStartEndPoint: Point2d, newStartEndPoint: Point2d) -> bool """
        pass

    @staticmethod
    def Create(unmanagedPointer, bAutoDelete):
        """ Create(unmanagedPointer: IntPtr, bAutoDelete: bool) -> Segment2d """
        pass

    def DirectionAtParameter(self, parameter):
        """ DirectionAtParameter(self: Segment2d, parameter: float) -> Vector2d """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def DistanceTo(self, point, tolerance):
        """ DistanceTo(self: Segment2d, point: Point2d, tolerance: Tolerance) -> float """
        pass

    def EvaluateLength(self, fromParameter, toParameter, tolerance):
        """ EvaluateLength(self: Segment2d, fromParameter: float, toParameter: float, tolerance: Tolerance) -> float """
        pass

    def EvaluatePoint(self, parameter):
        """ EvaluatePoint(self: Segment2d, parameter: float) -> Point2d """
        pass

    def Extent(self, topLeft, bottomRight):
        """ Extent(self: Segment2d) -> (Point2d, Point2d) """
        pass

    def GetBounds(self, lowerBoundParameter, upperBoundParameter):
        """ GetBounds(self: Segment2d) -> (float, float) """
        pass

    def GetClosestPointTo(self, point, tolerance):
        """ GetClosestPointTo(self: Segment2d, point: Point2d, tolerance: Tolerance) -> PointOnCurve2d """
        pass

    def GetCurvature(self, *__args):
        """
        GetCurvature(self: Segment2d, parameter: float) -> float
        GetCurvature(self: Segment2d, point: Point2d) -> float
        """
        pass

    def GetPointOnCurve2d(self, parameter):
        """ GetPointOnCurve2d(self: Segment2d, parameter: float) -> PointOnCurve2d """
        pass

    def GetProjectedIntersectionPoints(self, segment, point1, point2):
        """ GetProjectedIntersectionPoints(self: Segment2d, segment: Segment2d) -> (int, Point2d, Point2d) """
        pass

    def IntersectSegments(self, segment, count, point1, point2):
        """ IntersectSegments(self: Segment2d, segment: Segment2d) -> (bool, int, Point2d, Point2d) """
        pass

    def IntersectWith(self, line, count, point1, point2, tolerance):
        """ IntersectWith(self: Segment2d, line: LinearEntity2d, tolerance: Tolerance) -> (bool, int, Point2d, Point2d) """
        pass

    def IntersectWithCurve(self, segment, count, point1, point2):
        """ IntersectWithCurve(self: Segment2d, segment: Curve2d) -> (bool, int, Point2d, Point2d) """
        pass

    def IsColinearTo(self, *__args):
        """
        IsColinearTo(self: Segment2d, segment: Segment2d, tolerance: Tolerance) -> bool
        IsColinearTo(self: Segment2d, line: LinearEntity2d, tolerance: Tolerance) -> bool
        """
        pass

    def IsExtending(self, oldStartEndPoint, newStartEndPoint):
        """ IsExtending(self: Segment2d, oldStartEndPoint: Point2d, newStartEndPoint: Point2d) -> bool """
        pass

    def IsOn(self, point, *__args):
        """
        IsOn(self: Segment2d, point: Point2d, tolerance: Tolerance) -> bool
        IsOn(self: Segment2d, point: Point2d, tolerance: Tolerance) -> (bool, float)
        """
        pass

    def IsOnSameUnboundedCurveAs(self, segment):
        """ IsOnSameUnboundedCurveAs(self: Segment2d, segment: Segment2d) -> bool """
        pass

    def MoveStartEndPoint(self, oldStartEndPoint, newStartEndPoint):
        """ MoveStartEndPoint(self: Segment2d, oldStartEndPoint: Point2d, newStartEndPoint: Point2d) """
        pass

    def ParameterAtLength(self, datumParameter, length, positiveParameterDirection, tolerance):
        """ ParameterAtLength(self: Segment2d, datumParameter: float, length: float, positiveParameterDirection: bool, tolerance: Tolerance) -> float """
        pass

    def ParameterOf(self, point, tolerance):
        """ ParameterOf(self: Segment2d, point: Point2d, tolerance: Tolerance) -> float """
        pass

    def Reverse(self):
        """ Reverse(self: Segment2d) """
        pass

    def Scale(self, x, y):
        """ Scale(self: Segment2d, x: float, y: float) """
        pass

    @staticmethod
    def SegmentPositionName(position):
        """ SegmentPositionName(position: SegmentPosition) -> str """
        pass

    def Split(self, point):
        """ Split(self: Segment2d, point: Point2d) -> Segment2d """
        pass

    def Tangent(self, point, line, tolerance):
        """ Tangent(self: Segment2d, point: Point2d, tolerance: Tolerance) -> (bool, Line2d) """
        pass

    def TransferJoinedSegmentData(self, segment):
        """ TransferJoinedSegmentData(self: Segment2d, segment: Segment2d) """
        pass

    def TransformBy(self, matrix):
        """ TransformBy(self: Segment2d, matrix: Matrix3d)TransformBy(self: Segment2d, matrix: Matrix2d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, startPoint: Point2d, endPoint: Point2d)
        __new__(cls: type, curve: Curve2d, segmentPosition: SegmentPosition)
        __new__(cls: type, curve: Curve2d)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attribute(self: Segment2d) -> Attribute

Set: Attribute(self: Segment2d) = value
"""

    BoundBox2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundBox2d(self: Segment2d) -> BoundBox2d

"""

    Bulge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bulge(self: Segment2d) -> float

"""

    Curve = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Curve(self: Segment2d) -> Curve2d

Set: Curve(self: Segment2d) = value
"""

    CurveDirectionPositive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveDirectionPositive(self: Segment2d) -> bool

"""

    EndParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndParameter(self: Segment2d) -> float

"""

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Segment2d) -> Point2d

Set: EndPoint(self: Segment2d) = value
"""

    Interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interval(self: Segment2d) -> Interval

Set: Interval(self: Segment2d) = value
"""

    IsClosed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsClosed(self: Segment2d) -> bool

"""

    IsCurveCircularArc2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCurveCircularArc2d(self: Segment2d) -> bool

"""

    IsCurveLineSegment2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCurveLineSegment2d(self: Segment2d) -> bool

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: Segment2d) -> float

"""

    MidPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidPoint(self: Segment2d) -> Point2d

"""

    SegmentPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentPosition(self: Segment2d) -> SegmentPosition

Set: SegmentPosition(self: Segment2d) = value
"""

    StartParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartParameter(self: Segment2d) -> float

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Segment2d) -> Point2d

Set: StartPoint(self: Segment2d) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: Segment2d) -> bool

Set: Visible(self: Segment2d) = value
"""



class CompoundSegment2d(Segment2d):
    """ CompoundSegment2d(curve: Curve2d) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, curve):
        """
        __new__(cls: type, curve: Curve2d)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    GraphicSystemMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicSystemMarker(self: CompoundSegment2d) -> int

Set: GraphicSystemMarker(self: CompoundSegment2d) = value
"""



class Polyline2d(CompoundCurve2d):
    """ Polyline2d() """
    def ClipEnd(self, clipLine):
        """ ClipEnd(self: Polyline2d, clipLine: Line2d) """
        pass

    def ClipStart(self, clipLine):
        """ ClipStart(self: Polyline2d, clipLine: Line2d) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetAfter(self, *__args):
        """
        GetAfter(self: Polyline2d, startPoint: Point2d) -> Polyline2d
        GetAfter(self: Polyline2d, startDistanceAlong: float) -> Polyline2d
        GetAfter(self: Polyline2d, startIndex: int, startParameter: float) -> Polyline2d
        GetAfter(self: Polyline2d, startClip: Curve2d) -> Polyline2d
        """
        pass

    def GetBefore(self, *__args):
        """
        GetBefore(self: Polyline2d, endPoint: Point2d) -> Polyline2d
        GetBefore(self: Polyline2d, endDistanceAlong: float) -> Polyline2d
        GetBefore(self: Polyline2d, endIndex: int, endParameter: float) -> Polyline2d
        GetBefore(self: Polyline2d, endClip: Curve2d) -> Polyline2d
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class Profile(ImpObject):
    """ Profile() """
    def AddRing(self, ring):
        """ AddRing(self: Profile, ring: Ring) """
        pass

    def AddRingsFrom(self, profile):
        """ AddRingsFrom(self: Profile, profile: Profile) """
        pass

    def Area(self, tolerance):
        """ Area(self: Profile, tolerance: float) -> float """
        pass

    def CalculateSegmentPositions(self, extrusionDirection, calculateOnlyForNonMarked):
        """ CalculateSegmentPositions(self: Profile, extrusionDirection: ProfileExtrusionDirection, calculateOnlyForNonMarked: bool) """
        pass

    def CleanupVertices(self, doChange):
        """ CleanupVertices(self: Profile, doChange: bool) -> int """
        pass

    def ConsistentlyOrientRings(self):
        """ ConsistentlyOrientRings(self: Profile) """
        pass

    @staticmethod
    def Create(unmanagedPointer, bAutoDelete):
        """ Create(unmanagedPointer: IntPtr, bAutoDelete: bool) -> Profile """
        pass

    @staticmethod
    def CreateCircle(*__args):
        """
        CreateCircle(width: float, height: float, translation: Vector2d) -> Profile
        CreateCircle(radius: float, translation: Vector2d) -> Profile
        """
        pass

    @staticmethod
    def CreateFromEntity(entity, toWcs):
        """ CreateFromEntity(entity: Entity, toWcs: Matrix3d) -> Profile """
        pass

    @staticmethod
    def CreateIsoscelesTriangle(width, height, rotation, translation):
        """ CreateIsoscelesTriangle(width: float, height: float, rotation: float, translation: Vector2d) -> Profile """
        pass

    @staticmethod
    def CreateLeftHandSideRightAngleTriangle(width, height, rotation, translation):
        """ CreateLeftHandSideRightAngleTriangle(width: float, height: float, rotation: float, translation: Vector2d) -> Profile """
        pass

    @staticmethod
    def CreateOval(width, height, rotation, translation):
        """ CreateOval(width: float, height: float, rotation: float, translation: Vector2d) -> Profile """
        pass

    @staticmethod
    def CreatePolygon(sideCount, sideLength, rotation, translation):
        """ CreatePolygon(sideCount: int, sideLength: float, rotation: float, translation: Vector2d) -> Profile """
        pass

    @staticmethod
    def CreateQuarterCircle(*__args):
        """
        CreateQuarterCircle(width: float, height: float, rotation: float, translation: Vector2d) -> Profile
        CreateQuarterCircle(radius: float, rotation: float, translation: Vector2d) -> Profile
        """
        pass

    @staticmethod
    def CreateQuarterCircularRing(*__args):
        """
        CreateQuarterCircularRing(width: float, height: float, thickness: float, rotation: float, translation: Vector2d) -> Profile
        CreateQuarterCircularRing(outerRadius: float, thickness: float, rotation: float, translation: Vector2d) -> Profile
        """
        pass

    @staticmethod
    def CreateRectangle(width, height, rotation, translation):
        """ CreateRectangle(width: float, height: float, rotation: float, translation: Vector2d) -> Profile """
        pass

    @staticmethod
    def CreateRightHandSideRightAngleTriangle(width, height, rotation, translation):
        """ CreateRightHandSideRightAngleTriangle(width: float, height: float, rotation: float, translation: Vector2d) -> Profile """
        pass

    @staticmethod
    def CreateSemiCircle(*__args):
        """
        CreateSemiCircle(width: float, height: float, rotation: float, translation: Vector2d) -> Profile
        CreateSemiCircle(radius: float, rotation: float, translation: Vector2d) -> Profile
        """
        pass

    @staticmethod
    def CreateSemiCircularRing(*__args):
        """
        CreateSemiCircularRing(width: float, height: float, thickness: float, rotation: float, translation: Vector2d) -> Profile
        CreateSemiCircularRing(outerRadius: float, thickness: float, rotation: float, translation: Vector2d) -> Profile
        """
        pass

    @staticmethod
    def CreateUShape(width, height, thickness, rotation, translation):
        """ CreateUShape(width: float, height: float, thickness: float, rotation: float, translation: Vector2d) -> Profile """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def Equals(*__args):
        """ Equals(profile1: Profile, profile2: Profile) -> bool """
        pass

    def Extent(self, topLeft, bottomRight):
        """ Extent(self: Profile) -> (Point2d, Point2d) """
        pass

    def GetClosestParameterTo(self, point, ringIndex, segmentIndex, segmentParameter):
        """ GetClosestParameterTo(self: Profile, point: Point2d) -> (int, int, float) """
        pass

    def GetExtrusion(self, direction, deviation, maxFacetsOnCircle):
        """ GetExtrusion(self: Profile, direction: Vector3d, deviation: float, maxFacetsOnCircle: int) -> Body """
        pass

    def IntersectWith(self, profile, tolerance):
        """ IntersectWith(self: Profile, profile: Profile, tolerance: Tolerance) -> Profile """
        pass

    def IsEqualTo(self, otherProfile):
        """ IsEqualTo(self: Profile, otherProfile: Profile) -> bool """
        pass

    def IsTopologicallyEquivalent(self, otherProfile, offsets):
        """ IsTopologicallyEquivalent(self: Profile, otherProfile: Profile) -> (bool, IntegerCollection) """
        pass

    def IsValidProfile(self, performAdditionalChecksOnRing):
        """ IsValidProfile(self: Profile, performAdditionalChecksOnRing: bool) -> bool """
        pass

    def IsValidRingNesting(self, checkingLevel):
        """ IsValidRingNesting(self: Profile, checkingLevel: int) -> bool """
        pass

    def JoinColinearSegments(self):
        """ JoinColinearSegments(self: Profile) """
        pass

    def MirrorSegmentPositions(self):
        """ MirrorSegmentPositions(self: Profile) """
        pass

    def ModifySegmentPositions(self, *__args):
        """ ModifySegmentPositions(self: Profile, oldSegmentPosition: SegmentPosition, newSegmentPosition: SegmentPosition)ModifySegmentPositions(self: Profile, oldExtrusionDirection: ProfileExtrusionDirection, newExtrusionDirection: ProfileExtrusionDirection) """
        pass

    def OffsetUniform(self, distance):
        """ OffsetUniform(self: Profile, distance: float) -> Profile """
        pass

    def OffsetUniformRingAt(self, index, distance):
        """ OffsetUniformRingAt(self: Profile, index: int, distance: float) -> Profile """
        pass

    def OrientAboutPoint(self, point):
        """ OrientAboutPoint(self: Profile, point: Point2d) """
        pass

    def OrientAboutTopLeftCorner(self):
        """ OrientAboutTopLeftCorner(self: Profile) """
        pass

    def Perimeter(self, tolerance):
        """ Perimeter(self: Profile, tolerance: float) -> float """
        pass

    def PointInProfile(self, point):
        """ PointInProfile(self: Profile, point: Point2d) -> ProfileResult """
        pass

    def PopRingAt(self, index):
        """ PopRingAt(self: Profile, index: int) -> Ring """
        pass

    def RemoveAllRings(self):
        """ RemoveAllRings(self: Profile) """
        pass

    def RemoveRingAt(self, index):
        """ RemoveRingAt(self: Profile, index: int) """
        pass

    def RemoveVoidRings(self):
        """ RemoveVoidRings(self: Profile) """
        pass

    def Ring(self, index):
        """ Ring(self: Profile, index: int) -> Ring """
        pass

    def RingInProfile(self, ring):
        """ RingInProfile(self: Profile, ring: Ring) -> ProfileResult """
        pass

    def Scale(self, x, y):
        """ Scale(self: Profile, x: float, y: float) """
        pass

    def SetExtent(self, width, height):
        """ SetExtent(self: Profile, width: float, height: float) """
        pass

    def Split(self, line):
        """ Split(self: Profile, line: Line2d) -> Profile """
        pass

    def SubtractProfile(self, profile, tolerance):
        """ SubtractProfile(self: Profile, profile: Profile, tolerance: Tolerance) -> Profile """
        pass

    def TransferRingsFrom(self, profile):
        """ TransferRingsFrom(self: Profile, profile: Profile) """
        pass

    def TransformBy(self, matrix):
        """ TransformBy(self: Profile, matrix: Matrix3d)TransformBy(self: Profile, matrix: Matrix2d) """
        pass

    def TranslateBy(self, vector):
        """ TranslateBy(self: Profile, vector: Vector2d) """
        pass

    def UnionWith(self, profile, tolerance):
        """ UnionWith(self: Profile, profile: Profile, tolerance: Tolerance) -> Profile """
        pass

    def UpdateTransientData(self):
        """ UpdateTransientData(self: Profile) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Attribute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attribute(self: Profile) -> Attribute

Set: Attribute(self: Profile) = value
"""

    CenterOfGravity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterOfGravity(self: Profile) -> Point2d

"""

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centroid(self: Profile) -> Point2d

"""

    DirtyFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirtyFlag(self: Profile) -> bool

Set: DirtyFlag(self: Profile) = value
"""

    HasHiddenEdge = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasHiddenEdge(self: Profile) -> bool

"""

    IsSelfIntersecting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSelfIntersecting(self: Profile) -> bool

"""

    RingCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RingCount(self: Profile) -> int

"""

    Rings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rings(self: Profile) -> RingCollection

"""

    Vertices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Vertices(self: Profile) -> CompoundCurve2dVertexCollection

"""



class ProfileExtrusionDirection(Enum):
    """ enum ProfileExtrusionDirection, values: ExtrudeInXDir (0), ExtrudeInYDir (1), ExtrudeInZDir (2) """
    ExtrudeInXDir = None
    ExtrudeInYDir = None
    ExtrudeInZDir = None
    value__ = None


class ProfileResult(Enum):
    """ enum ProfileResult, values: PointInProfile (0), PointInRing (4), PointOnRing (2), PointOnVoidRing (3), PointOutsideProfile (1), PointOutsideRing (5), RingCoincidesWithRing (7), RingCoincidesWithVoidRing (8), RingInsideProfile (6), RingOutsideProfile (9) """
    PointInProfile = None
    PointInRing = None
    PointOnRing = None
    PointOnVoidRing = None
    PointOutsideProfile = None
    PointOutsideRing = None
    RingCoincidesWithRing = None
    RingCoincidesWithVoidRing = None
    RingInsideProfile = None
    RingOutsideProfile = None
    value__ = None


class Ring(CompoundCurve2d):
    """
    Ring(points: Point2dCollection)
    Ring()
    """
    def CalculateSegmentPositions(self, *__args):
        """ CalculateSegmentPositions(self: Ring, extrusionDirection: ProfileExtrusionDirection, calculateOnlyForNonMarked: bool)CalculateSegmentPositions(self: Ring, topLeft: Point2d, bottomRight: Point2d, extrusionDirection: ProfileExtrusionDirection, calculateOnlyForNonMarked: bool) """
        pass

    @staticmethod
    def Create(unmanagedPointer, bAutoDelete):
        """ Create(unmanagedPointer: IntPtr, bAutoDelete: bool) -> Ring """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetExtrusion(self, direction, deviation, maxFacetsPerSegment):
        """ GetExtrusion(self: Ring, direction: Vector3d, deviation: float, maxFacetsPerSegment: int) -> Body """
        pass

    def GetFace(self, deviation, maxFacetsPerSegment):
        """ GetFace(self: Ring, deviation: float, maxFacetsPerSegment: int) -> Body """
        pass

    def IsContainedBy(self, otherRing):
        """ IsContainedBy(self: Ring, otherRing: Ring) -> bool """
        pass

    def IsTopologicallyEquivalent(self, otherRing, offset):
        """ IsTopologicallyEquivalent(self: Ring, otherRing: Ring) -> (bool, int) """
        pass

    def MirrorSegmentPositions(self):
        """ MirrorSegmentPositions(self: Ring) """
        pass

    def ModifySegmentPositions(self, *__args):
        """ ModifySegmentPositions(self: Ring, oldSegmentPosition: SegmentPosition, newSegmentPosition: SegmentPosition)ModifySegmentPositions(self: Ring, oldExtrusionDirection: ProfileExtrusionDirection, newExtrusionDirection: ProfileExtrusionDirection) """
        pass

    def PointInRing(self, point):
        """ PointInRing(self: Ring, point: Point2d) -> ProfileResult """
        pass

    @staticmethod # known case of __new__
    def __new__(self, points=None):
        """
        __new__(cls: type, points: Point2dCollection)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: Ring) -> float

"""

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centroid(self: Ring) -> Point2d

"""

    IsCircle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCircle(self: Ring) -> bool

"""

    IsValidRing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValidRing(self: Ring) -> bool

"""

    IsVoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVoid(self: Ring) -> bool

Set: IsVoid(self: Ring) = value
"""

    Segments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Segments(self: Ring) -> Segment2dCollection

"""



class RingCollection(DisposableWrapper):
    # no doc
    def CopyTo(self, array, start):
        """ CopyTo(self: RingCollection, array: Array[Ring], start: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: RingCollection) -> IEnumerator """
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
    """Get: Count(self: RingCollection) -> int

"""



class Segment2dCollection(DisposableWrapper):
    # no doc
    def CopyTo(self, array, start):
        """ CopyTo(self: Segment2dCollection, array: Array[Segment2d], start: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Segment2dCollection) -> IEnumerator """
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
    """Get: Count(self: Segment2dCollection) -> int

"""



class SegmentPosition(Enum):
    """ enum SegmentPosition, values: Back (3), Bottom (7), Discard (1), Front (2), Left (4), None (0), Right (5), Top (6) """
    Back = None
    Bottom = None
    Discard = None
    Front = None
    Left = None
    None = None
    Right = None
    Top = None
    value__ = None


