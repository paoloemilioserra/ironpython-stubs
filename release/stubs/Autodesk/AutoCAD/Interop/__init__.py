# encoding: utf-8
# module Autodesk.AutoCAD.Interop calls itself Interop
# from Autodesk.AutoCAD.Interop, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null, Autodesk.AutoCAD.Interop.Common, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class IAcadApplication:
    # no doc
    def Eval(self, Expression):
        """ Eval(self: IAcadApplication, Expression: str) """
        pass

    def GetAcadState(self):
        """ GetAcadState(self: IAcadApplication) -> AcadState """
        pass

    def GetInterfaceObject(self, ProgID):
        """ GetInterfaceObject(self: IAcadApplication, ProgID: str) -> object """
        pass

    def ListArx(self):
        """ ListArx(self: IAcadApplication) -> object """
        pass

    def LoadArx(self, Name):
        """ LoadArx(self: IAcadApplication, Name: str) """
        pass

    def LoadDVB(self, Name):
        """ LoadDVB(self: IAcadApplication, Name: str) """
        pass

    def Quit(self):
        """ Quit(self: IAcadApplication) """
        pass

    def RunMacro(self, MacroPath):
        """ RunMacro(self: IAcadApplication, MacroPath: str) """
        pass

    def UnloadArx(self, Name):
        """ UnloadArx(self: IAcadApplication, Name: str) """
        pass

    def UnloadDVB(self, Name):
        """ UnloadDVB(self: IAcadApplication, Name: str) """
        pass

    def Update(self):
        """ Update(self: IAcadApplication) """
        pass

    def Zoom(self, Type, vParams):
        """ Zoom(self: IAcadApplication, Type: int, vParams: object) -> object """
        pass

    def ZoomAll(self):
        """ ZoomAll(self: IAcadApplication) """
        pass

    def ZoomCenter(self, Center, Magnify):
        """ ZoomCenter(self: IAcadApplication, Center: object, Magnify: float) """
        pass

    def ZoomExtents(self):
        """ ZoomExtents(self: IAcadApplication) """
        pass

    def ZoomPickWindow(self):
        """ ZoomPickWindow(self: IAcadApplication) """
        pass

    def ZoomPrevious(self):
        """ ZoomPrevious(self: IAcadApplication) """
        pass

    def ZoomScaled(self, Scale, ScaleType):
        """ ZoomScaled(self: IAcadApplication, Scale: float, ScaleType: AcZoomScaleType) """
        pass

    def ZoomWindow(self, LowerLeft, UpperRight):
        """ ZoomWindow(self: IAcadApplication, LowerLeft: object, UpperRight: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActiveDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveDocument(self: IAcadApplication) -> AcadDocument

Set: ActiveDocument(self: IAcadApplication) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadApplication) -> IAcadApplication

"""

    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Caption(self: IAcadApplication) -> str

"""

    Documents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Documents(self: IAcadApplication) -> AcadDocuments

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: IAcadApplication) -> str

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: IAcadApplication) -> int

Set: Height(self: IAcadApplication) = value
"""

    HWND = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HWND(self: IAcadApplication) -> Int64

"""

    LocaleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocaleId(self: IAcadApplication) -> int

"""

    MenuBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuBar(self: IAcadApplication) -> AcadMenuBar

"""

    MenuGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuGroups(self: IAcadApplication) -> AcadMenuGroups

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAcadApplication) -> str

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: IAcadApplication) -> str

"""

    Preferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preferences(self: IAcadApplication) -> AcadPreferences

"""

    VBE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VBE(self: IAcadApplication) -> object

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: IAcadApplication) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: IAcadApplication) -> bool

Set: Visible(self: IAcadApplication) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: IAcadApplication) -> int

Set: Width(self: IAcadApplication) = value
"""

    WindowLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowLeft(self: IAcadApplication) -> int

Set: WindowLeft(self: IAcadApplication) = value
"""

    WindowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowState(self: IAcadApplication) -> AcWindowState

Set: WindowState(self: IAcadApplication) = value
"""

    WindowTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowTop(self: IAcadApplication) -> int

Set: WindowTop(self: IAcadApplication) = value
"""



class _DAcadApplicationEvents_Event:
    # no doc
    def add_AppActivate(self, A_1):
        """ add_AppActivate(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_AppActivateEventHandler) """
        pass

    def add_AppDeactivate(self, A_1):
        """ add_AppDeactivate(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_AppDeactivateEventHandler) """
        pass

    def add_ARXLoaded(self, A_1):
        """ add_ARXLoaded(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_ARXLoadedEventHandler) """
        pass

    def add_ARXUnloaded(self, A_1):
        """ add_ARXUnloaded(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_ARXUnloadedEventHandler) """
        pass

    def add_BeginCommand(self, A_1):
        """ add_BeginCommand(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginCommandEventHandler) """
        pass

    def add_BeginFileDrop(self, A_1):
        """ add_BeginFileDrop(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginFileDropEventHandler) """
        pass

    def add_BeginLisp(self, A_1):
        """ add_BeginLisp(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginLispEventHandler) """
        pass

    def add_BeginModal(self, A_1):
        """ add_BeginModal(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginModalEventHandler) """
        pass

    def add_BeginOpen(self, A_1):
        """ add_BeginOpen(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginOpenEventHandler) """
        pass

    def add_BeginPlot(self, A_1):
        """ add_BeginPlot(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginPlotEventHandler) """
        pass

    def add_BeginQuit(self, A_1):
        """ add_BeginQuit(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginQuitEventHandler) """
        pass

    def add_BeginSave(self, A_1):
        """ add_BeginSave(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginSaveEventHandler) """
        pass

    def add_EndCommand(self, A_1):
        """ add_EndCommand(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndCommandEventHandler) """
        pass

    def add_EndLisp(self, A_1):
        """ add_EndLisp(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndLispEventHandler) """
        pass

    def add_EndModal(self, A_1):
        """ add_EndModal(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndModalEventHandler) """
        pass

    def add_EndOpen(self, A_1):
        """ add_EndOpen(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndOpenEventHandler) """
        pass

    def add_EndPlot(self, A_1):
        """ add_EndPlot(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndPlotEventHandler) """
        pass

    def add_EndSave(self, A_1):
        """ add_EndSave(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndSaveEventHandler) """
        pass

    def add_LispCancelled(self, A_1):
        """ add_LispCancelled(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_LispCancelledEventHandler) """
        pass

    def add_NewDrawing(self, A_1):
        """ add_NewDrawing(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_NewDrawingEventHandler) """
        pass

    def add_SysVarChanged(self, A_1):
        """ add_SysVarChanged(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_SysVarChangedEventHandler) """
        pass

    def add_WindowChanged(self, A_1):
        """ add_WindowChanged(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_WindowChangedEventHandler) """
        pass

    def add_WindowMovedOrResized(self, A_1):
        """ add_WindowMovedOrResized(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_WindowMovedOrResizedEventHandler) """
        pass

    def remove_AppActivate(self, A_1):
        """ remove_AppActivate(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_AppActivateEventHandler) """
        pass

    def remove_AppDeactivate(self, A_1):
        """ remove_AppDeactivate(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_AppDeactivateEventHandler) """
        pass

    def remove_ARXLoaded(self, A_1):
        """ remove_ARXLoaded(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_ARXLoadedEventHandler) """
        pass

    def remove_ARXUnloaded(self, A_1):
        """ remove_ARXUnloaded(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_ARXUnloadedEventHandler) """
        pass

    def remove_BeginCommand(self, A_1):
        """ remove_BeginCommand(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginCommandEventHandler) """
        pass

    def remove_BeginFileDrop(self, A_1):
        """ remove_BeginFileDrop(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginFileDropEventHandler) """
        pass

    def remove_BeginLisp(self, A_1):
        """ remove_BeginLisp(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginLispEventHandler) """
        pass

    def remove_BeginModal(self, A_1):
        """ remove_BeginModal(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginModalEventHandler) """
        pass

    def remove_BeginOpen(self, A_1):
        """ remove_BeginOpen(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginOpenEventHandler) """
        pass

    def remove_BeginPlot(self, A_1):
        """ remove_BeginPlot(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginPlotEventHandler) """
        pass

    def remove_BeginQuit(self, A_1):
        """ remove_BeginQuit(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginQuitEventHandler) """
        pass

    def remove_BeginSave(self, A_1):
        """ remove_BeginSave(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_BeginSaveEventHandler) """
        pass

    def remove_EndCommand(self, A_1):
        """ remove_EndCommand(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndCommandEventHandler) """
        pass

    def remove_EndLisp(self, A_1):
        """ remove_EndLisp(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndLispEventHandler) """
        pass

    def remove_EndModal(self, A_1):
        """ remove_EndModal(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndModalEventHandler) """
        pass

    def remove_EndOpen(self, A_1):
        """ remove_EndOpen(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndOpenEventHandler) """
        pass

    def remove_EndPlot(self, A_1):
        """ remove_EndPlot(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndPlotEventHandler) """
        pass

    def remove_EndSave(self, A_1):
        """ remove_EndSave(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_EndSaveEventHandler) """
        pass

    def remove_LispCancelled(self, A_1):
        """ remove_LispCancelled(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_LispCancelledEventHandler) """
        pass

    def remove_NewDrawing(self, A_1):
        """ remove_NewDrawing(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_NewDrawingEventHandler) """
        pass

    def remove_SysVarChanged(self, A_1):
        """ remove_SysVarChanged(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_SysVarChangedEventHandler) """
        pass

    def remove_WindowChanged(self, A_1):
        """ remove_WindowChanged(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_WindowChangedEventHandler) """
        pass

    def remove_WindowMovedOrResized(self, A_1):
        """ remove_WindowMovedOrResized(self: _DAcadApplicationEvents_Event, A_1: _DAcadApplicationEvents_WindowMovedOrResizedEventHandler) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AppActivate = None
    AppDeactivate = None
    ARXLoaded = None
    ARXUnloaded = None
    BeginCommand = None
    BeginFileDrop = None
    BeginLisp = None
    BeginModal = None
    BeginOpen = None
    BeginPlot = None
    BeginQuit = None
    BeginSave = None
    EndCommand = None
    EndLisp = None
    EndModal = None
    EndOpen = None
    EndPlot = None
    EndSave = None
    LispCancelled = None
    NewDrawing = None
    SysVarChanged = None
    WindowChanged = None
    WindowMovedOrResized = None


class AcadApplication(IAcadApplication, _DAcadApplicationEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadApplicationClass(__ComObject):
    """ AcadApplicationClass() """
    def add_AppActivate(self, A_1):
        """ add_AppActivate(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_AppActivateEventHandler) """
        pass

    def add_AppDeactivate(self, A_1):
        """ add_AppDeactivate(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_AppDeactivateEventHandler) """
        pass

    def add_ARXLoaded(self, A_1):
        """ add_ARXLoaded(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_ARXLoadedEventHandler) """
        pass

    def add_ARXUnloaded(self, A_1):
        """ add_ARXUnloaded(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_ARXUnloadedEventHandler) """
        pass

    def add_BeginCommand(self, A_1):
        """ add_BeginCommand(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginCommandEventHandler) """
        pass

    def add_BeginFileDrop(self, A_1):
        """ add_BeginFileDrop(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginFileDropEventHandler) """
        pass

    def add_BeginLisp(self, A_1):
        """ add_BeginLisp(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginLispEventHandler) """
        pass

    def add_BeginModal(self, A_1):
        """ add_BeginModal(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginModalEventHandler) """
        pass

    def add_BeginOpen(self, A_1):
        """ add_BeginOpen(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginOpenEventHandler) """
        pass

    def add_BeginPlot(self, A_1):
        """ add_BeginPlot(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginPlotEventHandler) """
        pass

    def add_BeginQuit(self, A_1):
        """ add_BeginQuit(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginQuitEventHandler) """
        pass

    def add_BeginSave(self, A_1):
        """ add_BeginSave(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginSaveEventHandler) """
        pass

    def add_EndCommand(self, A_1):
        """ add_EndCommand(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndCommandEventHandler) """
        pass

    def add_EndLisp(self, A_1):
        """ add_EndLisp(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndLispEventHandler) """
        pass

    def add_EndModal(self, A_1):
        """ add_EndModal(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndModalEventHandler) """
        pass

    def add_EndOpen(self, A_1):
        """ add_EndOpen(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndOpenEventHandler) """
        pass

    def add_EndPlot(self, A_1):
        """ add_EndPlot(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndPlotEventHandler) """
        pass

    def add_EndSave(self, A_1):
        """ add_EndSave(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndSaveEventHandler) """
        pass

    def add_LispCancelled(self, A_1):
        """ add_LispCancelled(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_LispCancelledEventHandler) """
        pass

    def add_NewDrawing(self, A_1):
        """ add_NewDrawing(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_NewDrawingEventHandler) """
        pass

    def add_SysVarChanged(self, A_1):
        """ add_SysVarChanged(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_SysVarChangedEventHandler) """
        pass

    def add_WindowChanged(self, A_1):
        """ add_WindowChanged(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_WindowChangedEventHandler) """
        pass

    def add_WindowMovedOrResized(self, A_1):
        """ add_WindowMovedOrResized(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_WindowMovedOrResizedEventHandler) """
        pass

    def Eval(self, Expression):
        """ Eval(self: AcadApplicationClass, Expression: str) """
        pass

    def GetAcadState(self):
        """ GetAcadState(self: AcadApplicationClass) -> AcadState """
        pass

    def GetInterfaceObject(self, ProgID):
        """ GetInterfaceObject(self: AcadApplicationClass, ProgID: str) -> object """
        pass

    def ListArx(self):
        """ ListArx(self: AcadApplicationClass) -> object """
        pass

    def LoadArx(self, Name):
        """ LoadArx(self: AcadApplicationClass, Name: str) """
        pass

    def LoadDVB(self, Name):
        """ LoadDVB(self: AcadApplicationClass, Name: str) """
        pass

    def Quit(self):
        """ Quit(self: AcadApplicationClass) """
        pass

    def remove_AppActivate(self, A_1):
        """ remove_AppActivate(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_AppActivateEventHandler) """
        pass

    def remove_AppDeactivate(self, A_1):
        """ remove_AppDeactivate(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_AppDeactivateEventHandler) """
        pass

    def remove_ARXLoaded(self, A_1):
        """ remove_ARXLoaded(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_ARXLoadedEventHandler) """
        pass

    def remove_ARXUnloaded(self, A_1):
        """ remove_ARXUnloaded(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_ARXUnloadedEventHandler) """
        pass

    def remove_BeginCommand(self, A_1):
        """ remove_BeginCommand(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginCommandEventHandler) """
        pass

    def remove_BeginFileDrop(self, A_1):
        """ remove_BeginFileDrop(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginFileDropEventHandler) """
        pass

    def remove_BeginLisp(self, A_1):
        """ remove_BeginLisp(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginLispEventHandler) """
        pass

    def remove_BeginModal(self, A_1):
        """ remove_BeginModal(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginModalEventHandler) """
        pass

    def remove_BeginOpen(self, A_1):
        """ remove_BeginOpen(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginOpenEventHandler) """
        pass

    def remove_BeginPlot(self, A_1):
        """ remove_BeginPlot(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginPlotEventHandler) """
        pass

    def remove_BeginQuit(self, A_1):
        """ remove_BeginQuit(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginQuitEventHandler) """
        pass

    def remove_BeginSave(self, A_1):
        """ remove_BeginSave(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_BeginSaveEventHandler) """
        pass

    def remove_EndCommand(self, A_1):
        """ remove_EndCommand(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndCommandEventHandler) """
        pass

    def remove_EndLisp(self, A_1):
        """ remove_EndLisp(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndLispEventHandler) """
        pass

    def remove_EndModal(self, A_1):
        """ remove_EndModal(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndModalEventHandler) """
        pass

    def remove_EndOpen(self, A_1):
        """ remove_EndOpen(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndOpenEventHandler) """
        pass

    def remove_EndPlot(self, A_1):
        """ remove_EndPlot(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndPlotEventHandler) """
        pass

    def remove_EndSave(self, A_1):
        """ remove_EndSave(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_EndSaveEventHandler) """
        pass

    def remove_LispCancelled(self, A_1):
        """ remove_LispCancelled(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_LispCancelledEventHandler) """
        pass

    def remove_NewDrawing(self, A_1):
        """ remove_NewDrawing(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_NewDrawingEventHandler) """
        pass

    def remove_SysVarChanged(self, A_1):
        """ remove_SysVarChanged(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_SysVarChangedEventHandler) """
        pass

    def remove_WindowChanged(self, A_1):
        """ remove_WindowChanged(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_WindowChangedEventHandler) """
        pass

    def remove_WindowMovedOrResized(self, A_1):
        """ remove_WindowMovedOrResized(self: AcadApplicationClass, A_1: _DAcadApplicationEvents_WindowMovedOrResizedEventHandler) """
        pass

    def RunMacro(self, MacroPath):
        """ RunMacro(self: AcadApplicationClass, MacroPath: str) """
        pass

    def UnloadArx(self, Name):
        """ UnloadArx(self: AcadApplicationClass, Name: str) """
        pass

    def UnloadDVB(self, Name):
        """ UnloadDVB(self: AcadApplicationClass, Name: str) """
        pass

    def Update(self):
        """ Update(self: AcadApplicationClass) """
        pass

    def Zoom(self, Type, vParams):
        """ Zoom(self: AcadApplicationClass, Type: int, vParams: object) -> object """
        pass

    def ZoomAll(self):
        """ ZoomAll(self: AcadApplicationClass) """
        pass

    def ZoomCenter(self, Center, Magnify):
        """ ZoomCenter(self: AcadApplicationClass, Center: object, Magnify: float) """
        pass

    def ZoomExtents(self):
        """ ZoomExtents(self: AcadApplicationClass) """
        pass

    def ZoomPickWindow(self):
        """ ZoomPickWindow(self: AcadApplicationClass) """
        pass

    def ZoomPrevious(self):
        """ ZoomPrevious(self: AcadApplicationClass) """
        pass

    def ZoomScaled(self, Scale, ScaleType):
        """ ZoomScaled(self: AcadApplicationClass, Scale: float, ScaleType: AcZoomScaleType) """
        pass

    def ZoomWindow(self, LowerLeft, UpperRight):
        """ ZoomWindow(self: AcadApplicationClass, LowerLeft: object, UpperRight: object) """
        pass

    ActiveDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveDocument(self: AcadApplicationClass) -> AcadDocument

Set: ActiveDocument(self: AcadApplicationClass) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadApplicationClass) -> IAcadApplication

"""

    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Caption(self: AcadApplicationClass) -> str

"""

    Documents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Documents(self: AcadApplicationClass) -> AcadDocuments

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: AcadApplicationClass) -> str

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: AcadApplicationClass) -> int

Set: Height(self: AcadApplicationClass) = value
"""

    HWND = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HWND(self: AcadApplicationClass) -> Int64

"""

    LocaleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocaleId(self: AcadApplicationClass) -> int

"""

    MenuBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuBar(self: AcadApplicationClass) -> AcadMenuBar

"""

    MenuGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuGroups(self: AcadApplicationClass) -> AcadMenuGroups

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadApplicationClass) -> str

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: AcadApplicationClass) -> str

"""

    Preferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preferences(self: AcadApplicationClass) -> AcadPreferences

"""

    VBE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VBE(self: AcadApplicationClass) -> object

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: AcadApplicationClass) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: AcadApplicationClass) -> bool

Set: Visible(self: AcadApplicationClass) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: AcadApplicationClass) -> int

Set: Width(self: AcadApplicationClass) = value
"""

    WindowLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowLeft(self: AcadApplicationClass) -> int

Set: WindowLeft(self: AcadApplicationClass) = value
"""

    WindowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowState(self: AcadApplicationClass) -> AcWindowState

Set: WindowState(self: AcadApplicationClass) = value
"""

    WindowTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowTop(self: AcadApplicationClass) -> int

Set: WindowTop(self: AcadApplicationClass) = value
"""


    AppActivate = None
    AppDeactivate = None
    ARXLoaded = None
    ARXUnloaded = None
    BeginCommand = None
    BeginFileDrop = None
    BeginLisp = None
    BeginModal = None
    BeginOpen = None
    BeginPlot = None
    BeginQuit = None
    BeginSave = None
    EndCommand = None
    EndLisp = None
    EndModal = None
    EndOpen = None
    EndPlot = None
    EndSave = None
    LispCancelled = None
    NewDrawing = None
    SysVarChanged = None
    WindowChanged = None
    WindowMovedOrResized = None


