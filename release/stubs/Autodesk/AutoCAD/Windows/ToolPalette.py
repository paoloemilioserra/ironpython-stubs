# encoding: utf-8
# module Autodesk.AutoCAD.Windows.ToolPalette calls itself ToolPalette
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcTcToolReactorImpl(object):
    # no doc

class ContextMenuMode(Enum):
    """ enum ContextMenuMode, values: ContextMenuEditorImage (1), ContextMenuPaletteBackground (2), ContextMenuPaletteSetCaption (4), ContextMenuPaletteSetOptionButton (5), ContextMenuPaletteSetTab (3), ContextMenuPaletteTool (0), ContextNone (-1) """
    ContextMenuEditorImage = None
    ContextMenuPaletteBackground = None
    ContextMenuPaletteSetCaption = None
    ContextMenuPaletteSetOptionButton = None
    ContextMenuPaletteSetTab = None
    ContextMenuPaletteTool = None
    ContextNone = None
    value__ = None


class CustomToolBase(object):
    # no doc
    def BeginEdit(self):
        """ BeginEdit(self: CustomToolBase) """
        pass

    def BeginMultipleEdit(self, tools, stockToolIds):
        """ BeginMultipleEdit(self: CustomToolBase, tools: object, stockToolIds: object) """
        pass

    def CreateCommandTool(self, palette, toolName, bitmapName, macro):
        """ CreateCommandTool(self: CustomToolBase, palette: Package, toolName: str, bitmapName: ImageInfo, macro: str) -> Tool """
        pass

    def CreateFlyoutTool(self, palette, shapePackage, toolNameOverride):
        """ CreateFlyoutTool(self: CustomToolBase, palette: Package, shapePackage: Package, toolNameOverride: str) -> Tool """
        pass

    def CreatePalette(self, catalogName, paletteName):
        """ CreatePalette(self: CustomToolBase, catalogName: Catalog, paletteName: str) -> Palette """
        pass

    def CreateShapeCatalog(self, shapeName):
        """ CreateShapeCatalog(self: CustomToolBase, shapeName: str) -> Package """
        pass

    def CreateStockTool(self, catalogName):
        """ CreateStockTool(self: CustomToolBase, catalogName: str) -> Catalog """
        pass

    def CreateTool(self, palette=None, toolNameOverride=None, toolImageOverride=None):
        """
        CreateTool(self: CustomToolBase, palette: Package, toolNameOverride: str, toolImageOverride: ImageInfo) -> Tool
        CreateTool(self: CustomToolBase) -> object
        """
        pass

    def Customize(self, contextFlag, menuHandle, idCommandFirst, idCommandLast, paletteId):
        """ Customize(self: CustomToolBase, contextFlag: int, menuHandle: UInt32, idCommandFirst: UInt32, idCommandLast: UInt32, paletteId: Guid) -> (UInt32, Guid) """
        pass

    def Dispose(self):
        """ Dispose(self: CustomToolBase) """
        pass

    def DoModal(self, propertyValue, activeShapes):
        """ DoModal(self: CustomToolBase, activeShapes: ObjectIdCollection) -> str """
        pass

    def DragEnter(self, data, keyState, point, effect):
        """ DragEnter(self: CustomToolBase, data: IDataObject, keyState: UInt32, point: POINTL) -> UInt32 """
        pass

    def DragLeave(self):
        """ DragLeave(self: CustomToolBase) """
        pass

    def DragOver(self, keyState, pt, effect):
        """ DragOver(self: CustomToolBase, keyState: UInt32, pt: POINTL) -> UInt32 """
        pass

    def Drop(self, data, keyState, pt, effect):
        """ Drop(self: CustomToolBase, data: IDataObject, keyState: UInt32, pt: POINTL) -> UInt32 """
        pass

    def DropCallback(self, entity):
        """ DropCallback(self: CustomToolBase, entity: Entity) -> bool """
        pass

    def Dropped(self, url):
        """ Dropped(self: CustomToolBase, url: str) """
        pass

    def Edit(self, property, parentWindow, success):
        """
        Edit(self: CustomToolBase, property: object, parentWindow: int) -> bool
        Edit(self: CustomToolBase, property: object, parentWindow: Int64) -> bool
        Edit(self: CustomToolBase, property: object, parentWindow: IntPtr) -> bool
        """
        pass

    def Editable(self, dispatchId, editable):
        """ Editable(self: CustomToolBase, dispatchId: int) -> int """
        pass

    def EndEdit(self, bEditCancelled):
        """ EndEdit(self: CustomToolBase, bEditCancelled: bool) """
        pass

    def EndMultipleEdit(self, tools, stockToolIds, editCancelled):
        """ EndMultipleEdit(self: CustomToolBase, tools: object, stockToolIds: object, editCancelled: bool) """
        pass

    def Execute(self, flag, window, point, keyState):
        """ Execute(self: CustomToolBase, flag: int, window: UInt32, point: UInt32, keyState: UInt32) """
        pass

    def ExecuteCallback(self):
        """ ExecuteCallback(self: CustomToolBase) -> bool """
        pass

    def GetCommandString(self, idCommand):
        """ GetCommandString(self: CustomToolBase, idCommand: UInt32) -> str """
        pass

    def GetContextMenu(self, contextFlag, menu, idCommandFirst, idCommandLast):
        """ GetContextMenu(self: CustomToolBase, contextFlag: int, menu: UInt32, idCommandFirst: UInt32, idCommandLast: UInt32) -> UInt32 """
        pass

    def GetCustomPropertyCtrl(self, id, lcid, programId):
        """ GetCustomPropertyCtrl(self: CustomToolBase, id: object, lcid: UInt32) -> str """
        pass

    def GetData(self, staticProperties, dynamicProperties):
        """ GetData(self: CustomToolBase) -> (object, object) """
        pass

    def GetDisplayName(self, dispatchId, propertyName):
        """ GetDisplayName(self: CustomToolBase, dispatchId: int) -> str """
        pass

    def GetDisplayString(self, dispatchId, value):
        """ GetDisplayString(self: CustomToolBase, dispatchId: int) -> str """
        pass

    def GetDragDropContextInfo(self, pIUnknown, toolName, flag):
        """ GetDragDropContextInfo(self: CustomToolBase, pIUnknown: object) -> (str, UInt32) """
        pass

    def GetDropTarget(self):
        """ GetDropTarget(self: CustomToolBase) -> object """
        pass

    def GetMenuHelp(self, idCmd):
        """ GetMenuHelp(self: CustomToolBase, idCmd: UInt32) -> str """
        pass

    def GetPredefinedStrings(self, dispatchId, value, cookie):
        """ GetPredefinedStrings(self: CustomToolBase, dispatchId: int) -> (tagCALPOLESTR, tagCADWORD) """
        pass

    def GetPredefinedValue(self, dispatchId, cookie, value):
        """ GetPredefinedValue(self: CustomToolBase, dispatchId: int, cookie: UInt32) -> object """
        pass

    def GetPropertyIcon(self, id, icon):
        """ GetPropertyIcon(self: CustomToolBase, id: object) -> object """
        pass

    def GetPropertyWeight(self, id, pPropertyWeight):
        """ GetPropertyWeight(self: CustomToolBase, id: object) -> int """
        pass

    def GetPropTextColor(self, id, textColor):
        """ GetPropTextColor(self: CustomToolBase, id: object) -> UInt32 """
        pass

    def GetStockTool(self):
        """ GetStockTool(self: CustomToolBase) -> object """
        pass

    def GetToolProperties(self):
        """ GetToolProperties(self: CustomToolBase) -> object """
        pass

    def GetUnspecifiedString(self, id):
        """ GetUnspecifiedString(self: CustomToolBase, id: object) -> str """
        pass

    def InvokeCommand(self, idCommand, window):
        """ InvokeCommand(self: CustomToolBase, idCommand: UInt32, window: UInt32) """
        pass

    def InvokeMenuCommand(self, idCmd, paletteId, windowHandle):
        """ InvokeMenuCommand(self: CustomToolBase, idCmd: UInt32, paletteId: Guid, windowHandle: UInt32) -> (UInt32, Guid) """
        pass

    def IsFullView(self, id, visible, integralHeight):
        """ IsFullView(self: CustomToolBase, id: object) -> (bool, UInt32) """
        pass

    def IsUnspecifiedAllowed(self, id, returnValue):
        """ IsUnspecifiedAllowed(self: CustomToolBase, id: object) -> (int, bool) """
        pass

    def IsValueUnspecified(self, id, returnValue):
        """ IsValueUnspecified(self: CustomToolBase, id: object) -> (int, bool) """
        pass

    def Load(self, xmlElement):
        """ Load(self: CustomToolBase, xmlElement: object) """
        pass

    def MapPropertyToPage(self, dispatchId, clsid):
        """ MapPropertyToPage(self: CustomToolBase, dispatchId: int) -> Guid """
        pass

    def MultipleEdit(self, tools, stockToolIds, parentWindow, success):
        """ MultipleEdit(self: CustomToolBase, tools: object, stockToolIds: object, parentWindow: int) -> bool """
        pass

    def New(self):
        """ New(self: CustomToolBase) """
        pass

    def Refreshed(self, url):
        """ Refreshed(self: CustomToolBase, url: str) """
        pass

    def Save(self, xmlElement):
        """ Save(self: CustomToolBase, xmlElement: object) """
        pass

    def SetEditorWindow(self, editorWindow, propertyInspector):
        """ SetEditorWindow(self: CustomToolBase, editorWindow: int, propertyInspector: object)SetEditorWindow(self: CustomToolBase, editorWindow: Int64, propertyInspector: object)SetEditorWindow(self: CustomToolBase, editorWindow: IntPtr, propertyInspector: object) """
        pass

    def SetFlyoutTools(self, flyoutToolIds):
        """ SetFlyoutTools(self: CustomToolBase, flyoutToolIds: object) """
        pass

    def SetToolProperties(self, toolProperties):
        """ SetToolProperties(self: CustomToolBase, toolProperties: object) """
        pass

    def SetUnspecified(self, id, isUnspecified):
        """ SetUnspecified(self: CustomToolBase, id: object, isUnspecified: bool) """
        pass

    def ShowProperty(self, dispatchId, show):
        """ ShowProperty(self: CustomToolBase, dispatchId: int) -> int """
        pass

    def ValidateEditChanges(self):
        """ ValidateEditChanges(self: CustomToolBase) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CurrentShapeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentShapeId(self: CustomToolBase) -> Guid

Set: CurrentShapeId(self: CustomToolBase) = value
"""

    EditMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditMode(self: CustomToolBase) -> int

