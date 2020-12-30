# encoding: utf-8
# module Autodesk.AutoCAD.EditorInput calls itself EditorInput
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null, accoremgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddedKeywords(Enum):
    """ enum AddedKeywords, values: All (4), CrossingCPolygon (32), Fence (64), Group (1024), Last (128), LastAllPrevious (1), Multiple (16), PickImplied (2), Previous (256), WindowCrossingBoxWPolygonCPolygon (8), WindowWPolygon (512) """
    All = None
    CrossingCPolygon = None
    Fence = None
    Group = None
    Last = None
    LastAllPrevious = None
    Multiple = None
    PickImplied = None
    Previous = None
    value__ = None
    WindowCrossingBoxWPolygonCPolygon = None
    WindowWPolygon = None


class Camera(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    BackClipDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackClipDistance(self: Camera) -> float

"""

    BackClipEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackClipEnabled(self: Camera) -> bool

"""

    FieldOfView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FieldOfView(self: Camera) -> float

"""

    FrontClipDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrontClipDistance(self: Camera) -> float

"""

    FrontClipEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FrontClipEnabled(self: Camera) -> bool

"""

    IsCameraPlottable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCameraPlottable(self: Camera) -> bool

"""

    LensLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LensLength(self: Camera) -> float

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Position(self: Camera) -> Point3d

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: Camera) -> Point3d

"""

    ViewId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewId(self: Camera) -> ObjectId

"""

    ViewTwist = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewTwist(self: Camera) -> float

"""



class ConstraintUtilities(object):
    """ ConstraintUtilities() """
    @staticmethod
    def ShowConstraintBar(subentityPaths, bToShow):
        """ ShowConstraintBar(subentityPaths: Array[FullSubentityPath], bToShow: bool) -> bool """
        pass


class SelectedObject(object):
    """
    SelectedObject(id: ObjectId, subSelections: Array[SelectedSubObject])
    SelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: IntPtr)
    SelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: Int64)
    """
    def GetSubentities(self):
        """ GetSubentities(self: SelectedObject) -> Array[SelectedSubObject] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: SelectedObject, provider: IFormatProvider) -> str
        ToString(self: SelectedObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, *__args):
        """
        __new__(cls: type, id: ObjectId, subSelections: Array[SelectedSubObject])
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: IntPtr)
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: Int64)
        """
        pass

    GraphicsSystemMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsSystemMarker(self: SelectedObject) -> Int64

"""

    GraphicsSystemMarkerPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsSystemMarkerPtr(self: SelectedObject) -> IntPtr

"""

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: SelectedObject) -> ObjectId

"""

    OptionalDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OptionalDetails(self: SelectedObject) -> SelectionDetails

"""

    SelectionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionMethod(self: SelectedObject) -> SelectionMethod

"""



class CrossingOrWindowSelectedObject(SelectedObject):
    """
    CrossingOrWindowSelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: IntPtr)
    CrossingOrWindowSelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: Int64)
    """
    def GetPickPoints(self):
        """ GetPickPoints(self: CrossingOrWindowSelectedObject) -> Array[PickPointDescriptor] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: CrossingOrWindowSelectedObject, provider: IFormatProvider) -> str
        ToString(self: CrossingOrWindowSelectedObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, method, gsMarker):
        """
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: IntPtr)
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: Int64)
        """
        pass


class SelectedSubObject(object):
    """
    SelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr)
    SelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64)
    """
    def ToString(self, provider=None):
        """
        ToString(self: SelectedSubObject, provider: IFormatProvider) -> str
        ToString(self: SelectedSubObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path, method, gsMarker):
        """
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr)
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64)
        """
        pass

    FullSubentityPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullSubentityPath(self: SelectedSubObject) -> FullSubentityPath

"""

    GraphicsSystemMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsSystemMarker(self: SelectedSubObject) -> Int64

"""

    GraphicsSystemMarkerPtr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsSystemMarkerPtr(self: SelectedSubObject) -> IntPtr

"""

    OptionalDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OptionalDetails(self: SelectedSubObject) -> SelectionDetails

"""

    SelectionMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionMethod(self: SelectedSubObject) -> SelectionMethod

"""



class CrossingOrWindowSelectedSubObject(SelectedSubObject):
    """
    CrossingOrWindowSelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr)
    CrossingOrWindowSelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64)
    """
    def GetPickPoints(self):
        """ GetPickPoints(self: CrossingOrWindowSelectedSubObject) -> Array[PickPointDescriptor] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: CrossingOrWindowSelectedSubObject, provider: IFormatProvider) -> str
        ToString(self: CrossingOrWindowSelectedSubObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path, method, gsMarker):
        """
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr)
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64)
        """
        pass


class CursorBadgeUtilities(object):
    """ CursorBadgeUtilities() """
    def AddSupplementalCursorImage(self, cursorImage, priority):
        """ AddSupplementalCursorImage(self: CursorBadgeUtilities, cursorImage: ImageBGRA32, priority: int) -> bool """
        pass

    def GetSupplementalCursorOffset(self, x, y):
        """ GetSupplementalCursorOffset(self: CursorBadgeUtilities, x: int, y: int) -> (int, int) """
        pass

    def HasSupplementalCursorImage(self):
        """ HasSupplementalCursorImage(self: CursorBadgeUtilities) -> bool """
        pass

    def RemoveSupplementalCursorImage(self, cursorImage):
        """ RemoveSupplementalCursorImage(self: CursorBadgeUtilities, cursorImage: ImageBGRA32) -> bool """
        pass

    def SetSupplementalCursorOffset(self, x, y):
        """ SetSupplementalCursorOffset(self: CursorBadgeUtilities, x: int, y: int) """
        pass


class CursorType(Enum):
    """ enum CursorType, values: Crosshair (0), CrosshairNoRotate (6), EntitySelect (8), EntitySelectNoPerspective (10), Invisible (7), NoSpecialCursor (-1), NotRotated (3), Parallelogram (9), PickfirstOrGrips (11), RectangularCursor (1), RotatedCrosshair (5), RubberBand (2), TargetBox (4) """
    Crosshair = None
    CrosshairNoRotate = None
    EntitySelect = None
    EntitySelectNoPerspective = None
    Invisible = None
    NoSpecialCursor = None
    NotRotated = None
    Parallelogram = None
    PickfirstOrGrips = None
    RectangularCursor = None
    RotatedCrosshair = None
    RubberBand = None
    TargetBox = None
    value__ = None


class DeviceInputEventArgs(EventArgs):
    # no doc
    GraphicsSystemMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsSystemMarker(self: DeviceInputEventArgs) -> IntPtr

"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handled(self: DeviceInputEventArgs) -> bool

Set: Handled(self: DeviceInputEventArgs) = value
"""

    LParam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LParam(self: DeviceInputEventArgs) -> IntPtr

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: DeviceInputEventArgs) -> int

"""

    WParam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WParam(self: DeviceInputEventArgs) -> IntPtr

"""



class DeviceInputEventHandler(MulticastDelegate):
    """ DeviceInputEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DeviceInputEventHandler, sender: object, e: DeviceInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DeviceInputEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DeviceInputEventHandler, sender: object, e: DeviceInputEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DisposableSelectionSet(object):
    """ DisposableSelectionSet(selectionSet: SelectionSetDelayMarshalled) """
    def Dispose(self):
        """ Dispose(self: DisposableSelectionSet) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, selectionSet):
        """ __new__(cls: type, selectionSet: SelectionSetDelayMarshalled) """
        pass


class DragCallback(MulticastDelegate):
    """ DragCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, current, xform, callback, obj):
        """ BeginInvoke(self: DragCallback, current: Point3d, callback: AsyncCallback, obj: object) -> (IAsyncResult, Matrix3d) """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DragCallback, result: IAsyncResult) -> SamplerStatus """
        pass

    def Invoke(self, current, xform):
        """ Invoke(self: DragCallback, current: Point3d) -> (SamplerStatus, Matrix3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DragCursor(Enum):
    """ enum DragCursor, values: None (1), Normal (0), Selection (2) """
    None = None
    Normal = None
    Selection = None
    value__ = None


class DraggingEndedEventArgs(EventArgs):
    # no doc
    Offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Offset(self: DraggingEndedEventArgs) -> Vector3d

"""

    PickPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickPoint(self: DraggingEndedEventArgs) -> Point3d

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: DraggingEndedEventArgs) -> PromptStatus

"""



class DraggingEndedEventHandler(MulticastDelegate):
    """ DraggingEndedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DraggingEndedEventHandler, sender: object, e: DraggingEndedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DraggingEndedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DraggingEndedEventHandler, sender: object, e: DraggingEndedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DraggingEventArgs(EventArgs):
    """ DraggingEventArgs(prompt: str) """
    @staticmethod # known case of __new__
    def __new__(self, prompt):
        """ __new__(cls: type, prompt: str) """
        pass

    Prompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Prompt(self: DraggingEventArgs) -> str

"""



class DraggingEventHandler(MulticastDelegate):
    """ DraggingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: DraggingEventHandler, sender: object, e: DraggingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DraggingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: DraggingEventHandler, sender: object, e: DraggingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class Jig(object):
    # no doc
    def GetDynamicDimensionData(self, *args): #cannot find CLR method
        """ GetDynamicDimensionData(self: Jig, dimScale: float) -> DynamicDimensionDataCollection """
        pass

    def OnDimensionValueChanged(self, *args): #cannot find CLR method
        """ OnDimensionValueChanged(self: Jig, e: DynamicDimensionChangedEventArgs) """
        pass

    def Sampler(self, *args): #cannot find CLR method
        """ Sampler(self: Jig, prompts: JigPrompts) -> SamplerStatus """
        pass


class DrawJig(Jig):
    # no doc
    def ViewportDraw(self, *args): #cannot find CLR method
        """ ViewportDraw(self: DrawJig, draw: ViewportDraw) """
        pass

    def WorldDraw(self, *args): #cannot find CLR method
        """ WorldDraw(self: DrawJig, draw: WorldDraw) -> bool """
        pass


