# encoding: utf-8
# module System.Windows.Input calls itself Input
# from System, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089, PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, PresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35, WindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes
from __init___parts.AccessKeyEventArgs import AccessKeyEventArgs
from __init___parts.AccessKeyManager import AccessKeyManager
from __init___parts.AccessKeyPressedEventArgs import AccessKeyPressedEventArgs
from __init___parts.AccessKeyPressedEventHandler import AccessKeyPressedEventHandler
from __init___parts.ApplicationCommands import ApplicationCommands
from __init___parts.CanExecuteChangedEventManager import CanExecuteChangedEventManager
from __init___parts.CanExecuteRoutedEventArgs import CanExecuteRoutedEventArgs
from __init___parts.CanExecuteRoutedEventHandler import CanExecuteRoutedEventHandler
from __init___parts.CaptureMode import CaptureMode
from __init___parts.CommandBinding import CommandBinding
from __init___parts.CommandBindingCollection import CommandBindingCollection
from __init___parts.CommandConverter import CommandConverter
from __init___parts.CommandManager import CommandManager
from __init___parts.ComponentCommands import ComponentCommands
from __init___parts.Cursor import Cursor
from __init___parts.CursorConverter import CursorConverter
from __init___parts.Cursors import Cursors
from __init___parts.CursorType import CursorType
from __init___parts.ExecutedRoutedEventArgs import ExecutedRoutedEventArgs
from __init___parts.ExecutedRoutedEventHandler import ExecutedRoutedEventHandler
from __init___parts.FocusManager import FocusManager
from __init___parts.FocusNavigationDirection import FocusNavigationDirection
from __init___parts.ICommand import ICommand
from __init___parts.ICommandSource import ICommandSource
from __init___parts.IInputLanguageSource import IInputLanguageSource
from __init___parts.IManipulator import IManipulator
from __init___parts.ImeConversionModeValues import ImeConversionModeValues
from __init___parts.ImeSentenceModeValues import ImeSentenceModeValues
from __init___parts.InertiaExpansionBehavior import InertiaExpansionBehavior
from __init___parts.InertiaRotationBehavior import InertiaRotationBehavior
from __init___parts.InertiaTranslationBehavior import InertiaTranslationBehavior
from __init___parts.InputBinding import InputBinding
from __init___parts.InputBindingCollection import InputBindingCollection
from __init___parts.InputDevice import InputDevice
from __init___parts.InputEventArgs import InputEventArgs
from __init___parts.InputEventHandler import InputEventHandler
from __init___parts.InputGesture import InputGesture
from __init___parts.InputGestureCollection import InputGestureCollection
from __init___parts.InputLanguageEventArgs import InputLanguageEventArgs
from __init___parts.InputLanguageChangedEventArgs import InputLanguageChangedEventArgs
from __init___parts.InputLanguageChangingEventArgs import InputLanguageChangingEventArgs
from __init___parts.InputLanguageEventHandler import InputLanguageEventHandler
from __init___parts.InputLanguageManager import InputLanguageManager
from __init___parts.InputManager import InputManager
from __init___parts.InputMethod import InputMethod
from __init___parts.InputMethodState import InputMethodState
from __init___parts.InputMethodStateChangedEventArgs import InputMethodStateChangedEventArgs
from __init___parts.InputMethodStateChangedEventHandler import InputMethodStateChangedEventHandler
from __init___parts.InputMode import InputMode
from __init___parts.InputScope import InputScope
from __init___parts.InputScopeConverter import InputScopeConverter
from __init___parts.InputScopeName import InputScopeName
from __init___parts.InputScopeNameConverter import InputScopeNameConverter
from __init___parts.InputScopeNameValue import InputScopeNameValue
from __init___parts.InputScopePhrase import InputScopePhrase
from __init___parts.InputType import InputType
from __init___parts.Key import Key
from __init___parts.KeyBinding import KeyBinding
from __init___parts.Keyboard import Keyboard
from __init___parts.KeyboardDevice import KeyboardDevice
from __init___parts.KeyboardEventArgs import KeyboardEventArgs
from __init___parts.KeyboardEventHandler import KeyboardEventHandler
from __init___parts.KeyboardFocusChangedEventArgs import KeyboardFocusChangedEventArgs
from __init___parts.KeyboardFocusChangedEventHandler import KeyboardFocusChangedEventHandler
from __init___parts.KeyboardInputProviderAcquireFocusEventArgs import KeyboardInputProviderAcquireFocusEventArgs
from __init___parts.KeyboardInputProviderAcquireFocusEventHandler import KeyboardInputProviderAcquireFocusEventHandler
from __init___parts.KeyboardNavigation import KeyboardNavigation
from __init___parts.KeyboardNavigationMode import KeyboardNavigationMode
from __init___parts.KeyConverter import KeyConverter
from __init___parts.KeyEventArgs import KeyEventArgs
from __init___parts.KeyEventHandler import KeyEventHandler
from __init___parts.KeyGesture import KeyGesture
from __init___parts.KeyGestureConverter import KeyGestureConverter
from __init___parts.KeyGestureValueSerializer import KeyGestureValueSerializer
from __init___parts.KeyInterop import KeyInterop
from __init___parts.KeyStates import KeyStates
from __init___parts.KeyValueSerializer import KeyValueSerializer
from __init___parts.Manipulation import Manipulation
from __init___parts.ManipulationBoundaryFeedbackEventArgs import ManipulationBoundaryFeedbackEventArgs
from __init___parts.ManipulationCompletedEventArgs import ManipulationCompletedEventArgs
from __init___parts.ManipulationDelta import ManipulationDelta
from __init___parts.ManipulationDeltaEventArgs import ManipulationDeltaEventArgs
from __init___parts.ManipulationInertiaStartingEventArgs import ManipulationInertiaStartingEventArgs
from __init___parts.ManipulationModes import ManipulationModes
from __init___parts.ManipulationPivot import ManipulationPivot
from __init___parts.ManipulationStartedEventArgs import ManipulationStartedEventArgs
from __init___parts.ManipulationStartingEventArgs import ManipulationStartingEventArgs
from __init___parts.ManipulationVelocities import ManipulationVelocities
from __init___parts.MediaCommands import MediaCommands
from __init___parts.ModifierKeys import ModifierKeys
from __init___parts.ModifierKeysConverter import ModifierKeysConverter
from __init___parts.ModifierKeysValueSerializer import ModifierKeysValueSerializer
from __init___parts.Mouse import Mouse
from __init___parts.MouseAction import MouseAction
from __init___parts.MouseActionConverter import MouseActionConverter
from __init___parts.MouseActionValueSerializer import MouseActionValueSerializer
from __init___parts.MouseBinding import MouseBinding
from __init___parts.MouseButton import MouseButton
from __init___parts.MouseEventArgs import MouseEventArgs
from __init___parts.MouseButtonEventArgs import MouseButtonEventArgs
from __init___parts.MouseButtonEventHandler import MouseButtonEventHandler
from __init___parts.MouseButtonState import MouseButtonState
from __init___parts.MouseDevice import MouseDevice
from __init___parts.MouseEventHandler import MouseEventHandler
from __init___parts.MouseGesture import MouseGesture
from __init___parts.MouseGestureConverter import MouseGestureConverter
from __init___parts.MouseGestureValueSerializer import MouseGestureValueSerializer
from __init___parts.MouseWheelEventArgs import MouseWheelEventArgs
from __init___parts.MouseWheelEventHandler import MouseWheelEventHandler
from __init___parts.NavigationCommands import NavigationCommands
from __init___parts.NotifyInputEventArgs import NotifyInputEventArgs
from __init___parts.NotifyInputEventHandler import NotifyInputEventHandler
from __init___parts.ProcessInputEventArgs import ProcessInputEventArgs
from __init___parts.PreProcessInputEventArgs import PreProcessInputEventArgs
from __init___parts.PreProcessInputEventHandler import PreProcessInputEventHandler
from __init___parts.ProcessInputEventHandler import ProcessInputEventHandler
from __init___parts.QueryCursorEventArgs import QueryCursorEventArgs
from __init___parts.QueryCursorEventHandler import QueryCursorEventHandler
from __init___parts.RestoreFocusMode import RestoreFocusMode
from __init___parts.RoutedCommand import RoutedCommand
from __init___parts.RoutedUICommand import RoutedUICommand
from __init___parts.SpeechMode import SpeechMode
from __init___parts.StagingAreaInputItem import StagingAreaInputItem
from __init___parts.Stylus import Stylus
from __init___parts.StylusButton import StylusButton
from __init___parts.StylusButtonCollection import StylusButtonCollection
from __init___parts.StylusEventArgs import StylusEventArgs
from __init___parts.StylusButtonEventArgs import StylusButtonEventArgs
from __init___parts.StylusButtonEventHandler import StylusButtonEventHandler
from __init___parts.StylusButtonState import StylusButtonState
from __init___parts.StylusDevice import StylusDevice
from __init___parts.StylusDeviceCollection import StylusDeviceCollection
from __init___parts.StylusDownEventArgs import StylusDownEventArgs
from __init___parts.StylusDownEventHandler import StylusDownEventHandler
from __init___parts.StylusEventHandler import StylusEventHandler
from __init___parts.StylusPoint import StylusPoint
from __init___parts.StylusPointCollection import StylusPointCollection
from __init___parts.StylusPointDescription import StylusPointDescription
from __init___parts.StylusPointProperties import StylusPointProperties
from __init___parts.StylusPointProperty import StylusPointProperty
from __init___parts.StylusPointPropertyInfo import StylusPointPropertyInfo
from __init___parts.StylusPointPropertyUnit import StylusPointPropertyUnit
from __init___parts.StylusSystemGestureEventArgs import StylusSystemGestureEventArgs
from __init___parts.StylusSystemGestureEventHandler import StylusSystemGestureEventHandler
from __init___parts.SystemGesture import SystemGesture
from __init___parts.Tablet import Tablet
from __init___parts.TabletDevice import TabletDevice
from __init___parts.TabletDeviceCollection import TabletDeviceCollection
from __init___parts.TabletDeviceType import TabletDeviceType
from __init___parts.TabletHardwareCapabilities import TabletHardwareCapabilities
from __init___parts.TextComposition import TextComposition
from __init___parts.TextCompositionAutoComplete import TextCompositionAutoComplete
from __init___parts.TextCompositionEventArgs import TextCompositionEventArgs
from __init___parts.TextCompositionEventHandler import TextCompositionEventHandler
from __init___parts.TextCompositionManager import TextCompositionManager
from __init___parts.Touch import Touch
from __init___parts.TouchAction import TouchAction
from __init___parts.TouchDevice import TouchDevice
from __init___parts.TouchEventArgs import TouchEventArgs
from __init___parts.TouchFrameEventArgs import TouchFrameEventArgs
from __init___parts.TouchFrameEventHandler import TouchFrameEventHandler
from __init___parts.TouchPoint import TouchPoint
from __init___parts.TouchPointCollection import TouchPointCollection
from __init___parts.TraversalRequest import TraversalRequest
