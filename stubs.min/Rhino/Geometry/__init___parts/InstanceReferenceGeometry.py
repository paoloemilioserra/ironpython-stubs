class InstanceReferenceGeometry(GeometryBase, IDisposable, ISerializable):
    """ InstanceReferenceGeometry(instanceDefinitionId: Guid, transform: Transform) """
    def ConstructConstObject(self, *args): #cannot find CLR method
        """ ConstructConstObject(self: CommonObject, parentObject: object, subobject_index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: CommonObject, disposing: bool) """
        pass

    def NonConstOperation(self, *args): #cannot find CLR method
        """ NonConstOperation(self: CommonObject) """
        pass

    def OnSwitchToNonConst(self, *args): #cannot find CLR method
        """ OnSwitchToNonConst(self: GeometryBase) """
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
    def __new__(self, instanceDefinitionId, transform):
        """ __new__(cls: type, instanceDefinitionId: Guid, transform: Transform) """
        pass

    ParentIdefId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentIdefId(self: InstanceReferenceGeometry) -> Guid

"""

    Xform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Xform(self: InstanceReferenceGeometry) -> Transform

"""


