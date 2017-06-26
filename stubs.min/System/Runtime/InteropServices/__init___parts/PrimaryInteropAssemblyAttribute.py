class PrimaryInteropAssemblyAttribute(Attribute, _Attribute):
    """
    Indicates that the attributed assembly is a primary interop assembly.
    
    PrimaryInteropAssemblyAttribute(major: int, minor: int)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, major, minor):
        """ __new__(cls: type, major: int, minor: int) """
        pass

    MajorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the major version number of the type library for which this assembly is the primary interop assembly.

Get: MajorVersion(self: PrimaryInteropAssemblyAttribute) -> int

"""

    MinorVersion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minor version number of the type library for which this assembly is the primary interop assembly.

Get: MinorVersion(self: PrimaryInteropAssemblyAttribute) -> int

"""


