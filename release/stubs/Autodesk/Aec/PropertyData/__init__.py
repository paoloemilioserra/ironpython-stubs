# encoding: utf-8
# module Autodesk.Aec.PropertyData calls itself PropertyData
# from AecPropDataMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DataType(Enum):
    """
    Defines identifiers that indicate the data type.
    
    enum DataType, values: AlphaIncrement (5), AutoIncrement (4), Graphic (7), Integer (0), List (6), Real (1), Text (2), TrueFalse (3)
    """
    AlphaIncrement = None
    AutoIncrement = None
    Graphic = None
    Integer = None
    List = None
    Real = None
    Text = None
    TrueFalse = None
    value__ = None


class IteratorType(Enum):
    """
    Defines IteratorType for ScheduleTableStyleHeaderTreeIterator.
    
    enum IteratorType, values: DepthFirst (0), ParentFirst (1)
    """
    DepthFirst = None
    ParentFirst = None
    value__ = None


class ScheduleHeaderPositionNode(DisposableWrapper):
    """
    Represents a Schedule Header Position Node.
    
    ScheduleHeaderPositionNode(header: str, position: ScheduleTableHeaderPosition, headerNode: ScheduleTableStyleHeaderNode)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, header, position, headerNode):
        """
        __new__(cls: type, header: str, position: ScheduleTableHeaderPosition, headerNode: ScheduleTableStyleHeaderNode)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    HeaderNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the header node.

Get: HeaderNode(self: ScheduleHeaderPositionNode) -> ScheduleTableStyleHeaderNode

"""

    Heading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the heading.

Get: Heading(self: ScheduleHeaderPositionNode) -> str

"""

    Position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the position.

Get: Position(self: ScheduleHeaderPositionNode) -> ScheduleTableHeaderPosition

"""



class ScheduleTableColumnOrder(DisposableWrapper):
    """ Represents a schedule table column order. """
    def CompareRows(self, row1, row2, raw):
        """
        CompareRows(self: ScheduleTableColumnOrder, row1: int, row2: int, raw: bool) -> int
        
            Compares two rows.
        
            row1: The first row.
            row2: The second row.
            raw: Determines if the row and column are raw value. When row == false, need 
             indirection via our indexing arrays.
        
            Returns: Returns the comparing result.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class ScheduleTableColumnOrderAllColumns(ScheduleTableColumnOrder):
    """
    Represents  schedule table column order all columns.
    
    ScheduleTableColumnOrderAllColumns(matrix: ScheduleTableVariantMatrix, ascending: bool)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, matrix, ascending):
        """
        __new__(cls: type, matrix: ScheduleTableVariantMatrix, ascending: bool)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class ScheduleTableColumnOrderSingleColumn(ScheduleTableColumnOrder):
    """
    Represents schedule table column order single column.
    
    ScheduleTableColumnOrderSingleColumn(matrix: ScheduleTableVariantMatrix, column: int, ascending: bool)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, matrix, column, ascending):
        """
        __new__(cls: type, matrix: ScheduleTableVariantMatrix, column: int, ascending: bool)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class ScheduleTableHeaderPosition(DisposableWrapper):
    """
    Represents a Schedule Table Header Position.
    
    ScheduleTableHeaderPosition(left: float, right: float, bottom: float, top: float)
    ScheduleTableHeaderPosition()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, left=None, right=None, bottom=None, top=None):
        """
        __new__(cls: type, left: float, right: float, bottom: float, top: float)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Bottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets bottom.

Get: Bottom(self: ScheduleTableHeaderPosition) -> float

Set: Bottom(self: ScheduleTableHeaderPosition) = value
"""

    Left = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets left.

Get: Left(self: ScheduleTableHeaderPosition) -> float

Set: Left(self: ScheduleTableHeaderPosition) = value
"""

    Right = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets right.

Get: Right(self: ScheduleTableHeaderPosition) -> float

Set: Right(self: ScheduleTableHeaderPosition) = value
"""

    Top = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets top.

Get: Top(self: ScheduleTableHeaderPosition) -> float

Set: Top(self: ScheduleTableHeaderPosition) = value
"""