"""

    FlayoutPackageID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlayoutPackageID(self: CustomToolBase) -> Guid

Set: FlayoutPackageID(self: CustomToolBase) = value
"""

    ToolGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolGuid(self: CustomToolBase) -> Guid

"""

    ToolImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolImage(self: CustomToolBase) -> str

"""

    ToolName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolName(self: CustomToolBase) -> str

"""



class DragHandler(MulticastDelegate):
    """ DragHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, pTool, dwKeyState, tpOperationFlag, callback, obj):
        """ BeginInvoke(self: DragHandler, pTool: ValueType, dwKeyState: UInt32, tpOperationFlag: TPOperationFlag, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DragHandler, result: IAsyncResult) """
        pass

    def Invoke(self, pTool, dwKeyState, tpOperationFlag):
        """ Invoke(self: DragHandler, pTool: ValueType, dwKeyState: UInt32, tpOperationFlag: TPOperationFlag) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class DropPointHandler(MulticastDelegate):
    """ DropPointHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, point, callback, obj):
        """ BeginInvoke(self: DropPointHandler, point: Point3d, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DropPointHandler, result: IAsyncResult) """
        pass

    def Invoke(self, point):
        """ Invoke(self: DropPointHandler, point: Point3d) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ExecutionContext(Enum):
    """ enum ExecutionContext, values: DroppedInDrawing (1), LeftButtonClicked (0) """
    DroppedInDrawing = None
    LeftButtonClicked = None
    value__ = None


class FlyoutEntryAttribute(Attribute):
    """ FlyoutEntryAttribute(dispatchId: int) """
    @staticmethod # known case of __new__
    def __new__(self, dispatchId):
        """ __new__(cls: type, dispatchId: int) """
        pass

    DispId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispId(self: FlyoutEntryAttribute) -> int

"""