class Editor(MarshalByRefObject):
    # no doc
    def ApplyCurDwgLayerTableChanges(self):
        """ ApplyCurDwgLayerTableChanges(self: Editor) """
        pass

    def Command(self, parameter):
        """ Command(self: Editor, *parameter: Array[object]) """
        pass

    def CommandAsync(self, parameter):
        """ CommandAsync(self: Editor, *parameter: Array[object]) -> CommandResult """
        pass

    def DoPrompt(self, opt):
        """ DoPrompt(self: Editor, opt: PromptOptions) -> PromptResult """
        pass

    def Drag(self, *__args):
        """
        Drag(self: Editor, jig: Jig) -> PromptResult
        Drag(self: Editor, selection: SelectionSet, message: str, callback: DragCallback) -> PromptPointResult
        Drag(self: Editor, options: PromptDragOptions) -> PromptPointResult
        """
        pass

    def DrawVector(self, from, to, color, drawHighlighted):
        """ DrawVector(self: Editor, from: Point3d, to: Point3d, color: int, drawHighlighted: bool) """
        pass

    def DrawVectors(self, rb, transform):
        """ DrawVectors(self: Editor, rb: ResultBuffer, transform: Matrix3d) """
        pass

    def GetAngle(self, *__args):
        """
        GetAngle(self: Editor, message: str) -> PromptDoubleResult
        GetAngle(self: Editor, options: PromptAngleOptions) -> PromptDoubleResult
        """
        pass

    def GetCommandVersion(self):
        """ GetCommandVersion(self: Editor) -> int """
        pass

    def GetCorner(self, *__args):
        """
        GetCorner(self: Editor, message: str, basePoint: Point3d) -> PromptPointResult
        GetCorner(self: Editor, options: PromptCornerOptions) -> PromptPointResult
        """
        pass

    def GetCurrentView(self):
        """ GetCurrentView(self: Editor) -> ViewTableRecord """
        pass

    def GetDistance(self, *__args):
        """
        GetDistance(self: Editor, message: str) -> PromptDoubleResult
        GetDistance(self: Editor, options: PromptDistanceOptions) -> PromptDoubleResult
        """
        pass

    def GetDouble(self, *__args):
        """
        GetDouble(self: Editor, message: str) -> PromptDoubleResult
        GetDouble(self: Editor, options: PromptDoubleOptions) -> PromptDoubleResult
        """
        pass

    def GetEntity(self, *__args):
        """
        GetEntity(self: Editor, message: str) -> PromptEntityResult
        GetEntity(self: Editor, options: PromptEntityOptions) -> PromptEntityResult
        """
        pass

    def GetFileNameForOpen(self, *__args):
        """
        GetFileNameForOpen(self: Editor, message: str) -> PromptFileNameResult
        GetFileNameForOpen(self: Editor, options: PromptOpenFileOptions) -> PromptFileNameResult
        """
        pass

    def GetFileNameForSave(self, *__args):
        """
        GetFileNameForSave(self: Editor, message: str) -> PromptFileNameResult
        GetFileNameForSave(self: Editor, options: PromptSaveFileOptions) -> PromptFileNameResult
        """
        pass

    def GetInteger(self, *__args):
        """
        GetInteger(self: Editor, message: str) -> PromptIntegerResult
        GetInteger(self: Editor, options: PromptIntegerOptions) -> PromptIntegerResult
        """
        pass

    def GetKeywords(self, *__args):
        """
        GetKeywords(self: Editor, message: str, *globalKeywords: Array[str]) -> PromptResult
        GetKeywords(self: Editor, options: PromptKeywordOptions) -> PromptResult
        """
        pass

    def GetNestedEntity(self, *__args):
        """
        GetNestedEntity(self: Editor, message: str) -> PromptNestedEntityResult
        GetNestedEntity(self: Editor, options: PromptNestedEntityOptions) -> PromptNestedEntityResult
        """
        pass

    def GetPoint(self, *__args):
        """
        GetPoint(self: Editor, message: str) -> PromptPointResult
        GetPoint(self: Editor, options: PromptPointOptions) -> PromptPointResult
        """
        pass

    def GetSelection(self, *__args):
        """
        GetSelection(self: Editor, filter: SelectionFilter) -> PromptSelectionResult
        GetSelection(self: Editor) -> PromptSelectionResult
        GetSelection(self: Editor, options: PromptSelectionOptions, filter: SelectionFilter) -> PromptSelectionResult
        GetSelection(self: Editor, options: PromptSelectionOptions) -> PromptSelectionResult
        """
        pass

    def GetString(self, *__args):
        """
        GetString(self: Editor, message: str) -> PromptResult
        GetString(self: Editor, options: PromptStringOptions) -> PromptResult
        """
        pass

    def GetViewportNumber(self, point):
        """ GetViewportNumber(self: Editor, point: Point) -> int """
        pass

    def InitCommandVersion(self, nVersion):
        """ InitCommandVersion(self: Editor, nVersion: int) -> int """
        pass

    def PointToScreen(self, pt, viewportNumber):
        """ PointToScreen(self: Editor, pt: Point3d, viewportNumber: int) -> Point """
        pass

    def PointToWorld(self, pt, viewportNumber=None):
        """
        PointToWorld(self: Editor, pt: Point) -> Point3d
        PointToWorld(self: Editor, pt: Point, viewportNumber: int) -> Point3d
        """
        pass

    def PostCommandPrompt(self):
        """ PostCommandPrompt(self: Editor) """
        pass

    def Regen(self):
        """ Regen(self: Editor) """
        pass

    def SelectAll(self, filter=None):
        """
        SelectAll(self: Editor) -> PromptSelectionResult
        SelectAll(self: Editor, filter: SelectionFilter) -> PromptSelectionResult
        """
        pass

    def SelectCrossingPolygon(self, polygon, filter=None):
        """
        SelectCrossingPolygon(self: Editor, polygon: Point3dCollection) -> PromptSelectionResult
        SelectCrossingPolygon(self: Editor, polygon: Point3dCollection, filter: SelectionFilter) -> PromptSelectionResult
        """
        pass

    def SelectCrossingWindow(self, pt1, pt2, filter=None, forceSubEntitySelection=None):
        """
        SelectCrossingWindow(self: Editor, pt1: Point3d, pt2: Point3d) -> PromptSelectionResult
        SelectCrossingWindow(self: Editor, pt1: Point3d, pt2: Point3d, filter: SelectionFilter) -> PromptSelectionResult
        SelectCrossingWindow(self: Editor, pt1: Point3d, pt2: Point3d, filter: SelectionFilter, forceSubEntitySelection: bool) -> PromptSelectionResult
        """
        pass

    def SelectFence(self, fence, filter=None):
        """
        SelectFence(self: Editor, fence: Point3dCollection) -> PromptSelectionResult
        SelectFence(self: Editor, fence: Point3dCollection, filter: SelectionFilter) -> PromptSelectionResult
        """
        pass

    def SelectImplied(self):
        """ SelectImplied(self: Editor) -> PromptSelectionResult """
        pass

    def SelectLast(self):
        """ SelectLast(self: Editor) -> PromptSelectionResult """
        pass

    def SelectPrevious(self):
        """ SelectPrevious(self: Editor) -> PromptSelectionResult """
        pass

    def SelectWindow(self, pt1, pt2, filter=None):
        """
        SelectWindow(self: Editor, pt1: Point3d, pt2: Point3d) -> PromptSelectionResult
        SelectWindow(self: Editor, pt1: Point3d, pt2: Point3d, filter: SelectionFilter) -> PromptSelectionResult
        """
        pass

    def SelectWindowPolygon(self, polygon, filter=None):
        """
        SelectWindowPolygon(self: Editor, polygon: Point3dCollection) -> PromptSelectionResult
        SelectWindowPolygon(self: Editor, polygon: Point3dCollection, filter: SelectionFilter) -> PromptSelectionResult
        """
        pass

    def SetCurrentView(self, value):
        """ SetCurrentView(self: Editor, value: ViewTableRecord) """
        pass

    def SetImpliedSelection(self, *__args):
        """ SetImpliedSelection(self: Editor, selectedObjects: Array[ObjectId])SetImpliedSelection(self: Editor, selectionSet: SelectionSet) """
        pass

    def Snap(self, snapMode, input):
        """ Snap(self: Editor, snapMode: str, input: Point3d) -> Point3d """
        pass

    def StartUserInteraction(self, *__args):
        """
        StartUserInteraction(self: Editor, window: Window) -> EditorUserInteraction
        StartUserInteraction(self: Editor, hwnd: IntPtr) -> EditorUserInteraction
        """
        pass

    def SwitchToModelSpace(self):
        """ SwitchToModelSpace(self: Editor) """
        pass

    def SwitchToPaperSpace(self):
        """ SwitchToPaperSpace(self: Editor) """
        pass

    def TraceBoundary(self, seedPoint, detectIslands):
        """ TraceBoundary(self: Editor, seedPoint: Point3d, detectIslands: bool) -> DBObjectCollection """
        pass

    def TurnForcedPickOff(self):
        """ TurnForcedPickOff(self: Editor) -> int """
        pass

    def TurnForcedPickOn(self):
        """ TurnForcedPickOn(self: Editor) -> int """
        pass

    def TurnSubentityWindowSelectionOff(self):
        """ TurnSubentityWindowSelectionOff(self: Editor) """
        pass

    def TurnSubentityWindowSelectionOn(self):
        """ TurnSubentityWindowSelectionOn(self: Editor) """
        pass

    def UpdateScreen(self):
        """ UpdateScreen(self: Editor) """
        pass

    def UpdateTiledViewportsFromDatabase(self):
        """ UpdateTiledViewportsFromDatabase(self: Editor) """
        pass

    def UpdateTiledViewportsInDatabase(self):
        """ UpdateTiledViewportsInDatabase(self: Editor) """
        pass

    def ViewportIdFromNumber(self, viewportNumber):
        """ ViewportIdFromNumber(self: Editor, viewportNumber: int) -> ObjectId """
        pass

    def WriteMessage(self, message, parameter=None):
        """ WriteMessage(self: Editor, message: str)WriteMessage(self: Editor, message: str, *parameter: Array[object]) """
        pass

    ActiveViewportId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveViewportId(self: Editor) -> ObjectId

"""

    CurrentUserCoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentUserCoordinateSystem(self: Editor) -> Matrix3d

Set: CurrentUserCoordinateSystem(self: Editor) = value
"""

    CurrentViewportObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentViewportObjectId(self: Editor) -> ObjectId

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: Editor) -> Document

"""

    IsDragging = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDragging(self: Editor) -> bool

"""

    IsQuiescent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsQuiescent(self: Editor) -> bool

"""

    IsQuiescentForTransparentCommand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsQuiescentForTransparentCommand(self: Editor) -> bool

"""

    MouseHasMoved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MouseHasMoved(self: Editor) -> bool

