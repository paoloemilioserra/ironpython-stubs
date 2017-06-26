class TouchPointCollection(Collection[TouchPoint], IList[TouchPoint], ICollection[TouchPoint], IEnumerable[TouchPoint], IEnumerable, IList, ICollection, IReadOnlyList[TouchPoint], IReadOnlyCollection[TouchPoint]):
    """
    Contains a collection of System.Windows.Input.TouchPoint objects.
    
    TouchPointCollection()
    """
    def ClearItems(self, *args): #cannot find CLR method
        """
        ClearItems(self: Collection[TouchPoint])
            Removes all elements from the System.Collections.ObjectModel.Collection.
        """
        pass

    def InsertItem(self, *args): #cannot find CLR method
        """ InsertItem(self: Collection[TouchPoint], index: int, item: TouchPoint) """
        pass

    def RemoveItem(self, *args): #cannot find CLR method
        """
        RemoveItem(self: Collection[TouchPoint], index: int)
            Removes the element at the specified index of the System.Collections.ObjectModel.Collection.
        
            index: The zero-based index of the element to remove.
        """
        pass

    def SetItem(self, *args): #cannot find CLR method
        """ SetItem(self: Collection[TouchPoint], index: int, item: TouchPoint) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Collections.Generic.IList wrapper around the System.Collections.ObjectModel.Collection.

"""