class PerPropertyBrowsingEntryAttribute(Attribute):
    """ PerPropertyBrowsingEntryAttribute(dispatchId: int, programId: str, leftIconResource: str, leftIconType: int, ellipsisBmpResource: str, ellipsisBmpType: int, textColor: int, fullView: bool, integralHeight: int, weight: int) """
    @staticmethod # known case of __new__
    def __new__(self, dispatchId, programId, leftIconResource, leftIconType, ellipsisBmpResource, ellipsisBmpType, textColor, fullView, integralHeight, weight):
        """ __new__(cls: type, dispatchId: int, programId: str, leftIconResource: str, leftIconType: int, ellipsisBmpResource: str, ellipsisBmpType: int, textColor: int, fullView: bool, integralHeight: int, weight: int) """
        pass

    DispId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DispId(self: PerPropertyBrowsingEntryAttribute) -> int

"""

    EllipsisBmpResource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EllipsisBmpResource(self: PerPropertyBrowsingEntryAttribute) -> str

"""

    EllipsisBmpType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EllipsisBmpType(self: PerPropertyBrowsingEntryAttribute) -> int

"""

    IntegralHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntegralHeight(self: PerPropertyBrowsingEntryAttribute) -> int

"""

    IsFullView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFullView(self: PerPropertyBrowsingEntryAttribute) -> bool

