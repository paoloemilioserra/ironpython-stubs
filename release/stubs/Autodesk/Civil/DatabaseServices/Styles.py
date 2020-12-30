# encoding: utf-8
# module Autodesk.Civil.DatabaseServices.Styles calls itself Styles
# from AeccDbMgd, Version=13.3.854.0, Culture=neutral, PublicKeyToken=null, AeccPressurePipesMgd, Version=13.3.854.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class StyleBase(DBObject):
    # no doc
    def CopyAsSibling(self, styleName):
        """ CopyAsSibling(self: StyleBase, styleName: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def ExportTo(*__args):
        """ ExportTo(self: StyleBase, destinationDatabase: Database, conflictResolution: StyleConflictResolverType)ExportTo(styleIds: ObjectIdCollection, destinationDatabase: Database, conflictResolution: StyleConflictResolverType) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    CreateBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreateBy(self: StyleBase) -> str

Set: CreateBy(self: StyleBase) = value
"""

    DateCreated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateCreated(self: StyleBase) -> str

"""

    DateModified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DateModified(self: StyleBase) -> str

"""

    IsUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsUsed(self: StyleBase) -> bool

"""

    ModifiedBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModifiedBy(self: StyleBase) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: Name(self: StyleBase) = value
"""



class AlignmentDesignCheckSet(StyleBase):
    # no doc
    def AddDesignCheck(self, type, name):
        """ AddDesignCheck(self: AlignmentDesignCheckSet, type: AlignmentDesignCheckType, name: str) -> AlignmentDesignCheck """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAllDesignChecks(self):
        """ GetAllDesignChecks(self: AlignmentDesignCheckSet) -> Array[AlignmentDesignCheck] """
        pass

    def RemoveAllDesignCheck(self):
        """ RemoveAllDesignCheck(self: AlignmentDesignCheckSet) """
        pass

    def RemoveDesignCheck(self, *__args):
        """ RemoveDesignCheck(self: AlignmentDesignCheckSet, type: AlignmentDesignCheckType, name: str)RemoveDesignCheck(self: AlignmentDesignCheckSet, designCheck: AlignmentDesignCheck) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class StyleCollectionBase(TreeOidWrapper):
    # no doc
    def Add(self, name):
        """ Add(self: StyleCollectionBase, name: str) -> ObjectId """
        pass

    def Contains(self, *__args):
        """
        Contains(self: StyleCollectionBase, item: ObjectId) -> bool
        Contains(self: StyleCollectionBase, styleName: str) -> bool
        """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: StyleCollectionBase) -> IEnumerator[ObjectId] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: StyleCollectionBase) -> IEnumerator """
        pass

    def Remove(self, *__args):
        """ Remove(self: StyleCollectionBase, index: int)Remove(self: StyleCollectionBase, styleName: str)Remove(self: StyleCollectionBase, style: StyleBase) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ObjectId](enumerable: IEnumerable[ObjectId], value: ObjectId) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: StyleCollectionBase) -> int

"""



class AlignmentDesignCheckSetCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: AlignmentDesignCheckSetCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class AlignmentDisplayStyleType(Enum):
    """ enum AlignmentDisplayStyleType, values: Arrow (3), Curve (1), CurveExtensions (5), Line (0), LineExtensions (4), Spiral (2), TangentExtensions (11), WarningSymbol (20) """
    Arrow = None
    Curve = None
    CurveExtensions = None
    Line = None
    LineExtensions = None
    Spiral = None
    TangentExtensions = None
    value__ = None
    WarningSymbol = None


class BaseLabelSetItem(CivilWrapper<AeccDbAlignStnLabelsDlgTemplate>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignStnLabelsDlgTemplate>, A_0: bool) """
        pass

    def GetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,AcDbObjectId>(self, *args): #cannot find CLR method
        """ GetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,AcDbObjectId>(self: BaseLabelSetItem, : AcDbObjectId*, attributeId: UInt32) -> AcDbObjectId* """
        pass

    def GetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,double>(self, *args): #cannot find CLR method
        """ GetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,double>(self: BaseLabelSetItem, attributeId: UInt32) -> float """
        pass

    def GetAttributeValue<AeccDbSectionLabelsDlgTemplate,double>(self, *args): #cannot find CLR method
        """ GetAttributeValue<AeccDbSectionLabelsDlgTemplate,double>(self: BaseLabelSetItem, attributeId: UInt32) -> float """
        pass

    def GetAttributeValue<AeccDbSectionLabelsDlgTemplate,int>(self, *args): #cannot find CLR method
        """ GetAttributeValue<AeccDbSectionLabelsDlgTemplate,int>(self: BaseLabelSetItem, attributeId: UInt32) -> int """
        pass

    def GetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,double>(self, *args): #cannot find CLR method
        """ GetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,double>(self: BaseLabelSetItem, attributeId: UInt32) -> float """
        pass

    def GetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,int>(self, *args): #cannot find CLR method
        """ GetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,int>(self: BaseLabelSetItem, attributeId: UInt32) -> int """
        pass

    def GetDrawingValue(self, *args): #cannot find CLR method
        """ GetDrawingValue(self: BaseLabelSetItem, newValue: float) -> float """
        pass

    def GetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::AlignmentPointType>(self, *args): #cannot find CLR method
        """ GetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::AlignmentPointType>(self: BaseLabelSetItem) -> Dictionary[AlignmentPointType, bool] """
        pass

    def GetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::ProfilePointType>(self, *args): #cannot find CLR method
        """ GetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::ProfilePointType>(self: BaseLabelSetItem) -> Dictionary[ProfilePointType, bool] """
        pass

    def GetLabeledPointTypes<AeccSuperElevationDataElement::TransitionPointType,Autodesk::Civil::SuperelevationPointType>(self, *args): #cannot find CLR method
        """ GetLabeledPointTypes<AeccSuperElevationDataElement::TransitionPointType,Autodesk::Civil::SuperelevationPointType>(self: BaseLabelSetItem) -> Dictionary[SuperelevationPointType, bool] """
        pass

    def SetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,AcDbObjectId>(self, *args): #cannot find CLR method
        """ SetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,AcDbObjectId>(self: BaseLabelSetItem, attributeId: UInt32, newValue: AcDbObjectId) """
        pass

    def SetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,double>(self, *args): #cannot find CLR method
        """ SetAttributeValue<AeccDbAlignStnLabelsDlgTemplate,double>(self: BaseLabelSetItem, attributeId: UInt32, newValue: float) """
        pass

    def SetAttributeValue<AeccDbSectionLabelsDlgTemplate,double>(self, *args): #cannot find CLR method
        """ SetAttributeValue<AeccDbSectionLabelsDlgTemplate,double>(self: BaseLabelSetItem, attributeId: UInt32, newValue: float) """
        pass

    def SetAttributeValue<AeccDbSectionLabelsDlgTemplate,int>(self, *args): #cannot find CLR method
        """ SetAttributeValue<AeccDbSectionLabelsDlgTemplate,int>(self: BaseLabelSetItem, attributeId: UInt32, newValue: int) """
        pass

    def SetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,double>(self, *args): #cannot find CLR method
        """ SetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,double>(self: BaseLabelSetItem, attributeId: UInt32, newValue: float) """
        pass

    def SetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,int>(self, *args): #cannot find CLR method
        """ SetAttributeValue<AeccDbVAlignStnLabelsDlgTemplate,int>(self: BaseLabelSetItem, attributeId: UInt32, newValue: int) """
        pass

    def SetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::AlignmentPointType>(self, *args): #cannot find CLR method
        """ SetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::AlignmentPointType>(self: BaseLabelSetItem, pointTypes: Dictionary[AlignmentPointType, bool]) """
        pass

    def SetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::ProfilePointType>(self, *args): #cannot find CLR method
        """ SetLabeledPointTypes<AeccAlignStation::GeometryPointStnType,Autodesk::Civil::ProfilePointType>(self: BaseLabelSetItem, pointTypes: Dictionary[ProfilePointType, bool]) """
        pass

    def SetLabeledPointTypes<AeccSuperElevationDataElement::TransitionPointType,Autodesk::Civil::SuperelevationPointType>(self, *args): #cannot find CLR method
        """ SetLabeledPointTypes<AeccSuperElevationDataElement::TransitionPointType,Autodesk::Civil::SuperelevationPointType>(self: BaseLabelSetItem, pointTypes: Dictionary[SuperelevationPointType, bool]) """
        pass

    def ValidateDistance(self, *args): #cannot find CLR method
        """ ValidateDistance(self: BaseLabelSetItem, newValue: float, szSettingsRoot: Char*, nRangeType: RangeType, nAttrId: UInt32) """
        pass

    def ValidatePlotHeight(self, *args): #cannot find CLR method
        """ ValidatePlotHeight(self: BaseLabelSetItem, newValue: float, szSettingsRoot: Char*, nRangeType: RangeType) """
        pass

    LabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleId(self: BaseLabelSetItem) -> ObjectId

Set: LabelStyleId(self: BaseLabelSetItem) = value
"""

    LabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleName(self: BaseLabelSetItem) -> str

Set: LabelStyleName(self: BaseLabelSetItem) = value
"""

    LabelStyleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleType(self: BaseLabelSetItem) -> LabelStyleType

"""



class AlignmentLabelSetItem(BaseLabelSetItem):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignStnLabelsDlgTemplate>, A_0: bool) """
        pass

    def GetLabeledAlignmentGeometryPoints(self):
        """ GetLabeledAlignmentGeometryPoints(self: AlignmentLabelSetItem) -> Dictionary[AlignmentPointType, bool] """
        pass

    def GetLabeledProfileGeometryPoints(self):
        """ GetLabeledProfileGeometryPoints(self: AlignmentLabelSetItem) -> Dictionary[ProfilePointType, bool] """
        pass

    def GetLabeledSuperelevationTransitionPoints(self):
        """ GetLabeledSuperelevationTransitionPoints(self: AlignmentLabelSetItem) -> Dictionary[SuperelevationPointType, bool] """
        pass

    def SetLabeledAlignmentGeometryPoints(self, pointTypes):
        """ SetLabeledAlignmentGeometryPoints(self: AlignmentLabelSetItem, pointTypes: Dictionary[AlignmentPointType, bool]) """
        pass

    def SetLabeledProfileGeometryPoints(self, pointTypes):
        """ SetLabeledProfileGeometryPoints(self: AlignmentLabelSetItem, pointTypes: Dictionary[ProfilePointType, bool]) """
        pass

    def SetLabeledSuperelevationTransitionPoints(self, pointTypes):
        """ SetLabeledSuperelevationTransitionPoints(self: AlignmentLabelSetItem, pointTypes: Dictionary[SuperelevationPointType, bool]) """
        pass

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: AlignmentLabelSetItem) -> float

Set: Increment(self: AlignmentLabelSetItem) = value
"""



class BaseLabelSetStyle(StyleBase):
    # no doc
    def Add(self, *__args):
        """ Add(self: BaseLabelSetStyle, labelStyleType: LabelStyleType, labelStyleName: str)Add(self: BaseLabelSetStyle, labelStyleId: ObjectId)Add(self: BaseLabelSetStyle, majorStation: BaseLabelSetItem, minorStationLabelStyleName: str)Add(self: BaseLabelSetStyle, majorStation: BaseLabelSetItem, minorStationLabelStyleId: ObjectId) """
        pass

    def CheckLabelStyleType(self, *args): #cannot find CLR method
        """ CheckLabelStyleType(self: BaseLabelSetStyle, type: LabelStyleType) """
        pass

    def CreateLabelGroup(self, *args): #cannot find CLR method
        """ CreateLabelGroup(self: BaseLabelSetStyle, pLabelingClassDesc: AcRxClass*, oidLabelStyle: AeccDbTreeOid, pParent: LABEL_SET_DATA*) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetLabelingDesc(self, *args): #cannot find CLR method
        """ GetLabelingDesc(labelStyleType: AeccAtom*) -> AcRxClass* """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: BaseLabelSetStyle, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BaseLabelSetStyle) -> int

"""



class AlignmentLabelSetStyle(BaseLabelSetStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AlignmentLabelSetStyle) -> IEnumerator[AlignmentLabelSetItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: AlignmentLabelSetStyle) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[AlignmentLabelSetItem](enumerable: IEnumerable[AlignmentLabelSetItem], value: AlignmentLabelSetItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class AlignmentLabelSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: AlignmentLabelSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class AlignmentStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: AlignmentStyle, type: AlignmentDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: AlignmentStyle, type: AlignmentDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self):
        """ GetDisplayStyleSection(self: AlignmentStyle) -> DisplayStyle """
        pass

    def GetLineMarkerDisplayStyleSection(self):
        """ GetLineMarkerDisplayStyleSection(self: AlignmentStyle) -> DisplayStyle """
        pass

    ArrowHeadOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowHeadOption(self: AlignmentStyle) -> ArrowHeadOption

"""

    BeginPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeginPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: BeginPointMarkerStyle(self: AlignmentStyle) = value
"""

    CompoundCurveIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CompoundCurveIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: CompoundCurveIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    CurveLineIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveLineIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: CurveLineIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    CurveSpiralIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveSpiralIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: CurveSpiralIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    EnableRadiusSnap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableRadiusSnap(self: AlignmentStyle) -> bool

Set: EnableRadiusSnap(self: AlignmentStyle) = value
"""

    EndPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: EndPointMarkerStyle(self: AlignmentStyle) = value
"""

    IntersectionPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: IntersectionPointMarkerStyle(self: AlignmentStyle) = value
"""

    LineCurveIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineCurveIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: LineCurveIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    LineMarkerDisplayStyleSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineMarkerDisplayStyleSection(self: AlignmentStyle) -> DisplayStyle

"""

    LineSpiralIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSpiralIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: LineSpiralIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    MidPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: MidPointMarkerStyle(self: AlignmentStyle) = value
"""

    RadiusSnapValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadiusSnapValue(self: AlignmentStyle) -> float

Set: RadiusSnapValue(self: AlignmentStyle) = value
"""

    ReverseCurveIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseCurveIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: ReverseCurveIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    ReverseSpiralIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseSpiralIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: ReverseSpiralIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    SpiralCurveIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralCurveIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: SpiralCurveIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    SpiralLineIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralLineIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: SpiralLineIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    SpiralSpiralIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralSpiralIntersectPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: SpiralSpiralIntersectPointMarkerStyle(self: AlignmentStyle) = value
"""

    StationReferencePointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationReferencePointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: StationReferencePointMarkerStyle(self: AlignmentStyle) = value
"""

    ThroughPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPointMarkerStyle(self: AlignmentStyle) -> ObjectId

Set: ThroughPointMarkerStyle(self: AlignmentStyle) = value
"""



class AlignmentStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: AlignmentStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class ArrowHeadOption(CivilWrapper<AeccDbStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStyle>, A_0: bool) """
        pass

    ArrowBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowBlockName(self: ArrowHeadOption) -> str

Set: ArrowBlockName(self: ArrowHeadOption) = value
"""

    ArrowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowType(self: ArrowHeadOption) -> ArrowHeadType

Set: ArrowType(self: ArrowHeadOption) = value
"""

    Fit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Fit(self: ArrowHeadOption) -> ArrowHeadFitType

Set: Fit(self: ArrowHeadOption) = value
"""

    FixedScaleX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedScaleX(self: ArrowHeadOption) -> float

Set: FixedScaleX(self: ArrowHeadOption) = value
"""

    FixedScaleY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedScaleY(self: ArrowHeadOption) -> float

"""

    FixedScaleZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedScaleZ(self: ArrowHeadOption) -> float

"""

    SizeOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeOption(self: ArrowHeadOption) -> ArrowHeadSizeType

Set: SizeOption(self: ArrowHeadOption) = value
"""

    SizeValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeValue(self: ArrowHeadOption) -> float

Set: SizeValue(self: ArrowHeadOption) = value
"""



class AssemblyStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: AssemblyStyle, type: AssemblyDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: AssemblyStyle, type: AssemblyDisplayStyleType) -> DisplayStyle """
        pass

    MarkerStyleAtAssemblyOriginId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleAtAssemblyOriginId(self: AssemblyStyle) -> ObjectId

"""

    MarkerStyleAtMainBaselineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleAtMainBaselineId(self: AssemblyStyle) -> ObjectId

"""

    MarkerStyleAtMainBaselineOriginId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleAtMainBaselineOriginId(self: AssemblyStyle) -> ObjectId

"""

    MarkerStyleAtOffsetBaselineId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleAtOffsetBaselineId(self: AssemblyStyle) -> ObjectId

"""

    MarkerStyleAtOffsetBaselineOriginId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleAtOffsetBaselineOriginId(self: AssemblyStyle) -> ObjectId

"""



class AssemblyStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: AssemblyStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class AxisPosition(Enum):
    """ enum AxisPosition, values: Bottom (2), Center (4), Left (3), Middle (1), Right (5), Top (0) """
    Bottom = None
    Center = None
    Left = None
    Middle = None
    Right = None
    Top = None
    value__ = None


class AxisStyle(CivilWrapper<AeccDbGraphStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyle>, A_0: bool) """
        pass

    HorizontalGeometryTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HorizontalGeometryTickStyle(self: AxisStyle) -> AxisTickStyle

"""

    MajorTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorTickStyle(self: AxisStyle) -> AxisTickStyle

"""

    MinorTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorTickStyle(self: AxisStyle) -> AxisTickStyle

"""

    ShowTickAndLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowTickAndLabel(self: AxisStyle) -> bool

Set: ShowTickAndLabel(self: AxisStyle) = value
"""

    TitleStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleStyle(self: AxisStyle) -> AxisTitleStyle

"""



class AxisTickJustificationType(Enum):
    """ enum AxisTickJustificationType, values: BottomOrRight (1), Center (2), TopOrLeft (0) """
    BottomOrRight = None
    Center = None
    TopOrLeft = None
    value__ = None


class AxisTickStyle(CivilWrapper<AeccDbGraphStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyle>, A_0: bool) """
        pass

    Interval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interval(self: AxisTickStyle) -> float

Set: Interval(self: AxisTickStyle) = value
"""

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Justification(self: AxisTickStyle) -> AxisTickJustificationType

Set: Justification(self: AxisTickStyle) = value
"""

    LabelText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelText(self: AxisTickStyle) -> str

Set: LabelText(self: AxisTickStyle) = value
"""

    OffsetX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetX(self: AxisTickStyle) -> float

Set: OffsetX(self: AxisTickStyle) = value
"""

    OffsetY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetY(self: AxisTickStyle) -> float

Set: OffsetY(self: AxisTickStyle) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: AxisTickStyle) -> float

Set: Rotation(self: AxisTickStyle) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: AxisTickStyle) -> float

Set: Size(self: AxisTickStyle) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: AxisTickStyle) -> float

Set: TextHeight(self: AxisTickStyle) = value
"""

    TextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyle(self: AxisTickStyle) -> str

Set: TextStyle(self: AxisTickStyle) = value
"""

    TickAndLabelStartElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TickAndLabelStartElevation(self: AxisTickStyle) -> bool

Set: TickAndLabelStartElevation(self: AxisTickStyle) = value
"""



class AxisTickType(Enum):
    """ enum AxisTickType, values: HorizontalGeometry (2), Major (0), Minor (1) """
    HorizontalGeometry = None
    Major = None
    Minor = None
    value__ = None


class AxisTitleLocationType(Enum):
    """ enum AxisTitleLocationType, values: BottomOrRight (0), Center (1), TopOrLeft (2) """
    BottomOrRight = None
    Center = None
    TopOrLeft = None
    value__ = None


class AxisTitleStyle(CivilWrapper<AeccDbGraphStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyle>, A_0: bool) """
        pass

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: AxisTitleStyle) -> AxisTitleLocationType

Set: Location(self: AxisTitleStyle) = value
"""

    OffsetX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetX(self: AxisTitleStyle) -> float

Set: OffsetX(self: AxisTitleStyle) = value
"""

    OffsetY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetY(self: AxisTitleStyle) -> float

Set: OffsetY(self: AxisTitleStyle) = value
"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: AxisTitleStyle) -> float

Set: Rotation(self: AxisTitleStyle) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: AxisTitleStyle) -> str

Set: Text(self: AxisTitleStyle) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: AxisTitleStyle) -> float

Set: TextHeight(self: AxisTitleStyle) = value
"""

    TextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyle(self: AxisTitleStyle) -> str

Set: TextStyle(self: AxisTitleStyle) = value
"""



class BandLabelStyleType(Enum):
    """ enum BandLabelStyleType, values: HorizontalGeometryCurve (268547088), HorizontalGeometrySpiral (268547104), HorizontalGeometryTangent (268547072), PipeNetworkPipeLocation (268547648), PipeNetworkStructureLocation (268547632), ProfileDataHGP (268546592), ProfileDataIncrementalDistance (268546640), ProfileDataMajorIncrement (268546560), ProfileDataMinorIncrement (268546576), ProfileDataStationEquation (268546624), ProfileDataVGP (268546608), SectionalDataIncrementalSectionData (268547680), SectionalDataSampleLineLocation (268547664), SectionDataCenterline (268562976), SectionDataGradeBreaks (268563008), SectionDataIncrementalDistance (268563024), SectionDataMajorIncrement (268562944), SectionDataMinorIncrement (268562960), SectionDataSampleLineVertices (268562992), SectionSegmentSurfaceLabels (268563200), SuperelevationDataFullSuper (268547376), SuperelevationDataLevelCrown (268547392), SuperelevationDataNormalCrown (268547328), SuperelevationDataReverseCrown (268547360), SuperelevationDataShoulderCritical (268547616), SuperelevationDataSlopeTransition (268547408), VerticalGeometryCrestCurve (268546848), VerticalGeometryDownhillTangent (268546832), VerticalGeometrySagCurve (268546864), VerticalGeometryUphillTangent (268546816) """
    HorizontalGeometryCurve = None
    HorizontalGeometrySpiral = None
    HorizontalGeometryTangent = None
    PipeNetworkPipeLocation = None
    PipeNetworkStructureLocation = None
    ProfileDataHGP = None
    ProfileDataIncrementalDistance = None
    ProfileDataMajorIncrement = None
    ProfileDataMinorIncrement = None
    ProfileDataStationEquation = None
    ProfileDataVGP = None
    SectionalDataIncrementalSectionData = None
    SectionalDataSampleLineLocation = None
    SectionDataCenterline = None
    SectionDataGradeBreaks = None
    SectionDataIncrementalDistance = None
    SectionDataMajorIncrement = None
    SectionDataMinorIncrement = None
    SectionDataSampleLineVertices = None
    SectionSegmentSurfaceLabels = None
    SuperelevationDataFullSuper = None
    SuperelevationDataLevelCrown = None
    SuperelevationDataNormalCrown = None
    SuperelevationDataReverseCrown = None
    SuperelevationDataShoulderCritical = None
    SuperelevationDataSlopeTransition = None
    value__ = None
    VerticalGeometryCrestCurve = None
    VerticalGeometryDownhillTangent = None
    VerticalGeometrySagCurve = None
    VerticalGeometryUphillTangent = None


class BandSetItem(object):
    # no doc
    def GetImpObj(self, *args): #cannot find CLR method
        """ GetImpObj(self: BandSetItem) -> AeccDbBandStyleSetData* """
        pass

    BandStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandStyleId(self: BandSetItem) -> ObjectId

Set: BandStyleId(self: BandSetItem) = value
"""

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: BandSetItem) -> BandType

"""

    Gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Gap(self: BandSetItem) -> float

Set: Gap(self: BandSetItem) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: BandSetItem) -> BandLocationType

"""

    MajorInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorInterval(self: BandSetItem) -> float

Set: MajorInterval(self: BandSetItem) = value
"""

    MinorInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorInterval(self: BandSetItem) -> float

Set: MinorInterval(self: BandSetItem) = value
"""

    SettingsNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ShowLabels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowLabels(self: BandSetItem) -> bool

Set: ShowLabels(self: BandSetItem) = value
"""

    StaggerLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLabel(self: BandSetItem) -> StaggerLabelType

Set: StaggerLabel(self: BandSetItem) = value
"""

    StaggerLineHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight(self: BandSetItem) -> float

Set: StaggerLineHeight(self: BandSetItem) = value
"""

    Weeding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weeding(self: BandSetItem) -> float

Set: Weeding(self: BandSetItem) = value
"""



class BandSetItemCollection(object):
    """ BandSetItemCollection(location: BandLocationType) """
    def Add(self, bandStyleId):
        """ Add(self: BandSetItemCollection, bandStyleId: ObjectId) """
        pass

    def checkBandStyleIdByType(self, *args): #cannot find CLR method
        """ checkBandStyleIdByType(self: BandSetItemCollection, oidBandStyle: AcDbObjectId) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: BandSetItemCollection) """
        pass

    def getInitializedAeccDbBandStyleSetData(self, *args): #cannot find CLR method
        """ getInitializedAeccDbBandStyleSetData(self: BandSetItemCollection, oidBandStyle: AcDbObjectId) -> AeccDbBandStyleSetData* """
        pass

    def RemoveAll(self):
        """ RemoveAll(self: BandSetItemCollection) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: BandSetItemCollection, index: int) """
        pass

    def Swap(self, index1, index2):
        """ Swap(self: BandSetItemCollection, index1: int, index2: int) """
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

    @staticmethod # known case of __new__
    def __new__(self, location):
        """ __new__(cls: type, location: BandLocationType) """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: BandSetItemCollection) -> int

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: BandSetItemCollection) -> BandLocationType

"""



class BandSetStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def getBottomBandSet(self, *args): #cannot find CLR method
        """ getBottomBandSet(self: BandSetStyle) -> vector<AeccDbBandStyleSetData \*\,std::allocator<AeccDbBandStyleSetData \*> >* """
        pass

    def getTopBandSet(self, *args): #cannot find CLR method
        """ getTopBandSet(self: BandSetStyle) -> vector<AeccDbBandStyleSetData \*\,std::allocator<AeccDbBandStyleSetData \*> >* """
        pass

    def setBottomBandSetItems(self, *args): #cannot find CLR method
        """ setBottomBandSetItems(self: BandSetStyle, bandSetItems: BandSetItemCollection) """
        pass

    def setTopBandSetItems(self, *args): #cannot find CLR method
        """ setTopBandSetItems(self: BandSetStyle, bandSetItems: BandSetItemCollection) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    MatchIncrementToGridIntervals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchIncrementToGridIntervals(self: BandSetStyle) -> bool

Set: MatchIncrementToGridIntervals(self: BandSetStyle) = value
"""



class BandStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetBandStyleId(database, bandType, bandStyleName):
        """ GetBandStyleId(database: Database, bandType: BandType, bandStyleName: str) -> ObjectId """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    BandHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandHeight(self: BandStyle) -> float

Set: BandHeight(self: BandStyle) = value
"""

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: BandStyle) -> BandType

"""

    OffsetFromBand = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetFromBand(self: BandStyle) -> float

Set: OffsetFromBand(self: BandStyle) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: BandStyle) -> str

Set: Text(self: BandStyle) = value
"""

    TextBoxPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextBoxPosition(self: BandStyle) -> BandTitleBoxPosition

Set: TextBoxPosition(self: BandStyle) = value
"""

    TextBoxWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextBoxWidth(self: BandStyle) -> float

Set: TextBoxWidth(self: BandStyle) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: BandStyle) -> float

Set: TextHeight(self: BandStyle) = value
"""

    TextLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextLocation(self: BandStyle) -> BandTitleTextLocation

Set: TextLocation(self: BandStyle) = value
"""

    TextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyle(self: BandStyle) -> str

Set: TextStyle(self: BandStyle) = value
"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: BandStyle) -> ObjectId

"""

    WeedingFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WeedingFactor(self: BandStyle) -> float

Set: WeedingFactor(self: BandStyle) = value
"""



class BandStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: BandStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class BandStylesRoot(TreeOidWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    ProfileViewHorizontalGeometryBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewHorizontalGeometryBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""

    ProfileViewPipeNetworkBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewPipeNetworkBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""

    ProfileViewProfileDataBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewProfileDataBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""

    ProfileViewSectionalDataBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewSectionalDataBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""

    ProfileViewSuperElevationBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewSuperElevationBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""

    ProfileViewVerticalGeometryBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewVerticalGeometryBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""

    SectionViewSectionDataBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewSectionDataBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""

    SectionViewSegmentsBandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewSegmentsBandStyles(self: BandStylesRoot) -> BandStyleCollection

"""



class BandStylesRootPressurePipesExtension(object):
    # no doc
    @staticmethod
    def GetProfileViewPressureNetworkBandStyles(bandStylesRoot):
        """ GetProfileViewPressureNetworkBandStyles(bandStylesRoot: BandStylesRoot) -> BandStyleCollection """
        pass

    __all__ = [
        'GetProfileViewPressureNetworkBandStyles',
    ]


class BandTickStyle(CivilWrapper<AeccDbGraphStyleBands>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyleBands>, A_0: bool) """
        pass

    IncrementSmallTicksAtBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementSmallTicksAtBottom(self: BandTickStyle) -> bool

Set: IncrementSmallTicksAtBottom(self: BandTickStyle) = value
"""

    IncrementSmallTicksAtMiddle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementSmallTicksAtMiddle(self: BandTickStyle) -> bool

Set: IncrementSmallTicksAtMiddle(self: BandTickStyle) = value
"""

    IncrementSmallTicksAtTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementSmallTicksAtTop(self: BandTickStyle) -> bool

Set: IncrementSmallTicksAtTop(self: BandTickStyle) = value
"""

    IncrementTicksToFullHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementTicksToFullHeight(self: BandTickStyle) -> bool

Set: IncrementTicksToFullHeight(self: BandTickStyle) = value
"""

    SmallTicksAtBottomSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallTicksAtBottomSize(self: BandTickStyle) -> float

Set: SmallTicksAtBottomSize(self: BandTickStyle) = value
"""

    SmallTicksAtMiddleSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallTicksAtMiddleSize(self: BandTickStyle) -> float

Set: SmallTicksAtMiddleSize(self: BandTickStyle) = value
"""

    SmallTicksAtTopSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmallTicksAtTopSize(self: BandTickStyle) -> float

Set: SmallTicksAtTopSize(self: BandTickStyle) = value
"""



class BandTitleBoxPosition(Enum):
    """ enum BandTitleBoxPosition, values: LeftOfBand (0), RightOfBand (1) """
    LeftOfBand = None
    RightOfBand = None
    value__ = None


class BandTitleTextLocation(Enum):
    """ enum BandTitleTextLocation, values: Center (1), Left (2), Right (0) """
    Center = None
    Left = None
    Right = None
    value__ = None


class BuildingSiteDisplayStyleType(Enum):
    """ enum BuildingSiteDisplayStyleType, values: BuildingFootprint (0), BuildingModel (4), PropertyLines (1), SiteModel (3), Utilities (2) """
    BuildingFootprint = None
    BuildingModel = None
    PropertyLines = None
    SiteModel = None
    Utilities = None
    value__ = None


class BuildingSiteStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: BuildingSiteStyle, type: BuildingSiteDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: BuildingSiteStyle, type: BuildingSiteDisplayStyleType) -> DisplayStyle """
        pass

    MarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleId(self: BuildingSiteStyle) -> ObjectId

Set: MarkerStyleId(self: BuildingSiteStyle) = value
"""

    MarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleName(self: BuildingSiteStyle) -> str

Set: MarkerStyleName(self: BuildingSiteStyle) = value
"""



class BuildingSiteStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: BuildingSiteStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class CantViewStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: CantViewStyle, type: CantViewDisplayStyleType) -> DisplayStyle """
        pass

    AxisBottomMajorTickInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisBottomMajorTickInterval(self: CantViewStyle) -> float

Set: AxisBottomMajorTickInterval(self: CantViewStyle) = value
"""

    AxisTopMajorTickInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisTopMajorTickInterval(self: CantViewStyle) -> float

Set: AxisTopMajorTickInterval(self: CantViewStyle) = value
"""

    UseFullHeightTick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseFullHeightTick(self: CantViewStyle) -> bool

Set: UseFullHeightTick(self: CantViewStyle) = value
"""

    UseSmallTicksAtBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSmallTicksAtBottom(self: CantViewStyle) -> bool

Set: UseSmallTicksAtBottom(self: CantViewStyle) = value
"""

    UseSmallTicksAtMiddle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSmallTicksAtMiddle(self: CantViewStyle) -> bool

Set: UseSmallTicksAtMiddle(self: CantViewStyle) = value
"""

    UseSmallTicksAtTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSmallTicksAtTop(self: CantViewStyle) -> bool

