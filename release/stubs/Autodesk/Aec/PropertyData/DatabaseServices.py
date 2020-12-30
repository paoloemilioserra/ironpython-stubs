# encoding: utf-8
# module Autodesk.Aec.PropertyData.DatabaseServices calls itself DatabaseServices
# from AecPropDataMgd, Version=8.3.53.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AnchorTagToEntity(AnchorToReference):
    """
    Represents a AnchorTagToEntity.
    
    AnchorTagToEntity()
    """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def SetOverride(self, entityId, blockReferencePath):
        """
        SetOverride(self: AnchorTagToEntity, entityId: ObjectId, blockReferencePath: ObjectIdCollection)
            Sets override.
        
            entityId: The entity id.
            blockReferencePath: The block reference path.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    EntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the entity id.

Get: EntityId(self: AnchorTagToEntity) -> ObjectId

Set: EntityId(self: AnchorTagToEntity) = value
"""



class AnchorExtendedTagToEntity(AnchorTagToEntity):
    """
    Represents a AnchorExtendedTagToEntity.
    
    AnchorExtendedTagToEntity()
    """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def SetReferencedEntityId(self, geo):
        """
        SetReferencedEntityId(self: AnchorExtendedTagToEntity, geo: Geo)
            Set referenced entity id.
        
            geo: The geo.
        """
        pass

    def SetReferencedEntityOldEcs(self, mat):
        """
        SetReferencedEntityOldEcs(self: AnchorExtendedTagToEntity, mat: Matrix3d)
            Sets referenced entity old ecs.
        
            mat: The matrix.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AllowIndependentUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets allow independent update.

Get: AllowIndependentUpdate(self: AnchorExtendedTagToEntity) -> bool

Set: AllowIndependentUpdate(self: AnchorExtendedTagToEntity) = value
"""

    ForceHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the force horizontal.

Get: ForceHorizontal(self: AnchorExtendedTagToEntity) -> bool

Set: ForceHorizontal(self: AnchorExtendedTagToEntity) = value
"""

    ReferencedEntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the referenced entity id.

Get: ReferencedEntityId(self: AnchorExtendedTagToEntity) -> ObjectId

Set: ReferencedEntityId(self: AnchorExtendedTagToEntity) = value
"""



class AutomaticPropertyData(object):
    """
    Holds Automatic property data.
    
    AutomaticPropertyData(className: str, sourceName: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, className, sourceName):
        """ __new__(cls: type, className: str, sourceName: str) """
        pass

    ClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassName(self: AutomaticPropertyData) -> str

"""

    SourceName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceName(self: AutomaticPropertyData) -> str

"""



class CaseType(Enum):
    """
    Defines identifiers that indicate the case type.
    
    enum CaseType, values: CaseAsIs (0), CaseLower (2), CaseSentence (3), CaseTitle (4), CaseUpper (1)
    """
    CaseAsIs = None
    CaseLower = None
    CaseSentence = None
    CaseTitle = None
    CaseUpper = None
    value__ = None


class DictionaryPropertyDataFormat(Dictionary):
    """
    Represents a property data format dictionary.
    
    DictionaryPropertyDataFormat(db: Database)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardFormat(db):
        """
        GetStandardFormat(db: Database) -> ObjectId
        
            Get standard format.
        
            db: The database.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryPropertySetDefinitions(Dictionary):
    """
    Represents a property set definition dictionary.
    
    DictionaryPropertySetDefinitions(db: Database)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DictionaryScheduleTableStyle(Dictionary):
    """
    Represents a schedule table style dictionary.
    
    DictionaryScheduleTableStyle(db: Database)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetStandardStyle(db):
        """
        GetStandardStyle(db: Database) -> ObjectId
        
            Gets the standard table style id.
        
            db: The database.
            Returns: The standard table style id.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, db):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class DisplayThemeScheduleDataRule(DisplayThemeRuleBase):
    """
    Represents a display theme schedule data rule.
    
    DisplayThemeScheduleDataRule()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetValidPropertySetDefinitions(db, validAvailablePropertyDefinitionSets):
        """ GetValidPropertySetDefinitions(db: Database) -> (bool, NameObjectIdPairCollection) """
        pass

    def SetPropertyDefinitionId(self, id, isUpdate):
        """
        SetPropertyDefinitionId(self: DisplayThemeScheduleDataRule, id: int, isUpdate: bool)
            Set the id of the property definition.
        
            id: The new id of the property definition.
            isUpdate: Flag that indicates whether it is needed to update.
        """
        pass

    def SetPropertySetDefinitionId(self, id, isUpdate):
        """
        SetPropertySetDefinitionId(self: DisplayThemeScheduleDataRule, id: ObjectId, isUpdate: bool)
            Set the id of the property set definition.
        
            id: The new id of the property set definition.
            isUpdate: Flag that indicates whether it is needed to update.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    PropertyDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the id of the property definition.

Get: PropertyDefinitionId(self: DisplayThemeScheduleDataRule) -> int

"""

    PropertySetDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Retrieve the id of the property set definition.

Get: PropertySetDefinitionId(self: DisplayThemeScheduleDataRule) -> ObjectId

"""



class DisplayThemeScheduleDataRuleParameter(Enum):
    """
    DisplayThemeScheduleDataRuleParameter enumeration.
    
    enum DisplayThemeScheduleDataRuleParameter, values: PropertyDefinitionId (1), PropertySetDefinition (0)
    """
    PropertyDefinitionId = None
    PropertySetDefinition = None
    value__ = None


class DxfData(Enum):
    """
    Defines identifiers that indicate the dxf data type.
    
    enum DxfData, values: DxfId (70), DxfVariantBool (175), DxfVariantBstr (309), DxfVariantEmpty (71), DxfVariantI4 (99), DxfVariantR8 (147)
    """
    DxfId = None
    DxfVariantBool = None
    DxfVariantBstr = None
    DxfVariantEmpty = None
    DxfVariantI4 = None
    DxfVariantR8 = None
    value__ = None


class ForwardedType(Enum):
    """
    Defines identifiers that indicate the forwarded type.
    
    enum ForwardedType, values: External (2), Local (1), Same (0)
    """
    External = None
    Local = None
    Same = None
    value__ = None


class FractionType(Enum):
    """
    Defines identifiers that indicate the fraction type.
    
    enum FractionType, values: Diagonal (1), Horizontal (0), NotStacked (2)
    """
    Diagonal = None
    Horizontal = None
    NotStacked = None
    value__ = None


class GraphicType(Enum):
    """
    Defines identifiers that indicate the graphic type.
    
    enum GraphicType, values: Block (0), Image (1), Object (2)
    """
    Block = None
    Image = None
    Object = None
    value__ = None


class INodeOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: INodeOperation, A_0: ScheduleTableStyleHeaderNode) -> int """
        pass

    def Contains(self, A_0):
        """ Contains(self: INodeOperation, A_0: ScheduleTableStyleHeaderNode) -> bool """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: INodeOperation, A_0: int) -> ScheduleTableStyleHeaderNode """
        pass

    def GetCount(self):
        """ GetCount(self: INodeOperation) -> int """
        pass

    def IndexOf(self, A_0):
        """ IndexOf(self: INodeOperation, A_0: ScheduleTableStyleHeaderNode) -> int """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: INodeOperation, A_0: int, A_1: ScheduleTableStyleHeaderNode) """
        pass

    def Prepend(self, A_0):
        """ Prepend(self: INodeOperation, A_0: ScheduleTableStyleHeaderNode) """
        pass

    def Remove(self, A_0):
        """ Remove(self: INodeOperation, A_0: ScheduleTableStyleHeaderNode) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: INodeOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: INodeOperation, A_0: int) """
        pass

    def SetAt(self, A_0, A_1):
        """ SetAt(self: INodeOperation, A_0: int, A_1: ScheduleTableStyleHeaderNode) """
        pass

    def Shift(self, A_0, A_1):
        """ Shift(self: INodeOperation, A_0: ScheduleTableStyleHeaderNode, A_1: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IScheduleTablePageMaxHeightOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IScheduleTablePageMaxHeightOperation, A_0: float) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IScheduleTablePageMaxHeightOperation, A_0: int) -> float """
        pass

    def GetCount(self):
        """ GetCount(self: IScheduleTablePageMaxHeightOperation) -> int """
        pass

    def IndexOf(self, A_0):
        """ IndexOf(self: IScheduleTablePageMaxHeightOperation, A_0: float) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: IScheduleTablePageMaxHeightOperation, index: int, value: float) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IScheduleTablePageMaxHeightOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IScheduleTablePageMaxHeightOperation, A_0: int) """
        pass

    def SetAt(self, A_0, A_1):
        """ SetAt(self: IScheduleTablePageMaxHeightOperation, A_0: int, A_1: float) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IScheduleTableSortingOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IScheduleTableSortingOperation, A_0: ScheduleTableSorting) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IScheduleTableSortingOperation, A_0: int) -> ScheduleTableSorting """
        pass

    def GetCount(self):
        """ GetCount(self: IScheduleTableSortingOperation) -> int """
        pass

    def IndexOf(self, A_0):
        """ IndexOf(self: IScheduleTableSortingOperation, A_0: ScheduleTableSorting) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: IScheduleTableSortingOperation, index: int, value: ScheduleTableSorting) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IScheduleTableSortingOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IScheduleTableSortingOperation, A_0: int) """
        pass

    def Swap(self, index1, index2):
        """ Swap(self: IScheduleTableSortingOperation, index1: int, index2: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IScheduleTableStyleColumnOperation:
    # no doc
    def Add(self, A_0):
        """ Add(self: IScheduleTableStyleColumnOperation, A_0: ScheduleTableStyleColumn) -> int """
        pass

    def GetAt(self, A_0):
        """ GetAt(self: IScheduleTableStyleColumnOperation, A_0: int) -> ScheduleTableStyleColumn """
        pass

    def GetCount(self):
        """ GetCount(self: IScheduleTableStyleColumnOperation) -> int """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: IScheduleTableStyleColumnOperation, A_0: ScheduleTableStyleColumn) -> int
        IndexOf(self: IScheduleTableStyleColumnOperation, propSetDefId: ObjectId, propId: int) -> int
        """
        pass

    def Insert(self, A_0, A_1):
        """ Insert(self: IScheduleTableStyleColumnOperation, A_0: int, A_1: ScheduleTableStyleColumn) """
        pass

    def Prepend(self, A_0):
        """ Prepend(self: IScheduleTableStyleColumnOperation, A_0: ScheduleTableStyleColumn) """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: IScheduleTableStyleColumnOperation) """
        pass

    def RemoveAt(self, A_0):
        """ RemoveAt(self: IScheduleTableStyleColumnOperation, A_0: int) """
        pass

    def SetAt(self, A_0, A_1):
        """ SetAt(self: IScheduleTableStyleColumnOperation, A_0: int, A_1: ScheduleTableStyleColumn) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class MatrixSymbolType(Enum):
    """
    Defines identifiers that indicate the matrix symbol type.
    
    enum MatrixSymbolType, values: Check (0), Cross (2), Dot (1), Slash (3)
    """
    Check = None
    Cross = None
    Dot = None
    Slash = None
    value__ = None


class PageDirectionType(Enum):
    """
    Defines identifiers that indicate the page direction.
    
    enum PageDirectionType, values: PageDown (1), PageRight (0)
    """
    PageDown = None
    PageRight = None
    value__ = None


class Precision(Enum):
    """
    Defines identifiers that indicate the precision.
    
    enum Precision, values: PrecisionCount (9), PrecisionCountForDegreesMinutesSeconds (7), PrecisionCountForSurveyor (7)
    """
    PrecisionCount = None
    PrecisionCountForDegreesMinutesSeconds = None
    PrecisionCountForSurveyor = None
    value__ = None


class ProjectDataType(Enum):
    """ enum ProjectDataType, values: ProjectDescription (1), ProjectDetails (11), ProjectDivisionId (10), ProjectDivisions (5), ProjectLevelElevation (7), ProjectLevelHeight (8), ProjectLevelId (6), ProjectLevels (4), ProjectLocation (3), ProjectName (0), ProjectNumber (2), ProjectSheetDescription (13), ProjectSheetName (12) """
    ProjectDescription = None
    ProjectDetails = None
    ProjectDivisionId = None
    ProjectDivisions = None
    ProjectLevelElevation = None
    ProjectLevelHeight = None
    ProjectLevelId = None
    ProjectLevels = None
    ProjectLocation = None
    ProjectName = None
    ProjectNumber = None
    ProjectSheetDescription = None
    ProjectSheetName = None
    value__ = None


class PropertyDataFormat(DictionaryRecord):
    """
    Represents a ScheduleDataFormat.
    
    PropertyDataFormat()
    """
    @staticmethod
    def Convert(data, currentUnitType, targetUnitType):
        """
        Convert(data: object, currentUnitType: UnitType, targetUnitType: UnitType) -> object
        
            Convert from one unit type to another unit type.
        
            data: The variant data.
            currentUnitType: The current unit type.
            targetUnitType: The target unit type.
            Returns: System.Object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def DoRoundOff(self, value):
        """
        DoRoundOff(self: PropertyDataFormat, value: float) -> float
        
            Do round off.
        
            value: ?
            Returns: Double.
        """
        pass

    def FormatObject(self, object, *__args):
        """
        FormatObject(self: PropertyDataFormat, object: object, unitType: UnitType, plainText: bool) -> str
        FormatObject(self: PropertyDataFormat, object: object, plainText: bool) -> str
        
            Format object.
        
            plainText: True if is plain text, false otherwise.
            Returns: System.String.
        FormatObject(self: PropertyDataFormat, object: object, unitType: UnitType, es: ErrorStatus, plainText: bool) -> str
        FormatObject(self: PropertyDataFormat, object: object, es: ErrorStatus, plainText: bool) -> str
        """
        pass

    def FormatObjectExtend(self, object, *__args):
        """
        FormatObjectExtend(self: PropertyDataFormat, object: object, plainText: bool) -> str
        FormatObjectExtend(self: PropertyDataFormat, object: object, unitType: UnitType, plainText: bool) -> str
        """
        pass

    def FormatToObject(self, object, unitType=None):
        """
        FormatToObject(self: PropertyDataFormat, object: object) -> object
        
            Format to object.
            Returns: Object.
        FormatToObject(self: PropertyDataFormat, object: object, unitType: UnitType) -> object
        
            Format to object.
        
            unitType: The unit type.
            Returns: Object.
        """
        pass

    @staticmethod
    def FormatValues(readStatus, idPropertyFormat, *__args):
        """
        FormatValues(readStatus: ErrorStatus, idPropertyFormat: ObjectId) -> (bool, object, object)
        FormatValues(readStatus: ErrorStatus, idPropertyFormat: ObjectId, unitType: UnitType) -> (bool, object, object)
        """
        pass

    @staticmethod
    def ReadErrorValueMessage():
        """
        ReadErrorValueMessage() -> str
        
            Get read error value message.
            Returns: Read error value message.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BuiltinType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets built-in type.

Get: BuiltinType(self: PropertyDataFormat) -> BuiltInType

Set: BuiltinType(self: PropertyDataFormat) = value
"""

    Case = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the case.