"""

    LefIconResource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LefIconResource(self: PerPropertyBrowsingEntryAttribute) -> str

"""

    LeftIconType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftIconType(self: PerPropertyBrowsingEntryAttribute) -> int

"""

    ProgId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProgId(self: PerPropertyBrowsingEntryAttribute) -> str

"""

    TextColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextColor(self: PerPropertyBrowsingEntryAttribute) -> int

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: PerPropertyBrowsingEntryAttribute) -> int

"""



class PickHandler(MulticastDelegate):
    """ PickHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, pTool, dwKeyState, tpOperationFlag, nIndex, callback, obj):
        """ BeginInvoke(self: PickHandler, pTool: ValueType, dwKeyState: UInt32, tpOperationFlag: TPOperationFlag, nIndex: int, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PickHandler, result: IAsyncResult) """
        pass

    def Invoke(self, pTool, dwKeyState, tpOperationFlag, nIndex):
        """ Invoke(self: PickHandler, pTool: ValueType, dwKeyState: UInt32, tpOperationFlag: TPOperationFlag, nIndex: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ReturnStatus(Enum):
    """ enum ReturnStatus, values: ContextMenuHide (1), ContextMenuShow (0), ContextMenuUpdatePalette (4), ExecutionCanceled (2), ExecutionCancelRejected (3) """
    ContextMenuHide = None
    ContextMenuShow = None
    ContextMenuUpdatePalette = None
    ExecutionCanceled = None
    ExecutionCancelRejected = None
    value__ = None


class ToolAttribute(Attribute):
    """ ToolAttribute(toolName: str, toolImage: str) """
    @staticmethod # known case of __new__
    def __new__(self, toolName, toolImage):
        """ __new__(cls: type, toolName: str, toolImage: str) """
        pass

    ToolImage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolImage(self: ToolAttribute) -> str

"""

    ToolName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToolName(self: ToolAttribute) -> str

"""



class ToolEditFlags(Enum):
    """ enum (flags) ToolEditFlags, values: EditCustom (1), EditDefault (0), EditMultiple (4), EditNone (2) """
    EditCustom = None
    EditDefault = None
    EditMultiple = None
    EditNone = None
    value__ = None


class ToolItemInfo(object):
    # no doc
    Description = None
    ItemId = None
    Name = None


class ToolReactorManager(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> ToolReactorManager """
        pass

    def invokeToolContextMenu(self, itemId, nIndex):
        """ invokeToolContextMenu(self: ToolReactorManager, itemId: Guid, nIndex: int) """
        pass

    def invokeToolDrag(self, itemId, dwKeyState, point):
        """ invokeToolDrag(self: ToolReactorManager, itemId: Guid, dwKeyState: UInt32, point: Point3d) """
        pass

    def invokeToolPick(self, itemId, dwKeyState):
        """ invokeToolPick(self: ToolReactorManager, itemId: Guid, dwKeyState: UInt32) """
        pass

    def raise_Drag(self, *args): #cannot find CLR method
        """ raise_Drag(self: ToolReactorManager, value0: ValueType, value1: UInt32, value2: TPOperationFlag) """
        pass

    def raise_DropPoint(self, *args): #cannot find CLR method
        """ raise_DropPoint(self: ToolReactorManager, value0: Point3d) """
        pass

    def raise_Pick(self, *args): #cannot find CLR method
        """ raise_Pick(self: ToolReactorManager, value0: ValueType, value1: UInt32, value2: TPOperationFlag, value3: int) """
        pass

    Drag = None
    DropPoint = None
    Pick = None


class TPOperationFlag(Enum):
    """ enum TPOperationFlag, values: ContextMenu (4), Drag (2), Pick (1) """
    ContextMenu = None
    Drag = None
    Pick = None
    value__ = None