class AcadApplicationMinorVersion1(IAcadApplication, _DAcadApplicationEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadApplicationMinorVersion1Class(__ComObject):
    """ AcadApplicationMinorVersion1Class() """
    def add_AppActivate(self, A_1):
        """ add_AppActivate(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_AppActivateEventHandler) """
        pass

    def add_AppDeactivate(self, A_1):
        """ add_AppDeactivate(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_AppDeactivateEventHandler) """
        pass

    def add_ARXLoaded(self, A_1):
        """ add_ARXLoaded(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_ARXLoadedEventHandler) """
        pass

    def add_ARXUnloaded(self, A_1):
        """ add_ARXUnloaded(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_ARXUnloadedEventHandler) """
        pass

    def add_BeginCommand(self, A_1):
        """ add_BeginCommand(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginCommandEventHandler) """
        pass

    def add_BeginFileDrop(self, A_1):
        """ add_BeginFileDrop(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginFileDropEventHandler) """
        pass

    def add_BeginLisp(self, A_1):
        """ add_BeginLisp(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginLispEventHandler) """
        pass

    def add_BeginModal(self, A_1):
        """ add_BeginModal(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginModalEventHandler) """
        pass

    def add_BeginOpen(self, A_1):
        """ add_BeginOpen(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginOpenEventHandler) """
        pass

    def add_BeginPlot(self, A_1):
        """ add_BeginPlot(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginPlotEventHandler) """
        pass

    def add_BeginQuit(self, A_1):
        """ add_BeginQuit(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginQuitEventHandler) """
        pass

    def add_BeginSave(self, A_1):
        """ add_BeginSave(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginSaveEventHandler) """
        pass

    def add_EndCommand(self, A_1):
        """ add_EndCommand(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndCommandEventHandler) """
        pass

    def add_EndLisp(self, A_1):
        """ add_EndLisp(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndLispEventHandler) """
        pass

    def add_EndModal(self, A_1):
        """ add_EndModal(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndModalEventHandler) """
        pass

    def add_EndOpen(self, A_1):
        """ add_EndOpen(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndOpenEventHandler) """
        pass

    def add_EndPlot(self, A_1):
        """ add_EndPlot(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndPlotEventHandler) """
        pass

    def add_EndSave(self, A_1):
        """ add_EndSave(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndSaveEventHandler) """
        pass

    def add_LispCancelled(self, A_1):
        """ add_LispCancelled(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_LispCancelledEventHandler) """
        pass

    def add_NewDrawing(self, A_1):
        """ add_NewDrawing(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_NewDrawingEventHandler) """
        pass

    def add_SysVarChanged(self, A_1):
        """ add_SysVarChanged(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_SysVarChangedEventHandler) """
        pass

    def add_WindowChanged(self, A_1):
        """ add_WindowChanged(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_WindowChangedEventHandler) """
        pass

    def add_WindowMovedOrResized(self, A_1):
        """ add_WindowMovedOrResized(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_WindowMovedOrResizedEventHandler) """
        pass

    def Eval(self, Expression):
        """ Eval(self: AcadApplicationMinorVersion1Class, Expression: str) """
        pass

    def GetAcadState(self):
        """ GetAcadState(self: AcadApplicationMinorVersion1Class) -> AcadState """
        pass

    def GetInterfaceObject(self, ProgID):
        """ GetInterfaceObject(self: AcadApplicationMinorVersion1Class, ProgID: str) -> object """
        pass

    def ListArx(self):
        """ ListArx(self: AcadApplicationMinorVersion1Class) -> object """
        pass

    def LoadArx(self, Name):
        """ LoadArx(self: AcadApplicationMinorVersion1Class, Name: str) """
        pass

    def LoadDVB(self, Name):
        """ LoadDVB(self: AcadApplicationMinorVersion1Class, Name: str) """
        pass

    def Quit(self):
        """ Quit(self: AcadApplicationMinorVersion1Class) """
        pass

    def remove_AppActivate(self, A_1):
        """ remove_AppActivate(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_AppActivateEventHandler) """
        pass

    def remove_AppDeactivate(self, A_1):
        """ remove_AppDeactivate(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_AppDeactivateEventHandler) """
        pass

    def remove_ARXLoaded(self, A_1):
        """ remove_ARXLoaded(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_ARXLoadedEventHandler) """
        pass

    def remove_ARXUnloaded(self, A_1):
        """ remove_ARXUnloaded(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_ARXUnloadedEventHandler) """
        pass

    def remove_BeginCommand(self, A_1):
        """ remove_BeginCommand(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginCommandEventHandler) """
        pass

    def remove_BeginFileDrop(self, A_1):
        """ remove_BeginFileDrop(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginFileDropEventHandler) """
        pass

    def remove_BeginLisp(self, A_1):
        """ remove_BeginLisp(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginLispEventHandler) """
        pass

    def remove_BeginModal(self, A_1):
        """ remove_BeginModal(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginModalEventHandler) """
        pass

    def remove_BeginOpen(self, A_1):
        """ remove_BeginOpen(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginOpenEventHandler) """
        pass

    def remove_BeginPlot(self, A_1):
        """ remove_BeginPlot(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginPlotEventHandler) """
        pass

    def remove_BeginQuit(self, A_1):
        """ remove_BeginQuit(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginQuitEventHandler) """
        pass

    def remove_BeginSave(self, A_1):
        """ remove_BeginSave(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_BeginSaveEventHandler) """
        pass

    def remove_EndCommand(self, A_1):
        """ remove_EndCommand(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndCommandEventHandler) """
        pass

    def remove_EndLisp(self, A_1):
        """ remove_EndLisp(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndLispEventHandler) """
        pass

    def remove_EndModal(self, A_1):
        """ remove_EndModal(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndModalEventHandler) """
        pass

    def remove_EndOpen(self, A_1):
        """ remove_EndOpen(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndOpenEventHandler) """
        pass

    def remove_EndPlot(self, A_1):
        """ remove_EndPlot(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndPlotEventHandler) """
        pass

    def remove_EndSave(self, A_1):
        """ remove_EndSave(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_EndSaveEventHandler) """
        pass

    def remove_LispCancelled(self, A_1):
        """ remove_LispCancelled(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_LispCancelledEventHandler) """
        pass

    def remove_NewDrawing(self, A_1):
        """ remove_NewDrawing(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_NewDrawingEventHandler) """
        pass

    def remove_SysVarChanged(self, A_1):
        """ remove_SysVarChanged(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_SysVarChangedEventHandler) """
        pass

    def remove_WindowChanged(self, A_1):
        """ remove_WindowChanged(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_WindowChangedEventHandler) """
        pass

    def remove_WindowMovedOrResized(self, A_1):
        """ remove_WindowMovedOrResized(self: AcadApplicationMinorVersion1Class, A_1: _DAcadApplicationEvents_WindowMovedOrResizedEventHandler) """
        pass

    def RunMacro(self, MacroPath):
        """ RunMacro(self: AcadApplicationMinorVersion1Class, MacroPath: str) """
        pass

    def UnloadArx(self, Name):
        """ UnloadArx(self: AcadApplicationMinorVersion1Class, Name: str) """
        pass

    def UnloadDVB(self, Name):
        """ UnloadDVB(self: AcadApplicationMinorVersion1Class, Name: str) """
        pass

    def Update(self):
        """ Update(self: AcadApplicationMinorVersion1Class) """
        pass

    def Zoom(self, Type, vParams):
        """ Zoom(self: AcadApplicationMinorVersion1Class, Type: int, vParams: object) -> object """
        pass

    def ZoomAll(self):
        """ ZoomAll(self: AcadApplicationMinorVersion1Class) """
        pass

    def ZoomCenter(self, Center, Magnify):
        """ ZoomCenter(self: AcadApplicationMinorVersion1Class, Center: object, Magnify: float) """
        pass

    def ZoomExtents(self):
        """ ZoomExtents(self: AcadApplicationMinorVersion1Class) """
        pass

    def ZoomPickWindow(self):
        """ ZoomPickWindow(self: AcadApplicationMinorVersion1Class) """
        pass

    def ZoomPrevious(self):
        """ ZoomPrevious(self: AcadApplicationMinorVersion1Class) """
        pass

    def ZoomScaled(self, Scale, ScaleType):
        """ ZoomScaled(self: AcadApplicationMinorVersion1Class, Scale: float, ScaleType: AcZoomScaleType) """
        pass

    def ZoomWindow(self, LowerLeft, UpperRight):
        """ ZoomWindow(self: AcadApplicationMinorVersion1Class, LowerLeft: object, UpperRight: object) """
        pass

    ActiveDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveDocument(self: AcadApplicationMinorVersion1Class) -> AcadDocument

Set: ActiveDocument(self: AcadApplicationMinorVersion1Class) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadApplicationMinorVersion1Class) -> IAcadApplication

"""

    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Caption(self: AcadApplicationMinorVersion1Class) -> str

"""

    Documents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Documents(self: AcadApplicationMinorVersion1Class) -> AcadDocuments

"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: AcadApplicationMinorVersion1Class) -> str

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: AcadApplicationMinorVersion1Class) -> int

Set: Height(self: AcadApplicationMinorVersion1Class) = value
"""

    HWND = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HWND(self: AcadApplicationMinorVersion1Class) -> Int64

"""

    LocaleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocaleId(self: AcadApplicationMinorVersion1Class) -> int

"""

    MenuBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuBar(self: AcadApplicationMinorVersion1Class) -> AcadMenuBar

"""

    MenuGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuGroups(self: AcadApplicationMinorVersion1Class) -> AcadMenuGroups

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadApplicationMinorVersion1Class) -> str

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: AcadApplicationMinorVersion1Class) -> str

"""

    Preferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preferences(self: AcadApplicationMinorVersion1Class) -> AcadPreferences

"""

    VBE = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VBE(self: AcadApplicationMinorVersion1Class) -> object

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Version(self: AcadApplicationMinorVersion1Class) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: AcadApplicationMinorVersion1Class) -> bool

Set: Visible(self: AcadApplicationMinorVersion1Class) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: AcadApplicationMinorVersion1Class) -> int

Set: Width(self: AcadApplicationMinorVersion1Class) = value
"""

    WindowLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowLeft(self: AcadApplicationMinorVersion1Class) -> int

Set: WindowLeft(self: AcadApplicationMinorVersion1Class) = value
"""

    WindowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowState(self: AcadApplicationMinorVersion1Class) -> AcWindowState

Set: WindowState(self: AcadApplicationMinorVersion1Class) = value
"""

    WindowTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowTop(self: AcadApplicationMinorVersion1Class) -> int

Set: WindowTop(self: AcadApplicationMinorVersion1Class) = value
"""


    AppActivate = None
    AppDeactivate = None
    ARXLoaded = None
    ARXUnloaded = None
    BeginCommand = None
    BeginFileDrop = None
    BeginLisp = None
    BeginModal = None
    BeginOpen = None
    BeginPlot = None
    BeginQuit = None
    BeginSave = None
    EndCommand = None
    EndLisp = None
    EndModal = None
    EndOpen = None
    EndPlot = None
    EndSave = None
    LispCancelled = None
    NewDrawing = None
    SysVarChanged = None
    WindowChanged = None
    WindowMovedOrResized = None


class IAcadDocument(IAcadDatabase):
    # no doc
    def Activate(self):
        """ Activate(self: IAcadDocument) """
        pass

    def AuditInfo(self, FixErr):
        """ AuditInfo(self: IAcadDocument, FixErr: bool) """
        pass

    def Close(self, SaveChanges, FileName):
        """ Close(self: IAcadDocument, SaveChanges: object, FileName: object) """
        pass

    def CopyObjects(self, Objects, Owner, IdPairs):
        """ CopyObjects(self: IAcadDocument, Objects: object, Owner: object) -> (object, object) """
        pass

    def EndUndoMark(self):
        """ EndUndoMark(self: IAcadDocument) """
        pass

    def Export(self, FileName, Extension, SelectionSet):
        """ Export(self: IAcadDocument, FileName: str, Extension: str, SelectionSet: AcadSelectionSet) """
        pass

    def GetVariable(self, Name):
        """ GetVariable(self: IAcadDocument, Name: str) -> object """
        pass

    def HandleToObject(self, Handle):
        """ HandleToObject(self: IAcadDocument, Handle: str) -> object """
        pass

    def Import(self, FileName, InsertionPoint, ScaleFactor):
        """ Import(self: IAcadDocument, FileName: str, InsertionPoint: object, ScaleFactor: float) -> object """
        pass

    def LoadShapeFile(self, FullName):
        """ LoadShapeFile(self: IAcadDocument, FullName: str) """
        pass

    def New(self, TemplateFileName):
        """ New(self: IAcadDocument, TemplateFileName: str) -> AcadDocument """
        pass

    def ObjectIdToObject(self, ObjectID):
        """ ObjectIdToObject(self: IAcadDocument, ObjectID: Int64) -> object """
        pass

    def Open(self, FullName, Password):
        """ Open(self: IAcadDocument, FullName: str, Password: object) -> AcadDocument """
        pass

    def PostCommand(self, Command):
        """ PostCommand(self: IAcadDocument, Command: str) """
        pass

    def PurgeAll(self):
        """ PurgeAll(self: IAcadDocument) """
        pass

    def Regen(self, WhichViewports):
        """ Regen(self: IAcadDocument, WhichViewports: AcRegenType) """
        pass

    def Save(self):
        """ Save(self: IAcadDocument) """
        pass

    def SaveAs(self, FullFileName, SaveAsType, vSecurityParams):
        """ SaveAs(self: IAcadDocument, FullFileName: str, SaveAsType: object, vSecurityParams: object) """
        pass

    def SendCommand(self, Command):
        """ SendCommand(self: IAcadDocument, Command: str) """
        pass

    def SetVariable(self, Name, Value):
        """ SetVariable(self: IAcadDocument, Name: str, Value: object) """
        pass

    def StartUndoMark(self):
        """ StartUndoMark(self: IAcadDocument) """
        pass

    def Wblock(self, FileName, SelectionSet):
        """ Wblock(self: IAcadDocument, FileName: str, SelectionSet: AcadSelectionSet) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: IAcadDocument) -> bool

"""

    ActiveDimStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveDimStyle(self: IAcadDocument) -> AcadDimStyle

Set: ActiveDimStyle(self: IAcadDocument) = value
"""

    ActiveLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveLayer(self: IAcadDocument) -> AcadLayer

Set: ActiveLayer(self: IAcadDocument) = value
"""

    ActiveLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveLayout(self: IAcadDocument) -> AcadLayout

Set: ActiveLayout(self: IAcadDocument) = value
"""

    ActiveLinetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveLinetype(self: IAcadDocument) -> AcadLineType

Set: ActiveLinetype(self: IAcadDocument) = value
"""

    ActiveMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveMaterial(self: IAcadDocument) -> AcadMaterial

Set: ActiveMaterial(self: IAcadDocument) = value
"""

    ActivePViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActivePViewport(self: IAcadDocument) -> AcadPViewport

Set: ActivePViewport(self: IAcadDocument) = value
"""

    ActiveSelectionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveSelectionSet(self: IAcadDocument) -> AcadSelectionSet

"""

    ActiveSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveSpace(self: IAcadDocument) -> AcActiveSpace

Set: ActiveSpace(self: IAcadDocument) = value
"""

    ActiveTextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveTextStyle(self: IAcadDocument) -> AcadTextStyle

Set: ActiveTextStyle(self: IAcadDocument) = value
"""

    ActiveUCS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveUCS(self: IAcadDocument) -> AcadUCS

Set: ActiveUCS(self: IAcadDocument) = value
"""

    ActiveViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveViewport(self: IAcadDocument) -> AcadViewport

Set: ActiveViewport(self: IAcadDocument) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadDocument) -> IAcadApplication

"""

    Blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blocks(self: IAcadDocument) -> AcadBlocks

"""

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: IAcadDocument) -> AcadDatabase

"""

    Dictionaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dictionaries(self: IAcadDocument) -> AcadDictionaries

"""

    DimStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimStyles(self: IAcadDocument) -> AcadDimStyles

"""

    ElevationModelSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationModelSpace(self: IAcadDocument) -> float

Set: ElevationModelSpace(self: IAcadDocument) = value
"""

    ElevationPaperSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationPaperSpace(self: IAcadDocument) -> float

Set: ElevationPaperSpace(self: IAcadDocument) = value
"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: IAcadDocument) -> str

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Groups(self: IAcadDocument) -> AcadGroups

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: IAcadDocument) -> int

Set: Height(self: IAcadDocument) = value
"""

    HWND = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HWND(self: IAcadDocument) -> Int64

"""

    Layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layers(self: IAcadDocument) -> AcadLayers

"""

    Layouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layouts(self: IAcadDocument) -> AcadLayouts

"""

    Limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Limits(self: IAcadDocument) -> object

Set: Limits(self: IAcadDocument) = value
"""

    Linetypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetypes(self: IAcadDocument) -> AcadLineTypes

"""

    Materials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Materials(self: IAcadDocument) -> AcadMaterials

"""

    ModelSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelSpace(self: IAcadDocument) -> AcadModelSpace

"""

    MSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MSpace(self: IAcadDocument) -> bool

Set: MSpace(self: IAcadDocument) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAcadDocument) -> str

"""

    ObjectSnapMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectSnapMode(self: IAcadDocument) -> bool

Set: ObjectSnapMode(self: IAcadDocument) = value
"""

    PaperSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PaperSpace(self: IAcadDocument) -> AcadPaperSpace

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: IAcadDocument) -> str

"""

    PickfirstSelectionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickfirstSelectionSet(self: IAcadDocument) -> AcadSelectionSet

"""

    Plot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plot(self: IAcadDocument) -> AcadPlot

"""

    PlotConfigurations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotConfigurations(self: IAcadDocument) -> AcadPlotConfigurations

"""

    Preferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preferences(self: IAcadDocument) -> AcadDatabasePreferences

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: IAcadDocument) -> bool

"""

    RegisteredApplications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegisteredApplications(self: IAcadDocument) -> AcadRegisteredApplications

"""

    Saved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Saved(self: IAcadDocument) -> bool

"""

    SectionManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionManager(self: IAcadDocument) -> AcadSectionManager

"""

    SelectionSets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionSets(self: IAcadDocument) -> AcadSelectionSets

"""

    SummaryInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SummaryInfo(self: IAcadDocument) -> AcadSummaryInfo

"""

    TextStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyles(self: IAcadDocument) -> AcadTextStyles

"""

    UserCoordinateSystems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserCoordinateSystems(self: IAcadDocument) -> AcadUCSs

"""

    Utility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Utility(self: IAcadDocument) -> AcadUtility

"""

    Viewports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewports(self: IAcadDocument) -> AcadViewports

"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Views(self: IAcadDocument) -> AcadViews

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: IAcadDocument) -> int

Set: Width(self: IAcadDocument) = value
"""

    WindowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowState(self: IAcadDocument) -> AcWindowState

Set: WindowState(self: IAcadDocument) = value
"""

    WindowTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowTitle(self: IAcadDocument) -> str

"""



