class CompositionTarget(DispatcherObject, IDisposable, ICompositionTarget):
    """ Represents the display surface of your application. """
    def Dispose(self):
        """
        Dispose(self: CompositionTarget)
            Disposes System.Windows.Media.CompositionTarget.
        """
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

    RootVisual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the root visual of the System.Windows.Media.CompositionTarget.

Get: RootVisual(self: CompositionTarget) -> Visual

Set: RootVisual(self: CompositionTarget) = value
"""

    TransformFromDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a matrix that can be used to transform coordinates from the rendering destination device to this target.

Get: TransformFromDevice(self: CompositionTarget) -> Matrix

"""

    TransformToDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a matrix that can be used to transform coordinates from this target to the rendering destination device.

Get: TransformToDevice(self: CompositionTarget) -> Matrix

"""


    Rendering = None