Set: UseSmallTicksAtTop(self: CantViewStyle) = value
"""

    VerticalExaggeration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalExaggeration(self: CantViewStyle) -> float

Set: VerticalExaggeration(self: CantViewStyle) = value
"""



class CantViewStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: CantViewStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class CatchmentDisplayStylePlanType(Enum):
    """ enum CatchmentDisplayStylePlanType, values: CatchmentBoundary (0), CatchmentFlowPath (1) """
    CatchmentBoundary = None
    CatchmentFlowPath = None
    value__ = None


class CatchmentStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: CatchmentStyle, type: CatchmentDisplayStylePlanType) -> DisplayStyle """
        pass

    DischargePointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DischargePointMarkerStyle(self: CatchmentStyle) -> ObjectId

Set: DischargePointMarkerStyle(self: CatchmentStyle) = value
"""

    FlowSegmentStartPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowSegmentStartPointMarkerStyle(self: CatchmentStyle) -> ObjectId

Set: FlowSegmentStartPointMarkerStyle(self: CatchmentStyle) = value
"""

    MostDistantPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MostDistantPointMarkerStyle(self: CatchmentStyle) -> ObjectId

Set: MostDistantPointMarkerStyle(self: CatchmentStyle) = value
"""



class CatchmentStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: CatchmentStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class CenterMarkerSizeType(Enum):
    """ enum CenterMarkerSizeType, values: Fixed (2), PercentageOfScreen (0), Plotted (1) """
    Fixed = None
    PercentageOfScreen = None
    Plotted = None
    value__ = None


class CodeSetStyle(StyleBase):
    # no doc
    def Add(self, code, styleId):
        """ Add(self: CodeSetStyle, code: str, styleId: ObjectId) -> CodeSetStyleItem """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetCurrentStyleSetId():
        """ GetCurrentStyleSetId() -> ObjectId """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CodeSetStyle) -> IEnumerator[CodeSetStyleItem] """
        pass

    def GetItemBy(self, itemType, code):
        """ GetItemBy(self: CodeSetStyle, itemType: CodeSetStyleItemType, code: str) -> CodeSetStyleItem """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: CodeSetStyle) -> IEnumerator """
        pass

    def Remove(self, code):
        """ Remove(self: CodeSetStyle, code: str) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[CodeSetStyleItem](enumerable: IEnumerable[CodeSetStyleItem], value: CodeSetStyleItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: CodeSetStyle) -> int

"""

    SubentityStyleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubentityStyleType(self: CodeSetStyle) -> SubassemblySubentityStyleType

Set: SubentityStyleType(self: CodeSetStyle) = value
"""



class CodeSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: CodeSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class CodeSetStyleItem(CivilWrapper<AeccDbRoadwayStyleSet>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbRoadwayStyleSet>, A_0: bool) """
        pass

    Code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Code(self: CodeSetStyleItem) -> str

Set: Code(self: CodeSetStyleItem) = value
"""

    CodeStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeStyleId(self: CodeSetStyleItem) -> ObjectId

Set: CodeStyleId(self: CodeSetStyleItem) = value
"""

    CodeStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeStyleName(self: CodeSetStyleItem) -> str

Set: CodeStyleName(self: CodeSetStyleItem) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: CodeSetStyleItem) -> str

Set: Description(self: CodeSetStyleItem) = value
"""

    FeatureLineStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineStyleId(self: CodeSetStyleItem) -> ObjectId

Set: FeatureLineStyleId(self: CodeSetStyleItem) = value
"""

    FeatureLineStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineStyleName(self: CodeSetStyleItem) -> str

Set: FeatureLineStyleName(self: CodeSetStyleItem) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemType(self: CodeSetStyleItem) -> CodeSetStyleItemType

"""

    LabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleId(self: CodeSetStyleItem) -> ObjectId

Set: LabelStyleId(self: CodeSetStyleItem) = value
"""

    LabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleName(self: CodeSetStyleItem) -> str

Set: LabelStyleName(self: CodeSetStyleItem) = value
"""

    MaterialAreaFillStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialAreaFillStyleId(self: CodeSetStyleItem) -> ObjectId

Set: MaterialAreaFillStyleId(self: CodeSetStyleItem) = value
"""

    MaterialAreaFillStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialAreaFillStyleName(self: CodeSetStyleItem) -> str

Set: MaterialAreaFillStyleName(self: CodeSetStyleItem) = value
"""

    PayItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PayItems(self: CodeSetStyleItem) -> Array[str]

Set: PayItems(self: CodeSetStyleItem) = value
"""

    RenderMaterialStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMaterialStyleId(self: CodeSetStyleItem) -> ObjectId

Set: RenderMaterialStyleId(self: CodeSetStyleItem) = value
"""

    RenderMaterialStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMaterialStyleName(self: CodeSetStyleItem) -> str

Set: RenderMaterialStyleName(self: CodeSetStyleItem) = value
"""

    StyleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleType(self: CodeSetStyleItem) -> SubassemblySubentityStyleType

"""



class CodeSetStyleItemType(Enum):
    """ enum CodeSetStyleItemType, values: DefaultItemType (1), NoCodeItemType (2), NormalItemType (0) """
    DefaultItemType = None
    NoCodeItemType = None
    NormalItemType = None
    value__ = None


class ColorSchemeType(Enum):
    """ enum ColorSchemeType, values: Blues (0), Greens (1), Hydro (2), Land (3), Pastels (4), Rainbow (5), Reds (6) """
    Blues = None
    Greens = None
    Hydro = None
    Land = None
    Pastels = None
    Rainbow = None
    Reds = None
    value__ = None


class ColumnStyle(CivilWrapper<AeccDbScheduleTableStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbScheduleTableStyle>, A_0: bool) """
        pass

    def InternalGetContentString(self, *args): #cannot find CLR method
        """ InternalGetContentString(self: ColumnStyle, type: dataType) -> str """
        pass

    def InternalGetContentStringFormatted(self, *args): #cannot find CLR method
        """ InternalGetContentStringFormatted(self: ColumnStyle, type: dataType) -> str """
        pass

    def InternalSetContentString(self, *args): #cannot find CLR method
        """ InternalSetContentString(self: ColumnStyle, type: dataType, newVal: str) """
        pass

    def InternalSetContentStringFormatted(self, *args): #cannot find CLR method
        """ InternalSetContentStringFormatted(self: ColumnStyle, type: dataType, newVal: str) """
        pass

    ColumnWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnWidth(self: ColumnStyle) -> float

Set: ColumnWidth(self: ColumnStyle) = value
"""

    ContentJustification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentJustification(self: ColumnStyle) -> TextJustificationType

Set: ContentJustification(self: ColumnStyle) = value
"""

    ContentString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentString(self: ColumnStyle) -> str

Set: ContentString(self: ColumnStyle) = value
"""

    ContentStringFormatted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentStringFormatted(self: ColumnStyle) -> str

Set: ContentStringFormatted(self: ColumnStyle) = value
"""

    HeaderJustification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderJustification(self: ColumnStyle) -> TextJustificationType

Set: HeaderJustification(self: ColumnStyle) = value
"""

    HeaderString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderString(self: ColumnStyle) -> str

Set: HeaderString(self: ColumnStyle) = value
"""

    HeaderStringFormatted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderStringFormatted(self: ColumnStyle) -> str

Set: HeaderStringFormatted(self: ColumnStyle) = value
"""


    m_CurrentIndex = None


class ColumnStyleCollection(CivilWrapper<AeccDbScheduleTableStyle>):
    # no doc
    def Add(self):
        """ Add(self: ColumnStyleCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbScheduleTableStyle>, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ColumnStyleCollection) -> IEnumerator[ColumnStyle] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ColumnStyleCollection) -> IEnumerator """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ColumnStyleCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ColumnStyle](enumerable: IEnumerable[ColumnStyle], value: ColumnStyle) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ColumnStyleCollection) -> int

"""



class ContourSmoothingType(Enum):
    """ enum ContourSmoothingType, values: AddVertices (0), SplineCurve (1) """
    AddVertices = None
    SplineCurve = None
    value__ = None


class ContourValues(object):
    """ ContourValues(majorColr: Color, minorColor: Color, majorLineTypeId: ObjectId, minorLineTypeId: ObjectId, majorLineWight: LineWeight, minorLineWight: LineWeight) """
    @staticmethod # known case of __new__
    def __new__(self, majorColr, minorColor, majorLineTypeId, minorLineTypeId, majorLineWight, minorLineWight):
        """ __new__(cls: type, majorColr: Color, minorColor: Color, majorLineTypeId: ObjectId, minorLineTypeId: ObjectId, majorLineWight: LineWeight, minorLineWight: LineWeight) """
        pass

    MajorColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorColor(self: ContourValues) -> Color

Set: MajorColor(self: ContourValues) = value
"""

    MajorLineTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorLineTypeId(self: ContourValues) -> ObjectId

Set: MajorLineTypeId(self: ContourValues) = value
"""

    MajorLineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorLineWeight(self: ContourValues) -> LineWeight

Set: MajorLineWeight(self: ContourValues) = value
"""

    MinorColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorColor(self: ContourValues) -> Color

Set: MinorColor(self: ContourValues) = value
"""

    MinorLineTypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorLineTypeId(self: ContourValues) -> ObjectId

Set: MinorLineTypeId(self: ContourValues) = value
"""

    MinorLineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorLineWeight(self: ContourValues) -> LineWeight

Set: MinorLineWeight(self: ContourValues) = value
"""



class CorridorDisplayStyleType(Enum):
    """ enum CorridorDisplayStyleType, values: AssemblyInsertionStations (3), GeometricOverrideStations (2), ParameterOverrideStations (1), RegionBoundaries (0) """
    AssemblyInsertionStations = None
    GeometricOverrideStations = None
    ParameterOverrideStations = None
    RegionBoundaries = None
    value__ = None


class CorridorStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: CorridorStyle, type: CorridorDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: CorridorStyle, type: CorridorDisplayStyleType) -> DisplayStyle """
        pass


class CorridorStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: CorridorStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class CustomMarkerSuperimposeType(Enum):
    """ enum CustomMarkerSuperimposeType, values: Circle (2), None (0), Square (1), SquareCircle (3) """
    Circle = None
    None = None
    Square = None
    SquareCircle = None
    value__ = None


class CustomMarkerType(Enum):
    """ enum CustomMarkerType, values: CustomMarkerBlank (1), CustomMarkerDot (0), CustomMarkerPlus (2), CustomMarkerVLine (4), CustomMarkerX (3) """
    CustomMarkerBlank = None
    CustomMarkerDot = None
    CustomMarkerPlus = None
    CustomMarkerVLine = None
    CustomMarkerX = None
    value__ = None


class DataBandingType(Enum):
    """ enum DataBandingType, values: NumberOfRanges (0), RangesInterval (1), RangesIntervalWithDatum (2) """
    NumberOfRanges = None
    RangesInterval = None
    RangesIntervalWithDatum = None
    value__ = None


class DataPartFamily(object):
    # no doc
    BoundingShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingShape(self: DataPartFamily) -> BoundingShapeType

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: DataPartFamily) -> str

"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Domain(self: DataPartFamily) -> DomainType

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: DataPartFamily) -> str

"""

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartType(self: DataPartFamily) -> PartType

"""

    SweptShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SweptShape(self: DataPartFamily) -> SweptShapeType

"""



class DisplayStyle(CivilWrapper<AeccDbStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStyle>, A_0: bool) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: DisplayStyle) -> Color

Set: Color(self: DisplayStyle) = value
"""

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: DisplayStyle) -> str

Set: Layer(self: DisplayStyle) = value
"""

    Linetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetype(self: DisplayStyle) -> str

Set: Linetype(self: DisplayStyle) = value
"""

    LinetypeScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeScale(self: DisplayStyle) -> float

Set: LinetypeScale(self: DisplayStyle) = value
"""

    Lineweight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Lineweight(self: DisplayStyle) -> LineWeight

Set: Lineweight(self: DisplayStyle) = value
"""

    PlotStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotStyle(self: DisplayStyle) -> str

Set: PlotStyle(self: DisplayStyle) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: DisplayStyle) -> bool

Set: Visible(self: DisplayStyle) = value
"""



class Expression(object):
    # no doc
    def GetAttributeTypeInfoExpression(self, *args): #cannot find CLR method
        """ GetAttributeTypeInfoExpression(self: Expression) -> AeccAttributeTypeInfoExpression* """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: Expression) -> str

Set: Description(self: Expression) = value
"""

    ExpressionString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpressionString(self: Expression) -> str

Set: ExpressionString(self: Expression) = value
"""

    FormatResultAs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FormatResultAs(self: Expression) -> ExpressionFormatedType

Set: FormatResultAs(self: Expression) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Expression) -> str

"""



class ExpressionCollection(object):
    # no doc
    def Add(self, name, description, expression):
        """ Add(self: ExpressionCollection, name: str, description: str, expression: str) -> Expression """
        pass

    def Clear(self):
        """ Clear(self: ExpressionCollection) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ExpressionCollection) -> IEnumerator[Expression] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ExpressionCollection) -> IEnumerator """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: ExpressionCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Expression](enumerable: IEnumerable[Expression], value: Expression) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: ExpressionCollection) -> int

"""



class ExpressionFormatedType(Enum):
    """ enum ExpressionFormatedType, values: Angle (0), Area (1), Azimuth (2), Coordinate (3), Dimension (4), Direction (5), Distance (6), Double (7), Elevation (8), GradeSlope (9), Latitude (10), Longitude (11), Percent (12), Station (13), Volume (14) """
    Angle = None
    Area = None
    Azimuth = None
    Coordinate = None
    Dimension = None
    Direction = None
    Distance = None
    Double = None
    Elevation = None
    GradeSlope = None
    Latitude = None
    Longitude = None
    Percent = None
    Station = None
    value__ = None
    Volume = None


class FeatureLineDisplayStyleProfileType(Enum):
    """ enum FeatureLineDisplayStyleProfileType, values: BeginningVertex (2), EndingVertex (4), FeatureLine (0), InternalVertex (3) """
    BeginningVertex = None
    EndingVertex = None
    FeatureLine = None
    InternalVertex = None
    value__ = None


class FeatureLineStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleProfile(self, type):
        """ GetDisplayStyleProfile(self: FeatureLineStyle, type: FeatureLineDisplayStyleProfileType) -> DisplayStyle """
        pass

    def GetFeatureLineDisplayStyleModel(self):
        """ GetFeatureLineDisplayStyleModel(self: FeatureLineStyle) -> DisplayStyle """
        pass

    def GetFeatureLineDisplayStylePlan(self):
        """ GetFeatureLineDisplayStylePlan(self: FeatureLineStyle) -> DisplayStyle """
        pass

    def GetSectionMarkerDisplayStyleSection(self):
        """ GetSectionMarkerDisplayStyleSection(self: FeatureLineStyle) -> DisplayStyle """
        pass

    FeatureLineDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineDisplayStyleModel(self: FeatureLineStyle) -> DisplayStyle

"""

    FeatureLineDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineDisplayStylePlan(self: FeatureLineStyle) -> DisplayStyle

"""

    ProfileBeginningVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileBeginningVertexMarkerStyleId(self: FeatureLineStyle) -> ObjectId

Set: ProfileBeginningVertexMarkerStyleId(self: FeatureLineStyle) = value
"""

    ProfileBeginningVertexMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileBeginningVertexMarkerStyleName(self: FeatureLineStyle) -> str

Set: ProfileBeginningVertexMarkerStyleName(self: FeatureLineStyle) = value
"""

    ProfileEndingVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileEndingVertexMarkerStyleId(self: FeatureLineStyle) -> ObjectId

Set: ProfileEndingVertexMarkerStyleId(self: FeatureLineStyle) = value
"""

    ProfileEndingVertexMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileEndingVertexMarkerStyleName(self: FeatureLineStyle) -> str

Set: ProfileEndingVertexMarkerStyleName(self: FeatureLineStyle) = value
"""

    ProfileInternalVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileInternalVertexMarkerStyleId(self: FeatureLineStyle) -> ObjectId

Set: ProfileInternalVertexMarkerStyleId(self: FeatureLineStyle) = value
"""

    ProfileInternalVertexMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileInternalVertexMarkerStyleName(self: FeatureLineStyle) -> str

Set: ProfileInternalVertexMarkerStyleName(self: FeatureLineStyle) = value
"""

    SectionMarkerDisplayStyleSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionMarkerDisplayStyleSection(self: FeatureLineStyle) -> DisplayStyle

"""

    SectionMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionMarkerStyleId(self: FeatureLineStyle) -> ObjectId

Set: SectionMarkerStyleId(self: FeatureLineStyle) = value
"""

    SectionMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionMarkerStyleName(self: FeatureLineStyle) -> str

Set: SectionMarkerStyleName(self: FeatureLineStyle) = value
"""



class FeatureLineStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: FeatureLineStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class GradingCriteria(StyleBase):
    # no doc
    def CopyAsSibling(self, criteriaName):
        """ CopyAsSibling(self: GradingCriteria, criteriaName: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    CutSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutSlope(self: GradingCriteria) -> PropertyDouble

"""

    CutSlopeFormatType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutSlopeFormatType(self: GradingCriteria) -> PropertyEnum[GradingSlopeFormatType]

"""

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: GradingCriteria) -> PropertyDouble

"""

    DistanceProjectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceProjectionType(self: GradingCriteria) -> GradingDistanceProjectionType

Set: DistanceProjectionType(self: GradingCriteria) = value
"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: GradingCriteria) -> PropertyDouble

"""

    ElevationProjectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationProjectionType(self: GradingCriteria) -> GradingElevationProjectionType

Set: ElevationProjectionType(self: GradingCriteria) = value
"""

    FillSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillSlope(self: GradingCriteria) -> PropertyDouble

"""

    FillSlopeFormatType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillSlopeFormatType(self: GradingCriteria) -> PropertyEnum[GradingSlopeFormatType]

"""

    InteriorCornerOverlap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InteriorCornerOverlap(self: GradingCriteria) -> PropertyEnum[GradingInteriorCornerOverlapSolutionType]

"""

    ProjectionDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionDistance(self: GradingCriteria) -> PropertyDouble

"""

    ProjectionRelativeElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionRelativeElevation(self: GradingCriteria) -> PropertyDouble

"""

    RelativeElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeElevation(self: GradingCriteria) -> PropertyDouble

"""

    RelativeElevationProjectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RelativeElevationProjectionType(self: GradingCriteria) -> GradingRelativeElevationProjectionType

Set: RelativeElevationProjectionType(self: GradingCriteria) = value
"""

    SearchOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SearchOrder(self: GradingCriteria) -> PropertyEnum[GradingSearchOrderType]

"""

    Slope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Slope(self: GradingCriteria) -> PropertyDouble

"""

    SlopeFormatType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeFormatType(self: GradingCriteria) -> PropertyEnum[GradingSlopeFormatType]

"""

    SurfaceProjectionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceProjectionType(self: GradingCriteria) -> GradingSurfaceProjectionType

Set: SurfaceProjectionType(self: GradingCriteria) = value
"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: GradingCriteria) -> GradingTargetType

Set: Target(self: GradingCriteria) = value
"""



class GradingCriteriaSet(StyleBase):
    # no doc
    def AddCriteria(self, criteriaName):
        """ AddCriteria(self: GradingCriteriaSet, criteriaName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GradingCriteriaIds(self):
        """ GradingCriteriaIds(self: GradingCriteriaSet) -> ObjectIdCollection """
        pass

    def MoveCriteria(self, *__args):
        """ MoveCriteria(self: GradingCriteriaSet, criteriaId: ObjectId, criteriaSetId: ObjectId)MoveCriteria(self: GradingCriteriaSet, criteriaName: str, criteriaSetName: str) """
        pass

    def RemoveCriteria(self, *__args):
        """ RemoveCriteria(self: GradingCriteriaSet, criteriaName: str)RemoveCriteria(self: GradingCriteriaSet, index: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GradingCriteriaSet) -> int

"""



class GradingCriteriaSetCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: GradingCriteriaSetCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class GradingDisplayStyleType(Enum):
    """ enum GradingDisplayStyleType, values: CentroidMarker (0), InternalEdges (3), Projection (2), SlopePat (5), SolidShading (4), TargetLine (1) """
    CentroidMarker = None
    InternalEdges = None
    Projection = None
    SlopePat = None
    SolidShading = None
    TargetLine = None
    value__ = None


class GradingStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: GradingStyle, type: GradingDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: GradingStyle, type: GradingDisplayStyleType) -> DisplayStyle """
        pass

    CenterMarker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterMarker(self: GradingStyle) -> CenterMarkerSizeType

Set: CenterMarker(self: GradingStyle) = value
"""

    FixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FixedSize(self: GradingStyle) -> float

Set: FixedSize(self: GradingStyle) = value
"""

    PercentageOfScreen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentageOfScreen(self: GradingStyle) -> float

Set: PercentageOfScreen(self: GradingStyle) = value
"""

    PlottedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlottedSize(self: GradingStyle) -> float

Set: PlottedSize(self: GradingStyle) = value
"""

    SlopePatternStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopePatternStyleId(self: GradingStyle) -> ObjectId

Set: SlopePatternStyleId(self: GradingStyle) = value
"""

    SlopePatternStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopePatternStyleName(self: GradingStyle) -> str

Set: SlopePatternStyleName(self: GradingStyle) = value
"""

    SlopeRangeMax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeRangeMax(self: GradingStyle) -> float

Set: SlopeRangeMax(self: GradingStyle) = value
"""

    SlopeRangeMin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeRangeMin(self: GradingStyle) -> float

Set: SlopeRangeMin(self: GradingStyle) = value
"""

    UseSlopePatternStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSlopePatternStyle(self: GradingStyle) -> bool

"""

    UseSlopeRange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSlopeRange(self: GradingStyle) -> bool

Set: UseSlopeRange(self: GradingStyle) = value
"""



class GradingStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: GradingStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetCenterMarkerVisable(self, isVisable):
        """ SetCenterMarkerVisable(self: GradingStyleCollection, isVisable: bool) """
        pass

    def SetSlopePatternVisable(self, isVisable):
        """ SetSlopePatternVisable(self: GradingStyleCollection, isVisable: bool) """
        pass


class GraphDirectionType(Enum):
    """ enum GraphDirectionType, values: LeftToRight (0), RightToLeft (1) """
    LeftToRight = None
    RightToLeft = None
    value__ = None


class GraphStyle(CivilWrapper<AeccDbGraphStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyle>, A_0: bool) """
        pass

    CurrentHorizontalScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentHorizontalScale(self: GraphStyle) -> float

"""

    Direction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Direction(self: GraphStyle) -> GraphDirectionType

Set: Direction(self: GraphStyle) = value
"""

    TitleStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleStyle(self: GraphStyle) -> GraphTitleStyle

"""

    VerticalExaggeration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalExaggeration(self: GraphStyle) -> float

Set: VerticalExaggeration(self: GraphStyle) = value
"""

    VerticalScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalScale(self: GraphStyle) -> float

Set: VerticalScale(self: GraphStyle) = value
"""



class GraphTitleJustificationType(Enum):
    """ enum GraphTitleJustificationType, values: BottomOrRight (2), MiddleOrCenter (1), TopOrLeft (0) """
    BottomOrRight = None
    MiddleOrCenter = None
    TopOrLeft = None
    value__ = None


class GraphTitleLocationType(Enum):
    """ enum GraphTitleLocationType, values: Bottom (1), Left (2), Right (3), Top (0) """
    Bottom = None
    Left = None
    Right = None
    Top = None
    value__ = None


class GraphTitleStyle(CivilWrapper<AeccDbGraphStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyle>, A_0: bool) """
        pass

    Border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Border(self: GraphTitleStyle) -> bool

Set: Border(self: GraphTitleStyle) = value
"""

    BorderGap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BorderGap(self: GraphTitleStyle) -> float

Set: BorderGap(self: GraphTitleStyle) = value
"""

    Justification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Justification(self: GraphTitleStyle) -> GraphTitleJustificationType

Set: Justification(self: GraphTitleStyle) = value
"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: GraphTitleStyle) -> GraphTitleLocationType

Set: Location(self: GraphTitleStyle) = value
"""

    OffsetX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetX(self: GraphTitleStyle) -> float

Set: OffsetX(self: GraphTitleStyle) = value
"""

    OffsetY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetY(self: GraphTitleStyle) -> float

Set: OffsetY(self: GraphTitleStyle) = value
"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: GraphTitleStyle) -> str

Set: Text(self: GraphTitleStyle) = value
"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: GraphTitleStyle) -> float

Set: TextHeight(self: GraphTitleStyle) = value
"""

    TextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextStyle(self: GraphTitleStyle) -> str

Set: TextStyle(self: GraphTitleStyle) = value
"""



class GridOptions(CivilWrapper<AeccDbGraphStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyle>, A_0: bool) """
        pass

    ClipToHighestProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClipToHighestProfile(self: GridOptions) -> bool

Set: ClipToHighestProfile(self: GridOptions) = value
"""

    OmitGridInPaddingAreas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OmitGridInPaddingAreas(self: GridOptions) -> bool

Set: OmitGridInPaddingAreas(self: GridOptions) = value
"""

    UseClipGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseClipGrid(self: GridOptions) -> bool

Set: UseClipGrid(self: GridOptions) = value
"""



class GridStyle(CivilWrapper<AeccDbGraphStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbGraphStyle>, A_0: bool) """
        pass

    AxisOffsetAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisOffsetAbove(self: GridStyle) -> float

Set: AxisOffsetAbove(self: GridStyle) = value
"""

    AxisOffsetBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisOffsetBottom(self: GridStyle) -> float

Set: AxisOffsetBottom(self: GridStyle) = value
"""

    AxisOffsetLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisOffsetLeft(self: GridStyle) -> float

Set: AxisOffsetLeft(self: GridStyle) = value
"""

    AxisOffsetRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisOffsetRight(self: GridStyle) -> float

Set: AxisOffsetRight(self: GridStyle) = value
"""

    GridPaddingAbove = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridPaddingAbove(self: GridStyle) -> float

Set: GridPaddingAbove(self: GridStyle) = value
"""

    GridPaddingBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridPaddingBottom(self: GridStyle) -> float

Set: GridPaddingBottom(self: GridStyle) = value
"""

    GridPaddingLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridPaddingLeft(self: GridStyle) -> float

Set: GridPaddingLeft(self: GridStyle) = value
"""

    GridPaddingRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridPaddingRight(self: GridStyle) -> float

Set: GridPaddingRight(self: GridStyle) = value
"""

    HorizontalGridOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HorizontalGridOptions(self: GridStyle) -> GridOptions

"""

    VerticalGridOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalGridOptions(self: GridStyle) -> GridOptions

"""



class GridType(Enum):
    """ enum GridType, values: Horizontal (1), Vertical (0) """
    Horizontal = None
    value__ = None
    Vertical = None


class GroupPlotAlignType(Enum):
    """ enum GroupPlotAlignType, values: Centerline (1), Left (0), Right (2) """
    Centerline = None
    Left = None
    Right = None
    value__ = None


class GroupPlotCellSizeType(Enum):
    """ enum GroupPlotCellSizeType, values: UniformForAll (0), UniformPerRowOrColumn (1) """
    UniformForAll = None
    UniformPerRowOrColumn = None
    value__ = None


class GroupPlotDisplayStyleType(Enum):
    """ enum GroupPlotDisplayStyleType, values: Border (5), MajorHorizontalGrid (0), MajorVerticalGrid (2), MinorHorizontalGrid (1), MinorVerticalGrid (3), PrintArea (4) """
    Border = None
    MajorHorizontalGrid = None
    MajorVerticalGrid = None
    MinorHorizontalGrid = None
    MinorVerticalGrid = None
    PrintArea = None
    value__ = None


class GroupPlotStartCornerType(Enum):
    """ enum GroupPlotStartCornerType, values: LowerLeft (0), LowerRight (2), UpperLeft (1), UpperRight (3) """
    LowerLeft = None
    LowerRight = None
    UpperLeft = None
    UpperRight = None
    value__ = None


class GroupPlotStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayPlan(self, type):
        """ GetDisplayPlan(self: GroupPlotStyle, type: GroupPlotDisplayStyleType) -> DisplayStyle """
        pass

    AlignType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignType(self: GroupPlotStyle) -> GroupPlotAlignType

Set: AlignType(self: GroupPlotStyle) = value
"""

    CellSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CellSizeType(self: GroupPlotStyle) -> GroupPlotCellSizeType

Set: CellSizeType(self: GroupPlotStyle) = value
"""

    GapBetweenPages = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GapBetweenPages(self: GroupPlotStyle) -> float

Set: GapBetweenPages(self: GroupPlotStyle) = value
"""

    GridHorizontalMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridHorizontalMajor(self: GroupPlotStyle) -> float

Set: GridHorizontalMajor(self: GroupPlotStyle) = value
"""

    GridHorizontalMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridHorizontalMinor(self: GroupPlotStyle) -> float

Set: GridHorizontalMinor(self: GroupPlotStyle) = value
"""

    GridVerticalMajor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridVerticalMajor(self: GroupPlotStyle) -> float

Set: GridVerticalMajor(self: GroupPlotStyle) = value
"""

    GridVerticalMinor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridVerticalMinor(self: GroupPlotStyle) -> float

Set: GridVerticalMinor(self: GroupPlotStyle) = value
"""

    MaximumInColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumInColumn(self: GroupPlotStyle) -> int

Set: MaximumInColumn(self: GroupPlotStyle) = value
"""

    MaximumInRow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumInRow(self: GroupPlotStyle) -> int

Set: MaximumInRow(self: GroupPlotStyle) = value
"""

    PlotRule = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotRule(self: GroupPlotStyle) -> SectionViewPlotRuleType

Set: PlotRule(self: GroupPlotStyle) = value
"""

    SpaceColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpaceColumn(self: GroupPlotStyle) -> float

Set: SpaceColumn(self: GroupPlotStyle) = value
"""

    SpaceRow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpaceRow(self: GroupPlotStyle) -> float

Set: SpaceRow(self: GroupPlotStyle) = value
"""

    StartCorner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCorner(self: GroupPlotStyle) -> GroupPlotStartCornerType

Set: StartCorner(self: GroupPlotStyle) = value
"""



class GroupPlotStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: GroupPlotStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class HatchDisplayStyle(CivilWrapper<AeccDbStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStyle>, A_0: bool) """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: HatchDisplayStyle) -> float

Set: Angle(self: HatchDisplayStyle) = value
"""

    HatchType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchType(self: HatchDisplayStyle) -> HatchType

Set: HatchType(self: HatchDisplayStyle) = value
"""

    IsDoubleHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDoubleHatch(self: HatchDisplayStyle) -> bool

Set: IsDoubleHatch(self: HatchDisplayStyle) = value
"""

    Pattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pattern(self: HatchDisplayStyle) -> str

Set: Pattern(self: HatchDisplayStyle) = value
"""

    ScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleFactor(self: HatchDisplayStyle) -> float

Set: ScaleFactor(self: HatchDisplayStyle) = value
"""

    Spacing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Spacing(self: HatchDisplayStyle) -> float

Set: Spacing(self: HatchDisplayStyle) = value
"""

    UOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UOffset(self: HatchDisplayStyle) -> float

Set: UOffset(self: HatchDisplayStyle) = value
"""

    UseAngleOfObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseAngleOfObject(self: HatchDisplayStyle) -> bool

Set: UseAngleOfObject(self: HatchDisplayStyle) = value
"""

    VOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VOffset(self: HatchDisplayStyle) -> float

Set: VOffset(self: HatchDisplayStyle) = value
"""



class HatchType(Enum):
    """ enum HatchType, values: CustomDefined (2), PreDefined (1), SolidFill (3), UserDefined (0) """
    CustomDefined = None
    PreDefined = None
    SolidFill = None
    UserDefined = None
    value__ = None


class HorizontalGeometryBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: HorizontalGeometryBandStyle, type: HorizontalGeometryDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: HorizontalGeometryBandStyle) -> BandType

"""

    CurveLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveLabelStyleId(self: HorizontalGeometryBandStyle) -> ObjectId