class ScheduleTableHeaderPositionIterator(DisposableWrapper):
    """ Represents a Schedule Table Header Position Iterator. """
    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """
        Create(unmanagedPointer: IntPtr, autoDelete: bool) -> ScheduleTableHeaderPositionIterator
        
            Initializes a new instance of the ScheduleTableHeaderPosition class.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Reset(self):
        """
        Reset(self: ScheduleTableHeaderPositionIterator)
            Reset the iterator.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Next ScheduleHeaderPositionNode.

Get: Next(self: ScheduleTableHeaderPositionIterator) -> ScheduleHeaderPositionNode

"""



class ScheduleTableStyleHeaderTreeParameter(Enum):
    """
    Defines parameter for ScheduleTableStyleHeaderTree.
    
    enum ScheduleTableStyleHeaderTreeParameter, values:
    """
    value__ = None


class ScheduleTableUniqueVariantCollection(DisposableWrapper):
    """
    Represents a collection of Schedule Table Unique Variant.
    
    ScheduleTableUniqueVariantCollection(keepEmpty: bool, limit: int)
    ScheduleTableUniqueVariantCollection(keepEmpty: bool)
    ScheduleTableUniqueVariantCollection()
    """
    def Add(self, value):
        """
        Add(self: ScheduleTableUniqueVariantCollection, value: object) -> int
        
            Add value.
        
            value: The value.
            Returns: The added index.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: ScheduleTableUniqueVariantCollection, value: object) -> bool
        
            If contains value.
        
            value: The value.
            Returns: True if contains value, false other wise.
        """
        pass

    def CopyTo(self, array, start):
        """
        CopyTo(self: ScheduleTableUniqueVariantCollection, array: Array, start: int)
            Copy to array.
        
            array: The target array.
            start: The start position to copy.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Dump(self):
        """
        Dump(self: ScheduleTableUniqueVariantCollection)
            Dump.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScheduleTableUniqueVariantCollection) -> IEnumerator
        
            Returns an enumerator for this collection.
            Returns: Returns an enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: ScheduleTableUniqueVariantCollection, value: object) -> int
        
            Determines the index of the specified item.
        
            value: The item.
            Returns: Returns the index of the specified item.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IList, value: object) -> bool """
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

    @staticmethod # known case of __new__
    def __new__(self, keepEmpty=None, limit=None):
        """
        __new__(cls: type, keepEmpty: bool, limit: int)
        __new__(cls: type, keepEmpty: bool)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the count.

Get: Count(self: ScheduleTableUniqueVariantCollection) -> int

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If it is fixed size.

Get: IsFixedSize(self: ScheduleTableUniqueVariantCollection) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets if it is readonly.

Get: IsReadOnly(self: ScheduleTableUniqueVariantCollection) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is synchronized.

Get: IsSynchronized(self: ScheduleTableUniqueVariantCollection) -> bool

"""

    SplitDelimitedValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets if split delimited values.

Get: SplitDelimitedValues(self: ScheduleTableUniqueVariantCollection) -> bool