class _DAcadDocumentEvents_Event:
    # no doc
    def add_Activate(self, A_1):
        """ add_Activate(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ActivateEventHandler) """
        pass

    def add_BeginClose(self, A_1):
        """ add_BeginClose(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginCloseEventHandler) """
        pass

    def add_BeginCommand(self, A_1):
        """ add_BeginCommand(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginCommandEventHandler) """
        pass

    def add_BeginDocClose(self, A_1):
        """ add_BeginDocClose(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginDocCloseEventHandler) """
        pass

    def add_BeginDoubleClick(self, A_1):
        """ add_BeginDoubleClick(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginDoubleClickEventHandler) """
        pass

    def add_BeginLisp(self, A_1):
        """ add_BeginLisp(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginLispEventHandler) """
        pass

    def add_BeginPlot(self, A_1):
        """ add_BeginPlot(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginPlotEventHandler) """
        pass

    def add_BeginRightClick(self, A_1):
        """ add_BeginRightClick(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginRightClickEventHandler) """
        pass

    def add_BeginSave(self, A_1):
        """ add_BeginSave(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginSaveEventHandler) """
        pass

    def add_BeginShortcutMenuCommand(self, A_1):
        """ add_BeginShortcutMenuCommand(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuCommandEventHandler) """
        pass

    def add_BeginShortcutMenuDefault(self, A_1):
        """ add_BeginShortcutMenuDefault(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuDefaultEventHandler) """
        pass

    def add_BeginShortcutMenuEdit(self, A_1):
        """ add_BeginShortcutMenuEdit(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuEditEventHandler) """
        pass

    def add_BeginShortcutMenuGrip(self, A_1):
        """ add_BeginShortcutMenuGrip(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuGripEventHandler) """
        pass

    def add_BeginShortcutMenuOsnap(self, A_1):
        """ add_BeginShortcutMenuOsnap(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuOsnapEventHandler) """
        pass

    def add_Deactivate(self, A_1):
        """ add_Deactivate(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_DeactivateEventHandler) """
        pass

    def add_EndCommand(self, A_1):
        """ add_EndCommand(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndCommandEventHandler) """
        pass

    def add_EndLisp(self, A_1):
        """ add_EndLisp(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndLispEventHandler) """
        pass

    def add_EndPlot(self, A_1):
        """ add_EndPlot(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndPlotEventHandler) """
        pass

    def add_EndSave(self, A_1):
        """ add_EndSave(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndSaveEventHandler) """
        pass

    def add_EndShortcutMenu(self, A_1):
        """ add_EndShortcutMenu(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndShortcutMenuEventHandler) """
        pass

    def add_LayoutSwitched(self, A_1):
        """ add_LayoutSwitched(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_LayoutSwitchedEventHandler) """
        pass

    def add_LispCancelled(self, A_1):
        """ add_LispCancelled(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_LispCancelledEventHandler) """
        pass

    def add_ObjectAdded(self, A_1):
        """ add_ObjectAdded(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ObjectAddedEventHandler) """
        pass

    def add_ObjectErased(self, A_1):
        """ add_ObjectErased(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ObjectErasedEventHandler) """
        pass

    def add_ObjectModified(self, A_1):
        """ add_ObjectModified(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ObjectModifiedEventHandler) """
        pass

    def add_SelectionChanged(self, A_1):
        """ add_SelectionChanged(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_SelectionChangedEventHandler) """
        pass

    def add_WindowChanged(self, A_1):
        """ add_WindowChanged(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_WindowChangedEventHandler) """
        pass

    def add_WindowMovedOrResized(self, A_1):
        """ add_WindowMovedOrResized(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_WindowMovedOrResizedEventHandler) """
        pass

    def remove_Activate(self, A_1):
        """ remove_Activate(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ActivateEventHandler) """
        pass

    def remove_BeginClose(self, A_1):
        """ remove_BeginClose(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginCloseEventHandler) """
        pass

    def remove_BeginCommand(self, A_1):
        """ remove_BeginCommand(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginCommandEventHandler) """
        pass

    def remove_BeginDocClose(self, A_1):
        """ remove_BeginDocClose(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginDocCloseEventHandler) """
        pass

    def remove_BeginDoubleClick(self, A_1):
        """ remove_BeginDoubleClick(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginDoubleClickEventHandler) """
        pass

    def remove_BeginLisp(self, A_1):
        """ remove_BeginLisp(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginLispEventHandler) """
        pass

    def remove_BeginPlot(self, A_1):
        """ remove_BeginPlot(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginPlotEventHandler) """
        pass

    def remove_BeginRightClick(self, A_1):
        """ remove_BeginRightClick(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginRightClickEventHandler) """
        pass

    def remove_BeginSave(self, A_1):
        """ remove_BeginSave(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginSaveEventHandler) """
        pass

    def remove_BeginShortcutMenuCommand(self, A_1):
        """ remove_BeginShortcutMenuCommand(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuCommandEventHandler) """
        pass

    def remove_BeginShortcutMenuDefault(self, A_1):
        """ remove_BeginShortcutMenuDefault(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuDefaultEventHandler) """
        pass

    def remove_BeginShortcutMenuEdit(self, A_1):
        """ remove_BeginShortcutMenuEdit(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuEditEventHandler) """
        pass

    def remove_BeginShortcutMenuGrip(self, A_1):
        """ remove_BeginShortcutMenuGrip(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuGripEventHandler) """
        pass

    def remove_BeginShortcutMenuOsnap(self, A_1):
        """ remove_BeginShortcutMenuOsnap(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_BeginShortcutMenuOsnapEventHandler) """
        pass

    def remove_Deactivate(self, A_1):
        """ remove_Deactivate(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_DeactivateEventHandler) """
        pass

    def remove_EndCommand(self, A_1):
        """ remove_EndCommand(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndCommandEventHandler) """
        pass

    def remove_EndLisp(self, A_1):
        """ remove_EndLisp(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndLispEventHandler) """
        pass

    def remove_EndPlot(self, A_1):
        """ remove_EndPlot(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndPlotEventHandler) """
        pass

    def remove_EndSave(self, A_1):
        """ remove_EndSave(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndSaveEventHandler) """
        pass

    def remove_EndShortcutMenu(self, A_1):
        """ remove_EndShortcutMenu(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_EndShortcutMenuEventHandler) """
        pass

    def remove_LayoutSwitched(self, A_1):
        """ remove_LayoutSwitched(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_LayoutSwitchedEventHandler) """
        pass

    def remove_LispCancelled(self, A_1):
        """ remove_LispCancelled(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_LispCancelledEventHandler) """
        pass

    def remove_ObjectAdded(self, A_1):
        """ remove_ObjectAdded(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ObjectAddedEventHandler) """
        pass

    def remove_ObjectErased(self, A_1):
        """ remove_ObjectErased(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ObjectErasedEventHandler) """
        pass

    def remove_ObjectModified(self, A_1):
        """ remove_ObjectModified(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_ObjectModifiedEventHandler) """
        pass

    def remove_SelectionChanged(self, A_1):
        """ remove_SelectionChanged(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_SelectionChangedEventHandler) """
        pass

    def remove_WindowChanged(self, A_1):
        """ remove_WindowChanged(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_WindowChangedEventHandler) """
        pass

    def remove_WindowMovedOrResized(self, A_1):
        """ remove_WindowMovedOrResized(self: _DAcadDocumentEvents_Event, A_1: _DAcadDocumentEvents_WindowMovedOrResizedEventHandler) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Activate = None
    BeginClose = None
    BeginCommand = None
    BeginDocClose = None
    BeginDoubleClick = None
    BeginLisp = None
    BeginPlot = None
    BeginRightClick = None
    BeginSave = None
    BeginShortcutMenuCommand = None
    BeginShortcutMenuDefault = None
    BeginShortcutMenuEdit = None
    BeginShortcutMenuGrip = None
    BeginShortcutMenuOsnap = None
    Deactivate = None
    EndCommand = None
    EndLisp = None
    EndPlot = None
    EndSave = None
    EndShortcutMenu = None
    LayoutSwitched = None
    LispCancelled = None
    ObjectAdded = None
    ObjectErased = None
    ObjectModified = None
    SelectionChanged = None
    WindowChanged = None
    WindowMovedOrResized = None


class AcadDocument(IAcadDocument, IAcadDatabase, _DAcadDocumentEvents_Event):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadDocumentClass(__ComObject):
    """ AcadDocumentClass() """
    def Activate(self):
        """ Activate(self: AcadDocumentClass) """
        pass

    def add_Activate(self, A_1):
        """ add_Activate(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ActivateEventHandler) """
        pass

    def add_BeginClose(self, A_1):
        """ add_BeginClose(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginCloseEventHandler) """
        pass

    def add_BeginCommand(self, A_1):
        """ add_BeginCommand(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginCommandEventHandler) """
        pass

    def add_BeginDocClose(self, A_1):
        """ add_BeginDocClose(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginDocCloseEventHandler) """
        pass

    def add_BeginDoubleClick(self, A_1):
        """ add_BeginDoubleClick(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginDoubleClickEventHandler) """
        pass

    def add_BeginLisp(self, A_1):
        """ add_BeginLisp(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginLispEventHandler) """
        pass

    def add_BeginPlot(self, A_1):
        """ add_BeginPlot(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginPlotEventHandler) """
        pass

    def add_BeginRightClick(self, A_1):
        """ add_BeginRightClick(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginRightClickEventHandler) """
        pass

    def add_BeginSave(self, A_1):
        """ add_BeginSave(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginSaveEventHandler) """
        pass

    def add_BeginShortcutMenuCommand(self, A_1):
        """ add_BeginShortcutMenuCommand(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuCommandEventHandler) """
        pass

    def add_BeginShortcutMenuDefault(self, A_1):
        """ add_BeginShortcutMenuDefault(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuDefaultEventHandler) """
        pass

    def add_BeginShortcutMenuEdit(self, A_1):
        """ add_BeginShortcutMenuEdit(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuEditEventHandler) """
        pass

    def add_BeginShortcutMenuGrip(self, A_1):
        """ add_BeginShortcutMenuGrip(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuGripEventHandler) """
        pass

    def add_BeginShortcutMenuOsnap(self, A_1):
        """ add_BeginShortcutMenuOsnap(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuOsnapEventHandler) """
        pass

    def add_Deactivate(self, A_1):
        """ add_Deactivate(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_DeactivateEventHandler) """
        pass

    def add_EndCommand(self, A_1):
        """ add_EndCommand(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndCommandEventHandler) """
        pass

    def add_EndLisp(self, A_1):
        """ add_EndLisp(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndLispEventHandler) """
        pass

    def add_EndPlot(self, A_1):
        """ add_EndPlot(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndPlotEventHandler) """
        pass

    def add_EndSave(self, A_1):
        """ add_EndSave(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndSaveEventHandler) """
        pass

    def add_EndShortcutMenu(self, A_1):
        """ add_EndShortcutMenu(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndShortcutMenuEventHandler) """
        pass

    def add_LayoutSwitched(self, A_1):
        """ add_LayoutSwitched(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_LayoutSwitchedEventHandler) """
        pass

    def add_LispCancelled(self, A_1):
        """ add_LispCancelled(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_LispCancelledEventHandler) """
        pass

    def add_ObjectAdded(self, A_1):
        """ add_ObjectAdded(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ObjectAddedEventHandler) """
        pass

    def add_ObjectErased(self, A_1):
        """ add_ObjectErased(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ObjectErasedEventHandler) """
        pass

    def add_ObjectModified(self, A_1):
        """ add_ObjectModified(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ObjectModifiedEventHandler) """
        pass

    def add_SelectionChanged(self, A_1):
        """ add_SelectionChanged(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_SelectionChangedEventHandler) """
        pass

    def add_WindowChanged(self, A_1):
        """ add_WindowChanged(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_WindowChangedEventHandler) """
        pass

    def add_WindowMovedOrResized(self, A_1):
        """ add_WindowMovedOrResized(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_WindowMovedOrResizedEventHandler) """
        pass

    def AuditInfo(self, FixErr):
        """ AuditInfo(self: AcadDocumentClass, FixErr: bool) """
        pass

    def Close(self, SaveChanges, FileName):
        """ Close(self: AcadDocumentClass, SaveChanges: object, FileName: object) """
        pass

    def CopyObjects(self, Objects, Owner, IdPairs):
        """ CopyObjects(self: AcadDocumentClass, Objects: object, Owner: object) -> (object, object) """
        pass

    def EndUndoMark(self):
        """ EndUndoMark(self: AcadDocumentClass) """
        pass

    def Export(self, FileName, Extension, SelectionSet):
        """ Export(self: AcadDocumentClass, FileName: str, Extension: str, SelectionSet: AcadSelectionSet) """
        pass

    def GetVariable(self, Name):
        """ GetVariable(self: AcadDocumentClass, Name: str) -> object """
        pass

    def HandleToObject(self, Handle):
        """ HandleToObject(self: AcadDocumentClass, Handle: str) -> object """
        pass

    def Import(self, FileName, InsertionPoint, ScaleFactor):
        """ Import(self: AcadDocumentClass, FileName: str, InsertionPoint: object, ScaleFactor: float) -> object """
        pass

    def LoadShapeFile(self, FullName):
        """ LoadShapeFile(self: AcadDocumentClass, FullName: str) """
        pass

    def New(self, TemplateFileName):
        """ New(self: AcadDocumentClass, TemplateFileName: str) -> AcadDocument """
        pass

    def ObjectIdToObject(self, ObjectID):
        """ ObjectIdToObject(self: AcadDocumentClass, ObjectID: Int64) -> object """
        pass

    def Open(self, FullName, Password):
        """ Open(self: AcadDocumentClass, FullName: str, Password: object) -> AcadDocument """
        pass

    def PostCommand(self, Command):
        """ PostCommand(self: AcadDocumentClass, Command: str) """
        pass

    def PurgeAll(self):
        """ PurgeAll(self: AcadDocumentClass) """
        pass

    def Regen(self, WhichViewports):
        """ Regen(self: AcadDocumentClass, WhichViewports: AcRegenType) """
        pass

    def remove_Activate(self, A_1):
        """ remove_Activate(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ActivateEventHandler) """
        pass

    def remove_BeginClose(self, A_1):
        """ remove_BeginClose(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginCloseEventHandler) """
        pass

    def remove_BeginCommand(self, A_1):
        """ remove_BeginCommand(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginCommandEventHandler) """
        pass

    def remove_BeginDocClose(self, A_1):
        """ remove_BeginDocClose(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginDocCloseEventHandler) """
        pass

    def remove_BeginDoubleClick(self, A_1):
        """ remove_BeginDoubleClick(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginDoubleClickEventHandler) """
        pass

    def remove_BeginLisp(self, A_1):
        """ remove_BeginLisp(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginLispEventHandler) """
        pass

    def remove_BeginPlot(self, A_1):
        """ remove_BeginPlot(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginPlotEventHandler) """
        pass

    def remove_BeginRightClick(self, A_1):
        """ remove_BeginRightClick(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginRightClickEventHandler) """
        pass

    def remove_BeginSave(self, A_1):
        """ remove_BeginSave(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginSaveEventHandler) """
        pass

    def remove_BeginShortcutMenuCommand(self, A_1):
        """ remove_BeginShortcutMenuCommand(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuCommandEventHandler) """
        pass

    def remove_BeginShortcutMenuDefault(self, A_1):
        """ remove_BeginShortcutMenuDefault(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuDefaultEventHandler) """
        pass

    def remove_BeginShortcutMenuEdit(self, A_1):
        """ remove_BeginShortcutMenuEdit(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuEditEventHandler) """
        pass

    def remove_BeginShortcutMenuGrip(self, A_1):
        """ remove_BeginShortcutMenuGrip(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuGripEventHandler) """
        pass

    def remove_BeginShortcutMenuOsnap(self, A_1):
        """ remove_BeginShortcutMenuOsnap(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_BeginShortcutMenuOsnapEventHandler) """
        pass

    def remove_Deactivate(self, A_1):
        """ remove_Deactivate(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_DeactivateEventHandler) """
        pass

    def remove_EndCommand(self, A_1):
        """ remove_EndCommand(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndCommandEventHandler) """
        pass

    def remove_EndLisp(self, A_1):
        """ remove_EndLisp(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndLispEventHandler) """
        pass

    def remove_EndPlot(self, A_1):
        """ remove_EndPlot(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndPlotEventHandler) """
        pass

    def remove_EndSave(self, A_1):
        """ remove_EndSave(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndSaveEventHandler) """
        pass

    def remove_EndShortcutMenu(self, A_1):
        """ remove_EndShortcutMenu(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_EndShortcutMenuEventHandler) """
        pass

    def remove_LayoutSwitched(self, A_1):
        """ remove_LayoutSwitched(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_LayoutSwitchedEventHandler) """
        pass

    def remove_LispCancelled(self, A_1):
        """ remove_LispCancelled(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_LispCancelledEventHandler) """
        pass

    def remove_ObjectAdded(self, A_1):
        """ remove_ObjectAdded(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ObjectAddedEventHandler) """
        pass

    def remove_ObjectErased(self, A_1):
        """ remove_ObjectErased(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ObjectErasedEventHandler) """
        pass

    def remove_ObjectModified(self, A_1):
        """ remove_ObjectModified(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_ObjectModifiedEventHandler) """
        pass

    def remove_SelectionChanged(self, A_1):
        """ remove_SelectionChanged(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_SelectionChangedEventHandler) """
        pass

    def remove_WindowChanged(self, A_1):
        """ remove_WindowChanged(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_WindowChangedEventHandler) """
        pass

    def remove_WindowMovedOrResized(self, A_1):
        """ remove_WindowMovedOrResized(self: AcadDocumentClass, A_1: _DAcadDocumentEvents_WindowMovedOrResizedEventHandler) """
        pass

    def Save(self):
        """ Save(self: AcadDocumentClass) """
        pass

    def SaveAs(self, FullFileName, SaveAsType, vSecurityParams):
        """ SaveAs(self: AcadDocumentClass, FullFileName: str, SaveAsType: object, vSecurityParams: object) """
        pass

    def SendCommand(self, Command):
        """ SendCommand(self: AcadDocumentClass, Command: str) """
        pass

    def SetVariable(self, Name, Value):
        """ SetVariable(self: AcadDocumentClass, Name: str, Value: object) """
        pass

    def StartUndoMark(self):
        """ StartUndoMark(self: AcadDocumentClass) """
        pass

    def Wblock(self, FileName, SelectionSet):
        """ Wblock(self: AcadDocumentClass, FileName: str, SelectionSet: AcadSelectionSet) """
        pass

    Active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Active(self: AcadDocumentClass) -> bool

"""

    ActiveDimStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveDimStyle(self: AcadDocumentClass) -> AcadDimStyle

Set: ActiveDimStyle(self: AcadDocumentClass) = value
"""

    ActiveLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveLayer(self: AcadDocumentClass) -> AcadLayer

Set: ActiveLayer(self: AcadDocumentClass) = value
"""

    ActiveLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveLayout(self: AcadDocumentClass) -> AcadLayout

Set: ActiveLayout(self: AcadDocumentClass) = value
"""

    ActiveLinetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveLinetype(self: AcadDocumentClass) -> AcadLineType

Set: ActiveLinetype(self: AcadDocumentClass) = value
"""

    ActiveMaterial = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveMaterial(self: AcadDocumentClass) -> AcadMaterial

Set: ActiveMaterial(self: AcadDocumentClass) = value
"""

    ActivePViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActivePViewport(self: AcadDocumentClass) -> AcadPViewport

Set: ActivePViewport(self: AcadDocumentClass) = value
"""

    ActiveSelectionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveSelectionSet(self: AcadDocumentClass) -> AcadSelectionSet

"""

    ActiveSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveSpace(self: AcadDocumentClass) -> AcActiveSpace

Set: ActiveSpace(self: AcadDocumentClass) = value
"""

    ActiveTextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveTextStyle(self: AcadDocumentClass) -> AcadTextStyle

Set: ActiveTextStyle(self: AcadDocumentClass) = value
"""

    ActiveUCS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveUCS(self: AcadDocumentClass) -> AcadUCS

Set: ActiveUCS(self: AcadDocumentClass) = value
"""

    ActiveViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveViewport(self: AcadDocumentClass) -> AcadViewport

Set: ActiveViewport(self: AcadDocumentClass) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadDocumentClass) -> IAcadApplication

"""

    Blocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blocks(self: AcadDocumentClass) -> AcadBlocks

"""

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: AcadDocumentClass) -> AcadDatabase

"""

    Dictionaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dictionaries(self: AcadDocumentClass) -> AcadDictionaries

"""

    DimStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimStyles(self: AcadDocumentClass) -> AcadDimStyles

"""

    ElevationModelSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationModelSpace(self: AcadDocumentClass) -> float

Set: ElevationModelSpace(self: AcadDocumentClass) = value
"""

    ElevationPaperSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationPaperSpace(self: AcadDocumentClass) -> float

Set: ElevationPaperSpace(self: AcadDocumentClass) = value
"""

    FullName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullName(self: AcadDocumentClass) -> str

"""

    Groups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Groups(self: AcadDocumentClass) -> AcadGroups

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: AcadDocumentClass) -> int

Set: Height(self: AcadDocumentClass) = value
"""

    HWND = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HWND(self: AcadDocumentClass) -> Int64

"""

    Layers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layers(self: AcadDocumentClass) -> AcadLayers

"""

    Layouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layouts(self: AcadDocumentClass) -> AcadLayouts

"""

    Limits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Limits(self: AcadDocumentClass) -> object

Set: Limits(self: AcadDocumentClass) = value
"""

    Linetypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetypes(self: AcadDocumentClass) -> AcadLineTypes

"""

    Materials = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Materials(self: AcadDocumentClass) -> AcadMaterials

"""

    ModelSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelSpace(self: AcadDocumentClass) -> AcadModelSpace

"""

    MSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MSpace(self: AcadDocumentClass) -> bool

Set: MSpace(self: AcadDocumentClass) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadDocumentClass) -> str

"""

    ObjectSnapMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectSnapMode(self: AcadDocumentClass) -> bool

Set: ObjectSnapMode(self: AcadDocumentClass) = value
"""

    PaperSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PaperSpace(self: AcadDocumentClass) -> AcadPaperSpace

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: AcadDocumentClass) -> str

"""

    PickfirstSelectionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickfirstSelectionSet(self: AcadDocumentClass) -> AcadSelectionSet

"""

    Plot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Plot(self: AcadDocumentClass) -> AcadPlot

"""

    PlotConfigurations = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotConfigurations(self: AcadDocumentClass) -> AcadPlotConfigurations

"""

    Preferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Preferences(self: AcadDocumentClass) -> AcadDatabasePreferences

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: AcadDocumentClass) -> bool

"""

    RegisteredApplications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RegisteredApplications(self: AcadDocumentClass) -> AcadRegisteredApplications

"""

    Saved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Saved(self: AcadDocumentClass) -> bool

"""

    SectionManager = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionManager(self: AcadDocumentClass) -> AcadSectionManager

"""

    SelectionSets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionSets(self: AcadDocumentClass) -> AcadSelectionSets

"""

    SummaryInfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SummaryInfo(self: AcadDocumentClass) -> AcadSummaryInfo

"""

    TextStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyles(self: AcadDocumentClass) -> AcadTextStyles

"""

    UserCoordinateSystems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserCoordinateSystems(self: AcadDocumentClass) -> AcadUCSs

"""

    Utility = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Utility(self: AcadDocumentClass) -> AcadUtility

"""

    Viewports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Viewports(self: AcadDocumentClass) -> AcadViewports

"""

    Views = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Views(self: AcadDocumentClass) -> AcadViews

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: AcadDocumentClass) -> int

Set: Width(self: AcadDocumentClass) = value
"""

    WindowState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowState(self: AcadDocumentClass) -> AcWindowState

Set: WindowState(self: AcadDocumentClass) = value
"""

    WindowTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WindowTitle(self: AcadDocumentClass) -> str

"""


    BeginClose = None
    BeginCommand = None
    BeginDocClose = None
    BeginDoubleClick = None
    BeginLisp = None
    BeginPlot = None
    BeginRightClick = None
    BeginSave = None
    BeginShortcutMenuCommand = None
    BeginShortcutMenuDefault = None
    BeginShortcutMenuEdit = None
    BeginShortcutMenuGrip = None
    BeginShortcutMenuOsnap = None
    Deactivate = None
    EndCommand = None
    EndLisp = None
    EndPlot = None
    EndSave = None
    EndShortcutMenu = None
    LayoutSwitched = None
    LispCancelled = None
    ObjectAdded = None
    ObjectErased = None
    ObjectModified = None
    SelectionChanged = None
    WindowChanged = None
    WindowMovedOrResized = None
    _DAcadDocumentEvents_Event_Activate = None


class IAcadDocuments(IEnumerable):
    # no doc
    def Add(self, TemplateName):
        """ Add(self: IAcadDocuments, TemplateName: object) -> AcadDocument """
        pass

    def Close(self):
        """ Close(self: IAcadDocuments) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadDocuments) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: IAcadDocuments, Index: object) -> AcadDocument """
        pass

    def Open(self, Name, ReadOnly, Password):
        """ Open(self: IAcadDocuments, Name: str, ReadOnly: object, Password: object) -> AcadDocument """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadDocuments) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadDocuments) -> int

"""



class AcadDocuments(IAcadDocuments, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadDocumentsClass(__ComObject):
    # no doc
    def Add(self, TemplateName):
        """ Add(self: AcadDocumentsClass, TemplateName: object) -> AcadDocument """
        pass

    def Close(self):
        """ Close(self: AcadDocumentsClass) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcadDocumentsClass) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: AcadDocumentsClass, Index: object) -> AcadDocument """
        pass

    def Open(self, Name, ReadOnly, Password):
        """ Open(self: AcadDocumentsClass, Name: str, ReadOnly: object, Password: object) -> AcadDocument """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadDocumentsClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadDocumentsClass) -> int

"""



class IAcadMenuBar(IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadMenuBar) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: IAcadMenuBar, Index: object) -> AcadPopupMenu """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadMenuBar) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadMenuBar) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadMenuBar) -> IAcadApplication

"""



class AcadMenuBar(IAcadMenuBar, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadMenuBarClass(__ComObject):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: AcadMenuBarClass) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: AcadMenuBarClass, Index: object) -> AcadPopupMenu """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadMenuBarClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadMenuBarClass) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadMenuBarClass) -> IAcadApplication

"""



class IAcadMenuGroup:
    # no doc
    def Save(self, MenuFileType):
        """ Save(self: IAcadMenuGroup, MenuFileType: AcMenuFileType) """
        pass

    def SaveAs(self, MenuFileName, MenuFileType):
        """ SaveAs(self: IAcadMenuGroup, MenuFileName: str, MenuFileType: AcMenuFileType) """
        pass

    def Unload(self):
        """ Unload(self: IAcadMenuGroup) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadMenuGroup) -> IAcadApplication

"""

    MenuFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuFileName(self: IAcadMenuGroup) -> str

"""

    Menus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Menus(self: IAcadMenuGroup) -> AcadPopupMenus

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAcadMenuGroup) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadMenuGroup) -> AcadMenuGroups

"""

    Toolbars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Toolbars(self: IAcadMenuGroup) -> AcadToolbars

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: IAcadMenuGroup) -> AcMenuGroupType

"""



class AcadMenuGroup(IAcadMenuGroup):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadMenuGroupClass(__ComObject):
    # no doc
    def Save(self, MenuFileType):
        """ Save(self: AcadMenuGroupClass, MenuFileType: AcMenuFileType) """
        pass

    def SaveAs(self, MenuFileName, MenuFileType):
        """ SaveAs(self: AcadMenuGroupClass, MenuFileName: str, MenuFileType: AcMenuFileType) """
        pass

    def Unload(self):
        """ Unload(self: AcadMenuGroupClass) """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadMenuGroupClass) -> IAcadApplication

"""

    MenuFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuFileName(self: AcadMenuGroupClass) -> str

"""

    Menus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Menus(self: AcadMenuGroupClass) -> AcadPopupMenus

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadMenuGroupClass) -> str

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadMenuGroupClass) -> AcadMenuGroups

