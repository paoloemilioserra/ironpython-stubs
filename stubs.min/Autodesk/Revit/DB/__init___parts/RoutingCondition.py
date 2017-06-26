class RoutingCondition(object, IDisposable):
    """
    RoutingCondition represents routing information that is used as input when determining if a routing criterion,
       such as minimum or maximum diameter, is met.
    
    RoutingCondition(diameter: float)
    """
    def Dispose(self):
        """ Dispose(self: RoutingCondition) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RoutingCondition, disposing: bool) """
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

    @staticmethod # known case of __new__
    def __new__(self, diameter):
        """ __new__(cls: type, diameter: float) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Diameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The diameter of the segment or fitting specified for the routing condition.

Get: Diameter(self: RoutingCondition) -> float

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: RoutingCondition) -> bool

"""


