class ProgressBar(RangeBase, IResource, IAnimatable, IInputElement, IFrameworkInputElement, ISupportInitialize, IHaveResources, IQueryAmbient):
    """
    Indicates the progress of an operation.
    
    ProgressBar()
    """
    def AddLogicalChild(self, *args): #cannot find CLR method
        """
        AddLogicalChild(self: FrameworkElement, child: object)
            Adds the provided object to the logical tree of this element.
        
            child: Child element to be added.
        """
        pass

    def AddVisualChild(self, *args): #cannot find CLR method
        """
        AddVisualChild(self: Visual, child: Visual)
            Defines the parent-child relationship between two visuals.
        
            child: The child visual object to add to parent visual.
        """
        pass

    def ArrangeCore(self, *args): #cannot find CLR method
        """
        ArrangeCore(self: FrameworkElement, finalRect: Rect)
            Implements System.Windows.UIElement.ArrangeCore(System.Windows.Rect) (defined as virtual in System.Windows.UIElement) and seals the implementation.
        
            finalRect: The final area within the parent that this element should use to arrange itself and its children.
        """
        pass

    def ArrangeOverride(self, *args): #cannot find CLR method
        """
        ArrangeOverride(self: Control, arrangeBounds: Size) -> Size
        
            Called to arrange and size the content of a System.Windows.Controls.Control object.
        
            arrangeBounds: The computed size that is used to arrange the content.
            Returns: The size of the control.
        """
        pass

    def GetLayoutClip(self, *args): #cannot find CLR method
        """
        GetLayoutClip(self: FrameworkElement, layoutSlotSize: Size) -> Geometry
        
            Returns a geometry for a clipping mask. The mask applies if the layout system attempts to arrange an element that is larger than the available display space.
        
            layoutSlotSize: The size of the part of the element that does visual presentation.
            Returns: The clipping geometry.
        """
        pass

    def GetTemplateChild(self, *args): #cannot find CLR method
        """
        GetTemplateChild(self: FrameworkElement, childName: str) -> DependencyObject
        
            Returns the named element in the visual tree of an instantiated System.Windows.Controls.ControlTemplate.
        
            childName: Name of the child to find.
            Returns: The requested element. May be null if no element of the requested name exists.
        """
        pass

    def GetUIParentCore(self, *args): #cannot find CLR method
        """
        GetUIParentCore(self: FrameworkElement) -> DependencyObject
        
            Returns an alternative logical parent for this element if there is no visual parent.
            Returns: Returns something other than null whenever a WPF framework-level implementation of this method has a non-visual parent connection.
        """
        pass

    def GetVisualChild(self, *args): #cannot find CLR method
        """
        GetVisualChild(self: FrameworkElement, index: int) -> Visual
        
            Overrides System.Windows.Media.Visual.GetVisualChild(System.Int32), and returns a child at the specified index from a collection of child elements.
        
            index: The zero-based index of the requested child element in the collection.
            Returns: The requested child element. This should not return null; if the provided index is out of range, an exception is thrown.
        """
        pass

    def HitTestCore(self, *args): #cannot find CLR method
        """
        HitTestCore(self: UIElement, hitTestParameters: GeometryHitTestParameters) -> GeometryHitTestResult
        
            Implements System.Windows.Media.Visual.HitTestCore(System.Windows.Media.GeometryHitTestParameters) to supply base element hit testing behavior (returning System.Windows.Media.GeometryHitTestResult).
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated geometry.
        HitTestCore(self: UIElement, hitTestParameters: PointHitTestParameters) -> HitTestResult
        
            Implements System.Windows.Media.Visual.HitTestCore(System.Windows.Media.PointHitTestParameters) to supply base element hit testing behavior (returning System.Windows.Media.HitTestResult).
        
            hitTestParameters: Describes the hit test to perform, including the initial hit point.
            Returns: Results of the test, including the evaluated point.
        """
        pass

    def MeasureCore(self, *args): #cannot find CLR method
        """
        MeasureCore(self: FrameworkElement, availableSize: Size) -> Size
        
            Implements basic measure-pass layout system behavior for System.Windows.FrameworkElement.
        
            availableSize: The available size that the parent element can give to the child elements.
            Returns: The desired size of this element in layout.
        """
        pass

    def MeasureOverride(self, *args): #cannot find CLR method
        """
        MeasureOverride(self: Control, constraint: Size) -> Size
        
            Called to remeasure a control.
        
            constraint: The maximum size that the method can return.
            Returns: The size of the control, up to the maximum specified by constraint.
        """
        pass

    def OnAccessKey(self, *args): #cannot find CLR method
        """
        OnAccessKey(self: UIElement, e: AccessKeyEventArgs)
            Provides class handling for when an access key that is meaningful for this element is invoked.
        
            e: The event data to the access key event. The event data reports which key was invoked, and indicate whether the System.Windows.Input.AccessKeyManager object that controls the sending of these events also 
             sent this access key invocation to other elements.
        """
        pass

    def OnApplyTemplate(self):
        """
        OnApplyTemplate(self: ProgressBar)
            Called when a template is applied to a System.Windows.Controls.ProgressBar.
        """
        pass

    def OnChildDesiredSizeChanged(self, *args): #cannot find CLR method
        """
        OnChildDesiredSizeChanged(self: UIElement, child: UIElement)
            Supports layout behavior when a child element is resized.
        
            child: The child element that is being resized.
        """
        pass

    def OnContextMenuClosing(self, *args): #cannot find CLR method
        """
        OnContextMenuClosing(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ContextMenuClosing routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: Provides data about the event.
        """
        pass

    def OnContextMenuOpening(self, *args): #cannot find CLR method
        """
        OnContextMenuOpening(self: FrameworkElement, e: ContextMenuEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ContextMenuOpening routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        """
        pass

    def OnCreateAutomationPeer(self, *args): #cannot find CLR method
        """
        OnCreateAutomationPeer(self: ProgressBar) -> AutomationPeer
        
            Provides an appropriate System.Windows.Automation.Peers.ProgressBarAutomationPeer implementation for this control, as part of the WPF automation infrastructure.
            Returns: The type-specific System.Windows.Automation.Peers.AutomationPeer implementation.
        """
        pass

    def OnDpiChanged(self, *args): #cannot find CLR method
        """ OnDpiChanged(self: Visual, oldDpi: DpiScale, newDpi: DpiScale) """
        pass

    def OnDragEnter(self, *args): #cannot find CLR method
        """
        OnDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragLeave(self, *args): #cannot find CLR method
        """
        OnDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDragOver(self, *args): #cannot find CLR method
        """
        OnDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnDrop(self, *args): #cannot find CLR method
        """
        OnDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.DragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnGiveFeedback(self, *args): #cannot find CLR method
        """
        OnGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.GiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnGotFocus(self, *args): #cannot find CLR method
        """
        OnGotFocus(self: FrameworkElement, e: RoutedEventArgs)
            Invoked whenever an unhandled System.Windows.UIElement.GotFocus event reaches this element in its route.
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        """
        pass

    def OnGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.GotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnGotMouseCapture(self, *args): #cannot find CLR method
        """
        OnGotMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.GotMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnGotStylusCapture(self, *args): #cannot find CLR method
        """
        OnGotStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.GotStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnGotTouchCapture(self, *args): #cannot find CLR method
        """
        OnGotTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.GotTouchCapture routed event that occurs when a touch is captured to this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnInitialized(self, *args): #cannot find CLR method
        """
        OnInitialized(self: FrameworkElement, e: EventArgs)
            Raises the System.Windows.FrameworkElement.Initialized event. This method is invoked whenever System.Windows.FrameworkElement.IsInitialized is set to true internally.
        
            e: The System.Windows.RoutedEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusedChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsKeyboardFocusedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsKeyboardFocusWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsKeyboardFocusWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked just before the System.Windows.UIElement.IsKeyboardFocusWithinChanged event is raised by this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsMouseDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsMouseDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsMouseDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCapturedChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCapturedChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCapturedChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: A System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusCaptureWithinChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusCaptureWithinChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusCaptureWithinChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnIsStylusDirectlyOverChanged(self, *args): #cannot find CLR method
        """
        OnIsStylusDirectlyOverChanged(self: UIElement, e: DependencyPropertyChangedEventArgs)
            Invoked when an unhandled System.Windows.UIElement.IsStylusDirectlyOverChanged event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.DependencyPropertyChangedEventArgs that contains the event data.
        """
        pass

    def OnKeyDown(self, *args): #cannot find CLR method
        """
        OnKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnKeyUp(self, *args): #cannot find CLR method
        """
        OnKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.KeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnLostFocus(self, *args): #cannot find CLR method
        """
        OnLostFocus(self: UIElement, e: RoutedEventArgs)
            Raises the System.Windows.UIElement.LostFocus�routed event by using the event data that is provided.
        
            e: A System.Windows.RoutedEventArgs that contains event data. This event data must contain the identifier for the System.Windows.UIElement.LostFocus event.
        """
        pass

    def OnLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.LostKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains event data.
        """
        pass

    def OnLostMouseCapture(self, *args): #cannot find CLR method
        """
        OnLostMouseCapture(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.LostMouseCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains event data.
        """
        pass

    def OnLostStylusCapture(self, *args): #cannot find CLR method
        """
        OnLostStylusCapture(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.LostStylusCapture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains event data.
        """
        pass

    def OnLostTouchCapture(self, *args): #cannot find CLR method
        """
        OnLostTouchCapture(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.LostTouchCapture routed event that occurs when this element loses a touch capture.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnManipulationBoundaryFeedback(self, *args): #cannot find CLR method
        """
        OnManipulationBoundaryFeedback(self: UIElement, e: ManipulationBoundaryFeedbackEventArgs)
            Called when the System.Windows.UIElement.ManipulationBoundaryFeedback event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationCompleted(self, *args): #cannot find CLR method
        """
        OnManipulationCompleted(self: UIElement, e: ManipulationCompletedEventArgs)
            Called when the System.Windows.UIElement.ManipulationCompleted event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationDelta(self, *args): #cannot find CLR method
        """
        OnManipulationDelta(self: UIElement, e: ManipulationDeltaEventArgs)
            Called when the System.Windows.UIElement.ManipulationDelta event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationInertiaStarting(self, *args): #cannot find CLR method
        """
        OnManipulationInertiaStarting(self: UIElement, e: ManipulationInertiaStartingEventArgs)
            Called when the System.Windows.UIElement.ManipulationInertiaStarting event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationStarted(self, *args): #cannot find CLR method
        """
        OnManipulationStarted(self: UIElement, e: ManipulationStartedEventArgs)
            Called when the System.Windows.UIElement.ManipulationStarted event occurs.
        
            e: The data for the event.
        """
        pass

    def OnManipulationStarting(self, *args): #cannot find CLR method
        """
        OnManipulationStarting(self: UIElement, e: ManipulationStartingEventArgs)
            Provides class handling for the System.Windows.UIElement.ManipulationStarting routed event that occurs when the manipulation processor is first created.
        
            e: A System.Windows.Input.ManipulationStartingEventArgs  that contains the event data.
        """
        pass

    def OnMaximumChanged(self, *args): #cannot find CLR method
        """
        OnMaximumChanged(self: ProgressBar, oldMaximum: float, newMaximum: float)
            Updates the current position of the System.Windows.Controls.ProgressBar when the System.Windows.Controls.Primitives.RangeBase.Maximum property changes.
        
            oldMaximum: Old value of the System.Windows.Controls.Primitives.RangeBase.Maximum property.
            newMaximum: New value of the System.Windows.Controls.Primitives.RangeBase.Maximum property.
        """
        pass

    def OnMinimumChanged(self, *args): #cannot find CLR method
        """
        OnMinimumChanged(self: ProgressBar, oldMinimum: float, newMinimum: float)
            Updates the current position of the System.Windows.Controls.ProgressBar when the System.Windows.Controls.Primitives.RangeBase.Minimum property changes.
        
            oldMinimum: Old value of the System.Windows.Controls.Primitives.RangeBase.Minimum property.
            newMinimum: New value of the System.Windows.Controls.Primitives.RangeBase.Minimum property.
        """
        pass

    def OnMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnMouseDoubleClick(self: Control, e: MouseButtonEventArgs)
            Raises the System.Windows.Controls.Control.MouseDoubleClick routed event.
        
            e: The event data.
        """
        pass

    def OnMouseDown(self, *args): #cannot find CLR method
        """
        OnMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. This event data reports details about the mouse button that was pressed and the handled state.
        """
        pass

    def OnMouseEnter(self, *args): #cannot find CLR method
        """
        OnMouseEnter(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseEnter�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeave(self, *args): #cannot find CLR method
        """
        OnMouseLeave(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseLeave�attached event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonDown�routed event is raised on this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnMouseMove(self, *args): #cannot find CLR method
        """
        OnMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.MouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnMouseUp(self, *args): #cannot find CLR method
        """
        OnMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the mouse button was released.
        """
        pass

    def OnMouseWheel(self, *args): #cannot find CLR method
        """
        OnMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.MouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragEnter(self, *args): #cannot find CLR method
        """
        OnPreviewDragEnter(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragEnter�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragLeave(self, *args): #cannot find CLR method
        """
        OnPreviewDragLeave(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragLeave�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDragOver(self, *args): #cannot find CLR method
        """
        OnPreviewDragOver(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDragOver�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewDrop(self, *args): #cannot find CLR method
        """
        OnPreviewDrop(self: UIElement, e: DragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewDrop�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.DragEventArgs that contains the event data.
        """
        pass

    def OnPreviewGiveFeedback(self, *args): #cannot find CLR method
        """
        OnPreviewGiveFeedback(self: UIElement, e: GiveFeedbackEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewGiveFeedback�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.GiveFeedbackEventArgs that contains the event data.
        """
        pass

    def OnPreviewGotKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewGotKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewGotKeyboardFocus�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyDown(self, *args): #cannot find CLR method
        """
        OnPreviewKeyDown(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewKeyUp(self, *args): #cannot find CLR method
        """
        OnPreviewKeyUp(self: UIElement, e: KeyEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyEventArgs that contains the event data.
        """
        pass

    def OnPreviewLostKeyboardFocus(self, *args): #cannot find CLR method
        """
        OnPreviewLostKeyboardFocus(self: UIElement, e: KeyboardFocusChangedEventArgs)
            Invoked when an unhandled System.Windows.Input.Keyboard.PreviewKeyDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.KeyboardFocusChangedEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseDoubleClick(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDoubleClick(self: Control, e: MouseButtonEventArgs)
            Raises the System.Windows.Controls.Control.PreviewMouseDoubleClick routed event.
        
            e: The event data.
        """
        pass

    def OnPreviewMouseDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseDown attached�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were pressed.
        """
        pass

    def OnPreviewMouseLeftButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was pressed.
        """
        pass

    def OnPreviewMouseLeftButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseLeftButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseLeftButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the left mouse button was released.
        """
        pass

    def OnPreviewMouseMove(self, *args): #cannot find CLR method
        """
        OnPreviewMouseMove(self: UIElement, e: MouseEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseEventArgs that contains the event data.
        """
        pass

    def OnPreviewMouseRightButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonDown(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonDown�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was pressed.
        """
        pass

    def OnPreviewMouseRightButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseRightButtonUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.UIElement.PreviewMouseRightButtonUp�routed event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that the right mouse button was released.
        """
        pass

    def OnPreviewMouseUp(self, *args): #cannot find CLR method
        """
        OnPreviewMouseUp(self: UIElement, e: MouseButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseButtonEventArgs that contains the event data. The event data reports that one or more mouse buttons were released.
        """
        pass

    def OnPreviewMouseWheel(self, *args): #cannot find CLR method
        """
        OnPreviewMouseWheel(self: UIElement, e: MouseWheelEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.PreviewMouseWheel�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.MouseWheelEventArgs that contains the event data.
        """
        pass

    def OnPreviewQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnPreviewQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.PreviewQueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusDown(self, *args): #cannot find CLR method
        """
        OnPreviewStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusInRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusMove(self, *args): #cannot find CLR method
        """
        OnPreviewStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnPreviewStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnPreviewStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnPreviewStylusUp(self, *args): #cannot find CLR method
        """
        OnPreviewStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.PreviewStylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnPreviewTextInput(self, *args): #cannot find CLR method
        """
        OnPreviewTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.PreviewTextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class 
             handling for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchDown(self, *args): #cannot find CLR method
        """
        OnPreviewTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchDown routed event that occurs when a touch presses this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchMove(self, *args): #cannot find CLR method
        """
        OnPreviewTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPreviewTouchUp(self, *args): #cannot find CLR method
        """
        OnPreviewTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.PreviewTouchUp routed event that occurs when a touch is released inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnPropertyChanged(self, *args): #cannot find CLR method
        """
        OnPropertyChanged(self: FrameworkElement, e: DependencyPropertyChangedEventArgs)
            Invoked whenever the effective value of any dependency property on this System.Windows.FrameworkElement has been updated. The specific dependency property that changed is reported in the arguments 
             parameter. Overrides System.Windows.DependencyObject.OnPropertyChanged(System.Windows.DependencyPropertyChangedEventArgs).
        
        
            e: The event data that describes the property that changed, as well as old and new values.
        """
        pass

    def OnQueryContinueDrag(self, *args): #cannot find CLR method
        """
        OnQueryContinueDrag(self: UIElement, e: QueryContinueDragEventArgs)
            Invoked when an unhandled System.Windows.DragDrop.QueryContinueDrag�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.QueryContinueDragEventArgs that contains the event data.
        """
        pass

    def OnQueryCursor(self, *args): #cannot find CLR method
        """
        OnQueryCursor(self: UIElement, e: QueryCursorEventArgs)
            Invoked when an unhandled System.Windows.Input.Mouse.QueryCursor�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.QueryCursorEventArgs that contains the event data.
        """
        pass

    def OnRender(self, *args): #cannot find CLR method
        """
        OnRender(self: UIElement, drawingContext: DrawingContext)
            When overridden in a derived class, participates in rendering operations that are directed by the layout system. The rendering instructions for this element are not used directly when this method is 
             invoked, and are instead preserved for later asynchronous use by layout and drawing.
        
        
            drawingContext: The drawing instructions for a specific element. This context is provided to the layout system.
        """
        pass

    def OnRenderSizeChanged(self, *args): #cannot find CLR method
        """
        OnRenderSizeChanged(self: FrameworkElement, sizeInfo: SizeChangedInfo)
            Raises the System.Windows.FrameworkElement.SizeChanged event, using the specified information as part of the eventual event data.
        
            sizeInfo: Details of the old and new size involved in the change.
        """
        pass

    def OnStyleChanged(self, *args): #cannot find CLR method
        """
        OnStyleChanged(self: FrameworkElement, oldStyle: Style, newStyle: Style)
            Invoked when the style in use on this element changes, which will invalidate the layout.
        
            oldStyle: The old style.
            newStyle: The new style.
        """
        pass

    def OnStylusButtonDown(self, *args): #cannot find CLR method
        """
        OnStylusButtonDown(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusButtonUp(self, *args): #cannot find CLR method
        """
        OnStylusButtonUp(self: UIElement, e: StylusButtonEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusButtonUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusButtonEventArgs that contains the event data.
        """
        pass

    def OnStylusDown(self, *args): #cannot find CLR method
        """
        OnStylusDown(self: UIElement, e: StylusDownEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusDown�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusDownEventArgs that contains the event data.
        """
        pass

    def OnStylusEnter(self, *args): #cannot find CLR method
        """
        OnStylusEnter(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusEnter�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInAirMove(self, *args): #cannot find CLR method
        """
        OnStylusInAirMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInAirMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusInRange(self, *args): #cannot find CLR method
        """
        OnStylusInRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusInRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusLeave(self, *args): #cannot find CLR method
        """
        OnStylusLeave(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusLeave�attached event is raised by this element. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusMove(self, *args): #cannot find CLR method
        """
        OnStylusMove(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusMove�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusOutOfRange(self, *args): #cannot find CLR method
        """
        OnStylusOutOfRange(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusOutOfRange�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this 
             event.
        
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnStylusSystemGesture(self, *args): #cannot find CLR method
        """
        OnStylusSystemGesture(self: UIElement, e: StylusSystemGestureEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusSystemGesture�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for 
             this event.
        
        
            e: The System.Windows.Input.StylusSystemGestureEventArgs that contains the event data.
        """
        pass

    def OnStylusUp(self, *args): #cannot find CLR method
        """
        OnStylusUp(self: UIElement, e: StylusEventArgs)
            Invoked when an unhandled System.Windows.Input.Stylus.StylusUp�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling for this event.
        
            e: The System.Windows.Input.StylusEventArgs that contains the event data.
        """
        pass

    def OnTemplateChanged(self, *args): #cannot find CLR method
        """
        OnTemplateChanged(self: Control, oldTemplate: ControlTemplate, newTemplate: ControlTemplate)
            Called whenever the control's template changes.
        
            oldTemplate: The old template.
            newTemplate: The new template.
        """
        pass

    def OnTextInput(self, *args): #cannot find CLR method
        """
        OnTextInput(self: UIElement, e: TextCompositionEventArgs)
            Invoked when an unhandled System.Windows.Input.TextCompositionManager.TextInput�attached event reaches an element in its route that is derived from this class. Implement this method to add class handling 
             for this event.
        
        
            e: The System.Windows.Input.TextCompositionEventArgs that contains the event data.
        """
        pass

    def OnToolTipClosing(self, *args): #cannot find CLR method
        """
        OnToolTipClosing(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever an unhandled System.Windows.FrameworkElement.ToolTipClosing routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: Provides data about the event.
        """
        pass

    def OnToolTipOpening(self, *args): #cannot find CLR method
        """
        OnToolTipOpening(self: FrameworkElement, e: ToolTipEventArgs)
            Invoked whenever the System.Windows.FrameworkElement.ToolTipOpening routed event reaches this class in its route. Implement this method to add class handling for this event.
        
            e: Provides data about the event.
        """
        pass

    def OnTouchDown(self, *args): #cannot find CLR method
        """
        OnTouchDown(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchDown routed event that occurs when a touch presses inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchEnter(self, *args): #cannot find CLR method
        """
        OnTouchEnter(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchEnter routed event that occurs when a touch moves from outside to inside the bounds of this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchLeave(self, *args): #cannot find CLR method
        """
        OnTouchLeave(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchLeave routed event that occurs when a touch moves from inside to outside the bounds of this System.Windows.UIElement.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchMove(self, *args): #cannot find CLR method
        """
        OnTouchMove(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchMove routed event that occurs when a touch moves while inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnTouchUp(self, *args): #cannot find CLR method
        """
        OnTouchUp(self: UIElement, e: TouchEventArgs)
            Provides class handling for the System.Windows.UIElement.TouchUp routed event that occurs when a touch is released inside this element.
        
            e: A System.Windows.Input.TouchEventArgs that contains the event data.
        """
        pass

    def OnValueChanged(self, *args): #cannot find CLR method
        """
        OnValueChanged(self: ProgressBar, oldValue: float, newValue: float)
            Updates the current position of the System.Windows.Controls.ProgressBar when the System.Windows.Controls.Primitives.RangeBase.Value property changes.
        
            oldValue: Old value of the System.Windows.Controls.Primitives.RangeBase.Value property.
            newValue: New value of the System.Windows.Controls.Primitives.RangeBase.Value property.
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
        OnVisualParentChanged(self: FrameworkElement, oldParent: DependencyObject)
            Invoked when the parent of this element in the visual tree is changed. Overrides System.Windows.UIElement.OnVisualParentChanged(System.Windows.DependencyObject).
        
            oldParent: The old parent element. May be null to indicate that the element did not have a visual parent previously.
        """
        pass

    def ParentLayoutInvalidated(self, *args): #cannot find CLR method
        """
        ParentLayoutInvalidated(self: FrameworkElement, child: UIElement)
            Supports incremental layout implementations in specialized subclasses of System.Windows.FrameworkElement. System.Windows.FrameworkElement.ParentLayoutInvalidated(System.Windows.UIElement)  is invoked when 
             a child element has invalidated a property that is marked in metadata as affecting the parent's measure or arrange passes during layout.
        
        
            child: The child element reporting the change.
        """
        pass

    def RemoveLogicalChild(self, *args): #cannot find CLR method
        """
        RemoveLogicalChild(self: FrameworkElement, child: object)
            Removes the provided object from this element's logical tree. System.Windows.FrameworkElement updates the affected logical tree parent pointers to keep in sync with this deletion.
        
            child: The element to remove.
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

    def __str__(self, *args): #cannot find CLR method
        pass

    DefaultStyleKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the key to use to reference the style for this control, when theme styles are used or defined.

"""

    HandlesScrolling = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that indicates whether a control supports scrolling.

"""

    HasEffectiveKeyboardFocus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    InheritanceBehavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the scope limits for property value inheritance, resource key lookup, and RelativeSource FindAncestor lookup.

"""

    IsEnabledCore = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that becomes the return value of System.Windows.UIElement.IsEnabled in derived classes.

"""

    IsIndeterminate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the System.Windows.Controls.ProgressBar shows actual values or generic, continuous progress feedback.

Get: IsIndeterminate(self: ProgressBar) -> bool

Set: IsIndeterminate(self: ProgressBar) = value
"""

    LogicalChildren = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an enumerator for logical child elements of this element.

"""

    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the orientation of a System.Windows.Controls.ProgressBar: horizontal or vertical.

Get: Orientation(self: ProgressBar) -> Orientation

Set: Orientation(self: ProgressBar) = value
"""

    StylusPlugIns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a collection of all stylus plug-in (customization) objects associated with this element.

"""

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
    """Gets the number of visual child elements within this element.

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


    IsIndeterminateProperty = None
    OrientationProperty = None