"""

    UseCommandLineInterface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseCommandLineInterface(self: Editor) -> bool

"""


    CommandResult = None
    Dragging = None
    DraggingEnded = None
    EnteringQuiescentState = None
    LeavingQuiescentState = None
    PauseToken = '\\'
    PointFilter = None
    PointMonitor = None
    PromptedForAngle = None
    PromptedForCorner = None
    PromptedForDistance = None
    PromptedForDouble = None
    PromptedForEntity = None
    PromptedForInteger = None
    PromptedForKeyword = None
    PromptedForNestedEntity = None
    PromptedForPoint = None
    PromptedForSelection = None
    PromptedForString = None
    PromptForEntityEnding = None
    PromptForSelectionEnding = None
    PromptingForAngle = None
    PromptingForCorner = None
    PromptingForDistance = None
    PromptingForDouble = None
    PromptingForEntity = None
    PromptingForInteger = None
    PromptingForKeyword = None
    PromptingForNestedEntity = None
    PromptingForPoint = None
    PromptingForSelection = None
    PromptingForString = None
    Rollover = None
    SelectionAdded = None
    SelectionRemoved = None


class EditorExtension(object):
    # no doc
    @staticmethod
    def GetViewportNumber(editor, point):
        """ GetViewportNumber(editor: Editor, point: Point) -> int """
        pass

    @staticmethod
    def PointToScreen(editor, pt, viewportNumber):
        """ PointToScreen(editor: Editor, pt: Point3d, viewportNumber: int) -> Point """
        pass

    @staticmethod
    def PointToWorld(editor, pt, viewportNumber=None):
        """
        PointToWorld(editor: Editor, pt: Point) -> Point3d
        PointToWorld(editor: Editor, pt: Point, viewportNumber: int) -> Point3d
        """
        pass

    @staticmethod
    def StartUserInteraction(editor, modalForm):
        """ StartUserInteraction(editor: Editor, modalForm: Control) -> EditorUserInteraction """
        pass

    __all__ = [
        'GetViewportNumber',
        'PointToScreen',
        'PointToWorld',
        'StartUserInteraction',
    ]


class EditorUserInteraction(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: EditorUserInteraction) """
        pass

    def End(self):
        """ End(self: EditorUserInteraction) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass


class EditorVisualStyle(object):
    """ EditorVisualStyle() """
    @staticmethod
    def setCvpVS2d():
        """ setCvpVS2d() """
        pass

    IsVS2dType = True
    IsVS3dType = False


class EntityJig(Jig):
    # no doc
    def Update(self, *args): #cannot find CLR method
        """ Update(self: EntityJig) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, entity: Entity) """
        pass

    Entity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class FenceSelectedObject(SelectedObject):
    """
    FenceSelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: IntPtr, descriptors: Array[PickPointDescriptor])
    FenceSelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: Int64, descriptors: Array[PickPointDescriptor])
    """
    def GetIntersectionPoints(self):
        """ GetIntersectionPoints(self: FenceSelectedObject) -> Array[PickPointDescriptor] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: FenceSelectedObject, provider: IFormatProvider) -> str
        ToString(self: FenceSelectedObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, method, gsMarker, descriptors):
        """
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: IntPtr, descriptors: Array[PickPointDescriptor])
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: Int64, descriptors: Array[PickPointDescriptor])
        """
        pass


class FenceSelectedSubObject(SelectedSubObject):
    """
    FenceSelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr, descriptors: Array[PickPointDescriptor])
    FenceSelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64, descriptors: Array[PickPointDescriptor])
    """
    def GetIntersectionPoints(self):
        """ GetIntersectionPoints(self: FenceSelectedSubObject) -> Array[PickPointDescriptor] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: FenceSelectedSubObject, provider: IFormatProvider) -> str
        ToString(self: FenceSelectedSubObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path, method, gsMarker, descriptors):
        """
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr, descriptors: Array[PickPointDescriptor])
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64, descriptors: Array[PickPointDescriptor])
        """
        pass


class InputPointContext(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: InputPointContext) """
        pass

    def GetAlignmentPaths(self):
        """ GetAlignmentPaths(self: InputPointContext) -> Array[Curve3d] """
        pass

    def GetCustomObjectSnapModes(self):
        """ GetCustomObjectSnapModes(self: InputPointContext) -> Array[CustomObjectSnapMode] """
        pass

    def GetCustomObjectSnapOverrides(self):
        """ GetCustomObjectSnapOverrides(self: InputPointContext) -> Array[CustomObjectSnapMode] """
        pass

    def GetKeyPointEntities(self):
        """ GetKeyPointEntities(self: InputPointContext) -> Array[FullSubentityPath] """
        pass

    def GetPickedEntities(self):
        """ GetPickedEntities(self: InputPointContext) -> Array[FullSubentityPath] """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CartesianSnappedPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CartesianSnappedPoint(self: InputPointContext) -> Point3d

"""

    ComputedPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComputedPoint(self: InputPointContext) -> Point3d

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: InputPointContext) -> Document

"""

    DrawContext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawContext(self: InputPointContext) -> ViewportDraw

"""

    GrippedPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GrippedPoint(self: InputPointContext) -> Point3d

"""

    History = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: History(self: InputPointContext) -> PointHistoryBits

"""

    LastPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastPoint(self: InputPointContext) -> Point3d

"""

    ObjectSnapMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectSnapMask(self: InputPointContext) -> ObjectSnapMasks

"""

    ObjectSnapOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectSnapOverrides(self: InputPointContext) -> ObjectSnapMasks

"""

    ObjectSnappedPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectSnappedPoint(self: InputPointContext) -> Point3d

"""

    PointComputed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointComputed(self: InputPointContext) -> bool

"""

    RawPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RawPoint(self: InputPointContext) -> Point3d

"""

    ToolTipText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTipText(self: InputPointContext) -> str

"""



class PromptOptions(object):
    # no doc
    def DoIt(self, *args): #cannot find CLR method
        """ DoIt(self: PromptOptions) -> PromptResult """
        pass

    def FormatPrompt(self, *args): #cannot find CLR method
        """ FormatPrompt(self: PromptOptions) -> str """
        pass

    def GetDefaultValueString(self, *args): #cannot find CLR method
        """ GetDefaultValueString(self: PromptOptions) -> str """
        pass

    def SetMessageAndKeywords(self, messageAndKeywords, globalKeywords):
        """ SetMessageAndKeywords(self: PromptOptions, messageAndKeywords: str, globalKeywords: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    AppendKeywordsToMessage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppendKeywordsToMessage(self: PromptOptions) -> bool

Set: AppendKeywordsToMessage(self: PromptOptions) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: PromptOptions) -> bool

"""

    Keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keywords(self: PromptOptions) -> KeywordCollection

"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: PromptOptions) -> str

Set: Message(self: PromptOptions) = value
"""



class JigPromptOptions(PromptOptions):
    # no doc
    def CalculateResult(self, *args): #cannot find CLR method
        """ CalculateResult(self: JigPromptOptions, status: DragStatus, result: PromptResult) """
        pass

    def CommonInit(self, *args): #cannot find CLR method
        """ CommonInit(self: JigPromptOptions) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    Cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cursor(self: JigPromptOptions) -> CursorType

Set: Cursor(self: JigPromptOptions) = value
"""

    UserInputControls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserInputControls(self: JigPromptOptions) -> UserInputControls

Set: UserInputControls(self: JigPromptOptions) = value
"""



class JigPromptGeometryOptions(JigPromptOptions):
    """
    JigPromptGeometryOptions(messageAndKeywords: str, globalKeywords: str)
    JigPromptGeometryOptions(message: str)
    JigPromptGeometryOptions()
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    BasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasePoint(self: JigPromptGeometryOptions) -> Point3d

Set: BasePoint(self: JigPromptGeometryOptions) = value
"""

    UseBasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseBasePoint(self: JigPromptGeometryOptions) -> bool

Set: UseBasePoint(self: JigPromptGeometryOptions) = value
"""



class JigPromptAngleOptions(JigPromptGeometryOptions):
    """
    JigPromptAngleOptions(messageAndKeywords: str, globalKeywords: str)
    JigPromptAngleOptions(message: str)
    JigPromptAngleOptions()
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: JigPromptAngleOptions) -> float

Set: DefaultValue(self: JigPromptAngleOptions) = value
"""



class JigPromptDistanceOptions(JigPromptGeometryOptions):
    """
    JigPromptDistanceOptions(messageAndKeywords: str, globalKeywords: str)
    JigPromptDistanceOptions(message: str)
    JigPromptDistanceOptions()
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: JigPromptDistanceOptions) -> float

Set: DefaultValue(self: JigPromptDistanceOptions) = value
"""



class JigPromptPointOptions(JigPromptGeometryOptions):
    """
    JigPromptPointOptions(messageAndKeywords: str, globalKeywords: str)
    JigPromptPointOptions(message: str)
    JigPromptPointOptions()
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: JigPromptPointOptions) -> Point3d

Set: DefaultValue(self: JigPromptPointOptions) = value
"""



class JigPrompts(object):
    # no doc
    def AcquireAngle(self, *__args):
        """
        AcquireAngle(self: JigPrompts) -> PromptDoubleResult
        AcquireAngle(self: JigPrompts, options: JigPromptAngleOptions) -> PromptDoubleResult
        AcquireAngle(self: JigPrompts, messageAndKeywords: str, globalKeywords: str) -> PromptDoubleResult
        AcquireAngle(self: JigPrompts, message: str) -> PromptDoubleResult
        """
        pass

    def AcquireDistance(self, *__args):
        """
        AcquireDistance(self: JigPrompts) -> PromptDoubleResult
        AcquireDistance(self: JigPrompts, options: JigPromptDistanceOptions) -> PromptDoubleResult
        AcquireDistance(self: JigPrompts, messageAndKeywords: str, globalKeywords: str) -> PromptDoubleResult
        AcquireDistance(self: JigPrompts, message: str) -> PromptDoubleResult
        """
        pass

    def AcquirePoint(self, *__args):
        """
        AcquirePoint(self: JigPrompts) -> PromptPointResult
        AcquirePoint(self: JigPrompts, options: JigPromptPointOptions) -> PromptPointResult
        AcquirePoint(self: JigPrompts, messageAndKeywords: str, globalKeywords: str) -> PromptPointResult
        AcquirePoint(self: JigPrompts, message: str) -> PromptPointResult
        """
        pass

    def AcquireString(self, *__args):
        """
        AcquireString(self: JigPrompts) -> PromptResult
        AcquireString(self: JigPrompts, options: JigPromptStringOptions) -> PromptResult
        AcquireString(self: JigPrompts, messageAndKeywords: str, globalKeywords: str) -> PromptResult
        AcquireString(self: JigPrompts, message: str) -> PromptResult
        """
        pass


