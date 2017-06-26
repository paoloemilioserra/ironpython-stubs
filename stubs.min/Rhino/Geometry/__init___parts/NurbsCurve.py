class NurbsCurve(Curve, IDisposable, ISerializable, IEpsilonComparable[NurbsCurve]):
    """
    NurbsCurve(other: NurbsCurve)
    NurbsCurve(degree: int, pointCount: int)
    NurbsCurve(dimension: int, rational: bool, order: int, pointCount: int)
    """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    @staticmethod
    def Create(periodic, degree, points):
        """ Create(periodic: bool, degree: int, points: IEnumerable[Point3d]) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromArc(arc):
        """ CreateFromArc(arc: Arc) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromCircle(circle):
        """ CreateFromCircle(circle: Circle) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromEllipse(ellipse):
        """ CreateFromEllipse(ellipse: Ellipse) -> NurbsCurve """
        pass

    @staticmethod
    def CreateFromLine(line):
        """ CreateFromLine(line: Line) -> NurbsCurve """
        pass

    def Dispose(self):
        """ Dispose(self: Curve, disposing: bool) """
        pass

    def EpsilonEquals(self, other, epsilon):
        """ EpsilonEquals(self: NurbsCurve, other: NurbsCurve, epsilon: float) -> bool """
        pass

    def GrevilleParameter(self, index):
        """ GrevilleParameter(self: NurbsCurve, index: int) -> float """
        pass

    def GrevilleParameters(self):
        """ GrevilleParameters(self: NurbsCurve) -> Array[float] """
        pass

    def GrevillePoint(self, index):
        """ GrevillePoint(self: NurbsCurve, index: int) -> Point3d """
        pass

    def GrevillePoints(self):
        """ GrevillePoints(self: NurbsCurve) -> Point3dList """
        pass

    def IncreaseDegree(self, desiredDegree):
        """ IncreaseDegree(self: NurbsCurve, desiredDegree: int) -> bool """
        pass

    @staticmethod
    def IsDuplicate(curveA, curveB, ignoreParameterization, tolerance):
        """ IsDuplicate(curveA: NurbsCurve, curveB: NurbsCurve, ignoreParameterization: bool, tolerance: float) -> bool """
        pass

    def MakePiecewiseBezier(self, setEndWeightsToOne):
        """ MakePiecewiseBezier(self: NurbsCurve, setEndWeightsToOne: bool) -> bool """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: Curve) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
        pass

    def Reparameterize(self, c):
        """ Reparameterize(self: NurbsCurve, c: float) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, other: NurbsCurve)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, degree: int, pointCount: int)
        __new__(cls: type, dimension: int, rational: bool, order: int, pointCount: int)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    HasBezierSpans = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasBezierSpans(self: NurbsCurve) -> bool

"""

    IsRational = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRational(self: NurbsCurve) -> bool

"""

    Knots = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Knots(self: NurbsCurve) -> NurbsCurveKnotList

"""

    Order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Order(self: NurbsCurve) -> int

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: NurbsCurve) -> NurbsCurvePointList

"""