Get: Case(self: PropertyDataFormat) -> CaseType

Set: Case(self: PropertyDataFormat) = value
"""

    FalseText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the false text.

Get: FalseText(self: PropertyDataFormat) -> str

Set: FalseText(self: PropertyDataFormat) = value
"""

    Fraction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the fraction.

Get: Fraction(self: PropertyDataFormat) -> FractionType

Set: Fraction(self: PropertyDataFormat) = value
"""

    LeadingZeros = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if it is leading zeros.

Get: LeadingZeros(self: PropertyDataFormat) -> bool

Set: LeadingZeros(self: PropertyDataFormat) = value
"""

    NotApplicable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the not applicable string.

Get: NotApplicable(self: PropertyDataFormat) -> str

Set: NotApplicable(self: PropertyDataFormat) = value
"""

    Precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the precision.

Get: Precision(self: PropertyDataFormat) -> Int16

Set: Precision(self: PropertyDataFormat) = value
"""

    Prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the prefix.

Get: Prefix(self: PropertyDataFormat) -> str

Set: Prefix(self: PropertyDataFormat) = value
"""

    RoundingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets rounding mode.

Get: RoundingMode(self: PropertyDataFormat) -> RoundingType

Set: RoundingMode(self: PropertyDataFormat) = value
"""

    RoundOff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the round off.

Get: RoundOff(self: PropertyDataFormat) -> float

Set: RoundOff(self: PropertyDataFormat) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets scale.

Get: Scale(self: PropertyDataFormat) -> float

Set: Scale(self: PropertyDataFormat) = value
"""

    Separator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the separator.

Get: Separator(self: PropertyDataFormat) -> SeparatorType

Set: Separator(self: PropertyDataFormat) = value
"""

    SeparatorComma = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets separator comma.

Get: SeparatorComma(self: PropertyDataFormat) -> SeparatorType

Set: SeparatorComma(self: PropertyDataFormat) = value
"""

    Suffix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the suffix.

Get: Suffix(self: PropertyDataFormat) -> str

Set: Suffix(self: PropertyDataFormat) = value
"""

    TrailingZeros = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if it is trailing zeros.

Get: TrailingZeros(self: PropertyDataFormat) -> bool

Set: TrailingZeros(self: PropertyDataFormat) = value
"""

    TrueText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the true text.

Get: TrueText(self: PropertyDataFormat) -> str

Set: TrueText(self: PropertyDataFormat) = value
"""

    Undefined = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the undefined string.

Get: Undefined(self: PropertyDataFormat) -> str

Set: Undefined(self: PropertyDataFormat) = value
"""

    Units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the units.

Get: Units(self: PropertyDataFormat) -> UnitsType

Set: Units(self: PropertyDataFormat) = value
"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets unit type.

Get: UnitType(self: PropertyDataFormat) -> UnitType

Set: UnitType(self: PropertyDataFormat) = value
"""

    ZeroFeet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if it is zero feet.

Get: ZeroFeet(self: PropertyDataFormat) -> bool

Set: ZeroFeet(self: PropertyDataFormat) = value
"""

    ZeroInches = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if it is zero Inches.

Get: ZeroInches(self: PropertyDataFormat) -> bool

Set: ZeroInches(self: PropertyDataFormat) = value
"""

    ZeroPadding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the zero padding.

Get: ZeroPadding(self: PropertyDataFormat) -> Int16

