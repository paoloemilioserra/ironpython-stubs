class ItemPropertyInfo(object):
    """
    Contains information about a property.
    
    ItemPropertyInfo(name: str, type: Type, descriptor: object)
    """
    @staticmethod # known case of __new__
    def __new__(self, name, type, descriptor):
        """ __new__(cls: type, name: str, type: Type, descriptor: object) """
        pass

    Descriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get an object that contains additional information about the property.

Get: Descriptor(self: ItemPropertyInfo) -> object

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the name of the property.

Get: Name(self: ItemPropertyInfo) -> str

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the property.

Get: PropertyType(self: ItemPropertyInfo) -> Type

"""


