class RebarShapeConstraintCircumference(RebarShapeConstraint, IDisposable):
    """
    A circumference constraint associated with an arc in a RebarShapeDefinition.
    
    RebarShapeConstraintCircumference(paramId: ElementId, refType: RebarShapeArcReferenceType)
    """
    def Dispose(self):
        """ Dispose(self: RebarShapeConstraint, A_0: bool) """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: RebarShapeConstraint, disposing: bool) """
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
    def __new__(self, paramId, refType):
        """ __new__(cls: type, paramId: ElementId, refType: RebarShapeArcReferenceType) """
        pass

    ArcReferenceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The choice of rule for measuring the diameter.

Get: ArcReferenceType(self: RebarShapeConstraintCircumference) -> RebarShapeArcReferenceType

"""


