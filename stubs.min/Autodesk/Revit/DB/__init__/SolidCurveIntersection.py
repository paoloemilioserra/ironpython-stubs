class SolidCurveIntersection(object, IEnumerable[Curve], IEnumerable, IDisposable):
    """ This class represents the results of a calculation of intersection between a solid volume and a curve. """
    def Dispose(self):
        """ Dispose(self: SolidCurveIntersection) """
        pass

    def GetCurveSegment(self, index):
        """
        GetCurveSegment(self: SolidCurveIntersection, index: int) -> Curve
        
            Gets the curve segment generated by intersection.
        
            index: The index.
            Returns: The curve.
        """
        pass

    def GetCurveSegmentExtents(self, index):
        """
        GetCurveSegmentExtents(self: SolidCurveIntersection, index: int) -> CurveExtents
        
            Gets the extents for the given curve segment generated by intersection.
        
            index: The index.
            Returns: The curve extents.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: SolidCurveIntersection) -> IEnumerator[Curve]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: SolidCurveIntersection, disposing: bool) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Curve](enumerable: IEnumerable[Curve], value: Curve) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: SolidCurveIntersection) -> bool

"""

    ResultType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The result type used to calculate the intersections.

Get: ResultType(self: SolidCurveIntersection) -> SolidCurveIntersectionMode

"""

    SegmentCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The number of segments in the results.

Get: SegmentCount(self: SolidCurveIntersection) -> int

"""


