# encoding: utf-8
# module Autodesk.Gis.Map.Platform.Utils calls itself Utils
# from Autodesk.Map.Platform.Utils, Version=24.0.30.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ConfigDocument(object):
    """
    ConfigDocument()
    ConfigDocument(defaultSchemaName: str)
    """
    def AddClass(self, *args): #cannot find CLR method
        """ AddClass(self: ConfigDocument, fdoClassDefintion: ClassDefinition) """
        pass

    def CreateClass(self, *args): #cannot find CLR method
        """ CreateClass(self: ConfigDocument, rasterItem: RasterItem) -> ClassDefinition """
        pass

    def IndexOfSchemaCollection(self, *args): #cannot find CLR method
        """ IndexOfSchemaCollection(self: ConfigDocument, name: str) -> int """
        pass

    def IndexOfSpatailContextCollection(self, *args): #cannot find CLR method
        """ IndexOfSpatailContextCollection(self: ConfigDocument, name: str) -> int """
        pass

    def IsValidRasterItem(self, *args): #cannot find CLR method
        """ IsValidRasterItem(self: ConfigDocument, rasterItem: RasterItem) -> bool """
        pass

    def ToXML(self):
        """ ToXML(self: ConfigDocument) -> Array[Byte] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, defaultSchemaName=None):
        """
        __new__(cls: type)
        __new__(cls: type, defaultSchemaName: str)
        """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: ConfigDocument) -> bool

"""

    SchemaMappings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SchemaMappings(self: ConfigDocument) -> PhysicalSchemaMappingCollection

Set: SchemaMappings(self: ConfigDocument) = value
"""

    Schemas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Schemas(self: ConfigDocument) -> FeatureSchemaCollection

Set: Schemas(self: ConfigDocument) = value
"""

    SpatailContexts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatailContexts(self: ConfigDocument) -> List[SpatialContextInfo]

Set: SpatailContexts(self: ConfigDocument) = value
"""


    defaultSchemaNameField = None


class Features(DataTable):
    """
    Features()
    Features(classDef: MgClassDefinition, features: MgBatchPropertyCollection, layer: MgLayerBase)
    """
    def Dispose(self):
        """ Dispose(self: MarshalByValueComponent, disposing: bool) """
        pass

    @staticmethod
    def GetFeatures(classDef, reader):
        """ GetFeatures(classDef: MgClassDefinition, reader: MgFeatureReader) -> MgBatchPropertyCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, classDef=None, features=None, layer=None):
        """
        __new__(cls: type)
        __new__(cls: type, classDef: MgClassDefinition, features: MgBatchPropertyCollection, layer: MgLayerBase)
        """
        pass

    ClassDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassDefinition(self: Features) -> MgClassDefinition

Set: ClassDefinition(self: Features) = value
"""

    Events = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    FeatureData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureData(self: Features) -> MgBatchPropertyCollection

Set: FeatureData(self: Features) = value
"""

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: Features) -> MgLayerBase

Set: Layer(self: Features) = value
"""


    fInitInProgress = None


class OdbcConfigDocument(ConfigDocument):
    """ OdbcConfigDocument() """
    def AddOverrideInfo(self, schemaName, classDef, spatialContextName, xColumnName, yColumnName, zColumnName):
        """ AddOverrideInfo(self: OdbcConfigDocument, schemaName: str, classDef: ClassDefinition, spatialContextName: str, xColumnName: str, yColumnName: str, zColumnName: str) """
        pass

    defaultSchemaNameField = None


class PropUtil(object):
    """ PropUtil() """
    @staticmethod
    def GetSystemType(type):
        """ GetSystemType(type: int) -> str """
        pass


class RasterConfigDocument(ConfigDocument):
    """ RasterConfigDocument() """
    def AddOverrideInfo(self, *__args):
        """ AddOverrideInfo(self: RasterConfigDocument, rasterItem: RasterFileItem)AddOverrideInfo(self: RasterConfigDocument, rasters: List[RasterFileItem], isCombined: bool) """
        pass

    defaultSchemaNameField = None


class RasterItem(object):
    """
    RasterItem()
    RasterItem(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: RasterItem) -> str

