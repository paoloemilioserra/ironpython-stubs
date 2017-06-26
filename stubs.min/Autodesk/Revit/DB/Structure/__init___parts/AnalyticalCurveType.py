class AnalyticalCurveType(Enum, IComparable, IFormattable, IConvertible):
    """
    Identifies what type of Analytical Model curves should be extracted.
    
    enum AnalyticalCurveType, values: ActiveCurves (3), AllRigidLinks (6), ApproximatedCurves (4), BaseCurve (5), RawCurves (0), RigidLinkHead (1), RigidLinkTail (2)
    """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    ActiveCurves = None
    AllRigidLinks = None
    ApproximatedCurves = None
    BaseCurve = None
    RawCurves = None
    RigidLinkHead = None
    RigidLinkTail = None
    value__ = None