class JigPromptStringOptions(JigPromptOptions):
    """
    JigPromptStringOptions(messageAndKeywords: str, globalKeywords: str)
    JigPromptStringOptions(message: str)
    JigPromptStringOptions()
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        __new__(cls: type)
        """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: JigPromptStringOptions) -> str

Set: DefaultValue(self: JigPromptStringOptions) = value
"""



class Keyword(object):
    # no doc
    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: Keyword) -> str

Set: DisplayName(self: Keyword) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: Keyword) -> bool

Set: Enabled(self: Keyword) = value
"""

    GlobalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalName(self: Keyword) -> str

Set: GlobalName(self: Keyword) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: Keyword) -> bool

"""

    LocalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalName(self: Keyword) -> str

Set: LocalName(self: Keyword) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: Keyword) -> bool

Set: Visible(self: Keyword) = value
"""



class KeywordCollection(object):
    """ KeywordCollection() """
    def Add(self, globalName, localName=None, displayName=None, visible=None, enabled=None):
        """ Add(self: KeywordCollection, globalName: str, localName: str, displayName: str)Add(self: KeywordCollection, globalName: str, localName: str, displayName: str, visible: bool, enabled: bool)Add(self: KeywordCollection, globalName: str)Add(self: KeywordCollection, globalName: str, localName: str) """
        pass

    def Clear(self):
        """ Clear(self: KeywordCollection) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: KeywordCollection, array: Array[Keyword], index: int) """
        pass

    def GetDisplayString(self, showNoDefault):
        """ GetDisplayString(self: KeywordCollection, showNoDefault: bool) -> str """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: KeywordCollection) -> IEnumerator """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: KeywordCollection) -> int

"""

    Default = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Default(self: KeywordCollection) -> str

Set: Default(self: KeywordCollection) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: KeywordCollection) -> bool

"""



class LivePreview(DisposableWrapper):
    """
    LivePreview()
    LivePreview(doc: Document)
    LivePreview(doc: Document, startPending: bool)
    """
    def AbortAll(self):
        """ AbortAll(self: LivePreview) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EndPreview(self, *__args):
        """ EndPreview(self: LivePreview, delayTime: int)EndPreview(self: LivePreview)EndPreview(self: LivePreview, delayTime: int, bRegen: bool)EndPreview(self: LivePreview, bRegen: bool) """
        pass

    def EndRecording(self):
        """ EndRecording(self: LivePreview) """
        pass

    @staticmethod
    def IsPreviewRecording(doc=None):
        """
        IsPreviewRecording(doc: Document) -> bool
        IsPreviewRecording() -> bool
        """
        pass

    @staticmethod
    def IsPreviewStarted(doc=None):
        """
        IsPreviewStarted(doc: Document) -> bool
        IsPreviewStarted() -> bool
        """
        pass

    def QueueAction(self, action, delayTime=None):
        """ QueueAction(self: LivePreview, action: LivePreviewActionBase)QueueAction(self: LivePreview, action: LivePreviewActionBase, delayTime: int) """
        pass

    def StartRecording(self):
        """ StartRecording(self: LivePreview) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, doc=None, startPending=None):
        """
        __new__(cls: type)
        __new__(cls: type, doc: Document)
        __new__(cls: type, doc: Document, startPending: bool)
        """
        pass

    PreviewEnded = None
    Previewing = None
    PreviewStarted = None
    PreviewWillEnd = None
    PreviewWillStart = None
    RecordingEnded = None
    RecordingStarted = None
    RecordingWillEnd = None
    RecordingWillStart = None


class LivePreviewActionBase(object):
    # no doc
    def Execute(self):
        """ Execute(self: LivePreviewActionBase) """
        pass

    def OnAborted(self):
        """ OnAborted(self: LivePreviewActionBase) """
        pass


class LivePreviewAction(LivePreviewActionBase):
    """ LivePreviewAction(method: Delegate, *args: Array[object]) """
    def Execute(self):
        """ Execute(self: LivePreviewAction) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, method, args):
        """ __new__(cls: type, method: Delegate, *args: Array[object]) """
        pass


class LivePreviewCallback(MulticastDelegate):
    """ LivePreviewCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, callback, obj):
        """ BeginInvoke(self: LivePreviewCallback, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LivePreviewCallback, result: IAsyncResult) """
        pass

    def Invoke(self):
        """ Invoke(self: LivePreviewCallback) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class LivePreviewCommand(LivePreviewActionBase):
    """ LivePreviewCommand(cmd: str) """
    def Execute(self):
        """ Execute(self: LivePreviewCommand) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cmd):
        """ __new__(cls: type, cmd: str) """
        pass


class LivePreviewContextCallback(MulticastDelegate):
    """ LivePreviewContextCallback(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, contextName, contextVal, callback, obj):
        """ BeginInvoke(self: LivePreviewContextCallback, contextName: str, contextVal: object, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LivePreviewContextCallback, result: IAsyncResult) """
        pass

    def Invoke(self, contextName, contextVal):
        """ Invoke(self: LivePreviewContextCallback, contextName: str, contextVal: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class LivePreviewContextParameter(object):
    # no doc
    LivePreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LivePreview(self: LivePreviewContextParameter) -> LivePreview

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: LivePreviewContextParameter) -> LivePreviewContextType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: LivePreviewContextParameter) -> object

"""



class LivePreviewContextProxy(object):
    """ LivePreviewContextProxy(contexName: str, callback: Delegate, *parameters: Array[object]) """
    def Dispose(self):
        """ Dispose(self: LivePreviewContextProxy) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, contexName, callback, parameters):
        """ __new__(cls: type, contexName: str, callback: Delegate, *parameters: Array[object]) """
        pass


class LivePreviewContextType(Enum):
    """ enum LivePreviewContextType, values: EndPreview (0), UpdatePreview (1) """
    EndPreview = None
    UpdatePreview = None
    value__ = None


class LivePreviewDelegate(LivePreviewActionBase):
    """
    LivePreviewDelegate(actCallback: LivePreviewCallback, abortedCallback: LivePreviewCallback)
    LivePreviewDelegate(actCallback: LivePreviewCallback)
    """
    def Execute(self):
        """ Execute(self: LivePreviewDelegate) """
        pass

    def OnAborted(self):
        """ OnAborted(self: LivePreviewDelegate) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, actCallback, abortedCallback=None):
        """
        __new__(cls: type, actCallback: LivePreviewCallback, abortedCallback: LivePreviewCallback)
        __new__(cls: type, actCallback: LivePreviewCallback)
        """
        pass


class LivePreviewEventArgs(EventArgs):
    """
    LivePreviewEventArgs(*parameters: Array[object])
    LivePreviewEventArgs(document: Document, *parameters: Array[object])
    LivePreviewEventArgs()
    """
    def LockDocument(self):
        """ LockDocument(self: LivePreviewEventArgs) -> IDisposable """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, *parameters: Array[object])
        __new__(cls: type, document: Document, *parameters: Array[object])
        __new__(cls: type)
        """
        pass

    AbortPreview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbortPreview(self: LivePreviewEventArgs) -> bool

Set: AbortPreview(self: LivePreviewEventArgs) = value
"""

    CommandParameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandParameter(self: LivePreviewEventArgs) -> object

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: LivePreviewEventArgs) -> Document

"""

    Parameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameters(self: LivePreviewEventArgs) -> Array[object]

"""



class LivePreviewPropertySetting(LivePreviewActionBase):
    """ LivePreviewPropertySetting(prop: PropertyDescriptor, component: object, value: object) """
    def Execute(self):
        """ Execute(self: LivePreviewPropertySetting) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, prop, component, value):
        """ __new__(cls: type, prop: PropertyDescriptor, component: object, value: object) """
        pass


class ObjectSnapMasks(Enum):
    """ enum (flags) ObjectSnapMasks, values: AllowTangent (131072), ApparentIntersection (2048), Center (4), DisablePerpendicular (262144), End (1), Immediate (65536), Insertion (64), Intersection (32), Middle (2), Near (512), Node (8), NoneOverride (2097152), Perpendicular (128), Quadrant (16), Quick (1024), RelativeCartesian (524288), RelativePolar (1048576), Tangent (256) """
    AllowTangent = None
    ApparentIntersection = None
    Center = None
    DisablePerpendicular = None
    End = None
    Immediate = None
    Insertion = None
    Intersection = None
    Middle = None
    Near = None
    Node = None
    NoneOverride = None
    Perpendicular = None
    Quadrant = None
    Quick = None
    RelativeCartesian = None
    RelativePolar = None
    Tangent = None
    value__ = None


class PickPointDescriptor(object):
    """ PickPointDescriptor(kind: PickPointKind, pointOnLine: Point3d, direction: Vector3d) """
    def Equals(self, obj):
        """ Equals(self: PickPointDescriptor, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PickPointDescriptor) -> int """
        pass

    def IsEqualTo(self, a, tolerance=None):
        """
        IsEqualTo(self: PickPointDescriptor, a: PickPointDescriptor, tolerance: Tolerance) -> bool
        IsEqualTo(self: PickPointDescriptor, a: PickPointDescriptor) -> bool
        """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: PickPointDescriptor, provider: IFormatProvider) -> str
        ToString(self: PickPointDescriptor) -> str
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, kind, pointOnLine, direction):
        """
        __new__[PickPointDescriptor]() -> PickPointDescriptor
        
        __new__(cls: type, kind: PickPointKind, pointOnLine: Point3d, direction: Vector3d)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: PickPointDescriptor) -> Vector3d

"""

    Kind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Kind(self: PickPointDescriptor) -> PickPointKind

"""

    PointOnLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointOnLine(self: PickPointDescriptor) -> Point3d

"""



class PickPointKind(Enum):
    """ enum PickPointKind, values: InfiniteLine (0), LineSegment (2), Ray (1) """
    InfiniteLine = None
    LineSegment = None
    Ray = None
    value__ = None


class PickPointSelectedObject(SelectedObject):
    """
    PickPointSelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: IntPtr, descriptor: PickPointDescriptor)
    PickPointSelectedObject(id: ObjectId, method: SelectionMethod, gsMarker: Int64, descriptor: PickPointDescriptor)
    """
    def ToString(self, provider=None):
        """
        ToString(self: PickPointSelectedObject, provider: IFormatProvider) -> str
        ToString(self: PickPointSelectedObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, id, method, gsMarker, descriptor):
        """
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: IntPtr, descriptor: PickPointDescriptor)
        __new__(cls: type, id: ObjectId, method: SelectionMethod, gsMarker: Int64, descriptor: PickPointDescriptor)
        """
        pass

    PickPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickPoint(self: PickPointSelectedObject) -> PickPointDescriptor