"""

    CurveTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveTickStyle(self: HorizontalGeometryBandStyle) -> BandTickStyle

"""

    PointOfIntersectionLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointOfIntersectionLabelStyleId(self: HorizontalGeometryBandStyle) -> ObjectId

"""

    PointOfIntersectionTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointOfIntersectionTickStyle(self: HorizontalGeometryBandStyle) -> BandTickStyle

"""

    SchematicLineType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SchematicLineType(self: HorizontalGeometryBandStyle) -> SchematicLineOption

Set: SchematicLineType(self: HorizontalGeometryBandStyle) = value
"""

    SpiralLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralLabelStyleId(self: HorizontalGeometryBandStyle) -> ObjectId

"""

    SpiralTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralTickStyle(self: HorizontalGeometryBandStyle) -> BandTickStyle

"""

    TangentLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentLabelStyleId(self: HorizontalGeometryBandStyle) -> ObjectId

"""

    TangentTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentTickStyle(self: HorizontalGeometryBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: HorizontalGeometryBandStyle) -> ObjectId

"""



class HorizontalGeometryDisplayStyleType(Enum):
    """ enum HorizontalGeometryDisplayStyleType, values: Border (0), CurveGeometry (8), CurveLabels (5), PILabels (14), SpiralGeometry (9), SpiralLabels (6), TangentGeometry (7), TangentLabels (4), Ticks (3), TicksAtPI (13), TitleBox (1), TitleBoxText (2) """
    Border = None
    CurveGeometry = None
    CurveLabels = None
    PILabels = None
    SpiralGeometry = None
    SpiralLabels = None
    TangentGeometry = None
    TangentLabels = None
    Ticks = None
    TicksAtPI = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class InterferenceDisplayStyleType(Enum):
    """ enum InterferenceDisplayStyleType, values: Solid (1), Symbol (0) """
    Solid = None
    Symbol = None
    value__ = None


class InterferenceModelSizeOptionType(Enum):
    """ enum InterferenceModelSizeOptionType, values: UseAbsoluteUnits (0), UseDrawingUnits (1) """
    UseAbsoluteUnits = None
    UseDrawingUnits = None
    value__ = None


class InterferenceModelSizeType(Enum):
    """ enum InterferenceModelSizeType, values: SolidExtents (0), UserSpecified (1) """
    SolidExtents = None
    UserSpecified = None
    value__ = None


class InterferenceModelType(Enum):
    """ enum InterferenceModelType, values: Sphere (1), TrueSolid (0) """
    Sphere = None
    TrueSolid = None
    value__ = None


class InterferenceStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, component):
        """ GetDisplayStyleModel(self: InterferenceStyle, component: InterferenceDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, component):
        """ GetDisplayStylePlan(self: InterferenceStyle, component: InterferenceDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, component):
        """ GetDisplayStyleSection(self: InterferenceStyle, component: InterferenceDisplayStyleType) -> DisplayStyle """
        pass

    AbsoluteModelSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AbsoluteModelSize(self: InterferenceStyle) -> float

Set: AbsoluteModelSize(self: InterferenceStyle) = value
"""

    DrawingScaleModelSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawingScaleModelSize(self: InterferenceStyle) -> float

Set: DrawingScaleModelSize(self: InterferenceStyle) = value
"""

    MarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyle(self: InterferenceStyle) -> ObjectId

Set: MarkerStyle(self: InterferenceStyle) = value
"""

    ModelOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelOptions(self: InterferenceStyle) -> InterferenceModelType

Set: ModelOptions(self: InterferenceStyle) = value
"""

    ModelSizeOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelSizeOptions(self: InterferenceStyle) -> InterferenceModelSizeOptionType

Set: ModelSizeOptions(self: InterferenceStyle) = value
"""

    ModelSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelSizeType(self: InterferenceStyle) -> InterferenceModelSizeType

Set: ModelSizeType(self: InterferenceStyle) = value
"""



class InterferenceStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: InterferenceStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class IntersectionStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self):
        """ GetDisplayStyleModel(self: IntersectionStyle) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self):
        """ GetDisplayStylePlan(self: IntersectionStyle) -> DisplayStyle """
        pass

    MarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyleId(self: IntersectionStyle) -> ObjectId

"""



class IntersectionStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: IntersectionStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class LabelDisplayModeType(Enum):
    """ enum LabelDisplayModeType, values: Label (0), Tag (1) """
    Label = None
    Tag = None
    value__ = None


class LabelSetStylesRoot(TreeOidWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AlignmentLabelSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentLabelSetStyles(self: LabelSetStylesRoot) -> AlignmentLabelSetStyleCollection

"""

    ProfileLabelSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileLabelSetStyles(self: LabelSetStylesRoot) -> ProfileLabelSetStyleCollection

"""

    SectionLabelSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionLabelSetStyles(self: LabelSetStylesRoot) -> SectionLabelSetStyleCollection

"""



class LabelStyle(StyleBase):
    # no doc
    def AddChild(self, labelStyleName):
        """ AddChild(self: LabelStyle, labelStyleName: str) -> ObjectId """
        pass

    def AddComponent(self, name, type):
        """ AddComponent(self: LabelStyle, name: str, type: LabelStyleComponentType) -> ObjectId """
        pass

    def AddReferenceTextComponent(self, name, selectedType):
        """ AddReferenceTextComponent(self: LabelStyle, name: str, selectedType: ReferenceTextComponentSelectedType) -> ObjectId """
        pass

    def AddTextForEachComponent(self, name, selectedType):
        """ AddTextForEachComponent(self: LabelStyle, name: str, selectedType: TextForEachComponentSelectedType) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetComponents(self, type):
        """ GetComponents(self: LabelStyle, type: LabelStyleComponentType) -> ObjectIdCollection """
        pass

    def GetComponentsCount(self, type=None):
        """
        GetComponentsCount(self: LabelStyle, type: LabelStyleComponentType) -> int
        GetComponentsCount(self: LabelStyle) -> int
        """
        pass

    def GetComponentsDrawOrder(self):
        """ GetComponentsDrawOrder(self: LabelStyle) -> Array[ObjectId] """
        pass

    def IsSupportedComponent(self, type):
        """ IsSupportedComponent(self: LabelStyle, type: LabelStyleComponentType) -> bool """
        pass

    def RemoveAllDescendants(self):
        """ RemoveAllDescendants(self: LabelStyle) """
        pass

    def RemoveChild(self, *__args):
        """ RemoveChild(self: LabelStyle, labelStyleName: str)RemoveChild(self: LabelStyle, index: int) """
        pass

    def RemoveComponent(self, name):
        """ RemoveComponent(self: LabelStyle, name: str) """
        pass

    def SetComponentsDrawOrder(self, componentIds):
        """ SetComponentsDrawOrder(self: LabelStyle, componentIds: Array[ObjectId]) """
        pass

    def SwitchComponentsDrawOrder(self, index1, index2):
        """ SwitchComponentsDrawOrder(self: LabelStyle, index1: int, index2: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    ChildrenCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChildrenCount(self: LabelStyle) -> int

"""

    ParentLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParentLabelStyleId(self: LabelStyle) -> ObjectId

"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: LabelStyle) -> LabelStyleBase

"""



class LabelStyleBase(CivilWrapper<AeccDbLabelStyleCollector>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbLabelStyleCollector>, A_0: bool) """
        pass

    Behavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Behavior(self: LabelStyleBase) -> BaseBehavior

"""

    DraggedStateComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DraggedStateComponents(self: LabelStyleBase) -> BaseDraggedStateComponents

"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: LabelStyleBase) -> BaseLabel

"""

    Leader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Leader(self: LabelStyleBase) -> BaseLeader

"""

    PlanReadability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanReadability(self: LabelStyleBase) -> BasePlanReadability

"""


    BaseBehavior = None
    BaseDraggedStateComponents = None
    BaseLabel = None
    BaseLeader = None
    BasePlanReadability = None


class LabelStyleComponent(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class LabelStyleBlockComponent(LabelStyleComponent):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Block = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Block(self: LabelStyleBlockComponent) -> StyleBlock

"""

    General = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: General(self: LabelStyleBlockComponent) -> StyleGeneral

"""


    StyleBlock = None
    StyleGeneral = None


class LabelStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: LabelStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetClassNodeId(self, *args): #cannot find CLR method
        """ GetClassNodeId(self: LabelStyleCollection, : AcDbObjectId*, type: int) -> AcDbObjectId* """
        pass

    def Remove(self, *__args):
        """ Remove(self: LabelStyleCollection, index: int)Remove(self: LabelStyleCollection, styleName: str) """
        pass

    DefaultLabelStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultLabelStyle(self: LabelStyleCollection) -> LabelStyleDefault

"""

    Expressions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Expressions(self: LabelStyleCollection) -> ExpressionCollection

"""



class LabelStyleComponentType(Enum):
    """ enum LabelStyleComponentType, values: Block (4), DirectionArrow (32), Line (2), ReferenceText (16), Text (1), TextForEach (64), Tick (8) """
    Block = None
    DirectionArrow = None
    Line = None
    ReferenceText = None
    Text = None
    TextForEach = None
    Tick = None
    value__ = None


class LabelStyleDefault(TreeOidWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    Behavior = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Behavior(self: LabelStyleDefault) -> DefaultBehavior

"""

    Components = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Components(self: LabelStyleDefault) -> DefaultComponents

"""

    DraggedStateComponents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DraggedStateComponents(self: LabelStyleDefault) -> DefaultDraggedStateComponents

"""

    Label = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Label(self: LabelStyleDefault) -> DefaultLabel

"""

    Leader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Leader(self: LabelStyleDefault) -> DefaultLeader

"""

    PlanReadability = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanReadability(self: LabelStyleDefault) -> DefaultPlanReadability

"""


    DefaultBehavior = None
    DefaultComponents = None
    DefaultDraggedStateComponents = None
    DefaultLabel = None
    DefaultLeader = None
    DefaultPlanReadability = None


class LabelStyleDirectionArrowComponent(LabelStyleComponent):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    DirectionArrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionArrow(self: LabelStyleDirectionArrowComponent) -> StyleDirectionArrow

"""

    General = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: General(self: LabelStyleDirectionArrowComponent) -> StyleGeneral

"""


    StyleDirectionArrow = None
    StyleGeneral = None


class LabelStyleLineComponent(LabelStyleComponent):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    General = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: General(self: LabelStyleLineComponent) -> StyleGeneral

"""

    Line = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Line(self: LabelStyleLineComponent) -> StyleLine

"""


    StyleGeneral = None
    StyleLine = None


class LabelStyleReferenceTextComponent(LabelStyleComponent):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Border(self: LabelStyleReferenceTextComponent) -> StyleBorder

"""

    General = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: General(self: LabelStyleReferenceTextComponent) -> StyleGeneral

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: LabelStyleReferenceTextComponent) -> StyleText

"""


    StyleBorder = None
    StyleGeneral = None
    StyleText = None


class LabelStylesNode(TreeOidWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    DefaultLabelStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultLabelStyle(self: LabelStylesNode) -> LabelStyleDefault

"""



class LabelStylesAlignmentRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CantCriticalPointsLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CantCriticalPointsLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    CurveLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    DesignSpeedLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DesignSpeedLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    GeometryPointLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryPointLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    LineLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    MajorStationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorStationLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    MinorStationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorStationLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    PointOfIntersectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointOfIntersectionLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    SpiralLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpiralLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    StationEquationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationEquationLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    StationOffsetLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationOffsetLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    SuperelevationCriticalPointsLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperelevationCriticalPointsLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    TangentIntersectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TangentIntersectionLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""

    VerticalGeometryPointLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalGeometryPointLabelStyles(self: LabelStylesAlignmentRoot) -> LabelStyleCollection

"""



class LabelStylesCatchmentRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AreaLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaLabelStyles(self: LabelStylesCatchmentRoot) -> LabelStyleCollection

"""

    FlowSegmentLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlowSegmentLabelStyles(self: LabelStylesCatchmentRoot) -> LabelStyleCollection

"""



class LabelStylesIntersectionRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LocationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocationLabelStyles(self: LabelStylesIntersectionRoot) -> LabelStyleCollection

"""



class LabelStylesMatchLineRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LeftLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftLabelStyles(self: LabelStylesMatchLineRoot) -> LabelStyleCollection

"""

    RightLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightLabelStyles(self: LabelStylesMatchLineRoot) -> LabelStyleCollection

"""



class LabelStylesParcelRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AreaLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaLabelStyles(self: LabelStylesParcelRoot) -> LabelStyleCollection

"""

    CurveLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveLabelStyles(self: LabelStylesParcelRoot) -> LabelStyleCollection

"""

    LineLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineLabelStyles(self: LabelStylesParcelRoot) -> LabelStyleCollection

"""



class LabelStylesPipeRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CrossProfileLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossProfileLabelStyles(self: LabelStylesPipeRoot) -> LabelStyleCollection

"""

    CrossSectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossSectionLabelStyles(self: LabelStylesPipeRoot) -> LabelStyleCollection

"""

    PlanProfileLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanProfileLabelStyles(self: LabelStylesPipeRoot) -> LabelStyleCollection

"""



class LabelStylesPointRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: LabelStylesPointRoot) -> LabelStyleCollection

"""



class LabelStylesPressureAppurtenanceRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: LabelStylesPressureAppurtenanceRoot) -> LabelStyleCollection

"""



class LabelStylesPressureFittingRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: LabelStylesPressureFittingRoot) -> LabelStyleCollection

"""



class LabelStylesPressurePipeRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CrossingProfileLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingProfileLabelStyles(self: LabelStylesPressurePipeRoot) -> LabelStyleCollection

"""

    CrossingSectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingSectionLabelStyles(self: LabelStylesPressurePipeRoot) -> LabelStyleCollection

"""

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: LabelStylesPressurePipeRoot) -> LabelStyleCollection

"""

    PlanProfileLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanProfileLabelStyles(self: LabelStylesPressurePipeRoot) -> LabelStyleCollection

"""



class LabelStylesProfileRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CurveLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveLabelStyles(self: LabelStylesProfileRoot) -> LabelStyleCollection

"""

    GradeBreadLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeBreadLabelStyles(self: LabelStylesProfileRoot) -> LabelStyleCollection

"""

    GradeBreakLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeBreakLabelStyles(self: LabelStylesProfileRoot) -> LabelStyleCollection

"""

    HorizontalGeometryPointLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HorizontalGeometryPointLabelStyles(self: LabelStylesProfileRoot) -> LabelStyleCollection

"""

    LineLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineLabelStyles(self: LabelStylesProfileRoot) -> LabelStyleCollection

"""

    MajorStationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorStationLabelStyles(self: LabelStylesProfileRoot) -> LabelStyleCollection

"""

    MinorStationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorStationLabelStyles(self: LabelStylesProfileRoot) -> LabelStyleCollection

"""



class LabelStylesProfileViewRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    DepthLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepthLabelStyles(self: LabelStylesProfileViewRoot) -> LabelStyleCollection

"""

    StationElevationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationElevationLabelStyles(self: LabelStylesProfileViewRoot) -> LabelStyleCollection

"""



class LabelStylesProjectionRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    ProfileViewProjectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewProjectionLabelStyles(self: LabelStylesProjectionRoot) -> LabelStyleCollection

"""

    SectionViewProjectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewProjectionLabelStyles(self: LabelStylesProjectionRoot) -> LabelStyleCollection

"""



class LabelStylesRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetSurveyLabelStyles(self):
        """ GetSurveyLabelStyles(self: LabelStylesRoot) -> LabelStylesSurveyRoot """
        pass

    AlignmentLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentLabelStyles(self: LabelStylesRoot) -> LabelStylesAlignmentRoot

"""

    CatchmentLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CatchmentLabelStyles(self: LabelStylesRoot) -> LabelStylesCatchmentRoot

"""

    GeneralCurveLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralCurveLabelStyles(self: LabelStylesRoot) -> LabelStyleCollection

"""

    GeneralLineLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralLineLabelStyles(self: LabelStylesRoot) -> LabelStyleCollection

"""

    GeneralLinkLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralLinkLabelStyles(self: LabelStylesRoot) -> LabelStyleCollection

"""

    GeneralMarkerLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralMarkerLabelStyles(self: LabelStylesRoot) -> LabelStyleCollection

"""

    GeneralNoteLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralNoteLabelStyles(self: LabelStylesRoot) -> LabelStyleCollection

"""

    GeneralShapeLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeneralShapeLabelStyles(self: LabelStylesRoot) -> LabelStyleCollection

"""

    IntersectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionLabelStyles(self: LabelStylesRoot) -> LabelStylesIntersectionRoot

"""

    MatchLineLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchLineLabelStyles(self: LabelStylesRoot) -> LabelStylesMatchLineRoot

"""

    ParcelLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParcelLabelStyles(self: LabelStylesRoot) -> LabelStylesParcelRoot

"""

    PipeLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeLabelStyles(self: LabelStylesRoot) -> LabelStylesPipeRoot

"""

    PointLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointLabelStyles(self: LabelStylesRoot) -> LabelStylesPointRoot

"""

    ProfileLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileLabelStyles(self: LabelStylesRoot) -> LabelStylesProfileRoot

"""

    ProfileViewLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewLabelStyles(self: LabelStylesRoot) -> LabelStylesProfileViewRoot

"""

    ProjectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionLabelStyles(self: LabelStylesRoot) -> LabelStylesProjectionRoot

"""

    SampleLineLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineLabelStyles(self: LabelStylesRoot) -> LabelStylesSampleLineRoot

"""

    SectionLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionLabelStyles(self: LabelStylesRoot) -> LabelStylesSectionRoot

"""

    SectionViewLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewLabelStyles(self: LabelStylesRoot) -> LabelStylesSectionViewRoot

"""

    StructureLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureLabelStyles(self: LabelStylesRoot) -> LabelStylesStructureRoot

"""

    SurfaceLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceLabelStyles(self: LabelStylesRoot) -> LabelStylesSurfaceRoot

"""

    ViewFrameLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewFrameLabelStyles(self: LabelStylesRoot) -> LabelStylesViewFrameRoot

"""



class LabelStylesRootPressurePipesExtension(object):
    # no doc
    @staticmethod
    def GetPressureAppurtenanceLabelStyles(stylesRoot):
        """ GetPressureAppurtenanceLabelStyles(stylesRoot: LabelStylesRoot) -> LabelStylesPressureAppurtenanceRoot """
        pass

    @staticmethod
    def GetPressureFittingLabelStyles(stylesRoot):
        """ GetPressureFittingLabelStyles(stylesRoot: LabelStylesRoot) -> LabelStylesPressureFittingRoot """
        pass

    @staticmethod
    def GetPressurePipeLabelStyles(stylesRoot):
        """ GetPressurePipeLabelStyles(stylesRoot: LabelStylesRoot) -> LabelStylesPressurePipeRoot """
        pass

    __all__ = [
        'GetPressureAppurtenanceLabelStyles',
        'GetPressureFittingLabelStyles',
        'GetPressurePipeLabelStyles',
    ]


class LabelStylesSampleLineRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: LabelStylesSampleLineRoot) -> LabelStyleCollection

"""



class LabelStylesSectionRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    GradeBreakLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeBreakLabelStyles(self: LabelStylesSectionRoot) -> LabelStyleCollection

"""

    MajorOffsetLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorOffsetLabelStyles(self: LabelStylesSectionRoot) -> LabelStyleCollection

"""

    MinorOffsetLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorOffsetLabelStyles(self: LabelStylesSectionRoot) -> LabelStyleCollection

"""

    SegmentLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLabelStyles(self: LabelStylesSectionRoot) -> LabelStyleCollection

"""



class LabelStylesSectionViewRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    GradeLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeLabelStyles(self: LabelStylesSectionViewRoot) -> LabelStyleCollection

"""

    OffsetElevationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetElevationLabelStyles(self: LabelStylesSectionViewRoot) -> LabelStyleCollection

"""



class LabelStylesStructureRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: LabelStylesStructureRoot) -> LabelStyleCollection

"""



class LabelStylesSurfaceRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    ContourLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContourLabelStyles(self: LabelStylesSurfaceRoot) -> LabelStyleCollection

"""

    SlopeLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeLabelStyles(self: LabelStylesSurfaceRoot) -> LabelStyleCollection

"""

    SpotElevationLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpotElevationLabelStyles(self: LabelStylesSurfaceRoot) -> LabelStyleCollection

"""

    WatershedLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WatershedLabelStyles(self: LabelStylesSurfaceRoot) -> LabelStyleCollection

"""



class LabelStylesSurveyRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    CurveLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurveLabelStyles(self: LabelStylesSurveyRoot) -> LabelStyleCollection

"""

    FigureLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FigureLabelStyles(self: LabelStylesSurveyRoot) -> LabelStyleCollection

"""

    LineLabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineLabelStyles(self: LabelStylesSurveyRoot) -> LabelStyleCollection

"""



class LabelStylesViewFrameRoot(LabelStylesNode):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: LabelStylesViewFrameRoot) -> LabelStyleCollection

"""



class LabelStyleTextComponent(LabelStyleComponent):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Border(self: LabelStyleTextComponent) -> StyleBorder

"""

    General = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: General(self: LabelStyleTextComponent) -> StyleGeneral

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: LabelStyleTextComponent) -> StyleText

"""


    StyleBorder = None
    StyleGeneral = None
    StyleText = None


class LabelStyleTextForEachComponent(LabelStyleComponent):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    Border = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Border(self: LabelStyleTextForEachComponent) -> StyleBorder

"""

    General = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: General(self: LabelStyleTextForEachComponent) -> StyleGeneral

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: LabelStyleTextForEachComponent) -> StyleText

"""


    StyleBorder = None
    StyleGeneral = None
    StyleText = None


class LabelStyleTickComponent(LabelStyleComponent):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    General = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: General(self: LabelStyleTickComponent) -> StyleGeneral

"""

    Tick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tick(self: LabelStyleTickComponent) -> StyleTick

"""


    StyleGeneral = None
    StyleTick = None


class LabelStyleType(Enum):
    """ enum LabelStyleType, values: AlignmentCurve (251704330), AlignmentDesignSpeed (251704325), AlignmentGeometryPoint (251704323), AlignmentLine (251704328), AlignmentMajorStation (251704321), AlignmentMinorStation (251704322), AlignmentPointOfIntersection (251704833), AlignmentProfileGeometryPoint (251704832), AlignmentSpiral (251704329), AlignmentStationEquation (251704324), AlignmentStationOffset (251704326), AlignmentSuperelevationCriticalPoints (251704331), AlignmentTangentIntersection (251704327), Appurtenance (251704727), CatchmentArea (251704720), CatchmentFlowSegment (251704721), Fitting (251704726), GeneralCurve (251704376), GeneralLine (251704375), GeneralLink (251704406), GeneralMarker (251704407), GeneralNote (251704374), GeneralShape (251704408), IntersectionLocationLabels (251704697), MatchLineLeft (251704608), MatchLineRight (251704609), ParcelArea (251704370), ParcelCurve (251704372), ParcelLine (251704371), PipeCrossSection (251704412), PipePlanProfile (251704379), Point (268481548), PressurePipe (251704725), ProfileBandHGP (268546592), ProfileBandHorizontalGeometryCurve (268547088), ProfileBandHorizontalGeometryPointOfIntersection (268547120), ProfileBandHorizontalGeometrySpiral (268547104), ProfileBandHorizontalGeometryTangent (268547072), ProfileBandIncrementalDistance (268546640), ProfileBandMajorIncrement (268546560), ProfileBandMinorIncrement (268546576), ProfileBandPipeNetworkPipeLocation (268547648), ProfileBandPipeNetworkStructureLocation (268547632), ProfileBandSectionalDataIncrementalSectionData (268547680), ProfileBandSectionalDataSampleLineLocation (268547664), ProfileBandStationEquation (268546624), ProfileBandSuperelevationDataFullSuper (268547376), ProfileBandSuperelevationDataLevelCrown (268547392), ProfileBandSuperelevationDataNormalCrown (268547328), ProfileBandSuperelevationDataReverseCrown (268547360), ProfileBandSuperelevationDataShoulderCritical (268547616), ProfileBandSuperelevationDataSlopeTransition (268547408), ProfileBandVerticalGeometryCrestCurve (268546848), ProfileBandVerticalGeometryDownhillTangent (268546832), ProfileBandVerticalGeometrySagCurve (268546864), ProfileBandVerticalGeometryUphillTangent (268546816), ProfileBandVGP (268546608), ProfileCrestCurve (251704342), ProfileCurve (251704339), ProfileGradeBreaks (251704340), ProfileHorizontalGeometryPoint (251704335), ProfileLine (251704338), ProfileMajorStation (251704333), ProfileMinorStation (251704334), ProfileSagCurve (251704341), ProfileViewDepth (251704347), ProfileViewProjection (251704694), ProfileViewStationElevation (251704346), SampleLineLabelStyles (268607503), SectionBandCenterline (268562976), SectionBandGradeBreaks (268563008), SectionBandIncrementalDistance (268563024), SectionBandMajorIncrement (268562944), SectionBandMinorIncrement (268562960), SectionBandSampleLineVertices (268562992), SectionBandSegmentSurfaceLabels (268563200), SectionGradeBreak (251704401), SectionMajorOffset (251704399), SectionMinorOffset (251704400), SectionSegment (251704402), SectionViewGrade (251704404), SectionViewOffsetElevation (251704403), SectionViewProjection (251704695), StructureLabelStyle (251704380), SurfaceContour (251704366), SurfaceSlope (251704367), SurfaceSpotElevation (251704369), SurfaceWatershed (251704397), ViewFrame (251704607) """
    AlignmentCurve = None
    AlignmentDesignSpeed = None
    AlignmentGeometryPoint = None
    AlignmentLine = None
    AlignmentMajorStation = None
    AlignmentMinorStation = None
    AlignmentPointOfIntersection = None
    AlignmentProfileGeometryPoint = None
    AlignmentSpiral = None
    AlignmentStationEquation = None
    AlignmentStationOffset = None
    AlignmentSuperelevationCriticalPoints = None
    AlignmentTangentIntersection = None
    Appurtenance = None
    CatchmentArea = None
    CatchmentFlowSegment = None
    Fitting = None
    GeneralCurve = None
    GeneralLine = None
    GeneralLink = None
    GeneralMarker = None
    GeneralNote = None
    GeneralShape = None
    IntersectionLocationLabels = None
    MatchLineLeft = None
    MatchLineRight = None
    ParcelArea = None
    ParcelCurve = None
    ParcelLine = None
    PipeCrossSection = None
    PipePlanProfile = None
    Point = None
    PressurePipe = None
    ProfileBandHGP = None
    ProfileBandHorizontalGeometryCurve = None
    ProfileBandHorizontalGeometryPointOfIntersection = None
    ProfileBandHorizontalGeometrySpiral = None
    ProfileBandHorizontalGeometryTangent = None
    ProfileBandIncrementalDistance = None
    ProfileBandMajorIncrement = None
    ProfileBandMinorIncrement = None
    ProfileBandPipeNetworkPipeLocation = None
    ProfileBandPipeNetworkStructureLocation = None
    ProfileBandSectionalDataIncrementalSectionData = None
    ProfileBandSectionalDataSampleLineLocation = None
    ProfileBandStationEquation = None
    ProfileBandSuperelevationDataFullSuper = None
    ProfileBandSuperelevationDataLevelCrown = None
    ProfileBandSuperelevationDataNormalCrown = None
    ProfileBandSuperelevationDataReverseCrown = None
    ProfileBandSuperelevationDataShoulderCritical = None
    ProfileBandSuperelevationDataSlopeTransition = None
    ProfileBandVerticalGeometryCrestCurve = None
    ProfileBandVerticalGeometryDownhillTangent = None
    ProfileBandVerticalGeometrySagCurve = None
    ProfileBandVerticalGeometryUphillTangent = None
    ProfileBandVGP = None
    ProfileCrestCurve = None
    ProfileCurve = None
    ProfileGradeBreaks = None
    ProfileHorizontalGeometryPoint = None
    ProfileLine = None
    ProfileMajorStation = None
    ProfileMinorStation = None
    ProfileSagCurve = None
    ProfileViewDepth = None
    ProfileViewProjection = None
    ProfileViewStationElevation = None
    SampleLineLabelStyles = None
    SectionBandCenterline = None
    SectionBandGradeBreaks = None
    SectionBandIncrementalDistance = None
    SectionBandMajorIncrement = None
    SectionBandMinorIncrement = None
    SectionBandSampleLineVertices = None
    SectionBandSegmentSurfaceLabels = None
    SectionGradeBreak = None
    SectionMajorOffset = None
    SectionMinorOffset = None
    SectionSegment = None
    SectionViewGrade = None
    SectionViewOffsetElevation = None
    SectionViewProjection = None
    StructureLabelStyle = None
    SurfaceContour = None
    SurfaceSlope = None
    SurfaceSpotElevation = None
    SurfaceWatershed = None
    value__ = None
    ViewFrame = None


class SubassemblySubentityStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    StyleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleType(self: SubassemblySubentityStyle) -> SubassemblySubentityStyleType

"""



class LinkStyle(SubassemblySubentityStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self):
        """ GetDisplayStyleModel(self: LinkStyle) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self):
        """ GetDisplayStylePlan(self: LinkStyle) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self):
        """ GetDisplayStyleSection(self: LinkStyle) -> DisplayStyle """
        pass

    def GetLinkDisplayStyleModel(self):
        """ GetLinkDisplayStyleModel(self: LinkStyle) -> DisplayStyle """
        pass

    def GetLinkDisplayStylePlan(self):
        """ GetLinkDisplayStylePlan(self: LinkStyle) -> DisplayStyle """
        pass

    LinkDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkDisplayStyleModel(self: LinkStyle) -> DisplayStyle

"""

    LinkDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkDisplayStylePlan(self: LinkStyle) -> DisplayStyle

"""

    StyleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleType(self: LinkStyle) -> SubassemblySubentityStyleType

"""



class LinkStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: LinkStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class MarkerDisplayType(Enum):
    """ enum MarkerDisplayType, values: UseCustomMarker (1), UsePointForMarker (0), UseSymbolForMarker (2), UseVerticalLineForMarker (3) """
    UseCustomMarker = None
    UsePointForMarker = None
    UseSymbolForMarker = None
    UseVerticalLineForMarker = None
    value__ = None


class MarkerOrientationType(Enum):
    """ enum MarkerOrientationType, values: OrientToObject (0), OrientToView (2), OrientToWCS (1) """
    OrientToObject = None
    OrientToView = None
    OrientToWCS = None
    value__ = None


class MarkerSizeType(Enum):
    """ enum MarkerSizeType, values: AbsoluteUnits (2), DrawingScale (0), FixedScale (3), RelativeToScreen (1) """
    AbsoluteUnits = None
    DrawingScale = None
    FixedScale = None
    RelativeToScreen = None
    value__ = None


class MarkerStyleBase(StyleBase):
    """ MarkerStyleBase(unmanagedPointer: IntPtr, autoDelete: bool) """
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def getAttributeId(self, *args): #cannot find CLR method
        """ getAttributeId(self: MarkerStyleBase, ptVal: markStylePropertyType) -> UInt32 """
        pass

    def getDisplayComponentId(self, *args): #cannot find CLR method
        """ getDisplayComponentId(self: MarkerStyleBase) -> UInt32 """
        pass

    def GetMarkerDisplayStyleModel(self):
        """ GetMarkerDisplayStyleModel(self: MarkerStyleBase) -> DisplayStyle """
        pass

    def GetMarkerDisplayStylePlan(self):
        """ GetMarkerDisplayStylePlan(self: MarkerStyleBase) -> DisplayStyle """
        pass

    @staticmethod # known case of __new__
    def __new__(self, unmanagedPointer, autoDelete):
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    CustomMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomMarkerStyle(self: MarkerStyleBase) -> CustomMarkerType

Set: CustomMarkerStyle(self: MarkerStyleBase) = value
"""

    CustomMarkerSuperimposeStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CustomMarkerSuperimposeStyle(self: MarkerStyleBase) -> CustomMarkerSuperimposeType

Set: CustomMarkerSuperimposeStyle(self: MarkerStyleBase) = value
"""

    MarkerDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerDisplayStyleModel(self: MarkerStyleBase) -> DisplayStyle

"""

    MarkerDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerDisplayStylePlan(self: MarkerStyleBase) -> DisplayStyle

"""

    MarkerFixedScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerFixedScale(self: MarkerStyleBase) -> Point3d

