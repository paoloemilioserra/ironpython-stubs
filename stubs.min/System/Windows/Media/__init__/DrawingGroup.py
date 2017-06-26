class DrawingGroup(Drawing, ISealable, IAnimatable, IResource, IDrawingContent):
    """
    Represents a collection of drawings that can be operated upon as a single drawing.
    
    DrawingGroup()
    """
    def Append(self):
        """
        Append(self: DrawingGroup) -> DrawingContext
        
            Opens the System.Windows.Media.DrawingGroup in order to populate its System.Windows.Media.DrawingGroup.Children. This method enables you to append additional System.Windows.Media.DrawingGroup.Children to 
             this System.Windows.Media.DrawingGroup.
        
            Returns: A System.Windows.Media.DrawingContext that you can use to describe the contents of this System.Windows.Media.DrawingGroup object.
        """
        pass

    def Clone(self):
        """
        Clone(self: DrawingGroup) -> DrawingGroup
        
            Creates a modifiable deep copy of this System.Windows.Media.DrawingGroup and makes deep copies of its values.
            Returns: A modifiable clone of the current object. The System.Windows.Freezable.IsFrozen property of the cloned object returns false even if the System.Windows.Freezable.IsFrozen property of the source is true.
        """
        pass

    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a clone (deep copy) of the specified System.Windows.Freezable using base (non-animated) property values.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValue(self):
        """
        CloneCurrentValue(self: DrawingGroup) -> DrawingGroup
        
            Creates a modifiable deep copy of this System.Windows.Media.DrawingGroup object and makes deep copies of its current values.
            Returns: A modifiable clone of the current object. The System.Windows.Freezable.IsFrozen property of the cloned object is false even if the System.Windows.Freezable.IsFrozen property of the source is true.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a modifiable clone (deep copy) of the specified System.Windows.Freezable using current property values.
        
            sourceFreezable: The System.Windows.Freezable to be cloned.
        """
        pass

    def CreateInstance(self, *args): #cannot find CLR method
        """
        CreateInstance(self: Freezable) -> Freezable
        
            Initializes a new instance of the System.Windows.Freezable class.
            Returns: The new instance.
        """
        pass

    def CreateInstanceCore(self, *args): #cannot find CLR method
        """ CreateInstanceCore(self: DrawingGroup) -> Freezable """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Animatable, isChecking: bool) -> bool
        
            Makes this System.Windows.Media.Animation.Animatable object unmodifiable or determines whether it can be made unmodifiable.
        
            isChecking: true if this method should simply determine whether this instance can be frozen. false if this instance should actually freeze itself when this method is called.
            Returns: If isChecking is true, this method returns true if this System.Windows.Media.Animation.Animatable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method 
             returns true if the if this System.Windows.Media.Animation.Animatable is now unmodifiable, or false if it cannot be made unmodifiable, with the side effect of having begun to change the frozen status of 
             this object.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the instance a frozen clone of the specified System.Windows.Freezable using base (non-animated) property values.
        
            sourceFreezable: The instance to copy.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: Freezable, sourceFreezable: Freezable)
            Makes the current instance a frozen clone of the specified System.Windows.Freezable. If the object has animated dependency properties, their current animated values are copied.
        
            sourceFreezable: The System.Windows.Freezable to copy and freeze.
        """
        pass

    def OnChanged(self, *args): #cannot find CLR method
        """
        OnChanged(self: Freezable)
            Called when the current System.Windows.Freezable object is modified.
        """
        pass

    def OnFreezablePropertyChanged(self, *args): #cannot find CLR method
        """
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject, property: DependencyProperty)
            This member supports the Windows Presentation Foundation (WPF) infrastructure and is not intended to be used directly from your code.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
            property: The property that changed.
        OnFreezablePropertyChanged(self: Freezable, oldValue: DependencyObject, newValue: DependencyObject)
            Ensures that appropriate context pointers are established for a System.Windows.DependencyObjectType data member that has just been set.
        
            oldValue: The previous value of the data member.
            newValue: The current value of the data member.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: Freezable, e: DependencyPropertyChangedEventArgs)
            Overrides the System.Windows.DependencyObject implementation of System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs) to also invoke any 
             System.Windows.Freezable.Changed handlers in response to a changing dependency property of type System.Windows.Freezable.
        
        
            e: Event data that contains information about which property changed, and its old and new values.
        """
        pass

    def Open(self):
        """
        Open(self: DrawingGroup) -> DrawingContext
        
            Opens the System.Windows.Media.DrawingGroup in order to populate its System.Windows.Media.DrawingGroup.Children and clears any existing System.Windows.Media.DrawingGroup.Children.
            Returns: A System.Windows.Media.DrawingContext that can be used to describe the contents of this System.Windows.Media.DrawingGroup object.
        """
        pass

    def ReadPreamble(self, *args): #cannot find CLR method
        """
        ReadPreamble(self: Freezable)
            Ensures that the System.Windows.Freezable is being accessed from a valid thread. Inheritors of System.Windows.Freezable must call this method at the beginning of any API that reads data members that are 
             not dependency properties.
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

    def WritePostscript(self, *args): #cannot find CLR method
        """
        WritePostscript(self: Freezable)
            Raises the System.Windows.Freezable.Changed event for the System.Windows.Freezable and invokes its System.Windows.Freezable.OnChanged method. Classes that derive from System.Windows.Freezable should call 
             this method at the end of any API that modifies class members that are not stored as dependency properties.
        """
        pass

    def WritePreamble(self, *args): #cannot find CLR method
        """
        WritePreamble(self: Freezable)
            Verifies that the System.Windows.Freezable is not frozen and that it is being accessed from a valid threading context. System.Windows.Freezable inheritors should call this method at the beginning of any 
             API that writes to data members that are not dependency properties.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    BitmapEffect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Effects.BitmapEffect to apply to this System.Windows.Media.DrawingGroup.

Get: BitmapEffect(self: DrawingGroup) -> BitmapEffect

Set: BitmapEffect(self: DrawingGroup) = value
"""

    BitmapEffectInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the region where the System.Windows.Media.DrawingGroup applies its System.Windows.Media.DrawingGroup.BitmapEffect and, optionally, a System.Windows.Media.Imaging.BitmapSource to use as input for its System.Windows.Media.DrawingGroup.BitmapEffect.