"""



class PickPointSelectedSubObject(SelectedSubObject):
    """
    PickPointSelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr, descriptor: PickPointDescriptor)
    PickPointSelectedSubObject(path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64, descriptor: PickPointDescriptor)
    """
    def ToString(self, provider=None):
        """
        ToString(self: PickPointSelectedSubObject, provider: IFormatProvider) -> str
        ToString(self: PickPointSelectedSubObject) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, path, method, gsMarker, descriptor):
        """
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: IntPtr, descriptor: PickPointDescriptor)
        __new__(cls: type, path: FullSubentityPath, method: SelectionMethod, gsMarker: Int64, descriptor: PickPointDescriptor)
        """
        pass

    PickPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickPoint(self: PickPointSelectedSubObject) -> PickPointDescriptor

"""



class PointFilterEventArgs(EventArgs):
    # no doc
    def Dispose(self):
        """ Dispose(self: PointFilterEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CallNext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CallNext(self: PointFilterEventArgs) -> bool

Set: CallNext(self: PointFilterEventArgs) = value
"""

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Context(self: PointFilterEventArgs) -> InputPointContext

"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PointFilterEventArgs) -> PointFilterResult

"""



class PointFilterEventHandler(MulticastDelegate):
    """ PointFilterEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PointFilterEventHandler, sender: object, e: PointFilterEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PointFilterEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PointFilterEventHandler, sender: object, e: PointFilterEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PointFilterResult(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: PointFilterResult) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    DisplayObjectSnapGlyph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayObjectSnapGlyph(self: PointFilterResult) -> bool

Set: DisplayObjectSnapGlyph(self: PointFilterResult) = value
"""

    NewPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewPoint(self: PointFilterResult) -> Point3d

Set: NewPoint(self: PointFilterResult) = value
"""

    Retry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Retry(self: PointFilterResult) -> bool

Set: Retry(self: PointFilterResult) = value
"""

    ToolTipText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolTipText(self: PointFilterResult) -> str

Set: ToolTipText(self: PointFilterResult) = value
"""



class PointHistoryBits(Enum):
    """ enum (flags) PointHistoryBits, values: Aligned (1024), AppFiltered (2048), CartSnapped (16), CoordinatePending (458752), CyclingPoint (64), DidNotPick (0), ForcedPick (4096), FromKeyboard (524288), Gripped (8), LastPoint (4), NotDigitizer (2), NotInteractive (1048576), ObjectSnapped (128), Ortho (32), PickAborted (32768), PickMask (57344), PolarAngle (256), Tablet (1), UsedObjectSnapBox (16384), UsedPickBox (8192), XPending (65536), YPending (131072), ZPending (262144) """
    Aligned = None
    AppFiltered = None
    CartSnapped = None
    CoordinatePending = None
    CyclingPoint = None
    DidNotPick = None
    ForcedPick = None
    FromKeyboard = None
    Gripped = None
    LastPoint = None
    NotDigitizer = None
    NotInteractive = None
    ObjectSnapped = None
    Ortho = None
    PickAborted = None
    PickMask = None
    PolarAngle = None
    Tablet = None
    UsedObjectSnapBox = None
    UsedPickBox = None
    value__ = None
    XPending = None
    YPending = None
    ZPending = None


class PointInputEventArgs(EventArgs):
    # no doc
    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Context(self: PointInputEventArgs) -> InputPointContext

"""

    GraphicsSystemMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphicsSystemMarker(self: PointInputEventArgs) -> IntPtr

"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handled(self: PointInputEventArgs) -> bool

Set: Handled(self: PointInputEventArgs) = value
"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PointInputEventArgs) -> PointFilterResult

"""



class PointInputEventHandler(MulticastDelegate):
    """ PointInputEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PointInputEventHandler, sender: object, e: PointInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PointInputEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PointInputEventHandler, sender: object, e: PointInputEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PointMonitorEventArgs(EventArgs):
    # no doc
    def AppendToolTipText(self, value):
        """ AppendToolTipText(self: PointMonitorEventArgs, value: str) """
        pass

    def Dispose(self):
        """ Dispose(self: PointMonitorEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Context = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Context(self: PointMonitorEventArgs) -> InputPointContext

"""



class PointMonitorEventHandler(MulticastDelegate):
    """ PointMonitorEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PointMonitorEventHandler, sender: object, e: PointMonitorEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PointMonitorEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PointMonitorEventHandler, sender: object, e: PointMonitorEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptEditorOptions(PromptOptions):
    # no doc
    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass


class PromptAngleOptions(PromptEditorOptions):
    """
    PromptAngleOptions(messageAndKeywords: str, globalKeywords: str)
    PromptAngleOptions(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    AllowArbitraryInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowArbitraryInput(self: PromptAngleOptions) -> bool

Set: AllowArbitraryInput(self: PromptAngleOptions) = value
"""

    AllowNone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNone(self: PromptAngleOptions) -> bool

Set: AllowNone(self: PromptAngleOptions) = value
"""

    AllowZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowZero(self: PromptAngleOptions) -> bool

Set: AllowZero(self: PromptAngleOptions) = value
"""

    BasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasePoint(self: PromptAngleOptions) -> Point3d

Set: BasePoint(self: PromptAngleOptions) = value
"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: PromptAngleOptions) -> float

Set: DefaultValue(self: PromptAngleOptions) = value
"""

    UseAngleBase = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseAngleBase(self: PromptAngleOptions) -> bool

Set: UseAngleBase(self: PromptAngleOptions) = value
"""

    UseBasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseBasePoint(self: PromptAngleOptions) -> bool

Set: UseBasePoint(self: PromptAngleOptions) = value
"""

    UseDashedLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDashedLine(self: PromptAngleOptions) -> bool

Set: UseDashedLine(self: PromptAngleOptions) = value
"""

    UseDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultValue(self: PromptAngleOptions) -> bool

Set: UseDefaultValue(self: PromptAngleOptions) = value
"""



class PromptAngleOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptAngleOptionsEventArgs) -> PromptAngleOptions

"""



class PromptAngleOptionsEventHandler(MulticastDelegate):
    """ PromptAngleOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptAngleOptionsEventHandler, sender: object, e: PromptAngleOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptAngleOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptAngleOptionsEventHandler, sender: object, e: PromptAngleOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptCornerOptions(PromptEditorOptions):
    """
    PromptCornerOptions(messageAndKeywords: str, globalKeywords: str, basePoint: Point3d)
    PromptCornerOptions(message: str, basePoint: Point3d)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str, basePoint: Point3d)
        __new__(cls: type, message: str, basePoint: Point3d)
        """
        pass

    AllowArbitraryInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowArbitraryInput(self: PromptCornerOptions) -> bool

Set: AllowArbitraryInput(self: PromptCornerOptions) = value
"""

    AllowNone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNone(self: PromptCornerOptions) -> bool

Set: AllowNone(self: PromptCornerOptions) = value
"""

    BasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasePoint(self: PromptCornerOptions) -> Point3d

Set: BasePoint(self: PromptCornerOptions) = value
"""

    LimitsChecked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LimitsChecked(self: PromptCornerOptions) -> bool

Set: LimitsChecked(self: PromptCornerOptions) = value
"""

    UseDashedLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDashedLine(self: PromptCornerOptions) -> bool

Set: UseDashedLine(self: PromptCornerOptions) = value
"""



class PromptNumericalOptions(PromptEditorOptions):
    # no doc
    AllowArbitraryInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowArbitraryInput(self: PromptNumericalOptions) -> bool

Set: AllowArbitraryInput(self: PromptNumericalOptions) = value
"""

    AllowNegative = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNegative(self: PromptNumericalOptions) -> bool

Set: AllowNegative(self: PromptNumericalOptions) = value
"""

    AllowNone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNone(self: PromptNumericalOptions) -> bool

Set: AllowNone(self: PromptNumericalOptions) = value
"""

    AllowZero = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowZero(self: PromptNumericalOptions) -> bool

Set: AllowZero(self: PromptNumericalOptions) = value
"""

    UseDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultValue(self: PromptNumericalOptions) -> bool

Set: UseDefaultValue(self: PromptNumericalOptions) = value
"""



class PromptDistanceOptions(PromptNumericalOptions):
    """
    PromptDistanceOptions(messageAndKeywords: str, globalKeywords: str)
    PromptDistanceOptions(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    BasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BasePoint(self: PromptDistanceOptions) -> Point3d

Set: BasePoint(self: PromptDistanceOptions) = value
"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: PromptDistanceOptions) -> float

Set: DefaultValue(self: PromptDistanceOptions) = value
"""

    Only2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Only2d(self: PromptDistanceOptions) -> bool

Set: Only2d(self: PromptDistanceOptions) = value
"""

    UseBasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseBasePoint(self: PromptDistanceOptions) -> bool

Set: UseBasePoint(self: PromptDistanceOptions) = value
"""

    UseDashedLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDashedLine(self: PromptDistanceOptions) -> bool

Set: UseDashedLine(self: PromptDistanceOptions) = value
"""



class PromptDistanceOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptDistanceOptionsEventArgs) -> PromptDistanceOptions

"""



class PromptDistanceOptionsEventHandler(MulticastDelegate):
    """ PromptDistanceOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptDistanceOptionsEventHandler, sender: object, e: PromptDistanceOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptDistanceOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptDistanceOptionsEventHandler, sender: object, e: PromptDistanceOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptDoubleOptions(PromptNumericalOptions):
    """
    PromptDoubleOptions(messageAndKeywords: str, globalKeywords: str)
    PromptDoubleOptions(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: PromptDoubleOptions) -> float

Set: DefaultValue(self: PromptDoubleOptions) = value
"""



class PromptDoubleOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptDoubleOptionsEventArgs) -> PromptDoubleOptions

"""



class PromptDoubleOptionsEventHandler(MulticastDelegate):
    """ PromptDoubleOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptDoubleOptionsEventHandler, sender: object, e: PromptDoubleOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptDoubleOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptDoubleOptionsEventHandler, sender: object, e: PromptDoubleOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptResult(object):
    # no doc
    def ToString(self, provider=None):
        """
        ToString(self: PromptResult, provider: IFormatProvider) -> str
        ToString(self: PromptResult) -> str
        """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: PromptResult) -> PromptStatus

"""

    StringResult = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringResult(self: PromptResult) -> str

"""



class PromptDoubleResult(PromptResult):
    # no doc
    def ToString(self, provider=None):
        """
        ToString(self: PromptDoubleResult, provider: IFormatProvider) -> str
        ToString(self: PromptDoubleResult) -> str
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: PromptDoubleResult) -> float