"""

    Toolbars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Toolbars(self: AcadMenuGroupClass) -> AcadToolbars

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AcadMenuGroupClass) -> AcMenuGroupType

"""



class IAcadMenuGroups(IEnumerable):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadMenuGroups) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: IAcadMenuGroups, Index: object) -> AcadMenuGroup """
        pass

    def Load(self, MenuFileName, BaseMenu):
        """ Load(self: IAcadMenuGroups, MenuFileName: str, BaseMenu: object) -> AcadMenuGroup """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadMenuGroups) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadMenuGroups) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadMenuGroups) -> IAcadApplication

"""



class AcadMenuGroups(IAcadMenuGroups, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadMenuGroupsClass(__ComObject):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: AcadMenuGroupsClass) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: AcadMenuGroupsClass, Index: object) -> AcadMenuGroup """
        pass

    def Load(self, MenuFileName, BaseMenu):
        """ Load(self: AcadMenuGroupsClass, MenuFileName: str, BaseMenu: object) -> AcadMenuGroup """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadMenuGroupsClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadMenuGroupsClass) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadMenuGroupsClass) -> IAcadApplication

"""



class IAcadPlot:
    # no doc
    def DisplayPlotPreview(self, Preview):
        """ DisplayPlotPreview(self: IAcadPlot, Preview: AcPreviewMode) """
        pass

    def PlotToDevice(self, plotConfig):
        """ PlotToDevice(self: IAcadPlot, plotConfig: object) -> bool """
        pass

    def PlotToFile(self, plotFile, plotConfig):
        """ PlotToFile(self: IAcadPlot, plotFile: str, plotConfig: object) -> bool """
        pass

    def SetLayoutsToPlot(self, layoutList):
        """ SetLayoutsToPlot(self: IAcadPlot, layoutList: object) """
        pass

    def StartBatchMode(self, entryCount):
        """ StartBatchMode(self: IAcadPlot, entryCount: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPlot) -> IAcadApplication

"""

    BatchPlotProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchPlotProgress(self: IAcadPlot) -> bool

Set: BatchPlotProgress(self: IAcadPlot) = value
"""

    NumberOfCopies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfCopies(self: IAcadPlot) -> int

Set: NumberOfCopies(self: IAcadPlot) = value
"""

    QuietErrorMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuietErrorMode(self: IAcadPlot) -> bool

Set: QuietErrorMode(self: IAcadPlot) = value
"""



class AcadPlot(IAcadPlot):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPlotClass(__ComObject):
    # no doc
    def DisplayPlotPreview(self, Preview):
        """ DisplayPlotPreview(self: AcadPlotClass, Preview: AcPreviewMode) """
        pass

    def PlotToDevice(self, plotConfig):
        """ PlotToDevice(self: AcadPlotClass, plotConfig: object) -> bool """
        pass

    def PlotToFile(self, plotFile, plotConfig):
        """ PlotToFile(self: AcadPlotClass, plotFile: str, plotConfig: object) -> bool """
        pass

    def SetLayoutsToPlot(self, layoutList):
        """ SetLayoutsToPlot(self: AcadPlotClass, layoutList: object) """
        pass

    def StartBatchMode(self, entryCount):
        """ StartBatchMode(self: AcadPlotClass, entryCount: int) """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPlotClass) -> IAcadApplication

"""

    BatchPlotProgress = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BatchPlotProgress(self: AcadPlotClass) -> bool

Set: BatchPlotProgress(self: AcadPlotClass) = value
"""

    NumberOfCopies = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfCopies(self: AcadPlotClass) -> int

Set: NumberOfCopies(self: AcadPlotClass) = value
"""

    QuietErrorMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuietErrorMode(self: AcadPlotClass) -> bool

Set: QuietErrorMode(self: AcadPlotClass) = value
"""



class IAcadPopupMenu(IEnumerable):
    # no doc
    def AddMenuItem(self, Index, Label, Macro):
        """ AddMenuItem(self: IAcadPopupMenu, Index: object, Label: str, Macro: str) -> AcadPopupMenuItem """
        pass

    def AddSeparator(self, Index):
        """ AddSeparator(self: IAcadPopupMenu, Index: object) -> AcadPopupMenuItem """
        pass

    def AddSubMenu(self, Index, Label):
        """ AddSubMenu(self: IAcadPopupMenu, Index: object, Label: str) -> AcadPopupMenu """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadPopupMenu) -> IEnumerator """
        pass

    def InsertInMenuBar(self, Index):
        """ InsertInMenuBar(self: IAcadPopupMenu, Index: object) """
        pass

    def Item(self, Index):
        """ Item(self: IAcadPopupMenu, Index: object) -> AcadPopupMenuItem """
        pass

    def RemoveFromMenuBar(self):
        """ RemoveFromMenuBar(self: IAcadPopupMenu) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPopupMenu) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadPopupMenu) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAcadPopupMenu) -> str

Set: Name(self: IAcadPopupMenu) = value
"""

    NameNoMnemonic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameNoMnemonic(self: IAcadPopupMenu) -> str

"""

    OnMenuBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnMenuBar(self: IAcadPopupMenu) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadPopupMenu) -> object

"""

    ShortcutMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShortcutMenu(self: IAcadPopupMenu) -> bool

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: IAcadPopupMenu) -> str

"""



class AcadPopupMenu(IAcadPopupMenu, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadPopupMenuClass(__ComObject):
    # no doc
    def AddMenuItem(self, Index, Label, Macro):
        """ AddMenuItem(self: AcadPopupMenuClass, Index: object, Label: str, Macro: str) -> AcadPopupMenuItem """
        pass

    def AddSeparator(self, Index):
        """ AddSeparator(self: AcadPopupMenuClass, Index: object) -> AcadPopupMenuItem """
        pass

    def AddSubMenu(self, Index, Label):
        """ AddSubMenu(self: AcadPopupMenuClass, Index: object, Label: str) -> AcadPopupMenu """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcadPopupMenuClass) -> IEnumerator """
        pass

    def InsertInMenuBar(self, Index):
        """ InsertInMenuBar(self: AcadPopupMenuClass, Index: object) """
        pass

    def Item(self, Index):
        """ Item(self: AcadPopupMenuClass, Index: object) -> AcadPopupMenuItem """
        pass

    def RemoveFromMenuBar(self):
        """ RemoveFromMenuBar(self: AcadPopupMenuClass) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPopupMenuClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadPopupMenuClass) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadPopupMenuClass) -> str

Set: Name(self: AcadPopupMenuClass) = value
"""

    NameNoMnemonic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameNoMnemonic(self: AcadPopupMenuClass) -> str

"""

    OnMenuBar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OnMenuBar(self: AcadPopupMenuClass) -> bool

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadPopupMenuClass) -> object

"""

    ShortcutMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShortcutMenu(self: AcadPopupMenuClass) -> bool

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: AcadPopupMenuClass) -> str

"""



class IAcadPopupMenuItem:
    # no doc
    def Delete(self):
        """ Delete(self: IAcadPopupMenuItem) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPopupMenuItem) -> IAcadApplication

"""

    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Caption(self: IAcadPopupMenuItem) -> str

"""

    Check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Check(self: IAcadPopupMenuItem) -> bool

Set: Check(self: IAcadPopupMenuItem) = value
"""

    Enable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enable(self: IAcadPopupMenuItem) -> bool

Set: Enable(self: IAcadPopupMenuItem) = value
"""

    EndSubMenuLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndSubMenuLevel(self: IAcadPopupMenuItem) -> int

Set: EndSubMenuLevel(self: IAcadPopupMenuItem) = value
"""

    HelpString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpString(self: IAcadPopupMenuItem) -> str

Set: HelpString(self: IAcadPopupMenuItem) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: IAcadPopupMenuItem) -> int

"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: IAcadPopupMenuItem) -> str

Set: Label(self: IAcadPopupMenuItem) = value
"""

    Macro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Macro(self: IAcadPopupMenuItem) -> str

Set: Macro(self: IAcadPopupMenuItem) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadPopupMenuItem) -> AcadPopupMenu

"""

    SubMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubMenu(self: IAcadPopupMenuItem) -> AcadPopupMenu

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: IAcadPopupMenuItem) -> str

Set: TagString(self: IAcadPopupMenuItem) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: IAcadPopupMenuItem) -> AcMenuItemType

"""



class AcadPopupMenuItem(IAcadPopupMenuItem):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPopupMenuItemClass(__ComObject):
    # no doc
    def Delete(self):
        """ Delete(self: AcadPopupMenuItemClass) """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPopupMenuItemClass) -> IAcadApplication

"""

    Caption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Caption(self: AcadPopupMenuItemClass) -> str

"""

    Check = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Check(self: AcadPopupMenuItemClass) -> bool

Set: Check(self: AcadPopupMenuItemClass) = value
"""

    Enable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enable(self: AcadPopupMenuItemClass) -> bool

Set: Enable(self: AcadPopupMenuItemClass) = value
"""

    EndSubMenuLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndSubMenuLevel(self: AcadPopupMenuItemClass) -> int

Set: EndSubMenuLevel(self: AcadPopupMenuItemClass) = value
"""

    HelpString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpString(self: AcadPopupMenuItemClass) -> str

Set: HelpString(self: AcadPopupMenuItemClass) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: AcadPopupMenuItemClass) -> int

"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: AcadPopupMenuItemClass) -> str

Set: Label(self: AcadPopupMenuItemClass) = value
"""

    Macro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Macro(self: AcadPopupMenuItemClass) -> str

Set: Macro(self: AcadPopupMenuItemClass) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadPopupMenuItemClass) -> AcadPopupMenu

"""

    SubMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubMenu(self: AcadPopupMenuItemClass) -> AcadPopupMenu

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: AcadPopupMenuItemClass) -> str

Set: TagString(self: AcadPopupMenuItemClass) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AcadPopupMenuItemClass) -> AcMenuItemType

"""



class IAcadPopupMenus(IEnumerable):
    # no doc
    def Add(self, MenuName):
        """ Add(self: IAcadPopupMenus, MenuName: str) -> AcadPopupMenu """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadPopupMenus) -> IEnumerator """
        pass

    def InsertMenuInMenuBar(self, MenuName, Index):
        """ InsertMenuInMenuBar(self: IAcadPopupMenus, MenuName: str, Index: object) """
        pass

    def Item(self, Index):
        """ Item(self: IAcadPopupMenus, Index: object) -> AcadPopupMenu """
        pass

    def RemoveMenuFromMenuBar(self, Index):
        """ RemoveMenuFromMenuBar(self: IAcadPopupMenus, Index: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPopupMenus) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadPopupMenus) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadPopupMenus) -> AcadMenuGroup

"""



class AcadPopupMenus(IAcadPopupMenus, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadPopupMenusClass(__ComObject):
    # no doc
    def Add(self, MenuName):
        """ Add(self: AcadPopupMenusClass, MenuName: str) -> AcadPopupMenu """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcadPopupMenusClass) -> IEnumerator """
        pass

    def InsertMenuInMenuBar(self, MenuName, Index):
        """ InsertMenuInMenuBar(self: AcadPopupMenusClass, MenuName: str, Index: object) """
        pass

    def Item(self, Index):
        """ Item(self: AcadPopupMenusClass, Index: object) -> AcadPopupMenu """
        pass

    def RemoveMenuFromMenuBar(self, Index):
        """ RemoveMenuFromMenuBar(self: AcadPopupMenusClass, Index: object) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPopupMenusClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadPopupMenusClass) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadPopupMenusClass) -> AcadMenuGroup

"""



class IAcadPreferences:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferences) -> IAcadApplication

"""

    Display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display(self: IAcadPreferences) -> AcadPreferencesDisplay

"""

    Drafting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Drafting(self: IAcadPreferences) -> AcadPreferencesDrafting

"""

    Files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Files(self: IAcadPreferences) -> AcadPreferencesFiles

"""

    OpenSave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpenSave(self: IAcadPreferences) -> AcadPreferencesOpenSave

"""

    Output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Output(self: IAcadPreferences) -> AcadPreferencesOutput

"""

    Profiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profiles(self: IAcadPreferences) -> AcadPreferencesProfiles

"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection(self: IAcadPreferences) -> AcadPreferencesSelection

"""

    System = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: System(self: IAcadPreferences) -> AcadPreferencesSystem

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: User(self: IAcadPreferences) -> AcadPreferencesUser

"""



class AcadPreferences(IAcadPreferences):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesClass(__ComObject):
    # no doc
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesClass) -> IAcadApplication

"""

    Display = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display(self: AcadPreferencesClass) -> AcadPreferencesDisplay

"""

    Drafting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Drafting(self: AcadPreferencesClass) -> AcadPreferencesDrafting

"""

    Files = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Files(self: AcadPreferencesClass) -> AcadPreferencesFiles

"""

    OpenSave = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OpenSave(self: AcadPreferencesClass) -> AcadPreferencesOpenSave

"""

    Output = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Output(self: AcadPreferencesClass) -> AcadPreferencesOutput

"""

    Profiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Profiles(self: AcadPreferencesClass) -> AcadPreferencesProfiles

"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection(self: AcadPreferencesClass) -> AcadPreferencesSelection

"""

    System = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: System(self: AcadPreferencesClass) -> AcadPreferencesSystem

"""

    User = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: User(self: AcadPreferencesClass) -> AcadPreferencesUser

"""



class IAcadPreferencesDisplay:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesDisplay) -> IAcadApplication

"""

    AutoTrackingVecColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoTrackingVecColor(self: IAcadPreferencesDisplay) -> UInt32

Set: AutoTrackingVecColor(self: IAcadPreferencesDisplay) = value
"""

    CursorSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CursorSize(self: IAcadPreferencesDisplay) -> int

Set: CursorSize(self: IAcadPreferencesDisplay) = value
"""

    DisplayLayoutTabs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayLayoutTabs(self: IAcadPreferencesDisplay) -> bool

Set: DisplayLayoutTabs(self: IAcadPreferencesDisplay) = value
"""

    DisplayScreenMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayScreenMenu(self: IAcadPreferencesDisplay) -> bool

Set: DisplayScreenMenu(self: IAcadPreferencesDisplay) = value
"""

    DisplayScrollBars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayScrollBars(self: IAcadPreferencesDisplay) -> bool

Set: DisplayScrollBars(self: IAcadPreferencesDisplay) = value
"""

    DockedVisibleLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DockedVisibleLines(self: IAcadPreferencesDisplay) -> int

Set: DockedVisibleLines(self: IAcadPreferencesDisplay) = value
"""

    GraphicsWinLayoutBackgrndColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsWinLayoutBackgrndColor(self: IAcadPreferencesDisplay) -> UInt32

Set: GraphicsWinLayoutBackgrndColor(self: IAcadPreferencesDisplay) = value
"""

    GraphicsWinModelBackgrndColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsWinModelBackgrndColor(self: IAcadPreferencesDisplay) -> UInt32

Set: GraphicsWinModelBackgrndColor(self: IAcadPreferencesDisplay) = value
"""

    HistoryLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryLines(self: IAcadPreferencesDisplay) -> int

Set: HistoryLines(self: IAcadPreferencesDisplay) = value
"""

    ImageFrameHighlight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageFrameHighlight(self: IAcadPreferencesDisplay) -> bool

Set: ImageFrameHighlight(self: IAcadPreferencesDisplay) = value
"""

    LayoutCreateViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCreateViewport(self: IAcadPreferencesDisplay) -> bool

Set: LayoutCreateViewport(self: IAcadPreferencesDisplay) = value
"""

    LayoutCrosshairColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCrosshairColor(self: IAcadPreferencesDisplay) -> UInt32

Set: LayoutCrosshairColor(self: IAcadPreferencesDisplay) = value
"""

    LayoutDisplayMargins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutDisplayMargins(self: IAcadPreferencesDisplay) -> bool

Set: LayoutDisplayMargins(self: IAcadPreferencesDisplay) = value
"""

    LayoutDisplayPaper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutDisplayPaper(self: IAcadPreferencesDisplay) -> bool

Set: LayoutDisplayPaper(self: IAcadPreferencesDisplay) = value
"""

    LayoutDisplayPaperShadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutDisplayPaperShadow(self: IAcadPreferencesDisplay) -> bool

Set: LayoutDisplayPaperShadow(self: IAcadPreferencesDisplay) = value
"""

    LayoutShowPlotSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutShowPlotSetup(self: IAcadPreferencesDisplay) -> bool

Set: LayoutShowPlotSetup(self: IAcadPreferencesDisplay) = value
"""

    MaxAutoCADWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxAutoCADWindow(self: IAcadPreferencesDisplay) -> bool

Set: MaxAutoCADWindow(self: IAcadPreferencesDisplay) = value
"""

    ModelCrosshairColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelCrosshairColor(self: IAcadPreferencesDisplay) -> UInt32

Set: ModelCrosshairColor(self: IAcadPreferencesDisplay) = value
"""

    ShowRasterImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowRasterImage(self: IAcadPreferencesDisplay) -> bool

Set: ShowRasterImage(self: IAcadPreferencesDisplay) = value
"""

    TextFont = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFont(self: IAcadPreferencesDisplay) -> str

Set: TextFont(self: IAcadPreferencesDisplay) = value
"""

    TextFontSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFontSize(self: IAcadPreferencesDisplay) -> int

Set: TextFontSize(self: IAcadPreferencesDisplay) = value
"""

    TextFontStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFontStyle(self: IAcadPreferencesDisplay) -> AcTextFontStyle

Set: TextFontStyle(self: IAcadPreferencesDisplay) = value
"""

    TextWinBackgrndColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextWinBackgrndColor(self: IAcadPreferencesDisplay) -> UInt32

Set: TextWinBackgrndColor(self: IAcadPreferencesDisplay) = value
"""

    TextWinTextColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextWinTextColor(self: IAcadPreferencesDisplay) -> UInt32

Set: TextWinTextColor(self: IAcadPreferencesDisplay) = value
"""

    TrueColorImages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrueColorImages(self: IAcadPreferencesDisplay) -> bool

Set: TrueColorImages(self: IAcadPreferencesDisplay) = value
"""

    XRefFadeIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XRefFadeIntensity(self: IAcadPreferencesDisplay) -> int

Set: XRefFadeIntensity(self: IAcadPreferencesDisplay) = value
"""



class AcadPreferencesDisplay(IAcadPreferencesDisplay):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesDisplayClass(__ComObject):
    # no doc
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesDisplayClass) -> IAcadApplication

"""

    AutoTrackingVecColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoTrackingVecColor(self: AcadPreferencesDisplayClass) -> UInt32

Set: AutoTrackingVecColor(self: AcadPreferencesDisplayClass) = value
"""

    CursorSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CursorSize(self: AcadPreferencesDisplayClass) -> int

Set: CursorSize(self: AcadPreferencesDisplayClass) = value
"""

    DisplayLayoutTabs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayLayoutTabs(self: AcadPreferencesDisplayClass) -> bool

Set: DisplayLayoutTabs(self: AcadPreferencesDisplayClass) = value
"""

    DisplayScreenMenu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayScreenMenu(self: AcadPreferencesDisplayClass) -> bool

Set: DisplayScreenMenu(self: AcadPreferencesDisplayClass) = value
"""

    DisplayScrollBars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayScrollBars(self: AcadPreferencesDisplayClass) -> bool

Set: DisplayScrollBars(self: AcadPreferencesDisplayClass) = value
"""

    DockedVisibleLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DockedVisibleLines(self: AcadPreferencesDisplayClass) -> int

Set: DockedVisibleLines(self: AcadPreferencesDisplayClass) = value
"""

    GraphicsWinLayoutBackgrndColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsWinLayoutBackgrndColor(self: AcadPreferencesDisplayClass) -> UInt32

Set: GraphicsWinLayoutBackgrndColor(self: AcadPreferencesDisplayClass) = value
"""

    GraphicsWinModelBackgrndColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsWinModelBackgrndColor(self: AcadPreferencesDisplayClass) -> UInt32

Set: GraphicsWinModelBackgrndColor(self: AcadPreferencesDisplayClass) = value
"""

    HistoryLines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HistoryLines(self: AcadPreferencesDisplayClass) -> int

Set: HistoryLines(self: AcadPreferencesDisplayClass) = value
"""

    ImageFrameHighlight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageFrameHighlight(self: AcadPreferencesDisplayClass) -> bool

Set: ImageFrameHighlight(self: AcadPreferencesDisplayClass) = value
"""

    LayoutCreateViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCreateViewport(self: AcadPreferencesDisplayClass) -> bool

Set: LayoutCreateViewport(self: AcadPreferencesDisplayClass) = value
"""

    LayoutCrosshairColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutCrosshairColor(self: AcadPreferencesDisplayClass) -> UInt32

Set: LayoutCrosshairColor(self: AcadPreferencesDisplayClass) = value
"""

    LayoutDisplayMargins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutDisplayMargins(self: AcadPreferencesDisplayClass) -> bool

Set: LayoutDisplayMargins(self: AcadPreferencesDisplayClass) = value
"""

    LayoutDisplayPaper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutDisplayPaper(self: AcadPreferencesDisplayClass) -> bool

Set: LayoutDisplayPaper(self: AcadPreferencesDisplayClass) = value
"""

    LayoutDisplayPaperShadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutDisplayPaperShadow(self: AcadPreferencesDisplayClass) -> bool

Set: LayoutDisplayPaperShadow(self: AcadPreferencesDisplayClass) = value
"""

    LayoutShowPlotSetup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutShowPlotSetup(self: AcadPreferencesDisplayClass) -> bool

Set: LayoutShowPlotSetup(self: AcadPreferencesDisplayClass) = value
"""

    MaxAutoCADWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxAutoCADWindow(self: AcadPreferencesDisplayClass) -> bool

Set: MaxAutoCADWindow(self: AcadPreferencesDisplayClass) = value
"""

    ModelCrosshairColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelCrosshairColor(self: AcadPreferencesDisplayClass) -> UInt32

Set: ModelCrosshairColor(self: AcadPreferencesDisplayClass) = value
"""

    ShowRasterImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowRasterImage(self: AcadPreferencesDisplayClass) -> bool

Set: ShowRasterImage(self: AcadPreferencesDisplayClass) = value
"""

    TextFont = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFont(self: AcadPreferencesDisplayClass) -> str

Set: TextFont(self: AcadPreferencesDisplayClass) = value
"""

    TextFontSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFontSize(self: AcadPreferencesDisplayClass) -> int

Set: TextFontSize(self: AcadPreferencesDisplayClass) = value
"""

    TextFontStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextFontStyle(self: AcadPreferencesDisplayClass) -> AcTextFontStyle

