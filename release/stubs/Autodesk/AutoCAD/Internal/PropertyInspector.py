# encoding: utf-8
# module Autodesk.AutoCAD.Internal.PropertyInspector calls itself PropertyInspector
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcEdPropertyInspectorReactorImpl(object):
    # no doc

class CollectableObject(DisposableWrapper):
    """ CollectableObject() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CollectableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectableName(self: CollectableObject) -> str

"""

    ObjectCollectableKind = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectCollectableKind(self: CollectableObject) -> int

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: CollectableObject) -> int

"""



class CategoryCollectable(CollectableObject):
    """ CategoryCollectable() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def IsCollapsed(self):
        """ IsCollapsed(self: CategoryCollectable) -> bool """
        pass

    def IsEqual(self, *__args):
        """
        IsEqual(self: CategoryCollectable, name: str, categoryId: int) -> bool
        IsEqual(self: CategoryCollectable, name: str) -> bool
        IsEqual(self: CategoryCollectable, category: CategoryCollectable, check: CHECK_LEVEL, flags: UInt32) -> (bool, UInt32)
        IsEqual(self: CategoryCollectable, name: str, categoryId: int, parentCategoryId: int) -> bool
        """
        pass

    def RemoveDynamicCollectables(self, deleteProperty=None):
        """ RemoveDynamicCollectables(self: CategoryCollectable)RemoveDynamicCollectables(self: CategoryCollectable, deleteProperty: bool) """
        pass

    def Sync(self, category, inequalityFlags=None, literalUnion=None):
        """ Sync(self: CategoryCollectable, category: CategoryCollectable)Sync(self: CategoryCollectable, category: CategoryCollectable, inequalityFlags: UInt32)Sync(self: CategoryCollectable, category: CategoryCollectable, inequalityFlags: UInt32, literalUnion: bool) """
        pass

    def ToggleState(self):
        """ ToggleState(self: CategoryCollectable) -> int """
        pass

    CategoryId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CategoryId(self: CategoryCollectable) -> int

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: CategoryCollectable) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: CategoryCollectable) -> str

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: CategoryCollectable) -> CollectionVector

"""

    Weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weight(self: CategoryCollectable) -> int

Set: Weight(self: CategoryCollectable) = value
"""



class CategoryInequalityFlags(Enum):
    """ enum (flags) CategoryInequalityFlags, values: CategoryCommandButtons (4), CategoryId (8), Description (2), Name (1), Parent (32), Visible (64), Weight (16) """
    CategoryCommandButtons = None
    CategoryId = None
    Description = None
    Name = None
    Parent = None
    value__ = None
    Visible = None
    Weight = None


class CollectionVector(DisposableWrapper):
    """
    CollectionVector(initialSize: int)
    CollectionVector()
    """
    def Add(self, *__args):
        """ Add(self: CollectionVector, value: CollectableObject)Add(self: CollectionVector, vector: CollectionVector) """
        pass

    def ApplyOemFilter(self, general, zeroBased=None):
        """ ApplyOemFilter(self: CollectionVector, general: str)ApplyOemFilter(self: CollectionVector, general: str, zeroBased: bool) """
        pass

    def Cleanup(self, zeroBased=None):
        """ Cleanup(self: CollectionVector)Cleanup(self: CollectionVector, zeroBased: bool) """
        pass

    def Count(self):
        """ Count(self: CollectionVector) -> int """
        pass

    def DestroyControls(self, zeroBased=None):
        """ DestroyControls(self: CollectionVector)DestroyControls(self: CollectionVector, zeroBased: bool) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def FindCategory(self, name, categoryId=None, parentCategoryId=None, zeroBased=None):
        """
        FindCategory(self: CollectionVector, name: str, categoryId: int) -> CategoryCollectable
        FindCategory(self: CollectionVector, name: str) -> CategoryCollectable
        FindCategory(self: CollectionVector, name: str, categoryId: int, parentCategoryId: int, zeroBased: bool) -> CategoryCollectable
        FindCategory(self: CollectionVector, name: str, categoryId: int, parentCategoryId: int) -> CategoryCollectable
        """
        pass

    def InsertAt(self, index, value):
        """ InsertAt(self: CollectionVector, index: int, value: CollectableObject) """
        pass

    def Item(self, index):
        """ Item(self: CollectionVector, index: int) -> CollectableObject """
        pass

    def NestCategories(self, zeroBased=None):
        """ NestCategories(self: CollectionVector)NestCategories(self: CollectionVector, zeroBased: bool) """
        pass

    def Print(self, logFile, append=None):
        """ Print(self: CollectionVector, logFile: str)Print(self: CollectionVector, logFile: str, append: bool) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: CollectionVector) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: CollectionVector, index: int) """
        pass

    def RemoveDynamicCollectables(self):
        """ RemoveDynamicCollectables(self: CollectionVector) """
        pass

    def SetAt(self, index, value):
        """ SetAt(self: CollectionVector, index: int, value: CollectableObject) """
        pass

    def SetCategoryWeight(self, categoryName, weight, zeroBased=None):
        """ SetCategoryWeight(self: CollectionVector, categoryName: str, weight: int)SetCategoryWeight(self: CollectionVector, categoryName: str, weight: int, zeroBased: bool) """
        pass

    def Sort(self, begin, finish):
        """ Sort(self: CollectionVector, begin: int, finish: int) """
        pass

    def SortVectorByWeights(self, begin, finish):
        """ SortVectorByWeights(self: CollectionVector, begin: int, finish: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, initialSize=None):
        """
        __new__(cls: type, initialSize: int)
        __new__(cls: type)
        """
        pass