"""



class PromptDoubleResultEventArgs(EventArgs):
    # no doc
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptDoubleResultEventArgs) -> PromptDoubleResult

"""



class PromptDoubleResultEventHandler(MulticastDelegate):
    """ PromptDoubleResultEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptDoubleResultEventHandler, sender: object, e: PromptDoubleResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptDoubleResultEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptDoubleResultEventHandler, sender: object, e: PromptDoubleResultEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptDragOptions(PromptEditorOptions):
    """
    PromptDragOptions(selection: SelectionSet, messageAndKeywords: str, globalKeywords: str, callback: DragCallback)
    PromptDragOptions(selection: SelectionSet, message: str, callback: DragCallback)
    """
    @staticmethod # known case of __new__
    def __new__(self, selection, *__args):
        """
        __new__(cls: type, selection: SelectionSet, messageAndKeywords: str, globalKeywords: str, callback: DragCallback)
        __new__(cls: type, selection: SelectionSet, message: str, callback: DragCallback)
        """
        pass

    AllowArbitraryInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowArbitraryInput(self: PromptDragOptions) -> bool

Set: AllowArbitraryInput(self: PromptDragOptions) = value
"""

    AllowNone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNone(self: PromptDragOptions) -> bool

Set: AllowNone(self: PromptDragOptions) = value
"""

    Callback = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Callback(self: PromptDragOptions) -> DragCallback

Set: Callback(self: PromptDragOptions) = value
"""

    Cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cursor(self: PromptDragOptions) -> DragCursor

Set: Cursor(self: PromptDragOptions) = value
"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection(self: PromptDragOptions) -> SelectionSet

"""



class PromptEntityOptions(PromptEditorOptions):
    """
    PromptEntityOptions(messageAndKeywords: str, globalKeywords: str)
    PromptEntityOptions(message: str)
    """
    def AddAllowedClass(self, type, exactMatch):
        """ AddAllowedClass(self: PromptEntityOptions, type: Type, exactMatch: bool) """
        pass

    def RemoveAllowedClass(self, type):
        """ RemoveAllowedClass(self: PromptEntityOptions, type: Type) """
        pass

    def SetRejectMessage(self, message):
        """ SetRejectMessage(self: PromptEntityOptions, message: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    AllowNone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNone(self: PromptEntityOptions) -> bool

Set: AllowNone(self: PromptEntityOptions) = value
"""

    AllowObjectOnLockedLayer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowObjectOnLockedLayer(self: PromptEntityOptions) -> bool

Set: AllowObjectOnLockedLayer(self: PromptEntityOptions) = value
"""



class PromptEntityOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptEntityOptionsEventArgs) -> PromptEntityOptions

"""



class PromptEntityOptionsEventHandler(MulticastDelegate):
    """ PromptEntityOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptEntityOptionsEventHandler, sender: object, e: PromptEntityOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptEntityOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptEntityOptionsEventHandler, sender: object, e: PromptEntityOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptEntityResult(PromptResult):
    # no doc
    def ToString(self, provider=None):
        """
        ToString(self: PromptEntityResult, provider: IFormatProvider) -> str
        ToString(self: PromptEntityResult) -> str
        """
        pass

    ObjectId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectId(self: PromptEntityResult) -> ObjectId

"""

    PickedPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PickedPoint(self: PromptEntityResult) -> Point3d

"""



class PromptEntityResultEventArgs(EventArgs):
    # no doc
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptEntityResultEventArgs) -> PromptEntityResult

"""



class PromptEntityResultEventHandler(MulticastDelegate):
    """ PromptEntityResultEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptEntityResultEventHandler, sender: object, e: PromptEntityResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptEntityResultEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptEntityResultEventHandler, sender: object, e: PromptEntityResultEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptFileNameResult(PromptResult):
    # no doc
    def ToString(self, provider=None):
        """
        ToString(self: PromptFileNameResult) -> str
        ToString(self: PromptFileNameResult, provider: IFormatProvider) -> str
        """
        pass

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: PromptFileNameResult) -> bool

"""



class PromptFileOptions(object):
    # no doc
    AllowUrls = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowUrls(self: PromptFileOptions) -> bool

Set: AllowUrls(self: PromptFileOptions) = value
"""

    DialogCaption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DialogCaption(self: PromptFileOptions) -> str

Set: DialogCaption(self: PromptFileOptions) = value
"""

    DialogName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DialogName(self: PromptFileOptions) -> str

Set: DialogName(self: PromptFileOptions) = value
"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: PromptFileOptions) -> str

Set: Filter(self: PromptFileOptions) = value
"""

    FilterIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterIndex(self: PromptFileOptions) -> int

Set: FilterIndex(self: PromptFileOptions) = value
"""

    InitialDirectory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialDirectory(self: PromptFileOptions) -> str

Set: InitialDirectory(self: PromptFileOptions) = value
"""

    InitialFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialFileName(self: PromptFileOptions) -> str

Set: InitialFileName(self: PromptFileOptions) = value
"""

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: PromptFileOptions) -> str

Set: Message(self: PromptFileOptions) = value
"""

    PreferCommandLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreferCommandLine(self: PromptFileOptions) -> bool

Set: PreferCommandLine(self: PromptFileOptions) = value
"""



class PromptForEntityEndingEventArgs(EventArgs):
    # no doc
    def Dispose(self):
        """ Dispose(self: PromptForEntityEndingEventArgs) """
        pass

    def RemoveSelectedObject(self):
        """ RemoveSelectedObject(self: PromptForEntityEndingEventArgs) """
        pass

    def ReplaceSelectedObject(self, newValue):
        """ ReplaceSelectedObject(self: PromptForEntityEndingEventArgs, newValue: SelectedObject) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptForEntityEndingEventArgs) -> PromptEntityResult

"""



class PromptForEntityEndingEventHandler(MulticastDelegate):
    """ PromptForEntityEndingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptForEntityEndingEventHandler, sender: object, e: PromptForEntityEndingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptForEntityEndingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptForEntityEndingEventHandler, sender: object, e: PromptForEntityEndingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptForSelectionEndingEventArgs(EventArgs):
    # no doc
    def Add(self, value):
        """ Add(self: PromptForSelectionEndingEventArgs, value: SelectedObject) """
        pass

    def AddSubEntity(self, value):
        """ AddSubEntity(self: PromptForSelectionEndingEventArgs, value: SelectedSubObject) """
        pass

    def Dispose(self):
        """ Dispose(self: PromptForSelectionEndingEventArgs) """
        pass

    def Remove(self, index):
        """ Remove(self: PromptForSelectionEndingEventArgs, index: int) """
        pass

    def RemoveSubEntity(self, entityIndex, subEntityIndex):
        """ RemoveSubEntity(self: PromptForSelectionEndingEventArgs, entityIndex: int, subEntityIndex: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: PromptForSelectionEndingEventArgs) -> SelectionFlags

"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection(self: PromptForSelectionEndingEventArgs) -> SelectionSet

"""



class PromptForSelectionEndingEventHandler(MulticastDelegate):
    """ PromptForSelectionEndingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptForSelectionEndingEventHandler, sender: object, e: PromptForSelectionEndingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptForSelectionEndingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptForSelectionEndingEventHandler, sender: object, e: PromptForSelectionEndingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptIntegerOptions(PromptNumericalOptions):
    """
    PromptIntegerOptions(messageAndKeywords: str, globalKeywords: str, lowerLimit: int, upperLimit: int)
    PromptIntegerOptions(messageAndKeywords: str, globalKeywords: str)
    PromptIntegerOptions(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str, lowerLimit: int, upperLimit: int)
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: PromptIntegerOptions) -> int

Set: DefaultValue(self: PromptIntegerOptions) = value
"""

    LowerLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerLimit(self: PromptIntegerOptions) -> int

Set: LowerLimit(self: PromptIntegerOptions) = value
"""

    UpperLimit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperLimit(self: PromptIntegerOptions) -> int

Set: UpperLimit(self: PromptIntegerOptions) = value
"""



class PromptIntegerOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptIntegerOptionsEventArgs) -> PromptIntegerOptions

"""



class PromptIntegerOptionsEventHandler(MulticastDelegate):
    """ PromptIntegerOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptIntegerOptionsEventHandler, sender: object, e: PromptIntegerOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptIntegerOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptIntegerOptionsEventHandler, sender: object, e: PromptIntegerOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptIntegerResult(PromptResult):
    # no doc
    def ToString(self, provider=None):
        """
        ToString(self: PromptIntegerResult, provider: IFormatProvider) -> str
        ToString(self: PromptIntegerResult) -> str
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: PromptIntegerResult) -> int

"""



class PromptIntegerResultEventArgs(EventArgs):
    # no doc
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptIntegerResultEventArgs) -> PromptIntegerResult

"""



class PromptIntegerResultEventHandler(MulticastDelegate):
    """ PromptIntegerResultEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptIntegerResultEventHandler, sender: object, e: PromptIntegerResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptIntegerResultEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptIntegerResultEventHandler, sender: object, e: PromptIntegerResultEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptKeywordOptions(PromptEditorOptions):
    """
    PromptKeywordOptions(messageAndKeywords: str, globalKeywords: str)
    PromptKeywordOptions(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    AllowArbitraryInput = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowArbitraryInput(self: PromptKeywordOptions) -> bool

Set: AllowArbitraryInput(self: PromptKeywordOptions) = value
"""

    AllowNone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNone(self: PromptKeywordOptions) -> bool

Set: AllowNone(self: PromptKeywordOptions) = value
"""



class PromptKeywordOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptKeywordOptionsEventArgs) -> PromptKeywordOptions

"""



class PromptKeywordOptionsEventHandler(MulticastDelegate):
    """ PromptKeywordOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptKeywordOptionsEventHandler, sender: object, e: PromptKeywordOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptKeywordOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptKeywordOptionsEventHandler, sender: object, e: PromptKeywordOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptNestedEntityOptions(PromptEditorOptions):
    """
    PromptNestedEntityOptions(messageAndKeywords: str, globalKeywords: str)
    PromptNestedEntityOptions(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    AllowNone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowNone(self: PromptNestedEntityOptions) -> bool

Set: AllowNone(self: PromptNestedEntityOptions) = value
"""

    NonInteractivePickPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonInteractivePickPoint(self: PromptNestedEntityOptions) -> Point3d