"""



class ScheduleTableVariantMatrix(DisposableWrapper):
    """
    Represents a schedule table variant matrix.
    
    ScheduleTableVariantMatrix(rows: int, columns: int, styleId: ObjectId)
    ScheduleTableVariantMatrix()
    """
    def AppendRowDataAt(self, row, *__args):
        """
        AppendRowDataAt(self: ScheduleTableVariantMatrix, row: int, entityId: ObjectId, blockReferencePathIdArray: ObjectIdCollection, sorted: bool)
            Appends the row data at the specified row.
        
            row: The row.
            entityId: The id of entity.
            blockReferencePathIdArray: An id array of block reference path.
            sorted: Indicates if has been sorted.
        AppendRowDataAt(self: ScheduleTableVariantMatrix, row: int, entityId: ObjectId, blockReferencePathIdArray: ObjectIdCollection)
            Appends the row data at the specified row.
        
            row: The row.
            entityId: The id of entity.
            blockReferencePathIdArray: An id array of block reference path.
        AppendRowDataAt(self: ScheduleTableVariantMatrix, row: int, idAndBlockReferencePathContainer: ObjectIdAndBlockReferencePathCollection, sorted: bool)
            Appends the row data at the specified row.
        
            row: The row.
            idAndBlockReferencePathContainer: A container of id and block reference path.
            sorted: Indicates if has been sorted.
        AppendRowDataAt(self: ScheduleTableVariantMatrix, row: int, idAndBlockReferencePathContainer: ObjectIdAndBlockReferencePathCollection)
            Appends the row data at the specified row.
        
            row: The row.
            idAndBlockReferencePathContainer: A container of id and block reference path.
        """
        pass

    def CreateQuantity(self, desiredQuantityColumn, dataColumn, desiredProductColumn, repeatFirstColumn):
        """
        CreateQuantity(self: ScheduleTableVariantMatrix, desiredQuantityColumn: int, dataColumn: int, desiredProductColumn: int, repeatFirstColumn: bool) -> ScheduleTableVariantMatrix
        
            Creates quantity matrix from the given, pre-sorted matrix.
        
            desiredQuantityColumn: The desire quantity column.
            dataColumn: The data column, dataColumn must be a numeric data type.
            desiredProductColumn: The desired product column.
            repeatFirstColumn: Indicates if repeat the first column.
            Returns: Returns quantity matrix from the given, pre-sorted matrix.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetRowDataAt(self, row, sorted=None):
        """
        GetRowDataAt(self: ScheduleTableVariantMatrix, row: int) -> ObjectIdAndBlockReferencePathCollection
        
            Gets the row data at the specifed row index.
        
            row: The row.
        GetRowDataAt(self: ScheduleTableVariantMatrix, row: int, sorted: bool) -> ObjectIdAndBlockReferencePathCollection
        
            Gets the row data at the specifed row index.
        
            row: The row.
            sorted: Indicates if has been sorted.
        """
        pass

    def GetValue(self, row, column, raw=None):
        """
        GetValue(self: ScheduleTableVariantMatrix, row: int, column: int) -> object
        
            Gets the variant at the specifed row and column.
        
            row: The row.
            column: The column.
            Returns: Returns the variant.
        GetValue(self: ScheduleTableVariantMatrix, row: int, column: int, raw: bool) -> object
        
            Gets the variant at the specifed row and column.
        
            row: The row.
            column: The column.
            raw: Determines if the row and column are raw value. When row == false, need 
             indirection via our indexing arrays.
        
            Returns: Returns the variant.
        """
        pass

    def SetValue(self, row, column, variant, raw=None):
        """
        SetValue(self: ScheduleTableVariantMatrix, row: int, column: int, variant: object)
            Sets the value at the speficied row and column.
        
            row: The row.
            column: The column.
            variant: The variant to set.
        SetValue(self: ScheduleTableVariantMatrix, row: int, column: int, variant: object, raw: bool)
            Sets the value at the speficied row and column.
        
            row: The row.
            column: The column.
            variant: The variant to set.
            raw: Determines if the row and column are raw value. When row == false, need 
             indirection via our indexing arrays.
        """
        pass

    def SortedRowIndex(self, row):
        """
        SortedRowIndex(self: ScheduleTableVariantMatrix, row: int) -> int
        
            Gets the row index after being sorted.
        
            row: The input row.
            Returns: Returns the row index after being sorted.
        """
        pass

    def SortRows(self, order):
        """
        SortRows(self: ScheduleTableVariantMatrix, order: Array[ScheduleTableColumnOrder])
            Sorts by row data given order.
        
            order: Input the order.
        SortRows(self: ScheduleTableVariantMatrix, order: ScheduleTableColumnOrder)
            Sorts by row data given order.
        
            order: Input the order.
        """
        pass

    def SwapColumns(self, column1, column2):
        """
        SwapColumns(self: ScheduleTableVariantMatrix, column1: int, column2: int)
            Swaps two columns.
        
            column1: The first column to be swapped.
            column2: The second column to be swapped.
            Returns: Returns a boolean to indicate if the row or column is out of range.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, rows=None, columns=None, styleId=None):
        """
        __new__(cls: type, rows: int, columns: int, styleId: ObjectId)
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    NumberOfColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of columns.

Get: NumberOfColumns(self: ScheduleTableVariantMatrix) -> int

"""

    NumberOfRows = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of rows.

Get: NumberOfRows(self: ScheduleTableVariantMatrix) -> int

"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the style id used.

Get: StyleId(self: ScheduleTableVariantMatrix) -> ObjectId

"""



# variables with complex values