Set: ZeroPadding(self: PropertyDataFormat) = value
"""



class PropertyDataServices(object):
    """ Represents the property data services. """
    @staticmethod
    def AddExtendedClasses(entityFilter):
        """
        AddExtendedClasses(entityFilter: StringCollection)
            Adds extended classes.
        
            entityFilter: Input entity type names.
        """
        pass

    @staticmethod
    def AddPropertySet(*__args):
        """
        AddPropertySet(obj: DBObject, propertySetDefinitionId: ObjectId)
            Adds the specified property set to the object.
        
            obj: The object.
            propertySetDefinitionId: The property set definition id.
        AddPropertySet(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId)
            Adds the specified property set to the object.
        
            id: The object id.
            idOverrideContainerOwner: The override container owner id.
            blockRefPath: The block ref path.
            propertySetDefinitionId: The property set definition id.
        """
        pass

    @staticmethod
    def DataToString(variantObject):
        """
        DataToString(variantObject: object) -> str
        
            Variant to string.
        
            variantObject: The variant object.
        """
        pass

    @staticmethod
    def ExtractExtendedObjects(id):
        """
        ExtractExtendedObjects(id: ObjectId) -> ObjectIdCollection
        
            This tells which "extended" objects can have PropertySets attached that are 
             applicable to the given object (i.e. for a Door, it will return the DoorStyle). 
             This is an easy way to get the owner of the style-based property sets for a 
             given object.  If you pass in the style's object id, you will get the 
             classifications for the style.
        
        
            id: Input the Object Id to extract the extended objects for.
            Returns: An object id colection containing the supporting objects of the specified 
             object.
        """
        pass

    @staticmethod
    def FindAutomaticSourceNames(objectName, db):
        """
        FindAutomaticSourceNames(objectName: str, db: Database) -> Array[str]
        
            Find automatic source names.
        
            objectName: The object name.
            db: The database.
            Returns: Returns the automatic source names.
        """
        pass

    @staticmethod
    def FindEligibleClassNames():
        """
        FindEligibleClassNames() -> Array[str]
        
            Find the names of the eligible classes to which the schedule table system can 
             apply.
        
            Returns: Returns the eligible class names.
        """
        pass

    @staticmethod
    def FindOverrideContainer(idBlockReference, createIfNotFound):
        """
        FindOverrideContainer(idBlockReference: ObjectId, createIfNotFound: bool) -> ObjectId
        
            Determines the override container for the block reference.
        
            idBlockReference: The block reference id.
            createIfNotFound: Determines if the container is created if not found.
            Returns: Returns the override container for the block reference.
        """
        pass

    @staticmethod
    def FormatValue(idPropertyFormat, unitType, propertyValue, readStatus):
        """
        FormatValue(idPropertyFormat: ObjectId, unitType: UnitType, propertyValue: object, readStatus: ErrorStatus) -> object
        
            Formats the value using the specified property data format.
        
            idPropertyFormat: The property data format id.
            unitType: The unit type.
            propertyValue: The property value to be formatted.
            readStatus: The error status returned in the exception thrown while retrieving the property 
             value, or OK.
        
            Returns: Returns the formatted value as a string.
        """
        pass

    @staticmethod
    def GetAllPropertySetsUsingDefinition(propertySetDefinition, allowErased):
        """
        GetAllPropertySetsUsingDefinition(propertySetDefinition: ObjectId, allowErased: bool) -> ObjectIdCollection
        
            Gets all property sets that use the specified property set definition.
        
            propertySetDefinition: The property set definition id.
            allowErased: Determines if erased property sets are included.
            Returns: Returns all property sets that use the specified property set definition.
        """
        pass

    @staticmethod
    def GetNearestPropertySet(*__args):
        """
        GetNearestPropertySet(id: ObjectId, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId) -> ObjectId
        
            Gets the nearest property set definiton id.
        
            id: Input an object id.
            blockRefPath: Input the block reference path ids.
            propertySetDefinitionId: Input the property set definition id.
            Returns: The nearest property set definiton id.
        GetNearestPropertySet(objectInstance: DBObject, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId) -> ObjectId
        
            Gets the nearest property set definiton id.
        
            objectInstance: Input an open for read database resident object.
            blockRefPath: Input the block reference path ids.
            propertySetDefinitionId: Input the property set definition id.
            Returns: The nearest property set definiton id.
        GetNearestPropertySet(objectInstance: DBObject, propertySetDefinitionId: ObjectId) -> ObjectId
        
            Gets the nearest property set definiton id.
        
            objectInstance: Input an open for read database resident object.
            propertySetDefinitionId: Input the property set definition id.
            Returns: The nearest property set definiton id.
        """
        pass

    @staticmethod
    def GetPropertySet(*__args):
        """
        GetPropertySet(obj: DBObject, propertySetDefinitionId: ObjectId) -> ObjectId
        
            Gets the property set for the specified object and property set definition id.
        
            obj: The object.
            propertySetDefinitionId: The property set definition id.
            Returns: Returns the property set for the specified object and property set definition 
             id.
        
        GetPropertySet(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId) -> ObjectId
        
            Gets the property set for the specified object id, override container, block 
             ref path and property set definition id.
        
        
            id: The object id.
            idOverrideContainerOwner: The override container owner id.
            blockRefPath: The block ref path.
            propertySetDefinitionId: The property set definition id.
            Returns: Returns the property set for the specified object id, override container, block 
             ref path and property set definition id.
        """
        pass

    @staticmethod
    def GetPropertySetDefinitionsUsed(*__args):
        """
        GetPropertySetDefinitionsUsed(obj: DBObject) -> ObjectIdCollection
        
            Gets the ids of the property set definitions used by the object.
        
            obj: The object.
            Returns: Gets the ids of the property set definitions used by the object.
        GetPropertySetDefinitionsUsed(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection) -> ObjectIdCollection
        
            Gets the ids of the property set definitions used for the object.
        
            id: The object id.
            idOverrideContainerOwner: The override container owner id.
            blockRefPath: The block ref path.
            Returns: Returns the ids of the property set definitions used for the object.
        """
        pass

    @staticmethod
    def GetPropertySets(*__args):
        """
        GetPropertySets(obj: DBObject) -> ObjectIdCollection
        
            Gets the property sets for the specified object.
        
            obj: The object.
            Returns: Returns the property sets for the specified object.
        GetPropertySets(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection) -> ObjectIdCollection
        
            Gets the property sets for the specified object id, override container and 
             block ref path.
        
        
            id: The property owner.
            idOverrideContainerOwner: The override container.
            blockRefPath: The block reference path.
            Returns: Returns the property sets for the specified object id, override container and 
             block ref path.
        """
        pass

    @staticmethod
    def GetPropertyValueExt(*__args):
        """
        GetPropertyValueExt(objectId: ObjectId, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, propertyId: int) -> object
        
            Get the property value.
        
            objectId: The object id.
            blockReferencePath: The block reference path.
            propertySetDefinitionId: The property set definition id.
            propertyId: The property id.
        GetPropertyValueExt(dbObject: DBObject, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, propertyId: int) -> object
        
            Get the property value.
        
            dbObject: The database object.
            blockReferencePath: The block reference path.
            propertySetDefinitionId: The property set definition id.
            propertyId: The property id.
        """
        pass

    @staticmethod
    def GetPropertyValueUnitExt(*__args):
        """
        GetPropertyValueUnitExt(objectId: ObjectId, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, globalName: str) -> PropertyValueUnitPair
        
            Get the property value and unit.
        
            objectId: The object id.
            blockReferencePath: The block reference path.
            propertySetDefinitionId: The property set definition id.
            globalName: The global name.
        GetPropertyValueUnitExt(objectId: ObjectId, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, propertyId: int) -> PropertyValueUnitPair
        
            Get the property value and unit.
        
            objectId: The object id.
            blockReferencePath: The block reference path.
            propertySetDefinitionId: The property set definition id.
            propertyId: The property id.
        GetPropertyValueUnitExt(dbObject: DBObject, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, propertyId: int, searchByName: bool) -> PropertyValueUnitPair
        
            Get the property value and unit.
        
            dbObject: The database object.
            blockReferencePath: The block reference path.
            propertySetDefinitionId: The property set definition id.
            propertyId: The property id.
            searchByName: If search by name.
        GetPropertyValueUnitExt(dbObject: DBObject, blockReferencePath: ObjectIdCollection, propertySetDefinitionId: ObjectId, propertyId: int) -> PropertyValueUnitPair
        
            Get the property value and unit.
        
            dbObject: The database object.
            blockReferencePath: The block reference path.
            propertySetDefinitionId: The property set definition id.
            propertyId: The property id.
        """
        pass

    @staticmethod
    def PropertyExists(db, fullPropertyName, propertyId):
        """
        PropertyExists(db: Database, fullPropertyName: str) -> (ObjectId, int)
        
            Determines whether a property exists.
        
            db: Input database.
            fullPropertyName: Input string representing the full property name. (This format includes the 
             definition and set names in like the format from a tag.)
        
            Returns: The object id of the property set definition.
        """
        pass

    @staticmethod
    def PurgeDuplicatePropertySets(obj, verbose):
        """
        PurgeDuplicatePropertySets(obj: DBObject, verbose: bool)
            Purges duplicate property sets.
        
            obj: The object.
            verbose: Determines if messages are displayed.
        """
        pass

    @staticmethod
    def RemovePropertySet(*__args):
        """
        RemovePropertySet(obj: DBObject, propertySetDefinitionId: ObjectId)
            Removes the specified property set from the object.
        
            obj: The object.
            propertySetDefinitionId: The property set definition id.
        RemovePropertySet(id: ObjectId, idOverrideContainerOwner: ObjectId, blockRefPath: ObjectIdCollection, propertySetDefinitionId: ObjectId)
            Removes the specified property set from the object.
        
            id: The object id.
            idOverrideContainerOwner: The override container owner id.
            blockRefPath: The block ref path.
            propertySetDefinitionId: The property set definition id.
        """
        pass

    @staticmethod
    def ResolvePropertySetLocations(originalIds, resolvedIds, forwardedIds, duplicateIds):
        """ ResolvePropertySetLocations(originalIds: ObjectIdCollection) -> (ObjectIdCollection, ObjectIdCollection, ObjectIdCollection) """
        pass

    @staticmethod
    def ResolvePropertySetLocationsAndFilterLockedLayers(originalIds, resolvedIds, forwardedIds, duplicateIds, lockedIds, speak):
        """ ResolvePropertySetLocationsAndFilterLockedLayers(originalIds: ObjectIdCollection, speak: bool) -> (ObjectIdCollection, ObjectIdCollection, ObjectIdCollection, ObjectIdCollection) """
        pass

    @staticmethod
    def SearchPathForPropertySet(*__args):
        """
        SearchPathForPropertySet(object: DBObject, blockRefPathIds: ObjectIdCollection, propertySetName: str) -> ObjectId
        
            Returns the property set id found based on input parameters.
        
            object: Input object. Must be open for read.
            blockRefPathIds: Input block reference path ids.
            propertySetName: Input property set name.
            Returns: Property set id.
        SearchPathForPropertySet(entityId: ObjectId, blockRefPathIds: ObjectIdCollection, propertySetName: str) -> ObjectId
        
            Returns the property set id found based on input parameters.
        
            entityId: Input entity id.
            blockRefPathIds: Input block ref path.
            propertySetName: Input property set name.
            Returns: Property set id.
        """
        pass

    @staticmethod
    def UsePropertySetExclusive(propertySetDefinitionId, entityFilter, filterReadOnlySets, filterHiddenSets, includeExtendedClasses, matchTypes, entitiesAreStyles):
        """
        UsePropertySetExclusive(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool
        
            Determines if a property set definition applies to ALL of the entity types in 
             the entity filter.
        
        
            propertySetDefinitionId: Input the object id for the property set definition.
            entityFilter: Input a string collection of entity type names to query for.
            filterReadOnlySets: Input true to indicate a read-only PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            filterHiddenSets: Input true to indicate a hidden PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            includeExtendedClasses: Input true to include "extended" classes (i.e. styles) in the query.
            matchTypes: Input true to match the property set with the type of entities in entityFilter. 
             For example, if matchTypes == true, and entityFilter contains entities ( 
             entitiesAreStyles == false ), and propSetDef applies to styles (styleBased == 
             true), then this returns false.
        
            entitiesAreStyles: Input true to indicate that the objects in the entityFilter are styles, not 
             entities.
        
            Returns: True if a property set applies to ALL of the entity type names, or false 
             otherwise.
        """
        pass

    @staticmethod
    def UsePropertySetExclusiveMatchClassifications(propertySetDefinitionId, entityFilter, matchingClassifications, filterReadOnlySets, filterHiddenSets, includeExtendedClasses, matchTypes, entitiesAreStyles):
        """
        UsePropertySetExclusiveMatchClassifications(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, matchingClassifications: ClassificationCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool
        
            Determines if a property set definition applies to ALL of the entity type names 
             in an entity filter, and ALL of the input classifications match the 
             classifications of the property set definition.  A first pass is done using 
             UsePropertySetExclusive, so please see its description for additional 
             information.
        
        
            propertySetDefinitionId: Input the object id for the property set definition.
            entityFilter: Input a string collection of entity type names to query for.
            matchingClassifications: Input thje classifications to query for.
            filterReadOnlySets: Input true to indicate a read-only PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            filterHiddenSets: Input true to indicate a hidden PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            includeExtendedClasses: Input true to include "extended" classes (i.e. styles) in the query.
            matchTypes: Input true to match the property set with the type of entities in entityFilter. 
             For example, if matchTypes == true, and entityFilter contains entities ( 
             entitiesAreStyles == false ), and propSetDef applies to styles (styleBased == 
             true), then this returns false.
        
            entitiesAreStyles: Input true to indicate that the objects in the entityFilter are styles, not 
             entities.
        
            Returns: True if it applies to ALL of the entity type names specified and matches ALL of 
             the classifications, or false otherwise.
        """
        pass

    @staticmethod
    def UsePropertySetExclusiveMatchEntityClassifications(propertySetDefinitionId, entityFilter, matchingEntities, filterReadOnlySets, filterHiddenSets, includeExtendedClasses, matchTypes, entitiesAreStyles):
        """
        UsePropertySetExclusiveMatchEntityClassifications(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, matchingEntities: ObjectIdCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool
        
            Determines if a property set definition applies to ALL of the entity type names 
             in an entity filter, and ALL of the entities in the input id array have the 
             same classifications as the property set definition.  A first pass is done 
             using UsePropertySetExclusive, so please see its description for additional 
             information.
        
        
            propertySetDefinitionId: Input the object id for the property set definition.
            entityFilter: Input a string collection of entity type names to query for.
            matchingEntities: ?= Input thje classifications to query for.
            filterReadOnlySets: Input true to indicate a read-only PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            filterHiddenSets: Input true to indicate a hidden PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            includeExtendedClasses: Input true to include "extended" classes (i.e. styles) in the query.
            matchTypes: Input true to match the property set with the type of entities in entityFilter. 
             For example, if matchTypes == true, and entityFilter contains entities ( 
             entitiesAreStyles == false ), and propSetDef applies to styles (styleBased == 
             true), then this returns false.
        
            entitiesAreStyles: Input true to indicate that the objects in the entityFilter are styles, not 
             entities.
        
            Returns: True if it applies to ALL of the entity type names specified and matches ALL of 
             the entity classifications, or false otherwise.
        """
        pass

    @staticmethod
    def UsePropertySetInclusive(propertySetDefinitionId, entityFilter, filterReadOnlySets, filterHiddenSets, includeExtendedClasses, matchTypes, entitiesAreStyles):
        """
        UsePropertySetInclusive(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool
        
            Determines if a property set definition applies to ANY of the entity types in 
             the entity filter.
        
        
            propertySetDefinitionId: Input the object id for the property set definition.
            entityFilter: Input a string collection of entity type names to query for.
            filterReadOnlySets: Input true to indicate a read-only PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            filterHiddenSets: Input true to indicate a hidden PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            includeExtendedClasses: Input true to include "extended" classes (i.e. styles) in the query.
            matchTypes: Input true to match the property set with the type of entities in entityFilter. 
             For example, if matchTypes == true, and entityFilter contains entities ( 
             entitiesAreStyles == false ), and propSetDef applies to styles (styleBased == 
             true), then this returns false.
        
            entitiesAreStyles: Input true to indicate that the objects in the entityFilter are styles, not 
             entities.
        
            Returns: True if a property set applies to ANY of the entity types, or false otherwise.
        """
        pass

    @staticmethod
    def UsePropertySetInclusiveMatchClassifications(propertySetDefinitionId, entityFilter, matchingClassifications, filterReadOnlySets, filterHiddenSets, includeExtendedClasses, matchTypes, entitiesAreStyles):
        """
        UsePropertySetInclusiveMatchClassifications(propertySetDefinitionId: ObjectId, entityFilter: StringCollection, matchingClassifications: ClassificationCollection, filterReadOnlySets: bool, filterHiddenSets: bool, includeExtendedClasses: bool, matchTypes: bool, entitiesAreStyles: bool) -> bool
        
            Determines if a property set definition applies to ANY of the entity type names 
             in an entity filter, and ALL of the input classifications match the 
             classifications of the property set definition.  A first pass is done using 
             UsePropertySetInclusive, so please see its description for additional 
             information.
        
        
            propertySetDefinitionId: Input the object id for the property set definition.
            entityFilter: Input a string collection of entity type names to query for.
            matchingClassifications: Input thje classifications to query for.
            filterReadOnlySets: Input true to indicate a read-only PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            filterHiddenSets: Input true to indicate a hidden PropertySetDefinition should be ignored. 
             Returns false if PropertySetDefinition is read-only.
        
            includeExtendedClasses: Input true to include "extended" classes (i.e. styles) in the query.
            matchTypes: Input true to match the property set with the type of entities in entityFilter. 
             For example, if matchTypes == true, and entityFilter contains entities ( 
             entitiesAreStyles == false ), and propSetDef applies to styles (styleBased == 
             true), then this returns false.
        
            entitiesAreStyles: Input true to indicate that the objects in the entityFilter are styles, not 
             entities.
        
            Returns: True if it applies to ANY of the entity type names specified and matches ALL of 
             the classifications, or false otherwise.
        """
        pass


class PropertyDefinition(ImpObject):
    """
    Represents a property definition.
    
    PropertyDefinition()
    """
    def ClearAutomaticData(self):
        """
        ClearAutomaticData(self: PropertyDefinition)
            Clears automatic data.
        """
        pass

    def ClearFieldData(self):
        """
        ClearFieldData(self: PropertyDefinition)
            Clears the field data.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetAutomaticData(self):
        """
        GetAutomaticData(self: PropertyDefinition) -> Array[AutomaticPropertyData]
        
            Gets the automatic data.
            Returns: Returns the automatic data.
        """
        pass

    def GetFieldGeneratedData(self, asFieldCode):
        """
        GetFieldGeneratedData(self: PropertyDefinition, asFieldCode: bool) -> object
        
            Get the field generated data.
        
            asFieldCode: Determines if the value returned is a field code or text.
            Returns: Returns the field generated data, or null if not found.
        """
        pass

    def GetFieldId(self):
        """
        GetFieldId(self: PropertyDefinition) -> ObjectId
        
            Get the field id.
        """
        pass

    def GetSampleValue(self, unitType=None):
        """
        GetSampleValue(self: PropertyDefinition) -> object
        
            Gets a sample value.
        GetSampleValue(self: PropertyDefinition, unitType: UnitType) -> object
        
            Gets a sample value for the given unit type.
        
            unitType: The unit type.
        """
        pass

    @staticmethod
    def References(propertySetDefinitionId, propertyDefinitionId, propertySetDefinitionId2, propertyDefinitionId2):
        """
        References(propertySetDefinitionId: ObjectId, propertyDefinitionId: int, propertySetDefinitionId2: ObjectId, propertyDefinitionId2: int) -> bool
        
            Determines if this property definition references the specified property 
             definition.
        
        
            propertySetDefinitionId: The other property set definition.
            propertyDefinitionId: The other property definition Id.
            propertySetDefinitionId2: This property set definition.
            propertyDefinitionId2: This property definition Id.
            Returns: Returns true if this property definition references the specified property 
             definition.
        """
        pass

    def RemoveAutomaticData(self, className):
        """
        RemoveAutomaticData(self: PropertyDefinition, className: str)
            Removes automatic data based on the class name.
        
            className: The class name to search for.
        """
        pass

    def SetAutomaticData(self, className, sourceName):
        """
        SetAutomaticData(self: PropertyDefinition, className: str, sourceName: str)
            Sets automatic data. If the function name is not found, a KeyNotFound exception 
             is thrown.
        
        
            className: The object type name. This is a string similar to the AppliesTo values. It is 
             the internal class/type name. For example: AecDbWall.
        
            sourceName: The source name. This is the same name (aka function name) as provided in the 
             ACA UI.
        """
        pass

    def Synchronize(self, propertySet, definition, attachedTo):
        """
        Synchronize(self: PropertyDefinition, propertySet: PropertySet, definition: PropertySetDefinition, attachedTo: DBObject)
            Synchronizes the property definition by updating its state.
        
            propertySet: The property set.
            definition: The property set definition.
            attachedTo: The object attached to.
        """
        pass

    def Value(self, *__args):
        """
        Value(self: PropertyDefinition, id: ObjectId, blockRefPath: ObjectIdCollection) -> object
        
            Determines the value of the property.
        
            id: The id of the object.
            blockRefPath: The block reference paths Ids.
            Returns: Returns the value of the property, or null if not found.
        Value(self: PropertyDefinition, dbObject: DBObject, blockRefPath: ObjectIdCollection) -> object
        
            Determines the value of the property.
        
            dbObject: The object.
            blockRefPath: The block reference paths Ids.
            Returns: Returns the value of the property, or null if not found.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Automatic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the value indicating if the property is automatic.

Get: Automatic(self: PropertyDefinition) -> bool

Set: Automatic(self: PropertyDefinition) = value
"""

    ContainsFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value that indicates if the property definition contains fields.

Get: ContainsFields(self: PropertyDefinition) -> bool

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the data type.

Get: DataType(self: PropertyDefinition) -> DataType

Set: DataType(self: PropertyDefinition) = value
"""

    DefaultData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default data.

Get: DefaultData(self: PropertyDefinition) -> object

Set: DefaultData(self: PropertyDefinition) = value
"""

    DefaultIsUnspecified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value indicating if the default value is unspecified.

Get: DefaultIsUnspecified(self: PropertyDefinition) -> bool

Set: DefaultIsUnspecified(self: PropertyDefinition) = value
"""

    DisplayOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display order of the property definition.

Get: DisplayOrder(self: PropertyDefinition) -> int

"""

    ExampleString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the example string.

Get: ExampleString(self: PropertyDefinition) -> str

"""

    FieldBucketId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the field code Id.

Get: FieldBucketId(self: PropertyDefinition) -> str

"""

    FormatId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the format Id.

Get: FormatId(self: PropertyDefinition) -> ObjectId

Set: FormatId(self: PropertyDefinition) = value
"""

    FormatString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the format string.

Get: FormatString(self: PropertyDefinition) -> str

"""

    GlobalName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the global name.

Get: GlobalName(self: PropertyDefinition) -> str

Set: GlobalName(self: PropertyDefinition) = value
"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the Id.

Get: Id(self: PropertyDefinition) -> int

Set: Id(self: PropertyDefinition) = value
"""

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the property definition is locked.

Get: IsLocked(self: PropertyDefinition) -> bool

Set: IsLocked(self: PropertyDefinition) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the property definition is read-only.

Get: IsReadOnly(self: PropertyDefinition) -> bool

Set: IsReadOnly(self: PropertyDefinition) = value
"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the property definition is visible.

Get: IsVisible(self: PropertyDefinition) -> bool

Set: IsVisible(self: PropertyDefinition) = value
"""

    ListDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the list definition id.

Get: ListDefinitionId(self: PropertyDefinition) -> ObjectId

Set: ListDefinitionId(self: PropertyDefinition) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name.

Get: Name(self: PropertyDefinition) -> str

Set: Name(self: PropertyDefinition) = value
"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the unit type.

Get: UnitType(self: PropertyDefinition) -> UnitType

Set: UnitType(self: PropertyDefinition) = value
"""



class PropertyDefinitionAnchor(PropertyDefinition):
    """
    Represents an anchor property definition.
    
    PropertyDefinitionAnchor()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def ExtractAnchoredToObject(A_0):
        """
        ExtractAnchoredToObject(A_0: Geo) -> ObjectId
        
            Extracts the object id of the anchored to object.
            Returns: The object id of the anchored to object.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DisplayString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display string.

Get: DisplayString(self: PropertyDefinitionAnchor) -> str

"""

    PropertyDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the id of the property definition inside the property set definition to which it references.

Get: PropertyDefinitionId(self: PropertyDefinitionAnchor) -> UInt32

Set: PropertyDefinitionId(self: PropertyDefinitionAnchor) = value
"""

    PropertySetDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object id of the property set definition to which it references.

Get: PropertySetDefinitionId(self: PropertyDefinitionAnchor) -> ObjectId

Set: PropertySetDefinitionId(self: PropertyDefinitionAnchor) = value
"""

    UsePropertyDefinitionNamesForDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the property definition names, to which it references, should be used for description.

Get: UsePropertyDefinitionNamesForDescription(self: PropertyDefinitionAnchor) -> bool

Set: UsePropertyDefinitionNamesForDescription(self: PropertyDefinitionAnchor) = value
"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this property definition is valid.

Get: Valid(self: PropertyDefinitionAnchor) -> bool

"""



class PropertyDefinitionClassification(PropertyDefinition):
    """
    Represents a classification property definition.
    
    PropertyDefinitionClassification()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ClassificationDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object id of the classification definition to which it references.

Get: ClassificationDefinitionId(self: PropertyDefinitionClassification) -> ObjectId

Set: ClassificationDefinitionId(self: PropertyDefinitionClassification) = value
"""

    PropertyDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the id of the property definition inside the property set definition to which it references.

Get: PropertyDefinitionId(self: PropertyDefinitionClassification) -> UInt32

Set: PropertyDefinitionId(self: PropertyDefinitionClassification) = value
"""

    PropertySetDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object id of the property set definition to which it references.

Get: PropertySetDefinitionId(self: PropertyDefinitionClassification) -> ObjectId

Set: PropertySetDefinitionId(self: PropertyDefinitionClassification) = value
"""

    UseClassificationNamesForDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the classification definition names, to which it references, should be used for description.

Get: UseClassificationNamesForDescription(self: PropertyDefinitionClassification) -> bool

Set: UseClassificationNamesForDescription(self: PropertyDefinitionClassification) = value
"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this property definition is valid.

Get: Valid(self: PropertyDefinitionClassification) -> bool

"""



class PropertyDefinitionCollection(object):
    """ Represents a collection of property definitions. """
    def Add(self, value):
        """
        Add(self: PropertyDefinitionCollection, value: PropertyDefinition) -> int
        
            Adds the specified item to the collection.
        
            value: The item to add.
            Returns: The number of items in the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: PropertyDefinitionCollection)
            Removes all items from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: PropertyDefinitionCollection, value: PropertyDefinition) -> bool
        
            Determines if the collection contains the specified item.
        
            value: The item.
            Returns: Returns true if the collection contains the specified item.
        """
        pass

    def CopyTo(self, array, start):
        """
        CopyTo(self: PropertyDefinitionCollection, array: Array[PropertyDefinition], start: int)
            Copies the collection to the PropertyDefinition array.
        
            array: The PropertyDefinition array.
            start: The start index to begin copying.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PropertyDefinitionCollection) -> IEnumerator
        
            Gets the enumerator for this collection.
            Returns: Returns the enumerator for this collection.
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: PropertyDefinitionCollection, value: PropertyDefinition) -> int
        
            Determines the index of the specified item.
        
            value: The item.
            Returns: Returns the index of the specified item.
        IndexOf(self: PropertyDefinitionCollection, propertyName: str) -> int
        
            Determines the index of the property set with the specifed name.
        
            propertyName: The name of the property set.
            Returns: Returns the index of the property set with the specifed name.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: PropertyDefinitionCollection, index: int, value: PropertyDefinition)
            Inserts the specified item into the collection at the specified index.
        
            index: The index to insert the item at.
            value: The item to insert.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: PropertyDefinitionCollection, value: PropertyDefinition)
            Removes the specified item from the collection.
        
            value: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: PropertyDefinitionCollection, index: int)
            Removes an item from the collection at the specified index.
        
            index: The index of the item to remove.
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in the collection.

Get: Count(self: PropertyDefinitionCollection) -> int

"""



class PropertyDefinitionFormula(PropertyDefinition):
    """
    Represents a formula property definition.
    
    PropertyDefinitionFormula()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetFormulaString(self):
        """
        GetFormulaString(self: PropertyDefinitionFormula) -> str
        
            Gets the formula string.
            Returns: Returns the formula string.
        """
        pass

    def SetFormulaString(self, formulaString):
        """
        SetFormulaString(self: PropertyDefinitionFormula, formulaString: str) -> bool
        
            Sets the formula string.
            Returns: True if the formula string is correctly parsed.
        """
        pass

    def Value(self, *__args):
        """
        Value(self: PropertyDefinitionFormula, dbObject: DBObject, blockRefPath: ObjectIdCollection, quantity: int) -> object
        
            Gets the value by evaluating the formula with specified quantity.
        
            dbObject: The object.
            blockRefPath: The block reference path ids.
            quantity: The quantity.
            Returns: The value of the calculation.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DataItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets data items which support the formula calculation.

Get: DataItems(self: PropertyDefinitionFormula) -> Array[PropertyDefinitionFormulaDataItem]

"""

    DisplayString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display string of the formula.

Get: DisplayString(self: PropertyDefinitionFormula) -> str

"""

    DisplayStringClean = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display string of the formula. This property differs from the DisplayString property by removing the helper strings from the formula. E.g. &gt;Helper&lt;,&gt;/Helper&lt;

Get: DisplayStringClean(self: PropertyDefinitionFormula) -> str

"""

    EnableQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether this formula can contain quantity property.

Get: EnableQuantity(self: PropertyDefinitionFormula) -> bool

Set: EnableQuantity(self: PropertyDefinitionFormula) = value
"""

    FormulaString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the formula string. This is the equivalent of GetFormulaString().

Get: FormulaString(self: PropertyDefinitionFormula) -> str

"""

    HasQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this formula contains quantity property.

Get: HasQuantity(self: PropertyDefinitionFormula) -> bool

"""

    UseFormulaForDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the formula string should be used as description of this property.

Get: UseFormulaForDescription(self: PropertyDefinitionFormula) -> bool

Set: UseFormulaForDescription(self: PropertyDefinitionFormula) = value
"""



class PropertyDefinitionFormulaDataItem(ImpObject):
    """ Represents the data of an item inside formula property definition. """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetSampleToDefault(self):
        """
        SetSampleToDefault(self: PropertyDefinitionFormulaDataItem)
            Sets the sample data to its default value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    DisplayString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display string of the data item.

Get: DisplayString(self: PropertyDefinitionFormulaDataItem) -> str

"""

    FormatId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the property format id.

Get: FormatId(self: PropertyDefinitionFormulaDataItem) -> ObjectId

Set: FormatId(self: PropertyDefinitionFormulaDataItem) = value
"""

    IsProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this data item is a property item.

Get: IsProperty(self: PropertyDefinitionFormulaDataItem) -> bool

"""

    IsQuantity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this data item is a quantity item.

Get: IsQuantity(self: PropertyDefinitionFormulaDataItem) -> bool

"""

    Sample = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sample data.

Get: Sample(self: PropertyDefinitionFormulaDataItem) -> object

Set: Sample(self: PropertyDefinitionFormulaDataItem) = value
"""



class PropertyDefinitionGraphic(PropertyDefinition):
    """
    Represents a graphic property definition.
    
    PropertyDefinitionGraphic()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetDisplayString(self, graphicType):
        """
        GetDisplayString(self: PropertyDefinitionGraphic, graphicType: GraphicType) -> str
        
            Gets the display string of the specified graphic type.
        """
        pass

    def SetImageFileName(self, fileName, fileNameStripped):
        """
        SetImageFileName(self: PropertyDefinitionGraphic, fileName: str, fileNameStripped: str)
            Sets the image name.
        
            fileName: The image name.
            fileNameStripped: The stripped image name.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    BlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object id of the block to which it references.

Get: BlockId(self: PropertyDefinitionGraphic) -> ObjectId

Set: BlockId(self: PropertyDefinitionGraphic) = value
"""

    BlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the block name.

Get: BlockName(self: PropertyDefinitionGraphic) -> str

Set: BlockName(self: PropertyDefinitionGraphic) = value
"""

    GraphicType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the graphic type.

Get: GraphicType(self: PropertyDefinitionGraphic) -> GraphicType

Set: GraphicType(self: PropertyDefinitionGraphic) = value
"""

    ImageFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the image file name.

Get: ImageFileName(self: PropertyDefinitionGraphic) -> str

Set: ImageFileName(self: PropertyDefinitionGraphic) = value
"""

    ImageFileNameStripped = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the stripped image file name.

Get: ImageFileNameStripped(self: PropertyDefinitionGraphic) -> str

"""

    LayerKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the layer key.

Get: LayerKey(self: PropertyDefinitionGraphic) -> str

Set: LayerKey(self: PropertyDefinitionGraphic) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation.

Get: Rotation(self: PropertyDefinitionGraphic) -> float

Set: Rotation(self: PropertyDefinitionGraphic) = value
"""

    SupportedImageTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the supported image types.

Get: SupportedImageTypes(self: PropertyDefinitionGraphic) -> str

"""

    UsePropertyDefinitionNamesForDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the property definition names, to which it references, should be used for description.

Get: UsePropertyDefinitionNamesForDescription(self: PropertyDefinitionGraphic) -> bool

Set: UsePropertyDefinitionNamesForDescription(self: PropertyDefinitionGraphic) = value
"""



class PropertyDefinitionLocation(PropertyDefinition):
    """
    Represents a location property definition.
    
    PropertyDefinitionLocation()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetAppliesTo(self, A_0):
        """
        SetAppliesTo(self: PropertyDefinitionLocation, A_0: str)
            Sets the class type to which this location property applies using the class 
             name.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AppliesTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the class type to which this location property applies.

Get: AppliesTo(self: PropertyDefinitionLocation) -> RXClass

Set: AppliesTo(self: PropertyDefinitionLocation) = value
"""

    DisplayString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the display string.

Get: DisplayString(self: PropertyDefinitionLocation) -> str

"""

    PropertyDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the id of the property definition inside the property set definition to which it references.

Get: PropertyDefinitionId(self: PropertyDefinitionLocation) -> UInt32

Set: PropertyDefinitionId(self: PropertyDefinitionLocation) = value
"""

    PropertySetDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the object id of the property set definition to which it references.

Get: PropertySetDefinitionId(self: PropertyDefinitionLocation) -> ObjectId

Set: PropertySetDefinitionId(self: PropertyDefinitionLocation) = value
"""

    UsePropertyDefinitionNamesForDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the property definition names, to which it references, should be used for description.

Get: UsePropertyDefinitionNamesForDescription(self: PropertyDefinitionLocation) -> bool

Set: UsePropertyDefinitionNamesForDescription(self: PropertyDefinitionLocation) = value
"""

    Valid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets whether this property definition is valid.

Get: Valid(self: PropertyDefinitionLocation) -> bool

"""



class PropertyDefinitionProject(PropertyDefinition):
    """
    Represents a project property definition.
    
    PropertyDefinitionProject()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetDisplayString(self, dataType):
        """
        GetDisplayString(self: PropertyDefinitionProject, dataType: ProjectDataType) -> str
        
            Gets the display string of the specified project data type.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ProjectDataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the project data type.

Get: ProjectDataType(self: PropertyDefinitionProject) -> ProjectDataType

Set: ProjectDataType(self: PropertyDefinitionProject) = value
"""

    ProjectDetailCategory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the project detail category.

Get: ProjectDetailCategory(self: PropertyDefinitionProject) -> str

Set: ProjectDetailCategory(self: PropertyDefinitionProject) = value
"""

    ProjectDetailName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the project detail name.

Get: ProjectDetailName(self: PropertyDefinitionProject) -> str

Set: ProjectDetailName(self: PropertyDefinitionProject) = value
"""

    UseProjectInfoForDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the project information should be used for description.

Get: UseProjectInfoForDescription(self: PropertyDefinitionProject) -> bool

Set: UseProjectInfoForDescription(self: PropertyDefinitionProject) = value
"""



class PropertySet(DictionaryRecord):
    """
    Represents a property set.
    
    PropertySet()
    """
    @staticmethod
    def CompareAlphaIncrementValues(string1, string2):
        """
        CompareAlphaIncrementValues(string1: str, string2: str) -> int
        
            Compares two alpha-increment values.
        
            string1: The first alpha-increment value.
            string2: The second alpha-increment value.
            Returns: A value representing the result of the comparison.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAt(self, *__args):
        """
        GetAt(self: PropertySet, propertyId: int, dbObject: DBObject) -> object
        
            Gets the property data for the specified property id.
        
            propertyId: The property id.
            dbObject: The object.
            Returns: Returns the property data for the specified property id, or null if not found.
        GetAt(self: PropertySet, propertyId: int, unitType: UnitType) -> object
        
            Gets the property data for the specified property id.
        
            propertyId: The property id.
            unitType: The unit type.
            Returns: Returns the property data for the specified property id, or null if not found.
        GetAt(self: PropertySet, propertyId: int) -> object
        
            Gets the property data for the specified property id.
        
            propertyId: The property id.
            Returns: Returns the property data for the specified property id, or null if not found.
        GetAt(self: PropertySet, dbObject: DBObject, blockRefPath: ObjectIdCollection, propertyId: int, unitType: UnitType) -> object
        
            Gets the property data indicated by the specified object, block reference 
             paths, property id and unit type.
        
        
            dbObject: The object.
            blockRefPath: The collection of block reference paths to uniquely refer to the object.
            propertyId: The property id.
            Returns: Returns the property data indicated by the specified object, block reference 
             paths, property id and unit type, or null if not found.
        
        GetAt(self: PropertySet, dbObject: DBObject, blockRefPath: ObjectIdCollection, propertyId: int) -> object
        
            Gets the property data indicated by the specified object, block reference 
             paths, and property id.
        
        
            dbObject: The object.
            blockRefPath: The collection of block reference paths to uniquely refer to the object.
            propertyId: The property id.
            Returns: Returns the property data indicated by the specified object, block reference 
             paths, and property id, or null if not found.
        
        GetAt(self: PropertySet, id: ObjectId, blockRefPath: ObjectIdCollection, propertyId: int) -> object
        
            Gets the property data indicated by the specified object id, block reference 
             paths, and property id.
        
        
            id: The object id.
            blockRefPath: The collection of block reference paths to uniquely refer to the object.
            propertyId: The property id.
            Returns: Returns the property data indicated by the specified object id, block reference 
             paths, and property id, or null if not found.
        """
        pass

    def GetCurrentAlphaIncrementValue(self, propertySetDefinition, propertyId):
        """
        GetCurrentAlphaIncrementValue(self: PropertySet, propertySetDefinition: PropertySetDefinition, propertyId: int) -> str
        
            Gets the current alpha-increment value.
        
            propertySetDefinition: The property set definition.
            propertyId: The property id.
            Returns: Returns the current alpha-increment value.
        """
        pass

    def GetCurrentAutoIncrementValue(self, propertySetDefinition, propertyId):
        """
        GetCurrentAutoIncrementValue(self: PropertySet, propertySetDefinition: PropertySetDefinition, propertyId: int) -> int
        
            Gets the highest value across all property sets that use the specified 
             definition.
        
        
            propertySetDefinition: The property set definition.
            propertyId: The property id.
            Returns: Returns the current auto-increment value.
        """
        pass

    def GetPropertySetDataAt(self, propertyId):
        """
        GetPropertySetDataAt(self: PropertySet, propertyId: int) -> PropertySetData
        
            Gets the property set data for the specified property.
        
            propertyId: The property id.
            Returns: Returns the property set data for the specified property.
        """
        pass

    def GetValueAndUnitAt(self, *__args):
        """
        GetValueAndUnitAt(self: PropertySet, propertyId: int) -> PropertyValueUnitPair
        
            Gets the property value and unit type for the specified property id.
        
            propertyId: The property id.
            Returns: Returns the property value and unit type for the specified property id, or null 
             if not found.
        
        GetValueAndUnitAt(self: PropertySet, id: ObjectId, blockRefPath: ObjectIdCollection, propertyId: int) -> PropertyValueUnitPair
        
            Gets the property value and unit type for the specified property id.
        
            id: The object id.
            blockRefPath: The collection of block reference paths to uniquely refer to the object.
            propertyId: The property id.
            Returns: Returns the property value and unit type for the specified property id, or null 
             if not found.
        """
        pass

    @staticmethod
    def IncrementAlphaValue(alpha):
        """
        IncrementAlphaValue(alpha: str) -> str
        
            Increments the specified alphabetical value.
        
            alpha: The alphabetical value.
            Returns: The incremented alphabetical value.
        """
        pass

    def PropertyIdToName(self, propertyId):
        """
        PropertyIdToName(self: PropertySet, propertyId: int) -> str
        
            Gets the property name for the specified property id.
        
            propertyId: The property id.
            Returns: Returns the property name for the specified property id.
        """
        pass

    def PropertyNameToId(self, name):
        """
        PropertyNameToId(self: PropertySet, name: str) -> int
        
            Gets the id for the specified property name.
        
            name: The property name.
            Returns: Returns the id for the specified property name.
        """
        pass

    def SetAt(self, propertyId, data, unitType=None):
        """
        SetAt(self: PropertySet, propertyId: int, data: object)
            Sets the property data for the specified property id.
        
            propertyId: The property id.
            data: The property data value.
        SetAt(self: PropertySet, propertyId: int, data: bool)
            Sets the property data for the specified property id.
        
            propertyId: The property id.
            data: The property data value.
        SetAt(self: PropertySet, propertyId: int, data: str)
            Sets the property data for the specified property id.
        
            propertyId: The property id.
            data: The property data value.
        SetAt(self: PropertySet, propertyId: int, data: object, unitType: UnitType)
            Sets the property data for the specified property id.
        
            propertyId: The property id.
            data: The property data value.
            unitType: The unit type.
        SetAt(self: PropertySet, propertyId: int, data: float, unitType: UnitType)
            Sets the property data for the specified property id.
        
            propertyId: The property id.
            data: The property data value.
            unitType: The unit type.
        SetAt(self: PropertySet, propertyId: int, data: float)
            Sets the property data for the specified property id.
        
            propertyId: The property id.
            data: The property data value.
        SetAt(self: PropertySet, propertyId: int, data: int)
            Sets the property data for the specified property id.
        
            propertyId: The property id.
            data: The property data value.
        """
        pass

    def Synchronize(self, propertySetDefinition, db):
        """
        Synchronize(self: PropertySet, propertySetDefinition: PropertySetDefinition, db: DBObject)
            Synchronizes the property set by updating its state.
        
            propertySetDefinition: The property set definition.
            db: The database.
        """
        pass

    def UpdateAutoIncrementProperties(self):
        """
        UpdateAutoIncrementProperties(self: PropertySet)
            Updates the auto-increment properties.
        """
        pass

    def UpdateReferencingAttributes(self):
        """
        UpdateReferencingAttributes(self: PropertySet)
            Updates the referencing attributes.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ObjectAttachedTo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the id of the object that the property set is attached to.

Get: ObjectAttachedTo(self: PropertySet) -> ObjectId

Set: ObjectAttachedTo(self: PropertySet) = value
"""

    PropertySetData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of property set data.

Get: PropertySetData(self: PropertySet) -> PropertySetDataCollection

"""

    PropertySetDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the property set definition.

Get: PropertySetDefinition(self: PropertySet) -> ObjectId

Set: PropertySetDefinition(self: PropertySet) = value
"""

    PropertySetDefinitionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property set definition name.

Get: PropertySetDefinitionName(self: PropertySet) -> str

"""



class PropertySetData(ImpObject):
    """
    Represents property set data.
    
    PropertySetData()
    """
    def ClearFieldData(self):
        """
        ClearFieldData(self: PropertySetData)
            Clears the field data for the property.
        """
        pass

    def CopyFrom(self, other):
        """
        CopyFrom(self: PropertySetData, other: RXObject)
            Copies property set data from the specified property set data object.
        
            other: The other property set data object.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetData(self, unitType=None):
        """
        GetData(self: PropertySetData) -> object
        
            Gets the property data.
            Returns: Returns the property data, or null if not found.
        GetData(self: PropertySetData, unitType: UnitType) -> object
        
            Gets the property data.
        
            unitType: The unit type.
        """
        pass

    def GetFieldGeneratedData(self, asFieldCode):
        """
        GetFieldGeneratedData(self: PropertySetData, asFieldCode: bool) -> object
        
            Gets the field generated data for the property.
        
            asFieldCode: Determines if the value returned is a field code or text.
            Returns: Returns the field generated data for the property.
        """
        pass

    def GetFieldId(self):
        """ GetFieldId(self: PropertySetData) -> ObjectId """
        pass

    def SetData(self, data, unitType=None):
        """
        SetData(self: PropertySetData, data: object)
            Sets the property data.
        
            data: The property data.
        SetData(self: PropertySetData, data: object, unitType: UnitType)
            Sets the property data.
        
            data: The property data.
            unitType: The unit type.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    ContainsFields = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the value that indicates if the property contains fields.

Get: ContainsFields(self: PropertySetData) -> bool

"""

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the property data type.

Get: DataType(self: PropertySetData) -> DataType

Set: DataType(self: PropertySetData) = value
"""

    FieldBucketId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the field code Id.

Get: FieldBucketId(self: PropertySetData) -> str

"""

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the property Id.

Get: Id(self: PropertySetData) -> int

Set: Id(self: PropertySetData) = value
"""

    IsUnspecified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value that indicates if the property is unspecified.

Get: IsUnspecified(self: PropertySetData) -> bool

Set: IsUnspecified(self: PropertySetData) = value
"""

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the property unit type.

Get: UnitType(self: PropertySetData) -> UnitType

Set: UnitType(self: PropertySetData) = value
"""



class PropertySetDataCollection(object):
    """ Represents a collection of property set data. """
    def Add(self, value):
        """
        Add(self: PropertySetDataCollection, value: PropertySetData) -> int
        
            Adds the specified item to the collection.
        
            value: The item to add.
            Returns: The number of items in the collection.
        """
        pass

    def Clear(self):
        """
        Clear(self: PropertySetDataCollection)
            Removes all items from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: PropertySetDataCollection, value: PropertySetData) -> bool
        
            Determines if the collection contains the specified item.
        
            value: The item.
            Returns: Returns true if the collection contains the specified item.
        """
        pass

    def CopyTo(self, array, start):
        """
        CopyTo(self: PropertySetDataCollection, array: Array[PropertySetData], start: int)
            Copies the collection to the PropertySetData array.
        
            array: The PropertySetData array.
            start: The start index to begin copying.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: PropertySetDataCollection) -> IEnumerator
        
            Gets the enumerator for this collection.
            Returns: Returns the enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: PropertySetDataCollection, value: PropertySetData) -> int
        
            Determines the index of the specified item.
        
            value: The item.
            Returns: Returns the index of the specified item.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: PropertySetDataCollection, index: int, value: PropertySetData)
            Inserts the specified item into the collection at the specified index.
        
            index: The index to insert the item at.
            value: The item to insert.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: PropertySetDataCollection, value: PropertySetData)
            Removes the specified item from the collection.
        
            value: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: PropertySetDataCollection, index: int)
            Removes an item from the collection at the specified index.
        
            index: The index of the item to remove.
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

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of items in the collection.

