class HostVisual(ContainerVisual, IResource):
    """
    Represents a System.Windows.Media.Visual object that can be connected anywhere to a parent visual tree.
    
    HostVisual()
    """
    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: ContainerVisual, index: int) -> Visual
        
            Returns a specified child System.Windows.Media.Visual for the parent System.Windows.Media.ContainerVisual.
        
            index: A 32-bit signed integer that represents the index value of the child System.Windows.Media.Visual. The value of index must be between 0 and System.Windows.Media.ContainerVisual.VisualChildrenCount - 1.
            Returns: The child System.Windows.Media.Visual.
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: HostVisual, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements System.Windows.Media.HostVisual.HitTestCore(System.Windows.Media.GeometryHitTestParameters) to supply base hit testing behavior (returning System.Windows.Media.GeometryHitTestParameters).
        
            hitTestParameters: A value of type System.Windows.Media.GeometryHitTestParameters.
            Returns: Returns a value of type System.Windows.Media.GeometryHitTestResult. The System.Windows.Media.GeometryHitTestResult.VisualHit property contains the visual that was hit.
        HitTestCore(self: HostVisual, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements System.Windows.Media.HostVisual.HitTestCore(System.Windows.Media.PointHitTestParameters) to supply base hit testing behavior (returning System.Windows.Media.PointHitTestParameters).
        
            hitTestParameters: A value of type System.Windows.Media.PointHitTestParameters.
            Returns: Returns a value of type System.Windows.Media.HitTestResult. The System.Windows.Media.HitTestResult.VisualHit property contains the visual object that was hit.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: DependencyObject, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this System.Windows.DependencyObject has been updated. The specific dependency property that changed is reported in the event data.
        
            e: Event data that will contain the dependency property identifier of interest, the property metadata for the type, and old and new values.
        """
        pass

    def OnVisualChildrenChanged(self, *args): #cannot find CLR method
        """
        OnVisualChildrenChanged(self: Visual, visualAdded: DependencyObject, visualRemoved: DependencyObject)
            Called when the System.Windows.Media.VisualCollection of the visual object is modified.
        
            visualAdded: The System.Windows.Media.Visual that was added to the collection
            visualRemoved: The System.Windows.Media.Visual that was removed from the collection
        """
        pass

    def OnVisualParentChanged(self, *args): #cannot find CLR method
        """
        OnVisualParentChanged(self: Visual, oldParent: DependencyObject)
            Called when the parent of the visual object is changed.
        
            oldParent: A value of type System.Windows.DependencyObject that represents the previous parent of the System.Windows.Media.Visual object. If the System.Windows.Media.Visual object did not have a previous parent, the 
             value of the parameter is null.
        """
        pass

    def RemoveVisualChild(self, *args): #cannot find CLR method
        """
        RemoveVisualChild(self: Visual, child: Visual)
            Removes the parent-child relationship between two visuals.
        
            child: The child visual object to remove from the parent visual.
        """
        pass

    def ShouldSerializeProperty(self, *args): #cannot find CLR method
        """
        ShouldSerializeProperty(self: DependencyObject, dp: DependencyProperty) -> bool
        
            Returns a value that indicates whether serialization processes should serialize the value for the provided dependency property.
        
            dp: The identifier for the dependency property that should be serialized.
            Returns: true if the dependency property that is supplied should be value-serialized; otherwise, false.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    VisualBitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect value for the System.Windows.Media.Visual.

"""

    VisualBitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffectInput value for the System.Windows.Media.Visual.

"""

    VisualBitmapScalingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.BitmapScalingMode for the System.Windows.Media.Visual.

"""

    VisualCacheMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a cached representation of the System.Windows.Media.Visual.

"""

    VisualChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of children for the System.Windows.Media.ContainerVisual.

"""

    VisualClearTypeHint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.ClearTypeHint that determines how ClearType is rendered in the System.Windows.Media.Visual.

"""

    VisualClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of the System.Windows.Media.Visual as a System.Windows.Media.Geometry value.

"""

    VisualEdgeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the edge mode of the System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.

"""

    VisualEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the bitmap effect to apply to the System.Windows.Media.Visual.

"""

    VisualOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the offset value of the visual object.

"""

    VisualOpacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of the System.Windows.Media.Visual.

"""

    VisualOpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.

"""

    VisualParent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the visual tree parent of the visual object.

"""

    VisualScrollableAreaClip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a clipped scrollable area for the System.Windows.Media.Visual.

"""

    VisualTextHintingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextHintingMode of the System.Windows.Media.Visual.

"""

    VisualTextRenderingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.TextRenderingMode of the System.Windows.Media.Visual.

"""

    VisualTransform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform value for the System.Windows.Media.Visual.

"""

    VisualXSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate (vertical) guideline collection.

"""

    VisualYSnappingGuidelines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate (horizontal) guideline collection.

"""