Set: TextFontStyle(self: AcadPreferencesDisplayClass) = value
"""

    TextWinBackgrndColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextWinBackgrndColor(self: AcadPreferencesDisplayClass) -> UInt32

Set: TextWinBackgrndColor(self: AcadPreferencesDisplayClass) = value
"""

    TextWinTextColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextWinTextColor(self: AcadPreferencesDisplayClass) -> UInt32

Set: TextWinTextColor(self: AcadPreferencesDisplayClass) = value
"""

    TrueColorImages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TrueColorImages(self: AcadPreferencesDisplayClass) -> bool

Set: TrueColorImages(self: AcadPreferencesDisplayClass) = value
"""

    XRefFadeIntensity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XRefFadeIntensity(self: AcadPreferencesDisplayClass) -> int

Set: XRefFadeIntensity(self: AcadPreferencesDisplayClass) = value
"""



class IAcadPreferencesDrafting:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    AlignmentPointAcquisition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentPointAcquisition(self: IAcadPreferencesDrafting) -> AcAlignmentPointAcquisition

Set: AlignmentPointAcquisition(self: IAcadPreferencesDrafting) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesDrafting) -> IAcadApplication

"""

    AutoSnapAperture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapAperture(self: IAcadPreferencesDrafting) -> bool

Set: AutoSnapAperture(self: IAcadPreferencesDrafting) = value
"""

    AutoSnapApertureSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapApertureSize(self: IAcadPreferencesDrafting) -> int

Set: AutoSnapApertureSize(self: IAcadPreferencesDrafting) = value
"""

    AutoSnapMagnet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMagnet(self: IAcadPreferencesDrafting) -> bool

Set: AutoSnapMagnet(self: IAcadPreferencesDrafting) = value
"""

    AutoSnapMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMarker(self: IAcadPreferencesDrafting) -> bool

Set: AutoSnapMarker(self: IAcadPreferencesDrafting) = value
"""

    AutoSnapMarkerColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMarkerColor(self: IAcadPreferencesDrafting) -> AcColor

Set: AutoSnapMarkerColor(self: IAcadPreferencesDrafting) = value
"""

    AutoSnapMarkerSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMarkerSize(self: IAcadPreferencesDrafting) -> int

Set: AutoSnapMarkerSize(self: IAcadPreferencesDrafting) = value
"""

    AutoSnapTooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapTooltip(self: IAcadPreferencesDrafting) -> bool

Set: AutoSnapTooltip(self: IAcadPreferencesDrafting) = value
"""

    AutoTrackTooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoTrackTooltip(self: IAcadPreferencesDrafting) -> bool

Set: AutoTrackTooltip(self: IAcadPreferencesDrafting) = value
"""

    FullScreenTrackingVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullScreenTrackingVector(self: IAcadPreferencesDrafting) -> bool

Set: FullScreenTrackingVector(self: IAcadPreferencesDrafting) = value
"""

    PolarTrackingVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PolarTrackingVector(self: IAcadPreferencesDrafting) -> bool

Set: PolarTrackingVector(self: IAcadPreferencesDrafting) = value
"""



class AcadPreferencesDrafting(IAcadPreferencesDrafting):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesDraftingClass(__ComObject):
    # no doc
    AlignmentPointAcquisition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentPointAcquisition(self: AcadPreferencesDraftingClass) -> AcAlignmentPointAcquisition

Set: AlignmentPointAcquisition(self: AcadPreferencesDraftingClass) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesDraftingClass) -> IAcadApplication

"""

    AutoSnapAperture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapAperture(self: AcadPreferencesDraftingClass) -> bool

Set: AutoSnapAperture(self: AcadPreferencesDraftingClass) = value
"""

    AutoSnapApertureSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapApertureSize(self: AcadPreferencesDraftingClass) -> int

Set: AutoSnapApertureSize(self: AcadPreferencesDraftingClass) = value
"""

    AutoSnapMagnet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMagnet(self: AcadPreferencesDraftingClass) -> bool

Set: AutoSnapMagnet(self: AcadPreferencesDraftingClass) = value
"""

    AutoSnapMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMarker(self: AcadPreferencesDraftingClass) -> bool

Set: AutoSnapMarker(self: AcadPreferencesDraftingClass) = value
"""

    AutoSnapMarkerColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMarkerColor(self: AcadPreferencesDraftingClass) -> AcColor

Set: AutoSnapMarkerColor(self: AcadPreferencesDraftingClass) = value
"""

    AutoSnapMarkerSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapMarkerSize(self: AcadPreferencesDraftingClass) -> int

Set: AutoSnapMarkerSize(self: AcadPreferencesDraftingClass) = value
"""

    AutoSnapTooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSnapTooltip(self: AcadPreferencesDraftingClass) -> bool

Set: AutoSnapTooltip(self: AcadPreferencesDraftingClass) = value
"""

    AutoTrackTooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoTrackTooltip(self: AcadPreferencesDraftingClass) -> bool

Set: AutoTrackTooltip(self: AcadPreferencesDraftingClass) = value
"""

    FullScreenTrackingVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullScreenTrackingVector(self: AcadPreferencesDraftingClass) -> bool

Set: FullScreenTrackingVector(self: AcadPreferencesDraftingClass) = value
"""

    PolarTrackingVector = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PolarTrackingVector(self: AcadPreferencesDraftingClass) -> bool

Set: PolarTrackingVector(self: AcadPreferencesDraftingClass) = value
"""



class IAcadPreferencesFiles:
    # no doc
    def GetProjectFilePath(self, ProjectName):
        """ GetProjectFilePath(self: IAcadPreferencesFiles, ProjectName: str) -> str """
        pass

    def SetProjectFilePath(self, ProjectName, ProjectFilePath):
        """ SetProjectFilePath(self: IAcadPreferencesFiles, ProjectName: str, ProjectFilePath: str) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ActiveInvProject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveInvProject(self: IAcadPreferencesFiles) -> str

Set: ActiveInvProject(self: IAcadPreferencesFiles) = value
"""

    AltFontFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AltFontFile(self: IAcadPreferencesFiles) -> str

Set: AltFontFile(self: IAcadPreferencesFiles) = value
"""

    AltTabletMenuFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AltTabletMenuFile(self: IAcadPreferencesFiles) -> str

Set: AltTabletMenuFile(self: IAcadPreferencesFiles) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesFiles) -> IAcadApplication

"""

    AutoSavePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSavePath(self: IAcadPreferencesFiles) -> str

Set: AutoSavePath(self: IAcadPreferencesFiles) = value
"""

    ColorBookPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorBookPath(self: IAcadPreferencesFiles) -> str

Set: ColorBookPath(self: IAcadPreferencesFiles) = value
"""

    ConfigFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigFile(self: IAcadPreferencesFiles) -> str

"""

    CustomDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomDictionary(self: IAcadPreferencesFiles) -> str

Set: CustomDictionary(self: IAcadPreferencesFiles) = value
"""

    CustomIconPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomIconPath(self: IAcadPreferencesFiles) -> str

Set: CustomIconPath(self: IAcadPreferencesFiles) = value
"""

    DefaultInternetURL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultInternetURL(self: IAcadPreferencesFiles) -> str

Set: DefaultInternetURL(self: IAcadPreferencesFiles) = value
"""

    DriversPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriversPath(self: IAcadPreferencesFiles) -> str

Set: DriversPath(self: IAcadPreferencesFiles) = value
"""

    EnterpriseMenuFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnterpriseMenuFile(self: IAcadPreferencesFiles) -> str

Set: EnterpriseMenuFile(self: IAcadPreferencesFiles) = value
"""

    FontFileMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontFileMap(self: IAcadPreferencesFiles) -> str

Set: FontFileMap(self: IAcadPreferencesFiles) = value
"""

    HelpFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpFilePath(self: IAcadPreferencesFiles) -> str

Set: HelpFilePath(self: IAcadPreferencesFiles) = value
"""

    LicenseServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseServer(self: IAcadPreferencesFiles) -> str

"""

    LogFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogFilePath(self: IAcadPreferencesFiles) -> str

Set: LogFilePath(self: IAcadPreferencesFiles) = value
"""

    MainDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MainDictionary(self: IAcadPreferencesFiles) -> str

Set: MainDictionary(self: IAcadPreferencesFiles) = value
"""

    MenuFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuFile(self: IAcadPreferencesFiles) -> str

Set: MenuFile(self: IAcadPreferencesFiles) = value
"""

    ObjectARXPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectARXPath(self: IAcadPreferencesFiles) -> str

Set: ObjectARXPath(self: IAcadPreferencesFiles) = value
"""

    PageSetupOverridesTemplateFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageSetupOverridesTemplateFile(self: IAcadPreferencesFiles) -> str

Set: PageSetupOverridesTemplateFile(self: IAcadPreferencesFiles) = value
"""

    PlotLogFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLogFilePath(self: IAcadPreferencesFiles) -> str

Set: PlotLogFilePath(self: IAcadPreferencesFiles) = value
"""

    PostScriptPrologFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PostScriptPrologFile(self: IAcadPreferencesFiles) -> str

Set: PostScriptPrologFile(self: IAcadPreferencesFiles) = value
"""

    PrinterConfigPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterConfigPath(self: IAcadPreferencesFiles) -> str

Set: PrinterConfigPath(self: IAcadPreferencesFiles) = value
"""

    PrinterDescPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterDescPath(self: IAcadPreferencesFiles) -> str

Set: PrinterDescPath(self: IAcadPreferencesFiles) = value
"""

    PrinterStyleSheetPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterStyleSheetPath(self: IAcadPreferencesFiles) -> str

Set: PrinterStyleSheetPath(self: IAcadPreferencesFiles) = value
"""

    PrintFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintFile(self: IAcadPreferencesFiles) -> str

Set: PrintFile(self: IAcadPreferencesFiles) = value
"""

    PrintSpoolerPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintSpoolerPath(self: IAcadPreferencesFiles) -> str

Set: PrintSpoolerPath(self: IAcadPreferencesFiles) = value
"""

    PrintSpoolExecutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintSpoolExecutable(self: IAcadPreferencesFiles) -> str

Set: PrintSpoolExecutable(self: IAcadPreferencesFiles) = value
"""

    QNewTemplateFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QNewTemplateFile(self: IAcadPreferencesFiles) -> str

Set: QNewTemplateFile(self: IAcadPreferencesFiles) = value
"""

    SupportPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportPath(self: IAcadPreferencesFiles) -> str

Set: SupportPath(self: IAcadPreferencesFiles) = value
"""

    TempFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempFilePath(self: IAcadPreferencesFiles) -> str

Set: TempFilePath(self: IAcadPreferencesFiles) = value
"""

    TemplateDwgPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemplateDwgPath(self: IAcadPreferencesFiles) -> str

Set: TemplateDwgPath(self: IAcadPreferencesFiles) = value
"""

    TempXrefPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempXrefPath(self: IAcadPreferencesFiles) -> str

Set: TempXrefPath(self: IAcadPreferencesFiles) = value
"""

    TextEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextEditor(self: IAcadPreferencesFiles) -> str

Set: TextEditor(self: IAcadPreferencesFiles) = value
"""

    TextureMapPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextureMapPath(self: IAcadPreferencesFiles) -> str

Set: TextureMapPath(self: IAcadPreferencesFiles) = value
"""

    ToolPalettePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolPalettePath(self: IAcadPreferencesFiles) -> str

Set: ToolPalettePath(self: IAcadPreferencesFiles) = value
"""

    WorkspacePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorkspacePath(self: IAcadPreferencesFiles) -> str

Set: WorkspacePath(self: IAcadPreferencesFiles) = value
"""



class AcadPreferencesFiles(IAcadPreferencesFiles):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesFilesClass(__ComObject):
    # no doc
    def GetProjectFilePath(self, ProjectName):
        """ GetProjectFilePath(self: AcadPreferencesFilesClass, ProjectName: str) -> str """
        pass

    def SetProjectFilePath(self, ProjectName, ProjectFilePath):
        """ SetProjectFilePath(self: AcadPreferencesFilesClass, ProjectName: str, ProjectFilePath: str) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ActiveInvProject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveInvProject(self: AcadPreferencesFilesClass) -> str

Set: ActiveInvProject(self: AcadPreferencesFilesClass) = value
"""

    AltFontFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AltFontFile(self: AcadPreferencesFilesClass) -> str

Set: AltFontFile(self: AcadPreferencesFilesClass) = value
"""

    AltTabletMenuFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AltTabletMenuFile(self: AcadPreferencesFilesClass) -> str

Set: AltTabletMenuFile(self: AcadPreferencesFilesClass) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesFilesClass) -> IAcadApplication

"""

    AutoSavePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSavePath(self: AcadPreferencesFilesClass) -> str

Set: AutoSavePath(self: AcadPreferencesFilesClass) = value
"""

    ColorBookPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorBookPath(self: AcadPreferencesFilesClass) -> str

Set: ColorBookPath(self: AcadPreferencesFilesClass) = value
"""

    ConfigFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConfigFile(self: AcadPreferencesFilesClass) -> str

"""

    CustomDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomDictionary(self: AcadPreferencesFilesClass) -> str

Set: CustomDictionary(self: AcadPreferencesFilesClass) = value
"""

    CustomIconPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomIconPath(self: AcadPreferencesFilesClass) -> str

Set: CustomIconPath(self: AcadPreferencesFilesClass) = value
"""

    DefaultInternetURL = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultInternetURL(self: AcadPreferencesFilesClass) -> str

Set: DefaultInternetURL(self: AcadPreferencesFilesClass) = value
"""

    DriversPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DriversPath(self: AcadPreferencesFilesClass) -> str

Set: DriversPath(self: AcadPreferencesFilesClass) = value
"""

    EnterpriseMenuFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnterpriseMenuFile(self: AcadPreferencesFilesClass) -> str

Set: EnterpriseMenuFile(self: AcadPreferencesFilesClass) = value
"""

    FontFileMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FontFileMap(self: AcadPreferencesFilesClass) -> str

Set: FontFileMap(self: AcadPreferencesFilesClass) = value
"""

    HelpFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpFilePath(self: AcadPreferencesFilesClass) -> str

Set: HelpFilePath(self: AcadPreferencesFilesClass) = value
"""

    LicenseServer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LicenseServer(self: AcadPreferencesFilesClass) -> str

"""

    LogFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogFilePath(self: AcadPreferencesFilesClass) -> str

Set: LogFilePath(self: AcadPreferencesFilesClass) = value
"""

    MainDictionary = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MainDictionary(self: AcadPreferencesFilesClass) -> str

Set: MainDictionary(self: AcadPreferencesFilesClass) = value
"""

    MenuFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MenuFile(self: AcadPreferencesFilesClass) -> str

Set: MenuFile(self: AcadPreferencesFilesClass) = value
"""

    ObjectARXPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectARXPath(self: AcadPreferencesFilesClass) -> str

Set: ObjectARXPath(self: AcadPreferencesFilesClass) = value
"""

    PageSetupOverridesTemplateFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageSetupOverridesTemplateFile(self: AcadPreferencesFilesClass) -> str

Set: PageSetupOverridesTemplateFile(self: AcadPreferencesFilesClass) = value
"""

    PlotLogFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLogFilePath(self: AcadPreferencesFilesClass) -> str

Set: PlotLogFilePath(self: AcadPreferencesFilesClass) = value
"""

    PostScriptPrologFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PostScriptPrologFile(self: AcadPreferencesFilesClass) -> str

Set: PostScriptPrologFile(self: AcadPreferencesFilesClass) = value
"""

    PrinterConfigPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterConfigPath(self: AcadPreferencesFilesClass) -> str

Set: PrinterConfigPath(self: AcadPreferencesFilesClass) = value
"""

    PrinterDescPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterDescPath(self: AcadPreferencesFilesClass) -> str

Set: PrinterDescPath(self: AcadPreferencesFilesClass) = value
"""

    PrinterStyleSheetPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterStyleSheetPath(self: AcadPreferencesFilesClass) -> str

Set: PrinterStyleSheetPath(self: AcadPreferencesFilesClass) = value
"""

    PrintFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintFile(self: AcadPreferencesFilesClass) -> str

Set: PrintFile(self: AcadPreferencesFilesClass) = value
"""

    PrintSpoolerPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintSpoolerPath(self: AcadPreferencesFilesClass) -> str

Set: PrintSpoolerPath(self: AcadPreferencesFilesClass) = value
"""

    PrintSpoolExecutable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintSpoolExecutable(self: AcadPreferencesFilesClass) -> str

Set: PrintSpoolExecutable(self: AcadPreferencesFilesClass) = value
"""

    QNewTemplateFile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QNewTemplateFile(self: AcadPreferencesFilesClass) -> str

Set: QNewTemplateFile(self: AcadPreferencesFilesClass) = value
"""

    SupportPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SupportPath(self: AcadPreferencesFilesClass) -> str

Set: SupportPath(self: AcadPreferencesFilesClass) = value
"""

    TempFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempFilePath(self: AcadPreferencesFilesClass) -> str

Set: TempFilePath(self: AcadPreferencesFilesClass) = value
"""

    TemplateDwgPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemplateDwgPath(self: AcadPreferencesFilesClass) -> str

Set: TemplateDwgPath(self: AcadPreferencesFilesClass) = value
"""

    TempXrefPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempXrefPath(self: AcadPreferencesFilesClass) -> str

Set: TempXrefPath(self: AcadPreferencesFilesClass) = value
"""

    TextEditor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextEditor(self: AcadPreferencesFilesClass) -> str

Set: TextEditor(self: AcadPreferencesFilesClass) = value
"""

    TextureMapPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextureMapPath(self: AcadPreferencesFilesClass) -> str

Set: TextureMapPath(self: AcadPreferencesFilesClass) = value
"""

    ToolPalettePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolPalettePath(self: AcadPreferencesFilesClass) -> str

Set: ToolPalettePath(self: AcadPreferencesFilesClass) = value
"""

    WorkspacePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WorkspacePath(self: AcadPreferencesFilesClass) -> str

Set: WorkspacePath(self: AcadPreferencesFilesClass) = value
"""



class IAcadPreferencesOpenSave:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesOpenSave) -> IAcadApplication

"""

    AutoAudit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoAudit(self: IAcadPreferencesOpenSave) -> bool

Set: AutoAudit(self: IAcadPreferencesOpenSave) = value
"""

    AutoSaveInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSaveInterval(self: IAcadPreferencesOpenSave) -> int

Set: AutoSaveInterval(self: IAcadPreferencesOpenSave) = value
"""

    CreateBackup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateBackup(self: IAcadPreferencesOpenSave) -> bool

Set: CreateBackup(self: IAcadPreferencesOpenSave) = value
"""

    DemandLoadARXApp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DemandLoadARXApp(self: IAcadPreferencesOpenSave) -> AcARXDemandLoad

Set: DemandLoadARXApp(self: IAcadPreferencesOpenSave) = value
"""

    FullCRCValidation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullCRCValidation(self: IAcadPreferencesOpenSave) -> bool

Set: FullCRCValidation(self: IAcadPreferencesOpenSave) = value
"""

    IncrementalSavePercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalSavePercent(self: IAcadPreferencesOpenSave) -> int

Set: IncrementalSavePercent(self: IAcadPreferencesOpenSave) = value
"""

    LogFileOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogFileOn(self: IAcadPreferencesOpenSave) -> bool

Set: LogFileOn(self: IAcadPreferencesOpenSave) = value
"""

    MRUNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MRUNumber(self: IAcadPreferencesOpenSave) -> int

"""

    ProxyImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProxyImage(self: IAcadPreferencesOpenSave) -> AcProxyImage

Set: ProxyImage(self: IAcadPreferencesOpenSave) = value
"""

    SaveAsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SaveAsType(self: IAcadPreferencesOpenSave) -> AcSaveAsType

Set: SaveAsType(self: IAcadPreferencesOpenSave) = value
"""

    SavePreviewThumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SavePreviewThumbnail(self: IAcadPreferencesOpenSave) -> bool

Set: SavePreviewThumbnail(self: IAcadPreferencesOpenSave) = value
"""

    ShowProxyDialogBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProxyDialogBox(self: IAcadPreferencesOpenSave) -> bool

Set: ShowProxyDialogBox(self: IAcadPreferencesOpenSave) = value
"""

    TempFileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempFileExtension(self: IAcadPreferencesOpenSave) -> str

Set: TempFileExtension(self: IAcadPreferencesOpenSave) = value
"""

    XrefDemandLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XrefDemandLoad(self: IAcadPreferencesOpenSave) -> AcXRefDemandLoad

Set: XrefDemandLoad(self: IAcadPreferencesOpenSave) = value
"""



class AcadPreferencesOpenSave(IAcadPreferencesOpenSave):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesOpenSaveClass(__ComObject):
    # no doc
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesOpenSaveClass) -> IAcadApplication

"""

    AutoAudit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoAudit(self: AcadPreferencesOpenSaveClass) -> bool

Set: AutoAudit(self: AcadPreferencesOpenSaveClass) = value
"""

    AutoSaveInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoSaveInterval(self: AcadPreferencesOpenSaveClass) -> int

Set: AutoSaveInterval(self: AcadPreferencesOpenSaveClass) = value
"""

    CreateBackup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateBackup(self: AcadPreferencesOpenSaveClass) -> bool

Set: CreateBackup(self: AcadPreferencesOpenSaveClass) = value
"""

    DemandLoadARXApp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DemandLoadARXApp(self: AcadPreferencesOpenSaveClass) -> AcARXDemandLoad

Set: DemandLoadARXApp(self: AcadPreferencesOpenSaveClass) = value
"""

    FullCRCValidation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullCRCValidation(self: AcadPreferencesOpenSaveClass) -> bool

Set: FullCRCValidation(self: AcadPreferencesOpenSaveClass) = value
"""

    IncrementalSavePercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalSavePercent(self: AcadPreferencesOpenSaveClass) -> int

Set: IncrementalSavePercent(self: AcadPreferencesOpenSaveClass) = value
"""

    LogFileOn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LogFileOn(self: AcadPreferencesOpenSaveClass) -> bool

Set: LogFileOn(self: AcadPreferencesOpenSaveClass) = value
"""

    MRUNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MRUNumber(self: AcadPreferencesOpenSaveClass) -> int

"""

    ProxyImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProxyImage(self: AcadPreferencesOpenSaveClass) -> AcProxyImage

Set: ProxyImage(self: AcadPreferencesOpenSaveClass) = value
"""

    SaveAsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SaveAsType(self: AcadPreferencesOpenSaveClass) -> AcSaveAsType