Get: Count(self: PropertySetDataCollection) -> int

"""



class PropertySetDefinition(DictionaryRecord):
    """
    Represents a property set definition.
    
    PropertySetDefinition()
    """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetValue(self, *__args):
        """
        GetValue(self: PropertySetDefinition, propertyId: int, id: ObjectId, blockRefPath: ObjectIdCollection) -> object
        
            Gets the value of the specified property.
        
            propertyId: The property id.
            id: The object id.
            blockRefPath: The block reference paths.
            Returns: Returns the value of the specified property, or null if not found.
        GetValue(self: PropertySetDefinition, propId: int, obj: DBObject, blockRefPath: ObjectIdCollection) -> object
        
            Gets the value of the specified property.
        
            propId: The property id.
            obj: The object.
            blockRefPath: The block reference paths.
            Returns: Returns the value of the specified property, or null if not found.
        """
        pass

    def IsEquivalent(self, otherDef):
        """
        IsEquivalent(self: PropertySetDefinition, otherDef: PropertySetDefinition) -> bool
        
            Determines if the definition is equivalvent to the specified definition.
        
            otherDef: The other definition.
            Returns: Returns true if the definition is equivalvent to the specified definition.
        """
        pass

    def RecordAsModified(self):
        """
        RecordAsModified(self: PropertySetDefinition)
            Triggers a message by checking if the object was opened for write.
        """
        pass

    def SetAppliesToFilter(self, filter, byStyle):
        """
        SetAppliesToFilter(self: PropertySetDefinition, filter: StringCollection, byStyle: bool)
            Sets the object (or style) names that the set applies to.
        
            filter: The object (or style) names.
            byStyle: Determines if the filter is style or object based.
        """
        pass

    def SetDisplayOrder(self, propertyDef, order):
        """ SetDisplayOrder(self: PropertySetDefinition, propertyDef: PropertyDefinition, order: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AppliesToAll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets whether the definition applies to all.

Get: AppliesToAll(self: PropertySetDefinition) -> bool

Set: AppliesToAll(self: PropertySetDefinition) = value
"""

    AppliesToFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the object (or style) names that the set applies to.

Get: AppliesToFilter(self: PropertySetDefinition) -> StringCollection

"""

    ClassificationFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the classification filter collection. Perform add/remove operations on the collection.

Get: ClassificationFilter(self: PropertySetDefinition) -> ClassificationCollection

"""

    Definitions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the collection of property definitions.

Get: Definitions(self: PropertySetDefinition) -> PropertyDefinitionCollection

"""

    IsStyleBased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value that indicates that the definition is style based.

Get: IsStyleBased(self: PropertySetDefinition) -> bool

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value that determines if the definition is visible.

Get: IsVisible(self: PropertySetDefinition) -> bool

Set: IsVisible(self: PropertySetDefinition) = value
"""

    IsWriteable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value that determines if the definition is writable.

Get: IsWriteable(self: PropertySetDefinition) -> bool

Set: IsWriteable(self: PropertySetDefinition) = value
"""



class PropertyValueUnitPair(DisposableWrapper):
    """
    Represents a value-unit pair for a given property.
    
    PropertyValueUnitPair(value: object, type: UnitType)
    PropertyValueUnitPair()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, value=None, type=None):
        """
        __new__(cls: type, value: object, type: UnitType)
        __new__(cls: type)
        """
        pass

    UnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the unit type.

Get: UnitType(self: PropertyValueUnitPair) -> UnitType

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the value.

Get: Value(self: PropertyValueUnitPair) -> object

"""



class RotationType(Enum):
    """
    Defines identifiers that indicate the Rotation Type.
    
    enum RotationType, values: Horizontal (0), Vertical (1)
    """
    Horizontal = None
    value__ = None
    Vertical = None


class RoundingType(Enum):
    """
    Defines identifiers that indicate the rounding type.
    
    enum RoundingType, values: RoundDown (2), RoundOff (0), RoundUp (1)
    """
    RoundDown = None
    RoundOff = None
    RoundUp = None
    value__ = None


class ScheduleTable(Geo):
    """
    Represents a schedule table.
    
    ScheduleTable()
    """
    def AddToSelectionSet(self, *__args):
        """
        AddToSelectionSet(self: ScheduleTable, entity: Entity) -> bool
        
            Add entity to section set.
        
            entity: The entity.
            Returns: True if success, false if it is rejected.
        AddToSelectionSet(self: ScheduleTable, entityId: ObjectId) -> bool
        
            Add entity id to selection set.
        
            entityId: The entity id.
            Returns: If it is filted.
        AddToSelectionSet(self: ScheduleTable, entityIds: ObjectIdCollection) -> ObjectIdCollection
        
            Add entity id collection to selection set.
        
            entityIds: The entity id collection.
        """
        pass

    def CellData(self, row, column):
        """
        CellData(self: ScheduleTable, row: int, column: int) -> object
        
            Cell data.
        
            row: Row.
            column: Column.
            Returns: The cell data.
        """
        pass

    def CellText(self, row, column):
        """
        CellText(self: ScheduleTable, row: int, column: int) -> str
        
            Cell text.
        
            row: Row.
            column: Column.
            Returns: Cell text.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def EvaluateFieldCodes(self):
        """
        EvaluateFieldCodes(self: ScheduleTable)
            Evaluate field codes.
        """
        pass

    def ForceUseCachedData(self, forceUseCache):
        """
        ForceUseCachedData(self: ScheduleTable, forceUseCache: bool)
            Force use cached data.
        
            forceUseCache: If force use cache.
        """
        pass

    def GetColumn(self, pickedMarker):
        """
        GetColumn(self: ScheduleTable, pickedMarker: IntPtr) -> int
        
            Get column.
        
            pickedMarker: The picked marker.
            Returns: Get column.
        """
        pass

    def GetColumnMatrix(self, index):
        """
        GetColumnMatrix(self: ScheduleTable, index: int) -> ScheduleTableUniqueVariantCollection
        
            Gets column matrix.
        
            index: The index.
            Returns: The column matrix.
        """
        pass

    def GetHeaderPosition(self, node):
        """
        GetHeaderPosition(self: ScheduleTable, node: ScheduleTableStyleHeaderNode) -> ScheduleTableHeaderPosition
        
            Gets header position.
        
            node: The node.
            Returns: The header position.
        """
        pass

    def GetHeaderPositionIterator(self):
        """
        GetHeaderPositionIterator(self: ScheduleTable) -> ScheduleTableHeaderPositionIterator
        
            Gets the header position iterator.
            Returns: The header position.
        """
        pass

    def GetMarker(self, row, column):
        """
        GetMarker(self: ScheduleTable, row: int, column: int) -> IntPtr
        
            Get marker.
        
            row: The row.
            column: The column.
            Returns: The marker.
        """
        pass

    def GetPageBreaks(self):
        """
        GetPageBreaks(self: ScheduleTable) -> IntegerCollection
        
            Gets page breaks.
        """
        pass

    def GetPageHeights(self):
        """
        GetPageHeights(self: ScheduleTable) -> DoubleCollection
        
            Gets page heights.
        """
        pass

    def GetPageWidths(self):
        """
        GetPageWidths(self: ScheduleTable) -> DoubleCollection
        
            Gets the page widths.
        """
        pass

    def GetRasterImageId(self, varValue):
        """
        GetRasterImageId(self: ScheduleTable, varValue: object) -> ObjectId
        
            Gets raster image id.
        
            varValue: The variant value.
            Returns: The raster image id.
        """
        pass

    def GetRow(self, pickedMarker):
        """
        GetRow(self: ScheduleTable, pickedMarker: IntPtr) -> int
        
            Get row.
        
            pickedMarker: Picked marker.
            Returns: The row.
        """
        pass

    def GetRowMarkers(self, row):
        """
        GetRowMarkers(self: ScheduleTable, row: int) -> IntPtrCollection
        
            Gets row markers.
        
            row: The row.
        """
        pass

    def GetScheduleDrawingName(self, fullPathIfRelative=None):
        """
        GetScheduleDrawingName(self: ScheduleTable) -> str
        
            Gets the schedule drawing name.
        GetScheduleDrawingName(self: ScheduleTable, fullPathIfRelative: bool) -> str
        
            Gets schedule drawing name.
        
            fullPathIfRelative: Full path if relative.
        """
        pass

    def ObjectsAtRow(self, row):
        """
        ObjectsAtRow(self: ScheduleTable, row: int) -> ObjectIdAndBlockReferencePathCollection
        
            Objects at row.
        
            row: The row.
        """
        pass

    def RegenerateSampleTable(self, forceUpdate):
        """
        RegenerateSampleTable(self: ScheduleTable, forceUpdate: bool)
            Regenerate sample table.
        
            forceUpdate: Force update.
        """
        pass

    def RegenerateTable(self, forceUpdate):
        """
        RegenerateTable(self: ScheduleTable, forceUpdate: bool)
            Regenerate table.
        
            forceUpdate: Force update.
        """
        pass

    def RemoveFromSelectionSet(self, entityId):
        """
        RemoveFromSelectionSet(self: ScheduleTable, entityId: ObjectId)
            Remove from selection Set.
        
            entityId: The entity id.
        """
        pass

    def RowHeight(self, row):
        """
        RowHeight(self: ScheduleTable, row: int) -> float
        
            Row height.
        
            row: The row.
            Returns: The row height.
        """
        pass

    def RowHeightSum(self, row):
        """
        RowHeightSum(self: ScheduleTable, row: int) -> float
        
            Row height sum.
        
            row: The row.
        """
        pass

    def SetCellData(self, row, column, cvar):
        """
        SetCellData(self: ScheduleTable, row: int, column: int, cvar: object)
            Set cell data.
        
            row: Row.
            column: Column.
            cvar: Cvar.
        """
        pass

    def SetScheduleDrawingName(self, scheduleDrawingName):
        """
        SetScheduleDrawingName(self: ScheduleTable, scheduleDrawingName: str)
            Sets the schedule drawing name.
        
            scheduleDrawingName: The schedule drawing name.
        """
        pass

    def SetSelectionSet(self, entityIds, entityFiltered):
        """
        SetSelectionSet(self: ScheduleTable, entityIds: ObjectIdCollection, entityFiltered: ObjectIdCollection)
            Set the selection set.
        
            entityIds: The entity object idcollection.
            entityFiltered: The entity filted.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AddNewEntriesAutomatically = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If add new entities automatically.

Get: AddNewEntriesAutomatically(self: ScheduleTable) -> bool

Set: AddNewEntriesAutomatically(self: ScheduleTable) = value
"""

    AutomaticUpdate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets automatic update.

Get: AutomaticUpdate(self: ScheduleTable) -> bool

Set: AutomaticUpdate(self: ScheduleTable) = value
"""

    BasePageWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the base page width.

Get: BasePageWidth(self: ScheduleTable) -> float

"""

    CenterPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the center point.

Get: CenterPoint(self: ScheduleTable) -> Point3d

"""

    ColumnCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the column count.

Get: ColumnCount(self: ScheduleTable) -> int

"""

    HeaderHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets header height.

Get: HeaderHeight(self: ScheduleTable) -> float

"""

    IsModelGeometry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets is model geometry.

Get: IsModelGeometry(self: ScheduleTable) -> bool

"""

    IsOutOfDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets if it is out of data.

Get: IsOutOfDate(self: ScheduleTable) -> bool

"""

    LayerWildcard = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the layer wild card.

Get: LayerWildcard(self: ScheduleTable) -> str

Set: LayerWildcard(self: ScheduleTable) = value
"""

    LowerLeftPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets lower left point.

Get: LowerLeftPoint(self: ScheduleTable) -> Point3d

"""

    LowerRightPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the lower right point.

Get: LowerRightPoint(self: ScheduleTable) -> Point3d

"""

    MatrixHeaderHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get matrix header height.

Get: MatrixHeaderHeight(self: ScheduleTable) -> float

"""

    MinimumRowHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the minimum row height.

Get: MinimumRowHeight(self: ScheduleTable) -> float

"""

    PageDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets page direction.

Get: PageDirection(self: ScheduleTable) -> PageDirectionType

Set: PageDirection(self: ScheduleTable) = value
"""

    PageMaxHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page max height.

Get: PageMaxHeight(self: ScheduleTable) -> float

Set: PageMaxHeight(self: ScheduleTable) = value
"""

    PageMaxHeights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets page max heights.

Get: PageMaxHeights(self: ScheduleTable) -> ScheduleTablePageMaxHeightCollection

"""

    PageSpacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the page spacing.

Get: PageSpacing(self: ScheduleTable) -> float

Set: PageSpacing(self: ScheduleTable) = value
"""

    RepeatHeaders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets repeat headers.

Get: RepeatHeaders(self: ScheduleTable) -> bool

Set: RepeatHeaders(self: ScheduleTable) = value
"""

    RepeatTitle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets repeat title.

Get: RepeatTitle(self: ScheduleTable) -> bool

Set: RepeatTitle(self: ScheduleTable) = value
"""

    RowCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the row count.

Get: RowCount(self: ScheduleTable) -> int

"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Scale.

Get: Scale(self: ScheduleTable) -> float

Set: Scale(self: ScheduleTable) = value
"""

    ScanBlockReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if scan block references.

Get: ScanBlockReferences(self: ScheduleTable) -> bool

Set: ScanBlockReferences(self: ScheduleTable) = value
"""

    ScanExternalReferences = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if scan external references.

Get: ScanExternalReferences(self: ScheduleTable) -> bool

Set: ScanExternalReferences(self: ScheduleTable) = value
"""

    ScheduleDrawing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the schedule drawing.

Get: ScheduleDrawing(self: ScheduleTable) -> bool

Set: ScheduleDrawing(self: ScheduleTable) = value
"""

    SelectionSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the seletion set.

Get: SelectionSet(self: ScheduleTable) -> ObjectIdCollection

"""

    TableHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the table height.

Get: TableHeight(self: ScheduleTable) -> float

"""

    TableWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the table width.

Get: TableWidth(self: ScheduleTable) -> float

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The title.

Get: Title(self: ScheduleTable) -> str

Set: Title(self: ScheduleTable) = value
"""

    TitleHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the title height.

Get: TitleHeight(self: ScheduleTable) -> float

"""

    TitleHeightOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the title height offset.

Get: TitleHeightOffset(self: ScheduleTable) -> float

"""

    TitleIsHorizontal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the title is horizontal.

Get: TitleIsHorizontal(self: ScheduleTable) -> bool

"""

    TitleWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the title width.

Get: TitleWidth(self: ScheduleTable) -> float

"""

    TitleWidthOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the title width offset.

Get: TitleWidthOffset(self: ScheduleTable) -> float

"""

    TotalRow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total row.

Get: TotalRow(self: ScheduleTable) -> bool

"""

    TotalRowHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets total row height.

Get: TotalRowHeight(self: ScheduleTable) -> float

"""

    UpperLeftPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets upper left point.

Get: UpperLeftPoint(self: ScheduleTable) -> Point3d

"""

    UpperRightPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the upper right point.

Get: UpperRightPoint(self: ScheduleTable) -> Point3d

"""

    UseManualHeights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets use manual heights.

Get: UseManualHeights(self: ScheduleTable) -> bool

Set: UseManualHeights(self: ScheduleTable) = value
"""

    XFormMatrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the xform matrix.

Get: XFormMatrix(self: ScheduleTable) -> Matrix3d

"""



class ScheduleTableCellFormat(ImpObject):
    """
    Represents a Schedule table cell format.
    
    ScheduleTableCellFormat()
    """
    def CellHeight(self, string, fixedWidth):
        """
        CellHeight(self: ScheduleTableCellFormat, string: str, fixedWidth: float) -> float
        
            Cell height.
        
            string: The string.
            fixedWidth: The fixed width.
            Returns: The cell height.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def ExtentsCellHeight(self, string):
        """
        ExtentsCellHeight(self: ScheduleTableCellFormat, string: str) -> float
        
            Extents cell height.
        
            string: The string.
            Returns: The extented cell height.
        """
        pass

    def ExtentsCellWidth(self, string):
        """
        ExtentsCellWidth(self: ScheduleTableCellFormat, string: str) -> float
        
            Extents cell width.
        
            string: The string.
            Returns: The extented cell width.
        """
        pass

    def ExtentsHeight(self, string):
        """
        ExtentsHeight(self: ScheduleTableCellFormat, string: str) -> float
        
            Extents height.
        
            string: The string.
            Returns: The extented height.
        """
        pass

    def ExtentsWidth(self, string):
        """
        ExtentsWidth(self: ScheduleTableCellFormat, string: str) -> float
        
            Extents width.
        
            string: The string.
            Returns: The width.
        """
        pass

    def GetRotatedTextCellWidth(self, string, fixedWidth):
        """
        GetRotatedTextCellWidth(self: ScheduleTableCellFormat, string: str, fixedWidth: float) -> float
        
            Gets the rotated text cell width.
        
            string: The string.
            fixedWidth: The fixed width.
            Returns: The rotated text cell width.
        """
        pass

    def MatrixExtentsCellHeight(self, count):
        """
        MatrixExtentsCellHeight(self: ScheduleTableCellFormat, count: int) -> float
        
            The matrix extents cell height.
        
            count: The count.
            Returns: The matrix extents cell height.
        """
        pass

    def MatrixExtentsCellWidth(self, count):
        """
        MatrixExtentsCellWidth(self: ScheduleTableCellFormat, count: int) -> float
        
            Matrix extents cell width.
        
            count: The count.
            Returns: The matrix extents cell width.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Alignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the alignment.

Get: Alignment(self: ScheduleTableCellFormat) -> AttachmentPoint

Set: Alignment(self: ScheduleTableCellFormat) = value
"""

    Gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the gap.

Get: Gap(self: ScheduleTableCellFormat) -> float

Set: Gap(self: ScheduleTableCellFormat) = value
"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the height.

Get: Height(self: ScheduleTableCellFormat) -> float

Set: Height(self: ScheduleTableCellFormat) = value
"""

    MatrixSymbolType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the matrix symbol type.

Get: MatrixSymbolType(self: ScheduleTableCellFormat) -> MatrixSymbolType

Set: MatrixSymbolType(self: ScheduleTableCellFormat) = value
"""

    RotationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the rotation type.

Get: RotationType(self: ScheduleTableCellFormat) -> RotationType

Set: RotationType(self: ScheduleTableCellFormat) = value
"""

    TextStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text style id.

Get: TextStyleId(self: ScheduleTableCellFormat) -> ObjectId

Set: TextStyleId(self: ScheduleTableCellFormat) = value
"""

    TextStyleIdString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the text style id string.

Get: TextStyleIdString(self: ScheduleTableCellFormat) -> str

"""

    UseMatrixForTrueFalse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the use matrix for true false.

Get: UseMatrixForTrueFalse(self: ScheduleTableCellFormat) -> bool

Set: UseMatrixForTrueFalse(self: ScheduleTableCellFormat) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the width.

Get: Width(self: ScheduleTableCellFormat) -> float

Set: Width(self: ScheduleTableCellFormat) = value
"""



class ScheduleTableCellFormatOverride(ScheduleTableCellFormat):
    """
    Represents a schedule table cell format override.
    
    ScheduleTableCellFormatOverride()
    """
    def ClearAlignmentOverride(self):
        """
        ClearAlignmentOverride(self: ScheduleTableCellFormatOverride)
            Clear alignment override.
        """
        pass

    def ClearGapOverride(self):
        """
        ClearGapOverride(self: ScheduleTableCellFormatOverride)
            Clear gap override.
        """
        pass

    def ClearHeightOverride(self):
        """
        ClearHeightOverride(self: ScheduleTableCellFormatOverride)
            Clear height override.
        """
        pass

    def ClearMatrixSymbolTypeOverride(self):
        """
        ClearMatrixSymbolTypeOverride(self: ScheduleTableCellFormatOverride)
            Clear matrix symbol type override.
        """
        pass

    def ClearRotationTypeOverride(self):
        """
        ClearRotationTypeOverride(self: ScheduleTableCellFormatOverride)
            Clear rotation type override.
        """
        pass

    def ClearTextStyleIdOverride(self):
        """
        ClearTextStyleIdOverride(self: ScheduleTableCellFormatOverride)
            Clear text style id override.
        """
        pass

    def ClearUseMatrixForTrueFalseOverride(self):
        """
        ClearUseMatrixForTrueFalseOverride(self: ScheduleTableCellFormatOverride)
            Clear use matrix for true false override.
        """
        pass

    def ClearWidthOverride(self):
        """
        ClearWidthOverride(self: ScheduleTableCellFormatOverride)
            Clear width override.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    DefaultCellFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default cell format.

Get: DefaultCellFormat(self: ScheduleTableCellFormatOverride) -> ScheduleTableCellFormat

Set: DefaultCellFormat(self: ScheduleTableCellFormatOverride) = value
"""

    HasOverrides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets if it has overrides.

Get: HasOverrides(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideAlignment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets override alignment.

Get: OverrideAlignment(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets override gap.

Get: OverrideGap(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets override height.

Get: OverrideHeight(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideMatrixSymbolType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the override matrix symbol type.

Get: OverrideMatrixSymbolType(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideRotationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Override rotation type.

Get: OverrideRotationType(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideTextStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets if it override text style id.

Get: OverrideTextStyleId(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideUseMatrixForTrueFalse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the override use matrix for true false.

Get: OverrideUseMatrixForTrueFalse(self: ScheduleTableCellFormatOverride) -> bool

"""

    OverrideWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the override width.

Get: OverrideWidth(self: ScheduleTableCellFormatOverride) -> bool

"""



class ScheduleTableColumn(DisposableWrapper):
    """
    Represents a schedule table column.
    
    ScheduleTableColumn()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetFixedCellWidth(self, cellWidth):
        """
        SetFixedCellWidth(self: ScheduleTableColumn, cellWidth: float)
            Sets the fixed cell width.
        
            cellWidth: The cell width.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cell width.

Get: CellWidth(self: ScheduleTableColumn) -> float

Set: CellWidth(self: ScheduleTableColumn) = value
"""

    CellX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the cell x.

Get: CellX(self: ScheduleTableColumn) -> float

Set: CellX(self: ScheduleTableColumn) = value
"""

    MatrixValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the matrix values.

Get: MatrixValues(self: ScheduleTableColumn) -> ScheduleTableUniqueVariantCollection

Set: MatrixValues(self: ScheduleTableColumn) = value
"""



class ScheduleTableImage(DisposableWrapper):
    """
    Represents a schedule table image.
    
    ScheduleTableImage()
    """
    def AddImage(self, imageId):
        """
        AddImage(self: ScheduleTableImage, imageId: ObjectId) -> bool
        
            Add image.
        
            imageId: The image id.
            Returns: True if found, false otherwise.
        """
        pass

    def AddImageDefinition(self, filename, definitionId):
        """
        AddImageDefinition(self: ScheduleTableImage, filename: str, definitionId: ObjectId)
            Add image definition.
        
            filename: The file name.
            definitionId: The definition id.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def FindImageDefinition(self, filename):
        """
        FindImageDefinition(self: ScheduleTableImage, filename: str) -> ObjectId
        
            Find the image definition.
        
            filename: The file name.
            Returns: The image definition id.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class ScheduleTablePageMaxHeightCollection(object):
    """
    Represents a collection of Schedule Table Page Max Height.
    
    ScheduleTablePageMaxHeightCollection(pOp: IScheduleTablePageMaxHeightOperation)
    """
    def Add(self, value):
        """
        Add(self: ScheduleTablePageMaxHeightCollection, value: float) -> int
        
            Adds an item to the collection.
        
            value: The item.
            Returns: Returns the index where the item was added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ScheduleTablePageMaxHeightCollection)
            Removes all items from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: ScheduleTablePageMaxHeightCollection, value: float) -> bool
        
            Determines if the collection contains the specified item.
        
            value: The item.
            Returns: Returns true if the collection contains the specified item.
        """
        pass

    def CopyTo(self, array, start):
        """
        CopyTo(self: ScheduleTablePageMaxHeightCollection, array: Array[float], start: int)
            Copies the collection to the array.
        
            array: The System::Double array.
            start: The start index to begin copying.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScheduleTablePageMaxHeightCollection) -> IEnumerator
        
            Returns an enumerator for this collection.
            Returns: Returns an enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: ScheduleTablePageMaxHeightCollection, value: float) -> int
        
            Determines the index of the specified item.
        
            value: The item.
            Returns: Returns the index of the specified item.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: ScheduleTablePageMaxHeightCollection, index: int, value: float)
            Inserts the specified item into the collection at the specified index.
        
            index: The index to insert the item at.
            value: The item to insert.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: ScheduleTablePageMaxHeightCollection, value: float)
            Removes the specified item from the collection.
        
            value: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ScheduleTablePageMaxHeightCollection, index: int)
            Removes the item at the specified index.
        
            index: The index.
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IScheduleTablePageMaxHeightOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of System::Double available in this collection.

Get: Count(self: ScheduleTablePageMaxHeightCollection) -> int

"""



class ScheduleTableSorting(ImpObject):
    """
    Represents a schedule table sorting.
    
    ScheduleTableSorting()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetColumnPropertyId(self):
        """
        GetColumnPropertyId(self: ScheduleTableSorting) -> int
        
            Gets the column property id.
            Returns: The column property id.
        """
        pass

    def GetColumnPropertySetDefinitionObjectId(self):
        """
        GetColumnPropertySetDefinitionObjectId(self: ScheduleTableSorting) -> ObjectId
        
            The column object id.
            Returns: The column object id.
        """
        pass

    def SetColumn(self, propertySetDefinitionId, propertyId, isFormulaColumn):
        """
        SetColumn(self: ScheduleTableSorting, propertySetDefinitionId: ObjectId, propertyId: int, isFormulaColumn: bool)
            Sets the column.
        
            propertySetDefinitionId: The property set definition id.
            propertyId: The property id.
            isFormulaColumn: Is formula column.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    FormulaColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets formula column.

Get: FormulaColumn(self: ScheduleTableSorting) -> bool

Set: FormulaColumn(self: ScheduleTableSorting) = value
"""

    GroupHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the group header.

Get: GroupHeader(self: ScheduleTableSorting) -> str

Set: GroupHeader(self: ScheduleTableSorting) = value
"""

    SortOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sort order.

Get: SortOrder(self: ScheduleTableSorting) -> SortOrder

Set: SortOrder(self: ScheduleTableSorting) = value
"""

    SubTotalHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the sub total header.

Get: SubTotalHeader(self: ScheduleTableSorting) -> str

Set: SubTotalHeader(self: ScheduleTableSorting) = value
"""

    UseGroupHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the use group header.

Get: UseGroupHeader(self: ScheduleTableSorting) -> bool

Set: UseGroupHeader(self: ScheduleTableSorting) = value
"""

    UseSubTotalHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets if use sub total header.

Get: UseSubTotalHeader(self: ScheduleTableSorting) -> bool

Set: UseSubTotalHeader(self: ScheduleTableSorting) = value
"""



class ScheduleTableSortingCollection(object):
    """
    Represents a collection of Schedule Table Page Max Height.
    
    ScheduleTableSortingCollection(sortingOperator: IScheduleTableSortingOperation)
    """
    def Add(self, value):
        """
        Add(self: ScheduleTableSortingCollection, value: ScheduleTableSorting) -> int
        
            Adds an item to the collection.
        
            value: The item.
            Returns: Returns the index where the item was added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ScheduleTableSortingCollection)
            Removes all items from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: ScheduleTableSortingCollection, value: ScheduleTableSorting) -> bool
        
            Determines if the collection contains the specified item.
        
            value: The item.
            Returns: Returns true if the collection contains the specified item.
        """
        pass

    def CopyTo(self, array, start):
        """
        CopyTo(self: ScheduleTableSortingCollection, array: Array[ScheduleTableSorting], start: int)
            Copies the collection to the array.
        
            array: The ScheduleTableSorting^ array.
            start: The start index to begin copying.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScheduleTableSortingCollection) -> IEnumerator
        
            Returns an enumerator for this collection.
            Returns: Returns an enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: ScheduleTableSortingCollection, value: ScheduleTableSorting) -> int
        
            Determines the index of the specified item.
        
            value: The item.
            Returns: Returns the index of the specified item.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: ScheduleTableSortingCollection, index: int, value: ScheduleTableSorting)
            Inserts the specified item into the collection at the specified index.
        
            index: The index to insert the item at.
            value: The item to insert.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ScheduleTableSortingCollection, index: int)
            Removes the item at the specified index.
        
            index: The index.
        """
        pass

    def Swap(self, index1, index2):
        """
        Swap(self: ScheduleTableSortingCollection, index1: int, index2: int)
            Swap two items.
        
            index1: The first item index.
            index2: The second item index.
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
    def __new__(self, sortingOperator):
        """ __new__(cls: type, sortingOperator: IScheduleTableSortingOperation) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of ScheduleTableSorting^ available in this collection.

Get: Count(self: ScheduleTableSortingCollection) -> int

"""



