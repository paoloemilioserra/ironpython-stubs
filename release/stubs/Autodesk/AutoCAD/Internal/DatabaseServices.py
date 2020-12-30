# encoding: utf-8
# module Autodesk.AutoCAD.Internal.DatabaseServices calls itself DatabaseServices
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class EvalExpr(DBObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class EvalConnectable(EvalExpr):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class BlockElement(EvalConnectable):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: BlockElement) -> str

Set: Name(self: BlockElement) = value
"""



class BlockParameter(BlockElement):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetPropertyConnectionName(self, propName):
        """ GetPropertyConnectionName(self: BlockParameter, propName: str) -> str """
        pass

    def GetPropertyValue(self, name, xform=None):
        """
        GetPropertyValue(self: BlockParameter, name: str) -> object
        GetPropertyValue(self: BlockParameter, name: str, xform: Matrix3d) -> (object, Matrix3d)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass

    PropertyDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyDescription(self: BlockParameter) -> BlockParameterPropertyDescriptorCollection

"""



class Block1PointParameter(BlockParameter):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class Block2PointParameter(BlockParameter):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class BlockAction(BlockElement):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class BlockElementEntity(Entity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Element(self: BlockElementEntity) -> ObjectId

"""



class BlockActionEntity(BlockElementEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class BlockFlipParameter(Block2PointParameter):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass

    BaseStateLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseStateLabel(self: BlockFlipParameter) -> str

"""

    FlippedStateLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlippedStateLabel(self: BlockFlipParameter) -> str

"""


    FlipState = None


class BlockLookupAction(BlockAction):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def DuplicateCellsInLookupColumn(aryTable, descArray, colIdx, outArray):
        """ DuplicateCellsInLookupColumn(aryTable: Array, descArray: LookupColumnDescriptorCollection, colIdx: int) -> (bool, Array) """
        pass

    @staticmethod
    def DuplicateRowsOverInputColumns(aryTable, descArray, outArray):
        """ DuplicateRowsOverInputColumns(aryTable: Array, descArray: LookupColumnDescriptorCollection) -> (bool, Array) """
        pass

    def GetLookupTable(self, pDataTable, descArray):
        """ GetLookupTable(self: BlockLookupAction) -> (Array, LookupColumnDescriptorCollection) """
        pass

    @staticmethod
    def NonSingletonRangeInInputColumns(aryTable, descArray, outArray):
        """ NonSingletonRangeInInputColumns(aryTable: Array, descArray: LookupColumnDescriptorCollection) -> (bool, Array) """
        pass

    @staticmethod
    def NullsInInputColumns(aryTable, descArray, outArray):
        """ NullsInInputColumns(aryTable: Array, descArray: LookupColumnDescriptorCollection) -> (bool, Array) """
        pass

    def SetLookupTable(self, aryTable, descArray):
        """ SetLookupTable(self: BlockLookupAction, aryTable: Array, descArray: LookupColumnDescriptorCollection) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass

    NumberOfInputColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfInputColumns(self: BlockLookupAction) -> int

"""

    NumberOfOutputColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfOutputColumns(self: BlockLookupAction) -> int

"""

    NumberOfRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRows(self: BlockLookupAction) -> int

"""



class BlockLookupActionEntity(BlockActionEntity):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class BlockLookupParameter(Block1PointParameter):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class BlockParameterPropertyDescriptor(object):
    # no doc
    ConnectionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionName(self: BlockParameterPropertyDescriptor) -> str

"""

    HasValueSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasValueSet(self: BlockParameterPropertyDescriptor) -> bool

"""

    PropertyDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyDescription(self: BlockParameterPropertyDescriptor) -> str

"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyName(self: BlockParameterPropertyDescriptor) -> str

"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: BlockParameterPropertyDescriptor) -> Int16

"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: BlockParameterPropertyDescriptor) -> bool

"""

    UnitsType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitsType(self: BlockParameterPropertyDescriptor) -> UnitsType

"""

    ValueSetValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueSetValues(self: BlockParameterPropertyDescriptor) -> Array

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: BlockParameterPropertyDescriptor) -> bool