Set: MarkerFixedScale(self: MarkerStyleBase) = value
"""

    MarkerRotationAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerRotationAngle(self: MarkerStyleBase) -> float

Set: MarkerRotationAngle(self: MarkerStyleBase) = value
"""

    MarkerSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerSize(self: MarkerStyleBase) -> float

Set: MarkerSize(self: MarkerStyleBase) = value
"""

    MarkerSymbolName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerSymbolName(self: MarkerStyleBase) -> str

Set: MarkerSymbolName(self: MarkerStyleBase) = value
"""

    Orientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Orientation(self: MarkerStyleBase) -> MarkerOrientationType

Set: Orientation(self: MarkerStyleBase) = value
"""

    SizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeType(self: MarkerStyleBase) -> MarkerSizeType

Set: SizeType(self: MarkerStyleBase) = value
"""



class MarkerStyle(MarkerStyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetMarkerDisplayStyleProfile(self):
        """ GetMarkerDisplayStyleProfile(self: MarkerStyle) -> DisplayStyle """
        pass

    def GetMarkerDisplayStyleSection(self):
        """ GetMarkerDisplayStyleSection(self: MarkerStyle) -> DisplayStyle """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    MarkerDisplayStyleProfile = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerDisplayStyleProfile(self: MarkerStyle) -> DisplayStyle

"""

    MarkerDisplayStyleSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerDisplayStyleSection(self: MarkerStyle) -> DisplayStyle

"""

    MarkerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerType(self: MarkerStyle) -> MarkerDisplayType

Set: MarkerType(self: MarkerStyle) = value
"""



class MarkerStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: MarkerStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class MassHaulLineStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleProfile(self, type):
        """ GetDisplayStyleProfile(self: MassHaulLineStyle, type: MassHaulLineDisplayStyleType) -> DisplayStyle """
        pass

    def GetHatchDisplayStyleProfile(self, type):
        """ GetHatchDisplayStyleProfile(self: MassHaulLineStyle, type: MassHaulLineHatchDisplayStyleType) -> HatchDisplayStyle """
        pass

    FreeHaulOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FreeHaulOption(self: MassHaulLineStyle) -> FreeHaulDisplayType

Set: FreeHaulOption(self: MassHaulLineStyle) = value
"""



class MassHaulLineStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: MassHaulLineStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class MassHaulViewStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: MassHaulViewStyle, type: MassHaulViewDisplayStyleType) -> DisplayStyle """
        pass

    BottomAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomAxis(self: MassHaulViewStyle) -> AxisStyle

"""

    GraphStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphStyle(self: MassHaulViewStyle) -> GraphStyle

"""

    GridStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridStyle(self: MassHaulViewStyle) -> GridStyle

"""

    LeftAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftAxis(self: MassHaulViewStyle) -> AxisStyle

"""

    MiddleAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MiddleAxis(self: MassHaulViewStyle) -> AxisStyle

"""

    RightAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightAxis(self: MassHaulViewStyle) -> AxisStyle

"""

    TopAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopAxis(self: MassHaulViewStyle) -> AxisStyle

"""



class MassHaulViewStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: MassHaulViewStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class MatchLineStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetLinesDisplayStylePlan(self):
        """ GetLinesDisplayStylePlan(self: MatchLineStyle) -> DisplayStyle """
        pass

    def GetMatchLineMaskDisplayStylePlan(self):
        """ GetMatchLineMaskDisplayStylePlan(self: MatchLineStyle) -> DisplayStyle """
        pass

    def GetMatchLineMaskHatchDisplayStyle(self):
        """ GetMatchLineMaskHatchDisplayStyle(self: MatchLineStyle) -> HatchDisplayStyle """
        pass

    LinesDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinesDisplayStylePlan(self: MatchLineStyle) -> DisplayStyle

"""

    MatchLineMaskDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchLineMaskDisplayStylePlan(self: MatchLineStyle) -> DisplayStyle

"""

    MatchLineMaskHatchDisplayStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchLineMaskHatchDisplayStyle(self: MatchLineStyle) -> HatchDisplayStyle

"""



class MatchLineStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: MatchLineStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class NetworkRuleSetStyle(StyleBase):
    # no doc
    def CloneAndAddRule(self, sourceRuleId):
        """ CloneAndAddRule(self: NetworkRuleSetStyle, sourceRuleId: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetRuleIds(self):
        """ GetRuleIds(self: NetworkRuleSetStyle) -> ObjectIdCollection """
        pass

    def RemoveAllRules(self):
        """ RemoveAllRules(self: NetworkRuleSetStyle) """
        pass

    def RemoveRule(self, ruleId):
        """ RemoveRule(self: NetworkRuleSetStyle, ruleId: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    RulesCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RulesCount(self: NetworkRuleSetStyle) -> int

"""



class ParcelDisplayStyleType(Enum):
    """ enum ParcelDisplayStyleType, values: AreaFill (1), Segments (0) """
    AreaFill = None
    Segments = None
    value__ = None


class ParcelStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAreaFillHatchDisplayStyleModel(self):
        """ GetAreaFillHatchDisplayStyleModel(self: ParcelStyle) -> HatchDisplayStyle """
        pass

    def GetAreaFillHatchDisplayStylePlan(self):
        """ GetAreaFillHatchDisplayStylePlan(self: ParcelStyle) -> HatchDisplayStyle """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: ParcelStyle, type: ParcelDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: ParcelStyle, type: ParcelDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self):
        """ GetDisplayStyleSection(self: ParcelStyle) -> DisplayStyle """
        pass

    AreaFillHatchDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaFillHatchDisplayStyleModel(self: ParcelStyle) -> HatchDisplayStyle

"""

    AreaFillHatchDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaFillHatchDisplayStylePlan(self: ParcelStyle) -> HatchDisplayStyle

"""

    NameTemplate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NameTemplate(self: ParcelStyle) -> str

Set: NameTemplate(self: ParcelStyle) = value
"""

    ObservePatternFillDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObservePatternFillDistance(self: ParcelStyle) -> bool

Set: ObservePatternFillDistance(self: ParcelStyle) = value
"""

    ParcelSegmentsMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParcelSegmentsMarkerStyle(self: ParcelStyle) -> ObjectId

Set: ParcelSegmentsMarkerStyle(self: ParcelStyle) = value
"""

    PatternFillDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternFillDistance(self: ParcelStyle) -> float

Set: PatternFillDistance(self: ParcelStyle) = value
"""



class ParcelStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ParcelStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PartDataSourceType(Enum):
    """ enum PartDataSourceType, values: BasicTable (1), Calculation (5), Constant (4), FixedList (2), Optional (6), RangeList (3), Undefined (0) """
    BasicTable = None
    Calculation = None
    Constant = None
    FixedList = None
    Optional = None
    RangeList = None
    Undefined = None
    value__ = None


class PartFamily(DBObject):
    # no doc
    def AddPartSize(self, partSizeFilter):
        """ AddPartSize(self: PartFamily, partSizeFilter: SizeFilterRecord) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def RemovePartSize(self, *__args):
        """ RemovePartSize(self: PartFamily, index: int)RemovePartSize(self: PartFamily, partSizeId: ObjectId) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    BoundingShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundingShape(self: PartFamily) -> BoundingShapeType

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PartFamily) -> str

"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Domain(self: PartFamily) -> DomainType

"""

    GUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GUID(self: PartFamily) -> str

"""

    PartSizeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartSizeCount(self: PartFamily) -> int

"""

    PartSizeFilter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartSizeFilter(self: PartFamily) -> SizeFilterRecord

"""

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartType(self: PartFamily) -> PartType

"""

    SweptShape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SweptShape(self: PartFamily) -> SweptShapeType

"""



class PartSize(DBObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    MaterialStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialStyleId(self: PartSize) -> ObjectId

Set: MaterialStyleId(self: PartSize) = value
"""

    PartStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartStyleId(self: PartSize) -> ObjectId

Set: PartStyleId(self: PartSize) = value
"""

    PayItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PayItems(self: PartSize) -> Array[str]

Set: PayItems(self: PartSize) = value
"""

    RulesStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RulesStyleId(self: PartSize) -> ObjectId

Set: RulesStyleId(self: PartSize) = value
"""

    SizeDataRecord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeDataRecord(self: PartSize) -> PartDataRecord

Set: SizeDataRecord(self: PartSize) = value
"""



class PartsList(StyleBase):
    # no doc
    def AddPartFamilyByDescription(self, domain, description):
        """ AddPartFamilyByDescription(self: PartsList, domain: DomainType, description: str) """
        pass

    def AddPartFamilyByGuid(self, domain, guid):
        """ AddPartFamilyByGuid(self: PartsList, domain: DomainType, guid: str) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailablePartFamilies(domain):
        """ GetAvailablePartFamilies(domain: DomainType) -> Array[DataPartFamily] """
        pass

    def GetPartFamilyIdsByDomain(self, domain):
        """ GetPartFamilyIdsByDomain(self: PartsList, domain: DomainType) -> ObjectIdCollection """
        pass

    def RemovePartFamily(self, *__args):
        """ RemovePartFamily(self: PartsList, description: str)RemovePartFamily(self: PartsList, partFamilyId: ObjectId) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    PartFamilyCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartFamilyCount(self: PartsList) -> int

"""



class PartsListCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PartsListCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PipeCenterlineType(Enum):
    """ enum PipeCenterlineType, values: ByLineWeight (0), SpecifyWidth (1) """
    ByLineWeight = None
    SpecifyWidth = None
    value__ = None


class PipeCenterlineWidthType(Enum):
    """ enum PipeCenterlineWidthType, values: DrawToInnerWalls (0), DrawToOuterWalls (1), UseAbsoluteUnits (3), UseDrawingScale (2), UseSizeAsPercentageOfScreen (4) """
    DrawToInnerWalls = None
    DrawToOuterWalls = None
    UseAbsoluteUnits = None
    UseDrawingScale = None
    UseSizeAsPercentageOfScreen = None
    value__ = None


class PipeDisplayStylePlanType(Enum):
    """ enum PipeDisplayStylePlanType, values: Centerline (0), EndLine (3), Hatch (4), InsideWalls (1), OutsideWalls (2), Solid (5) """
    Centerline = None
    EndLine = None
    Hatch = None
    InsideWalls = None
    OutsideWalls = None
    Solid = None
    value__ = None


class PipeDisplayStyleProfileType(Enum):
    """ enum PipeDisplayStyleProfileType, values: Centerline (0), CrossingPipeHatch (8), CrossingPipeInsideWall (6), CrossingPipeOutsideWall (7), EndLine (3), EnergyGradeLine (10), Hatch (4), HydraulicGradeLine (9), InsideWalls (1), OutsideWalls (2) """
    Centerline = None
    CrossingPipeHatch = None
    CrossingPipeInsideWall = None
    CrossingPipeOutsideWall = None
    EndLine = None
    EnergyGradeLine = None
    Hatch = None
    HydraulicGradeLine = None
    InsideWalls = None
    OutsideWalls = None
    value__ = None


class PipeDisplayStyleSectionType(Enum):
    """ enum PipeDisplayStyleSectionType, values: CrossingPipeHatch (8), CrossingPipeInsideWall (6), CrossingPipeOutsideWall (7) """
    CrossingPipeHatch = None
    CrossingPipeInsideWall = None
    CrossingPipeOutsideWall = None
    value__ = None


class PipeEndSizeType(Enum):
    """ enum PipeEndSizeType, values: DrawToInnerWall (0), DrawToOuterWall (1), UserDefinedEndSize (2) """
    DrawToInnerWall = None
    DrawToOuterWall = None
    UserDefinedEndSize = None
    value__ = None


class PipeHatchStyleProfileType(Enum):
    """ enum PipeHatchStyleProfileType, values: CrossingPipeHatch (1), Hatch (0) """
    CrossingPipeHatch = None
    Hatch = None
    value__ = None


class PipeHatchType(Enum):
    """ enum PipeHatchType, values: HatchToInnerWalls (0), HatchToOuterWalls (1), HatchWallsOnly (2) """
    HatchToInnerWalls = None
    HatchToOuterWalls = None
    HatchWallsOnly = None
    value__ = None


class PipeNetworkBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: PipeNetworkBandStyle, type: PipeNetworkDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: PipeNetworkBandStyle) -> BandType

"""

    PipeLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeLabelStyleId(self: PipeNetworkBandStyle) -> ObjectId

"""

    PipeTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeTickStyle(self: PipeNetworkBandStyle) -> BandTickStyle

"""

    StructureLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureLabelStyleId(self: PipeNetworkBandStyle) -> ObjectId

"""

    StructureTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureTickStyle(self: PipeNetworkBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: PipeNetworkBandStyle) -> ObjectId

"""



class PipeNetworkDisplayStyleType(Enum):
    """ enum PipeNetworkDisplayStyleType, values: Border (0), LabelsAtStructureLocation (5), LabelsForPipe (6), LinePipeSchematic (7), TicksAtPipeEnds (4), TicksAtStructureLocation (3), TitleBox (1), TitleBoxText (2) """
    Border = None
    LabelsAtStructureLocation = None
    LabelsForPipe = None
    LinePipeSchematic = None
    TicksAtPipeEnds = None
    TicksAtStructureLocation = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class PipeRuleSetStyle(NetworkRuleSetStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class PipeRuleSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PipeRuleSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PipeStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self):
        """ GetDisplayStyleModel(self: PipeStyle) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, component):
        """ GetDisplayStylePlan(self: PipeStyle, component: PipeDisplayStylePlanType) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self, component):
        """ GetDisplayStyleProfile(self: PipeStyle, component: PipeDisplayStyleProfileType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, component):
        """ GetDisplayStyleSection(self: PipeStyle, component: PipeDisplayStyleSectionType) -> DisplayStyle """
        pass

    def GetHatchStylePlan(self):
        """ GetHatchStylePlan(self: PipeStyle) -> HatchDisplayStyle """
        pass

    def GetHatchStyleProfile(self, component):
        """ GetHatchStyleProfile(self: PipeStyle, component: PipeHatchStyleProfileType) -> HatchDisplayStyle """
        pass

    def GetHatchStyleSection(self):
        """ GetHatchStyleSection(self: PipeStyle) -> HatchDisplayStyle """
        pass

    PlanOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanOption(self: PipeStyle) -> PipeStylePlanOption

"""

    ProfileOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileOption(self: PipeStyle) -> PipeStyleProfileOption

"""

    SectionCrossingHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionCrossingHatch(self: PipeStyle) -> PipeHatchType

Set: SectionCrossingHatch(self: PipeStyle) = value
"""



class PipeStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PipeStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PipeStyleOptionBase(CivilWrapper<AeccDbPipeStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbPipeStyle>, A_0: bool) """
        pass

    AlignHatchToPipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignHatchToPipe(self: PipeStyleOptionBase) -> bool

Set: AlignHatchToPipe(self: PipeStyleOptionBase) = value
"""

    EndLineSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndLineSize(self: PipeStyleOptionBase) -> float

Set: EndLineSize(self: PipeStyleOptionBase) = value
"""

    EndLineSizePercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndLineSizePercent(self: PipeStyleOptionBase) -> float

Set: EndLineSizePercent(self: PipeStyleOptionBase) = value
"""

    EndSizeOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndSizeOptions(self: PipeStyleOptionBase) -> PipeUserDefinedType

Set: EndSizeOptions(self: PipeStyleOptionBase) = value
"""

    EndSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndSizeType(self: PipeStyleOptionBase) -> PipeEndSizeType

Set: EndSizeType(self: PipeStyleOptionBase) = value
"""

    HatchOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchOptions(self: PipeStyleOptionBase) -> PipeHatchType

Set: HatchOptions(self: PipeStyleOptionBase) = value
"""

    InnerDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerDiameter(self: PipeStyleOptionBase) -> float

Set: InnerDiameter(self: PipeStyleOptionBase) = value
"""

    InnerDiameterPercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerDiameterPercent(self: PipeStyleOptionBase) -> float

Set: InnerDiameterPercent(self: PipeStyleOptionBase) = value
"""

    OuterDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterDiameter(self: PipeStyleOptionBase) -> float

Set: OuterDiameter(self: PipeStyleOptionBase) = value
"""

    OuterDiameterPercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterDiameterPercent(self: PipeStyleOptionBase) -> float

Set: OuterDiameterPercent(self: PipeStyleOptionBase) = value
"""

    PipeToPipeEndCleanup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeToPipeEndCleanup(self: PipeStyleOptionBase) -> bool

Set: PipeToPipeEndCleanup(self: PipeStyleOptionBase) = value
"""

    WallSizeOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallSizeOptions(self: PipeStyleOptionBase) -> PipeUserDefinedType

Set: WallSizeOptions(self: PipeStyleOptionBase) = value
"""

    WallSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallSizeType(self: PipeStyleOptionBase) -> PipeWallSizeType

Set: WallSizeType(self: PipeStyleOptionBase) = value
"""



class PipeStylePlanOption(PipeStyleOptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbPipeStyle>, A_0: bool) """
        pass

    CenterlineOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineOptions(self: PipeStylePlanOption) -> PipeCenterlineType

Set: CenterlineOptions(self: PipeStylePlanOption) = value
"""

    CenterlineSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineSize(self: PipeStylePlanOption) -> float

Set: CenterlineSize(self: PipeStylePlanOption) = value
"""

    CenterlineSizePercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineSizePercent(self: PipeStylePlanOption) -> float

Set: CenterlineSizePercent(self: PipeStylePlanOption) = value
"""

    CenterlineWidthOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineWidthOptions(self: PipeStylePlanOption) -> PipeCenterlineWidthType

Set: CenterlineWidthOptions(self: PipeStylePlanOption) = value
"""



class PipeStyleProfileOption(PipeStyleOptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbPipeStyle>, A_0: bool) """
        pass

    CrossingHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingHatch(self: PipeStyleProfileOption) -> PipeHatchType

Set: CrossingHatch(self: PipeStyleProfileOption) = value
"""



class PipeUserDefinedType(Enum):
    """ enum PipeUserDefinedType, values: UseAbsoluteUnits (1), UseDrawingScale (0), UseSizeAsPercentageOfScreen (2) """
    UseAbsoluteUnits = None
    UseDrawingScale = None
    UseSizeAsPercentageOfScreen = None
    value__ = None


class PipeWallSizeType(Enum):
    """ enum PipeWallSizeType, values: UsePartDimensions (0), UserDefinedWallSize (1) """
    UsePartDimensions = None
    UserDefinedWallSize = None
    value__ = None


class PointCloudClassificationInfo(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: PointCloudClassificationInfo) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: PointCloudClassificationInfo) -> Color

Set: Color(self: PointCloudClassificationInfo) = value
"""

    LayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerId(self: PointCloudClassificationInfo) -> ObjectId

Set: LayerId(self: PointCloudClassificationInfo) = value
"""

    Selected = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selected(self: PointCloudClassificationInfo) -> bool

Set: Selected(self: PointCloudClassificationInfo) = value
"""



class PointCloudClassificationInfoCollection(object):
    # no doc
    def GetEnumerator(self):
        """ GetEnumerator(self: PointCloudClassificationInfoCollection) -> IEnumerator[PointCloudClassificationInfo] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: PointCloudClassificationInfoCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[PointCloudClassificationInfo](enumerable: IEnumerable[PointCloudClassificationInfo], value: PointCloudClassificationInfo) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: PointCloudClassificationInfoCollection) -> int

"""



class PointCloudPointStyle(object):
    # no doc
    Display3dType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display3dType(self: PointCloudPointStyle) -> PointDisplay3dType

Set: Display3dType(self: PointCloudPointStyle) = value
"""

    ElevatinoRangeCreationType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevatinoRangeCreationType(self: PointCloudPointStyle) -> PointCloudElevationRangeCreationType

Set: ElevatinoRangeCreationType(self: PointCloudPointStyle) = value
"""

    ElevationRangeInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationRangeInterval(self: PointCloudPointStyle) -> float

Set: ElevationRangeInterval(self: PointCloudPointStyle) = value
"""

    IntensityRangeMaximum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntensityRangeMaximum(self: PointCloudPointStyle) -> float

Set: IntensityRangeMaximum(self: PointCloudPointStyle) = value
"""

    IntensityRangeMinimum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntensityRangeMinimum(self: PointCloudPointStyle) -> float

Set: IntensityRangeMinimum(self: PointCloudPointStyle) = value
"""

    NumberOfElevationRanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfElevationRanges(self: PointCloudPointStyle) -> int

Set: NumberOfElevationRanges(self: PointCloudPointStyle) = value
"""

    PointElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointElevation(self: PointCloudPointStyle) -> float

Set: PointElevation(self: PointCloudPointStyle) = value
"""

    PointsColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointsColorScheme(self: PointCloudPointStyle) -> PointCouldColorSchemeType

Set: PointsColorScheme(self: PointCloudPointStyle) = value
"""

    RangesColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangesColorScheme(self: PointCloudPointStyle) -> PointCloudRangeColorSchemeType

Set: RangesColorScheme(self: PointCloudPointStyle) = value
"""

    ScaledColorIntensityScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaledColorIntensityScheme(self: PointCloudPointStyle) -> PointCloudRangeColorSchemeType

Set: ScaledColorIntensityScheme(self: PointCloudPointStyle) = value
"""

    ScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleFactor(self: PointCloudPointStyle) -> float

Set: ScaleFactor(self: PointCloudPointStyle) = value
"""

    SingleColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SingleColor(self: PointCloudPointStyle) -> Color

Set: SingleColor(self: PointCloudPointStyle) = value
"""

    SizeInPixels = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeInPixels(self: PointCloudPointStyle) -> int

Set: SizeInPixels(self: PointCloudPointStyle) = value
"""



class PointCloudStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: PointCloudStyle, type: PointCloudDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: PointCloudStyle, type: PointCloudDisplayStyleType) -> DisplayStyle """
        pass

    ClassificationInfos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassificationInfos(self: PointCloudStyle) -> PointCloudClassificationInfoCollection

"""

    PointStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointStyle(self: PointCloudStyle) -> PointCloudPointStyle

"""



class PointCloudStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PointCloudStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PointDisplay3dType(Enum):
    """ enum PointDisplay3dType, values: ExaggeratePointElevations (2), FlattenPointElevations (1), UsePointElevation (0) """
    ExaggeratePointElevations = None
    FlattenPointElevations = None
    UsePointElevation = None
    value__ = None


class PointDisplayStyleType(Enum):
    """ enum PointDisplayStyleType, values: Label (1), Marker (0) """
    Label = None
    Marker = None
    value__ = None


class PointMarkerDisplayType(Enum):
    """ enum PointMarkerDisplayType, values: UseCustomMarker (1), UsePointForMarker (0), UseSymbolForMarker (2) """
    UseCustomMarker = None
    UsePointForMarker = None
    UseSymbolForMarker = None
    value__ = None


class PointStyle(MarkerStyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: PointStyle, type: PointDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: PointStyle, type: PointDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self):
        """ GetDisplayStyleProfile(self: PointStyle) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self):
        """ GetDisplayStyleSection(self: PointStyle) -> DisplayStyle """
        pass

    def GetLabelDisplayStyleModel(self):
        """ GetLabelDisplayStyleModel(self: PointStyle) -> DisplayStyle """
        pass

    def GetLabelDisplayStylePlan(self):
        """ GetLabelDisplayStylePlan(self: PointStyle) -> DisplayStyle """
        pass

    Display3dType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Display3dType(self: PointStyle) -> PointDisplay3dType

Set: Display3dType(self: PointStyle) = value
"""

    Elevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elevation(self: PointStyle) -> float

Set: Elevation(self: PointStyle) = value
"""

    LabelDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelDisplayStyleModel(self: PointStyle) -> DisplayStyle

"""

    LabelDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelDisplayStylePlan(self: PointStyle) -> DisplayStyle

"""

    MarkerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerType(self: PointStyle) -> PointMarkerDisplayType

Set: MarkerType(self: PointStyle) = value
"""

    ScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleFactor(self: PointStyle) -> float

Set: ScaleFactor(self: PointStyle) = value
"""



class PointStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PointStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PointSymbolType(Enum):
    """ enum PointSymbolType, values: K0 (0), K1 (1), K100 (100), K2 (2), K3 (3), K32 (32), K33 (33), K34 (34), K35 (35), K36 (36), K4 (4), K64 (64), K65 (65), K66 (66), K67 (67), K68 (68), K96 (96), K97 (97), K98 (98), K99 (99) """
    K0 = None
    K1 = None
    K100 = None
    K2 = None
    K3 = None
    K32 = None
    K33 = None
    K34 = None
    K35 = None
    K36 = None
    K4 = None
    K64 = None
    K65 = None
    K66 = None
    K67 = None
    K68 = None
    K96 = None
    K97 = None
    K98 = None
    K99 = None
    value__ = None


class PrecisionRangeType(Enum):
    """ enum PrecisionRangeType, values: Precision000001 (0), Precision00001 (1), Precision0001 (2), Precision001 (3), Precision01 (4), Precision1 (5), Precision10 (6), Precision100 (7), Precision1000 (8), Precision10000 (9), Precision100000 (10), Precision1000000 (11) """
    Precision000001 = None
    Precision00001 = None
    Precision0001 = None
    Precision001 = None
    Precision01 = None
    Precision1 = None
    Precision10 = None
    Precision100 = None
    Precision1000 = None
    Precision10000 = None
    Precision100000 = None
    Precision1000000 = None
    value__ = None


class PressureAppurtenanceDisplayStyleSectionType(Enum):
    """ enum PressureAppurtenanceDisplayStyleSectionType, values: Hatch (2), Walls (1) """
    Hatch = None
    value__ = None
    Walls = None


class PressureAppurtenancePlanViewType(Enum):
    """ enum PressureAppurtenancePlanViewType, values: CenterLine (0), ModelBlock (1), UserCustomBlock (2) """
    CenterLine = None
    ModelBlock = None
    UserCustomBlock = None
    value__ = None


class PressureAppurtenanceStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self):
        """ GetDisplayStyleModel(self: PressureAppurtenanceStyle) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self):
        """ GetDisplayStylePlan(self: PressureAppurtenanceStyle) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self):
        """ GetDisplayStyleProfile(self: PressureAppurtenanceStyle) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, component):
        """ GetDisplayStyleSection(self: PressureAppurtenanceStyle, component: PressureAppurtenanceDisplayStyleSectionType) -> DisplayStyle """
        pass

    def GetHatchStyleSection(self):
        """ GetHatchStyleSection(self: PressureAppurtenanceStyle) -> HatchDisplayStyle """
        pass

    PlanOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanOption(self: PressureAppurtenanceStyle) -> PressureAppurtenanceStylePlanOption

"""



class PressureAppurtenanceStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PressureAppurtenanceStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PressureAppurtenanceStylePlanOption(object):
    # no doc
    SymbolBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockId(self: PressureAppurtenanceStylePlanOption) -> ObjectId

Set: SymbolBlockId(self: PressureAppurtenanceStylePlanOption) = value
"""

    SymbolBlockScaleX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockScaleX(self: PressureAppurtenanceStylePlanOption) -> float

Set: SymbolBlockScaleX(self: PressureAppurtenanceStylePlanOption) = value
"""

    SymbolBlockScaleY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockScaleY(self: PressureAppurtenanceStylePlanOption) -> float

Set: SymbolBlockScaleY(self: PressureAppurtenanceStylePlanOption) = value
"""

    SymbolBlockScaleZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockScaleZ(self: PressureAppurtenanceStylePlanOption) -> float

Set: SymbolBlockScaleZ(self: PressureAppurtenanceStylePlanOption) = value
"""

    ViewOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewOptions(self: PressureAppurtenanceStylePlanOption) -> PressureAppurtenancePlanViewType

Set: ViewOptions(self: PressureAppurtenanceStylePlanOption) = value
"""



class PressureFittingDisplayStyleSectionType(Enum):
    """ enum PressureFittingDisplayStyleSectionType, values: Hatch (2), Walls (1) """
    Hatch = None
    value__ = None
    Walls = None


class PressureFittingPlanViewType(Enum):
    """ enum PressureFittingPlanViewType, values: CenterLine (0), ModelBlock (1), UserCustomBlock (2) """
    CenterLine = None
    ModelBlock = None
    UserCustomBlock = None
    value__ = None


class PressureFittingStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self):
        """ GetDisplayStyleModel(self: PressureFittingStyle) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self):
        """ GetDisplayStylePlan(self: PressureFittingStyle) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self):
        """ GetDisplayStyleProfile(self: PressureFittingStyle) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, component):
        """ GetDisplayStyleSection(self: PressureFittingStyle, component: PressureFittingDisplayStyleSectionType) -> DisplayStyle """
        pass

    def GetHatchStyleSection(self):
        """ GetHatchStyleSection(self: PressureFittingStyle) -> HatchDisplayStyle """
        pass

    PlanOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanOption(self: PressureFittingStyle) -> PressureFittingStylePlanOption

"""



class PressureFittingStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PressureFittingStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PressureFittingStylePlanOption(object):
    # no doc
    SymbolBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockId(self: PressureFittingStylePlanOption) -> ObjectId

Set: SymbolBlockId(self: PressureFittingStylePlanOption) = value
"""

    SymbolBlockScaleX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockScaleX(self: PressureFittingStylePlanOption) -> float

Set: SymbolBlockScaleX(self: PressureFittingStylePlanOption) = value
"""

    SymbolBlockScaleY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockScaleY(self: PressureFittingStylePlanOption) -> float

Set: SymbolBlockScaleY(self: PressureFittingStylePlanOption) = value
"""

    SymbolBlockScaleZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockScaleZ(self: PressureFittingStylePlanOption) -> float

Set: SymbolBlockScaleZ(self: PressureFittingStylePlanOption) = value
"""

    ViewOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewOptions(self: PressureFittingStylePlanOption) -> PressureFittingPlanViewType

Set: ViewOptions(self: PressureFittingStylePlanOption) = value
"""



class PressureNetworkBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: PressureNetworkBandStyle, type: PressureNetworkDisplayStyleType) -> DisplayStyle """
        pass

    AppurtenanceLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenanceLabelStyleId(self: PressureNetworkBandStyle) -> ObjectId

"""

    AppurtenanceTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AppurtenanceTickStyle(self: PressureNetworkBandStyle) -> BandTickStyle

"""

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: PressureNetworkBandStyle) -> BandType

"""

    FittingLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingLabelStyleId(self: PressureNetworkBandStyle) -> ObjectId

"""

    FittingTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FittingTickStyle(self: PressureNetworkBandStyle) -> BandTickStyle

"""

    PressurePipeLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PressurePipeLabelStyleId(self: PressureNetworkBandStyle) -> ObjectId

"""

    PressurePipeTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PressurePipeTickStyle(self: PressureNetworkBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: PressureNetworkBandStyle) -> ObjectId

"""



class PressureNetworkDisplayStyleType(Enum):
    """ enum PressureNetworkDisplayStyleType, values: Border (0), LabelsAtAppurtenanceLocation (8), LabelsAtFittingLocation (7), LabelsForPipe (6), LinePipeSchematicLine (9), TicksAtAppurtenanceLocation (5), TicksAtFittingLocation (4), TicksAtPipeEnds (3), TitleBox (1), TitleBoxText (2) """
    Border = None
    LabelsAtAppurtenanceLocation = None
    LabelsAtFittingLocation = None
    LabelsForPipe = None
    LinePipeSchematicLine = None
    TicksAtAppurtenanceLocation = None
    TicksAtFittingLocation = None
    TicksAtPipeEnds = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class PressurePartList(StyleBase):
    # no doc
    def AddPart(self, part):
        """ AddPart(self: PressurePartList, part: PressurePartSize) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    @staticmethod
    def GetAvailablePartLists(database):
        """ GetAvailablePartLists(database: Database) -> ObjectIdCollection """
        pass

    def GetCategories(self, domain):
        """ GetCategories(self: PressurePartList, domain: PressurePartDomainType) -> List[str] """
        pass

    def GetPart(self, guid):
        """ GetPart(self: PressurePartList, guid: str) -> PressurePartSize """
        pass

    def GetPartCategories(self, *__args):
        """
        GetPartCategories(self: PressurePartList, domain: PressurePartDomainType, context: PressurePartContextType) -> Dictionary[str, List[PressurePartSize]]
        GetPartCategories(self: PressurePartList, type: PressurePartType, context: PressurePartContextType) -> Dictionary[str, List[PressurePartSize]]
        """
        pass

    def GetParts(self, *__args):
        """
        GetParts(self: PressurePartList, domain: PressurePartDomainType) -> List[PressurePartSize]
        GetParts(self: PressurePartList, type: PressurePartType) -> List[PressurePartSize]
        """
        pass

    def GetPartTypes(self, domain):
        """ GetPartTypes(self: PressurePartList, domain: PressurePartDomainType) -> List[PressurePartType] """
        pass

    def RemovePart(self, part):
        """ RemovePart(self: PressurePartList, part: PressurePartSize) """
        pass

    def UpdatePart(self, part):
        """ UpdatePart(self: PressurePartList, part: PressurePartSize) """
        pass

    Catalog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Catalog(self: PressurePartList) -> PressurePartCatalog

"""

    CatalogGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CatalogGuid(self: PressurePartList) -> str