class ScheduleTableStyle(DictionaryRecord):
    """
    Represents a Schedule Table Style.
    
    ScheduleTableStyle()
    """
    def AddClassification(self, classificationId):
        """
        AddClassification(self: ScheduleTableStyle, classificationId: ObjectId)
            Add classification.
        
            classificationId: The classificationId.
        """
        pass

    def AddFormulaColumn(self, column):
        """
        AddFormulaColumn(self: ScheduleTableStyle, column: ScheduleTableStyleColumn)
            Add formula column.
        
            column: The column.
        """
        pass

    def AddQuantityColumn(self, column):
        """
        AddQuantityColumn(self: ScheduleTableStyle, column: ScheduleTableStyleColumn)
            Add quantity column.
        
            column: The column.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def FormatColumnVariant(self, data, formatId, column=None):
        """
        FormatColumnVariant(self: ScheduleTableStyle, data: object, formatId: ObjectId) -> str
        
            Format column variant.
        
            data: The variant data.
            formatId: The format id.
            Returns: The formated column variant.
        FormatColumnVariant(self: ScheduleTableStyle, data: object, formatId: ObjectId, column: int) -> str
        
            Format column variant.
        
            data: The variant data.
            formatId: The format id.
            column: The column.
            Returns: The formated column variant.
        """
        pass

    def GetColumnFormat(self, column):
        """
        GetColumnFormat(self: ScheduleTableStyle, column: int) -> ScheduleTableCellFormat
        
            Gets the column format.
        
            column: The column.
            Returns: The column format.
        """
        pass

    def IsFormulaColumn(self, column):
        """
        IsFormulaColumn(self: ScheduleTableStyle, column: ScheduleTableStyleColumn) -> bool
        
            Is formula column.
        
            column: The column.
            Returns: True if it is formula column, false otherwise.
        """
        pass

    def IsQuantityColumn(self, column):
        """
        IsQuantityColumn(self: ScheduleTableStyle, column: ScheduleTableStyleColumn) -> bool
        
            Is quantity column.
        
            column: The column.
            Returns: True if it is quantity column, false otherwise.
        """
        pass

    def RemapFormulaColumnIds(self, propertySetDefinition1, propertySetDefinition2, definition1PropertyIds, definition2PropertyIds, actions):
        """
        RemapFormulaColumnIds(self: ScheduleTableStyle, propertySetDefinition1: PropertySetDefinition, propertySetDefinition2: PropertySetDefinition, definition1PropertyIds: IntegerCollection, definition2PropertyIds: IntegerCollection, actions: IntegerCollection)
            Remap formulat column ids.
        
            propertySetDefinition1: The first property set definition.
            propertySetDefinition2: The second property set definition.
            definition1PropertyIds: The first definition property id collection.
            definition2PropertyIds: The second definition property id collection.
            actions: The actions.
        """
        pass

    def RemoveClassification(self, classificationId):
        """
        RemoveClassification(self: ScheduleTableStyle, classificationId: ObjectId)
            Remove classification.
        
            classificationId: The classificationId.
        """
        pass

    def SetValidityFlags(self):
        """
        SetValidityFlags(self: ScheduleTableStyle)
            Sets the validity flags.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    AppliesToAll = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets applies to all.