Set: NonInteractivePickPoint(self: PromptNestedEntityOptions) = value
"""

    UseNonInteractivePickPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseNonInteractivePickPoint(self: PromptNestedEntityOptions) -> bool

Set: UseNonInteractivePickPoint(self: PromptNestedEntityOptions) = value
"""



class PromptNestedEntityOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptNestedEntityOptionsEventArgs) -> PromptNestedEntityOptions

"""



class PromptNestedEntityOptionsEventHandler(MulticastDelegate):
    """ PromptNestedEntityOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptNestedEntityOptionsEventHandler, sender: object, e: PromptNestedEntityOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptNestedEntityOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptNestedEntityOptionsEventHandler, sender: object, e: PromptNestedEntityOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptNestedEntityResult(PromptEntityResult):
    # no doc
    def GetContainers(self):
        """ GetContainers(self: PromptNestedEntityResult) -> Array[ObjectId] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: PromptNestedEntityResult, provider: IFormatProvider) -> str
        ToString(self: PromptNestedEntityResult) -> str
        """
        pass

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: PromptNestedEntityResult) -> Matrix3d

"""



class PromptNestedEntityResultEventArgs(EventArgs):
    # no doc
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptNestedEntityResultEventArgs) -> PromptNestedEntityResult

"""



class PromptNestedEntityResultEventHandler(MulticastDelegate):
    """ PromptNestedEntityResultEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptNestedEntityResultEventHandler, sender: object, e: PromptNestedEntityResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptNestedEntityResultEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptNestedEntityResultEventHandler, sender: object, e: PromptNestedEntityResultEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptOpenFileOptions(PromptFileOptions):
    """ PromptOpenFileOptions(message: str) """
    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    SearchPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchPath(self: PromptOpenFileOptions) -> bool

Set: SearchPath(self: PromptOpenFileOptions) = value
"""

    TransferRemoteFiles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransferRemoteFiles(self: PromptOpenFileOptions) -> bool

Set: TransferRemoteFiles(self: PromptOpenFileOptions) = value
"""



class PromptPointOptions(PromptCornerOptions):
    """
    PromptPointOptions(messageAndKeywords: str, globalKeywords: str)
    PromptPointOptions(message: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, messageAndKeywords: str, globalKeywords: str)
        __new__(cls: type, message: str)
        """
        pass

    UseBasePoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseBasePoint(self: PromptPointOptions) -> bool

Set: UseBasePoint(self: PromptPointOptions) = value
"""



class PromptPointOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptPointOptionsEventArgs) -> PromptPointOptions

"""



class PromptPointOptionsEventHandler(MulticastDelegate):
    """ PromptPointOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptPointOptionsEventHandler, sender: object, e: PromptPointOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptPointOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptPointOptionsEventHandler, sender: object, e: PromptPointOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptPointResult(PromptResult):
    # no doc
    def ToString(self, provider=None):
        """
        ToString(self: PromptPointResult, provider: IFormatProvider) -> str
        ToString(self: PromptPointResult) -> str
        """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: PromptPointResult) -> Point3d

"""



class PromptPointResultEventArgs(EventArgs):
    # no doc
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptPointResultEventArgs) -> PromptPointResult

"""



class PromptPointResultEventHandler(MulticastDelegate):
    """ PromptPointResultEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptPointResultEventHandler, sender: object, e: PromptPointResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptPointResultEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptPointResultEventHandler, sender: object, e: PromptPointResultEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptSaveFileOptions(PromptFileOptions):
    """ PromptSaveFileOptions(message: str) """
    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    DeriveInitialFilenameFromDrawingName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeriveInitialFilenameFromDrawingName(self: PromptSaveFileOptions) -> bool

Set: DeriveInitialFilenameFromDrawingName(self: PromptSaveFileOptions) = value
"""

    DisplaySaveOptionsMenuItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplaySaveOptionsMenuItem(self: PromptSaveFileOptions) -> bool

Set: DisplaySaveOptionsMenuItem(self: PromptSaveFileOptions) = value
"""

    ForceOverwriteWarningForScriptsAndLisp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceOverwriteWarningForScriptsAndLisp(self: PromptSaveFileOptions) -> bool

Set: ForceOverwriteWarningForScriptsAndLisp(self: PromptSaveFileOptions) = value
"""



class PromptSelectionOptions(object):
    """ PromptSelectionOptions() """
    def AddKeywordsToMinimalList(self, kwds):
        """ AddKeywordsToMinimalList(self: PromptSelectionOptions, kwds: AddedKeywords) """
        pass

    def RemoveKeywordsFromFullList(self, kwds):
        """ RemoveKeywordsFromFullList(self: PromptSelectionOptions, kwds: SubtractedKeywords) """
        pass

    def SetKeywords(self, keywords, globalKeywords):
        """ SetKeywords(self: PromptSelectionOptions, keywords: str, globalKeywords: str) """
        pass

    AllowDuplicates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowDuplicates(self: PromptSelectionOptions) -> bool

Set: AllowDuplicates(self: PromptSelectionOptions) = value
"""

    AllowSubSelections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowSubSelections(self: PromptSelectionOptions) -> bool

Set: AllowSubSelections(self: PromptSelectionOptions) = value
"""

    ForceSubSelections = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceSubSelections(self: PromptSelectionOptions) -> bool

Set: ForceSubSelections(self: PromptSelectionOptions) = value
"""

    Keywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keywords(self: PromptSelectionOptions) -> KeywordCollection

"""

    MessageForAdding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MessageForAdding(self: PromptSelectionOptions) -> str

Set: MessageForAdding(self: PromptSelectionOptions) = value
"""

    MessageForRemoval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MessageForRemoval(self: PromptSelectionOptions) -> str

Set: MessageForRemoval(self: PromptSelectionOptions) = value
"""

    PrepareOptionalDetails = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrepareOptionalDetails(self: PromptSelectionOptions) -> bool

Set: PrepareOptionalDetails(self: PromptSelectionOptions) = value
"""

    RejectObjectsFromNonCurrentSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RejectObjectsFromNonCurrentSpace(self: PromptSelectionOptions) -> bool

Set: RejectObjectsFromNonCurrentSpace(self: PromptSelectionOptions) = value
"""

    RejectObjectsOnLockedLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RejectObjectsOnLockedLayers(self: PromptSelectionOptions) -> bool

Set: RejectObjectsOnLockedLayers(self: PromptSelectionOptions) = value
"""

    RejectPaperspaceViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RejectPaperspaceViewport(self: PromptSelectionOptions) -> bool

Set: RejectPaperspaceViewport(self: PromptSelectionOptions) = value
"""

    SelectEverythingInAperture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectEverythingInAperture(self: PromptSelectionOptions) -> bool

Set: SelectEverythingInAperture(self: PromptSelectionOptions) = value
"""

    SingleOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleOnly(self: PromptSelectionOptions) -> bool

Set: SingleOnly(self: PromptSelectionOptions) = value
"""

    SinglePickInSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SinglePickInSpace(self: PromptSelectionOptions) -> bool

Set: SinglePickInSpace(self: PromptSelectionOptions) = value
"""


    KeywordInput = None
    UnknownInput = None


class PromptSelectionOptionsEventArgs(EventArgs):
    # no doc
    def GetPoints(self):
        """ GetPoints(self: PromptSelectionOptionsEventArgs) -> Array[Point3d] """
        pass

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: PromptSelectionOptionsEventArgs) -> SelectionFilter

"""

    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptSelectionOptionsEventArgs) -> PromptSelectionOptions

"""



class PromptSelectionOptionsEventHandler(MulticastDelegate):
    """ PromptSelectionOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptSelectionOptionsEventHandler, sender: object, e: PromptSelectionOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptSelectionOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptSelectionOptionsEventHandler, sender: object, e: PromptSelectionOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptSelectionResult(object):
    # no doc
    def ToString(self, provider=None):
        """
        ToString(self: PromptSelectionResult, provider: IFormatProvider) -> str
        ToString(self: PromptSelectionResult) -> str
        """
        pass

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: PromptSelectionResult) -> PromptStatus

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: PromptSelectionResult) -> SelectionSet

"""



class PromptSelectionResultEventArgs(EventArgs):
    # no doc
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptSelectionResultEventArgs) -> PromptSelectionResult

"""



class PromptSelectionResultEventHandler(MulticastDelegate):
    """ PromptSelectionResultEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptSelectionResultEventHandler, sender: object, e: PromptSelectionResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptSelectionResultEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptSelectionResultEventHandler, sender: object, e: PromptSelectionResultEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptStatus(Enum):
    """ enum PromptStatus, values: Cancel (-5002), Error (-5001), Keyword (-5005), Modeless (5027), None (5000), OK (5100), Other (5028) """
    Cancel = None
    Error = None
    Keyword = None
    Modeless = None
    None = None
    OK = None
    Other = None
    value__ = None


class PromptStringOptions(PromptEditorOptions):
    """ PromptStringOptions(message: str) """
    @staticmethod # known case of __new__
    def __new__(self, message):
        """ __new__(cls: type, message: str) """
        pass

    AllowSpaces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowSpaces(self: PromptStringOptions) -> bool

Set: AllowSpaces(self: PromptStringOptions) = value
"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: PromptStringOptions) -> str

Set: DefaultValue(self: PromptStringOptions) = value
"""

    UseDefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDefaultValue(self: PromptStringOptions) -> bool

Set: UseDefaultValue(self: PromptStringOptions) = value
"""



class PromptStringOptionsEventArgs(EventArgs):
    # no doc
    Options = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Options(self: PromptStringOptionsEventArgs) -> PromptStringOptions

"""



class PromptStringOptionsEventHandler(MulticastDelegate):
    """ PromptStringOptionsEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptStringOptionsEventHandler, sender: object, e: PromptStringOptionsEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptStringOptionsEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptStringOptionsEventHandler, sender: object, e: PromptStringOptionsEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PromptStringResultEventArgs(EventArgs):
    # no doc
    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: PromptStringResultEventArgs) -> PromptResult

"""