Set: SaveAsType(self: AcadPreferencesOpenSaveClass) = value
"""

    SavePreviewThumbnail = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SavePreviewThumbnail(self: AcadPreferencesOpenSaveClass) -> bool

Set: SavePreviewThumbnail(self: AcadPreferencesOpenSaveClass) = value
"""

    ShowProxyDialogBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowProxyDialogBox(self: AcadPreferencesOpenSaveClass) -> bool

Set: ShowProxyDialogBox(self: AcadPreferencesOpenSaveClass) = value
"""

    TempFileExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TempFileExtension(self: AcadPreferencesOpenSaveClass) -> str

Set: TempFileExtension(self: AcadPreferencesOpenSaveClass) = value
"""

    XrefDemandLoad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XrefDemandLoad(self: AcadPreferencesOpenSaveClass) -> AcXRefDemandLoad

Set: XrefDemandLoad(self: AcadPreferencesOpenSaveClass) = value
"""



class IAcadPreferencesOutput:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesOutput) -> IAcadApplication

"""

    AutomaticPlotLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticPlotLog(self: IAcadPreferencesOutput) -> bool

Set: AutomaticPlotLog(self: IAcadPreferencesOutput) = value
"""

    ContinuousPlotLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContinuousPlotLog(self: IAcadPreferencesOutput) -> bool

Set: ContinuousPlotLog(self: IAcadPreferencesOutput) = value
"""

    DefaultOutputDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultOutputDevice(self: IAcadPreferencesOutput) -> str

Set: DefaultOutputDevice(self: IAcadPreferencesOutput) = value
"""

    DefaultPlotStyleForLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotStyleForLayer(self: IAcadPreferencesOutput) -> str

Set: DefaultPlotStyleForLayer(self: IAcadPreferencesOutput) = value
"""

    DefaultPlotStyleForObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotStyleForObjects(self: IAcadPreferencesOutput) -> str

Set: DefaultPlotStyleForObjects(self: IAcadPreferencesOutput) = value
"""

    DefaultPlotStyleTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotStyleTable(self: IAcadPreferencesOutput) -> str

Set: DefaultPlotStyleTable(self: IAcadPreferencesOutput) = value
"""

    DefaultPlotToFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotToFilePath(self: IAcadPreferencesOutput) -> str

Set: DefaultPlotToFilePath(self: IAcadPreferencesOutput) = value
"""

    OLEQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OLEQuality(self: IAcadPreferencesOutput) -> AcOleQuality

Set: OLEQuality(self: IAcadPreferencesOutput) = value
"""

    PlotLegacy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLegacy(self: IAcadPreferencesOutput) -> bool

Set: PlotLegacy(self: IAcadPreferencesOutput) = value
"""

    PlotPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotPolicy(self: IAcadPreferencesOutput) -> AcPlotPolicy

Set: PlotPolicy(self: IAcadPreferencesOutput) = value
"""

    PrinterPaperSizeAlert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterPaperSizeAlert(self: IAcadPreferencesOutput) -> bool

Set: PrinterPaperSizeAlert(self: IAcadPreferencesOutput) = value
"""

    PrinterSpoolAlert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterSpoolAlert(self: IAcadPreferencesOutput) -> AcPrinterSpoolAlert

Set: PrinterSpoolAlert(self: IAcadPreferencesOutput) = value
"""

    UseLastPlotSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseLastPlotSettings(self: IAcadPreferencesOutput) -> bool

Set: UseLastPlotSettings(self: IAcadPreferencesOutput) = value
"""



class AcadPreferencesOutput(IAcadPreferencesOutput):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesOutputClass(__ComObject):
    # no doc
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesOutputClass) -> IAcadApplication

"""

    AutomaticPlotLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutomaticPlotLog(self: AcadPreferencesOutputClass) -> bool

Set: AutomaticPlotLog(self: AcadPreferencesOutputClass) = value
"""

    ContinuousPlotLog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContinuousPlotLog(self: AcadPreferencesOutputClass) -> bool

Set: ContinuousPlotLog(self: AcadPreferencesOutputClass) = value
"""

    DefaultOutputDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultOutputDevice(self: AcadPreferencesOutputClass) -> str

Set: DefaultOutputDevice(self: AcadPreferencesOutputClass) = value
"""

    DefaultPlotStyleForLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotStyleForLayer(self: AcadPreferencesOutputClass) -> str

Set: DefaultPlotStyleForLayer(self: AcadPreferencesOutputClass) = value
"""

    DefaultPlotStyleForObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotStyleForObjects(self: AcadPreferencesOutputClass) -> str

Set: DefaultPlotStyleForObjects(self: AcadPreferencesOutputClass) = value
"""

    DefaultPlotStyleTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotStyleTable(self: AcadPreferencesOutputClass) -> str

Set: DefaultPlotStyleTable(self: AcadPreferencesOutputClass) = value
"""

    DefaultPlotToFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultPlotToFilePath(self: AcadPreferencesOutputClass) -> str

Set: DefaultPlotToFilePath(self: AcadPreferencesOutputClass) = value
"""

    OLEQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OLEQuality(self: AcadPreferencesOutputClass) -> AcOleQuality

Set: OLEQuality(self: AcadPreferencesOutputClass) = value
"""

    PlotLegacy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLegacy(self: AcadPreferencesOutputClass) -> bool

Set: PlotLegacy(self: AcadPreferencesOutputClass) = value
"""

    PlotPolicy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotPolicy(self: AcadPreferencesOutputClass) -> AcPlotPolicy

Set: PlotPolicy(self: AcadPreferencesOutputClass) = value
"""

    PrinterPaperSizeAlert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterPaperSizeAlert(self: AcadPreferencesOutputClass) -> bool

Set: PrinterPaperSizeAlert(self: AcadPreferencesOutputClass) = value
"""

    PrinterSpoolAlert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrinterSpoolAlert(self: AcadPreferencesOutputClass) -> AcPrinterSpoolAlert

Set: PrinterSpoolAlert(self: AcadPreferencesOutputClass) = value
"""

    UseLastPlotSettings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseLastPlotSettings(self: AcadPreferencesOutputClass) -> bool

Set: UseLastPlotSettings(self: AcadPreferencesOutputClass) = value
"""



class IAcadPreferencesProfiles:
    # no doc
    def CopyProfile(self, oldProfileName, newProfileName):
        """ CopyProfile(self: IAcadPreferencesProfiles, oldProfileName: str, newProfileName: str) """
        pass

    def DeleteProfile(self, ProfileName):
        """ DeleteProfile(self: IAcadPreferencesProfiles, ProfileName: str) """
        pass

    def ExportProfile(self, ProfileName, RegFile):
        """ ExportProfile(self: IAcadPreferencesProfiles, ProfileName: str, RegFile: str) """
        pass

    def GetAllProfileNames(self, pNames):
        """ GetAllProfileNames(self: IAcadPreferencesProfiles) -> object """
        pass

    def ImportProfile(self, ProfileName, RegFile, IncludePathInfo):
        """ ImportProfile(self: IAcadPreferencesProfiles, ProfileName: str, RegFile: str, IncludePathInfo: bool) """
        pass

    def RenameProfile(self, origProfileName, newProfileName):
        """ RenameProfile(self: IAcadPreferencesProfiles, origProfileName: str, newProfileName: str) """
        pass

    def ResetProfile(self, Profile):
        """ ResetProfile(self: IAcadPreferencesProfiles, Profile: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ActiveProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveProfile(self: IAcadPreferencesProfiles) -> str

Set: ActiveProfile(self: IAcadPreferencesProfiles) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesProfiles) -> IAcadApplication

"""



class AcadPreferencesProfiles(IAcadPreferencesProfiles):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesProfilesClass(__ComObject):
    # no doc
    def CopyProfile(self, oldProfileName, newProfileName):
        """ CopyProfile(self: AcadPreferencesProfilesClass, oldProfileName: str, newProfileName: str) """
        pass

    def DeleteProfile(self, ProfileName):
        """ DeleteProfile(self: AcadPreferencesProfilesClass, ProfileName: str) """
        pass

    def ExportProfile(self, ProfileName, RegFile):
        """ ExportProfile(self: AcadPreferencesProfilesClass, ProfileName: str, RegFile: str) """
        pass

    def GetAllProfileNames(self, pNames):
        """ GetAllProfileNames(self: AcadPreferencesProfilesClass) -> object """
        pass

    def ImportProfile(self, ProfileName, RegFile, IncludePathInfo):
        """ ImportProfile(self: AcadPreferencesProfilesClass, ProfileName: str, RegFile: str, IncludePathInfo: bool) """
        pass

    def RenameProfile(self, origProfileName, newProfileName):
        """ RenameProfile(self: AcadPreferencesProfilesClass, origProfileName: str, newProfileName: str) """
        pass

    def ResetProfile(self, Profile):
        """ ResetProfile(self: AcadPreferencesProfilesClass, Profile: str) """
        pass

    ActiveProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveProfile(self: AcadPreferencesProfilesClass) -> str

Set: ActiveProfile(self: AcadPreferencesProfilesClass) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesProfilesClass) -> IAcadApplication

"""



class IAcadPreferencesSelection:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesSelection) -> IAcadApplication

"""

    DisplayGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayGrips(self: IAcadPreferencesSelection) -> bool

Set: DisplayGrips(self: IAcadPreferencesSelection) = value
"""

    DisplayGripsWithinBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayGripsWithinBlocks(self: IAcadPreferencesSelection) -> bool

Set: DisplayGripsWithinBlocks(self: IAcadPreferencesSelection) = value
"""

    GripColorSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripColorSelected(self: IAcadPreferencesSelection) -> AcColor

Set: GripColorSelected(self: IAcadPreferencesSelection) = value
"""

    GripColorUnselected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripColorUnselected(self: IAcadPreferencesSelection) -> AcColor

Set: GripColorUnselected(self: IAcadPreferencesSelection) = value
"""

    GripSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripSize(self: IAcadPreferencesSelection) -> int

Set: GripSize(self: IAcadPreferencesSelection) = value
"""

    PickAdd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickAdd(self: IAcadPreferencesSelection) -> bool

Set: PickAdd(self: IAcadPreferencesSelection) = value
"""

    PickAuto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickAuto(self: IAcadPreferencesSelection) -> bool

Set: PickAuto(self: IAcadPreferencesSelection) = value
"""

    PickBoxSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickBoxSize(self: IAcadPreferencesSelection) -> int

Set: PickBoxSize(self: IAcadPreferencesSelection) = value
"""

    PickDrag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickDrag(self: IAcadPreferencesSelection) -> bool

Set: PickDrag(self: IAcadPreferencesSelection) = value
"""

    PickFirst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickFirst(self: IAcadPreferencesSelection) -> bool

Set: PickFirst(self: IAcadPreferencesSelection) = value
"""

    PickGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickGroup(self: IAcadPreferencesSelection) -> bool

Set: PickGroup(self: IAcadPreferencesSelection) = value
"""



class AcadPreferencesSelection(IAcadPreferencesSelection):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesSelectionClass(__ComObject):
    # no doc
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesSelectionClass) -> IAcadApplication

"""

    DisplayGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayGrips(self: AcadPreferencesSelectionClass) -> bool

Set: DisplayGrips(self: AcadPreferencesSelectionClass) = value
"""

    DisplayGripsWithinBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayGripsWithinBlocks(self: AcadPreferencesSelectionClass) -> bool

Set: DisplayGripsWithinBlocks(self: AcadPreferencesSelectionClass) = value
"""

    GripColorSelected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripColorSelected(self: AcadPreferencesSelectionClass) -> AcColor

Set: GripColorSelected(self: AcadPreferencesSelectionClass) = value
"""

    GripColorUnselected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripColorUnselected(self: AcadPreferencesSelectionClass) -> AcColor

Set: GripColorUnselected(self: AcadPreferencesSelectionClass) = value
"""

    GripSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GripSize(self: AcadPreferencesSelectionClass) -> int

Set: GripSize(self: AcadPreferencesSelectionClass) = value
"""

    PickAdd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickAdd(self: AcadPreferencesSelectionClass) -> bool

Set: PickAdd(self: AcadPreferencesSelectionClass) = value
"""

    PickAuto = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickAuto(self: AcadPreferencesSelectionClass) -> bool

Set: PickAuto(self: AcadPreferencesSelectionClass) = value
"""

    PickBoxSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickBoxSize(self: AcadPreferencesSelectionClass) -> int

Set: PickBoxSize(self: AcadPreferencesSelectionClass) = value
"""

    PickDrag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickDrag(self: AcadPreferencesSelectionClass) -> bool

Set: PickDrag(self: AcadPreferencesSelectionClass) = value
"""

    PickFirst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickFirst(self: AcadPreferencesSelectionClass) -> bool

Set: PickFirst(self: AcadPreferencesSelectionClass) = value
"""

    PickGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickGroup(self: AcadPreferencesSelectionClass) -> bool

Set: PickGroup(self: AcadPreferencesSelectionClass) = value
"""



class IAcadPreferencesSystem:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesSystem) -> IAcadApplication

"""

    BeepOnError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeepOnError(self: IAcadPreferencesSystem) -> bool

Set: BeepOnError(self: IAcadPreferencesSystem) = value
"""

    DisplayOLEScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOLEScale(self: IAcadPreferencesSystem) -> bool

Set: DisplayOLEScale(self: IAcadPreferencesSystem) = value
"""

    EnableStartupDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableStartupDialog(self: IAcadPreferencesSystem) -> bool

Set: EnableStartupDialog(self: IAcadPreferencesSystem) = value
"""

    LoadAcadLspInAllDocuments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadAcadLspInAllDocuments(self: IAcadPreferencesSystem) -> bool

Set: LoadAcadLspInAllDocuments(self: IAcadPreferencesSystem) = value
"""

    ShowWarningMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowWarningMessages(self: IAcadPreferencesSystem) -> bool

Set: ShowWarningMessages(self: IAcadPreferencesSystem) = value
"""

    SingleDocumentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleDocumentMode(self: IAcadPreferencesSystem) -> bool

Set: SingleDocumentMode(self: IAcadPreferencesSystem) = value
"""

    StoreSQLIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StoreSQLIndex(self: IAcadPreferencesSystem) -> bool

Set: StoreSQLIndex(self: IAcadPreferencesSystem) = value
"""

    TablesReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TablesReadOnly(self: IAcadPreferencesSystem) -> bool

Set: TablesReadOnly(self: IAcadPreferencesSystem) = value
"""



class AcadPreferencesSystem(IAcadPreferencesSystem):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesSystemClass(__ComObject):
    # no doc
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesSystemClass) -> IAcadApplication

"""

    BeepOnError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeepOnError(self: AcadPreferencesSystemClass) -> bool

Set: BeepOnError(self: AcadPreferencesSystemClass) = value
"""

    DisplayOLEScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayOLEScale(self: AcadPreferencesSystemClass) -> bool

Set: DisplayOLEScale(self: AcadPreferencesSystemClass) = value
"""

    EnableStartupDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableStartupDialog(self: AcadPreferencesSystemClass) -> bool

Set: EnableStartupDialog(self: AcadPreferencesSystemClass) = value
"""

    LoadAcadLspInAllDocuments = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LoadAcadLspInAllDocuments(self: AcadPreferencesSystemClass) -> bool

Set: LoadAcadLspInAllDocuments(self: AcadPreferencesSystemClass) = value
"""

    ShowWarningMessages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowWarningMessages(self: AcadPreferencesSystemClass) -> bool

Set: ShowWarningMessages(self: AcadPreferencesSystemClass) = value
"""

    SingleDocumentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleDocumentMode(self: AcadPreferencesSystemClass) -> bool

Set: SingleDocumentMode(self: AcadPreferencesSystemClass) = value
"""

    StoreSQLIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StoreSQLIndex(self: AcadPreferencesSystemClass) -> bool

Set: StoreSQLIndex(self: AcadPreferencesSystemClass) = value
"""

    TablesReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TablesReadOnly(self: AcadPreferencesSystemClass) -> bool

Set: TablesReadOnly(self: AcadPreferencesSystemClass) = value
"""



class IAcadPreferencesUser:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    ADCInsertUnitsDefaultSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ADCInsertUnitsDefaultSource(self: IAcadPreferencesUser) -> AcInsertUnits

Set: ADCInsertUnitsDefaultSource(self: IAcadPreferencesUser) = value
"""

    ADCInsertUnitsDefaultTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ADCInsertUnitsDefaultTarget(self: IAcadPreferencesUser) -> AcInsertUnits

Set: ADCInsertUnitsDefaultTarget(self: IAcadPreferencesUser) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadPreferencesUser) -> IAcadApplication

"""

    HyperlinkDisplayCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HyperlinkDisplayCursor(self: IAcadPreferencesUser) -> bool

Set: HyperlinkDisplayCursor(self: IAcadPreferencesUser) = value
"""

    KeyboardAccelerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyboardAccelerator(self: IAcadPreferencesUser) -> AcKeyboardAccelerator

Set: KeyboardAccelerator(self: IAcadPreferencesUser) = value
"""

    KeyboardPriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyboardPriority(self: IAcadPreferencesUser) -> AcKeyboardPriority

Set: KeyboardPriority(self: IAcadPreferencesUser) = value
"""

    SCMCommandMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMCommandMode(self: IAcadPreferencesUser) -> AcDrawingAreaSCMCommand

Set: SCMCommandMode(self: IAcadPreferencesUser) = value
"""

    SCMDefaultMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMDefaultMode(self: IAcadPreferencesUser) -> AcDrawingAreaSCMDefault

Set: SCMDefaultMode(self: IAcadPreferencesUser) = value
"""

    SCMEditMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMEditMode(self: IAcadPreferencesUser) -> AcDrawingAreaSCMEdit

Set: SCMEditMode(self: IAcadPreferencesUser) = value
"""

    SCMTimeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMTimeMode(self: IAcadPreferencesUser) -> bool

Set: SCMTimeMode(self: IAcadPreferencesUser) = value
"""

    SCMTimeValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMTimeValue(self: IAcadPreferencesUser) -> int

Set: SCMTimeValue(self: IAcadPreferencesUser) = value
"""

    ShortCutMenuDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShortCutMenuDisplay(self: IAcadPreferencesUser) -> bool

Set: ShortCutMenuDisplay(self: IAcadPreferencesUser) = value
"""



class AcadPreferencesUser(IAcadPreferencesUser):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadPreferencesUserClass(__ComObject):
    # no doc
    ADCInsertUnitsDefaultSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ADCInsertUnitsDefaultSource(self: AcadPreferencesUserClass) -> AcInsertUnits

Set: ADCInsertUnitsDefaultSource(self: AcadPreferencesUserClass) = value
"""

    ADCInsertUnitsDefaultTarget = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ADCInsertUnitsDefaultTarget(self: AcadPreferencesUserClass) -> AcInsertUnits

Set: ADCInsertUnitsDefaultTarget(self: AcadPreferencesUserClass) = value
"""

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadPreferencesUserClass) -> IAcadApplication

"""

    HyperlinkDisplayCursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HyperlinkDisplayCursor(self: AcadPreferencesUserClass) -> bool

Set: HyperlinkDisplayCursor(self: AcadPreferencesUserClass) = value
"""

    KeyboardAccelerator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyboardAccelerator(self: AcadPreferencesUserClass) -> AcKeyboardAccelerator

Set: KeyboardAccelerator(self: AcadPreferencesUserClass) = value
"""

    KeyboardPriority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyboardPriority(self: AcadPreferencesUserClass) -> AcKeyboardPriority

Set: KeyboardPriority(self: AcadPreferencesUserClass) = value
"""

    SCMCommandMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMCommandMode(self: AcadPreferencesUserClass) -> AcDrawingAreaSCMCommand

Set: SCMCommandMode(self: AcadPreferencesUserClass) = value
"""

    SCMDefaultMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMDefaultMode(self: AcadPreferencesUserClass) -> AcDrawingAreaSCMDefault

Set: SCMDefaultMode(self: AcadPreferencesUserClass) = value
"""

    SCMEditMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMEditMode(self: AcadPreferencesUserClass) -> AcDrawingAreaSCMEdit

Set: SCMEditMode(self: AcadPreferencesUserClass) = value
"""

    SCMTimeMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMTimeMode(self: AcadPreferencesUserClass) -> bool

Set: SCMTimeMode(self: AcadPreferencesUserClass) = value
"""

    SCMTimeValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SCMTimeValue(self: AcadPreferencesUserClass) -> int

Set: SCMTimeValue(self: AcadPreferencesUserClass) = value
"""

    ShortCutMenuDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShortCutMenuDisplay(self: AcadPreferencesUserClass) -> bool

Set: ShortCutMenuDisplay(self: AcadPreferencesUserClass) = value
"""



class IAcadSelectionSet(IEnumerable):
    # no doc
    def AddItems(self, pSelSet):
        """ AddItems(self: IAcadSelectionSet, pSelSet: object) """
        pass

    def Clear(self):
        """ Clear(self: IAcadSelectionSet) """
        pass

    def Delete(self):
        """ Delete(self: IAcadSelectionSet) """
        pass

    def Erase(self):
        """ Erase(self: IAcadSelectionSet) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadSelectionSet) -> IEnumerator """
        pass

    def Highlight(self, bFlag):
        """ Highlight(self: IAcadSelectionSet, bFlag: bool) """
        pass

    def Item(self, Index):
        """ Item(self: IAcadSelectionSet, Index: object) -> AcadEntity """
        pass

    def RemoveItems(self, Objects):
        """ RemoveItems(self: IAcadSelectionSet, Objects: object) """
        pass

    def Select(self, Mode, Point1, Point2, FilterType, FilterData):
        """ Select(self: IAcadSelectionSet, Mode: AcSelect, Point1: object, Point2: object, FilterType: object, FilterData: object) """
        pass

    def SelectAtPoint(self, Point, FilterType, FilterData):
        """ SelectAtPoint(self: IAcadSelectionSet, Point: object, FilterType: object, FilterData: object) """
        pass

    def SelectByPolygon(self, Mode, PointsList, FilterType, FilterData):
        """ SelectByPolygon(self: IAcadSelectionSet, Mode: AcSelect, PointsList: object, FilterType: object, FilterData: object) """
        pass

    def SelectOnScreen(self, FilterType, FilterData):
        """ SelectOnScreen(self: IAcadSelectionSet, FilterType: object, FilterData: object) """
        pass

    def Update(self):
        """ Update(self: IAcadSelectionSet) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadSelectionSet) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadSelectionSet) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAcadSelectionSet) -> str