Get: AppliesToAll(self: ScheduleTableStyle) -> bool

Set: AppliesToAll(self: ScheduleTableStyle) = value
"""

    AppliesToFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the entity filter.

Get: AppliesToFilter(self: ScheduleTableStyle) -> StringCollection

Set: AppliesToFilter(self: ScheduleTableStyle) = value
"""

    ClassificationFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the classification filter.

Get: ClassificationFilter(self: ScheduleTableStyle) -> ClassificationCollection

"""

    ColumnHeaderFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Column header format.

Get: ColumnHeaderFormat(self: ScheduleTableStyle) -> ScheduleTableCellFormat

"""

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the columns.

Get: Columns(self: ScheduleTableStyle) -> ScheduleTableStyleColumnCollection

"""

    DefaultCellFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Default cell format.

Get: DefaultCellFormat(self: ScheduleTableStyle) -> ScheduleTableCellFormat

"""

    FormulaColumnTotalNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the formula column total number.

Get: FormulaColumnTotalNumber(self: ScheduleTableStyle) -> int

"""

    GroupHeaderFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Group header format.

Get: GroupHeaderFormat(self: ScheduleTableStyle) -> ScheduleTableCellFormat

"""

    HasFormulaColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has formula column.

Get: HasFormulaColumn(self: ScheduleTableStyle) -> bool

