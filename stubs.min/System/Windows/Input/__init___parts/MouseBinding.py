class MouseBinding(InputBinding, ISealable, ICommandSource):
    """
    Binds a System.Windows.Input.MouseGesture to a System.Windows.Input.RoutedCommand (or another System.Windows.Input.ICommand implementation).
    
    MouseBinding()
    MouseBinding(command: ICommand, gesture: MouseGesture)
    """
    def CloneCore(self, *args): #cannot find CLR method
        """
        CloneCore(self: MouseBinding, sourceFreezable: Freezable)
            Copies the base (non-animated) values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
        """
        pass

    def CloneCurrentValueCore(self, *args): #cannot find CLR method
        """
        CloneCurrentValueCore(self: MouseBinding, sourceFreezable: Freezable)
            Copies the current values of the properties of the specified object.
        
            sourceFreezable: The object to clone.
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
        """
        CreateInstanceCore(self: MouseBinding) -> Freezable
        
            Creates an instance of an System.Windows.Input.MouseBinding.
            Returns: The new object.
        """
        pass

    def FreezeCore(self, *args): #cannot find CLR method
        """
        FreezeCore(self: Freezable, isChecking: bool) -> bool
        
            Makes the System.Windows.Freezable object unmodifiable or tests whether it can be made unmodifiable.
        
            isChecking: true to return an indication of whether the object can be frozen (without actually freezing it); false to actually freeze the object.
            Returns: If isChecking is true, this method returns true if the System.Windows.Freezable can be made unmodifiable, or false if it cannot be made unmodifiable. If isChecking is false, this method returns true if the 
             if the specified System.Windows.Freezable is now unmodifiable, or false if it cannot be made unmodifiable.
        """
        pass

    def GetAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetAsFrozenCore(self: MouseBinding, sourceFreezable: Freezable)
            Creates the instance a frozen clone of the specified System.Windows.Freezable by using base (non-animated) property values.
        
            sourceFreezable: The object to clone.
        """
        pass

    def GetCurrentValueAsFrozenCore(self, *args): #cannot find CLR method
        """
        GetCurrentValueAsFrozenCore(self: MouseBinding, sourceFreezable: Freezable)
            Creates the current instance a frozen clone of the specified System.Windows.Freezable. If the object has animated dependency properties, their current animated values are copied.
        
            sourceFreezable: The object to clone.
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

    @staticmethod # known case of __new__
    def __new__(self, command=None, gesture=None):
        """
        __new__(cls: type)
        __new__(cls: type, command: ICommand, gesture: MouseGesture)
        """
        pass

    Gesture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the gesture associated with this System.Windows.Input.MouseBinding.

Get: Gesture(self: MouseBinding) -> InputGesture

Set: Gesture(self: MouseBinding) = value
"""

    MouseAction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Windows.Input.MouseAction associated with this System.Windows.Input.MouseBinding.

Get: MouseAction(self: MouseBinding) -> MouseAction

Set: MouseAction(self: MouseBinding) = value
"""


    MouseActionProperty = None