"""



class AcadSelectionSet(IAcadSelectionSet, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadSelectionSetClass(__ComObject):
    # no doc
    def AddItems(self, pSelSet):
        """ AddItems(self: AcadSelectionSetClass, pSelSet: object) """
        pass

    def Clear(self):
        """ Clear(self: AcadSelectionSetClass) """
        pass

    def Delete(self):
        """ Delete(self: AcadSelectionSetClass) """
        pass

    def Erase(self):
        """ Erase(self: AcadSelectionSetClass) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcadSelectionSetClass) -> IEnumerator """
        pass

    def Highlight(self, bFlag):
        """ Highlight(self: AcadSelectionSetClass, bFlag: bool) """
        pass

    def Item(self, Index):
        """ Item(self: AcadSelectionSetClass, Index: object) -> AcadEntity """
        pass

    def RemoveItems(self, Objects):
        """ RemoveItems(self: AcadSelectionSetClass, Objects: object) """
        pass

    def Select(self, Mode, Point1, Point2, FilterType, FilterData):
        """ Select(self: AcadSelectionSetClass, Mode: AcSelect, Point1: object, Point2: object, FilterType: object, FilterData: object) """
        pass

    def SelectAtPoint(self, Point, FilterType, FilterData):
        """ SelectAtPoint(self: AcadSelectionSetClass, Point: object, FilterType: object, FilterData: object) """
        pass

    def SelectByPolygon(self, Mode, PointsList, FilterType, FilterData):
        """ SelectByPolygon(self: AcadSelectionSetClass, Mode: AcSelect, PointsList: object, FilterType: object, FilterData: object) """
        pass

    def SelectOnScreen(self, FilterType, FilterData):
        """ SelectOnScreen(self: AcadSelectionSetClass, FilterType: object, FilterData: object) """
        pass

    def Update(self):
        """ Update(self: AcadSelectionSetClass) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadSelectionSetClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadSelectionSetClass) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadSelectionSetClass) -> str

"""



class IAcadSelectionSets(IEnumerable):
    # no doc
    def Add(self, Name):
        """ Add(self: IAcadSelectionSets, Name: str) -> AcadSelectionSet """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadSelectionSets) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: IAcadSelectionSets, Index: object) -> AcadSelectionSet """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadSelectionSets) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadSelectionSets) -> int

"""



class AcadSelectionSets(IAcadSelectionSets, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadSelectionSetsClass(__ComObject):
    # no doc
    def Add(self, Name):
        """ Add(self: AcadSelectionSetsClass, Name: str) -> AcadSelectionSet """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcadSelectionSetsClass) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: AcadSelectionSetsClass, Index: object) -> AcadSelectionSet """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadSelectionSetsClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadSelectionSetsClass) -> int

"""



class IAcadState:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadState) -> IAcadApplication

"""

    IsQuiescent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsQuiescent(self: IAcadState) -> bool

"""



class AcadState(IAcadState):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadStateClass(__ComObject):
    # no doc
    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadStateClass) -> IAcadApplication

"""

    IsQuiescent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsQuiescent(self: AcadStateClass) -> bool

"""



class IAcadToolbar(IEnumerable):
    # no doc
    def AddSeparator(self, Index):
        """ AddSeparator(self: IAcadToolbar, Index: object) -> AcadToolbarItem """
        pass

    def AddToolbarButton(self, Index, Name, HelpString, Macro, FlyoutButton):
        """ AddToolbarButton(self: IAcadToolbar, Index: object, Name: str, HelpString: str, Macro: str, FlyoutButton: object) -> AcadToolbarItem """
        pass

    def Delete(self):
        """ Delete(self: IAcadToolbar) """
        pass

    def Dock(self, Side):
        """ Dock(self: IAcadToolbar, Side: AcToolbarDockStatus) """
        pass

    def Float(self, top, left, NumberFloatRows):
        """ Float(self: IAcadToolbar, top: int, left: int, NumberFloatRows: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadToolbar) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: IAcadToolbar, Index: object) -> AcadToolbarItem """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadToolbar) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadToolbar) -> int

"""

    DockStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DockStatus(self: IAcadToolbar) -> AcToolbarDockStatus

"""

    FloatingRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FloatingRows(self: IAcadToolbar) -> int

Set: FloatingRows(self: IAcadToolbar) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: IAcadToolbar) -> int

"""

    HelpString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpString(self: IAcadToolbar) -> str

Set: HelpString(self: IAcadToolbar) = value
"""

    LargeButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeButtons(self: IAcadToolbar) -> bool

"""

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: left(self: IAcadToolbar) -> int

Set: left(self: IAcadToolbar) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAcadToolbar) -> str

Set: Name(self: IAcadToolbar) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadToolbar) -> object

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: IAcadToolbar) -> str

"""

    top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: top(self: IAcadToolbar) -> int

Set: top(self: IAcadToolbar) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: IAcadToolbar) -> bool

Set: Visible(self: IAcadToolbar) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: IAcadToolbar) -> int

"""



class AcadToolbar(IAcadToolbar, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadToolbarClass(__ComObject):
    # no doc
    def AddSeparator(self, Index):
        """ AddSeparator(self: AcadToolbarClass, Index: object) -> AcadToolbarItem """
        pass

    def AddToolbarButton(self, Index, Name, HelpString, Macro, FlyoutButton):
        """ AddToolbarButton(self: AcadToolbarClass, Index: object, Name: str, HelpString: str, Macro: str, FlyoutButton: object) -> AcadToolbarItem """
        pass

    def Delete(self):
        """ Delete(self: AcadToolbarClass) """
        pass

    def Dock(self, Side):
        """ Dock(self: AcadToolbarClass, Side: AcToolbarDockStatus) """
        pass

    def Float(self, top, left, NumberFloatRows):
        """ Float(self: AcadToolbarClass, top: int, left: int, NumberFloatRows: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcadToolbarClass) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: AcadToolbarClass, Index: object) -> AcadToolbarItem """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadToolbarClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadToolbarClass) -> int

"""

    DockStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DockStatus(self: AcadToolbarClass) -> AcToolbarDockStatus

"""

    FloatingRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FloatingRows(self: AcadToolbarClass) -> int

Set: FloatingRows(self: AcadToolbarClass) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: AcadToolbarClass) -> int

"""

    HelpString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpString(self: AcadToolbarClass) -> str

Set: HelpString(self: AcadToolbarClass) = value
"""

    LargeButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeButtons(self: AcadToolbarClass) -> bool

"""

    left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: left(self: AcadToolbarClass) -> int

Set: left(self: AcadToolbarClass) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadToolbarClass) -> str

Set: Name(self: AcadToolbarClass) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadToolbarClass) -> object

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: AcadToolbarClass) -> str

"""

    top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: top(self: AcadToolbarClass) -> int

Set: top(self: AcadToolbarClass) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: AcadToolbarClass) -> bool

Set: Visible(self: AcadToolbarClass) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: AcadToolbarClass) -> int

"""



class IAcadToolbarItem:
    # no doc
    def AttachToolbarToFlyout(self, MenuGroupName, ToolbarName):
        """ AttachToolbarToFlyout(self: IAcadToolbarItem, MenuGroupName: str, ToolbarName: str) """
        pass

    def Delete(self):
        """ Delete(self: IAcadToolbarItem) """
        pass

    def GetBitmaps(self, SmallIconName, LargeIconName):
        """ GetBitmaps(self: IAcadToolbarItem) -> (str, str) """
        pass

    def SetBitmaps(self, SmallIconName, LargeIconName):
        """ SetBitmaps(self: IAcadToolbarItem, SmallIconName: str, LargeIconName: str) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadToolbarItem) -> IAcadApplication

"""

    CommandDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandDisplayName(self: IAcadToolbarItem) -> str

Set: CommandDisplayName(self: IAcadToolbarItem) = value
"""

    Flyout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flyout(self: IAcadToolbarItem) -> AcadToolbar

"""

    HelpString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpString(self: IAcadToolbarItem) -> str

Set: HelpString(self: IAcadToolbarItem) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: IAcadToolbarItem) -> int

"""

    Macro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Macro(self: IAcadToolbarItem) -> str

Set: Macro(self: IAcadToolbarItem) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IAcadToolbarItem) -> str

Set: Name(self: IAcadToolbarItem) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadToolbarItem) -> AcadToolbar

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: IAcadToolbarItem) -> str

Set: TagString(self: IAcadToolbarItem) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: IAcadToolbarItem) -> AcToolbarItemType

"""



class AcadToolbarItem(IAcadToolbarItem):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadToolbarItemClass(__ComObject):
    # no doc
    def AttachToolbarToFlyout(self, MenuGroupName, ToolbarName):
        """ AttachToolbarToFlyout(self: AcadToolbarItemClass, MenuGroupName: str, ToolbarName: str) """
        pass

    def Delete(self):
        """ Delete(self: AcadToolbarItemClass) """
        pass

    def GetBitmaps(self, SmallIconName, LargeIconName):
        """ GetBitmaps(self: AcadToolbarItemClass) -> (str, str) """
        pass

    def SetBitmaps(self, SmallIconName, LargeIconName):
        """ SetBitmaps(self: AcadToolbarItemClass, SmallIconName: str, LargeIconName: str) """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadToolbarItemClass) -> IAcadApplication

"""

    CommandDisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandDisplayName(self: AcadToolbarItemClass) -> str

Set: CommandDisplayName(self: AcadToolbarItemClass) = value
"""

    Flyout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flyout(self: AcadToolbarItemClass) -> AcadToolbar

"""

    HelpString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HelpString(self: AcadToolbarItemClass) -> str

Set: HelpString(self: AcadToolbarItemClass) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: AcadToolbarItemClass) -> int

"""

    Macro = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Macro(self: AcadToolbarItemClass) -> str

Set: Macro(self: AcadToolbarItemClass) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcadToolbarItemClass) -> str

Set: Name(self: AcadToolbarItemClass) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadToolbarItemClass) -> AcadToolbar

"""

    TagString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TagString(self: AcadToolbarItemClass) -> str

Set: TagString(self: AcadToolbarItemClass) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: AcadToolbarItemClass) -> AcToolbarItemType

"""



class IAcadToolbars(IEnumerable):
    # no doc
    def Add(self, ToolbarName):
        """ Add(self: IAcadToolbars, ToolbarName: str) -> AcadToolbar """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: IAcadToolbars) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: IAcadToolbars, Index: object) -> AcadToolbar """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: IAcadToolbars) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: IAcadToolbars) -> int

"""

    LargeButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeButtons(self: IAcadToolbars) -> bool

Set: LargeButtons(self: IAcadToolbars) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: IAcadToolbars) -> AcadMenuGroup

"""



class AcadToolbars(IAcadToolbars, IEnumerable):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AcadToolbarsClass(__ComObject):
    # no doc
    def Add(self, ToolbarName):
        """ Add(self: AcadToolbarsClass, ToolbarName: str) -> AcadToolbar """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcadToolbarsClass) -> IEnumerator """
        pass

    def Item(self, Index):
        """ Item(self: AcadToolbarsClass, Index: object) -> AcadToolbar """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Application = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Application(self: AcadToolbarsClass) -> IAcadApplication

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcadToolbarsClass) -> int

"""

    LargeButtons = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LargeButtons(self: AcadToolbarsClass) -> bool

Set: LargeButtons(self: AcadToolbarsClass) = value
"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: AcadToolbarsClass) -> AcadMenuGroup