"""

    HasQuantityColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Has quantity column.

Get: HasQuantityColumn(self: ScheduleTableStyle) -> bool

"""

    MatrixHeaderFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Matrix header format.

Get: MatrixHeaderFormat(self: ScheduleTableStyle) -> ScheduleTableCellFormat

"""

    NextFormulaId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets next formula id.

Get: NextFormulaId(self: ScheduleTableStyle) -> int

"""

    QuantityColumnHeading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the quantity heading.

Get: QuantityColumnHeading(self: ScheduleTableStyle) -> str

"""

    QuantityColumnNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets quantity column number.

Get: QuantityColumnNumber(self: ScheduleTableStyle) -> int

"""

    RepeatFirstColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the repeat first column.

Get: RepeatFirstColumn(self: ScheduleTableStyle) -> bool

Set: RepeatFirstColumn(self: ScheduleTableStyle) = value
"""

    Sortings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the sortings.

Get: Sortings(self: ScheduleTableStyle) -> ScheduleTableSortingCollection

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the title.

Get: Title(self: ScheduleTableStyle) -> str

Set: Title(self: ScheduleTableStyle) = value
"""

    TitleFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the title format.

Get: TitleFormat(self: ScheduleTableStyle) -> ScheduleTableCellFormat

"""

    TotalHeaderFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Total header format.

Get: TotalHeaderFormat(self: ScheduleTableStyle) -> ScheduleTableCellFormat

"""

    Tree = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the tree.

Get: Tree(self: ScheduleTableStyle) -> ScheduleTableStyleHeaderTree

"""



class ScheduleTableStyleHeaderNode(ImpObject):
    """
    Represents a ScheduleTableStyleHeaderNode.
    
    ScheduleTableStyleHeaderNode()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetTreeParent(self, parent):
        """
        SetTreeParent(self: ScheduleTableStyleHeaderNode, parent: ScheduleTableStyleHeaderNode)
            Sets the tree parent.
        
            parent: The parent node.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the child nodes of this node.

Get: Children(self: ScheduleTableStyleHeaderNode) -> ScheduleTableStyleHeaderNodeCollection

"""

    FormatOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the format value.

Get: FormatOverride(self: ScheduleTableStyleHeaderNode) -> ScheduleTableCellFormatOverride

Set: FormatOverride(self: ScheduleTableStyleHeaderNode) = value
"""

    Level = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the level property.

Get: Level(self: ScheduleTableStyleHeaderNode) -> int

"""

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the parent node.

Get: Parent(self: ScheduleTableStyleHeaderNode) -> ScheduleTableStyleHeaderNode

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the text value.

Get: Text(self: ScheduleTableStyleHeaderNode) -> str