"""



class BlockParameterPropertyDescriptorCollection(DisposableWrapper):
    """ BlockParameterPropertyDescriptorCollection() """
    def CopyTo(self, array, size):
        """ CopyTo(self: BlockParameterPropertyDescriptorCollection, array: Array[BlockParameterPropertyDescriptor], size: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: BlockParameterPropertyDescriptorCollection) -> IEnumerator """
        pass

    def ICollectionCopyTo(self, array, size):
        """ ICollectionCopyTo(self: BlockParameterPropertyDescriptorCollection, array: Array, size: int) """
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
    """Get: Count(self: BlockParameterPropertyDescriptorCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: BlockParameterPropertyDescriptorCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: BlockParameterPropertyDescriptorCollection) -> object

"""



class BlockUserParameter(Block1PointParameter):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass

    UserParamType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UserParamType(self: BlockUserParameter) -> UserParameterType

"""



class EvalGraph(DBObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAllNodes(self):
        """ GetAllNodes(self: EvalGraph) -> Array[int] """
        pass

    def GetNode(self, nodeId, mode, pTrans):
        """ GetNode(self: EvalGraph, nodeId: UInt32, mode: OpenMode, pTrans: Transaction) -> DBObject """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool) """
        pass


class LookupColumnDescriptor(RXObject):
    """ LookupColumnDescriptor() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool)
        """
        pass

    ConnectableId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectableId(self: LookupColumnDescriptor) -> UInt32

Set: ConnectableId(self: LookupColumnDescriptor) = value
"""

    ConnectionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ConnectionName(self: LookupColumnDescriptor) -> str

Set: ConnectionName(self: LookupColumnDescriptor) = value
"""

    IsInvertible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsInvertible(self: LookupColumnDescriptor) -> bool

Set: IsInvertible(self: LookupColumnDescriptor) = value
"""

    IsOutputColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsOutputColumn(self: LookupColumnDescriptor) -> bool

Set: IsOutputColumn(self: LookupColumnDescriptor) = value
"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: LookupColumnDescriptor) -> Int16

Set: PropertyType(self: LookupColumnDescriptor) = value
"""

    PropertyUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyUnits(self: LookupColumnDescriptor) -> UnitsType

Set: PropertyUnits(self: LookupColumnDescriptor) = value
"""

    UnmatchedValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnmatchedValue(self: LookupColumnDescriptor) -> str

Set: UnmatchedValue(self: LookupColumnDescriptor) = value
"""



class LookupColumnDescriptorCollection(DisposableWrapper):
    """ LookupColumnDescriptorCollection() """
    def Add(self, value):
        """ Add(self: LookupColumnDescriptorCollection, value: LookupColumnDescriptor) -> int """
        pass

    def Clear(self):
        """ Clear(self: LookupColumnDescriptorCollection) """
        pass

    def CopyTo(self, array, size):
        """ CopyTo(self: LookupColumnDescriptorCollection, array: Array[LookupColumnDescriptor], size: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: LookupColumnDescriptorCollection) -> IEnumerator """
        pass

    def ICollectionCopyTo(self, array, size):
        """ ICollectionCopyTo(self: LookupColumnDescriptorCollection, array: Array, size: int) """
        pass

    def Insert(self, index, value):
        """ Insert(self: LookupColumnDescriptorCollection, index: int, value: LookupColumnDescriptor) """
        pass

    def Remove(self, value):
        """ Remove(self: LookupColumnDescriptorCollection, value: LookupColumnDescriptor) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: LookupColumnDescriptorCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: LookupColumnDescriptorCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: LookupColumnDescriptorCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: LookupColumnDescriptorCollection) -> object

"""



class UnitsType(Enum):
    """ enum UnitsType, values: Angular (1), Area (3), Distance (2), NoUnits (0) """
    Angular = None
    Area = None
    Distance = None
    NoUnits = None
    value__ = None


class UserParameterType(Enum):
    """ enum UserParameterType, values: Angle (4), Area (1), Distance (0), Scalar (3), String (5), Volume (2) """
    Angle = None
    Area = None
    Distance = None
    Scalar = None
    String = None
    value__ = None
    Volume = None