Set: Description(self: RasterItem) = value
"""

    FeatureClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureClassName(self: RasterItem) -> str

Set: FeatureClassName(self: RasterItem) = value
"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: RasterItem) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: RasterItem) -> str

Set: Name(self: RasterItem) = value
"""

    SpatialContextAssociation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialContextAssociation(self: RasterItem) -> str

Set: SpatialContextAssociation(self: RasterItem) = value
"""



class RasterFileItem(RasterItem):
    """
    RasterFileItem()
    RasterFileItem(name: str)
    """
    def SetPosition(self, xInsertionPoint, yInsertionPoint, xResolution, yResolution, xRotation, yRotation):
        """ SetPosition(self: RasterFileItem, xInsertionPoint: float, yInsertionPoint: float, xResolution: float, yResolution: float, xRotation: float, yRotation: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    HasPosition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasPosition(self: RasterFileItem) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: RasterFileItem) -> str

Set: Location(self: RasterFileItem) = value
"""

    XInsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XInsertionPoint(self: RasterFileItem) -> float

"""

    XResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XResolution(self: RasterFileItem) -> float

"""

    XRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XRotation(self: RasterFileItem) -> float

"""

    YInsertionPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YInsertionPoint(self: RasterFileItem) -> float

"""

    YResolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YResolution(self: RasterFileItem) -> float

"""

    YRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: YRotation(self: RasterFileItem) -> float

"""



class RasterWmsItem(RasterItem):
    """
    RasterWmsItem()
    RasterWmsItem(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name=None):
        """
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: RasterWmsItem) -> MgColor

Set: BackgroundColor(self: RasterWmsItem) = value
"""

    ImageFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageFormat(self: RasterWmsItem) -> str

Set: ImageFormat(self: RasterWmsItem) = value
"""

    Transparent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transparent(self: RasterWmsItem) -> bool

Set: Transparent(self: RasterWmsItem) = value
"""

    WmsStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WmsStyle(self: RasterWmsItem) -> str

Set: WmsStyle(self: RasterWmsItem) = value
"""



class SpatialContextInfo(object):
    """
    SpatialContextInfo()
    SpatialContextInfo(coordinateSystemWkt: str)
    SpatialContextInfo(reader: MgSpatialContextReader)
    SpatialContextInfo(reader: ISpatialContextReader)
    """
    def SetExtent(self, xMin, yMin, xMax, yMax):
        """ SetExtent(self: SpatialContextInfo, xMin: float, yMin: float, xMax: float, yMax: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, coordinateSystemWkt: str)
        __new__(cls: type, reader: MgSpatialContextReader)
        __new__(cls: type, reader: ISpatialContextReader)
        """
        pass

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystem(self: SpatialContextInfo) -> str

Set: CoordinateSystem(self: SpatialContextInfo) = value
"""

    CoordinateSystemWkt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystemWkt(self: SpatialContextInfo) -> str

Set: CoordinateSystemWkt(self: SpatialContextInfo) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: SpatialContextInfo) -> str

Set: Description(self: SpatialContextInfo) = value
"""

    Extent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extent(self: SpatialContextInfo) -> MgEnvelope

Set: Extent(self: SpatialContextInfo) = value
"""

    ExtentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtentType(self: SpatialContextInfo) -> int

Set: ExtentType(self: SpatialContextInfo) = value
"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: SpatialContextInfo) -> bool

Set: IsActive(self: SpatialContextInfo) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: SpatialContextInfo) -> str

Set: Name(self: SpatialContextInfo) = value
"""

    XYTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XYTolerance(self: SpatialContextInfo) -> float

Set: XYTolerance(self: SpatialContextInfo) = value
"""

    ZTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZTolerance(self: SpatialContextInfo) -> float