Set: Text(self: ScheduleTableStyleHeaderNode) = value
"""



class ScheduleTableStyleColumn(ScheduleTableStyleHeaderNode):
    """
    Represents a Schedule Table Style Column.
    
    ScheduleTableStyleColumn()
    """
    def CheckPropertyValid(self):
        """
        CheckPropertyValid(self: ScheduleTableStyleColumn)
            Checks if the property is valid.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Evaluate(self, formula=None, quantity=None):
        """
        Evaluate(self: ScheduleTableStyleColumn) -> object
        
            Evaluates the formula and return result with Quantity.
            Returns: Returns the variant.
        Evaluate(self: ScheduleTableStyleColumn, formula: str, quantity: int) -> (object, str)
        
            Evaluates the formula and return result with Quantity.
        
            formula: The formula string.
            quantity: The quantity.
            Returns: Returns the variant.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    CellFormatOverride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the schedule table cell format override.

Get: CellFormatOverride(self: ScheduleTableStyleColumn) -> ScheduleTableCellFormatOverride

Set: CellFormatOverride(self: ScheduleTableStyleColumn) = value
"""

    ColumnType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the column type.

Get: ColumnType(self: ScheduleTableStyleColumn) -> ScheduleTableStyleColumnType

Set: ColumnType(self: ScheduleTableStyleColumn) = value
"""

    DefaultData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the default data.

Get: DefaultData(self: ScheduleTableStyleColumn) -> object

Set: DefaultData(self: ScheduleTableStyleColumn) = value
"""

    FormatId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the format id.

Get: FormatId(self: ScheduleTableStyleColumn) -> ObjectId

Set: FormatId(self: ScheduleTableStyleColumn) = value
"""

    Formula = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the property defination formula.

Get: Formula(self: ScheduleTableStyleColumn) -> PropertyDefinitionFormula

Set: Formula(self: ScheduleTableStyleColumn) = value
"""

    FormulaTotal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the formula total.

Get: FormulaTotal(self: ScheduleTableStyleColumn) -> bool

Set: FormulaTotal(self: ScheduleTableStyleColumn) = value
"""

    FullPropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property full name.

Get: FullPropertyName(self: ScheduleTableStyleColumn) -> str

"""

    Heading = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the heading.

Get: Heading(self: ScheduleTableStyleColumn) -> str

Set: Heading(self: ScheduleTableStyleColumn) = value
"""

    HideColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the column is hide.

Get: HideColumn(self: ScheduleTableStyleColumn) -> bool

Set: HideColumn(self: ScheduleTableStyleColumn) = value
"""

    IsPropertyValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Indicates if the property is valid.

Get: IsPropertyValid(self: ScheduleTableStyleColumn) -> bool

"""

    Matrix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the schedule table variant matrix.

Get: Matrix(self: ScheduleTableStyleColumn) -> bool

Set: Matrix(self: ScheduleTableStyleColumn) = value
"""

    MaximumMatrixColumns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Sets the maximum of matrix columns.

Get: MaximumMatrixColumns(self: ScheduleTableStyleColumn) -> Int16

Set: MaximumMatrixColumns(self: ScheduleTableStyleColumn) = value
"""

    PropertyId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the property id.

Get: PropertyId(self: ScheduleTableStyleColumn) -> int

Set: PropertyId(self: ScheduleTableStyleColumn) = value
"""

    PropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property name.

Get: PropertyName(self: ScheduleTableStyleColumn) -> str

"""

    PropertySetDefinitionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the propertyset definition id.

Get: PropertySetDefinitionId(self: ScheduleTableStyleColumn) -> ObjectId

Set: PropertySetDefinitionId(self: ScheduleTableStyleColumn) = value
"""

    PropertySetDefinitionName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the property name.

Get: PropertySetDefinitionName(self: ScheduleTableStyleColumn) -> str

"""

    Total = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the total.

Get: Total(self: ScheduleTableStyleColumn) -> bool

Set: Total(self: ScheduleTableStyleColumn) = value
"""



class ScheduleTableStyleColumnCollection(object):
    """
    Represents a collection of ScheduleTableStyleColumn.
    
    ScheduleTableStyleColumnCollection(pOp: IScheduleTableStyleColumnOperation)
    """
    def Add(self, value):
        """
        Add(self: ScheduleTableStyleColumnCollection, value: ScheduleTableStyleColumn) -> int
        
            Adds an item to the collection.
        
            value: The item.
            Returns: Returns the index where the item was added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ScheduleTableStyleColumnCollection)
            Removes all items from the collection.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: ScheduleTableStyleColumnCollection, value: ScheduleTableStyleColumn) -> bool
        
            Determines if the collection contains the specified item.
        
            value: The item.
            Returns: Returns true if the collection contains the specified item.
        """
        pass

    def CopyTo(self, array, start):
        """
        CopyTo(self: ScheduleTableStyleColumnCollection, array: Array[ScheduleTableStyleColumn], start: int)
            Copies the collection to the array.
        
            array: The ScheduleTableStyleColumn array.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScheduleTableStyleColumnCollection) -> IEnumerator
        
            Returns an enumerator for this collection.
            Returns: Returns an enumerator for this collection.
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: ScheduleTableStyleColumnCollection, value: ScheduleTableStyleColumn) -> int
        
            Determines the index of the specified item.
        
            value: The item.
            Returns: Returns the index of the specified item.
        IndexOf(self: ScheduleTableStyleColumnCollection, propSetDefId: ObjectId, propId: int) -> int
        
            Determines the index of the specified item.
        
            propSetDefId: The propSetDefId.
            propId: The propId.
            Returns: Returns the index of the specified item.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: ScheduleTableStyleColumnCollection, index: int, value: ScheduleTableStyleColumn)
            Inserts the specified item into the collection at the specified index.
        
            index: The index to insert the item at.
            value: The item to insert.
        """
        pass

    def Prepend(self, node):
        """
        Prepend(self: ScheduleTableStyleColumnCollection, node: ScheduleTableStyleColumn)
            Prepend a column to the collection.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: ScheduleTableStyleColumnCollection, value: ScheduleTableStyleColumn)
            Removes the specified item from the collection.
        
            value: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ScheduleTableStyleColumnCollection, index: int)
            Removes the item at the specified index.
        
            index: The index.
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: IScheduleTableStyleColumnOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of ScheduleTableStyleColumn available in this collection.

Get: Count(self: ScheduleTableStyleColumnCollection) -> int

"""



class ScheduleTableStyleColumnType(Enum):
    """
    Defines the column type.
    
    enum ScheduleTableStyleColumnType, values: Formula (3), Normal (0), Quantity (1)
    """
    Formula = None
    Normal = None
    Quantity = None
    value__ = None


class ScheduleTableStyleHeaderNodeCollection(object):
    """
    Represents a collection of ScheduleTableStyleHeaderNode.
    
    ScheduleTableStyleHeaderNodeCollection(pOp: INodeOperation)
    """
    def Add(self, value):
        """
        Add(self: ScheduleTableStyleHeaderNodeCollection, value: ScheduleTableStyleHeaderNode) -> int
        
            Adds an item to the collection.
        
            value: The item.
            Returns: Returns the index where the item was added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ScheduleTableStyleHeaderNodeCollection)
            Removes all items from the collection. After the nodes are removed, any old 
             references to these nodes should not be used.
        """
        pass

    def Contains(self, value):
        """
        Contains(self: ScheduleTableStyleHeaderNodeCollection, value: ScheduleTableStyleHeaderNode) -> bool
        
            Determines if the collection contains the specified item.
        
            value: The item.
            Returns: Returns true if the collection contains the specified item.
        """
        pass

    def CopyTo(self, array, start):
        """ CopyTo(self: ScheduleTableStyleHeaderNodeCollection, array: Array[ScheduleTableStyleHeaderNode], start: int) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ScheduleTableStyleHeaderNodeCollection) -> IEnumerator
        
            Returns an enumerator for this collection.
            Returns: Returns an enumerator for this collection.
        """
        pass

    def IndexOf(self, value):
        """
        IndexOf(self: ScheduleTableStyleHeaderNodeCollection, value: ScheduleTableStyleHeaderNode) -> int
        
            Determines the index of the specified item.
        
            value: The item.
            Returns: Returns the index of the specified item.
        """
        pass

    def Insert(self, index, value):
        """
        Insert(self: ScheduleTableStyleHeaderNodeCollection, index: int, value: ScheduleTableStyleHeaderNode)
            Inserts the specified item into the collection at the specified index.
        
            index: The index to insert the item at.
            value: The item to insert.
        """
        pass

    def Prepend(self, node):
        """
        Prepend(self: ScheduleTableStyleHeaderNodeCollection, node: ScheduleTableStyleHeaderNode)
            Prepend a node to the collection.
        
            node: The new node.
        """
        pass

    def Remove(self, value):
        """
        Remove(self: ScheduleTableStyleHeaderNodeCollection, value: ScheduleTableStyleHeaderNode)
            Removes the specified item from the collection. You can still use the reference 
             to the removed node if you remove it using this function.
        
        
            value: The item to remove.
        """
        pass

    def RemoveAt(self, index):
        """
        RemoveAt(self: ScheduleTableStyleHeaderNodeCollection, index: int)
            Removes the item at the specified index. After the node is removed, any old 
             references to this node should not be used.
        
        
            index: The index.
        """
        pass

    def Shift(self, node, amount):
        """
        Shift(self: ScheduleTableStyleHeaderNodeCollection, node: ScheduleTableStyleHeaderNode, amount: int)
            Shift the node.
        
            node: The node to be shifted.
            amount: Amount.
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
    def __new__(self, pOp):
        """ __new__(cls: type, pOp: INodeOperation) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the number of ScheduleTableStyleHeaderNode available in this collection.

Get: Count(self: ScheduleTableStyleHeaderNodeCollection) -> int

"""



class ScheduleTableStyleHeaderTree(ImpObject):
    """
    Represents a ScheduleTableStyleHeaderTree.
    
    ScheduleTableStyleHeaderTree()
    """
    def Contains(self, node):
        """
        Contains(self: ScheduleTableStyleHeaderTree, node: ScheduleTableStyleHeaderNode) -> bool
        
            Determines if the tree contains the specified node.
        
            node: The specified node.
            Returns: Whether the tree contains the specified node.
        """
        pass

    def DeleteNode(self, pNode):
        """
        DeleteNode(self: ScheduleTableStyleHeaderTree, pNode: ScheduleTableStyleHeaderNode)
            Delete a specified node.
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def InsertNode(self, text, newIndex, parent, children):
        """
        InsertNode(self: ScheduleTableStyleHeaderTree, text: str, newIndex: int, parent: ScheduleTableStyleHeaderNode, children: Array[ScheduleTableStyleHeaderNode]) -> ScheduleTableStyleHeaderNode
        
            Insert a node to specific position.
        
            text: Text of the node.
            newIndex: The new index of the node.
            parent: Parent of the node.
            children: Children of the node.
            Returns: The newly inserted node.
        """
        pass

    def IsNodeChildOf(self, node, parent):
        """
        IsNodeChildOf(self: ScheduleTableStyleHeaderTree, node: ScheduleTableStyleHeaderNode, parent: ScheduleTableStyleHeaderNode) -> bool
        
            Determine if a specified node is the child node of another node.
        
            node: The node.
            parent: The parent node.
            Returns: Whether the node is the child node of another node.
        """
        pass

    def MoveNode(self, node, originalParent, originalIndex, newParent, newIndex):
        """
        MoveNode(self: ScheduleTableStyleHeaderTree, node: ScheduleTableStyleHeaderNode, originalParent: ScheduleTableStyleHeaderNode, originalIndex: int, newParent: ScheduleTableStyleHeaderNode, newIndex: int)
            Move the specified node from the old parent to a new parent.
        
            node: The node to be moved.
            originalParent: The original parent.
            originalIndex: The original index of the node.
            newParent: The new parent.
            newIndex: The new index of the node.
        """
        pass

    def ShiftNode(self, node, amount):
        """
        ShiftNode(self: ScheduleTableStyleHeaderTree, node: ScheduleTableStyleHeaderNode, amount: int)
            Shift specified node.
        
            node: The node to be shifted.
            amount: The amount.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass

    Columns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the ScheduleTableStyleColumn collection.

Get: Columns(self: ScheduleTableStyleHeaderTree) -> ScheduleTableStyleColumnCollection

"""

    MaxLevel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the max level of the tree.

Get: MaxLevel(self: ScheduleTableStyleHeaderTree) -> int

"""

    Root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the root node of the tree.

Get: Root(self: ScheduleTableStyleHeaderTree) -> ScheduleTableStyleHeaderNode

"""



class ScheduleTableStyleHeaderTreeIterator(DisposableWrapper):
    """
    Represents a ScheduleTableStyleHeaderTreeIterator.
    
    ScheduleTableStyleHeaderTreeIterator(tree: ScheduleTableStyleHeaderTree, type: IteratorType)
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Dump(self):
        """
        Dump(self: ScheduleTableStyleHeaderTreeIterator)
            Debug function.
        """
        pass

    def GetNext(self):
        """ GetNext(self: ScheduleTableStyleHeaderTreeIterator) -> ScheduleTableStyleHeaderNode """
        pass

    def Reset(self):
        """
        Reset(self: ScheduleTableStyleHeaderTreeIterator)
            Reset the iterator. Note that this operation DOES NOT reload the tree. If your 
             tree is modified, then you're in trouble.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tree, type):
        """
        __new__(cls: type, tree: ScheduleTableStyleHeaderTree, type: IteratorType)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class ScheduleTableStyleHeaderTreeNode(ScheduleTableStyleHeaderNode):
    """
    Represents a ScheduleTableStyleHeaderTreeNode.
    
    ScheduleTableStyleHeaderTreeNode()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        """
        pass


class SeparatorType(Enum):
    """
    Defines identifiers that indicate the separator type.
    
    enum SeparatorType, values: Comma (1), None (3), Period (0), Space (2)
    """
    Comma = None
    None = None
    Period = None
    Space = None
    value__ = None


class SortOrder(Enum):
    """
    Defines identifiers that indicate the sort order.
    
    enum SortOrder, values: Ascending (1), Descending (2)
    """
    Ascending = None
    Descending = None
    value__ = None


class UnitsType(Enum):
    """
    Defines identifiers that indicate the unit type.
    
    enum UnitsType, values: Architectural (4), Decimal (2), Degrees (0), DegreesMinutesSeconds (1), Engineering (3), Fractional (5), Gradians (2), Radians (3), Scientific (1), Surveyor (4), WindowsDesktop (6)
    """
    Architectural = None
    Decimal = None
    Degrees = None
    DegreesMinutesSeconds = None
    Engineering = None
    Fractional = None
    Gradians = None
    Radians = None
    Scientific = None
    Surveyor = None
    value__ = None
    WindowsDesktop = None