Get: BitmapEffectInput(self: DrawingGroup) -> BitmapEffectInput

Set: BitmapEffectInput(self: DrawingGroup) = value
"""

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Drawing objects that are contained in this System.Windows.Media.DrawingGroup.

Get: Children(self: DrawingGroup) -> DrawingCollection

Set: Children(self: DrawingGroup) = value
"""

    ClipGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the clip region of this System.Windows.Media.DrawingGroup.

Get: ClipGeometry(self: DrawingGroup) -> Geometry

Set: ClipGeometry(self: DrawingGroup) = value
"""

    GuidelineSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.GuidelineSet to apply to this System.Windows.Media.DrawingGroup.

Get: GuidelineSet(self: DrawingGroup) -> GuidelineSet

Set: GuidelineSet(self: DrawingGroup) = value
"""

    Opacity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the opacity of this System.Windows.Media.DrawingGroup.

Get: Opacity(self: DrawingGroup) -> float

Set: Opacity(self: DrawingGroup) = value
"""

    OpacityMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the brush used to alter the opacity of select regions of this System.Windows.Media.DrawingGroup.

Get: OpacityMask(self: DrawingGroup) -> Brush

Set: OpacityMask(self: DrawingGroup) = value
"""

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Media.Transform that is applied to this System.Windows.Media.DrawingGroup.

Get: Transform(self: DrawingGroup) -> Transform

Set: Transform(self: DrawingGroup) = value
"""


    BitmapEffectInputProperty = None
    BitmapEffectProperty = None
    ChildrenProperty = None
    ClipGeometryProperty = None
    GuidelineSetProperty = None
    OpacityMaskProperty = None
    OpacityProperty = None
    TransformProperty = None