"""



class PressurePartSize(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Equals(self, rhs):
        """
        Equals(self: PressurePartSize, rhs: PressurePartSize) -> bool
        Equals(self: PressurePartSize, rhs: object) -> bool
        """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: PressurePartSize) -> int """
        pass

    def GetProperty(self, prop):
        """ GetProperty(self: PressurePartSize, prop: PressurePartContextType) -> object """
        pass

    def SetProperty(self, prop, newVal):
        """ SetProperty(self: PressurePartSize, prop: PressurePartContextType, newVal: object) """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: PressurePartSize) -> str

Set: Description(self: PressurePartSize) = value
"""

    Domain = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Domain(self: PressurePartSize) -> PressurePartDomainType

"""

    FamilyGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FamilyGuid(self: PressurePartSize) -> str

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: PressurePartSize) -> bool

"""

    PartSizeGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartSizeGuid(self: PressurePartSize) -> str

"""

    PartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartType(self: PressurePartSize) -> PressurePartType

"""

    RenderMaterialId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RenderMaterialId(self: PressurePartSize) -> ObjectId

Set: RenderMaterialId(self: PressurePartSize) = value
"""

    StyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleId(self: PressurePartSize) -> ObjectId

Set: StyleId(self: PressurePartSize) = value
"""



class PressurePipeDisplayStylePlanType(Enum):
    """ enum PressurePipeDisplayStylePlanType, values: Centerline (0), EndLine (3), Hatch (4), InsideWalls (1), OutsideWalls (2), Solid (5) """
    Centerline = None
    EndLine = None
    Hatch = None
    InsideWalls = None
    OutsideWalls = None
    Solid = None
    value__ = None


class PressurePipeDisplayStyleProfileType(Enum):
    """ enum PressurePipeDisplayStyleProfileType, values: Centerline (0), CrossingPipeHatch (8), CrossingPipeInsideWall (6), CrossingPipeOutsideWall (7), EndLine (3), Hatch (4), InsideWalls (1), OutsideWalls (2) """
    Centerline = None
    CrossingPipeHatch = None
    CrossingPipeInsideWall = None
    CrossingPipeOutsideWall = None
    EndLine = None
    Hatch = None
    InsideWalls = None
    OutsideWalls = None
    value__ = None


class PressurePipeDisplayStyleSectionType(Enum):
    """ enum PressurePipeDisplayStyleSectionType, values: Hatch (4), Walls (11) """
    Hatch = None
    value__ = None
    Walls = None


class PressurePipeEndSizeType(Enum):
    """ enum PressurePipeEndSizeType, values: DrawToInnerWall (0), DrawToOuterWall (1), UserDefinedEndSize (2) """
    DrawToInnerWall = None
    DrawToOuterWall = None
    UserDefinedEndSize = None
    value__ = None


class PressurePipeHatchStyleProfileType(Enum):
    """ enum PressurePipeHatchStyleProfileType, values: CrossingPipeHatch (1), Hatch (0) """
    CrossingPipeHatch = None
    Hatch = None
    value__ = None


class PressurePipeHatchType(Enum):
    """ enum PressurePipeHatchType, values: HatchToInnerWalls (0), HatchToOuterWalls (1), HatchWallsOnly (2) """
    HatchToInnerWalls = None
    HatchToOuterWalls = None
    HatchWallsOnly = None
    value__ = None


class PressurePipeStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self):
        """ GetDisplayStyleModel(self: PressurePipeStyle) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, component):
        """ GetDisplayStylePlan(self: PressurePipeStyle, component: PressurePipeDisplayStylePlanType) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self, component):
        """ GetDisplayStyleProfile(self: PressurePipeStyle, component: PressurePipeDisplayStyleProfileType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, component):
        """ GetDisplayStyleSection(self: PressurePipeStyle, component: PressurePipeDisplayStyleSectionType) -> DisplayStyle """
        pass

    def GetHatchStylePlan(self):
        """ GetHatchStylePlan(self: PressurePipeStyle) -> HatchDisplayStyle """
        pass

    def GetHatchStyleProfile(self, component):
        """ GetHatchStyleProfile(self: PressurePipeStyle, component: PressurePipeHatchStyleProfileType) -> HatchDisplayStyle """
        pass

    def GetHatchStyleSection(self):
        """ GetHatchStyleSection(self: PressurePipeStyle) -> HatchDisplayStyle """
        pass

    PlanOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanOption(self: PressurePipeStyle) -> PressurePipeStylePlanOption

"""

    ProfileOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileOption(self: PressurePipeStyle) -> PressurePipeStyleProfileOption

"""



class PressurePipeStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: PressurePipeStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class PressurePipeStylePlanOption(object):
    # no doc
    AlignHatchToPipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignHatchToPipe(self: PressurePipeStylePlanOption) -> bool

Set: AlignHatchToPipe(self: PressurePipeStylePlanOption) = value
"""

    EndLineSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndLineSize(self: PressurePipeStylePlanOption) -> float

Set: EndLineSize(self: PressurePipeStylePlanOption) = value
"""

    EndSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndSizeType(self: PressurePipeStylePlanOption) -> PressurePipeEndSizeType

Set: EndSizeType(self: PressurePipeStylePlanOption) = value
"""

    HatchOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchOptions(self: PressurePipeStylePlanOption) -> PressurePipeHatchType

Set: HatchOptions(self: PressurePipeStylePlanOption) = value
"""

    InnerDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerDiameter(self: PressurePipeStylePlanOption) -> float

Set: InnerDiameter(self: PressurePipeStylePlanOption) = value
"""

    OuterDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterDiameter(self: PressurePipeStylePlanOption) -> float

Set: OuterDiameter(self: PressurePipeStylePlanOption) = value
"""

    WallSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallSizeType(self: PressurePipeStylePlanOption) -> PressurePipeWallSizeType

Set: WallSizeType(self: PressurePipeStylePlanOption) = value
"""



class PressurePipeStyleProfileOption(object):
    # no doc
    AlignHatchToPipe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignHatchToPipe(self: PressurePipeStyleProfileOption) -> bool

Set: AlignHatchToPipe(self: PressurePipeStyleProfileOption) = value
"""

    CrossingHatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingHatch(self: PressurePipeStyleProfileOption) -> PressurePipeHatchType

Set: CrossingHatch(self: PressurePipeStyleProfileOption) = value
"""

    EndLineSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndLineSize(self: PressurePipeStyleProfileOption) -> float

Set: EndLineSize(self: PressurePipeStyleProfileOption) = value
"""

    EndSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndSizeType(self: PressurePipeStyleProfileOption) -> PressurePipeEndSizeType

Set: EndSizeType(self: PressurePipeStyleProfileOption) = value
"""

    HatchOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchOptions(self: PressurePipeStyleProfileOption) -> PressurePipeHatchType

Set: HatchOptions(self: PressurePipeStyleProfileOption) = value
"""

    InnerDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InnerDiameter(self: PressurePipeStyleProfileOption) -> float

Set: InnerDiameter(self: PressurePipeStyleProfileOption) = value
"""

    OuterDiameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OuterDiameter(self: PressurePipeStyleProfileOption) -> float

Set: OuterDiameter(self: PressurePipeStyleProfileOption) = value
"""

    WallSizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WallSizeType(self: PressurePipeStyleProfileOption) -> PressurePipeWallSizeType

Set: WallSizeType(self: PressurePipeStyleProfileOption) = value
"""



class PressurePipeWallSizeType(Enum):
    """ enum PressurePipeWallSizeType, values: UsePartDimensions (0), UserDefinedWallSize (1) """
    UsePartDimensions = None
    UserDefinedWallSize = None
    value__ = None


class ProfileDataBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: ProfileDataBandStyle, type: ProfileDataDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: ProfileDataBandStyle) -> BandType

"""

    HGPLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HGPLabelStyleId(self: ProfileDataBandStyle) -> ObjectId

"""

    HGPTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HGPTickStyle(self: ProfileDataBandStyle) -> BandTickStyle

"""

    IncrementalDistanceLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalDistanceLabelStyleId(self: ProfileDataBandStyle) -> ObjectId

"""

    MajorIncrementLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorIncrementLabelStyleId(self: ProfileDataBandStyle) -> ObjectId

"""

    MajorIncrementTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorIncrementTickStyle(self: ProfileDataBandStyle) -> BandTickStyle

"""

    MinorIncrementLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorIncrementLabelStyleId(self: ProfileDataBandStyle) -> ObjectId

"""

    MinorIncrementTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorIncrementTickStyle(self: ProfileDataBandStyle) -> BandTickStyle

"""

    StationEquationLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationEquationLabelStyleId(self: ProfileDataBandStyle) -> ObjectId

"""

    StationEquationTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StationEquationTickStyle(self: ProfileDataBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: ProfileDataBandStyle) -> ObjectId

"""

    VGPLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VGPLabelStyleId(self: ProfileDataBandStyle) -> ObjectId

"""

    VGPTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VGPTickStyle(self: ProfileDataBandStyle) -> BandTickStyle

"""



class ProfileDataDisplayStyleType(Enum):
    """ enum ProfileDataDisplayStyleType, values: Border (0), LabelsAtHGP (11), LabelsAtIncrementalDistance (13), LabelsAtStationEquations (12), LabelsAtVGP (10), MajorStationLabel (8), MajorTicks (3), MinorStationLabel (9), MinorTicks (4), TicksAtHGP (6), TicksAtStationEquations (7), TicksAtVGP (5), TitleBox (1), TitleBoxText (2) """
    Border = None
    LabelsAtHGP = None
    LabelsAtIncrementalDistance = None
    LabelsAtStationEquations = None
    LabelsAtVGP = None
    MajorStationLabel = None
    MajorTicks = None
    MinorStationLabel = None
    MinorTicks = None
    TicksAtHGP = None
    TicksAtStationEquations = None
    TicksAtVGP = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class ProfileDesignCheckCurveType(Enum):
    """ enum ProfileDesignCheckCurveType, values: CrestCurvesOnly (1), CrestSagCurves (0), SagCurvesOnly (2) """
    CrestCurvesOnly = None
    CrestSagCurves = None
    SagCurvesOnly = None
    value__ = None


class ProfileDesignCheckSet(AlignmentDesignCheckSet):
    # no doc
    def AddDesignCheck(self, type, name):
        """
        AddDesignCheck(self: ProfileDesignCheckSet, type: ProfileDesignCheckType, name: str) -> ProfileDesignCheck
        AddDesignCheck(self: ProfileDesignCheckSet, type: AlignmentDesignCheckType, name: str) -> AlignmentDesignCheck
        """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetAllDesignChecks(self):
        """ GetAllDesignChecks(self: ProfileDesignCheckSet) -> Array[ProfileDesignCheck] """
        pass

    def GetCurveDesignCheckType(self, name):
        """ GetCurveDesignCheckType(self: ProfileDesignCheckSet, name: str) -> ProfileDesignCheckCurveType """
        pass

    def RemoveAllDesignCheck(self):
        """ RemoveAllDesignCheck(self: ProfileDesignCheckSet) """
        pass

    def RemoveDesignCheck(self, *__args):
        """ RemoveDesignCheck(self: ProfileDesignCheckSet, designCheck: ProfileDesignCheck)RemoveDesignCheck(self: ProfileDesignCheckSet, type: ProfileDesignCheckType, name: str)RemoveDesignCheck(self: ProfileDesignCheckSet, type: AlignmentDesignCheck)RemoveDesignCheck(self: ProfileDesignCheckSet, type: AlignmentDesignCheckType, name: str) """
        pass

    def SetCurveDesignCheckType(self, name, type):
        """ SetCurveDesignCheckType(self: ProfileDesignCheckSet, name: str, type: ProfileDesignCheckCurveType) """
        pass


class ProfileDesignCheckSetCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ProfileDesignCheckSetCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class ProfileDisplayStyleProfileType(Enum):
    """ enum ProfileDisplayStyleProfileType, values: Arrow (4), AsymmetricalParabola (3), Curve (1), Line (0), LineExtension (5), ParabolicCurveExtension (6), SymmetricalParabola (2), WarningSymbol (11) """
    Arrow = None
    AsymmetricalParabola = None
    Curve = None
    Line = None
    LineExtension = None
    ParabolicCurveExtension = None
    SymmetricalParabola = None
    value__ = None
    WarningSymbol = None


class ProfileLabelSetItem(BaseLabelSetItem):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignStnLabelsDlgTemplate>, A_0: bool) """
        pass

    def GetLabeledAlignmentGeometryPoints(self):
        """ GetLabeledAlignmentGeometryPoints(self: ProfileLabelSetItem) -> Dictionary[AlignmentPointType, bool] """
        pass

    def SetLabeledAlignmentGeometryPoints(self, pointTypes):
        """ SetLabeledAlignmentGeometryPoints(self: ProfileLabelSetItem, pointTypes: Dictionary[AlignmentPointType, bool]) """
        pass

    DimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorOption(self: ProfileLabelSetItem) -> DimensionAnchorType

Set: DimensionAnchorOption(self: ProfileLabelSetItem) = value
"""

    DimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorValue(self: ProfileLabelSetItem) -> float

Set: DimensionAnchorValue(self: ProfileLabelSetItem) = value
"""

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: ProfileLabelSetItem) -> float

Set: Increment(self: ProfileLabelSetItem) = value
"""

    StaggerLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLabel(self: ProfileLabelSetItem) -> StaggerLabelType

Set: StaggerLabel(self: ProfileLabelSetItem) = value
"""

    StaggerLineHeight1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight1(self: ProfileLabelSetItem) -> float

Set: StaggerLineHeight1(self: ProfileLabelSetItem) = value
"""

    StaggerLineHeight2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight2(self: ProfileLabelSetItem) -> float

Set: StaggerLineHeight2(self: ProfileLabelSetItem) = value
"""

    Weeding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weeding(self: ProfileLabelSetItem) -> float

