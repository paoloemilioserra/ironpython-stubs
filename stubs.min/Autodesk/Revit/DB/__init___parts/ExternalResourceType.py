class ExternalResourceType(GuidEnum):
    """
    A type class used to distinguish between different kinds of external resource.
    
    ExternalResourceType(guid: Guid)
    """
    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