class ObjectPropertyManagerProperties(object):
    # no doc
    @staticmethod
    def ClassIsVetoed(cls, isQPContext):
        """ ClassIsVetoed(cls: RXClass, isQPContext: bool) -> bool """
        pass

    @staticmethod
    def ConvertBlkrefToXref(objId):
        """ ConvertBlkrefToXref(objId: ObjectId) -> bool """
        pass

    @staticmethod
    def GetCategoryId(prop):
        """ GetCategoryId(prop: PropertyCollectable) -> int """
        pass

    @staticmethod
    def GetDisplayName(*__args):
        """
        GetDisplayName(objId: ObjectId) -> str
        GetDisplayName(obj: DBObject) -> str
        """
        pass

    @staticmethod
    def GetDisplayNameGuts(pUnk):
        """ GetDisplayNameGuts(pUnk: IUnknown*) -> str """
        pass

    @staticmethod
    def GetMultiplePropertyGuids(cls, GUIDs):
        """ GetMultiplePropertyGuids(cls: RXClass, GUIDs: StringCollection) -> bool """
        pass

    @staticmethod
    def GetNonEntityObjectTypes(isTooltipsContext):
        """ GetNonEntityObjectTypes(isTooltipsContext: bool) -> Dictionary[str, StringCollection] """
        pass

    @staticmethod
    def GetProperties(*__args):
        """
        GetProperties(objId: ObjectId, bFilterable: bool, bQPContext: bool) -> CollectionVector
        GetProperties(obj: DBObject, bFilterable: bool, bQPContext: bool) -> CollectionVector
        """
        pass

    @staticmethod
    def GetPropertiesForSubtype(*__args):
        """
        GetPropertiesForSubtype(objId: ObjectId, bFilterable: bool, sGUID: str, bQPContext: bool) -> CollectionVector
        GetPropertiesForSubtype(obj: DBObject, bFilterable: bool, sGUID: str, bQPContext: bool) -> CollectionVector
        """
        pass

    @staticmethod
    def GetPropertiesForSubtypeGuts(pUnk, bFilterable, sGUID, bQPContext):
        """ GetPropertiesForSubtypeGuts(pUnk: IUnknown*, bFilterable: bool, sGUID: str, bQPContext: bool) -> CollectionVector """
        pass

    @staticmethod
    def GetPropertiesGuts(pUnk, bFilterable, bQPContext):
        """ GetPropertiesGuts(pUnk: IUnknown*, bFilterable: bool, bQPContext: bool) -> CollectionVector """
        pass

    @staticmethod
    def GetSubtypes(cls, GUIDs, displayNames):
        """ GetSubtypes(cls: RXClass, GUIDs: StringCollection, displayNames: StringCollection) -> bool """
        pass

    @staticmethod
    def GiveClassChanceToCreate(cls, db, pEntOut, sGUID):
        """ GiveClassChanceToCreate(cls: RXClass, db: Database, pEntOut: Entity, sGUID: str) -> (ObjectId, Entity) """
        pass

    @staticmethod
    def IsDynamicProperty(prop, GUIDs):
        """ IsDynamicProperty(prop: PropertyCollectable, GUIDs: StringCollection) -> bool """
        pass


