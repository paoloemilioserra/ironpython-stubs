class FloorType(HostObjAttributes, IDisposable):
    """ An object that specifies the type of a floor in Autodesk Revit. """
    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
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

    IsFoundationSlab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns whether the element FloorAttributes type is FoundationSlab.

Get: IsFoundationSlab(self: FloorType) -> bool

"""

    StructuralMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the identifier of the material that defines the element's structural analysis properties.

Get: StructuralMaterialId(self: FloorType) -> ElementId

Set: StructuralMaterialId(self: FloorType) = value
"""

    ThermalProperties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The calculated and settable thermal properties of the FloorType

Get: ThermalProperties(self: FloorType) -> ThermalProperties

"""


