class TypeLibVarAttribute(Attribute, _Attribute):
    """
    Contains the System.Runtime.InteropServices.VARFLAGS that were originally imported for this field from the COM type library.
    
    TypeLibVarAttribute(flags: TypeLibVarFlags)
    TypeLibVarAttribute(flags: Int16)
    """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, flags):
        """
        __new__(cls: type, flags: TypeLibVarFlags)
        __new__(cls: type, flags: Int16)
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the System.Runtime.InteropServices.TypeLibVarFlags value for this field.

Get: Value(self: TypeLibVarAttribute) -> TypeLibVarFlags

"""