class ObjectPropertyManagerPropertyUtility(object):
    # no doc
    @staticmethod
    def GetIUnknownFromObject(obj, bAttachToObject):
        """ GetIUnknownFromObject(obj: DBObject, bAttachToObject: bool) -> IntPtr """
        pass

    @staticmethod
    def GetIUnknownFromObjectId(objId):
        """ GetIUnknownFromObjectId(objId: ObjectId) -> IntPtr """
        pass

    @staticmethod
    def GetTypeInfo(obj, lcid):
        """ GetTypeInfo(obj: object, lcid: int) -> ITypeInfo """
        pass

    @staticmethod
    def ObjectSupportsNonDBResidency(obj):
        """ ObjectSupportsNonDBResidency(obj: DBObject) -> bool """
        pass


class PropertyCategoryId(Enum):
    """ enum PropertyCategoryId, values: AltUnits (-20), Appearance (-5), Attributes (2941), Behavior (-6), ControlPoints (-18), Data (-7), DataPoints (-15), Dde (-11), Fit (-21), Font (-3), General (-12), Geometry (-25), ImageAdjust (-17), LinesArrows (-22), List (-8), Mass (-13), Mesh (-16), Misc (-2), Nil (-1), Pattern (-14), Position (-4), PrimaryUnits (-19), Scale (-10), Table (-24), Text (-9), Tolerances (-23) """
    AltUnits = None
    Appearance = None
    Attributes = None
    Behavior = None
    ControlPoints = None
    Data = None
    DataPoints = None
    Dde = None
    Fit = None
    Font = None
    General = None
    Geometry = None
    ImageAdjust = None
    LinesArrows = None
    List = None
    Mass = None
    Mesh = None
    Misc = None
    Nil = None
    Pattern = None
    Position = None
    PrimaryUnits = None
    Scale = None
    Table = None
    Text = None
    Tolerances = None
    value__ = None


class PropertyCollectable(CollectableObject):
    """ PropertyCollectable() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetValue(self, unknown, value):
        """ GetValue(self: PropertyCollectable, unknown: IntPtr, value: object) -> (bool, object) """
        pass

    def IsEqual(self, propertyCollectable, check, flags):
        """ IsEqual(self: PropertyCollectable, propertyCollectable: PropertyCollectable, check: CHECK_LEVEL, flags: UInt32) -> (bool, UInt32) """
        pass

    def Skip(self):
        """ Skip(self: PropertyCollectable) -> bool """
        pass

    def Sync(self, propertyCollectable, inequalityFlags=None):
        """ Sync(self: PropertyCollectable, propertyCollectable: PropertyCollectable)Sync(self: PropertyCollectable, propertyCollectable: PropertyCollectable, inequalityFlags: UInt32) """
        pass

    CollectableName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CollectableName(self: PropertyCollectable) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PropertyCollectable) -> str

"""

    DISP = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DISP(self: PropertyCollectable) -> object

"""

    dispid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: dispid(self: PropertyCollectable) -> int

"""

    MemberId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MemberId(self: PropertyCollectable) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: PropertyCollectable) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: PropertyCollectable) -> int

"""

    weight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: weight(self: PropertyCollectable) -> int

Set: weight(self: PropertyCollectable) = value
"""



class PropertyInequalityFlags(Enum):
    """ enum (flags) PropertyInequalityFlags, values: ClsidPropPage (2048), Disabled (512), Ellipses (1024), Enum (128), FullView (8), IntegralHeight (4), Name (1), Parent (64), PropertyControl (2), TextColor (16), Type (256), Visible (4096), Weight (32) """
    ClsidPropPage = None
    Disabled = None
    Ellipses = None
    Enum = None
    FullView = None
    IntegralHeight = None
    Name = None
    Parent = None
    PropertyControl = None
    TextColor = None
    Type = None
    value__ = None
    Visible = None
    Weight = None


class PropertyInspectorEventArgs(EventArgs):
    """ PropertyInspectorEventArgs() """
    OPMModeFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OPMModeFlag(self: PropertyInspectorEventArgs) -> int

"""

    ParentWindow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentWindow(self: PropertyInspectorEventArgs) -> IntPtr

"""

    Property = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Property(self: PropertyInspectorEventArgs) -> object

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: PropertyInspectorEventArgs) -> object

"""



class PropertyInspectorEventHandler(MulticastDelegate):
    """ PropertyInspectorEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: PropertyInspectorEventHandler, sender: object, e: PropertyInspectorEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PropertyInspectorEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: PropertyInspectorEventHandler, sender: object, e: PropertyInspectorEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class PropertyInspectorEventManager(object):
    # no doc
    @staticmethod
    def Instance():
        """ Instance() -> PropertyInspectorEventManager """
        pass

    propertyChanged = None
    propertyDialogDismissed = None
    propertyDialogInvoked = None
    propertyWillChange = None