"""



class IAcadUtility:
    # no doc
    def AngleFromXAxis(self, StartPoint, EndPoint):
        """ AngleFromXAxis(self: IAcadUtility, StartPoint: object, EndPoint: object) -> float """
        pass

    def AngleToReal(self, Angle, Unit):
        """ AngleToReal(self: IAcadUtility, Angle: str, Unit: AcAngleUnits) -> float """
        pass

    def AngleToString(self, Angle, Unit, Precision):
        """ AngleToString(self: IAcadUtility, Angle: float, Unit: AcAngleUnits, Precision: int) -> str """
        pass

    def CreateTypedArray(self, varArr, Type, inArgs):
        """ CreateTypedArray(self: IAcadUtility, Type: int, *inArgs: Array[object]) -> object """
        pass

    def DistanceToReal(self, Distance, Unit):
        """ DistanceToReal(self: IAcadUtility, Distance: str, Unit: AcUnits) -> float """
        pass

    def GetAngle(self, Point, Prompt):
        """ GetAngle(self: IAcadUtility, Point: object, Prompt: object) -> float """
        pass

    def GetCorner(self, Point, Prompt):
        """ GetCorner(self: IAcadUtility, Point: object, Prompt: object) -> object """
        pass

    def GetDistance(self, Point, Prompt):
        """ GetDistance(self: IAcadUtility, Point: object, Prompt: object) -> float """
        pass

    def GetEntity(self, Object, PickedPoint, Prompt):
        """ GetEntity(self: IAcadUtility, Prompt: object) -> (object, object) """
        pass

    def GetInput(self):
        """ GetInput(self: IAcadUtility) -> str """
        pass

    def GetInteger(self, Prompt):
        """ GetInteger(self: IAcadUtility, Prompt: object) -> int """
        pass

    def GetKeyword(self, Prompt):
        """ GetKeyword(self: IAcadUtility, Prompt: object) -> str """
        pass

    def GetObjectIdString(self, Object, bHex):
        """ GetObjectIdString(self: IAcadUtility, Object: object, bHex: bool) -> str """
        pass

    def GetOrientation(self, Point, Prompt):
        """ GetOrientation(self: IAcadUtility, Point: object, Prompt: object) -> float """
        pass

    def GetPoint(self, Point, Prompt):
        """ GetPoint(self: IAcadUtility, Point: object, Prompt: object) -> object """
        pass

    def GetReal(self, Prompt):
        """ GetReal(self: IAcadUtility, Prompt: object) -> float """
        pass

    def GetRemoteFile(self, URL, LocalFile, IgnoreCache):
        """ GetRemoteFile(self: IAcadUtility, URL: str, IgnoreCache: bool) -> str """
        pass

    def GetString(self, HasSpaces, Prompt):
        """ GetString(self: IAcadUtility, HasSpaces: int, Prompt: object) -> str """
        pass

    def GetSubEntity(self, Object, PickedPoint, TransMatrix, ContextData, Prompt):
        """ GetSubEntity(self: IAcadUtility, Prompt: object) -> (object, object, object, object) """
        pass

    def InitializeUserInput(self, Bits, KeyWordList):
        """ InitializeUserInput(self: IAcadUtility, Bits: int, KeyWordList: object) """
        pass

    def IsRemoteFile(self, LocalFile, URL):
        """ IsRemoteFile(self: IAcadUtility, LocalFile: str) -> (bool, str) """
        pass

    def IsURL(self, URL):
        """ IsURL(self: IAcadUtility, URL: str) -> bool """
        pass

    def LaunchBrowserDialog(self, SelectedURL, DialogTitle, OpenButtonCaption, StartPageURL, RegistryRootKey, OpenButtonAlwaysEnabled):
        """ LaunchBrowserDialog(self: IAcadUtility, DialogTitle: str, OpenButtonCaption: str, StartPageURL: str, RegistryRootKey: str, OpenButtonAlwaysEnabled: bool) -> (bool, str) """
        pass

    def PolarPoint(self, Point, Angle, Distance):
        """ PolarPoint(self: IAcadUtility, Point: object, Angle: float, Distance: float) -> object """
        pass

    def Prompt(self, Message):
        """ Prompt(self: IAcadUtility, Message: str) """
        pass

    def PutRemoteFile(self, URL, LocalFile):
        """ PutRemoteFile(self: IAcadUtility, URL: str, LocalFile: str) """
        pass

    def RealToString(self, Value, Unit, Precision):
        """ RealToString(self: IAcadUtility, Value: float, Unit: AcUnits, Precision: int) -> str """
        pass

    def SendModelessOperationEnded(self, Context):
        """ SendModelessOperationEnded(self: IAcadUtility, Context: str) """
        pass

    def SendModelessOperationStart(self, Context):
        """ SendModelessOperationStart(self: IAcadUtility, Context: str) """
        pass

    def TranslateCoordinates(self, Point, FromCoordSystem, ToCoordSystem, Displacement, OCSNormal):
        """ TranslateCoordinates(self: IAcadUtility, Point: object, FromCoordSystem: AcCoordinateSystem, ToCoordSystem: AcCoordinateSystem, Displacement: int, OCSNormal: object) -> object """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadUtility(IAcadUtility):
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class AcadUtilityClass(__ComObject):
    # no doc
    def AngleFromXAxis(self, StartPoint, EndPoint):
        """ AngleFromXAxis(self: AcadUtilityClass, StartPoint: object, EndPoint: object) -> float """
        pass

    def AngleToReal(self, Angle, Unit):
        """ AngleToReal(self: AcadUtilityClass, Angle: str, Unit: AcAngleUnits) -> float """
        pass

    def AngleToString(self, Angle, Unit, Precision):
        """ AngleToString(self: AcadUtilityClass, Angle: float, Unit: AcAngleUnits, Precision: int) -> str """
        pass

    def CreateTypedArray(self, varArr, Type, inArgs):
        """ CreateTypedArray(self: AcadUtilityClass, Type: int, *inArgs: Array[object]) -> object """
        pass

    def DistanceToReal(self, Distance, Unit):
        """ DistanceToReal(self: AcadUtilityClass, Distance: str, Unit: AcUnits) -> float """
        pass

    def GetAngle(self, Point, Prompt):
        """ GetAngle(self: AcadUtilityClass, Point: object, Prompt: object) -> float """
        pass

    def GetCorner(self, Point, Prompt):
        """ GetCorner(self: AcadUtilityClass, Point: object, Prompt: object) -> object """
        pass

    def GetDistance(self, Point, Prompt):
        """ GetDistance(self: AcadUtilityClass, Point: object, Prompt: object) -> float """
        pass

    def GetEntity(self, Object, PickedPoint, Prompt):
        """ GetEntity(self: AcadUtilityClass, Prompt: object) -> (object, object) """
        pass

    def GetInput(self):
        """ GetInput(self: AcadUtilityClass) -> str """
        pass

    def GetInteger(self, Prompt):
        """ GetInteger(self: AcadUtilityClass, Prompt: object) -> int """
        pass

    def GetKeyword(self, Prompt):
        """ GetKeyword(self: AcadUtilityClass, Prompt: object) -> str """
        pass

    def GetObjectIdString(self, Object, bHex):
        """ GetObjectIdString(self: AcadUtilityClass, Object: object, bHex: bool) -> str """
        pass

    def GetOrientation(self, Point, Prompt):
        """ GetOrientation(self: AcadUtilityClass, Point: object, Prompt: object) -> float """
        pass

    def GetPoint(self, Point, Prompt):
        """ GetPoint(self: AcadUtilityClass, Point: object, Prompt: object) -> object """
        pass

    def GetReal(self, Prompt):
        """ GetReal(self: AcadUtilityClass, Prompt: object) -> float """
        pass

    def GetRemoteFile(self, URL, LocalFile, IgnoreCache):
        """ GetRemoteFile(self: AcadUtilityClass, URL: str, IgnoreCache: bool) -> str """
        pass

    def GetString(self, HasSpaces, Prompt):
        """ GetString(self: AcadUtilityClass, HasSpaces: int, Prompt: object) -> str """
        pass

    def GetSubEntity(self, Object, PickedPoint, TransMatrix, ContextData, Prompt):
        """ GetSubEntity(self: AcadUtilityClass, Prompt: object) -> (object, object, object, object) """
        pass

    def InitializeUserInput(self, Bits, KeyWordList):
        """ InitializeUserInput(self: AcadUtilityClass, Bits: int, KeyWordList: object) """
        pass

    def IsRemoteFile(self, LocalFile, URL):
        """ IsRemoteFile(self: AcadUtilityClass, LocalFile: str) -> (bool, str) """
        pass

    def IsURL(self, URL):
        """ IsURL(self: AcadUtilityClass, URL: str) -> bool """
        pass

    def LaunchBrowserDialog(self, SelectedURL, DialogTitle, OpenButtonCaption, StartPageURL, RegistryRootKey, OpenButtonAlwaysEnabled):
        """ LaunchBrowserDialog(self: AcadUtilityClass, DialogTitle: str, OpenButtonCaption: str, StartPageURL: str, RegistryRootKey: str, OpenButtonAlwaysEnabled: bool) -> (bool, str) """
        pass

    def PolarPoint(self, Point, Angle, Distance):
        """ PolarPoint(self: AcadUtilityClass, Point: object, Angle: float, Distance: float) -> object """
        pass

    def Prompt(self, Message):
        """ Prompt(self: AcadUtilityClass, Message: str) """
        pass

    def PutRemoteFile(self, URL, LocalFile):
        """ PutRemoteFile(self: AcadUtilityClass, URL: str, LocalFile: str) """
        pass

    def RealToString(self, Value, Unit, Precision):
        """ RealToString(self: AcadUtilityClass, Value: float, Unit: AcUnits, Precision: int) -> str """
        pass

    def SendModelessOperationEnded(self, Context):
        """ SendModelessOperationEnded(self: AcadUtilityClass, Context: str) """
        pass

    def SendModelessOperationStart(self, Context):
        """ SendModelessOperationStart(self: AcadUtilityClass, Context: str) """
        pass

    def TranslateCoordinates(self, Point, FromCoordSystem, ToCoordSystem, Displacement, OCSNormal):
        """ TranslateCoordinates(self: AcadUtilityClass, Point: object, FromCoordSystem: AcCoordinateSystem, ToCoordSystem: AcCoordinateSystem, Displacement: int, OCSNormal: object) -> object """
        pass


class _DAcadApplicationEvents:
    # no doc
    def AppActivate(self):
        """ AppActivate(self: _DAcadApplicationEvents) """
        pass

    def AppDeactivate(self):
        """ AppDeactivate(self: _DAcadApplicationEvents) """
        pass

    def ARXLoaded(self, AppName):
        """ ARXLoaded(self: _DAcadApplicationEvents, AppName: str) """
        pass

    def ARXUnloaded(self, AppName):
        """ ARXUnloaded(self: _DAcadApplicationEvents, AppName: str) """
        pass

    def BeginCommand(self, CommandName):
        """ BeginCommand(self: _DAcadApplicationEvents, CommandName: str) """
        pass

    def BeginFileDrop(self, FileName, Cancel):
        """ BeginFileDrop(self: _DAcadApplicationEvents, FileName: str) -> bool """
        pass

    def BeginLisp(self, FirstLine):
        """ BeginLisp(self: _DAcadApplicationEvents, FirstLine: str) """
        pass

    def BeginModal(self):
        """ BeginModal(self: _DAcadApplicationEvents) """
        pass

    def BeginOpen(self, FileName):
        """ BeginOpen(self: _DAcadApplicationEvents) -> str """
        pass

    def BeginPlot(self, DrawingName):
        """ BeginPlot(self: _DAcadApplicationEvents, DrawingName: str) """
        pass

    def BeginQuit(self, Cancel):
        """ BeginQuit(self: _DAcadApplicationEvents) -> bool """
        pass

    def BeginSave(self, FileName):
        """ BeginSave(self: _DAcadApplicationEvents, FileName: str) """
        pass

    def EndCommand(self, CommandName):
        """ EndCommand(self: _DAcadApplicationEvents, CommandName: str) """
        pass

    def EndLisp(self):
        """ EndLisp(self: _DAcadApplicationEvents) """
        pass

    def EndModal(self):
        """ EndModal(self: _DAcadApplicationEvents) """
        pass

    def EndOpen(self, FileName):
        """ EndOpen(self: _DAcadApplicationEvents, FileName: str) """
        pass

    def EndPlot(self, DrawingName):
        """ EndPlot(self: _DAcadApplicationEvents, DrawingName: str) """
        pass

    def EndSave(self, FileName):
        """ EndSave(self: _DAcadApplicationEvents, FileName: str) """
        pass

    def LispCancelled(self):
        """ LispCancelled(self: _DAcadApplicationEvents) """
        pass

    def NewDrawing(self):
        """ NewDrawing(self: _DAcadApplicationEvents) """
        pass

    def SysVarChanged(self, SysvarName, newVal):
        """ SysVarChanged(self: _DAcadApplicationEvents, SysvarName: str, newVal: object) """
        pass

    def WindowChanged(self, WindowState):
        """ WindowChanged(self: _DAcadApplicationEvents, WindowState: AcWindowState) """
        pass

    def WindowMovedOrResized(self, HWNDFrame, bMoved):
        """ WindowMovedOrResized(self: _DAcadApplicationEvents, HWNDFrame: int, bMoved: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _DAcadApplicationEvents_AppActivateEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_AppActivateEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadApplicationEvents_AppActivateEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_AppDeactivateEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_AppDeactivateEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadApplicationEvents_AppDeactivateEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_ARXLoadedEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_ARXLoadedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, AppName):
        """ Invoke(self: _DAcadApplicationEvents_ARXLoadedEventHandler, AppName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_ARXUnloadedEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_ARXUnloadedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, AppName):
        """ Invoke(self: _DAcadApplicationEvents_ARXUnloadedEventHandler, AppName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginCommandEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginCommandEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, CommandName):
        """ Invoke(self: _DAcadApplicationEvents_BeginCommandEventHandler, CommandName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginFileDropEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginFileDropEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FileName, Cancel):
        """ Invoke(self: _DAcadApplicationEvents_BeginFileDropEventHandler, FileName: str) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginLispEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginLispEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FirstLine):
        """ Invoke(self: _DAcadApplicationEvents_BeginLispEventHandler, FirstLine: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginModalEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginModalEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadApplicationEvents_BeginModalEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginOpenEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginOpenEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FileName):
        """ Invoke(self: _DAcadApplicationEvents_BeginOpenEventHandler) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginPlotEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginPlotEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, DrawingName):
        """ Invoke(self: _DAcadApplicationEvents_BeginPlotEventHandler, DrawingName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginQuitEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginQuitEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, Cancel):
        """ Invoke(self: _DAcadApplicationEvents_BeginQuitEventHandler) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_BeginSaveEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_BeginSaveEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FileName):
        """ Invoke(self: _DAcadApplicationEvents_BeginSaveEventHandler, FileName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_EndCommandEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_EndCommandEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, CommandName):
        """ Invoke(self: _DAcadApplicationEvents_EndCommandEventHandler, CommandName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_EndLispEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_EndLispEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadApplicationEvents_EndLispEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_EndModalEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_EndModalEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadApplicationEvents_EndModalEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_EndOpenEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_EndOpenEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FileName):
        """ Invoke(self: _DAcadApplicationEvents_EndOpenEventHandler, FileName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_EndPlotEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_EndPlotEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, DrawingName):
        """ Invoke(self: _DAcadApplicationEvents_EndPlotEventHandler, DrawingName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_EndSaveEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_EndSaveEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FileName):
        """ Invoke(self: _DAcadApplicationEvents_EndSaveEventHandler, FileName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_LispCancelledEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_LispCancelledEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadApplicationEvents_LispCancelledEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_NewDrawingEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_NewDrawingEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadApplicationEvents_NewDrawingEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_SinkHelper(object):
    # no doc
    def AppActivate(self):
        """ AppActivate(self: _DAcadApplicationEvents_SinkHelper) """
        pass

    def AppDeactivate(self):
        """ AppDeactivate(self: _DAcadApplicationEvents_SinkHelper) """
        pass

    def ARXLoaded(self, A_1):
        """ ARXLoaded(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def ARXUnloaded(self, A_1):
        """ ARXUnloaded(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def BeginCommand(self, A_1):
        """ BeginCommand(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def BeginFileDrop(self, A_1, A_2):
        """ BeginFileDrop(self: _DAcadApplicationEvents_SinkHelper, A_1: str, A_2: bool) -> bool """
        pass

    def BeginLisp(self, A_1):
        """ BeginLisp(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def BeginModal(self):
        """ BeginModal(self: _DAcadApplicationEvents_SinkHelper) """
        pass

    def BeginOpen(self, A_1):
        """ BeginOpen(self: _DAcadApplicationEvents_SinkHelper, A_1: str) -> str """
        pass

    def BeginPlot(self, A_1):
        """ BeginPlot(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def BeginQuit(self, A_1):
        """ BeginQuit(self: _DAcadApplicationEvents_SinkHelper, A_1: bool) -> bool """
        pass

    def BeginSave(self, A_1):
        """ BeginSave(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def EndCommand(self, A_1):
        """ EndCommand(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def EndLisp(self):
        """ EndLisp(self: _DAcadApplicationEvents_SinkHelper) """
        pass

    def EndModal(self):
        """ EndModal(self: _DAcadApplicationEvents_SinkHelper) """
        pass

    def EndOpen(self, A_1):
        """ EndOpen(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def EndPlot(self, A_1):
        """ EndPlot(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def EndSave(self, A_1):
        """ EndSave(self: _DAcadApplicationEvents_SinkHelper, A_1: str) """
        pass

    def LispCancelled(self):
        """ LispCancelled(self: _DAcadApplicationEvents_SinkHelper) """
        pass

    def NewDrawing(self):
        """ NewDrawing(self: _DAcadApplicationEvents_SinkHelper) """
        pass

    def SysVarChanged(self, A_1, A_2):
        """ SysVarChanged(self: _DAcadApplicationEvents_SinkHelper, A_1: str, A_2: object) """
        pass

    def WindowChanged(self, A_1):
        """ WindowChanged(self: _DAcadApplicationEvents_SinkHelper, A_1: AcWindowState) """
        pass

    def WindowMovedOrResized(self, A_1, A_2):
        """ WindowMovedOrResized(self: _DAcadApplicationEvents_SinkHelper, A_1: int, A_2: bool) """
        pass

    m_AppActivateDelegate = None
    m_AppDeactivateDelegate = None
    m_ARXLoadedDelegate = None
    m_ARXUnloadedDelegate = None
    m_BeginCommandDelegate = None
    m_BeginFileDropDelegate = None
    m_BeginLispDelegate = None
    m_BeginModalDelegate = None
    m_BeginOpenDelegate = None
    m_BeginPlotDelegate = None
    m_BeginQuitDelegate = None
    m_BeginSaveDelegate = None
    m_dwCookie = None
    m_EndCommandDelegate = None
    m_EndLispDelegate = None
    m_EndModalDelegate = None
    m_EndOpenDelegate = None
    m_EndPlotDelegate = None
    m_EndSaveDelegate = None
    m_LispCancelledDelegate = None
    m_NewDrawingDelegate = None
    m_SysVarChangedDelegate = None
    m_WindowChangedDelegate = None
    m_WindowMovedOrResizedDelegate = None


class _DAcadApplicationEvents_SysVarChangedEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_SysVarChangedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, SysvarName, newVal):
        """ Invoke(self: _DAcadApplicationEvents_SysVarChangedEventHandler, SysvarName: str, newVal: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_WindowChangedEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_WindowChangedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, WindowState):
        """ Invoke(self: _DAcadApplicationEvents_WindowChangedEventHandler, WindowState: AcWindowState) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadApplicationEvents_WindowMovedOrResizedEventHandler(MulticastDelegate):
    """ _DAcadApplicationEvents_WindowMovedOrResizedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, HWNDFrame, bMoved):
        """ Invoke(self: _DAcadApplicationEvents_WindowMovedOrResizedEventHandler, HWNDFrame: int, bMoved: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents:
    # no doc
    def Activate(self):
        """ Activate(self: _DAcadDocumentEvents) """
        pass

    def BeginClose(self):
        """ BeginClose(self: _DAcadDocumentEvents) """
        pass

    def BeginCommand(self, CommandName):
        """ BeginCommand(self: _DAcadDocumentEvents, CommandName: str) """
        pass

    def BeginDocClose(self, Cancel):
        """ BeginDocClose(self: _DAcadDocumentEvents) -> bool """
        pass

    def BeginDoubleClick(self, PickPoint):
        """ BeginDoubleClick(self: _DAcadDocumentEvents, PickPoint: object) """
        pass

    def BeginLisp(self, FirstLine):
        """ BeginLisp(self: _DAcadDocumentEvents, FirstLine: str) """
        pass

    def BeginPlot(self, DrawingName):
        """ BeginPlot(self: _DAcadDocumentEvents, DrawingName: str) """
        pass

    def BeginRightClick(self, PickPoint):
        """ BeginRightClick(self: _DAcadDocumentEvents, PickPoint: object) """
        pass

    def BeginSave(self, FileName):
        """ BeginSave(self: _DAcadDocumentEvents, FileName: str) """
        pass

    def BeginShortcutMenuCommand(self, ShortcutMenu, Command):
        """ BeginShortcutMenuCommand(self: _DAcadDocumentEvents, Command: str) -> AcadPopupMenu """
        pass

    def BeginShortcutMenuDefault(self, ShortcutMenu):
        """ BeginShortcutMenuDefault(self: _DAcadDocumentEvents) -> AcadPopupMenu """
        pass

    def BeginShortcutMenuEdit(self, ShortcutMenu, SelectionSet):
        """ BeginShortcutMenuEdit(self: _DAcadDocumentEvents) -> (AcadPopupMenu, AcadSelectionSet) """
        pass

    def BeginShortcutMenuGrip(self, ShortcutMenu):
        """ BeginShortcutMenuGrip(self: _DAcadDocumentEvents) -> AcadPopupMenu """
        pass

    def BeginShortcutMenuOsnap(self, ShortcutMenu):
        """ BeginShortcutMenuOsnap(self: _DAcadDocumentEvents) -> AcadPopupMenu """
        pass

    def Deactivate(self):
        """ Deactivate(self: _DAcadDocumentEvents) """
        pass

    def EndCommand(self, CommandName):
        """ EndCommand(self: _DAcadDocumentEvents, CommandName: str) """
        pass

    def EndLisp(self):
        """ EndLisp(self: _DAcadDocumentEvents) """
        pass

    def EndPlot(self, DrawingName):
        """ EndPlot(self: _DAcadDocumentEvents, DrawingName: str) """
        pass

    def EndSave(self, FileName):
        """ EndSave(self: _DAcadDocumentEvents, FileName: str) """
        pass

    def EndShortcutMenu(self, ShortcutMenu):
        """ EndShortcutMenu(self: _DAcadDocumentEvents) -> AcadPopupMenu """
        pass

    def LayoutSwitched(self, LayoutName):
        """ LayoutSwitched(self: _DAcadDocumentEvents, LayoutName: str) """
        pass

    def LispCancelled(self):
        """ LispCancelled(self: _DAcadDocumentEvents) """
        pass

    def ObjectAdded(self, Object):
        """ ObjectAdded(self: _DAcadDocumentEvents, Object: object) """
        pass

    def ObjectErased(self, ObjectId):
        """ ObjectErased(self: _DAcadDocumentEvents, ObjectId: Int64) """
        pass

    def ObjectModified(self, Object):
        """ ObjectModified(self: _DAcadDocumentEvents, Object: object) """
        pass

    def SelectionChanged(self):
        """ SelectionChanged(self: _DAcadDocumentEvents) """
        pass

    def WindowChanged(self, WindowState):
        """ WindowChanged(self: _DAcadDocumentEvents, WindowState: AcWindowState) """
        pass

    def WindowMovedOrResized(self, HWNDFrame, bMoved):
        """ WindowMovedOrResized(self: _DAcadDocumentEvents, HWNDFrame: Int64, bMoved: bool) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class _DAcadDocumentEvents_ActivateEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_ActivateEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadDocumentEvents_ActivateEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginCloseEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginCloseEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadDocumentEvents_BeginCloseEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginCommandEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginCommandEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, CommandName):
        """ Invoke(self: _DAcadDocumentEvents_BeginCommandEventHandler, CommandName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginDocCloseEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginDocCloseEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, Cancel):
        """ Invoke(self: _DAcadDocumentEvents_BeginDocCloseEventHandler) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginDoubleClickEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginDoubleClickEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, PickPoint):
        """ Invoke(self: _DAcadDocumentEvents_BeginDoubleClickEventHandler, PickPoint: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginLispEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginLispEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FirstLine):
        """ Invoke(self: _DAcadDocumentEvents_BeginLispEventHandler, FirstLine: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginPlotEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginPlotEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, DrawingName):
        """ Invoke(self: _DAcadDocumentEvents_BeginPlotEventHandler, DrawingName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginRightClickEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginRightClickEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, PickPoint):
        """ Invoke(self: _DAcadDocumentEvents_BeginRightClickEventHandler, PickPoint: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginSaveEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginSaveEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FileName):
        """ Invoke(self: _DAcadDocumentEvents_BeginSaveEventHandler, FileName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginShortcutMenuCommandEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginShortcutMenuCommandEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, ShortcutMenu, Command):
        """ Invoke(self: _DAcadDocumentEvents_BeginShortcutMenuCommandEventHandler, Command: str) -> AcadPopupMenu """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginShortcutMenuDefaultEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginShortcutMenuDefaultEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, ShortcutMenu):
        """ Invoke(self: _DAcadDocumentEvents_BeginShortcutMenuDefaultEventHandler) -> AcadPopupMenu """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginShortcutMenuEditEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginShortcutMenuEditEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, ShortcutMenu, SelectionSet):
        """ Invoke(self: _DAcadDocumentEvents_BeginShortcutMenuEditEventHandler) -> (AcadPopupMenu, AcadSelectionSet) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginShortcutMenuGripEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginShortcutMenuGripEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, ShortcutMenu):
        """ Invoke(self: _DAcadDocumentEvents_BeginShortcutMenuGripEventHandler) -> AcadPopupMenu """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_BeginShortcutMenuOsnapEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_BeginShortcutMenuOsnapEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, ShortcutMenu):
        """ Invoke(self: _DAcadDocumentEvents_BeginShortcutMenuOsnapEventHandler) -> AcadPopupMenu """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_DeactivateEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_DeactivateEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadDocumentEvents_DeactivateEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_EndCommandEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_EndCommandEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, CommandName):
        """ Invoke(self: _DAcadDocumentEvents_EndCommandEventHandler, CommandName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_EndLispEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_EndLispEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadDocumentEvents_EndLispEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_EndPlotEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_EndPlotEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, DrawingName):
        """ Invoke(self: _DAcadDocumentEvents_EndPlotEventHandler, DrawingName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_EndSaveEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_EndSaveEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, FileName):
        """ Invoke(self: _DAcadDocumentEvents_EndSaveEventHandler, FileName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_EndShortcutMenuEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_EndShortcutMenuEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, ShortcutMenu):
        """ Invoke(self: _DAcadDocumentEvents_EndShortcutMenuEventHandler) -> AcadPopupMenu """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_LayoutSwitchedEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_LayoutSwitchedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, LayoutName):
        """ Invoke(self: _DAcadDocumentEvents_LayoutSwitchedEventHandler, LayoutName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_LispCancelledEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_LispCancelledEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadDocumentEvents_LispCancelledEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_ObjectAddedEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_ObjectAddedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, Object):
        """ Invoke(self: _DAcadDocumentEvents_ObjectAddedEventHandler, Object: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_ObjectErasedEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_ObjectErasedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, ObjectId):
        """ Invoke(self: _DAcadDocumentEvents_ObjectErasedEventHandler, ObjectId: Int64) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_ObjectModifiedEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_ObjectModifiedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, Object):
        """ Invoke(self: _DAcadDocumentEvents_ObjectModifiedEventHandler, Object: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_SelectionChangedEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_SelectionChangedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self):
        """ Invoke(self: _DAcadDocumentEvents_SelectionChangedEventHandler) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_SinkHelper(object):
    # no doc
    def Activate(self):
        """ Activate(self: _DAcadDocumentEvents_SinkHelper) """
        pass

    def BeginClose(self):
        """ BeginClose(self: _DAcadDocumentEvents_SinkHelper) """
        pass

    def BeginCommand(self, A_1):
        """ BeginCommand(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def BeginDocClose(self, A_1):
        """ BeginDocClose(self: _DAcadDocumentEvents_SinkHelper, A_1: bool) -> bool """
        pass

    def BeginDoubleClick(self, A_1):
        """ BeginDoubleClick(self: _DAcadDocumentEvents_SinkHelper, A_1: object) """
        pass

    def BeginLisp(self, A_1):
        """ BeginLisp(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def BeginPlot(self, A_1):
        """ BeginPlot(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def BeginRightClick(self, A_1):
        """ BeginRightClick(self: _DAcadDocumentEvents_SinkHelper, A_1: object) """
        pass

    def BeginSave(self, A_1):
        """ BeginSave(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def BeginShortcutMenuCommand(self, A_1, A_2):
        """ BeginShortcutMenuCommand(self: _DAcadDocumentEvents_SinkHelper, A_1: AcadPopupMenu, A_2: str) -> AcadPopupMenu """
        pass

    def BeginShortcutMenuDefault(self, A_1):
        """ BeginShortcutMenuDefault(self: _DAcadDocumentEvents_SinkHelper, A_1: AcadPopupMenu) -> AcadPopupMenu """
        pass

    def BeginShortcutMenuEdit(self, A_1, A_2):
        """ BeginShortcutMenuEdit(self: _DAcadDocumentEvents_SinkHelper, A_1: AcadPopupMenu, A_2: AcadSelectionSet) -> (AcadPopupMenu, AcadSelectionSet) """
        pass

    def BeginShortcutMenuGrip(self, A_1):
        """ BeginShortcutMenuGrip(self: _DAcadDocumentEvents_SinkHelper, A_1: AcadPopupMenu) -> AcadPopupMenu """
        pass

    def BeginShortcutMenuOsnap(self, A_1):
        """ BeginShortcutMenuOsnap(self: _DAcadDocumentEvents_SinkHelper, A_1: AcadPopupMenu) -> AcadPopupMenu """
        pass

    def Deactivate(self):
        """ Deactivate(self: _DAcadDocumentEvents_SinkHelper) """
        pass

    def EndCommand(self, A_1):
        """ EndCommand(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def EndLisp(self):
        """ EndLisp(self: _DAcadDocumentEvents_SinkHelper) """
        pass

    def EndPlot(self, A_1):
        """ EndPlot(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def EndSave(self, A_1):
        """ EndSave(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def EndShortcutMenu(self, A_1):
        """ EndShortcutMenu(self: _DAcadDocumentEvents_SinkHelper, A_1: AcadPopupMenu) -> AcadPopupMenu """
        pass

    def LayoutSwitched(self, A_1):
        """ LayoutSwitched(self: _DAcadDocumentEvents_SinkHelper, A_1: str) """
        pass

    def LispCancelled(self):
        """ LispCancelled(self: _DAcadDocumentEvents_SinkHelper) """
        pass

    def ObjectAdded(self, A_1):
        """ ObjectAdded(self: _DAcadDocumentEvents_SinkHelper, A_1: object) """
        pass

    def ObjectErased(self, A_1):
        """ ObjectErased(self: _DAcadDocumentEvents_SinkHelper, A_1: Int64) """
        pass

    def ObjectModified(self, A_1):
        """ ObjectModified(self: _DAcadDocumentEvents_SinkHelper, A_1: object) """
        pass

    def SelectionChanged(self):
        """ SelectionChanged(self: _DAcadDocumentEvents_SinkHelper) """
        pass

    def WindowChanged(self, A_1):
        """ WindowChanged(self: _DAcadDocumentEvents_SinkHelper, A_1: AcWindowState) """
        pass

    def WindowMovedOrResized(self, A_1, A_2):
        """ WindowMovedOrResized(self: _DAcadDocumentEvents_SinkHelper, A_1: Int64, A_2: bool) """
        pass

    m_ActivateDelegate = None
    m_BeginCloseDelegate = None
    m_BeginCommandDelegate = None
    m_BeginDocCloseDelegate = None
    m_BeginDoubleClickDelegate = None
    m_BeginLispDelegate = None
    m_BeginPlotDelegate = None
    m_BeginRightClickDelegate = None
    m_BeginSaveDelegate = None
    m_BeginShortcutMenuCommandDelegate = None
    m_BeginShortcutMenuDefaultDelegate = None
    m_BeginShortcutMenuEditDelegate = None
    m_BeginShortcutMenuGripDelegate = None
    m_BeginShortcutMenuOsnapDelegate = None
    m_DeactivateDelegate = None
    m_dwCookie = None
    m_EndCommandDelegate = None
    m_EndLispDelegate = None
    m_EndPlotDelegate = None
    m_EndSaveDelegate = None
    m_EndShortcutMenuDelegate = None
    m_LayoutSwitchedDelegate = None
    m_LispCancelledDelegate = None
    m_ObjectAddedDelegate = None
    m_ObjectErasedDelegate = None
    m_ObjectModifiedDelegate = None
    m_SelectionChangedDelegate = None
    m_WindowChangedDelegate = None
    m_WindowMovedOrResizedDelegate = None


class _DAcadDocumentEvents_WindowChangedEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_WindowChangedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, WindowState):
        """ Invoke(self: _DAcadDocumentEvents_WindowChangedEventHandler, WindowState: AcWindowState) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


class _DAcadDocumentEvents_WindowMovedOrResizedEventHandler(MulticastDelegate):
    """ _DAcadDocumentEvents_WindowMovedOrResizedEventHandler(A_1: object, A_2: UIntPtr) """
    def Invoke(self, HWNDFrame, bMoved):
        """ Invoke(self: _DAcadDocumentEvents_WindowMovedOrResizedEventHandler, HWNDFrame: Int64, bMoved: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_1, A_2):
        """ __new__(cls: type, A_1: object, A_2: UIntPtr) """
        pass


# variables with complex values