class PromptStringResultEventHandler(MulticastDelegate):
    """ PromptStringResultEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PromptStringResultEventHandler, sender: object, e: PromptStringResultEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PromptStringResultEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PromptStringResultEventHandler, sender: object, e: PromptStringResultEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class RolloverEventArgs(EventArgs):
    # no doc
    Highlighted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Highlighted(self: RolloverEventArgs) -> FullSubentityPath

Set: Highlighted(self: RolloverEventArgs) = value
"""

    Picked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Picked(self: RolloverEventArgs) -> FullSubentityPath

"""



class RolloverEventHandler(MulticastDelegate):
    """ RolloverEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: RolloverEventHandler, sender: object, e: RolloverEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: RolloverEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: RolloverEventHandler, sender: object, e: RolloverEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SamplerStatus(Enum):
    """ enum SamplerStatus, values: Cancel (2), NoChange (1), OK (0) """
    Cancel = None
    NoChange = None
    OK = None
    value__ = None


class SelectionAddedEventArgs(EventArgs):
    # no doc
    def Add(self, value):
        """ Add(self: SelectionAddedEventArgs, value: SelectedObject) """
        pass

    def AddSubEntity(self, value):
        """ AddSubEntity(self: SelectionAddedEventArgs, value: SelectedSubObject) """
        pass

    def Dispose(self):
        """ Dispose(self: SelectionAddedEventArgs) """
        pass

    def Highlight(self, subSelectionIndex, path):
        """ Highlight(self: SelectionAddedEventArgs, subSelectionIndex: int, path: FullSubentityPath) """
        pass

    def Remove(self, index):
        """ Remove(self: SelectionAddedEventArgs, index: int) """
        pass

    def RemoveSubEntity(self, entityIndex, subEntityIndex):
        """ RemoveSubEntity(self: SelectionAddedEventArgs, entityIndex: int, subEntityIndex: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    AddedObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AddedObjects(self: SelectionAddedEventArgs) -> SelectionSet

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: SelectionAddedEventArgs) -> SelectionFlags

"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection(self: SelectionAddedEventArgs) -> SelectionSet

"""



class SelectionAddedEventHandler(MulticastDelegate):
    """ SelectionAddedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: SelectionAddedEventHandler, sender: object, e: SelectionAddedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SelectionAddedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SelectionAddedEventHandler, sender: object, e: SelectionAddedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SelectionDetails(object):
    # no doc
    def GetContainers(self):
        """ GetContainers(self: SelectionDetails) -> Array[ObjectId] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: SelectionDetails, provider: IFormatProvider) -> str
        ToString(self: SelectionDetails) -> str
        """
        pass

    Transform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transform(self: SelectionDetails) -> Matrix3d

"""



class SelectionFilter(object):
    """ SelectionFilter(value: Array[TypedValue]) """
    def GetFilter(self):
        """ GetFilter(self: SelectionFilter) -> Array[TypedValue] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value):
        """ __new__(cls: type, value: Array[TypedValue]) """
        pass


class SelectionFlags(Enum):
    """ enum (flags) SelectionFlags, values: Duplicates (2), FailedPickAuto (512), NestedEntities (4), Normal (0), PickfirstSet (32), PickPoints (1), PreviousSet (64), SinglePick (16), SubEntities (8), SubSelection (128), Undo (256) """
    Duplicates = None
    FailedPickAuto = None
    NestedEntities = None
    Normal = None
    PickfirstSet = None
    PickPoints = None
    PreviousSet = None
    SinglePick = None
    SubEntities = None
    SubSelection = None
    Undo = None
    value__ = None


class SelectionMethod(Enum):
    """ enum SelectionMethod, values: Crossing (3), Fence (4), NonGraphical (0), PickPoint (1), SubEntity (5), Unavailable (-1), Window (2) """
    Crossing = None
    Fence = None
    NonGraphical = None
    PickPoint = None
    SubEntity = None
    Unavailable = None
    value__ = None
    Window = None


class SelectionMode(Enum):
    """ enum SelectionMode, values: All (6), Box (3), Crossing (2), CrossingPolygon (8), Entity (5), Every (11), Extents (12), FencePolyline (7), Group (13), Last (4), Multiple (15), Pick (10), Previous (14), Window (1), WindowPolygon (9) """
    All = None
    Box = None
    Crossing = None
    CrossingPolygon = None
    Entity = None
    Every = None
    Extents = None
    FencePolyline = None
    Group = None
    Last = None
    Multiple = None
    Pick = None
    Previous = None
    value__ = None
    Window = None
    WindowPolygon = None


class SelectionRemovedEventArgs(EventArgs):
    # no doc
    def Dispose(self):
        """ Dispose(self: SelectionRemovedEventArgs) """
        pass

    def Remove(self, index):
        """ Remove(self: SelectionRemovedEventArgs, index: int) """
        pass

    def RemoveSubentity(self, index, subentityIndex):
        """ RemoveSubentity(self: SelectionRemovedEventArgs, index: int, subentityIndex: int) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Flags(self: SelectionRemovedEventArgs) -> SelectionFlags

"""

    RemovedObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RemovedObjects(self: SelectionRemovedEventArgs) -> SelectionSet

"""

    Selection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selection(self: SelectionRemovedEventArgs) -> SelectionSet

"""



class SelectionRemovedEventHandler(MulticastDelegate):
    """ SelectionRemovedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: SelectionRemovedEventHandler, sender: object, e: SelectionRemovedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SelectionRemovedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SelectionRemovedEventHandler, sender: object, e: SelectionRemovedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SelectionSet(object):
    # no doc
    def CopyTo(self, array, index):
        """ CopyTo(self: SelectionSet, array: Array[SelectedObject], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: SelectionSet) """
        pass

    @staticmethod
    def FromObjectIds(ids):
        """ FromObjectIds(ids: Array[ObjectId]) -> SelectionSet """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SelectionSet) -> IEnumerator """
        pass

    def GetObjectIds(self):
        """ GetObjectIds(self: SelectionSet) -> Array[ObjectId] """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: SelectionSet, provider: IFormatProvider) -> str
        ToString(self: SelectionSet) -> str
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SelectionSet) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: SelectionSet) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: SelectionSet) -> object

"""



class SelectionSetDelayMarshalled(SelectionSet):
    # no doc
    def Dispose(self):
        """ Dispose(self: SelectionSetDelayMarshalled, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SelectionSetDelayMarshalled) -> IEnumerator """
        pass

    def GetObjectIds(self):
        """ GetObjectIds(self: SelectionSetDelayMarshalled) -> Array[ObjectId] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SelectionSetDelayMarshalled) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SelectionSetDelayMarshalled) -> AdsName

"""



class SelectionTextInputEventArgs(EventArgs):
    # no doc
    def AddObjects(self, ids):
        """ AddObjects(self: SelectionTextInputEventArgs, ids: Array[ObjectId]) """
        pass

    def SetErrorMessage(self, errorMessage):
        """ SetErrorMessage(self: SelectionTextInputEventArgs, errorMessage: str) """
        pass

    Input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Input(self: SelectionTextInputEventArgs) -> str

"""



class SelectionTextInputEventHandler(MulticastDelegate):
    """ SelectionTextInputEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: SelectionTextInputEventHandler, sender: object, e: SelectionTextInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SelectionTextInputEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SelectionTextInputEventHandler, sender: object, e: SelectionTextInputEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SubtractedKeywords(Enum):
    """ enum SubtractedKeywords, values: AddRemove (2048), All (4), BoxAuto (8), CrossingCPolygon (32), Fence (64), Group (1024), Last (128), LastAllGroupPrevious (1), Multiple (16), PickImplied (2), Previous (256), WindowWPolygon (512) """
    AddRemove = None
    All = None
    BoxAuto = None
    CrossingCPolygon = None
    Fence = None
    Group = None
    Last = None
    LastAllGroupPrevious = None
    Multiple = None
    PickImplied = None
    Previous = None
    value__ = None
    WindowWPolygon = None


class Transient(Drawable):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def OnCaptured(self, *args): #cannot find CLR method
        """ OnCaptured(self: Transient, e: EventArgs) """
        pass

    def OnCaptureReleased(self, *args): #cannot find CLR method
        """ OnCaptureReleased(self: Transient, e: EventArgs) """
        pass

    def OnDeviceInput(self, *args): #cannot find CLR method
        """ OnDeviceInput(self: Transient, e: DeviceInputEventArgs) """
        pass

    def OnPointInput(self, *args): #cannot find CLR method
        """ OnPointInput(self: Transient, e: PointInputEventArgs) """
        pass

    def raise_Captured(self, *args): #cannot find CLR method
        """ raise_Captured(self: Transient, value0: object, value1: EventArgs) """
        pass

    def raise_CaptureReleased(self, *args): #cannot find CLR method
        """ raise_CaptureReleased(self: Transient, value0: object, value1: EventArgs) """
        pass

    def raise_DeviceInput(self, *args): #cannot find CLR method
        """ raise_DeviceInput(self: Transient, value0: object, value1: DeviceInputEventArgs) """
        pass

    def raise_PointInput(self, *args): #cannot find CLR method
        """ raise_PointInput(self: Transient, value0: object, value1: PointInputEventArgs) """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: Transient) -> ObjectId

"""

    IsPersistent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPersistent(self: Transient) -> bool

"""


    Captured = None
    CapturedDrawable = None
    CaptureReleased = None
    DeviceInput = None
    PointInput = None


class UserInputControls(Enum):
    """ enum (flags) UserInputControls, values: Accept3dCoordinates (128), AcceptMouseUpAsPoint (256), AcceptOtherInputString (2048), AnyBlankTerminatesInput (512), DoNotEchoCancelForCtrlC (4), DoNotUpdateLastPoint (8), GovernedByOrthoMode (1), GovernedByUCSDetect (4096), InitialBlankTerminatesInput (1024), NoDwgLimitsChecking (16), NoNegativeResponseAccepted (64), NoZDirectionOrtho (8192), NoZeroResponseAccepted (32), NullResponseAccepted (2), UseBasePointElevation (32768) """
    Accept3dCoordinates = None
    AcceptMouseUpAsPoint = None
    AcceptOtherInputString = None
    AnyBlankTerminatesInput = None
    DoNotEchoCancelForCtrlC = None
    DoNotUpdateLastPoint = None
    GovernedByOrthoMode = None
    GovernedByUCSDetect = None
    InitialBlankTerminatesInput = None
    NoDwgLimitsChecking = None
    NoNegativeResponseAccepted = None
    NoZDirectionOrtho = None
    NoZeroResponseAccepted = None
    NullResponseAccepted = None
    UseBasePointElevation = None
    value__ = None