Set: Weeding(self: ProfileLabelSetItem) = value
"""



class ProfileLabelSetStyle(BaseLabelSetStyle):
    # no doc
    def AddCrestCurve(self, labelStyleId):
        """ AddCrestCurve(self: ProfileLabelSetStyle, labelStyleId: ObjectId) """
        pass

    def AddSagCurve(self, labelStyleId):
        """ AddSagCurve(self: ProfileLabelSetStyle, labelStyleId: ObjectId) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileLabelSetStyle) -> IEnumerator[ProfileLabelSetItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfileLabelSetStyle) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfileLabelSetItem](enumerable: IEnumerable[ProfileLabelSetItem], value: ProfileLabelSetItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ProfileLabelSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ProfileLabelSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class ProfileStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetChain3DDisplayStyleModel(self):
        """ GetChain3DDisplayStyleModel(self: ProfileStyle) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self, type):
        """ GetDisplayStyleProfile(self: ProfileStyle, type: ProfileDisplayStyleProfileType) -> DisplayStyle """
        pass

    def GetProfileMarkerDisplayStyleSection(self):
        """ GetProfileMarkerDisplayStyleSection(self: ProfileStyle) -> DisplayStyle """
        pass

    ArrowHeadOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowHeadOption(self: ProfileStyle) -> ArrowHeadOption

"""

    BeginPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeginPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: BeginPointMarkerStyle(self: ProfileStyle) = value
"""

    Chain3DDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Chain3DDisplayStyleModel(self: ProfileStyle) -> DisplayStyle

"""

    ChainTessellationDistance3D = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ChainTessellationDistance3D(self: ProfileStyle) -> float

Set: ChainTessellationDistance3D(self: ProfileStyle) = value
"""

    EndPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: EndPointMarkerStyle(self: ProfileStyle) = value
"""

    HighPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HighPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: HighPointMarkerStyle(self: ProfileStyle) = value
"""

    LowPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: LowPointMarkerStyle(self: ProfileStyle) = value
"""

    ProfileMarkerDisplayStyleSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileMarkerDisplayStyleSection(self: ProfileStyle) -> DisplayStyle

"""

    ProfileMarkerSectionViewMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileMarkerSectionViewMarkerStyle(self: ProfileStyle) -> ObjectId

Set: ProfileMarkerSectionViewMarkerStyle(self: ProfileStyle) = value
"""

    ThroughPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThroughPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: ThroughPointMarkerStyle(self: ProfileStyle) = value
"""

    VCompoundCurveIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VCompoundCurveIntersectPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: VCompoundCurveIntersectPointMarkerStyle(self: ProfileStyle) = value
"""

    VCurveTangentIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VCurveTangentIntersectPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: VCurveTangentIntersectPointMarkerStyle(self: ProfileStyle) = value
"""

    VIntersectionPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VIntersectionPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: VIntersectionPointMarkerStyle(self: ProfileStyle) = value
"""

    VReverseCurveIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VReverseCurveIntersectPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: VReverseCurveIntersectPointMarkerStyle(self: ProfileStyle) = value
"""

    VTangentCurveIntersectPointMarkerStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VTangentCurveIntersectPointMarkerStyle(self: ProfileStyle) -> ObjectId

Set: VTangentCurveIntersectPointMarkerStyle(self: ProfileStyle) = value
"""



class ProfileStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ProfileStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class ProfileViewBandSetItem(BandSetItem):
    # no doc
    def GetHorizontalGeometryPointsOptions(self):
        """ GetHorizontalGeometryPointsOptions(self: ProfileViewBandSetItem) -> GeometryPointSelector[AlignmentPointType] """
        pass

    def GetVerticalGeometryPointsOptions(self):
        """ GetVerticalGeometryPointsOptions(self: ProfileViewBandSetItem) -> GeometryPointSelector[ProfilePointType] """
        pass

    def SetHorizontalGeometryPointsOptions(self, alignmentGeometryPoints):
        """ SetHorizontalGeometryPointsOptions(self: ProfileViewBandSetItem, alignmentGeometryPoints: GeometryPointSelector[AlignmentPointType]) """
        pass

    def SetVerticalGeometryPointsOptions(self, alignmentVerticalGeometryPoints):
        """ SetVerticalGeometryPointsOptions(self: ProfileViewBandSetItem, alignmentVerticalGeometryPoints: GeometryPointSelector[ProfilePointType]) """
        pass

    BandStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: BandStyleId(self: ProfileViewBandSetItem) = value
"""

    LabelAtEndStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelAtEndStation(self: ProfileViewBandSetItem) -> bool

Set: LabelAtEndStation(self: ProfileViewBandSetItem) = value
"""

    LabelAtStartStation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelAtStartStation(self: ProfileViewBandSetItem) -> bool

Set: LabelAtStartStation(self: ProfileViewBandSetItem) = value
"""

    MajorInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorInterval(self: ProfileViewBandSetItem) -> float

Set: MajorInterval(self: ProfileViewBandSetItem) = value
"""

    MinorInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorInterval(self: ProfileViewBandSetItem) -> float

Set: MinorInterval(self: ProfileViewBandSetItem) = value
"""

    SettingsNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class ProfileViewBandSetItemCollection(BandSetItemCollection):
    """
    ProfileViewBandSetItemCollection(location: BandLocationType)
    ProfileViewBandSetItemCollection(location: BandLocationType, profileViewBandSetStyleId: ObjectId)
    """
    def Add(self, *__args):
        """ Add(self: ProfileViewBandSetItemCollection, database: Database, bandType: BandType, profileBandStyleName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: BandSetItemCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: ProfileViewBandSetItemCollection) -> IEnumerator[ProfileViewBandSetItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: ProfileViewBandSetItemCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ProfileViewBandSetItem](enumerable: IEnumerable[ProfileViewBandSetItem], value: ProfileViewBandSetItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, location, profileViewBandSetStyleId=None):
        """
        __new__(cls: type, location: BandLocationType)
        __new__(cls: type, location: BandLocationType, profileViewBandSetStyleId: ObjectId)
        """
        pass


class ProfileViewBandSetStyle(BandSetStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetBottomBandSetItems(self):
        """ GetBottomBandSetItems(self: ProfileViewBandSetStyle) -> ProfileViewBandSetItemCollection """
        pass

    def GetTopBandSetItems(self):
        """ GetTopBandSetItems(self: ProfileViewBandSetStyle) -> ProfileViewBandSetItemCollection """
        pass

    def SetBottomBandSetItems(self, bandSetItems):
        """ SetBottomBandSetItems(self: ProfileViewBandSetStyle, bandSetItems: ProfileViewBandSetItemCollection) """
        pass

    def SetTopBandSetItems(self, bandSetItems):
        """ SetTopBandSetItems(self: ProfileViewBandSetStyle, bandSetItems: ProfileViewBandSetItemCollection) """
        pass


class ProfileViewBandSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ProfileViewBandSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class ProfileViewDisplayStyleType(Enum):
    """ enum ProfileViewDisplayStyleType, values: BottomAxis (19), BottomAxisAnnotationHGP (49), BottomAxisAnnotationMajor (21), BottomAxisAnnotationMinor (22), BottomAxisTicksHGP (50), BottomAxisTicksMajor (23), BottomAxisTicksMinor (24), BottomAxisTitle (20), GraphTitle (0), GridAtHGP (44), GridAtSampleLineStations (53), GridHorizontalMajor (37), GridHorizontalMinor (38), GridVerticalMajor (39), GridVerticalMinor (40), LeftAxis (1), LeftAxisAnnotationMajor (3), LeftAxisAnnotationMinor (4), LeftAxisTicksMajor (5), LeftAxisTicksMinor (6), LeftAxisTitle (2), ProfileHatch (54), RightAxis (7), RightAxisAnnotationMajor (9), RightAxisAnnotationMinor (10), RightAxisTicksMajor (11), RightAxisTicksMinor (12), RightAxisTitle (8), TopAxis (13), TopAxisAnnotationHGP (47), TopAxisAnnotationMajor (15), TopAxisAnnotationMinor (16), TopAxisTicksHGP (48), TopAxisTicksMajor (17), TopAxisTicksMinor (18), TopAxisTitle (14) """
    BottomAxis = None
    BottomAxisAnnotationHGP = None
    BottomAxisAnnotationMajor = None
    BottomAxisAnnotationMinor = None
    BottomAxisTicksHGP = None
    BottomAxisTicksMajor = None
    BottomAxisTicksMinor = None
    BottomAxisTitle = None
    GraphTitle = None
    GridAtHGP = None
    GridAtSampleLineStations = None
    GridHorizontalMajor = None
    GridHorizontalMinor = None
    GridVerticalMajor = None
    GridVerticalMinor = None
    LeftAxis = None
    LeftAxisAnnotationMajor = None
    LeftAxisAnnotationMinor = None
    LeftAxisTicksMajor = None
    LeftAxisTicksMinor = None
    LeftAxisTitle = None
    ProfileHatch = None
    RightAxis = None
    RightAxisAnnotationMajor = None
    RightAxisAnnotationMinor = None
    RightAxisTicksMajor = None
    RightAxisTicksMinor = None
    RightAxisTitle = None
    TopAxis = None
    TopAxisAnnotationHGP = None
    TopAxisAnnotationMajor = None
    TopAxisAnnotationMinor = None
    TopAxisTicksHGP = None
    TopAxisTicksMajor = None
    TopAxisTicksMinor = None
    TopAxisTitle = None
    value__ = None


class ProfileViewStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: ProfileViewStyle, type: ProfileViewDisplayStyleType) -> DisplayStyle """
        pass

    BottomAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomAxis(self: ProfileViewStyle) -> AxisStyle

"""

    GraphStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphStyle(self: ProfileViewStyle) -> GraphStyle

"""

    GridStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridStyle(self: ProfileViewStyle) -> GridStyle

"""

    LeftAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftAxis(self: ProfileViewStyle) -> AxisStyle

"""

    RightAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightAxis(self: ProfileViewStyle) -> AxisStyle

"""

    TopAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopAxis(self: ProfileViewStyle) -> AxisStyle

"""



class ProfileViewStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ProfileViewStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class ProjectionBlockDisplayType(Enum):
    """ enum ProjectionBlockDisplayType, values: Block (2), Marker (1), NativeEntity (0) """
    Block = None
    Marker = None
    NativeEntity = None
    value__ = None


class ProjectionDisplayStyleProfileType(Enum):
    """ enum ProjectionDisplayStyleProfileType, values: BlockProfile (6), MvBlockProfile (7), PointProfile (1), SolidProfile (0), ThreeDPolylineBeginVertexProfile (3), ThreeDPolylineEndVertexProfile (5), ThreeDPolylineInternalVertexProfile (4), ThreeDPolylineSegmentsProfile (2) """
    BlockProfile = None
    MvBlockProfile = None
    PointProfile = None
    SolidProfile = None
    ThreeDPolylineBeginVertexProfile = None
    ThreeDPolylineEndVertexProfile = None
    ThreeDPolylineInternalVertexProfile = None
    ThreeDPolylineSegmentsProfile = None
    value__ = None


class ProjectionDisplayStyleSectionType(Enum):
    """ enum ProjectionDisplayStyleSectionType, values: BlockSection (11), MvBlockSection (12), PointSection (9), SolidSection (8), ThreeDPolylineSection (10) """
    BlockSection = None
    MvBlockSection = None
    PointSection = None
    SolidSection = None
    ThreeDPolylineSection = None
    value__ = None


class ProjectionEntityDisplayType(Enum):
    """ enum ProjectionEntityDisplayType, values: Marker (1), NativeEntity (0) """
    Marker = None
    NativeEntity = None
    value__ = None


class ProjectionProfileOptions(CivilWrapper<AeccDbProfileSectionEntityStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbProfileSectionEntityStyle>, A_0: bool) """
        pass

    AutoCAD3dPolylineBeginVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineBeginVertexMarkerStyleId(self: ProjectionProfileOptions) -> ObjectId

Set: AutoCAD3dPolylineBeginVertexMarkerStyleId(self: ProjectionProfileOptions) = value
"""

    AutoCAD3dPolylineBeginVertexMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineBeginVertexMarkerStyleName(self: ProjectionProfileOptions) -> str

Set: AutoCAD3dPolylineBeginVertexMarkerStyleName(self: ProjectionProfileOptions) = value
"""

    AutoCAD3dPolylineEndVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineEndVertexMarkerStyleId(self: ProjectionProfileOptions) -> ObjectId

Set: AutoCAD3dPolylineEndVertexMarkerStyleId(self: ProjectionProfileOptions) = value
"""

    AutoCAD3dPolylineEndVertexMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineEndVertexMarkerStyleName(self: ProjectionProfileOptions) -> str

Set: AutoCAD3dPolylineEndVertexMarkerStyleName(self: ProjectionProfileOptions) = value
"""

    AutoCAD3dPolylineInternalVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineInternalVertexMarkerStyleId(self: ProjectionProfileOptions) -> ObjectId

Set: AutoCAD3dPolylineInternalVertexMarkerStyleId(self: ProjectionProfileOptions) = value
"""

    AutoCAD3dPolylineInternalVertexMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineInternalVertexMarkerStyleName(self: ProjectionProfileOptions) -> str

Set: AutoCAD3dPolylineInternalVertexMarkerStyleName(self: ProjectionProfileOptions) = value
"""

    AutoCADBlockDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockDisplayOptions(self: ProjectionProfileOptions) -> ProjectionBlockDisplayType

Set: AutoCADBlockDisplayOptions(self: ProjectionProfileOptions) = value
"""

    AutoCADBlockMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockMarkerStyleId(self: ProjectionProfileOptions) -> ObjectId

Set: AutoCADBlockMarkerStyleId(self: ProjectionProfileOptions) = value
"""

    AutoCADBlockMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockMarkerStyleName(self: ProjectionProfileOptions) -> str

Set: AutoCADBlockMarkerStyleName(self: ProjectionProfileOptions) = value
"""

    AutoCADBlockSymbolBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockSymbolBlockId(self: ProjectionProfileOptions) -> ObjectId

Set: AutoCADBlockSymbolBlockId(self: ProjectionProfileOptions) = value
"""

    AutoCADBlockSymbolBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockSymbolBlockName(self: ProjectionProfileOptions) -> str

Set: AutoCADBlockSymbolBlockName(self: ProjectionProfileOptions) = value
"""

    AutoCADPointDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADPointDisplayOptions(self: ProjectionProfileOptions) -> ProjectionEntityDisplayType

Set: AutoCADPointDisplayOptions(self: ProjectionProfileOptions) = value
"""

    AutoCADPointMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADPointMarkerStyleId(self: ProjectionProfileOptions) -> ObjectId

Set: AutoCADPointMarkerStyleId(self: ProjectionProfileOptions) = value
"""

    AutoCADPointMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADPointMarkerStyleName(self: ProjectionProfileOptions) -> str

Set: AutoCADPointMarkerStyleName(self: ProjectionProfileOptions) = value
"""

    AutoCADSolidDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADSolidDisplayOptions(self: ProjectionProfileOptions) -> ProjectionEntityDisplayType

Set: AutoCADSolidDisplayOptions(self: ProjectionProfileOptions) = value
"""

    AutoCADSolidMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADSolidMarkerStyleId(self: ProjectionProfileOptions) -> ObjectId

Set: AutoCADSolidMarkerStyleId(self: ProjectionProfileOptions) = value
"""

    AutoCADSolidMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADSolidMarkerStyleName(self: ProjectionProfileOptions) -> str

Set: AutoCADSolidMarkerStyleName(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDirection(self: ProjectionProfileOptions) -> ViewDirection

Set: MultiViewBlockDirection(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDisplayOptions(self: ProjectionProfileOptions) -> ProjectionBlockDisplayType

Set: MultiViewBlockDisplayOptions(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockDisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDisplayRepresentationId(self: ProjectionProfileOptions) -> ObjectId

Set: MultiViewBlockDisplayRepresentationId(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockDisplayRepresentationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDisplayRepresentationName(self: ProjectionProfileOptions) -> str

Set: MultiViewBlockDisplayRepresentationName(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockMarkerStyleId(self: ProjectionProfileOptions) -> ObjectId

Set: MultiViewBlockMarkerStyleId(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockMarkerStyleName(self: ProjectionProfileOptions) -> str

Set: MultiViewBlockMarkerStyleName(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockSymbolBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockSymbolBlockId(self: ProjectionProfileOptions) -> ObjectId

Set: MultiViewBlockSymbolBlockId(self: ProjectionProfileOptions) = value
"""

    MultiViewBlockSymbolBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockSymbolBlockName(self: ProjectionProfileOptions) -> str

Set: MultiViewBlockSymbolBlockName(self: ProjectionProfileOptions) = value
"""

    VerticallyExaggerateBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticallyExaggerateBlocks(self: ProjectionProfileOptions) -> bool

Set: VerticallyExaggerateBlocks(self: ProjectionProfileOptions) = value
"""

    VerticallyExaggerateMultiViewBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticallyExaggerateMultiViewBlocks(self: ProjectionProfileOptions) -> bool

Set: VerticallyExaggerateMultiViewBlocks(self: ProjectionProfileOptions) = value
"""

    VerticallyExaggerateSolids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticallyExaggerateSolids(self: ProjectionProfileOptions) -> bool

Set: VerticallyExaggerateSolids(self: ProjectionProfileOptions) = value
"""



class ProjectionSectionOptions(CivilWrapper<AeccDbProfileSectionEntityStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbProfileSectionEntityStyle>, A_0: bool) """
        pass

    AutoCAD3dPolylineCrossingMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineCrossingMarkerStyleId(self: ProjectionSectionOptions) -> ObjectId

Set: AutoCAD3dPolylineCrossingMarkerStyleId(self: ProjectionSectionOptions) = value
"""

    AutoCAD3dPolylineCrossingMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCAD3dPolylineCrossingMarkerStyleName(self: ProjectionSectionOptions) -> str

Set: AutoCAD3dPolylineCrossingMarkerStyleName(self: ProjectionSectionOptions) = value
"""

    AutoCADBlockDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockDisplayOptions(self: ProjectionSectionOptions) -> ProjectionBlockDisplayType

Set: AutoCADBlockDisplayOptions(self: ProjectionSectionOptions) = value
"""

    AutoCADBlockMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockMarkerStyleId(self: ProjectionSectionOptions) -> ObjectId

Set: AutoCADBlockMarkerStyleId(self: ProjectionSectionOptions) = value
"""

    AutoCADBlockMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockMarkerStyleName(self: ProjectionSectionOptions) -> str

Set: AutoCADBlockMarkerStyleName(self: ProjectionSectionOptions) = value
"""

    AutoCADBlockSymbolBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockSymbolBlockId(self: ProjectionSectionOptions) -> ObjectId

Set: AutoCADBlockSymbolBlockId(self: ProjectionSectionOptions) = value
"""

    AutoCADBlockSymbolBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADBlockSymbolBlockName(self: ProjectionSectionOptions) -> str

Set: AutoCADBlockSymbolBlockName(self: ProjectionSectionOptions) = value
"""

    AutoCADPointDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADPointDisplayOptions(self: ProjectionSectionOptions) -> ProjectionEntityDisplayType

Set: AutoCADPointDisplayOptions(self: ProjectionSectionOptions) = value
"""

    AutoCADPointMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADPointMarkerStyleId(self: ProjectionSectionOptions) -> ObjectId

Set: AutoCADPointMarkerStyleId(self: ProjectionSectionOptions) = value
"""

    AutoCADPointMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADPointMarkerStyleName(self: ProjectionSectionOptions) -> str

Set: AutoCADPointMarkerStyleName(self: ProjectionSectionOptions) = value
"""

    AutoCADSolidDisplayAsTrueSection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADSolidDisplayAsTrueSection(self: ProjectionSectionOptions) -> bool

Set: AutoCADSolidDisplayAsTrueSection(self: ProjectionSectionOptions) = value
"""

    AutoCADSolidDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADSolidDisplayOptions(self: ProjectionSectionOptions) -> ProjectionEntityDisplayType

Set: AutoCADSolidDisplayOptions(self: ProjectionSectionOptions) = value
"""

    AutoCADSolidMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADSolidMarkerStyleId(self: ProjectionSectionOptions) -> ObjectId

Set: AutoCADSolidMarkerStyleId(self: ProjectionSectionOptions) = value
"""

    AutoCADSolidMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoCADSolidMarkerStyleName(self: ProjectionSectionOptions) -> str

Set: AutoCADSolidMarkerStyleName(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockDirection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDirection(self: ProjectionSectionOptions) -> ViewDirection

Set: MultiViewBlockDirection(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockDisplayOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDisplayOptions(self: ProjectionSectionOptions) -> ProjectionBlockDisplayType

Set: MultiViewBlockDisplayOptions(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockDisplayRepresentationId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDisplayRepresentationId(self: ProjectionSectionOptions) -> ObjectId

Set: MultiViewBlockDisplayRepresentationId(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockDisplayRepresentationName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockDisplayRepresentationName(self: ProjectionSectionOptions) -> str

Set: MultiViewBlockDisplayRepresentationName(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockMarkerStyleId(self: ProjectionSectionOptions) -> ObjectId

Set: MultiViewBlockMarkerStyleId(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockMarkerStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockMarkerStyleName(self: ProjectionSectionOptions) -> str

Set: MultiViewBlockMarkerStyleName(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockSymbolBlockId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockSymbolBlockId(self: ProjectionSectionOptions) -> ObjectId

Set: MultiViewBlockSymbolBlockId(self: ProjectionSectionOptions) = value
"""

    MultiViewBlockSymbolBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultiViewBlockSymbolBlockName(self: ProjectionSectionOptions) -> str

Set: MultiViewBlockSymbolBlockName(self: ProjectionSectionOptions) = value
"""

    VerticallyExaggerateBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticallyExaggerateBlocks(self: ProjectionSectionOptions) -> bool

Set: VerticallyExaggerateBlocks(self: ProjectionSectionOptions) = value
"""

    VerticallyExaggerateMultiViewBlocks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticallyExaggerateMultiViewBlocks(self: ProjectionSectionOptions) -> bool

Set: VerticallyExaggerateMultiViewBlocks(self: ProjectionSectionOptions) = value
"""

    VerticallyExaggerateSolids = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticallyExaggerateSolids(self: ProjectionSectionOptions) -> bool

Set: VerticallyExaggerateSolids(self: ProjectionSectionOptions) = value
"""



class ProjectionStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleProfile(self, type):
        """ GetDisplayStyleProfile(self: ProjectionStyle, type: ProjectionDisplayStyleProfileType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, type):
        """ GetDisplayStyleSection(self: ProjectionStyle, type: ProjectionDisplayStyleSectionType) -> DisplayStyle """
        pass

    ProfileOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileOptions(self: ProjectionStyle) -> ProjectionProfileOptions

"""

    SectionOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionOptions(self: ProjectionStyle) -> ProjectionSectionOptions

"""



class ProjectionStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ProjectionStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class QuantityTakeoffCriteria(StyleBase):
    # no doc
    def AddMaterial(self, materialName):
        """ AddMaterial(self: QuantityTakeoffCriteria, materialName: str) """
        pass

    def Clear(self):
        """ Clear(self: QuantityTakeoffCriteria) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: QuantityTakeoffCriteria, index: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QuantityTakeoffCriteria) -> int

"""



class QuantityTakeoffCriteriaCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: QuantityTakeoffCriteriaCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class QuantityTakeoffCriteriaData(CivilWrapper<AeccDbQuantityTakeoffCriteria>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbQuantityTakeoffCriteria>, A_0: bool) """
        pass

    Condition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Condition(self: QuantityTakeoffCriteriaData) -> MaterialConditionType

Set: Condition(self: QuantityTakeoffCriteriaData) = value
"""

    ItemType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ItemType(self: QuantityTakeoffCriteriaData) -> MaterialItemType

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: QuantityTakeoffCriteriaData) -> str

"""



class QuantityTakeoffCriteriaItem(CivilWrapper<AeccDbQuantityTakeoffCriteria>):
    # no doc
    def AddCorridorShape(self, shapeName):
        """ AddCorridorShape(self: QuantityTakeoffCriteriaItem, shapeName: str) """
        pass

    def AddSurface(self, surfaceName):
        """ AddSurface(self: QuantityTakeoffCriteriaItem, surfaceName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbQuantityTakeoffCriteria>, A_0: bool) """
        pass

    def RemoveCorridorShape(self, shapeName):
        """ RemoveCorridorShape(self: QuantityTakeoffCriteriaItem, shapeName: str) """
        pass

    def RemoveSurface(self, surfaceName):
        """ RemoveSurface(self: QuantityTakeoffCriteriaItem, surfaceName: str) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: QuantityTakeoffCriteriaItem) -> int

"""

    CutFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutFactor(self: QuantityTakeoffCriteriaItem) -> float

Set: CutFactor(self: QuantityTakeoffCriteriaItem) = value
"""

    FillFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillFactor(self: QuantityTakeoffCriteriaItem) -> float

Set: FillFactor(self: QuantityTakeoffCriteriaItem) = value
"""

    MaterialName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaterialName(self: QuantityTakeoffCriteriaItem) -> str

Set: MaterialName(self: QuantityTakeoffCriteriaItem) = value
"""

    QuantityType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityType(self: QuantityTakeoffCriteriaItem) -> MaterialQuantityType

Set: QuantityType(self: QuantityTakeoffCriteriaItem) = value
"""

    ReFillFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReFillFactor(self: QuantityTakeoffCriteriaItem) -> float

Set: ReFillFactor(self: QuantityTakeoffCriteriaItem) = value
"""

    ShapeStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeStyleId(self: QuantityTakeoffCriteriaItem) -> ObjectId

Set: ShapeStyleId(self: QuantityTakeoffCriteriaItem) = value
"""

    ShapeStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeStyleName(self: QuantityTakeoffCriteriaItem) -> str

Set: ShapeStyleName(self: QuantityTakeoffCriteriaItem) = value
"""



class ReferenceTextComponentSelectedType(Enum):
    """ enum ReferenceTextComponentSelectedType, values: Alignment (0), CogoPoint (1), Parcel (2), Profile (3), Surface (4) """
    Alignment = None
    CogoPoint = None
    Parcel = None
    Profile = None
    Surface = None
    value__ = None


class SampleLineDisplayStyleType(Enum):
    """ enum SampleLineDisplayStyleType, values: Lines (0), Vertices (1) """
    Lines = None
    value__ = None
    Vertices = None


class SampleLineStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: SampleLineStyle, type: SampleLineDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SampleLineStyle, type: SampleLineDisplayStyleType) -> DisplayStyle """
        pass


class SampleLineStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SampleLineStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class ScaleType(Enum):
    """ enum ScaleType, values: SizeInAbsoluteUnits (2), SizeRelativeToScreen (1), UseDrawingScale (0) """
    SizeInAbsoluteUnits = None
    SizeRelativeToScreen = None
    UseDrawingScale = None
    value__ = None


class ScalingMethodType(Enum):
    """ enum ScalingMethodType, values: SizeInAbsoluteUnits (2), SizeRelativeToScreen (1), UseDrawingScale (0) """
    SizeInAbsoluteUnits = None
    SizeRelativeToScreen = None
    UseDrawingScale = None
    value__ = None


class SchematicLineOption(Enum):
    """ enum SchematicLineOption, values: Curvature (2), Geometry (0), Radius (1) """
    Curvature = None
    Geometry = None
    Radius = None
    value__ = None


class SectionalDataBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SectionalDataBandStyle, type: SectionalDataDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: SectionalDataBandStyle) -> BandType

"""

    IncrementalSectionDataLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalSectionDataLabelStyleId(self: SectionalDataBandStyle) -> ObjectId

"""

    IncrementalSectionDataTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalSectionDataTickStyle(self: SectionalDataBandStyle) -> BandTickStyle

"""

    SampleLineStationLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineStationLabelStyleId(self: SectionalDataBandStyle) -> ObjectId

"""

    SampleLineStationTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineStationTickStyle(self: SectionalDataBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: SectionalDataBandStyle) -> ObjectId

"""



class SectionalDataDisplayStyleType(Enum):
    """ enum SectionalDataDisplayStyleType, values: Border (0), IncrementalStationRegionLabels (5), SampleLineStationLabels (4), TicksAtSampleLineStation (3), TitleBox (1), TitleBoxText (2) """
    Border = None
    IncrementalStationRegionLabels = None
    SampleLineStationLabels = None
    TicksAtSampleLineStation = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class SectionDataBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SectionDataBandStyle, type: SectionDataDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: SectionDataBandStyle) -> BandType

"""

    CenterlineLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineLabelStyleId(self: SectionDataBandStyle) -> ObjectId

"""

    CenterlineTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterlineTickStyle(self: SectionDataBandStyle) -> BandTickStyle

"""

    GradeBreaksLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeBreaksLabelStyleId(self: SectionDataBandStyle) -> ObjectId

"""

    GradeBreaksTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradeBreaksTickStyle(self: SectionDataBandStyle) -> BandTickStyle

"""

    IncrementalDistanceLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IncrementalDistanceLabelStyleId(self: SectionDataBandStyle) -> ObjectId

"""

    MajorIncrementLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorIncrementLabelStyleId(self: SectionDataBandStyle) -> ObjectId

"""

    MajorIncrementTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorIncrementTickStyle(self: SectionDataBandStyle) -> BandTickStyle

"""

    MinorIncrementLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorIncrementLabelStyleId(self: SectionDataBandStyle) -> ObjectId

"""

    MinorIncrementTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorIncrementTickStyle(self: SectionDataBandStyle) -> BandTickStyle

"""

    SampleLineVerticesLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineVerticesLabelStyleId(self: SectionDataBandStyle) -> ObjectId

"""

    SampleLineVerticesTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineVerticesTickStyle(self: SectionDataBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: SectionDataBandStyle) -> ObjectId

"""



class SectionDataDisplayStyleType(Enum):
    """ enum SectionDataDisplayStyleType, values: Border (0), LabelsAtCenterline (10), LabelsAtGradeBreaks (12), LabelsAtIncrementalDistance (13), LabelsAtMajorOffsets (8), LabelsAtMinorOffsets (9), LabelsAtSampleLineVertices (11), TicksAtCenterline (5), TicksAtGradeBreaks (7), TicksAtMajorOffsets (3), TicksAtMinorOffsets (4), TicksAtSampleLineVertices (6), TitleBox (1), TitleBoxText (2) """
    Border = None
    LabelsAtCenterline = None
    LabelsAtGradeBreaks = None
    LabelsAtIncrementalDistance = None
    LabelsAtMajorOffsets = None
    LabelsAtMinorOffsets = None
    LabelsAtSampleLineVertices = None
    TicksAtCenterline = None
    TicksAtGradeBreaks = None
    TicksAtMajorOffsets = None
    TicksAtMinorOffsets = None
    TicksAtSampleLineVertices = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class SectionDisplayStyleSectionType(Enum):
    """ enum SectionDisplayStyleSectionType, values: Points (1), Segments (0) """
    Points = None
    Segments = None
    value__ = None


class SectionLabelSetItem(BaseLabelSetItem):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbAlignStnLabelsDlgTemplate>, A_0: bool) """
        pass

    DimensionAnchorOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorOption(self: SectionLabelSetItem) -> DimensionAnchorType

Set: DimensionAnchorOption(self: SectionLabelSetItem) = value
"""

    DimensionAnchorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DimensionAnchorValue(self: SectionLabelSetItem) -> float

Set: DimensionAnchorValue(self: SectionLabelSetItem) = value
"""

    Increment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Increment(self: SectionLabelSetItem) -> float

Set: Increment(self: SectionLabelSetItem) = value
"""

    StaggerLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLabel(self: SectionLabelSetItem) -> StaggerLabelType

Set: StaggerLabel(self: SectionLabelSetItem) = value
"""

    StaggerLineHeight1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight1(self: SectionLabelSetItem) -> float

Set: StaggerLineHeight1(self: SectionLabelSetItem) = value
"""

    StaggerLineHeight2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StaggerLineHeight2(self: SectionLabelSetItem) -> float

Set: StaggerLineHeight2(self: SectionLabelSetItem) = value
"""

    Weeding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Weeding(self: SectionLabelSetItem) -> float

Set: Weeding(self: SectionLabelSetItem) = value
"""



class SectionLabelSetStyle(BaseLabelSetStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionLabelSetStyle) -> IEnumerator[SectionLabelSetItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SectionLabelSetStyle) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SectionLabelSetItem](enumerable: IEnumerable[SectionLabelSetItem], value: SectionLabelSetItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class SectionLabelSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SectionLabelSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SectionSegmentBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SectionSegmentBandStyle, type: SectionSegmentDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: SectionSegmentBandStyle) -> BandType

"""

    SegmentLabelsTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLabelsTickStyle(self: SectionSegmentBandStyle) -> BandTickStyle

"""

    SegmentsLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentsLabelStyleId(self: SectionSegmentBandStyle) -> ObjectId

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: SectionSegmentBandStyle) -> ObjectId

"""



class SectionSegmentDisplayStyleType(Enum):
    """ enum SectionSegmentDisplayStyleType, values: Border (0), Labels (4), Lines (5), Ticks (3), TitleBox (1), TitleBoxText (2) """
    Border = None
    Labels = None
    Lines = None
    Ticks = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class SectionStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleSection(self, type):
        """ GetDisplayStyleSection(self: SectionStyle, type: SectionDisplayStyleSectionType) -> DisplayStyle """
        pass


class SectionStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SectionStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SectionViewBandSetItem(BandSetItem):
    # no doc
    BandStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Set: BandStyleId(self: SectionViewBandSetItem) = value
"""

    LabelAtEndOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelAtEndOffset(self: SectionViewBandSetItem) -> bool

Set: LabelAtEndOffset(self: SectionViewBandSetItem) = value
"""

    LabelAtStartOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelAtStartOffset(self: SectionViewBandSetItem) -> bool

Set: LabelAtStartOffset(self: SectionViewBandSetItem) = value
"""

    MajorInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorInterval(self: SectionViewBandSetItem) -> float

Set: MajorInterval(self: SectionViewBandSetItem) = value
"""

    MinorInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorInterval(self: SectionViewBandSetItem) -> float

Set: MinorInterval(self: SectionViewBandSetItem) = value
"""

    SettingsNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class SectionViewBandSetItemCollection(BandSetItemCollection):
    """
    SectionViewBandSetItemCollection(location: BandLocationType, sectionViewBandSetStyleId: ObjectId)
    SectionViewBandSetItemCollection(location: BandLocationType)
    """
    def Add(self, *__args):
        """ Add(self: SectionViewBandSetItemCollection, database: Database, bandType: BandType, sectionBandStyleName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: BandSetItemCollection, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: SectionViewBandSetItemCollection) -> IEnumerator[SectionViewBandSetItem] """
        pass

    def GetObjectEnumerator(self):
        """ GetObjectEnumerator(self: SectionViewBandSetItemCollection) -> IEnumerator """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[SectionViewBandSetItem](enumerable: IEnumerable[SectionViewBandSetItem], value: SectionViewBandSetItem) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, location, sectionViewBandSetStyleId=None):
        """
        __new__(cls: type, location: BandLocationType, sectionViewBandSetStyleId: ObjectId)
        __new__(cls: type, location: BandLocationType)
        """
        pass


class SectionViewBandSetStyle(BandSetStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetBottomBandSetItems(self):
        """ GetBottomBandSetItems(self: SectionViewBandSetStyle) -> SectionViewBandSetItemCollection """
        pass

    def GetTopBandSetItems(self):
        """ GetTopBandSetItems(self: SectionViewBandSetStyle) -> SectionViewBandSetItemCollection """
        pass

    def SetBottomBandSetItems(self, bandSetItems):
        """ SetBottomBandSetItems(self: SectionViewBandSetStyle, bandSetItems: SectionViewBandSetItemCollection) """
        pass

    def SetTopBandSetItems(self, bandSetItems):
        """ SetTopBandSetItems(self: SectionViewBandSetStyle, bandSetItems: SectionViewBandSetItemCollection) """
        pass


class SectionViewBandSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SectionViewBandSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SectionViewDisplayStyleType(Enum):
    """ enum SectionViewDisplayStyleType, values: BottomAxis (19), BottomAxisAnnotationMajor (21), BottomAxisAnnotationMinor (22), BottomAxisTicksMajor (23), BottomAxisTicksMinor (24), BottomAxisTitle (20), CenterAxis (31), CenterAxisAnnotationMajor (33), CenterAxisAnnotationMinor (34), CenterAxisTicksMajor (35), CenterAxisTicksMinor (36), CenterAxisTitle (32), GraphTitle (0), GridAtPGP (43), GridAtSampleLineStations (41), GridHorizontalMajor (37), GridHorizontalMinor (38), GridVerticalMajor (39), GridVerticalMinor (40), LeftAxis (1), LeftAxisAnnotationMajor (3), LeftAxisAnnotationMinor (4), LeftAxisTicksMajor (5), LeftAxisTicksMinor (6), LeftAxisTitle (2), RightAxis (7), RightAxisAnnotationMajor (9), RightAxisAnnotationMinor (10), RightAxisTicksMajor (11), RightAxisTicksMinor (12), RightAxisTitle (8), TopAxis (13), TopAxisAnnotationMajor (15), TopAxisAnnotationMinor (16), TopAxisTicksMajor (17), TopAxisTicksMinor (18), TopAxisTitle (14) """
    BottomAxis = None
    BottomAxisAnnotationMajor = None
    BottomAxisAnnotationMinor = None
    BottomAxisTicksMajor = None
    BottomAxisTicksMinor = None
    BottomAxisTitle = None
    CenterAxis = None
    CenterAxisAnnotationMajor = None
    CenterAxisAnnotationMinor = None
    CenterAxisTicksMajor = None
    CenterAxisTicksMinor = None
    CenterAxisTitle = None
    GraphTitle = None
    GridAtPGP = None
    GridAtSampleLineStations = None
    GridHorizontalMajor = None
    GridHorizontalMinor = None
    GridVerticalMajor = None
    GridVerticalMinor = None
    LeftAxis = None
    LeftAxisAnnotationMajor = None
    LeftAxisAnnotationMinor = None
    LeftAxisTicksMajor = None
    LeftAxisTicksMinor = None
    LeftAxisTitle = None
    RightAxis = None
    RightAxisAnnotationMajor = None
    RightAxisAnnotationMinor = None
    RightAxisTicksMajor = None
    RightAxisTicksMinor = None
    RightAxisTitle = None
    TopAxis = None
    TopAxisAnnotationMajor = None
    TopAxisAnnotationMinor = None
    TopAxisTicksMajor = None
    TopAxisTicksMinor = None
    TopAxisTitle = None
    value__ = None


class SectionViewPlotRuleType(Enum):
    """ enum SectionViewPlotRuleType, values: ByColumns (1), ByRows (0) """
    ByColumns = None
    ByRows = None
    value__ = None


class SectionViewStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SectionViewStyle, type: SectionViewDisplayStyleType) -> DisplayStyle """
        pass

    BottomAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BottomAxis(self: SectionViewStyle) -> AxisStyle

"""

    CenterAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CenterAxis(self: SectionViewStyle) -> AxisStyle

"""

    GraphStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphStyle(self: SectionViewStyle) -> GraphStyle

"""

    GridStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridStyle(self: SectionViewStyle) -> GridStyle

"""

    LeftAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LeftAxis(self: SectionViewStyle) -> AxisStyle

"""

    RightAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RightAxis(self: SectionViewStyle) -> AxisStyle

"""

    TopAxis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TopAxis(self: SectionViewStyle) -> AxisStyle

"""



class SectionViewStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SectionViewStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SegmentColumnStyle(ColumnStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbScheduleTableStyle>, A_0: bool) """
        pass

    def GetContentString(self, type):
        """ GetContentString(self: SegmentColumnStyle, type: TableSegmentDataType) -> str """
        pass

    def GetContentStringFormatted(self, type):
        """ GetContentStringFormatted(self: SegmentColumnStyle, type: TableSegmentDataType) -> str """
        pass

    def SetContentString(self, type, newVal):
        """ SetContentString(self: SegmentColumnStyle, type: TableSegmentDataType, newVal: str) """
        pass

    def SetContentStringFormatted(self, type, newVal):
        """ SetContentStringFormatted(self: SegmentColumnStyle, type: TableSegmentDataType, newVal: str) """
        pass

    m_CurrentIndex = None


class ShapeDisplayStyleType(Enum):
    """ enum ShapeDisplayStyleType, values: AreaFill (1), Border (0) """
    AreaFill = None
    Border = None
    value__ = None


class ShapeStyle(SubassemblySubentityStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: ShapeStyle, type: ShapeDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: ShapeStyle, type: ShapeDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self, type):
        """ GetDisplayStyleProfile(self: ShapeStyle, type: ShapeDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, type):
        """ GetDisplayStyleSection(self: ShapeStyle, type: ShapeDisplayStyleType) -> DisplayStyle """
        pass

    def GetHatchDisplayStyleModel(self):
        """ GetHatchDisplayStyleModel(self: ShapeStyle) -> HatchDisplayStyle """
        pass

    def GetHatchDisplayStylePlan(self):
        """ GetHatchDisplayStylePlan(self: ShapeStyle) -> HatchDisplayStyle """
        pass

    def GetHatchDisplayStyleProfile(self):
        """ GetHatchDisplayStyleProfile(self: ShapeStyle) -> HatchDisplayStyle """
        pass

    def GetHatchDisplayStyleSection(self):
        """ GetHatchDisplayStyleSection(self: ShapeStyle) -> HatchDisplayStyle """
        pass

    AreaFillHatchDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaFillHatchDisplayStyleModel(self: ShapeStyle) -> HatchDisplayStyle

"""

    AreaFillHatchDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreaFillHatchDisplayStylePlan(self: ShapeStyle) -> HatchDisplayStyle

"""

    StyleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StyleType(self: ShapeStyle) -> SubassemblySubentityStyleType

"""



class ShapeStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ShapeStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SheetDisplayStyleType(Enum):
    """ enum SheetDisplayStyleType, values: Border (5), MajorHorizontalGrid (0), MajorVerticalGrid (2), MinorHorizontalGrid (1), MinorVerticalGrid (3), PrintArea (4) """
    Border = None
    MajorHorizontalGrid = None
    MajorVerticalGrid = None
    MinorHorizontalGrid = None
    MinorVerticalGrid = None
    PrintArea = None
    value__ = None


class SheetStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    PageLayoutId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageLayoutId(self: SheetStyle) -> ObjectId

Set: PageLayoutId(self: SheetStyle) = value
"""

    PageMarginBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageMarginBottom(self: SheetStyle) -> float

Set: PageMarginBottom(self: SheetStyle) = value
"""

    PageMarginLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageMarginLeft(self: SheetStyle) -> float

Set: PageMarginLeft(self: SheetStyle) = value
"""

    PageMarginRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageMarginRight(self: SheetStyle) -> float

Set: PageMarginRight(self: SheetStyle) = value
"""

    PageMarginTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PageMarginTop(self: SheetStyle) -> float

Set: PageMarginTop(self: SheetStyle) = value
"""



class SheetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SheetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SizeFilterField(PartDataField):
    # no doc
    DataSource = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataSource(self: SizeFilterField) -> PartDataSourceType

"""

    IsMultipleSelect = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMultipleSelect(self: SizeFilterField) -> bool

Set: IsMultipleSelect(self: SizeFilterField) = value
"""


    m_dataField = None
    m_domain = None
    m_parentDataRecord = None
    m_rawTable = None


class SizeFilterRecord(object):
    """ SizeFilterRecord(partFamily: PartFamily) """
    def Dispose(self):
        """ Dispose(self: SizeFilterRecord) """
        pass

    def GetParamByContextAndIndex(self, context, index):
        """ GetParamByContextAndIndex(self: SizeFilterRecord, context: PartContextType, index: int) -> SizeFilterField """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, partFamily):
        """ __new__(cls: type, partFamily: PartFamily) """
        pass

    ParamCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParamCount(self: SizeFilterRecord) -> int

"""

    PartFamilyGuid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartFamilyGuid(self: SizeFilterRecord) -> str

"""



class SlopeArrowType(Enum):
    """ enum SlopeArrowType, values: Closed (1), Double (3), Filled (0), Open (2) """
    Closed = None
    Double = None
    Filled = None
    Open = None
    value__ = None


class SlopePatternComponent(CivilWrapper<AeccDbSlopePatternStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSlopePatternStyle>, A_0: bool) """
        pass

    SlopeLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeLine(self: SlopePatternComponent) -> SlopePatternLine

"""

    SlopeLineOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeLineOffset(self: SlopePatternComponent) -> SlopePatternLineOffset

"""

    SlopeLineSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeLineSymbol(self: SlopePatternComponent) -> SlopePatternLineSymbol

"""



class SlopePatternLine(CivilWrapper<AeccDbSlopePatternStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSlopePatternStyle>, A_0: bool) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: SlopePatternLine) -> Color

Set: Color(self: SlopePatternLine) = value
"""

    Grade1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grade1(self: SlopePatternLine) -> float

Set: Grade1(self: SlopePatternLine) = value
"""

    Grade2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grade2(self: SlopePatternLine) -> float

Set: Grade2(self: SlopePatternLine) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: SlopePatternLine) -> float

Set: Length(self: SlopePatternLine) = value
"""

    LengthType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthType(self: SlopePatternLine) -> SlopePatternLengthType

Set: LengthType(self: SlopePatternLine) = value
"""

    Linetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetype(self: SlopePatternLine) -> str

Set: Linetype(self: SlopePatternLine) = value
"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWeight(self: SlopePatternLine) -> LineWeight

Set: LineWeight(self: SlopePatternLine) = value
"""

    MaximumLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumLength(self: SlopePatternLine) -> float

Set: MaximumLength(self: SlopePatternLine) = value
"""

    PercentofLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentofLength(self: SlopePatternLine) -> float

Set: PercentofLength(self: SlopePatternLine) = value
"""

    PercentofLength1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentofLength1(self: SlopePatternLine) -> float

Set: PercentofLength1(self: SlopePatternLine) = value
"""

    PercentofLength2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentofLength2(self: SlopePatternLine) -> float

Set: PercentofLength2(self: SlopePatternLine) = value
"""

    StartType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartType(self: SlopePatternLine) -> SlopePatternStartType

Set: StartType(self: SlopePatternLine) = value
"""



class SlopePatternLineOffset(CivilWrapper<AeccDbSlopePatternStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSlopePatternStyle>, A_0: bool) """
        pass

    Distance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Distance(self: SlopePatternLineOffset) -> float

Set: Distance(self: SlopePatternLineOffset) = value
"""

    MaximumDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumDistance(self: SlopePatternLineOffset) -> float

Set: MaximumDistance(self: SlopePatternLineOffset) = value
"""

    MinimumDistance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumDistance(self: SlopePatternLineOffset) -> float

Set: MinimumDistance(self: SlopePatternLineOffset) = value
"""

    Numberoflines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Numberoflines(self: SlopePatternLineOffset) -> int

Set: Numberoflines(self: SlopePatternLineOffset) = value
"""

    OffsetType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OffsetType(self: SlopePatternLineOffset) -> SlopePatternOffsetType

Set: OffsetType(self: SlopePatternLineOffset) = value
"""

    PercentofLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentofLength(self: SlopePatternLineOffset) -> float

Set: PercentofLength(self: SlopePatternLineOffset) = value
"""

    RadialOffsetAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RadialOffsetAngle(self: SlopePatternLineOffset) -> float

Set: RadialOffsetAngle(self: SlopePatternLineOffset) = value
"""



class SlopePatternLineSymbol(CivilWrapper<AeccDbSlopePatternStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSlopePatternStyle>, A_0: bool) """
        pass

    BlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockName(self: SlopePatternLineSymbol) -> str

Set: BlockName(self: SlopePatternLineSymbol) = value
"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: SlopePatternLineSymbol) -> Color

Set: Color(self: SlopePatternLineSymbol) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: SlopePatternLineSymbol) -> float

Set: Length(self: SlopePatternLineSymbol) = value
"""

    LengthType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LengthType(self: SlopePatternLineSymbol) -> SlopePatternLengthType

Set: LengthType(self: SlopePatternLineSymbol) = value
"""

    Linetype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Linetype(self: SlopePatternLineSymbol) -> str

Set: Linetype(self: SlopePatternLineSymbol) = value
"""

    LineWeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineWeight(self: SlopePatternLineSymbol) -> LineWeight

Set: LineWeight(self: SlopePatternLineSymbol) = value
"""

    Numberoflines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Numberoflines(self: SlopePatternLineSymbol) -> int

Set: Numberoflines(self: SlopePatternLineSymbol) = value
"""

    PercentofLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PercentofLength(self: SlopePatternLineSymbol) -> float

Set: PercentofLength(self: SlopePatternLineSymbol) = value
"""

    SymbolType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolType(self: SlopePatternLineSymbol) -> SlopePatternSymbolType

Set: SymbolType(self: SlopePatternLineSymbol) = value
"""

    WidthRatio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WidthRatio(self: SlopePatternLineSymbol) -> float

Set: WidthRatio(self: SlopePatternLineSymbol) = value
"""



class SlopePatternStyle(StyleBase):
    # no doc
    def AddComponent(self, position):
        """ AddComponent(self: SlopePatternStyle, position: int) """
        pass

    def CopyComponent(self, index, insertPosition):
        """ CopyComponent(self: SlopePatternStyle, index: int, insertPosition: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: SlopePatternStyle, index: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: SlopePatternStyle) -> int

"""

    MinDisplayLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinDisplayLength(self: SlopePatternStyle) -> float

Set: MinDisplayLength(self: SlopePatternStyle) = value
"""

    PreviewFeatureLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviewFeatureLength(self: SlopePatternStyle) -> float

Set: PreviewFeatureLength(self: SlopePatternStyle) = value
"""

    PreviewSlope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviewSlope(self: SlopePatternStyle) -> float

Set: PreviewSlope(self: SlopePatternStyle) = value
"""

    PreviewSlopeLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreviewSlopeLength(self: SlopePatternStyle) -> float

Set: PreviewSlopeLength(self: SlopePatternStyle) = value
"""



class SlopePatternStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SlopePatternStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class StaggerLabelType(Enum):
    """ enum StaggerLabelType, values: Both (1), Left (3), None (0), Right (2) """
    Both = None
    Left = None
    None = None
    Right = None
    value__ = None


class StructureColumnComponentData(CivilWrapper<tableCellComponentVec>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<tableCellComponentVec>, A_0: bool) """
        pass

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: StructureColumnComponentData) -> StructureColumnComponentType

"""

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: StructureColumnComponentData) -> str

Set: Content(self: StructureColumnComponentData) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: StructureColumnComponentData) -> str

Set: Name(self: StructureColumnComponentData) = value
"""



class StructureColumnComponents(CivilWrapper<tableCellComponentVec>):
    # no doc
    def AddComponent(self, name, componentType):
        """ AddComponent(self: StructureColumnComponents, name: str, componentType: StructureColumnComponentType) """
        pass

    def Clear(self):
        """ Clear(self: StructureColumnComponents) """
        pass

    def Dispose(self):
        """ Dispose(self: CivilWrapper<tableCellComponentVec>, A_0: bool) """
        pass

    def RemoveAt(self, *__args):
        """ RemoveAt(self: StructureColumnComponents, index: int)RemoveAt(self: StructureColumnComponents, name: str) """
        pass

    def SwitchComponentsOrder(self, index1, index2):
        """ SwitchComponentsOrder(self: StructureColumnComponents, index1: int, index2: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: StructureColumnComponents) -> int

"""



class StructureColumnStyle(ColumnStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbScheduleTableStyle>, A_0: bool) """
        pass

    def GetComponents(self):
        """ GetComponents(self: StructureColumnStyle) -> StructureColumnComponents """
        pass

    def SetComponents(self, componentDatas):
        """ SetComponents(self: StructureColumnStyle, componentDatas: StructureColumnComponents) """
        pass

    m_CurrentIndex = None


class StructureDisplayStylePlanType(Enum):
    """ enum StructureDisplayStylePlanType, values: Solid (2), Structure (0), StructureHatch (1) """
    Solid = None
    Structure = None
    StructureHatch = None
    value__ = None


class StructureDisplayStyleProfileType(Enum):
    """ enum StructureDisplayStyleProfileType, values: Structure (0), StructureHatch (1), StructurePipeOutlines (3) """
    Structure = None
    StructureHatch = None
    StructurePipeOutlines = None
    value__ = None


class StructureDisplayStyleSectionType(Enum):
    """ enum StructureDisplayStyleSectionType, values: Structure (0), StructureHatch (1), StructurePipeOutlines (3) """
    Structure = None
    StructureHatch = None
    StructurePipeOutlines = None
    value__ = None


class StructureInsertionLocation(Enum):
    """ enum StructureInsertionLocation, values: Rim (0), Sump (1) """
    Rim = None
    Sump = None
    value__ = None


class StructureModelViewOptionType(Enum):
    """ enum StructureModelViewOptionType, values: UseCatalogDefined3DPart (0), UseSimple3DPart (1) """
    UseCatalogDefined3DPart = None
    UseSimple3DPart = None
    value__ = None


class StructurePlanViewType(Enum):
    """ enum StructurePlanViewType, values: UseOuterPartBoundary (0), UserDefinedPart (1) """
    UseOuterPartBoundary = None
    UserDefinedPart = None
    value__ = None


class StructureRuleSetStyle(NetworkRuleSetStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass


class StructureRuleSetStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: StructureRuleSetStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class StructureSimpleSolidType(Enum):
    """ enum StructureSimpleSolidType, values: Box (0), Cylinder (1), PartDefinedShape (3), Sphere (2) """
    Box = None
    Cylinder = None
    PartDefinedShape = None
    Sphere = None
    value__ = None


class StructureSizeOptionsType(Enum):
    """ enum StructureSizeOptionsType, values: UseAbsoluteUnits (2), UseDrawingScale (0), UseFixedScale (1), UseFixedScaleFromPartSize (4), UseSizeAsPercentageOfScreen (3) """
    UseAbsoluteUnits = None
    UseDrawingScale = None
    UseFixedScale = None
    UseFixedScaleFromPartSize = None
    UseSizeAsPercentageOfScreen = None
    value__ = None


class StructureStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self):
        """ GetDisplayStyleModel(self: StructureStyle) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, component):
        """ GetDisplayStylePlan(self: StructureStyle, component: StructureDisplayStylePlanType) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self, component):
        """ GetDisplayStyleProfile(self: StructureStyle, component: StructureDisplayStyleProfileType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, component):
        """ GetDisplayStyleSection(self: StructureStyle, component: StructureDisplayStyleSectionType) -> DisplayStyle """
        pass

    def GetHatchStylePlan(self):
        """ GetHatchStylePlan(self: StructureStyle) -> HatchDisplayStyle """
        pass

    def GetHatchStyleProfile(self):
        """ GetHatchStyleProfile(self: StructureStyle) -> HatchDisplayStyle """
        pass

    def GetHatchStyleSection(self):
        """ GetHatchStyleSection(self: StructureStyle) -> HatchDisplayStyle """
        pass

    ModelOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelOption(self: StructureStyle) -> StructureStyleModelOption

"""

    PlanOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanOption(self: StructureStyle) -> StructureStylePlanOption

"""

    ProfileOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileOption(self: StructureStyle) -> StructureStyleProfileOption

"""

    SectionOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionOption(self: StructureStyle) -> StructureStyleSectionOption

"""



class StructureStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: StructureStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class StructureStyleModelOption(CivilWrapper<AeccDbStructureStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStructureStyle>, A_0: bool) """
        pass

    ModelViewOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ModelViewOptions(self: StructureStyleModelOption) -> StructureModelViewOptionType

Set: ModelViewOptions(self: StructureStyleModelOption) = value
"""

    SimpleSolidType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SimpleSolidType(self: StructureStyleModelOption) -> StructureSimpleSolidType

Set: SimpleSolidType(self: StructureStyleModelOption) = value
"""



class StructureStyleOptionBase(CivilWrapper<AeccDbStructureStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStructureStyle>, A_0: bool) """
        pass

    BlockInsertLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BlockInsertLocation(self: StructureStyleOptionBase) -> StructureInsertionLocation

Set: BlockInsertLocation(self: StructureStyleOptionBase) = value
"""

    MaskConnectedObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskConnectedObjects(self: StructureStyleOptionBase) -> bool

Set: MaskConnectedObjects(self: StructureStyleOptionBase) = value
"""

    SizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeType(self: StructureStyleOptionBase) -> StructureSizeOptionsType

Set: SizeType(self: StructureStyleOptionBase) = value
"""

    SymbolBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockName(self: StructureStyleOptionBase) -> str

Set: SymbolBlockName(self: StructureStyleOptionBase) = value
"""

    SymbolBlockXScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockXScale(self: StructureStyleOptionBase) -> float

Set: SymbolBlockXScale(self: StructureStyleOptionBase) = value
"""

    SymbolBlockYScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockYScale(self: StructureStyleOptionBase) -> float

Set: SymbolBlockYScale(self: StructureStyleOptionBase) = value
"""

    SymbolBlockZScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockZScale(self: StructureStyleOptionBase) -> float

Set: SymbolBlockZScale(self: StructureStyleOptionBase) = value
"""

    ViewOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewOptions(self: StructureStyleOptionBase) -> StructureViewType

Set: ViewOptions(self: StructureStyleOptionBase) = value
"""

    XSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XSize(self: StructureStyleOptionBase) -> float

Set: XSize(self: StructureStyleOptionBase) = value
"""

    XSizePercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XSizePercent(self: StructureStyleOptionBase) -> float

Set: XSizePercent(self: StructureStyleOptionBase) = value
"""

    YSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YSize(self: StructureStyleOptionBase) -> float

Set: YSize(self: StructureStyleOptionBase) = value
"""

    YSizePercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YSizePercent(self: StructureStyleOptionBase) -> float

Set: YSizePercent(self: StructureStyleOptionBase) = value
"""



class StructureStylePlanOption(CivilWrapper<AeccDbStructureStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStructureStyle>, A_0: bool) """
        pass

    MaskConnectedObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaskConnectedObjects(self: StructureStylePlanOption) -> bool

Set: MaskConnectedObjects(self: StructureStylePlanOption) = value
"""

    PlanViewOptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlanViewOptions(self: StructureStylePlanOption) -> StructurePlanViewType

Set: PlanViewOptions(self: StructureStylePlanOption) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: StructureStylePlanOption) -> float

Set: Size(self: StructureStylePlanOption) = value
"""

    SizePercent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizePercent(self: StructureStylePlanOption) -> float

Set: SizePercent(self: StructureStylePlanOption) = value
"""

    SizeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SizeType(self: StructureStylePlanOption) -> StructureSizeOptionsType

Set: SizeType(self: StructureStylePlanOption) = value
"""

    SymbolBlockName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockName(self: StructureStylePlanOption) -> str

Set: SymbolBlockName(self: StructureStylePlanOption) = value
"""

    SymbolBlockXScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockXScale(self: StructureStylePlanOption) -> float

Set: SymbolBlockXScale(self: StructureStylePlanOption) = value
"""

    SymbolBlockYScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockYScale(self: StructureStylePlanOption) -> float

Set: SymbolBlockYScale(self: StructureStylePlanOption) = value
"""

    SymbolBlockZScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SymbolBlockZScale(self: StructureStylePlanOption) -> float

Set: SymbolBlockZScale(self: StructureStylePlanOption) = value
"""



class StructureStyleProfileOption(StructureStyleOptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStructureStyle>, A_0: bool) """
        pass


class StructureStyleSectionOption(StructureStyleOptionBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbStructureStyle>, A_0: bool) """
        pass


class StructureViewType(Enum):
    """ enum StructureViewType, values: DisplayAsBlock (1), DisplayAsBoundary (0), DisplayAsSolid (2) """
    DisplayAsBlock = None
    DisplayAsBoundary = None
    DisplayAsSolid = None
    value__ = None


class StylesRoot(TreeOidWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AlignmentDesignCheckSets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentDesignCheckSets(self: StylesRoot) -> AlignmentDesignCheckSetCollection

"""

    AlignmentStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentStyles(self: StylesRoot) -> AlignmentStyleCollection

"""

    AssemblyStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyStyles(self: StylesRoot) -> AssemblyStyleCollection

"""

    BandStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandStyles(self: StylesRoot) -> BandStylesRoot

"""

    BuildingSiteStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BuildingSiteStyles(self: StylesRoot) -> BuildingSiteStyleCollection

"""

    CantViewStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CantViewStyles(self: StylesRoot) -> CantViewStyleCollection

"""

    CatchmentStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CatchmentStyles(self: StylesRoot) -> CatchmentStyleCollection

"""

    CodeSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CodeSetStyles(self: StylesRoot) -> CodeSetStyleCollection

"""

    CorridorStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorStyles(self: StylesRoot) -> CorridorStyleCollection

"""

    FeatureLineStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureLineStyles(self: StylesRoot) -> FeatureLineStyleCollection

"""

    GradingCriteriaSets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradingCriteriaSets(self: StylesRoot) -> GradingCriteriaSetCollection

"""

    GradingStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GradingStyles(self: StylesRoot) -> GradingStyleCollection

"""

    GroupPlotStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupPlotStyles(self: StylesRoot) -> GroupPlotStyleCollection

"""

    InterferenceStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InterferenceStyles(self: StylesRoot) -> InterferenceStyleCollection

"""

    IntersectionStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntersectionStyles(self: StylesRoot) -> IntersectionStyleCollection

"""

    LabelSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelSetStyles(self: StylesRoot) -> LabelSetStylesRoot

"""

    LabelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyles(self: StylesRoot) -> LabelStylesRoot

"""

    LinkStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkStyles(self: StylesRoot) -> LinkStyleCollection

"""

    MarkerStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MarkerStyles(self: StylesRoot) -> MarkerStyleCollection

"""

    MassHaulLineStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MassHaulLineStyles(self: StylesRoot) -> MassHaulLineStyleCollection

"""

    MassHaulViewStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MassHaulViewStyles(self: StylesRoot) -> MassHaulViewStyleCollection

"""

    MatchLineStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MatchLineStyles(self: StylesRoot) -> MatchLineStyleCollection

"""

    ParcelStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParcelStyles(self: StylesRoot) -> ParcelStyleCollection

"""

    PartsListSet = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PartsListSet(self: StylesRoot) -> PartsListCollection

"""

    PipeRuleSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeRuleSetStyles(self: StylesRoot) -> PipeRuleSetStyleCollection

"""

    PipeStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeStyles(self: StylesRoot) -> PipeStyleCollection

"""

    PointCloudStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointCloudStyles(self: StylesRoot) -> PointCloudStyleCollection

"""

    PointStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointStyles(self: StylesRoot) -> PointStyleCollection

"""

    ProfileDesignCheckSets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileDesignCheckSets(self: StylesRoot) -> ProfileDesignCheckSetCollection

"""

    ProfileStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileStyles(self: StylesRoot) -> ProfileStyleCollection

"""

    ProfileViewBandSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewBandSetStyles(self: StylesRoot) -> ProfileViewBandSetStyleCollection

"""

    ProfileViewStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProfileViewStyles(self: StylesRoot) -> ProfileViewStyleCollection

"""

    ProjectionStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionStyles(self: StylesRoot) -> ProjectionStyleCollection

"""

    QuantityTakeoffCriterias = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityTakeoffCriterias(self: StylesRoot) -> QuantityTakeoffCriteriaCollection

"""

    SampleLineStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SampleLineStyles(self: StylesRoot) -> SampleLineStyleCollection

"""

    SectionStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionStyles(self: StylesRoot) -> SectionStyleCollection

"""

    SectionViewBandSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewBandSetStyles(self: StylesRoot) -> SectionViewBandSetStyleCollection

"""

    SectionViewStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewStyles(self: StylesRoot) -> SectionViewStyleCollection

"""

    ShapeStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShapeStyles(self: StylesRoot) -> ShapeStyleCollection

"""

    SheetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SheetStyles(self: StylesRoot) -> SheetStyleCollection

"""

    SlopePatternStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopePatternStyles(self: StylesRoot) -> SlopePatternStyleCollection

"""

    StructureRuleSetStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureRuleSetStyles(self: StylesRoot) -> StructureRuleSetStyleCollection

"""

    StructureStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureStyles(self: StylesRoot) -> StructureStyleCollection

"""

    SuperelevationViewStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SuperelevationViewStyles(self: StylesRoot) -> SuperelevationViewStyleCollection

"""

    SurfaceStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceStyles(self: StylesRoot) -> SurfaceStyleCollection

"""

    SurveyFigureStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurveyFigureStyles(self: StylesRoot) -> SurveyFigureStyleCollection

"""

    SurveyNetworkStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurveyNetworkStyles(self: StylesRoot) -> SurveyNetworkStyleCollection

"""

    TableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableStyles(self: StylesRoot) -> TableStylesRoot

"""

    ViewFrameStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewFrameStyles(self: StylesRoot) -> ViewFrameStyleCollection

"""



class StylesRootPressurePipesExtension(object):
    # no doc
    @staticmethod
    def GetPressureAppurtenanceStyles(stylesRoot):
        """ GetPressureAppurtenanceStyles(stylesRoot: StylesRoot) -> PressureAppurtenanceStyleCollection """
        pass

    @staticmethod
    def GetPressureFittingStyles(stylesRoot):
        """ GetPressureFittingStyles(stylesRoot: StylesRoot) -> PressureFittingStyleCollection """
        pass

    @staticmethod
    def GetPressurePipeStyles(stylesRoot):
        """ GetPressurePipeStyles(stylesRoot: StylesRoot) -> PressurePipeStyleCollection """
        pass

    __all__ = [
        'GetPressureAppurtenanceStyles',
        'GetPressureFittingStyles',
        'GetPressurePipeStyles',
    ]


class SubassemblySubentityStyleType(Enum):
    """ enum SubassemblySubentityStyleType, values: LinkType (1), MarkerType (0), ShapeType (2) """
    LinkType = None
    MarkerType = None
    ShapeType = None
    value__ = None


class SuperelevationDataBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SuperelevationDataBandStyle, type: SuperelevationDataDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: SuperelevationDataBandStyle) -> BandType

"""

    FullSuperLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullSuperLabelStyleId(self: SuperelevationDataBandStyle) -> ObjectId

"""

    FullSuperTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FullSuperTickStyle(self: SuperelevationDataBandStyle) -> BandTickStyle

"""

    LevelCrownLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LevelCrownLabelStyleId(self: SuperelevationDataBandStyle) -> ObjectId

"""

    LevelCrownTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LevelCrownTickStyle(self: SuperelevationDataBandStyle) -> BandTickStyle

"""

    NormalCrownLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalCrownLabelStyleId(self: SuperelevationDataBandStyle) -> ObjectId

"""

    NormalCrownTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NormalCrownTickStyle(self: SuperelevationDataBandStyle) -> BandTickStyle

"""

    ReverseCrownLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseCrownLabelStyleId(self: SuperelevationDataBandStyle) -> ObjectId

"""

    ReverseCrownTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReverseCrownTickStyle(self: SuperelevationDataBandStyle) -> BandTickStyle

"""

    ShoulderCriticalPointsLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShoulderCriticalPointsLabelStyleId(self: SuperelevationDataBandStyle) -> ObjectId

"""

    ShoulderCriticalPointsTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShoulderCriticalPointsTickStyle(self: SuperelevationDataBandStyle) -> BandTickStyle

"""

    SlopeTransitionRegionLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeTransitionRegionLabelStyleId(self: SuperelevationDataBandStyle) -> ObjectId

"""

    SlopeTransitionRegionTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeTransitionRegionTickStyle(self: SuperelevationDataBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: SuperelevationDataBandStyle) -> ObjectId

"""



class SuperelevationDataDisplayStyleType(Enum):
    """ enum SuperelevationDataDisplayStyleType, values: Border (0), LabelsAlongTransitionSegment (13), LabelsAtFullSuper (12), LabelsAtLevelCrown (10), LabelsAtNormalCrown (8), LabelsAtReverseCrown (11), LabelsAtShoulderBreakOver (9), LineLeftInsidePavement (17), LineLeftInsideShoulder (18), LineLeftOutsidePavement (16), LineLeftOutsideShoulder (15), LineRightInsidePavement (20), LineRightInsideShoulder (19), LineRightOutsidePavement (21), LineRightOutsideShoulder (22), ReferenceLine (14), TicksAtFullSuper (7), TicksAtLevelCrown (5), TicksAtNormalCrown (3), TicksAtReverseCrown (6), TicksAtShoulderBreakOver (4), TitleBox (1), TitleBoxText (2) """
    Border = None
    LabelsAlongTransitionSegment = None
    LabelsAtFullSuper = None
    LabelsAtLevelCrown = None
    LabelsAtNormalCrown = None
    LabelsAtReverseCrown = None
    LabelsAtShoulderBreakOver = None
    LineLeftInsidePavement = None
    LineLeftInsideShoulder = None
    LineLeftOutsidePavement = None
    LineLeftOutsideShoulder = None
    LineRightInsidePavement = None
    LineRightInsideShoulder = None
    LineRightOutsidePavement = None
    LineRightOutsideShoulder = None
    ReferenceLine = None
    TicksAtFullSuper = None
    TicksAtLevelCrown = None
    TicksAtNormalCrown = None
    TicksAtReverseCrown = None
    TicksAtShoulderBreakOver = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class SuperelevationViewStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SuperelevationViewStyle, type: SuperElevationViewDisplayStyleType) -> DisplayStyle """
        pass

    AxisBottomMajorTickInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisBottomMajorTickInterval(self: SuperelevationViewStyle) -> float

Set: AxisBottomMajorTickInterval(self: SuperelevationViewStyle) = value
"""

    AxisTopMajorTickInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AxisTopMajorTickInterval(self: SuperelevationViewStyle) -> float

Set: AxisTopMajorTickInterval(self: SuperelevationViewStyle) = value
"""

    UseFullHeightTick = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseFullHeightTick(self: SuperelevationViewStyle) -> bool

Set: UseFullHeightTick(self: SuperelevationViewStyle) = value
"""

    UseSmallTicksAtBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSmallTicksAtBottom(self: SuperelevationViewStyle) -> bool

Set: UseSmallTicksAtBottom(self: SuperelevationViewStyle) = value
"""

    UseSmallTicksAtMiddle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSmallTicksAtMiddle(self: SuperelevationViewStyle) -> bool

Set: UseSmallTicksAtMiddle(self: SuperelevationViewStyle) = value
"""

    UseSmallTicksAtTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSmallTicksAtTop(self: SuperelevationViewStyle) -> bool

Set: UseSmallTicksAtTop(self: SuperelevationViewStyle) = value
"""

    VerticalUnitHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VerticalUnitHeight(self: SuperelevationViewStyle) -> float

Set: VerticalUnitHeight(self: SuperelevationViewStyle) = value
"""



class SuperelevationViewStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SuperelevationViewStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SurfaceBaseStyle(CivilWrapper<AeccDbSurfaceStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    def GetDisplayModeAttributeId(self, *args): #cannot find CLR method
        """ GetDisplayModeAttributeId(self: SurfaceBaseStyle) -> UInt32 """
        pass

    def GetExaggerateElevationByAttributeId(self, *args): #cannot find CLR method
        """ GetExaggerateElevationByAttributeId(self: SurfaceBaseStyle) -> UInt32 """
        pass

    def GetFlattenToElevationByAttributeId(self, *args): #cannot find CLR method
        """ GetFlattenToElevationByAttributeId(self: SurfaceBaseStyle) -> UInt32 """
        pass

    DisplayMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayMode(self: SurfaceBaseStyle) -> SurfaceDisplay3dType

Set: DisplayMode(self: SurfaceBaseStyle) = value
"""

    ExaggerateElevationBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExaggerateElevationBy(self: SurfaceBaseStyle) -> float

Set: ExaggerateElevationBy(self: SurfaceBaseStyle) = value
"""

    FlattenToElevationBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlattenToElevationBy(self: SurfaceBaseStyle) -> float

Set: FlattenToElevationBy(self: SurfaceBaseStyle) = value
"""



class SurfaceBoundaryStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    DatumElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DatumElevation(self: SurfaceBoundaryStyle) -> float

Set: DatumElevation(self: SurfaceBoundaryStyle) = value
"""

    DisplayExteriorBoundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayExteriorBoundaries(self: SurfaceBoundaryStyle) -> bool

Set: DisplayExteriorBoundaries(self: SurfaceBoundaryStyle) = value
"""

    DisplayInteriorBoundaries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayInteriorBoundaries(self: SurfaceBoundaryStyle) -> bool

Set: DisplayInteriorBoundaries(self: SurfaceBoundaryStyle) = value
"""

    ProjectGridToDatum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectGridToDatum(self: SurfaceBoundaryStyle) -> bool

Set: ProjectGridToDatum(self: SurfaceBoundaryStyle) = value
"""

    UseDatum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseDatum(self: SurfaceBoundaryStyle) -> bool

Set: UseDatum(self: SurfaceBoundaryStyle) = value
"""



class SurfaceContourStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    def GetContourValues(self):
        """ GetContourValues(self: SurfaceContourStyle) -> Array[ContourValues] """
        pass

    def SetContourValues(self, contourValuesArray):
        """ SetContourValues(self: SurfaceContourStyle, contourValuesArray: Array[ContourValues]) """
        pass

    BaseElevationInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseElevationInterval(self: SurfaceContourStyle) -> float

Set: BaseElevationInterval(self: SurfaceContourStyle) = value
"""

    DepressionTickMarkInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepressionTickMarkInterval(self: SurfaceContourStyle) -> float

Set: DepressionTickMarkInterval(self: SurfaceContourStyle) = value
"""

    DepressionTickMarkLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepressionTickMarkLength(self: SurfaceContourStyle) -> float

Set: DepressionTickMarkLength(self: SurfaceContourStyle) = value
"""

    DisplayDepressions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayDepressions(self: SurfaceContourStyle) -> bool

Set: DisplayDepressions(self: SurfaceContourStyle) = value
"""

    GroupRangeValuesBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupRangeValuesBy(self: SurfaceContourStyle) -> SurfaceGroupValuesByType

Set: GroupRangeValuesBy(self: SurfaceContourStyle) = value
"""

    LegendStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleId(self: SurfaceContourStyle) -> ObjectId

Set: LegendStyleId(self: SurfaceContourStyle) = value
"""

    LegendStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleName(self: SurfaceContourStyle) -> str

Set: LegendStyleName(self: SurfaceContourStyle) = value
"""

    MajorContourColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorContourColorScheme(self: SurfaceContourStyle) -> ColorSchemeType

Set: MajorContourColorScheme(self: SurfaceContourStyle) = value
"""

    MajorContourInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MajorContourInterval(self: SurfaceContourStyle) -> float

Set: MajorContourInterval(self: SurfaceContourStyle) = value
"""

    MinorContourColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorContourColorScheme(self: SurfaceContourStyle) -> ColorSchemeType

Set: MinorContourColorScheme(self: SurfaceContourStyle) = value
"""

    MinorContourInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinorContourInterval(self: SurfaceContourStyle) -> float

Set: MinorContourInterval(self: SurfaceContourStyle) = value
"""

    NumberOfRanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRanges(self: SurfaceContourStyle) -> int

Set: NumberOfRanges(self: SurfaceContourStyle) = value
"""

    RangePrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangePrecision(self: SurfaceContourStyle) -> PrecisionRangeType

Set: RangePrecision(self: SurfaceContourStyle) = value
"""

    SmoothContours = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothContours(self: SurfaceContourStyle) -> bool

Set: SmoothContours(self: SurfaceContourStyle) = value
"""

    SmoothingFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothingFactor(self: SurfaceContourStyle) -> int

Set: SmoothingFactor(self: SurfaceContourStyle) = value
"""

    SmoothingType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SmoothingType(self: SurfaceContourStyle) -> ContourSmoothingType

Set: SmoothingType(self: SurfaceContourStyle) = value
"""

    UseColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseColorScheme(self: SurfaceContourStyle) -> bool

Set: UseColorScheme(self: SurfaceContourStyle) = value
"""



class SurfaceDirectionStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    ColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorScheme(self: SurfaceDirectionStyle) -> ColorSchemeType

Set: ColorScheme(self: SurfaceDirectionStyle) = value
"""

    DisplayEntityMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayEntityMode(self: SurfaceDirectionStyle) -> SurfaceDisplayType

Set: DisplayEntityMode(self: SurfaceDirectionStyle) = value
"""

    GroupValuesBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupValuesBy(self: SurfaceDirectionStyle) -> SurfaceGroupValuesByType

Set: GroupValuesBy(self: SurfaceDirectionStyle) = value
"""

    LegendStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleId(self: SurfaceDirectionStyle) -> ObjectId

Set: LegendStyleId(self: SurfaceDirectionStyle) = value
"""

    LegendStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleName(self: SurfaceDirectionStyle) -> str

Set: LegendStyleName(self: SurfaceDirectionStyle) = value
"""

    NumberOfRanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRanges(self: SurfaceDirectionStyle) -> int

Set: NumberOfRanges(self: SurfaceDirectionStyle) = value
"""

    RangePrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangePrecision(self: SurfaceDirectionStyle) -> PrecisionRangeType

Set: RangePrecision(self: SurfaceDirectionStyle) = value
"""



class SurfaceDisplay3dType(Enum):
    """ enum SurfaceDisplay3dType, values: ExaggerateElevations (4), FlattenElevations (2), UseSurfaceElevation (1) """
    ExaggerateElevations = None
    FlattenElevations = None
    UseSurfaceElevation = None
    value__ = None


class SurfaceDisplayStyleType(Enum):
    """ enum SurfaceDisplayStyleType, values: Boundary (2), Directions (7), Elevations (8), Gridded (6), MajorContour (3), MinorContour (4), Points (0), SlopeArrows (10), Slopes (9), Triangles (1), UserContours (5), Watersheds (11) """
    Boundary = None
    Directions = None
    Elevations = None
    Gridded = None
    MajorContour = None
    MinorContour = None
    Points = None
    SlopeArrows = None
    Slopes = None
    Triangles = None
    UserContours = None
    value__ = None
    Watersheds = None


class SurfaceDisplayType(Enum):
    """ enum SurfaceDisplayType, values: Faces3d (2), HatchSolid (4), PolyMesh (8), Solid2d (1) """
    Faces3d = None
    HatchSolid = None
    PolyMesh = None
    Solid2d = None
    value__ = None


class SurfaceElevationStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    ColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorScheme(self: SurfaceElevationStyle) -> ColorSchemeType

Set: ColorScheme(self: SurfaceElevationStyle) = value
"""

    CutScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CutScheme(self: SurfaceElevationStyle) -> ColorSchemeType

Set: CutScheme(self: SurfaceElevationStyle) = value
"""

    DataBandingMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataBandingMode(self: SurfaceElevationStyle) -> DataBandingType

Set: DataBandingMode(self: SurfaceElevationStyle) = value
"""

    DisplayEntityMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayEntityMode(self: SurfaceElevationStyle) -> SurfaceDisplayType

Set: DisplayEntityMode(self: SurfaceElevationStyle) = value
"""

    FillScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FillScheme(self: SurfaceElevationStyle) -> ColorSchemeType

Set: FillScheme(self: SurfaceElevationStyle) = value
"""

    GroupValuesBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupValuesBy(self: SurfaceElevationStyle) -> SurfaceGroupValuesByType

Set: GroupValuesBy(self: SurfaceElevationStyle) = value
"""

    IntervalLength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntervalLength(self: SurfaceElevationStyle) -> float

Set: IntervalLength(self: SurfaceElevationStyle) = value
"""

    LegendStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleId(self: SurfaceElevationStyle) -> ObjectId

Set: LegendStyleId(self: SurfaceElevationStyle) = value
"""

    LegendStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleName(self: SurfaceElevationStyle) -> str

Set: LegendStyleName(self: SurfaceElevationStyle) = value
"""

    NumberOfRanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRanges(self: SurfaceElevationStyle) -> int

Set: NumberOfRanges(self: SurfaceElevationStyle) = value
"""

    RangePrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangePrecision(self: SurfaceElevationStyle) -> PrecisionRangeType

Set: RangePrecision(self: SurfaceElevationStyle) = value
"""



class SurfaceGridStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    PrimaryGridInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryGridInterval(self: SurfaceGridStyle) -> float

Set: PrimaryGridInterval(self: SurfaceGridStyle) = value
"""

    PrimaryGridOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryGridOrientation(self: SurfaceGridStyle) -> float

Set: PrimaryGridOrientation(self: SurfaceGridStyle) = value
"""

    SecondaryGridInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryGridInterval(self: SurfaceGridStyle) -> float

Set: SecondaryGridInterval(self: SurfaceGridStyle) = value
"""

    SecondaryGridOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryGridOrientation(self: SurfaceGridStyle) -> float

Set: SecondaryGridOrientation(self: SurfaceGridStyle) = value
"""

    UsePrimaryGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UsePrimaryGrid(self: SurfaceGridStyle) -> bool

Set: UsePrimaryGrid(self: SurfaceGridStyle) = value
"""

    UseSecondaryGrid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseSecondaryGrid(self: SurfaceGridStyle) -> bool

Set: UseSecondaryGrid(self: SurfaceGridStyle) = value
"""



class SurfaceGroupValuesByType(Enum):
    """ enum SurfaceGroupValuesByType, values: EqualInterval (0), Quantile (1), StandardDeviation (2) """
    EqualInterval = None
    Quantile = None
    StandardDeviation = None
    value__ = None


class SurfaceHatchInfo(object):
    # no doc
    def SetHatchPattern(self, patternType, patternName):
        """ SetHatchPattern(self: SurfaceHatchInfo, patternType: HatchPatternType, patternName: str) """
        pass

    PatternAngle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternAngle(self: SurfaceHatchInfo) -> float

Set: PatternAngle(self: SurfaceHatchInfo) = value
"""

    PatternDouble = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternDouble(self: SurfaceHatchInfo) -> bool

Set: PatternDouble(self: SurfaceHatchInfo) = value
"""

    PatternName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternName(self: SurfaceHatchInfo) -> str

"""

    PatternScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternScale(self: SurfaceHatchInfo) -> float

Set: PatternScale(self: SurfaceHatchInfo) = value
"""

    PatternScaleType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternScaleType(self: SurfaceHatchInfo) -> bool

"""

    PatternSpace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternSpace(self: SurfaceHatchInfo) -> float

Set: PatternSpace(self: SurfaceHatchInfo) = value
"""

    PatternType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PatternType(self: SurfaceHatchInfo) -> HatchPatternType

"""



class SurfacePointStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    DataPointsColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataPointsColor(self: SurfacePointStyle) -> Color

Set: DataPointsColor(self: SurfacePointStyle) = value
"""

    DataPointsSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataPointsSymbol(self: SurfacePointStyle) -> PointSymbolType

Set: DataPointsSymbol(self: SurfacePointStyle) = value
"""

    DerivedPointsColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DerivedPointsColor(self: SurfacePointStyle) -> Color

Set: DerivedPointsColor(self: SurfacePointStyle) = value
"""

    DerivedPointsSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DerivedPointsSymbol(self: SurfacePointStyle) -> PointSymbolType

Set: DerivedPointsSymbol(self: SurfacePointStyle) = value
"""

    NondestructivePointsColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NondestructivePointsColor(self: SurfacePointStyle) -> Color

Set: NondestructivePointsColor(self: SurfacePointStyle) = value
"""

    NondestructivePointsSymbol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NondestructivePointsSymbol(self: SurfacePointStyle) -> PointSymbolType

Set: NondestructivePointsSymbol(self: SurfacePointStyle) = value
"""

    ScalingMethodType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScalingMethodType(self: SurfacePointStyle) -> ScaleType

Set: ScalingMethodType(self: SurfacePointStyle) = value
"""

    Units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Units(self: SurfacePointStyle) -> float

Set: Units(self: SurfacePointStyle) = value
"""



class SurfaceSlopeArrowStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    ArrowScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowScale(self: SurfaceSlopeArrowStyle) -> float

Set: ArrowScale(self: SurfaceSlopeArrowStyle) = value
"""

    ArrowType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArrowType(self: SurfaceSlopeArrowStyle) -> SlopeArrowType

Set: ArrowType(self: SurfaceSlopeArrowStyle) = value
"""

    ColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorScheme(self: SurfaceSlopeArrowStyle) -> ColorSchemeType

Set: ColorScheme(self: SurfaceSlopeArrowStyle) = value
"""

    GroupValuesBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupValuesBy(self: SurfaceSlopeArrowStyle) -> SurfaceGroupValuesByType

Set: GroupValuesBy(self: SurfaceSlopeArrowStyle) = value
"""

    LegendStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleId(self: SurfaceSlopeArrowStyle) -> ObjectId

Set: LegendStyleId(self: SurfaceSlopeArrowStyle) = value
"""

    LegendStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleName(self: SurfaceSlopeArrowStyle) -> str

Set: LegendStyleName(self: SurfaceSlopeArrowStyle) = value
"""

    NumberOfRanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRanges(self: SurfaceSlopeArrowStyle) -> int

Set: NumberOfRanges(self: SurfaceSlopeArrowStyle) = value
"""

    RangePrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangePrecision(self: SurfaceSlopeArrowStyle) -> PrecisionRangeType

Set: RangePrecision(self: SurfaceSlopeArrowStyle) = value
"""



class SurfaceSlopeStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    ColorScheme = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColorScheme(self: SurfaceSlopeStyle) -> ColorSchemeType

Set: ColorScheme(self: SurfaceSlopeStyle) = value
"""

    DisplayEntityMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayEntityMode(self: SurfaceSlopeStyle) -> SurfaceDisplayType

Set: DisplayEntityMode(self: SurfaceSlopeStyle) = value
"""

    GroupValuesBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupValuesBy(self: SurfaceSlopeStyle) -> SurfaceGroupValuesByType

Set: GroupValuesBy(self: SurfaceSlopeStyle) = value
"""

    LegendStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleId(self: SurfaceSlopeStyle) -> ObjectId

Set: LegendStyleId(self: SurfaceSlopeStyle) = value
"""

    LegendStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleName(self: SurfaceSlopeStyle) -> str

Set: LegendStyleName(self: SurfaceSlopeStyle) = value
"""

    NumberOfRanges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NumberOfRanges(self: SurfaceSlopeStyle) -> int

Set: NumberOfRanges(self: SurfaceSlopeStyle) = value
"""

    RangePrecision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RangePrecision(self: SurfaceSlopeStyle) -> PrecisionRangeType

Set: RangePrecision(self: SurfaceSlopeStyle) = value
"""



class SurfaceStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: SurfaceStyle, type: SurfaceDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SurfaceStyle, type: SurfaceDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self):
        """ GetDisplayStyleSection(self: SurfaceStyle) -> DisplayStyle """
        pass

    BoundaryStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryStyle(self: SurfaceStyle) -> SurfaceBoundaryStyle

"""

    ContourStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContourStyle(self: SurfaceStyle) -> SurfaceContourStyle

"""

    DirectionStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DirectionStyle(self: SurfaceStyle) -> SurfaceDirectionStyle

"""

    ElevationStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElevationStyle(self: SurfaceStyle) -> SurfaceElevationStyle

"""

    GridStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GridStyle(self: SurfaceStyle) -> SurfaceGridStyle

"""

    PointStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointStyle(self: SurfaceStyle) -> SurfacePointStyle

"""

    SlopeArrowStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeArrowStyle(self: SurfaceStyle) -> SurfaceSlopeArrowStyle

"""

    SlopeStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SlopeStyle(self: SurfaceStyle) -> SurfaceSlopeStyle

"""

    TriangleStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TriangleStyle(self: SurfaceStyle) -> SurfaceTriangleStyle

"""

    WatershedStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WatershedStyle(self: SurfaceStyle) -> SurfaceWatershedStyle

"""



class SurfaceStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SurfaceStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SurfaceTriangleStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass


class SurfaceWatershedStyle(SurfaceBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    BoundaryPointStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundaryPointStyle(self: SurfaceWatershedStyle) -> WatershedBoundaryPointStyle

"""

    BoundarySegmentStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BoundarySegmentStyle(self: SurfaceWatershedStyle) -> WatershedBoundarySegmentStyle

"""

    DepressionStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DepressionStyle(self: SurfaceWatershedStyle) -> WatershedDepressionStyle

"""

    FlatAreaStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlatAreaStyle(self: SurfaceWatershedStyle) -> WatershedFlatAreaStyle

"""

    LabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleId(self: SurfaceWatershedStyle) -> ObjectId

Set: LabelStyleId(self: SurfaceWatershedStyle) = value
"""

    LabelStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelStyleName(self: SurfaceWatershedStyle) -> str

Set: LabelStyleName(self: SurfaceWatershedStyle) = value
"""

    LegendStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleId(self: SurfaceWatershedStyle) -> ObjectId

Set: LegendStyleId(self: SurfaceWatershedStyle) = value
"""

    LegendStyleName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendStyleName(self: SurfaceWatershedStyle) -> str

Set: LegendStyleName(self: SurfaceWatershedStyle) = value
"""

    MultipleDrainNotchStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultipleDrainNotchStyle(self: SurfaceWatershedStyle) -> WatershedMultipleDrainNotchStyle

"""

    MultipleDrainStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MultipleDrainStyle(self: SurfaceWatershedStyle) -> WatershedMultipleDrainStyle

"""

    PointScalingMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointScalingMethod(self: SurfaceWatershedStyle) -> ScalingMethodType

Set: PointScalingMethod(self: SurfaceWatershedStyle) = value
"""

    PointUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointUnits(self: SurfaceWatershedStyle) -> float

Set: PointUnits(self: SurfaceWatershedStyle) = value
"""



class SurveyElevationDisplayType(Enum):
    """ enum SurveyElevationDisplayType, values: ExaggerateElevations (2), FlattenElevation (1), UseElevation (0) """
    ExaggerateElevations = None
    FlattenElevation = None
    UseElevation = None
    value__ = None


class SurveyFigureDisplayType(Enum):
    """ enum SurveyFigureDisplayType, values: AdditionalMarkers (4), EndpointMarkers (3), FigureLines (0), MidpointMarkers (2), VertexMarkers (1) """
    AdditionalMarkers = None
    EndpointMarkers = None
    FigureLines = None
    MidpointMarkers = None
    value__ = None
    VertexMarkers = None


class SurveyFigureMarkerPlacementType(Enum):
    """ enum SurveyFigureMarkerPlacementType, values: AtInterval (1), Continuous (3), DivideFigure (2), None (0) """
    AtInterval = None
    Continuous = None
    DivideFigure = None
    None = None
    value__ = None


class SurveyFigureProfileDisplayType(Enum):
    """ enum SurveyFigureProfileDisplayType, values: BeginningVertexMarker (6), EndingVertexMarker (8), FigureLines (0), InternalVertexMarker (7) """
    BeginningVertexMarker = None
    EndingVertexMarker = None
    FigureLines = None
    InternalVertexMarker = None
    value__ = None


class SurveyFigureSectionDisplayType(Enum):
    """ enum SurveyFigureSectionDisplayType, values: CrossingMarker (5) """
    CrossingMarker = None
    value__ = None


class SurveyFigureStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, displayType):
        """ GetDisplayStyleModel(self: SurveyFigureStyle, displayType: SurveyFigureDisplayType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, displayType):
        """ GetDisplayStylePlan(self: SurveyFigureStyle, displayType: SurveyFigureDisplayType) -> DisplayStyle """
        pass

    def GetDisplayStyleProfile(self, displayType):
        """ GetDisplayStyleProfile(self: SurveyFigureStyle, displayType: SurveyFigureProfileDisplayType) -> DisplayStyle """
        pass

    def GetDisplayStyleSection(self, displayType):
        """ GetDisplayStyleSection(self: SurveyFigureStyle, displayType: SurveyFigureSectionDisplayType) -> DisplayStyle """
        pass

    AdditionalMarkerDivideFigureBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdditionalMarkerDivideFigureBy(self: SurveyFigureStyle) -> int

Set: AdditionalMarkerDivideFigureBy(self: SurveyFigureStyle) = value
"""

    AdditionalMarkerInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdditionalMarkerInterval(self: SurveyFigureStyle) -> float

Set: AdditionalMarkerInterval(self: SurveyFigureStyle) = value
"""

    AdditionalMarkerPlacementMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdditionalMarkerPlacementMethod(self: SurveyFigureStyle) -> SurveyFigureMarkerPlacementType

Set: AdditionalMarkerPlacementMethod(self: SurveyFigureStyle) = value
"""

    AdditionalMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdditionalMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: AdditionalMarkerStyleId(self: SurveyFigureStyle) = value
"""

    AlignAdditionalMarkersWithFigure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignAdditionalMarkersWithFigure(self: SurveyFigureStyle) -> bool

Set: AlignAdditionalMarkersWithFigure(self: SurveyFigureStyle) = value
"""

    AlignEndpointMarkersWithFigure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignEndpointMarkersWithFigure(self: SurveyFigureStyle) -> bool

Set: AlignEndpointMarkersWithFigure(self: SurveyFigureStyle) = value
"""

    AlignMidpointMarkersWithFigure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignMidpointMarkersWithFigure(self: SurveyFigureStyle) -> bool

Set: AlignMidpointMarkersWithFigure(self: SurveyFigureStyle) = value
"""

    AlignVertexMarkersWithFigure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignVertexMarkersWithFigure(self: SurveyFigureStyle) -> bool

Set: AlignVertexMarkersWithFigure(self: SurveyFigureStyle) = value
"""

    BeginningVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BeginningVertexMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: BeginningVertexMarkerStyleId(self: SurveyFigureStyle) = value
"""

    CrossingMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrossingMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: CrossingMarkerStyleId(self: SurveyFigureStyle) = value
"""

    EndingVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndingVertexMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: EndingVertexMarkerStyleId(self: SurveyFigureStyle) = value
"""

    EndPointMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPointMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: EndPointMarkerStyleId(self: SurveyFigureStyle) = value
"""

    ExaggerateElevationBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExaggerateElevationBy(self: SurveyFigureStyle) -> float

Set: ExaggerateElevationBy(self: SurveyFigureStyle) = value
"""

    FlattenToElevationBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlattenToElevationBy(self: SurveyFigureStyle) -> float

Set: FlattenToElevationBy(self: SurveyFigureStyle) = value
"""

    InternalVertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InternalVertexMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: InternalVertexMarkerStyleId(self: SurveyFigureStyle) = value
"""

    MidpointMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MidpointMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: MidpointMarkerStyleId(self: SurveyFigureStyle) = value
"""

    NetworkDisplayMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetworkDisplayMode(self: SurveyFigureStyle) -> SurveyElevationDisplayType

Set: NetworkDisplayMode(self: SurveyFigureStyle) = value
"""

    PlaceAdditionalMarkerAtFigureEndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaceAdditionalMarkerAtFigureEndPoint(self: SurveyFigureStyle) -> bool

Set: PlaceAdditionalMarkerAtFigureEndPoint(self: SurveyFigureStyle) = value
"""

    PlaceAdditionalMarkerAtFigureStartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlaceAdditionalMarkerAtFigureStartPoint(self: SurveyFigureStyle) -> bool

Set: PlaceAdditionalMarkerAtFigureStartPoint(self: SurveyFigureStyle) = value
"""

    StartPointMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPointMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: StartPointMarkerStyleId(self: SurveyFigureStyle) = value
"""

    VertexMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VertexMarkerStyleId(self: SurveyFigureStyle) -> ObjectId

Set: VertexMarkerStyleId(self: SurveyFigureStyle) = value
"""



class SurveyFigureStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SurveyFigureStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class SurveyNetworkDisplayStyleType(Enum):
    """ enum SurveyNetworkDisplayStyleType, values: DirectionLines (5), ErrorEllipses (7), KnownControlPoints (0), NetworkLines (4), NonControlPoints (2), SideshotLines (6), SideshotPoints (3), ToleranceErrorLines (9), ToleranceErrorPoints (8), UnknownControlPoints (1) """
    DirectionLines = None
    ErrorEllipses = None
    KnownControlPoints = None
    NetworkLines = None
    NonControlPoints = None
    SideshotLines = None
    SideshotPoints = None
    ToleranceErrorLines = None
    ToleranceErrorPoints = None
    UnknownControlPoints = None
    value__ = None


class SurveyNetworkStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: SurveyNetworkStyle, type: SurveyNetworkDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: SurveyNetworkStyle, type: SurveyNetworkDisplayStyleType) -> DisplayStyle """
        pass

    ErrorEllipseScaleFactor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorEllipseScaleFactor(self: SurveyNetworkStyle) -> float

Set: ErrorEllipseScaleFactor(self: SurveyNetworkStyle) = value
"""

    ExaggerateElevationBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExaggerateElevationBy(self: SurveyNetworkStyle) -> float

Set: ExaggerateElevationBy(self: SurveyNetworkStyle) = value
"""

    FlattenToElevationBy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FlattenToElevationBy(self: SurveyNetworkStyle) -> float

Set: FlattenToElevationBy(self: SurveyNetworkStyle) = value
"""

    KnownControlPointsMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KnownControlPointsMarkerStyleId(self: SurveyNetworkStyle) -> ObjectId

Set: KnownControlPointsMarkerStyleId(self: SurveyNetworkStyle) = value
"""

    NetworkDisplayMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetworkDisplayMode(self: SurveyNetworkStyle) -> SurveyElevationDisplayType

Set: NetworkDisplayMode(self: SurveyNetworkStyle) = value
"""

    NonControlPointsMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NonControlPointsMarkerStyleId(self: SurveyNetworkStyle) -> ObjectId

Set: NonControlPointsMarkerStyleId(self: SurveyNetworkStyle) = value
"""

    SideshotPointsMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SideshotPointsMarkerStyleId(self: SurveyNetworkStyle) -> ObjectId

Set: SideshotPointsMarkerStyleId(self: SurveyNetworkStyle) = value
"""

    ToleranceErrorPointsMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ToleranceErrorPointsMarkerStyleId(self: SurveyNetworkStyle) -> ObjectId

Set: ToleranceErrorPointsMarkerStyleId(self: SurveyNetworkStyle) = value
"""

    UnknownControlPointsMarkerStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnknownControlPointsMarkerStyleId(self: SurveyNetworkStyle) -> ObjectId

Set: UnknownControlPointsMarkerStyleId(self: SurveyNetworkStyle) = value
"""



class SurveyNetworkStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: SurveyNetworkStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class TableDisplayStyleType(Enum):
    """ enum TableDisplayStyleType, values: Border (0), DataAreaFill (7), DataDivider (4), DataSeparator (3), DataText (10), HeaderAreaFill (6), HeaderSeparator (2), HeaderText (9), TitleAreaFill (5), TitleSeparator (1), TitleText (8) """
    Border = None
    DataAreaFill = None
    DataDivider = None
    DataSeparator = None
    DataText = None
    HeaderAreaFill = None
    HeaderSeparator = None
    HeaderText = None
    TitleAreaFill = None
    TitleSeparator = None
    TitleText = None
    value__ = None


class TableSortingOrderType(Enum):
    """ enum TableSortingOrderType, values: Ascending (1), Descending (0) """
    Ascending = None
    Descending = None
    value__ = None


class TableStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStyleModel(self, type):
        """ GetDisplayStyleModel(self: TableStyle, type: TableDisplayStyleType) -> DisplayStyle """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: TableStyle, type: TableDisplayStyleType) -> DisplayStyle """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    BorderDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BorderDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    BorderDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BorderDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    ColumnStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnStyles(self: TableStyle) -> ColumnStyleCollection

"""

    DataAreaFillDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataAreaFillDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    DataAreaFillDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataAreaFillDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    DataDividerDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataDividerDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    DataDividerDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataDividerDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    DataSeparatorDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataSeparatorDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    DataSeparatorDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataSeparatorDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    DataTextDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTextDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    DataTextDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTextDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    DataTextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTextHeight(self: TableStyle) -> float

Set: DataTextHeight(self: TableStyle) = value
"""

    DataTextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataTextStyle(self: TableStyle) -> str

Set: DataTextStyle(self: TableStyle) = value
"""

    EnableWordWrapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableWordWrapping(self: TableStyle) -> bool

Set: EnableWordWrapping(self: TableStyle) = value
"""

    HeaderAreaFillDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderAreaFillDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    HeaderAreaFillDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderAreaFillDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    HeaderSeparatorDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderSeparatorDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    HeaderSeparatorDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderSeparatorDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    HeaderTextDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderTextDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    HeaderTextDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderTextDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    HeaderTextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderTextHeight(self: TableStyle) -> float

Set: HeaderTextHeight(self: TableStyle) = value
"""

    HeaderTextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HeaderTextStyle(self: TableStyle) -> str

Set: HeaderTextStyle(self: TableStyle) = value
"""

    MaintainViewOrientation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaintainViewOrientation(self: TableStyle) -> bool

Set: MaintainViewOrientation(self: TableStyle) = value
"""

    RepeatHeaderInSplitTables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RepeatHeaderInSplitTables(self: TableStyle) -> bool

Set: RepeatHeaderInSplitTables(self: TableStyle) = value
"""

    RepeatTitleInSplitTables = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RepeatTitleInSplitTables(self: TableStyle) -> bool

Set: RepeatTitleInSplitTables(self: TableStyle) = value
"""

    SortData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortData(self: TableStyle) -> bool

Set: SortData(self: TableStyle) = value
"""

    SortingColumn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortingColumn(self: TableStyle) -> int

Set: SortingColumn(self: TableStyle) = value
"""

    SortingOrder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SortingOrder(self: TableStyle) -> TableSortingOrderType

Set: SortingOrder(self: TableStyle) = value
"""

    TableType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableType(self: TableStyle) -> TableStyleType

"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: TableStyle) -> str

Set: Title(self: TableStyle) = value
"""

    TitleAreaFillDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleAreaFillDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    TitleAreaFillDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleAreaFillDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    TitleJustification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleJustification(self: TableStyle) -> TextJustificationType

Set: TitleJustification(self: TableStyle) = value
"""

    TitleSeparatorDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleSeparatorDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    TitleSeparatorDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleSeparatorDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    TitleTextDisplayStyleModel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextDisplayStyleModel(self: TableStyle) -> DisplayStyle

"""

    TitleTextDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextDisplayStylePlan(self: TableStyle) -> DisplayStyle

"""

    TitleTextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextHeight(self: TableStyle) -> float

Set: TitleTextHeight(self: TableStyle) = value
"""

    TitleTextStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextStyle(self: TableStyle) -> str

Set: TitleTextStyle(self: TableStyle) = value
"""

    TitleUnformatted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleUnformatted(self: TableStyle) -> str

Set: TitleUnformatted(self: TableStyle) = value
"""

    TransposeSectionViewTable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransposeSectionViewTable(self: TableStyle) -> bool

Set: TransposeSectionViewTable(self: TableStyle) = value
"""



class TableStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: TableStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class TableStylesRoot(TreeOidWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AlignmentCurveTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentCurveTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    AlignmentLineTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentLineTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    AlignmentSegmentTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentSegmentTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    AlignmentSpiralTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AlignmentSpiralTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    ParcelAreaTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParcelAreaTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    ParcelCurveTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParcelCurveTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    ParcelLineTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParcelLineTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    ParcelSegmentTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ParcelSegmentTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    PipeTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PipeTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    PointTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    QuantityTakeoffMaterialTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityTakeoffMaterialTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    QuantityTakeoffTotalVolumeTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QuantityTakeoffTotalVolumeTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SectionViewMaterialTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewMaterialTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SectionViewTotalVolumeTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SectionViewTotalVolumeTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    StructureTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StructureTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SurfaceContourTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceContourTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SurfaceDirectionTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceDirectionTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SurfaceElevationTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceElevationTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SurfaceSlopeArrowContourTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceSlopeArrowContourTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SurfaceSlopeTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceSlopeTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SurfaceUserDefinedContourTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceUserDefinedContourTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""

    SurfaceWatershedTableStyles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SurfaceWatershedTableStyles(self: TableStylesRoot) -> TableStyleCollection

"""



class TableStylesRootPressurePipesExtension(object):
    # no doc
    @staticmethod
    def GetPressureAppurtenanceTableStyles(tableStylesRoot):
        """ GetPressureAppurtenanceTableStyles(tableStylesRoot: TableStylesRoot) -> TableStyleCollection """
        pass

    @staticmethod
    def GetPressureFittingTableStyles(tableStylesRoot):
        """ GetPressureFittingTableStyles(tableStylesRoot: TableStylesRoot) -> TableStyleCollection """
        pass

    @staticmethod
    def GetPressurePipeTableStyles(tableStylesRoot):
        """ GetPressurePipeTableStyles(tableStylesRoot: TableStylesRoot) -> TableStyleCollection """
        pass

    __all__ = [
        'GetPressureAppurtenanceTableStyles',
        'GetPressureFittingTableStyles',
        'GetPressurePipeTableStyles',
    ]


class TableStyleType(Enum):
    """ enum TableStyleType, values: AlignmentCurve (133), AlignmentLine (132), AlignmentSegment (37), AlignmentSpiral (134), ParcelArea (2), ParcelCurve (8), ParcelLine (7), ParcelSegment (131), Pipe (332), Point (6), QuantityTakeoffMaterial (3778), QuantityTakeoffTotalVolume (3777), SectionViewMaterial (334), SectionViewTotalVolume (333), Structure (335), SurfaceContour (91), SurfaceContoursUser (3081), SurfaceDirection (41), SurfaceElevation (42), SurfaceSlope (43), SurfaceSlopeArrow (44), SurfaceWatershed (3083) """
    AlignmentCurve = None
    AlignmentLine = None
    AlignmentSegment = None
    AlignmentSpiral = None
    ParcelArea = None
    ParcelCurve = None
    ParcelLine = None
    ParcelSegment = None
    Pipe = None
    Point = None
    QuantityTakeoffMaterial = None
    QuantityTakeoffTotalVolume = None
    SectionViewMaterial = None
    SectionViewTotalVolume = None
    Structure = None
    SurfaceContour = None
    SurfaceContoursUser = None
    SurfaceDirection = None
    SurfaceElevation = None
    SurfaceSlope = None
    SurfaceSlopeArrow = None
    SurfaceWatershed = None
    value__ = None


class TextForEachComponentSelectedType(Enum):
    """ enum TextForEachComponentSelectedType, values: Curve (419485521), CurveOrSpiral (419485522), IntersectionAllAlignment (419930112), Spiral (419485523), StructureAllPipes (419811620), StructureInFlowPipes (419811621), StructureOutFlowPipes (419811622) """
    Curve = None
    CurveOrSpiral = None
    IntersectionAllAlignment = None
    Spiral = None
    StructureAllPipes = None
    StructureInFlowPipes = None
    StructureOutFlowPipes = None
    value__ = None


class VerticalGeometryBandStyle(BandStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetDisplayStylePlan(self, type):
        """ GetDisplayStylePlan(self: VerticalGeometryBandStyle, type: VerticalGeometryDisplayStyleType) -> DisplayStyle """
        pass

    BandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BandType(self: VerticalGeometryBandStyle) -> BandType

"""

    CrestCurveLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrestCurveLabelStyleId(self: VerticalGeometryBandStyle) -> ObjectId

"""

    CrestCurveTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CrestCurveTickStyle(self: VerticalGeometryBandStyle) -> BandTickStyle

"""

    DownhillTangentLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownhillTangentLabelStyleId(self: VerticalGeometryBandStyle) -> ObjectId

"""

    DownhillTangentTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DownhillTangentTickStyle(self: VerticalGeometryBandStyle) -> BandTickStyle

"""

    LabelOnlyTangents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LabelOnlyTangents(self: VerticalGeometryBandStyle) -> bool

Set: LabelOnlyTangents(self: VerticalGeometryBandStyle) = value
"""

    SagCurveLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SagCurveLabelStyleId(self: VerticalGeometryBandStyle) -> ObjectId

"""

    SagCurveTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SagCurveTickStyle(self: VerticalGeometryBandStyle) -> BandTickStyle

"""

    TitleTextLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TitleTextLabelStyleId(self: VerticalGeometryBandStyle) -> ObjectId

"""

    UphillTangentLabelStyleId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UphillTangentLabelStyleId(self: VerticalGeometryBandStyle) -> ObjectId

"""

    UphillTangentTickStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UphillTangentTickStyle(self: VerticalGeometryBandStyle) -> BandTickStyle

"""



class VerticalGeometryDisplayStyleType(Enum):
    """ enum VerticalGeometryDisplayStyleType, values: Border (0), CurveGeometry (7), CurveLabels (5), TangentGeometry (6), TangentLabels (4), Ticks (3), TitleBox (1), TitleBoxText (2) """
    Border = None
    CurveGeometry = None
    CurveLabels = None
    TangentGeometry = None
    TangentLabels = None
    Ticks = None
    TitleBox = None
    TitleBoxText = None
    value__ = None


class ViewFrameStyle(StyleBase):
    # no doc
    def Dispose(self):
        """ Dispose(self: DBObject, A_0: bool) """
        pass

    def GetViewFrameBoundaryDisplayStylePlan(self):
        """ GetViewFrameBoundaryDisplayStylePlan(self: ViewFrameStyle) -> DisplayStyle """
        pass

    ViewFrameBoundaryDisplayStylePlan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewFrameBoundaryDisplayStylePlan(self: ViewFrameStyle) -> DisplayStyle

"""



class ViewFrameStyleCollection(StyleCollectionBase):
    # no doc
    def Add(self, name):
        """ Add(self: ViewFrameStyleCollection, name: str) -> ObjectId """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass


class WatershedBaseStyle(CivilWrapper<AeccDbSurfaceStyle>):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: WatershedBaseStyle) -> Color

Set: Color(self: WatershedBaseStyle) = value
"""

    Hatch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hatch(self: WatershedBaseStyle) -> SurfaceHatchInfo

"""

    HatchPattern = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HatchPattern(self: WatershedBaseStyle) -> str

Set: HatchPattern(self: WatershedBaseStyle) = value
"""

    LinetypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeId(self: WatershedBaseStyle) -> ObjectId

Set: LinetypeId(self: WatershedBaseStyle) = value
"""

    LinetypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinetypeName(self: WatershedBaseStyle) -> str

Set: LinetypeName(self: WatershedBaseStyle) = value
"""

    UseHatching = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UseHatching(self: WatershedBaseStyle) -> bool

Set: UseHatching(self: WatershedBaseStyle) = value
"""



class WatershedDrainPointStyle(WatershedBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    DrawDrainPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawDrainPoint(self: WatershedDrainPointStyle) -> bool

Set: DrawDrainPoint(self: WatershedDrainPointStyle) = value
"""

    PointColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointColor(self: WatershedDrainPointStyle) -> Color

Set: PointColor(self: WatershedDrainPointStyle) = value
"""

    PointDisplayType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointDisplayType(self: WatershedDrainPointStyle) -> PointSymbolType

Set: PointDisplayType(self: WatershedDrainPointStyle) = value
"""



class WatershedBoundaryPointStyle(WatershedDrainPointStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass


class WatershedDrainSegmentStyle(WatershedBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    DrawDrainSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawDrainSegment(self: WatershedDrainSegmentStyle) -> bool

Set: DrawDrainSegment(self: WatershedDrainSegmentStyle) = value
"""

    SegmentColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentColor(self: WatershedDrainSegmentStyle) -> Color

Set: SegmentColor(self: WatershedDrainSegmentStyle) = value
"""

    SegmentLinetypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLinetypeId(self: WatershedDrainSegmentStyle) -> ObjectId

Set: SegmentLinetypeId(self: WatershedDrainSegmentStyle) = value
"""

    SegmentLinetypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLinetypeName(self: WatershedDrainSegmentStyle) -> str

Set: SegmentLinetypeName(self: WatershedDrainSegmentStyle) = value
"""



class WatershedBoundarySegmentStyle(WatershedDrainSegmentStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass


class WatershedDrainPointSegmentStyle(WatershedBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass

    DrawDrainPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawDrainPoint(self: WatershedDrainPointSegmentStyle) -> bool

Set: DrawDrainPoint(self: WatershedDrainPointSegmentStyle) = value
"""

    DrawDrainSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawDrainSegment(self: WatershedDrainPointSegmentStyle) -> bool

Set: DrawDrainSegment(self: WatershedDrainPointSegmentStyle) = value
"""

    PointColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointColor(self: WatershedDrainPointSegmentStyle) -> Color

Set: PointColor(self: WatershedDrainPointSegmentStyle) = value
"""

    PointDisplayType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointDisplayType(self: WatershedDrainPointSegmentStyle) -> PointSymbolType

Set: PointDisplayType(self: WatershedDrainPointSegmentStyle) = value
"""

    SegmentColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentColor(self: WatershedDrainPointSegmentStyle) -> Color

Set: SegmentColor(self: WatershedDrainPointSegmentStyle) = value
"""

    SegmentLinetypeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLinetypeId(self: WatershedDrainPointSegmentStyle) -> ObjectId

Set: SegmentLinetypeId(self: WatershedDrainPointSegmentStyle) = value
"""

    SegmentLinetypeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SegmentLinetypeName(self: WatershedDrainPointSegmentStyle) -> str

Set: SegmentLinetypeName(self: WatershedDrainPointSegmentStyle) = value
"""



class WatershedDepressionStyle(WatershedDrainPointSegmentStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass


class WatershedFlatAreaStyle(WatershedBaseStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass


class WatershedMultipleDrainNotchStyle(WatershedDrainSegmentStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass


class WatershedMultipleDrainStyle(WatershedDrainPointStyle):
    # no doc
    def Dispose(self):
        """ Dispose(self: CivilWrapper<AeccDbSurfaceStyle>, A_0: bool) """
        pass