Set: ZTolerance(self: SpatialContextInfo) = value
"""



class Util(object):
    # no doc
    @staticmethod
    def AddAllToMap(featureSourceId):
        """ AddAllToMap(featureSourceId: MgResourceIdentifier) -> List[MgLayerBase] """
        pass

    @staticmethod
    def AddFeatureClassToSchema(featureSourceId, schemaName, featureClass):
        """ AddFeatureClassToSchema(featureSourceId: MgResourceIdentifier, schemaName: str, featureClass: FeatureClass) -> str """
        pass

    @staticmethod
    def AddFirstFeatureClassToMap(featureSourceId, groupName):
        """ AddFirstFeatureClassToMap(featureSourceId: MgResourceIdentifier, groupName: str) -> MgLayerBase """
        pass

    @staticmethod
    def AddODBCToMap(featureSourceId, schemaName, className, groupName, xColumnName, yColumnName, zColumnName):
        """ AddODBCToMap(featureSourceId: MgResourceIdentifier, schemaName: str, className: str, groupName: str, xColumnName: str, yColumnName: str, zColumnName: str) -> MgLayerBase """
        pass

    @staticmethod
    def AddRasterToMap(featureSourceId, schemaName, className, featureName, groupName):
        """ AddRasterToMap(featureSourceId: MgResourceIdentifier, schemaName: str, className: str, featureName: str, groupName: str) -> MgLayerBase """
        pass

    @staticmethod
    def AddToMap(featureSourceId, schemaName, className, *__args):
        """
        AddToMap(featureSourceId: MgResourceIdentifier, schemaName: str, className: str, geometryName: str, groupName: str) -> MgLayerBase
        AddToMap(featureSourceId: MgResourceIdentifier, schemaName: str, className: str, groupName: str) -> MgLayerBase
        """
        pass

    @staticmethod
    def BytesToString(buffer):
        """ BytesToString(buffer: Array[Byte]) -> str """
        pass

    @staticmethod
    def ChangeSurfaceLayerStyle(layer):
        """ ChangeSurfaceLayerStyle(layer: MgLayerBase) """
        pass

    @staticmethod
    def ClearResources(keyword):
        """ ClearResources(keyword: str) """
        pass

    @staticmethod
    def ConnectToSdfFile(libraryPath, dataFileRelativePath, readOnly=None):
        """
        ConnectToSdfFile(libraryPath: str, dataFileRelativePath: str, readOnly: bool) -> MgResourceIdentifier
        ConnectToSdfFile(libraryPath: str, dataFileRelativePath: str) -> MgResourceIdentifier
        """
        pass

    @staticmethod
    def ConvertWktToCodeName(wkt):
        """ ConvertWktToCodeName(wkt: str) -> str """
        pass

    @staticmethod
    def CopyFeatures(srcFeatureSources, destFeatureSourceId, schemaName):
        """ CopyFeatures(srcFeatureSources: StringCollection, destFeatureSourceId: MgResourceIdentifier, schemaName: str) """
        pass

    @staticmethod
    def CreateFdoFeatureClass(featureSourceId, schemaName, className):
        """ CreateFdoFeatureClass(featureSourceId: MgResourceIdentifier, schemaName: str, className: str) -> FeatureClass """
        pass

    @staticmethod
    def CreateFeatureSourceDefinition(providerName, connParms):
        """ CreateFeatureSourceDefinition(providerName: str, connParms: Array[str]) -> str """
        pass

    @staticmethod
    def CreateFeatureSourceXmlForSdf(fileName, readOnly):
        """ CreateFeatureSourceXmlForSdf(fileName: str, readOnly: bool) -> str """
        pass

    @staticmethod
    def CreateLayerDefinitionObject(layerDefName, featureSourceId, schemaName, className, geometryName, geometricType):
        """ CreateLayerDefinitionObject(layerDefName: str, featureSourceId: MgResourceIdentifier, schemaName: str, className: str, geometryName: str, geometricType: int) -> LayerDefinition """
        pass

    @staticmethod
    def CreateLayerDefinitionXml(layerDefName, featureSourceId, schemaName, className, geometryName, geometricType):
        """ CreateLayerDefinitionXml(layerDefName: str, featureSourceId: MgResourceIdentifier, schemaName: str, className: str, geometryName: str, geometricType: int) -> str """
        pass

    @staticmethod
    def CreateRasterFeatureSourceDefinition(fileName, configName):
        """ CreateRasterFeatureSourceDefinition(fileName: str, configName: str) -> str """
        pass

    @staticmethod
    def CreateRasterLayerDefinitionXml(featureSourceId, featureName):
        """ CreateRasterLayerDefinitionXml(featureSourceId: MgResourceIdentifier, featureName: str) -> str """
        pass

    @staticmethod
    def CreateResultsFdoSchema(schemaName, className, *__args):
        """
        CreateResultsFdoSchema(schemaName: str, className: str, idPropertyName: str, geometryPropertyName: str, geometryType: int, extraPropertyName: str, extrPropertyDataType: DataType) -> FeatureSchema
        CreateResultsFdoSchema(schemaName: str, className: str, geometryType: int, extraPropertyName: str, extrPropertyDataType: DataType) -> FeatureSchema
        """
        pass

    @staticmethod
    def CreateSdfFeatureSourceDefinition(fileName, readOnly):
        """ CreateSdfFeatureSourceDefinition(fileName: str, readOnly: bool) -> str """
        pass

    @staticmethod
    def CreateSdfFile(sdfFilePath, schema, csWkt):
        """ CreateSdfFile(sdfFilePath: str, schema: FeatureSchema, csWkt: str) """
        pass

    @staticmethod
    def CreateSqliteFeatureSourceDefinition(fileName):
        """ CreateSqliteFeatureSourceDefinition(fileName: str) -> str """
        pass

    @staticmethod
    def CreateVectorLayerDefinition(featureSourceResId, schemaName, className, geometryName, geometricType, defaultColor):
        """ CreateVectorLayerDefinition(featureSourceResId: MgResourceIdentifier, schemaName: str, className: str, geometryName: str, geometricType: int, defaultColor: MgColor) -> str """
        pass

    @staticmethod
    def EnableLayerSelectable(enable):
        """ EnableLayerSelectable(enable: bool) """
        pass

    @staticmethod
    def GenerateUniqueResId(candidateResId):
        """ GenerateUniqueResId(candidateResId: str) -> str """
        pass

    @staticmethod
    def GetColor(geometricType, transparent=None):
        """
        GetColor(geometricType: int, transparent: bool) -> str
        GetColor(geometricType: int) -> str
        """
        pass

    @staticmethod
    def GetCoordSysWkt(featureSourceId):
        """ GetCoordSysWkt(featureSourceId: MgResourceIdentifier) -> str """
        pass

    @staticmethod
    def GetDefaultGeometryPropertyName(featureSourceId, schemaName, className):
        """ GetDefaultGeometryPropertyName(featureSourceId: MgResourceIdentifier, schemaName: str, className: str) -> str """
        pass

    @staticmethod
    def GetGeometryTypes(featureSourceId, schemaName, className, geomPropName):
        """ GetGeometryTypes(featureSourceId: MgResourceIdentifier, schemaName: str, className: str, geomPropName: str) -> (int, str) """
        pass

    @staticmethod
    def GetRasterConfigXml(xmlFilePath):
        """ GetRasterConfigXml(xmlFilePath: str) -> str """
        pass

    @staticmethod
    def GetRasterFeatureClassesFromConfig(fsId):
        """ GetRasterFeatureClassesFromConfig(fsId: MgResourceIdentifier) -> List[str] """
        pass

    @staticmethod
    def GetResource(strResId):
        """ GetResource[T](strResId: str) -> T """
        pass

    @staticmethod
    def GetWorkingDwg():
        """ GetWorkingDwg() -> str """
        pass

    @staticmethod
    def GetWorkingDwgPtr():
        """ GetWorkingDwgPtr() -> IntPtr """
        pass

    @staticmethod
    def Highlight(layer):
        """ Highlight(layer: MgLayerBase) """
        pass

    @staticmethod
    def IsGridLayer(layer):
        """ IsGridLayer(layer: MgLayerBase) -> bool """
        pass

    @staticmethod
    def IsIdentityProperty(propName, fc, fs, layerDef):
        """ IsIdentityProperty(propName: str, fc: str, fs: FeatureSource, layerDef: LayerDefinition) -> bool """
        pass

    @staticmethod
    def IsODBCLayer(featureSourceId):
        """ IsODBCLayer(featureSourceId: MgResourceIdentifier) -> bool """
        pass

    @staticmethod
    def IsRasterLayer(featureSourceId):
        """ IsRasterLayer(featureSourceId: MgResourceIdentifier) -> bool """
        pass

    @staticmethod
    def IsSecondaryProperty(propName, fc, fs, layerDef):
        """ IsSecondaryProperty(propName: str, fc: str, fs: FeatureSource, layerDef: LayerDefinition) -> bool """
        pass

    @staticmethod
    def IsVectorLayer(featureSourceId, schemaName, className):
        """ IsVectorLayer(featureSourceId: MgResourceIdentifier, schemaName: str, className: str) -> bool """
        pass

    @staticmethod
    def IsWmsLayer(featureSourceId):
        """ IsWmsLayer(featureSourceId: MgResourceIdentifier) -> bool """
        pass

    @staticmethod
    def NormalizeResourceName(resourceName):
        """ NormalizeResourceName(resourceName: str) -> str """
        pass

    @staticmethod
    def PopulateUniqueGroupName(*__args):
        """
        PopulateUniqueGroupName(map: AcMapMap, defaultName: str) -> str
        PopulateUniqueGroupName(defaultName: str) -> str
        """
        pass

    @staticmethod
    def PopulateUniqueLayerName(*__args):
        """
        PopulateUniqueLayerName(map: AcMapMap, defaultName: str) -> str
        PopulateUniqueLayerName(defaultName: str) -> str
        """
        pass

    @staticmethod
    def Print(msg):
        """ Print(msg: str) """
        pass

    @staticmethod
    def PrintLn(msg):
        """ PrintLn(msg: str) """
        pass

    @staticmethod
    def ReadFeature(reader, propertyNames):
        """ ReadFeature(reader: MgFeatureReader, propertyNames: StringCollection) -> MgPropertyCollection """
        pass

    @staticmethod
    def SaveXml(fileName, *__args):
        """ SaveXml(fileName: str, xml: str)SaveXml(fileName: str, buffer: Array[Byte]) """
        pass

    @staticmethod
    def StringToBytes(buffer):
        """ StringToBytes(buffer: str) -> Array[Byte] """
        pass

    @staticmethod
    def ToFdoDataType(mgPropertyType):
        """ ToFdoDataType(mgPropertyType: int) -> DataType """
        pass

    @staticmethod
    def ToResourceId(fileInfo):
        """ ToResourceId(fileInfo: FileInfo) -> str """
        pass

    @staticmethod
    def ToUniqueResourceId(*__args):
        """
        ToUniqueResourceId(dirInfo: DirectoryInfo) -> str
        ToUniqueResourceId(fileInfo: FileInfo) -> str
        """
        pass

    AcadEditor = None
    ArcSDEProviderName = 'OSGeo.ArcSDE'
    CurrentDir = 'C:\\Program Files\\Autodesk\\AutoCAD 2021\\Map'
    FeatureService = None
    FeatureSourceExtention = '.FeatureSource'
    GeometryPropertyName = 'geometry'
    IdentityPropertyName = 'Id'
    JpgFileExtention = '.jpg'
    LayerDefinitionExtention = '.LayerDefinition'
    LayerFileExtention = '.layer'
    MySqlProviderName = 'OSGeo.MySQL'
    ODBCProviderName = 'OSGeo.ODBC'
    OracleProviderName = 'Autodesk.Oracle'
    PostGISProviderName = 'OSGeo.PostgreSQL'
    RasterProviderName = 'Autodesk.Raster'
    ResourceService = None
    SdfFileExtention = '.sdf'
    SDFProviderName = 'OSGeo.SDF'
    SHPProviderName = 'OSGeo.SHP'
    SQLiteProviderName = 'OSGeo.SQLite'
    SqlServerProviderName = 'Autodesk.SqlServer'
    SQLServerSpatialProviderName = 'OSGeo.SQLServerSpatial'
    TopobaseProviderName = 'Autodesk.Topobase'
    WFSProviderName = 'OSGeo.WFS'
    WMSProviderName = 'OSGeo.WMS'
    __all__ = [
        'AddAllToMap',
        'AddFeatureClassToSchema',
        'AddFirstFeatureClassToMap',
        'AddODBCToMap',
        'AddRasterToMap',
        'AddToMap',
        'ArcSDEProviderName',
        'BytesToString',
        'ChangeSurfaceLayerStyle',
        'ClearResources',
        'ConnectToSdfFile',
        'ConvertWktToCodeName',
        'CopyFeatures',
        'CreateFdoFeatureClass',
        'CreateFeatureSourceDefinition',
        'CreateFeatureSourceXmlForSdf',
        'CreateLayerDefinitionObject',
        'CreateLayerDefinitionXml',
        'CreateRasterFeatureSourceDefinition',
        'CreateRasterLayerDefinitionXml',
        'CreateResultsFdoSchema',
        'CreateSdfFeatureSourceDefinition',
        'CreateSdfFile',
        'CreateSqliteFeatureSourceDefinition',
        'CreateVectorLayerDefinition',
        'EnableLayerSelectable',
        'FeatureSourceExtention',
        'GenerateUniqueResId',
        'GeometryPropertyName',
        'GetColor',
        'GetCoordSysWkt',
        'GetDefaultGeometryPropertyName',
        'GetGeometryTypes',
        'GetRasterConfigXml',
        'GetRasterFeatureClassesFromConfig',
        'GetResource',
        'GetWorkingDwg',
        'GetWorkingDwgPtr',
        'Highlight',
        'IdentityPropertyName',
        'IsGridLayer',
        'IsIdentityProperty',
        'IsODBCLayer',
        'IsRasterLayer',
        'IsSecondaryProperty',
        'IsVectorLayer',
        'IsWmsLayer',
        'JpgFileExtention',
        'LayerDefinitionExtention',
        'LayerFileExtention',
        'MySqlProviderName',
        'NormalizeResourceName',
        'ODBCProviderName',
        'OracleProviderName',
        'PopulateUniqueGroupName',
        'PopulateUniqueLayerName',
        'PostGISProviderName',
        'Print',
        'PrintLn',
        'RasterProviderName',
        'ReadFeature',
        'SaveXml',
        'SdfFileExtention',
        'SDFProviderName',
        'SHPProviderName',
        'SQLiteProviderName',
        'SqlServerProviderName',
        'SQLServerSpatialProviderName',
        'StringToBytes',
        'ToFdoDataType',
        'TopobaseProviderName',
        'ToResourceId',
        'ToUniqueResourceId',
        'WFSProviderName',
        'WMSProviderName',
    ]


class WmsConfigDocument(ConfigDocument):
    """ WmsConfigDocument() """
    def AddOverrideInfo(self, *__args):
        """ AddOverrideInfo(self: WmsConfigDocument, rasterItem: RasterWmsItem)AddOverrideInfo(self: WmsConfigDocument, rasters: List[RasterWmsItem], isCombined: bool) """
        pass

    defaultSchemaNameField = None


# variables with complex values

