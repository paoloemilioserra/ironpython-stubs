# encoding: utf-8
# module Autodesk.Gis.Map.Platform calls itself Platform
# from Autodesk.Map.Platform, Version=24.0.30.14, Culture=neutral, PublicKeyToken=null, Autodesk.Map.Platform.Utils, Version=24.0.30.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcMapAsyncLayerLoadingTask(MgAsyncTask):
    """ AcMapAsyncLayerLoadingTask(cPtr: IntPtr, cMemoryOwn: bool) """
    def Cancel(self):
        """ Cancel(self: AcMapAsyncLayerLoadingTask) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapAsyncLayerLoadingTask) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapAsyncLayerLoadingTask) -> IntPtr """
        pass

    def IsInProgress(self):
        """ IsInProgress(self: AcMapAsyncLayerLoadingTask) -> bool """
        pass

    def Wait(self):
        """ Wait(self: AcMapAsyncLayerLoadingTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AcMapEventArgs(ManagedEventArgs):
    """ AcMapEventArgs(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapEventArgs) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapEventArgs) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """ __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool) """
        pass

    swigCMemOwn = None


class AcMapCloningEventArgs(AcMapEventArgs):
    """
    AcMapCloningEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapCloningEventArgs(resource: MgResourceIdentifier, featuresOriginal: AcMapFeatureCollection, featuresCloned: AcMapFeatureCollection, additionalCloneData: MgByteReader)
    AcMapCloningEventArgs()
    """
    def Dispose(self):
        """ Dispose(self: AcMapCloningEventArgs) """
        pass

    def GetAdditionalClonedData(self):
        """ GetAdditionalClonedData(self: AcMapCloningEventArgs) -> MgByteReader """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapCloningEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapCloningEventArgs) -> IntPtr """
        pass

    def GetFeaturesCloned(self):
        """ GetFeaturesCloned(self: AcMapCloningEventArgs) -> AcMapFeatureCollection """
        pass

    def GetFeaturesOriginal(self):
        """ GetFeaturesOriginal(self: AcMapCloningEventArgs) -> AcMapFeatureCollection """
        pass

    def GetResourceIdentifier(self):
        """ GetResourceIdentifier(self: AcMapCloningEventArgs) -> MgResourceIdentifier """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type, resource: MgResourceIdentifier, featuresOriginal: AcMapFeatureCollection, featuresCloned: AcMapFeatureCollection, additionalCloneData: MgByteReader)
        __new__(cls: type)
        """
        pass

    AdditionalClonedData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AdditionalClonedData(self: AcMapCloningEventArgs) -> MgByteReader

"""

    FeaturesCloned = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeaturesCloned(self: AcMapCloningEventArgs) -> AcMapFeatureCollection

"""

    FeaturesOriginal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeaturesOriginal(self: AcMapCloningEventArgs) -> AcMapFeatureCollection

"""

    ResourceIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResourceIdentifier(self: AcMapCloningEventArgs) -> MgResourceIdentifier

"""


    swigCMemOwn = None


class AcMapCloningCancelHandledEventArgs(AcMapCloningEventArgs):
    """
    AcMapCloningCancelHandledEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapCloningCancelHandledEventArgs(resource: MgResourceIdentifier, featuresOriginal: AcMapFeatureCollection, featuresCloned: AcMapFeatureCollection, additionalCloneData: MgByteReader)
    AcMapCloningCancelHandledEventArgs()
    """
    def Dispose(self):
        """ Dispose(self: AcMapCloningCancelHandledEventArgs) """
        pass

    def GetCancel(self):
        """ GetCancel(self: AcMapCloningCancelHandledEventArgs) -> bool """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapCloningCancelHandledEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapCloningCancelHandledEventArgs) -> IntPtr """
        pass

    def GetHandled(self):
        """ GetHandled(self: AcMapCloningCancelHandledEventArgs) -> bool """
        pass

    def SetCancel(self, cancel):
        """ SetCancel(self: AcMapCloningCancelHandledEventArgs, cancel: bool) """
        pass

    def SetHandled(self, handled):
        """ SetHandled(self: AcMapCloningCancelHandledEventArgs, handled: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type, resource: MgResourceIdentifier, featuresOriginal: AcMapFeatureCollection, featuresCloned: AcMapFeatureCollection, additionalCloneData: MgByteReader)
        __new__(cls: type)
        """
        pass

    Cancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Cancel(self: AcMapCloningCancelHandledEventArgs) -> bool

Set: Cancel(self: AcMapCloningCancelHandledEventArgs) = value
"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handled(self: AcMapCloningCancelHandledEventArgs) -> bool

Set: Handled(self: AcMapCloningCancelHandledEventArgs) = value
"""


    swigCMemOwn = None


class AcMapEventAttribute(Attribute):
    """ AcMapEventAttribute() """
    ThrowException = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ThrowException(self: AcMapEventAttribute) -> bool

Set: ThrowException(self: AcMapEventAttribute) = value
"""



class AcMapFeature(MgGuardDisposable):
    """
    AcMapFeature(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapFeature(classDefinition: MgClassDefinition, properties: MgPropertyCollection, identity: AcMapIdentityCollection)
    """
    def Dispose(self):
        """ Dispose(self: AcMapFeature) """
        pass

    def GetClassDefinition(self):
        """ GetClassDefinition(self: AcMapFeature) -> MgClassDefinition """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapFeature) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeature) -> IntPtr """
        pass

    def GetIdentity(self):
        """ GetIdentity(self: AcMapFeature) -> AcMapIdentityCollection """
        pass

    def GetProperties(self):
        """ GetProperties(self: AcMapFeature) -> MgPropertyCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, classDefinition: MgClassDefinition, properties: MgPropertyCollection, identity: AcMapIdentityCollection)
        """
        pass

    swigCMemOwn = None


class AcMapFeatureCollection(MgGuardDisposable):
    """
    AcMapFeatureCollection(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapFeatureCollection()
    """
    def Add(self, value):
        """ Add(self: AcMapFeatureCollection, value: AcMapFeature) """
        pass

    def Clear(self):
        """ Clear(self: AcMapFeatureCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: AcMapFeatureCollection, value: AcMapFeature) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: AcMapFeatureCollection, array: Array[AcMapFeature], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapFeatureCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: AcMapFeatureCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcMapFeatureCollection) -> IEnumerator[AcMapFeature] """
        pass

    def GetItem(self, index):
        """ GetItem(self: AcMapFeatureCollection, index: int) -> AcMapFeature """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: AcMapFeatureCollection, value: AcMapFeature) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: AcMapFeatureCollection, index: int, value: AcMapFeature) """
        pass

    def Remove(self, value):
        """ Remove(self: AcMapFeatureCollection, value: AcMapFeature) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: AcMapFeatureCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: AcMapFeatureCollection, index: int, value: AcMapFeature) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[AcMapFeature], item: AcMapFeature) -> bool """
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
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcMapFeatureCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: AcMapFeatureCollection) -> bool

"""


    AcMapFeatureCollectionEnumerator = None
    swigCMemOwn = None


class AcMapFeatureEventArgs(AcMapEventArgs):
    """
    AcMapFeatureEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapFeatureEventArgs(resource: MgResourceIdentifier, feature: AcMapFeature, isUndoing: bool)
    """
    def Dispose(self):
        """ Dispose(self: AcMapFeatureEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapFeatureEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureEventArgs) -> IntPtr """
        pass

    def GetFeature(self):
        """ GetFeature(self: AcMapFeatureEventArgs) -> AcMapFeature """
        pass

    def GetResourceIdentifier(self):
        """ GetResourceIdentifier(self: AcMapFeatureEventArgs) -> MgResourceIdentifier """
        pass

    def IsUndoing(self):
        """ IsUndoing(self: AcMapFeatureEventArgs) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: MgResourceIdentifier, feature: AcMapFeature, isUndoing: bool)
        """
        pass

    swigCMemOwn = None


class AcMapFeatureService(MgFeatureService):
    """ AcMapFeatureService(cPtr: IntPtr, cMemoryOwn: bool) """
    def ApplySchema(self, resource, schema):
        """ ApplySchema(self: AcMapFeatureService, resource: MgResourceIdentifier, schema: MgFeatureSchema) """
        pass

    def BeginTransaction(self, resource):
        """ BeginTransaction(self: AcMapFeatureService, resource: MgResourceIdentifier) -> MgTransaction """
        pass

    def BindConnection(self, featureSourceId):
        """ BindConnection(self: AcMapFeatureService, featureSourceId: MgResourceIdentifier) """
        pass

    def CreateFeatureSource(self, resource, sourceParams):
        """ CreateFeatureSource(self: AcMapFeatureService, resource: MgResourceIdentifier, sourceParams: MgFeatureSourceParams) """
        pass

    def DeleteFeatures(self, resource, className, filter, trans=None):
        """
        DeleteFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, filter: str, trans: MgTransaction) -> int
        DeleteFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, filter: str) -> int
        """
        pass

    def DescribeSchema(self, resource, schemaNam, classNames=None):
        """
        DescribeSchema(self: AcMapFeatureService, resource: MgResourceIdentifier, schemaNam: str, classNames: MgStringCollection) -> MgFeatureSchemaCollection
        DescribeSchema(self: AcMapFeatureService, resource: MgResourceIdentifier, schemaNam: str) -> MgFeatureSchemaCollection
        """
        pass

    def DescribeSchemaAsXml(self, resource, schemaNam, classNames=None):
        """
        DescribeSchemaAsXml(self: AcMapFeatureService, resource: MgResourceIdentifier, schemaNam: str, classNames: MgStringCollection) -> str
        DescribeSchemaAsXml(self: AcMapFeatureService, resource: MgResourceIdentifier, schemaNam: str) -> str
        """
        pass

    def DescribeWfsFeatureType(self, featureSourceId, featureClasses, namespacePrefix=None, namespaceUrl=None):
        """
        DescribeWfsFeatureType(self: AcMapFeatureService, featureSourceId: MgResourceIdentifier, featureClasses: MgStringCollection, namespacePrefix: str, namespaceUrl: str) -> MgByteReader
        DescribeWfsFeatureType(self: AcMapFeatureService, featureSourceId: MgResourceIdentifier, featureClasses: MgStringCollection) -> MgByteReader
        """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapFeatureService) """
        pass

    def EnumerateDataStores(self, providerName, partialConnString):
        """ EnumerateDataStores(self: AcMapFeatureService, providerName: str, partialConnString: str) -> MgByteReader """
        pass

    def ExecuteSqlNonQuery(self, resource, sqlNonSelectStatement, parameters=None, transaction=None):
        """
        ExecuteSqlNonQuery(self: AcMapFeatureService, resource: MgResourceIdentifier, sqlNonSelectStatement: str, parameters: MgParameterCollection, transaction: MgTransaction) -> int
        ExecuteSqlNonQuery(self: AcMapFeatureService, resource: MgResourceIdentifier, sqlNonSelectStatement: str) -> int
        """
        pass

    def ExecuteSqlQuery(self, resource, sqlStatement, parameters=None, transaction=None):
        """
        ExecuteSqlQuery(self: AcMapFeatureService, resource: MgResourceIdentifier, sqlStatement: str, parameters: MgParameterCollection, transaction: MgTransaction) -> MgSqlDataReader
        ExecuteSqlQuery(self: AcMapFeatureService, resource: MgResourceIdentifier, sqlStatement: str) -> MgSqlDataReader
        """
        pass

    def GetCapabilities(self, providerName, connectionString=None):
        """
        GetCapabilities(self: AcMapFeatureService, providerName: str, connectionString: str) -> MgByteReader
        GetCapabilities(self: AcMapFeatureService, providerName: str) -> MgByteReader
        """
        pass

    def GetClassDefinition(self, resource, schemaName, className):
        """ GetClassDefinition(self: AcMapFeatureService, resource: MgResourceIdentifier, schemaName: str, className: str) -> MgClassDefinition """
        pass

    def GetClasses(self, resource, schemaNam):
        """ GetClasses(self: AcMapFeatureService, resource: MgResourceIdentifier, schemaNam: str) -> MgStringCollection """
        pass

    def GetConnectionPropertyValues(self, providerName, propertyName, partialConnString):
        """ GetConnectionPropertyValues(self: AcMapFeatureService, providerName: str, propertyName: str, partialConnString: str) -> MgStringCollection """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureService) -> IntPtr """
        pass

    def GetFdoConnection(self, resource):
        """ GetFdoConnection(self: AcMapFeatureService, resource: MgResourceIdentifier) -> IConnection """
        pass

    def GetFeatureProviders(self):
        """ GetFeatureProviders(self: AcMapFeatureService) -> MgByteReader """
        pass

    def GetLockedFeatures(self, resource, className, options):
        """ GetLockedFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, options: MgFeatureQueryOptions) -> MgFeatureReader """
        pass

    def GetLongTransactions(self, resource, bActiveOnly):
        """ GetLongTransactions(self: AcMapFeatureService, resource: MgResourceIdentifier, bActiveOnly: bool) -> MgLongTransactionReader """
        pass

    def GetSchemaMapping(self, providerName, partialConnString):
        """ GetSchemaMapping(self: AcMapFeatureService, providerName: str, partialConnString: str) -> MgByteReader """
        pass

    def GetSchemas(self, resourc):
        """ GetSchemas(self: AcMapFeatureService, resourc: MgResourceIdentifier) -> MgStringCollection """
        pass

    def GetSpatialContexts(self, resource, bActiveOnly):
        """ GetSpatialContexts(self: AcMapFeatureService, resource: MgResourceIdentifier, bActiveOnly: bool) -> MgSpatialContextReader """
        pass

    def GetWfsFeature(self, featureSourceId, featureClass, requiredProperties, srs, filter, maxFeatures, wfsVersion=None, outputFormat=None, sortCriteria=None, namespacePrefix=None, namespaceUrl=None):
        """
        GetWfsFeature(self: AcMapFeatureService, featureSourceId: MgResourceIdentifier, featureClass: str, requiredProperties: MgStringCollection, srs: str, filter: str, maxFeatures: int, wfsVersion: str, outputFormat: str, sortCriteria: str, namespacePrefix: str, namespaceUrl: str) -> MgByteReader
        GetWfsFeature(self: AcMapFeatureService, featureSourceId: MgResourceIdentifier, featureClass: str, requiredProperties: MgStringCollection, srs: str, filter: str, maxFeatures: int) -> MgByteReader
        """
        pass

    def InsertFeatures(self, resource, className, *__args):
        """
        InsertFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, batchPropertyValues: MgBatchPropertyCollection) -> MgFeatureReader
        InsertFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, batchPropertyValues: MgBatchPropertyCollection, trans: MgTransaction) -> MgFeatureReader
        InsertFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, propertyValues: MgPropertyCollection) -> MgFeatureReader
        InsertFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, propertyValues: MgPropertyCollection, trans: MgTransaction) -> MgFeatureReader
        """
        pass

    def OnFeatureDeleteCancelled(self, args):
        """ OnFeatureDeleteCancelled(self: AcMapFeatureService, args: AcMapFeatureEventArgs) """
        pass

    def OnFeatureDeleted(self, args):
        """ OnFeatureDeleted(self: AcMapFeatureService, args: AcMapFeatureEventArgs) """
        pass

    def OnFeatureInsertCancelled(self, args):
        """ OnFeatureInsertCancelled(self: AcMapFeatureService, args: AcMapFeatureEventArgs) """
        pass

    def OnFeatureInserted(self, args):
        """ OnFeatureInserted(self: AcMapFeatureService, args: AcMapFeatureEventArgs) """
        pass

    def OnFeatureSourceAdded(self, resource):
        """ OnFeatureSourceAdded(self: AcMapFeatureService, resource: AcMapResourceEventArgs) """
        pass

    def OnFeatureSourceConnected(self, resource):
        """ OnFeatureSourceConnected(self: AcMapFeatureService, resource: AcMapResourceEventArgs) """
        pass

    def OnFeatureSourceDisconnected(self, resource):
        """ OnFeatureSourceDisconnected(self: AcMapFeatureService, resource: AcMapResourceEventArgs) """
        pass

    def OnFeatureSourceRemoved(self, resource):
        """ OnFeatureSourceRemoved(self: AcMapFeatureService, resource: AcMapResourceEventArgs) """
        pass

    def OnFeatureToBeDeleted(self, args):
        """ OnFeatureToBeDeleted(self: AcMapFeatureService, args: AcMapFeatureToBeEventArgs) """
        pass

    def OnFeatureToBeInserted(self, args):
        """ OnFeatureToBeInserted(self: AcMapFeatureService, args: AcMapFeatureToBeEventArgs) """
        pass

    def OnFeatureToBeUpdated(self, args):
        """ OnFeatureToBeUpdated(self: AcMapFeatureService, args: AcMapFeatureToBeEventArgs) """
        pass

    def OnFeatureUpdateCancelled(self, args):
        """ OnFeatureUpdateCancelled(self: AcMapFeatureService, args: AcMapFeatureEventArgs) """
        pass

    def OnFeatureUpdated(self, args):
        """ OnFeatureUpdated(self: AcMapFeatureService, args: AcMapFeatureEventArgs) """
        pass

    def OnLongTransactionActivateCancelled(self, args):
        """ OnLongTransactionActivateCancelled(self: AcMapFeatureService, args: AcMapLongTransactionEventArgs) """
        pass

    def OnLongTransactionActivated(self, args):
        """ OnLongTransactionActivated(self: AcMapFeatureService, args: AcMapLongTransactionEventArgs) """
        pass

    def OnLongTransactionToBeActivated(self, args):
        """ OnLongTransactionToBeActivated(self: AcMapFeatureService, args: AcMapLongTransactionToBeEventArgs) """
        pass

    def SchemaToXml(self, schema):
        """ SchemaToXml(self: AcMapFeatureService, schema: MgFeatureSchemaCollection) -> str """
        pass

    def SelectAggregate(self, resource, className, option):
        """ SelectAggregate(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, option: MgFeatureAggregateOptions) -> MgDataReader """
        pass

    def SelectFeatures(self, resource, className, *__args):
        """
        SelectFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, options: MgFeatureQueryOptions, coordinateSystem: str) -> MgFeatureReader
        SelectFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, option: MgFeatureQueryOptions) -> MgFeatureReader
        """
        pass

    def SetLongTransaction(self, featureSourceId, longTransactionName):
        """ SetLongTransaction(self: AcMapFeatureService, featureSourceId: MgResourceIdentifier, longTransactionName: str) -> bool """
        pass

    def TestConnection(self, *__args):
        """
        TestConnection(self: AcMapFeatureService, resource: MgResourceIdentifier) -> bool
        TestConnection(self: AcMapFeatureService, providerName: str, connectionString: str) -> bool
        """
        pass

    def UnbindConnection(self, featureSourceId):
        """ UnbindConnection(self: AcMapFeatureService, featureSourceId: MgResourceIdentifier) """
        pass

    def UpdateFeatures(self, resource, commands, *__args):
        """
        UpdateFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, commands: MgFeatureCommandCollection, useTransaction: bool, bRecordForUndo: bool, bFireEvents: bool) -> MgPropertyCollection
        UpdateFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, commands: MgFeatureCommandCollection, transaction: MgTransaction, bRecordForUndo: bool, bFireEvents: bool) -> MgPropertyCollection
        UpdateFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, commands: MgFeatureCommandCollection, useTransaction: bool) -> MgPropertyCollection
        UpdateFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, commands: MgFeatureCommandCollection, transaction: MgTransaction) -> MgPropertyCollection
        """
        pass

    def UpdateMatchingFeatures(self, resource, className, properties, filter, trans=None):
        """
        UpdateMatchingFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, properties: MgPropertyCollection, filter: str, trans: MgTransaction) -> int
        UpdateMatchingFeatures(self: AcMapFeatureService, resource: MgResourceIdentifier, className: str, properties: MgPropertyCollection, filter: str) -> int
        """
        pass

    def XmlToSchema(self, xml):
        """ XmlToSchema(self: AcMapFeatureService, xml: str) -> MgFeatureSchemaCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    FeatureDeleteCancelled = None
    FeatureDeleted = None
    FeatureInsertCancelled = None
    FeatureInserted = None
    FeatureSourceAdded = None
    FeatureSourceConnected = None
    FeatureSourceDisconnected = None
    FeatureSourceRemoved = None
    FeatureToBeDeleted = None
    FeatureToBeInserted = None
    FeatureToBeUpdated = None
    FeatureUpdateCancelled = None
    FeatureUpdated = None
    LongTransactionActivateCancelled = None
    LongTransactionActivated = None
    LongTransactionToBeActivated = None
    swigCMemOwn = None


class AcMapFeatureToBeEventArgs(AcMapFeatureEventArgs):
    """
    AcMapFeatureToBeEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapFeatureToBeEventArgs(resource: MgResourceIdentifier, featureOrginal: AcMapFeature, featureCurrent: AcMapFeature, isUndoing: bool)
    """
    def Dispose(self):
        """ Dispose(self: AcMapFeatureToBeEventArgs) """
        pass

    def GetCancelled(self):
        """ GetCancelled(self: AcMapFeatureToBeEventArgs) -> bool """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapFeatureToBeEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureToBeEventArgs) -> IntPtr """
        pass

    def GetHandled(self):
        """ GetHandled(self: AcMapFeatureToBeEventArgs) -> bool """
        pass

    def GetOriginalFeature(self):
        """ GetOriginalFeature(self: AcMapFeatureToBeEventArgs) -> AcMapFeature """
        pass

    def GetRecordForUndo(self):
        """ GetRecordForUndo(self: AcMapFeatureToBeEventArgs) -> bool """
        pass

    def SetCancelled(self):
        """ SetCancelled(self: AcMapFeatureToBeEventArgs) """
        pass

    def SetHandled(self):
        """ SetHandled(self: AcMapFeatureToBeEventArgs) """
        pass

    def SetRecordForUndo(self):
        """ SetRecordForUndo(self: AcMapFeatureToBeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: MgResourceIdentifier, featureOrginal: AcMapFeature, featureCurrent: AcMapFeature, isUndoing: bool)
        """
        pass

    swigCMemOwn = None


class AcMapFeatureTransaction(MgTransaction):
    """ AcMapFeatureTransaction(cPtr: IntPtr, cMemoryOwn: bool) """
    def AddSavePoint(self, suggestName):
        """ AddSavePoint(self: AcMapFeatureTransaction, suggestName: str) -> str """
        pass

    def Commit(self):
        """ Commit(self: AcMapFeatureTransaction) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapFeatureTransaction) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureTransaction) -> IntPtr """
        pass

    def GetFeatureSource(self):
        """ GetFeatureSource(self: AcMapFeatureTransaction) -> MgResourceIdentifier """
        pass

    def IsNestedTransaction(self):
        """ IsNestedTransaction(self: AcMapFeatureTransaction) -> bool """
        pass

    def ReleaseSavePoint(self, savePointName):
        """ ReleaseSavePoint(self: AcMapFeatureTransaction, savePointName: str) """
        pass

    def Rollback(self, savePointName=None):
        """ Rollback(self: AcMapFeatureTransaction, savePointName: str)Rollback(self: AcMapFeatureTransaction) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AcMapIdentityCollection(MgPropertyCollection):
    """ AcMapIdentityCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapIdentityCollection) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapIdentityCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapIdentityCollection) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AcMapLayer(MgLayerBase):
    """ AcMapLayer(cPtr: IntPtr, cMemoryOwn: bool) """
    def AreLabelsDefined(self):
        """ AreLabelsDefined(self: AcMapLayer) -> bool """
        pass

    @staticmethod
    def Create(layerDefinition, resourceService):
        """ Create(layerDefinition: MgResourceIdentifier, resourceService: MgResourceService) -> AcMapLayer """
        pass

    def CreateAnnotativeTextForLabels(self, targetFeatureSource, selectedSchema, targetFeatureClass, doLabelsWithinView):
        """ CreateAnnotativeTextForLabels(self: AcMapLayer, targetFeatureSource: str, selectedSchema: str, targetFeatureClass: str, doLabelsWithinView: bool) """
        pass

    def CreateCache(self):
        """ CreateCache(self: AcMapLayer) """
        pass

    def DiscardFeatureChanges(self):
        """ DiscardFeatureChanges(self: AcMapLayer) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapLayer) """
        pass

    def ForceRefresh(self, pFeatureIds=None):
        """ ForceRefresh(self: AcMapLayer, pFeatureIds: MgBatchPropertyCollection)ForceRefresh(self: AcMapLayer) """
        pass

    def GetClassDefinition(self):
        """ GetClassDefinition(self: AcMapLayer) -> MgClassDefinition """
        pass

    def GetCoordinateSystemId(self):
        """ GetCoordinateSystemId(self: AcMapLayer) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLayer) -> IntPtr """
        pass

    def GetEditMode(self):
        """ GetEditMode(self: AcMapLayer) -> int """
        pass

    def GetExpandInLegend(self):
        """ GetExpandInLegend(self: AcMapLayer) -> bool """
        pass

    def GetExtents(self):
        """ GetExtents(self: AcMapLayer) -> MgEnvelope """
        pass

    def GetFeatures(self, pFeatureIds):
        """ GetFeatures(self: AcMapLayer, pFeatureIds: MgBatchPropertyCollection) -> MgFeatureReader """
        pass

    def GetIdsOfEditSetFeatures(self):
        """ GetIdsOfEditSetFeatures(self: AcMapLayer) -> MgBatchPropertyCollection """
        pass

    def GetIsLoaded(self):
        """ GetIsLoaded(self: AcMapLayer) -> bool """
        pass

    def GetLockedFeatures(self):
        """ GetLockedFeatures(self: AcMapLayer) -> MgFeatureReader """
        pass

    def GetOrder(self):
        """ GetOrder(self: AcMapLayer) -> int """
        pass

    def GetSpatialContext(self):
        """ GetSpatialContext(self: AcMapLayer) -> MgSpatialContextReader """
        pass

    def HasEditedLabels(self):
        """ HasEditedLabels(self: AcMapLayer) -> bool """
        pass

    def IsCached(self):
        """ IsCached(self: AcMapLayer) -> bool """
        pass

    def IsLayerReadOnly(self):
        """ IsLayerReadOnly(self: AcMapLayer) -> bool """
        pass

    def IsTextLayer(self):
        """ IsTextLayer(self: AcMapLayer) -> bool """
        pass

    def IsVisible(self):
        """ IsVisible(self: AcMapLayer) -> bool """
        pass

    def SaveFeatureChanges(self, options):
        """ SaveFeatureChanges(self: AcMapLayer, options: MgFeatureQueryOptions) """
        pass

    def SelectAggregate(self, options):
        """ SelectAggregate(self: AcMapLayer, options: MgFeatureAggregateOptions) -> MgDataReader """
        pass

    def SelectFeatures(self, options, coordinateSystem=None):
        """ SelectFeatures(self: AcMapLayer, options: MgFeatureQueryOptions) -> MgFeatureReader """
        pass

    def SetEditMode(self, editMode):
        """ SetEditMode(self: AcMapLayer, editMode: int) """
        pass

    def SetExpandInLegend(self, expand):
        """ SetExpandInLegend(self: AcMapLayer, expand: bool) """
        pass

    def SetFeatureClassName(self, featureClass):
        """ SetFeatureClassName(self: AcMapLayer, featureClass: str) """
        pass

    def SetFeatureVisibility(self, pSelection, bVisible):
        """ SetFeatureVisibility(self: AcMapLayer, pSelection: MgSelectionBase, bVisible: bool) """
        pass

    def SetLayerDefinition(self, layerDefinition, resourceService):
        """ SetLayerDefinition(self: AcMapLayer, layerDefinition: MgResourceIdentifier, resourceService: MgResourceService) """
        pass

    def SetLayerReadOnly(self):
        """ SetLayerReadOnly(self: AcMapLayer) -> bool """
        pass

    def SetName(self, layerName):
        """ SetName(self: AcMapLayer, layerName: str) """
        pass

    def SetOrder(self, value):
        """ SetOrder(self: AcMapLayer, value: int) """
        pass

    def SetVisible(self, bVisible):
        """ SetVisible(self: AcMapLayer, bVisible: bool) """
        pass

    def UpdateFeatures(self, commands, transaction=None):
        """ UpdateFeatures(self: AcMapLayer, commands: MgFeatureCommandCollection) -> MgPropertyCollection """
        pass

    def ZoomToLayer(self):
        """ ZoomToLayer(self: AcMapLayer) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    CoordinateSystemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystemId(self: AcMapLayer) -> str

"""

    EditMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditMode(self: AcMapLayer) -> int

Set: EditMode(self: AcMapLayer) = value
"""

    ExpandInLegend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpandInLegend(self: AcMapLayer) -> bool

Set: ExpandInLegend(self: AcMapLayer) = value
"""

    IsLoaded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLoaded(self: AcMapLayer) -> bool

"""


    swigCMemOwn = None


class AcMapLayerGroup(MgLayerGroup):
    """
    AcMapLayerGroup(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapLayerGroup(groupName: str)
    """
    def Dispose(self):
        """ Dispose(self: AcMapLayerGroup) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLayerGroup) -> IntPtr """
        pass

    def GetExpandInLegend(self):
        """ GetExpandInLegend(self: AcMapLayerGroup) -> bool """
        pass

    def GetName(self):
        """ GetName(self: AcMapLayerGroup) -> str """
        pass

    def GetOrder(self):
        """ GetOrder(self: AcMapLayerGroup) -> int """
        pass

    def SetExpandInLegend(self, expandInLegend):
        """ SetExpandInLegend(self: AcMapLayerGroup, expandInLegend: bool) """
        pass

    def SetName(self, groupName):
        """ SetName(self: AcMapLayerGroup, groupName: str) """
        pass

    def SetVisible(self, visible):
        """ SetVisible(self: AcMapLayerGroup, visible: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, groupName: str)
        """
        pass

    ExpandInLegend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpandInLegend(self: AcMapLayerGroup) -> bool

Set: ExpandInLegend(self: AcMapLayerGroup) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcMapLayerGroup) -> str

Set: Name(self: AcMapLayerGroup) = value
"""


    swigCMemOwn = None


class AcMapLongTransactionEventArgs(AcMapEventArgs):
    """
    AcMapLongTransactionEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapLongTransactionEventArgs(resource: MgResourceIdentifier, ltName: str)
    """
    def Dispose(self):
        """ Dispose(self: AcMapLongTransactionEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapLongTransactionEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLongTransactionEventArgs) -> IntPtr """
        pass

    def GetLtName(self):
        """ GetLtName(self: AcMapLongTransactionEventArgs) -> str """
        pass

    def GetResourceIdentifier(self):
        """ GetResourceIdentifier(self: AcMapLongTransactionEventArgs) -> MgResourceIdentifier """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: MgResourceIdentifier, ltName: str)
        """
        pass

    swigCMemOwn = None


class AcMapLongTransactionToBeEventArgs(AcMapLongTransactionEventArgs):
    """
    AcMapLongTransactionToBeEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapLongTransactionToBeEventArgs(resource: MgResourceIdentifier, ltName: str)
    """
    def Dispose(self):
        """ Dispose(self: AcMapLongTransactionToBeEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapLongTransactionToBeEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLongTransactionToBeEventArgs) -> IntPtr """
        pass

    def GetHandled(self):
        """ GetHandled(self: AcMapLongTransactionToBeEventArgs) -> bool """
        pass

    def SetHandled(self):
        """ SetHandled(self: AcMapLongTransactionToBeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: MgResourceIdentifier, ltName: str)
        """
        pass

    swigCMemOwn = None


class AcMapMap(MgMapBase):
    """ AcMapMap(cPtr: IntPtr, cMemoryOwn: bool) """
    def ActivateDrawOrder(self):
        """ ActivateDrawOrder(self: AcMapMap) """
        pass

    def AddLayersAsync(self, layers):
        """ AddLayersAsync(self: AcMapMap, layers: List[MgLayerBase]) -> MgAsyncTask """
        pass

    def BeginLoadingLayers(self):
        """ BeginLoadingLayers(self: AcMapMap) """
        pass

    def Create(self, *__args):
        """ Create(self: AcMapMap, mapSRS: str, mapExtent: MgEnvelope, mapName: str)Create(self: AcMapMap, resourceService: MgResourceService, mapDefinition: MgResourceIdentifier, mapName: str) """
        pass

    def CreateUniqueLayerElement(self, acadLayerName):
        """ CreateUniqueLayerElement(self: AcMapMap, acadLayerName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapMap) """
        pass

    def EndLoadingLayers(self):
        """ EndLoadingLayers(self: AcMapMap) """
        pass

    @staticmethod
    def ForceScreenRefresh():
        """ ForceScreenRefresh() """
        pass

    def GetBackgroundColor(self):
        """ GetBackgroundColor(self: AcMapMap) -> str """
        pass

    def GetCoordinateSystemId(self):
        """ GetCoordinateSystemId(self: AcMapMap) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapMap) -> IntPtr """
        pass

    @staticmethod
    def GetCurrentMap():
        """ GetCurrentMap() -> AcMapMap """
        pass

    def GetDataExtent(self):
        """ GetDataExtent(self: AcMapMap) -> MgEnvelope """
        pass

    def GetDisplayDpi(self):
        """ GetDisplayDpi(self: AcMapMap) -> int """
        pass

    def GetDisplayHeight(self):
        """ GetDisplayHeight(self: AcMapMap) -> int """
        pass

    def GetDisplayWidth(self):
        """ GetDisplayWidth(self: AcMapMap) -> int """
        pass

    def GetFiniteDisplayScaleAt(self, index):
        """ GetFiniteDisplayScaleAt(self: AcMapMap, index: int) -> float """
        pass

    def GetFiniteDisplayScaleCount(self):
        """ GetFiniteDisplayScaleCount(self: AcMapMap) -> int """
        pass

    def GetIsDefault(self):
        """ GetIsDefault(self: AcMapMap) -> bool """
        pass

    def GetLayerGroups(self):
        """ GetLayerGroups(self: AcMapMap) -> MgLayerGroupCollection """
        pass

    def GetLayers(self):
        """ GetLayers(self: AcMapMap) -> MgLayerCollection """
        pass

    def GetLayersForFeatureClass(self, pFeatureSourceResId, strQualifiedFeatureClass):
        """ GetLayersForFeatureClass(self: AcMapMap, pFeatureSourceResId: MgResourceIdentifier, strQualifiedFeatureClass: str) -> MgReadOnlyLayerCollection """
        pass

    def GetMapDefinition(self):
        """ GetMapDefinition(self: AcMapMap) -> MgResourceIdentifier """
        pass

    def GetMapExtent(self):
        """ GetMapExtent(self: AcMapMap) -> MgEnvelope """
        pass

    def GetMapSRS(self):
        """ GetMapSRS(self: AcMapMap) -> str """
        pass

    def GetName(self):
        """ GetName(self: AcMapMap) -> str """
        pass

    def GetObjectId(self):
        """ GetObjectId(self: AcMapMap) -> str """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: AcMapMap) -> str """
        pass

    def GetSynchronousLoading(self):
        """ GetSynchronousLoading(self: AcMapMap) -> bool """
        pass

    def GetViewCenter(self):
        """ GetViewCenter(self: AcMapMap) -> MgPoint """
        pass

    def GetViewScale(self):
        """ GetViewScale(self: AcMapMap) -> float """
        pass

    def ImportLayer(self, layerFile):
        """ ImportLayer(self: AcMapMap, layerFile: str) -> MgLayerBase """
        pass

    def IsSynchronousLoading(self):
        """ IsSynchronousLoading(self: AcMapMap) -> bool """
        pass

    def LoadLayer(self, layerFile):
        """ LoadLayer(self: AcMapMap, layerFile: str) """
        pass

    def OnAllLayerLoadingFinished(self, args):
        """ OnAllLayerLoadingFinished(self: AcMapMap, args: AllLayerLoadingFinishedEventArgs) """
        pass

    def OnFeatureInstanceAdded(self, args):
        """ OnFeatureInstanceAdded(self: AcMapMap, args: FeatureInstanceAddedEventArgs) """
        pass

    def OnFeatureInstanceModified(self, args):
        """ OnFeatureInstanceModified(self: AcMapMap, args: FeatureInstanceModifiedEventArgs) """
        pass

    def OnFeatureInstanceRemoved(self, args):
        """ OnFeatureInstanceRemoved(self: AcMapMap, args: FeatureInstanceRemovedEventArgs) """
        pass

    def OnFeatureInstanceToBeAdded(self, args):
        """ OnFeatureInstanceToBeAdded(self: AcMapMap, args: FeatureInstanceToBeAddedEventArgs) """
        pass

    def OnFeatureInstanceToBeModified(self, args):
        """ OnFeatureInstanceToBeModified(self: AcMapMap, args: FeatureInstanceToBeModifiedEventArgs) """
        pass

    def OnFeatureInstanceToBeRemoved(self, args):
        """ OnFeatureInstanceToBeRemoved(self: AcMapMap, args: FeatureInstanceToBeRemovedEventArgs) """
        pass

    def OnGroupAdded(self, args):
        """ OnGroupAdded(self: AcMapMap, args: AcMapMappingEventArgs) """
        pass

    def OnGroupModified(self, args):
        """ OnGroupModified(self: AcMapMap, args: AcMapMapObjectModifiedEventArgs) """
        pass

    def OnGroupRemoved(self, args):
        """ OnGroupRemoved(self: AcMapMap, args: AcMapMappingEventArgs) """
        pass

    def OnLayerAdded(self, args):
        """ OnLayerAdded(self: AcMapMap, args: AcMapMappingEventArgs) """
        pass

    def OnLayerCacheLoadingEnded(self, args):
        """ OnLayerCacheLoadingEnded(self: AcMapMap, args: LayerCacheLoadingEndedEventArgs) """
        pass

    def OnLayerCacheLoadingStarted(self, args):
        """ OnLayerCacheLoadingStarted(self: AcMapMap, args: LayerCacheLoadingStartedEventArgs) """
        pass

    def OnLayerInitialized(self, args):
        """ OnLayerInitialized(self: AcMapMap, args: AcMapMappingEventArgs) """
        pass

    def OnLayerModified(self, args):
        """ OnLayerModified(self: AcMapMap, args: AcMapMapObjectModifiedEventArgs) """
        pass

    def OnLayerRemoved(self, args):
        """ OnLayerRemoved(self: AcMapMap, args: AcMapMappingEventArgs) """
        pass

    def OnSchemaEditorOpening(self, args):
        """ OnSchemaEditorOpening(self: AcMapMap, args: SchemaEditorOpeningEventArgs) """
        pass

    def Open(self, resourceService, *__args):
        """ Open(self: AcMapMap, resourceService: MgResourceService, mapName: str) """
        pass

    def SaveLayer(self, layer, layerFile):
        """ SaveLayer(self: AcMapMap, layer: MgLayerBase, layerFile: str) """
        pass

    def SetCoordinateSystemId(self, csCode):
        """ SetCoordinateSystemId(self: AcMapMap, csCode: str) """
        pass

    def SetName(self, mapName):
        """ SetName(self: AcMapMap, mapName: str) """
        pass

    def SetSynchronousLoading(self, bSync):
        """ SetSynchronousLoading(self: AcMapMap, bSync: bool) """
        pass

    def SetViewCenter(self, center):
        """ SetViewCenter(self: AcMapMap, center: MgPoint) """
        pass

    def SetViewScale(self, scale):
        """ SetViewScale(self: AcMapMap, scale: float) """
        pass

    def ZoomToExtent(self, envelope):
        """ ZoomToExtent(self: AcMapMap, envelope: MgEnvelope) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    BackgroundColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BackgroundColor(self: AcMapMap) -> str

"""

    CoordinateSystemId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystemId(self: AcMapMap) -> str

Set: CoordinateSystemId(self: AcMapMap) = value
"""

    IsDefault = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDefault(self: AcMapMap) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcMapMap) -> str

Set: Name(self: AcMapMap) = value
"""


    AllLayerLoadingFinished = None
    FeatureInstanceAdded = None
    FeatureInstanceModified = None
    FeatureInstanceRemoved = None
    FeatureInstanceToBeAdded = None
    FeatureInstanceToBeModified = None
    FeatureInstanceToBeRemoved = None
    GroupAdded = None
    GroupModified = None
    GroupRemoved = None
    LayerAdded = None
    LayerCacheLoadingEnded = None
    LayerCacheLoadingStarted = None
    LayerInitialized = None
    LayerModified = None
    LayerRemoved = None
    SchemaEditorOpening = None
    swigCMemOwn = None


class AcMapMappingEventArgs(AcMapEventArgs):
    """
    AcMapMappingEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapMappingEventArgs(name: str, pmap: AcMapMap)
    """
    def Dispose(self):
        """ Dispose(self: AcMapMappingEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapMappingEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapMappingEventArgs) -> IntPtr """
        pass

    def GetMap(self):
        """ GetMap(self: AcMapMappingEventArgs) -> AcMapMap """
        pass

    def GetName(self):
        """ GetName(self: AcMapMappingEventArgs) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, pmap: AcMapMap)
        """
        pass

    Map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Map(self: AcMapMappingEventArgs) -> AcMapMap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: AcMapMappingEventArgs) -> str

"""


    swigCMemOwn = None


class AcMapMapChangeEventArgs(AcMapMappingEventArgs):
    """
    AcMapMapChangeEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapMapChangeEventArgs(name: str, newName: str, pMap: AcMapMap)
    """
    def Dispose(self):
        """ Dispose(self: AcMapMapChangeEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapMapChangeEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapMapChangeEventArgs) -> IntPtr """
        pass

    def GetNewName(self):
        """ GetNewName(self: AcMapMapChangeEventArgs) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, newName: str, pMap: AcMapMap)
        """
        pass

    NewName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewName(self: AcMapMapChangeEventArgs) -> str

"""


    swigCMemOwn = None


class AcMapMapCollection(MgGuardDisposable):
    """ AcMapMapCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Add(self, value):
        """ Add(self: AcMapMapCollection, value: MgMapBase) """
        pass

    def Clear(self):
        """ Clear(self: AcMapMapCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: AcMapMapCollection, value: MgMapBase) -> bool
        Contains(self: AcMapMapCollection, name: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: AcMapMapCollection, array: Array[MgMapBase], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapMapCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: AcMapMapCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapMapCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcMapMapCollection) -> IEnumerator[MgMapBase] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: AcMapMapCollection, name: str) -> MgMapBase
        GetItem(self: AcMapMapCollection, index: int) -> MgMapBase
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: AcMapMapCollection, value: MgMapBase) -> int
        IndexOf(self: AcMapMapCollection, name: str) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: AcMapMapCollection, index: int, value: MgMapBase) """
        pass

    def Remove(self, value):
        """ Remove(self: AcMapMapCollection, value: MgMapBase) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: AcMapMapCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: AcMapMapCollection, index: int, value: MgMapBase) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgMapBase], item: MgMapBase) -> bool """
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
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: AcMapMapCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: AcMapMapCollection) -> bool

"""


    AcMapMapCollectionEnumerator = None
    swigCMemOwn = None


class AcMapMapManagementService(MgService):
    """ AcMapMapManagementService(cPtr: IntPtr, cMemoryOwn: bool) """
    def CreateNewMap(self, mapName):
        """ CreateNewMap(self: AcMapMapManagementService, mapName: str) -> AcMapMap """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapMapManagementService) """
        pass

    def DuplicateMap(self, map):
        """ DuplicateMap(self: AcMapMapManagementService, map: AcMapMap) -> AcMapMap """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapMapManagementService) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapMapManagementService) -> IntPtr """
        pass

    def GetCurrentMap(self):
        """ GetCurrentMap(self: AcMapMapManagementService) -> AcMapMap """
        pass

    @staticmethod
    def GetInstance(db):
        """ GetInstance(db: Database) -> AcMapMapManagementService """
        pass

    def GetMaps(self):
        """ GetMaps(self: AcMapMapManagementService) -> AcMapMapCollection """
        pass

    def OnMapAdded(self, args):
        """ OnMapAdded(self: AcMapMapManagementService, args: AcMapMappingEventArgs) """
        pass

    def OnMapBecameCurrent(self, args):
        """ OnMapBecameCurrent(self: AcMapMapManagementService, args: AcMapMapChangeEventArgs) """
        pass

    def OnMapRemoved(self, args):
        """ OnMapRemoved(self: AcMapMapManagementService, args: AcMapMappingEventArgs) """
        pass

    def OnMapRenamed(self, args):
        """ OnMapRenamed(self: AcMapMapManagementService, args: AcMapMapChangeEventArgs) """
        pass

    def OnMapToBecomeCurrent(self, args):
        """ OnMapToBecomeCurrent(self: AcMapMapManagementService, args: AcMapMapChangeEventArgs) """
        pass

    def SetCurrentMap(self, map):
        """ SetCurrentMap(self: AcMapMapManagementService, map: AcMapMap) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    CurrentMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentMap(self: AcMapMapManagementService) -> AcMapMap

Set: CurrentMap(self: AcMapMapManagementService) = value
"""

    Maps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Maps(self: AcMapMapManagementService) -> AcMapMapCollection

"""


    MapAdded = None
    MapBecameCurrent = None
    MapRemoved = None
    MapRenamed = None
    MapToBecomeCurrent = None
    swigCMemOwn = None


class AcMapMapObjectModifiedEventArgs(AcMapMappingEventArgs):
    """
    AcMapMapObjectModifiedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapMapObjectModifiedEventArgs(name: str, pMap: AcMapMap, modificationBits: int)
    """
    def Dispose(self):
        """ Dispose(self: AcMapMapObjectModifiedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapMapObjectModifiedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapMapObjectModifiedEventArgs) -> IntPtr """
        pass

    def GetModification(self):
        """ GetModification(self: AcMapMapObjectModifiedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, pMap: AcMapMap, modificationBits: int)
        """
        pass

    Modification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modification(self: AcMapMapObjectModifiedEventArgs) -> int

"""


    swigCMemOwn = None


class AcMapMapObjectModifiedEventInfo(object):
    """ AcMapMapObjectModifiedEventInfo() """
    LayerSelectability = 4
    Name = 1
    ParentChanged = 8
    Visibility = 2


class AcMapPrintLayoutElementModifiedEventInfo(object):
    """ AcMapPrintLayoutElementModifiedEventInfo() """
    MapViewport_AssociatedMapErased = 2
    MapViewport_AssociatedMapUnerased = 3
    MapViewport_HiddenLayersChanged = 5
    MapViewport_MapAssociationChanged = 1
    MapViewport_NoChange = 0
    MapViewport_ViewportModified = 6
    MapViewport_ViewportScaleModified = 9


class AcMapResourceEventArgs(AcMapEventArgs):
    """
    AcMapResourceEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapResourceEventArgs(resource: MgResourceIdentifier)
    """
    def Dispose(self):
        """ Dispose(self: AcMapResourceEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapResourceEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapResourceEventArgs) -> IntPtr """
        pass

    def GetResourceIdentifier(self):
        """ GetResourceIdentifier(self: AcMapResourceEventArgs) -> MgResourceIdentifier """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: MgResourceIdentifier)
        """
        pass

    ResourceIdentifier = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResourceIdentifier(self: AcMapResourceEventArgs) -> MgResourceIdentifier

"""


    swigCMemOwn = None


class AcMapResourceService(MgResourceService):
    """ AcMapResourceService(cPtr: IntPtr, cMemoryOwn: bool) """
    def ApplyResourcePackage(self, resourcePackage):
        """ ApplyResourcePackage(self: AcMapResourceService, resourcePackage: MgByteReader) """
        pass

    def ChangeResourceOwner(self, resource, owner, includeDescendants):
        """ ChangeResourceOwner(self: AcMapResourceService, resource: MgResourceIdentifier, owner: str, includeDescendants: bool) """
        pass

    def CopyResource(self, sourceResource, destResource, overwrite):
        """ CopyResource(self: AcMapResourceService, sourceResource: MgResourceIdentifier, destResource: MgResourceIdentifier, overwrite: bool) """
        pass

    def DeleteResource(self, resource):
        """ DeleteResource(self: AcMapResourceService, resource: MgResourceIdentifier) """
        pass

    def DeleteResourceData(self, resource, dataName):
        """ DeleteResourceData(self: AcMapResourceService, resource: MgResourceIdentifier, dataName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapResourceService) """
        pass

    def EnumerateReferences(self, resource):
        """ EnumerateReferences(self: AcMapResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def EnumerateResourceData(self, resource):
        """ EnumerateResourceData(self: AcMapResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapResourceService) -> IntPtr """
        pass

    def GetGlobalResourceId(self, globalResourceId):
        """ GetGlobalResourceId(self: AcMapResourceService, globalResourceId: MgResourceIdentifier) -> MgResourceIdentifier """
        pass

    def GetLatestResourceContent(self, resource, preProcessTags):
        """ GetLatestResourceContent(self: AcMapResourceService, resource: MgResourceIdentifier, preProcessTags: str) -> MgByteReader """
        pass

    def GetName(self, resource):
        """ GetName(self: AcMapResourceService, resource: MgResourceIdentifier) -> str """
        pass

    def GetRepositoryContent(self, resource):
        """ GetRepositoryContent(self: AcMapResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetRepositoryHeader(self, resource):
        """ GetRepositoryHeader(self: AcMapResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetResourceData(self, resource, dataName):
        """ GetResourceData(self: AcMapResourceService, resource: MgResourceIdentifier, dataName: str) -> MgByteReader """
        pass

    def GetResourceHeader(self, resource):
        """ GetResourceHeader(self: AcMapResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetResourceMetadata(self, resource):
        """ GetResourceMetadata(self: AcMapResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def InheritPermissionsFrom(self, resource):
        """ InheritPermissionsFrom(self: AcMapResourceService, resource: MgResourceIdentifier) """
        pass

    def MoveResource(self, sourceResource, destResource, overwrite, cascade=None):
        """ MoveResource(self: AcMapResourceService, sourceResource: MgResourceIdentifier, destResource: MgResourceIdentifier, overwrite: bool) """
        pass

    def OnResourceAdded(self, args):
        """ OnResourceAdded(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceAdditionCancelled(self, args):
        """ OnResourceAdditionCancelled(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceModificationCancelled(self, args):
        """ OnResourceModificationCancelled(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceModified(self, args):
        """ OnResourceModified(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceRemovalCancelled(self, args):
        """ OnResourceRemovalCancelled(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceRemoved(self, args):
        """ OnResourceRemoved(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceToBeAdded(self, args):
        """ OnResourceToBeAdded(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceToBeModified(self, args):
        """ OnResourceToBeModified(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def OnResourceToBeRemoved(self, args):
        """ OnResourceToBeRemoved(self: AcMapResourceService, args: AcMapResourceEventArgs) """
        pass

    def RenameResourceData(self, resource, oldDataName, newDataName, overwrite):
        """ RenameResourceData(self: AcMapResourceService, resource: MgResourceIdentifier, oldDataName: str, newDataName: str, overwrite: bool) """
        pass

    def ResourceExists(self, resource):
        """ ResourceExists(self: AcMapResourceService, resource: MgResourceIdentifier) -> bool """
        pass

    def SetResource(self, resource, content, header):
        """ SetResource(self: AcMapResourceService, resource: MgResourceIdentifier, content: MgByteReader, header: MgByteReader) """
        pass

    def SetResourceData(self, resource, dataName, dataType, data):
        """ SetResourceData(self: AcMapResourceService, resource: MgResourceIdentifier, dataName: str, dataType: str, data: MgByteReader) """
        pass

    def SetResourceMetadata(self, resource, content):
        """ SetResourceMetadata(self: AcMapResourceService, resource: MgResourceIdentifier, content: MgByteReader) """
        pass

    def UpdateRepository(self, resource, content, header):
        """ UpdateRepository(self: AcMapResourceService, resource: MgResourceIdentifier, content: MgByteReader, header: MgByteReader) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    ResourceAdded = None
    ResourceAdditionCancelled = None
    ResourceModificationCancelled = None
    ResourceModified = None
    ResourceRemovalCancelled = None
    ResourceRemoved = None
    ResourceToBeAdded = None
    ResourceToBeModified = None
    ResourceToBeRemoved = None
    swigCMemOwn = None


class AcMapSelection(MgSelectionBase):
    """
    AcMapSelection(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapSelection(map: AcMapMap)
    AcMapSelection(map: AcMapMap, xmlSelectionString: str)
    """
    def Dispose(self):
        """ Dispose(self: AcMapSelection) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapSelection) -> IntPtr """
        pass

    def GetSelectedFeatures(self, layer, featureClass, *__args):
        """
        GetSelectedFeatures(self: AcMapSelection, layer: MgLayerBase, featureClass: str, propertyNames: MgStringCollection) -> MgFeatureReader
        GetSelectedFeatures(self: AcMapSelection, layer: MgLayerBase, featureClass: str, mappedOnly: bool) -> MgFeatureReader
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, map: AcMapMap)
        __new__(cls: type, map: AcMapMap, xmlSelectionString: str)
        """
        pass

    swigCMemOwn = None


class AcMapServiceFactory(object):
    """ AcMapServiceFactory(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapServiceFactory) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapServiceFactory) -> IntPtr """
        pass

    @staticmethod
    def GetService(serviceType):
        """ GetService(serviceType: int) -> MgService """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AcMapSqlDataReader(MgSqlDataReader):
    """ AcMapSqlDataReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Close(self):
        """ Close(self: AcMapSqlDataReader) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapSqlDataReader) """
        pass

    def GetBLOB(self, *__args):
        """
        GetBLOB(self: AcMapSqlDataReader, index: int) -> MgByteReader
        GetBLOB(self: AcMapSqlDataReader, propertyName: str) -> MgByteReader
        """
        pass

    def GetBoolean(self, *__args):
        """
        GetBoolean(self: AcMapSqlDataReader, index: int) -> bool
        GetBoolean(self: AcMapSqlDataReader, propertyName: str) -> bool
        """
        pass

    def GetByte(self, *__args):
        """
        GetByte(self: AcMapSqlDataReader, index: int) -> Byte
        GetByte(self: AcMapSqlDataReader, propertyName: str) -> Byte
        """
        pass

    def GetCLOB(self, *__args):
        """
        GetCLOB(self: AcMapSqlDataReader, index: int) -> MgByteReader
        GetCLOB(self: AcMapSqlDataReader, propertyName: str) -> MgByteReader
        """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapSqlDataReader) -> IntPtr """
        pass

    def GetDateTime(self, *__args):
        """
        GetDateTime(self: AcMapSqlDataReader, index: int) -> MgDateTime
        GetDateTime(self: AcMapSqlDataReader, propertyName: str) -> MgDateTime
        """
        pass

    def GetDouble(self, *__args):
        """
        GetDouble(self: AcMapSqlDataReader, index: int) -> float
        GetDouble(self: AcMapSqlDataReader, propertyName: str) -> float
        """
        pass

    def GetGeometry(self, *__args):
        """
        GetGeometry(self: AcMapSqlDataReader, index: int) -> MgByteReader
        GetGeometry(self: AcMapSqlDataReader, propertyName: str) -> MgByteReader
        """
        pass

    def GetInt16(self, *__args):
        """
        GetInt16(self: AcMapSqlDataReader, index: int) -> Int16
        GetInt16(self: AcMapSqlDataReader, propertyName: str) -> Int16
        """
        pass

    def GetInt32(self, *__args):
        """
        GetInt32(self: AcMapSqlDataReader, index: int) -> int
        GetInt32(self: AcMapSqlDataReader, propertyName: str) -> int
        """
        pass

    def GetInt64(self, *__args):
        """
        GetInt64(self: AcMapSqlDataReader, index: int) -> Int64
        GetInt64(self: AcMapSqlDataReader, propertyName: str) -> Int64
        """
        pass

    def GetPropertyCount(self):
        """ GetPropertyCount(self: AcMapSqlDataReader) -> int """
        pass

    def GetPropertyIndex(self, propertyName):
        """ GetPropertyIndex(self: AcMapSqlDataReader, propertyName: str) -> int """
        pass

    def GetPropertyName(self, index):
        """ GetPropertyName(self: AcMapSqlDataReader, index: int) -> str """
        pass

    def GetPropertyType(self, *__args):
        """
        GetPropertyType(self: AcMapSqlDataReader, index: int) -> int
        GetPropertyType(self: AcMapSqlDataReader, propertyName: str) -> int
        """
        pass

    def GetRaster(self, *__args):
        """
        GetRaster(self: AcMapSqlDataReader, index: int) -> MgRaster
        GetRaster(self: AcMapSqlDataReader, propertyName: str) -> MgRaster
        """
        pass

    def GetSingle(self, *__args):
        """
        GetSingle(self: AcMapSqlDataReader, index: int) -> Single
        GetSingle(self: AcMapSqlDataReader, propertyName: str) -> Single
        """
        pass

    def GetString(self, *__args):
        """
        GetString(self: AcMapSqlDataReader, index: int) -> str
        GetString(self: AcMapSqlDataReader, propertyName: str) -> str
        """
        pass

    def IsNull(self, *__args):
        """
        IsNull(self: AcMapSqlDataReader, index: int) -> bool
        IsNull(self: AcMapSqlDataReader, propertyName: str) -> bool
        """
        pass

    def ReadNext(self):
        """ ReadNext(self: AcMapSqlDataReader) -> bool """
        pass

    def ToXml(self):
        """ ToXml(self: AcMapSqlDataReader) -> MgByteReader """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AddDigitizePromptHandler(MulticastDelegate):
    """ AddDigitizePromptHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: AddDigitizePromptHandler, sender: object, args: AcMapEditingDigitizeAddPromptArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AddDigitizePromptHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: AddDigitizePromptHandler, sender: object, args: AcMapEditingDigitizeAddPromptArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class AllLayerLoadingFinishedEventArgs(AcMapEventArgs):
    """
    AllLayerLoadingFinishedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AllLayerLoadingFinishedEventArgs()
    """
    def Dispose(self):
        """ Dispose(self: AllLayerLoadingFinishedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AllLayerLoadingFinishedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AllLayerLoadingFinishedEventArgs) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AllLayerLoadingFinishedHandler(MulticastDelegate):
    """ AllLayerLoadingFinishedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: AllLayerLoadingFinishedHandler, sender: object, args: AllLayerLoadingFinishedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AllLayerLoadingFinishedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: AllLayerLoadingFinishedHandler, sender: object, args: AllLayerLoadingFinishedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class BulkCommandEndedOrCancelledHandler(MulticastDelegate):
    """ BulkCommandEndedOrCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: BulkCommandEndedOrCancelledHandler, sender: object, args: AcMapBulkCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BulkCommandEndedOrCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: BulkCommandEndedOrCancelledHandler, sender: object, args: AcMapBulkCommandEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class BulkCommandStartedHandler(MulticastDelegate):
    """ BulkCommandStartedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: BulkCommandStartedHandler, sender: object, args: AcMapBulkCommandEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BulkCommandStartedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: BulkCommandStartedHandler, sender: object, args: AcMapBulkCommandEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class BulkFeaturesToBeErasedHandler(MulticastDelegate):
    """ BulkFeaturesToBeErasedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: BulkFeaturesToBeErasedHandler, sender: object, args: AcMapBulkFeaturesToBeErasedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BulkFeaturesToBeErasedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: BulkFeaturesToBeErasedHandler, sender: object, args: AcMapBulkFeaturesToBeErasedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ClassSystemProperties(object):
    """ ClassSystemProperties() """
    FeatureLockStatus = 'GwsLockMode'
    FeatureStatus = 'GwsStatus'
    FeatureStatusDeleted = 4
    FeatureStatusModified = 2
    FeatureStatusNew = 1
    SessionId = 'GwsId'


class ColumnType(object):
    """ ColumnType() """
    DescriptionColumn = 5
    IdColumn = 4
    NotDefined = 0
    XColumn = 1
    YColumn = 2
    ZColumn = 3


class CreateCommandInvokedHandler(MulticastDelegate):
    """ CreateCommandInvokedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: CreateCommandInvokedHandler, sender: object, args: AcMapCommandInvokedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CreateCommandInvokedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: CreateCommandInvokedHandler, sender: object, args: AcMapCommandInvokedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class DigitizeKeyWordSelectedHandler(MulticastDelegate):
    """ DigitizeKeyWordSelectedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: DigitizeKeyWordSelectedHandler, sender: object, args: AcMapEditingKeyWordSelectedArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: DigitizeKeyWordSelectedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: DigitizeKeyWordSelectedHandler, sender: object, args: AcMapEditingKeyWordSelectedArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class EditMode(object):
    """ EditMode() """
    DirectUpdate = 1
    EditSet = 0


class EntityType(object):
    """ EntityType() """
    AutoCADEntity = 0
    BulkEntity = 2
    FeatureEntity = 1


class FeatureDeleteCancelledHandler(MulticastDelegate):
    """ FeatureDeleteCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureDeleteCancelledHandler, sender: object, args: AcMapFeatureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureDeleteCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureDeleteCancelledHandler, sender: object, args: AcMapFeatureEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureDeletedHandler(MulticastDelegate):
    """ FeatureDeletedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureDeletedHandler, sender: object, args: AcMapFeatureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureDeletedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureDeletedHandler, sender: object, args: AcMapFeatureEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureDigitizeCanceledHandler(MulticastDelegate):
    """ FeatureDigitizeCanceledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureDigitizeCanceledHandler, sender: object, args: AcMapEditingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureDigitizeCanceledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureDigitizeCanceledHandler, sender: object, args: AcMapEditingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureDigitizedHandler(MulticastDelegate):
    """ FeatureDigitizedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureDigitizedHandler, sender: object, args: AcMapEditingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureDigitizedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureDigitizedHandler, sender: object, args: AcMapEditingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureDigitizeUpdatedHandler(MulticastDelegate):
    """ FeatureDigitizeUpdatedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureDigitizeUpdatedHandler, sender: object, args: AcMapEditingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureDigitizeUpdatedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureDigitizeUpdatedHandler, sender: object, args: AcMapEditingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInsertCancelledHandler(MulticastDelegate):
    """ FeatureInsertCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInsertCancelledHandler, sender: object, args: AcMapFeatureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInsertCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInsertCancelledHandler, sender: object, args: AcMapFeatureEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInsertedHandler(MulticastDelegate):
    """ FeatureInsertedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInsertedHandler, sender: object, args: AcMapFeatureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInsertedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInsertedHandler, sender: object, args: AcMapFeatureEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInstanceAddedEventArgs(AcMapEventArgs):
    """
    FeatureInstanceAddedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    FeatureInstanceAddedEventArgs(cacheId: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: FeatureInstanceAddedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: FeatureInstanceAddedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: FeatureInstanceAddedEventArgs) -> IntPtr """
        pass

    def GetLayer(self):
        """ GetLayer(self: FeatureInstanceAddedEventArgs) -> AcMapLayer """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: FeatureInstanceAddedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, cacheId: int, pLayer: AcMapLayer)
        """
        pass

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: FeatureInstanceAddedEventArgs) -> AcMapLayer

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: FeatureInstanceAddedEventArgs) -> int

"""


    swigCMemOwn = None


class FeatureInstanceAddedHandler(MulticastDelegate):
    """ FeatureInstanceAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInstanceAddedHandler, sender: object, args: FeatureInstanceAddedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInstanceAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInstanceAddedHandler, sender: object, args: FeatureInstanceAddedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInstanceModifiedEventArgs(AcMapEventArgs):
    """
    FeatureInstanceModifiedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    FeatureInstanceModifiedEventArgs(cacheId: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: FeatureInstanceModifiedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: FeatureInstanceModifiedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: FeatureInstanceModifiedEventArgs) -> IntPtr """
        pass

    def GetLayer(self):
        """ GetLayer(self: FeatureInstanceModifiedEventArgs) -> AcMapLayer """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: FeatureInstanceModifiedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, cacheId: int, pLayer: AcMapLayer)
        """
        pass

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: FeatureInstanceModifiedEventArgs) -> AcMapLayer

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: FeatureInstanceModifiedEventArgs) -> int

"""


    swigCMemOwn = None


class FeatureInstanceModifiedHandler(MulticastDelegate):
    """ FeatureInstanceModifiedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInstanceModifiedHandler, sender: object, args: FeatureInstanceModifiedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInstanceModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInstanceModifiedHandler, sender: object, args: FeatureInstanceModifiedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInstanceRemovedEventArgs(AcMapEventArgs):
    """
    FeatureInstanceRemovedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    FeatureInstanceRemovedEventArgs(cacheId: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: FeatureInstanceRemovedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: FeatureInstanceRemovedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: FeatureInstanceRemovedEventArgs) -> IntPtr """
        pass

    def GetLayer(self):
        """ GetLayer(self: FeatureInstanceRemovedEventArgs) -> AcMapLayer """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: FeatureInstanceRemovedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, cacheId: int, pLayer: AcMapLayer)
        """
        pass

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: FeatureInstanceRemovedEventArgs) -> AcMapLayer

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: FeatureInstanceRemovedEventArgs) -> int

"""


    swigCMemOwn = None


class FeatureInstanceRemovedHandler(MulticastDelegate):
    """ FeatureInstanceRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInstanceRemovedHandler, sender: object, args: FeatureInstanceRemovedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInstanceRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInstanceRemovedHandler, sender: object, args: FeatureInstanceRemovedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInstanceToBeAddedEventArgs(AcMapEventArgs):
    """
    FeatureInstanceToBeAddedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    FeatureInstanceToBeAddedEventArgs(cacheId: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: FeatureInstanceToBeAddedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: FeatureInstanceToBeAddedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: FeatureInstanceToBeAddedEventArgs) -> IntPtr """
        pass

    def GetLayer(self):
        """ GetLayer(self: FeatureInstanceToBeAddedEventArgs) -> AcMapLayer """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: FeatureInstanceToBeAddedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, cacheId: int, pLayer: AcMapLayer)
        """
        pass

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: FeatureInstanceToBeAddedEventArgs) -> AcMapLayer

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: FeatureInstanceToBeAddedEventArgs) -> int

"""


    swigCMemOwn = None


class FeatureInstanceToBeAddedHandler(MulticastDelegate):
    """ FeatureInstanceToBeAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInstanceToBeAddedHandler, sender: object, args: FeatureInstanceToBeAddedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInstanceToBeAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInstanceToBeAddedHandler, sender: object, args: FeatureInstanceToBeAddedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInstanceToBeModifiedEventArgs(AcMapEventArgs):
    """
    FeatureInstanceToBeModifiedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    FeatureInstanceToBeModifiedEventArgs(cacheId: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: FeatureInstanceToBeModifiedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: FeatureInstanceToBeModifiedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: FeatureInstanceToBeModifiedEventArgs) -> IntPtr """
        pass

    def GetLayer(self):
        """ GetLayer(self: FeatureInstanceToBeModifiedEventArgs) -> AcMapLayer """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: FeatureInstanceToBeModifiedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, cacheId: int, pLayer: AcMapLayer)
        """
        pass

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: FeatureInstanceToBeModifiedEventArgs) -> AcMapLayer

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: FeatureInstanceToBeModifiedEventArgs) -> int

"""


    swigCMemOwn = None


class FeatureInstanceToBeModifiedHandler(MulticastDelegate):
    """ FeatureInstanceToBeModifiedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInstanceToBeModifiedHandler, sender: object, args: FeatureInstanceToBeModifiedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInstanceToBeModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInstanceToBeModifiedHandler, sender: object, args: FeatureInstanceToBeModifiedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureInstanceToBeRemovedEventArgs(AcMapEventArgs):
    """
    FeatureInstanceToBeRemovedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    FeatureInstanceToBeRemovedEventArgs(cacheId: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: FeatureInstanceToBeRemovedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: FeatureInstanceToBeRemovedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: FeatureInstanceToBeRemovedEventArgs) -> IntPtr """
        pass

    def GetLayer(self):
        """ GetLayer(self: FeatureInstanceToBeRemovedEventArgs) -> AcMapLayer """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: FeatureInstanceToBeRemovedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, cacheId: int, pLayer: AcMapLayer)
        """
        pass

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: FeatureInstanceToBeRemovedEventArgs) -> AcMapLayer

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: FeatureInstanceToBeRemovedEventArgs) -> int

"""


    swigCMemOwn = None


class FeatureInstanceToBeRemovedHandler(MulticastDelegate):
    """ FeatureInstanceToBeRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureInstanceToBeRemovedHandler, sender: object, args: FeatureInstanceToBeRemovedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureInstanceToBeRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureInstanceToBeRemovedHandler, sender: object, args: FeatureInstanceToBeRemovedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeaturesCloneCanceledHandler(MulticastDelegate):
    """ FeaturesCloneCanceledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeaturesCloneCanceledHandler, sender: object, args: AcMapCloningEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeaturesCloneCanceledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeaturesCloneCanceledHandler, sender: object, args: AcMapCloningEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeaturesClonedHandler(MulticastDelegate):
    """ FeaturesClonedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeaturesClonedHandler, sender: object, args: AcMapCloningEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeaturesClonedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeaturesClonedHandler, sender: object, args: AcMapCloningEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureSourceAddedHandler(MulticastDelegate):
    """ FeatureSourceAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, resource, callback, object):
        """ BeginInvoke(self: FeatureSourceAddedHandler, sender: object, resource: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureSourceAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, resource):
        """ Invoke(self: FeatureSourceAddedHandler, sender: object, resource: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureSourceConnectedHandler(MulticastDelegate):
    """ FeatureSourceConnectedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, resource, callback, object):
        """ BeginInvoke(self: FeatureSourceConnectedHandler, sender: object, resource: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureSourceConnectedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, resource):
        """ Invoke(self: FeatureSourceConnectedHandler, sender: object, resource: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureSourceDisconnectedHandler(MulticastDelegate):
    """ FeatureSourceDisconnectedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, resource, callback, object):
        """ BeginInvoke(self: FeatureSourceDisconnectedHandler, sender: object, resource: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureSourceDisconnectedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, resource):
        """ Invoke(self: FeatureSourceDisconnectedHandler, sender: object, resource: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureSourceRemovedHandler(MulticastDelegate):
    """ FeatureSourceRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, resource, callback, object):
        """ BeginInvoke(self: FeatureSourceRemovedHandler, sender: object, resource: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureSourceRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, resource):
        """ Invoke(self: FeatureSourceRemovedHandler, sender: object, resource: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeaturesToBeClonedHandler(MulticastDelegate):
    """ FeaturesToBeClonedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeaturesToBeClonedHandler, sender: object, args: AcMapCloningCancelHandledEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeaturesToBeClonedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeaturesToBeClonedHandler, sender: object, args: AcMapCloningCancelHandledEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureToBeDeletedHandler(MulticastDelegate):
    """ FeatureToBeDeletedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureToBeDeletedHandler, sender: object, args: AcMapFeatureToBeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureToBeDeletedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureToBeDeletedHandler, sender: object, args: AcMapFeatureToBeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureToBeDigitizedHandler(MulticastDelegate):
    """ FeatureToBeDigitizedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureToBeDigitizedHandler, sender: object, args: AcMapEditingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureToBeDigitizedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureToBeDigitizedHandler, sender: object, args: AcMapEditingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureToBeGripEditedHandler(MulticastDelegate):
    """ FeatureToBeGripEditedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureToBeGripEditedHandler, sender: object, args: AcMapGripEditEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureToBeGripEditedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureToBeGripEditedHandler, sender: object, args: AcMapGripEditEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureToBeInsertedHandler(MulticastDelegate):
    """ FeatureToBeInsertedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureToBeInsertedHandler, sender: object, args: AcMapFeatureToBeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureToBeInsertedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureToBeInsertedHandler, sender: object, args: AcMapFeatureToBeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureToBeUpdatedHandler(MulticastDelegate):
    """ FeatureToBeUpdatedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureToBeUpdatedHandler, sender: object, args: AcMapFeatureToBeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureToBeUpdatedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureToBeUpdatedHandler, sender: object, args: AcMapFeatureToBeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureUpdateCancelledHandler(MulticastDelegate):
    """ FeatureUpdateCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureUpdateCancelledHandler, sender: object, args: AcMapFeatureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureUpdateCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureUpdateCancelledHandler, sender: object, args: AcMapFeatureEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class FeatureUpdatedHandler(MulticastDelegate):
    """ FeatureUpdatedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: FeatureUpdatedHandler, sender: object, args: AcMapFeatureEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: FeatureUpdatedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: FeatureUpdatedHandler, sender: object, args: AcMapFeatureEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class GripEditBeginHandler(MulticastDelegate):
    """ GripEditBeginHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: GripEditBeginHandler, sender: object, args: AcMapGripEditEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GripEditBeginHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: GripEditBeginHandler, sender: object, args: AcMapGripEditEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class GripEditDragHandler(MulticastDelegate):
    """ GripEditDragHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: GripEditDragHandler, sender: object, args: AcMapGripEditEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GripEditDragHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: GripEditDragHandler, sender: object, args: AcMapGripEditEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class GripEditEndHandler(MulticastDelegate):
    """ GripEditEndHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: GripEditEndHandler, sender: object, args: AcMapGripEditEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GripEditEndHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: GripEditEndHandler, sender: object, args: AcMapGripEditEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class GroupAddedHandler(MulticastDelegate):
    """ GroupAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: GroupAddedHandler, sender: object, args: AcMapMappingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GroupAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: GroupAddedHandler, sender: object, args: AcMapMappingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class GroupModifiedHandler(MulticastDelegate):
    """ GroupModifiedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: GroupModifiedHandler, sender: object, args: AcMapMapObjectModifiedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GroupModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: GroupModifiedHandler, sender: object, args: AcMapMapObjectModifiedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class GroupRemovedHandler(MulticastDelegate):
    """ GroupRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: GroupRemovedHandler, sender: object, args: AcMapMappingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GroupRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: GroupRemovedHandler, sender: object, args: AcMapMappingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class IsEditingCloningSupportedHandler(MulticastDelegate):
    """ IsEditingCloningSupportedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: IsEditingCloningSupportedHandler, sender: object, args: AcMapEditingCloningSupportedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: IsEditingCloningSupportedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: IsEditingCloningSupportedHandler, sender: object, args: AcMapEditingCloningSupportedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LayerAddedHandler(MulticastDelegate):
    """ LayerAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LayerAddedHandler, sender: object, args: AcMapMappingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayerAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LayerAddedHandler, sender: object, args: AcMapMappingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LayerCacheLoadingEndedEventArgs(AcMapEventArgs):
    """
    LayerCacheLoadingEndedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    LayerCacheLoadingEndedEventArgs(name: str)
    """
    def Dispose(self):
        """ Dispose(self: LayerCacheLoadingEndedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: LayerCacheLoadingEndedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: LayerCacheLoadingEndedEventArgs) -> IntPtr """
        pass

    def GetLayerName(self):
        """ GetLayerName(self: LayerCacheLoadingEndedEventArgs) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    LayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerName(self: LayerCacheLoadingEndedEventArgs) -> str

"""


    swigCMemOwn = None


class LayerCacheLoadingEndedHandler(MulticastDelegate):
    """ LayerCacheLoadingEndedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LayerCacheLoadingEndedHandler, sender: object, args: LayerCacheLoadingEndedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayerCacheLoadingEndedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LayerCacheLoadingEndedHandler, sender: object, args: LayerCacheLoadingEndedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LayerCacheLoadingStartedEventArgs(AcMapEventArgs):
    """
    LayerCacheLoadingStartedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    LayerCacheLoadingStartedEventArgs(name: str)
    """
    def Dispose(self):
        """ Dispose(self: LayerCacheLoadingStartedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: LayerCacheLoadingStartedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: LayerCacheLoadingStartedEventArgs) -> IntPtr """
        pass

    def GetLayerName(self):
        """ GetLayerName(self: LayerCacheLoadingStartedEventArgs) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    LayerName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerName(self: LayerCacheLoadingStartedEventArgs) -> str

"""


    swigCMemOwn = None


class LayerCacheLoadingStartedHandler(MulticastDelegate):
    """ LayerCacheLoadingStartedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LayerCacheLoadingStartedHandler, sender: object, args: LayerCacheLoadingStartedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayerCacheLoadingStartedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LayerCacheLoadingStartedHandler, sender: object, args: LayerCacheLoadingStartedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LayerInitializedHandler(MulticastDelegate):
    """ LayerInitializedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LayerInitializedHandler, sender: object, args: AcMapMappingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayerInitializedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LayerInitializedHandler, sender: object, args: AcMapMappingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LayerModifiedHandler(MulticastDelegate):
    """ LayerModifiedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LayerModifiedHandler, sender: object, args: AcMapMapObjectModifiedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayerModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LayerModifiedHandler, sender: object, args: AcMapMapObjectModifiedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LayerRemovedHandler(MulticastDelegate):
    """ LayerRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LayerRemovedHandler, sender: object, args: AcMapMappingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LayerRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LayerRemovedHandler, sender: object, args: AcMapMappingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LongTransactionActivateCancelledHandler(MulticastDelegate):
    """ LongTransactionActivateCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LongTransactionActivateCancelledHandler, sender: object, args: AcMapLongTransactionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LongTransactionActivateCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LongTransactionActivateCancelledHandler, sender: object, args: AcMapLongTransactionEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LongTransactionActivatedHandler(MulticastDelegate):
    """ LongTransactionActivatedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LongTransactionActivatedHandler, sender: object, args: AcMapLongTransactionEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LongTransactionActivatedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LongTransactionActivatedHandler, sender: object, args: AcMapLongTransactionEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class LongTransactionToBeActivatedHandler(MulticastDelegate):
    """ LongTransactionToBeActivatedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: LongTransactionToBeActivatedHandler, sender: object, args: AcMapLongTransactionToBeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: LongTransactionToBeActivatedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: LongTransactionToBeActivatedHandler, sender: object, args: AcMapLongTransactionToBeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class MapAddedHandler(MulticastDelegate):
    """ MapAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: MapAddedHandler, sender: object, args: AcMapMappingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MapAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: MapAddedHandler, sender: object, args: AcMapMappingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class MapApi(object):
    """ MapApi() """

class MapAppendContextMenuHandler(MulticastDelegate):
    """ MapAppendContextMenuHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: MapAppendContextMenuHandler, sender: object, args: AcMapContextMenuItemEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MapAppendContextMenuHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: MapAppendContextMenuHandler, sender: object, args: AcMapContextMenuItemEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class MapBecameCurrentHandler(MulticastDelegate):
    """ MapBecameCurrentHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: MapBecameCurrentHandler, sender: object, args: AcMapMapChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MapBecameCurrentHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: MapBecameCurrentHandler, sender: object, args: AcMapMapChangeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class MapRemovedHandler(MulticastDelegate):
    """ MapRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: MapRemovedHandler, sender: object, args: AcMapMappingEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MapRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: MapRemovedHandler, sender: object, args: AcMapMappingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class MapRenamedHandler(MulticastDelegate):
    """ MapRenamedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: MapRenamedHandler, sender: object, args: AcMapMapChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MapRenamedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: MapRenamedHandler, sender: object, args: AcMapMapChangeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class MapToBecomeCurrentHandler(MulticastDelegate):
    """ MapToBecomeCurrentHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: MapToBecomeCurrentHandler, sender: object, args: AcMapMapChangeEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: MapToBecomeCurrentHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: MapToBecomeCurrentHandler, sender: object, args: AcMapMapChangeEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class PrintLayoutElementAddedHandler(MulticastDelegate):
    """ PrintLayoutElementAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, pArgs, callback, object):
        """ BeginInvoke(self: PrintLayoutElementAddedHandler, sender: object, pArgs: AcMapPrintLayoutElementEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PrintLayoutElementAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, pArgs):
        """ Invoke(self: PrintLayoutElementAddedHandler, sender: object, pArgs: AcMapPrintLayoutElementEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class PrintLayoutElementModifiedHandler(MulticastDelegate):
    """ PrintLayoutElementModifiedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, pArgs, callback, object):
        """ BeginInvoke(self: PrintLayoutElementModifiedHandler, sender: object, pArgs: AcMapPrintLayoutElementModifiedEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PrintLayoutElementModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, pArgs):
        """ Invoke(self: PrintLayoutElementModifiedHandler, sender: object, pArgs: AcMapPrintLayoutElementModifiedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class PrintLayoutElementRemovedHandler(MulticastDelegate):
    """ PrintLayoutElementRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, pArgs, callback, object):
        """ BeginInvoke(self: PrintLayoutElementRemovedHandler, sender: object, pArgs: AcMapPrintLayoutElementEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PrintLayoutElementRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, pArgs):
        """ Invoke(self: PrintLayoutElementRemovedHandler, sender: object, pArgs: AcMapPrintLayoutElementEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceAddedHandler(MulticastDelegate):
    """ ResourceAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceAddedHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceAddedHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceAdditionCancelledHandler(MulticastDelegate):
    """ ResourceAdditionCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceAdditionCancelledHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceAdditionCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceAdditionCancelledHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceModificationCancelledHandler(MulticastDelegate):
    """ ResourceModificationCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceModificationCancelledHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceModificationCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceModificationCancelledHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceModifiedHandler(MulticastDelegate):
    """ ResourceModifiedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceModifiedHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceModifiedHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceRemovalCancelledHandler(MulticastDelegate):
    """ ResourceRemovalCancelledHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceRemovalCancelledHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceRemovalCancelledHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceRemovalCancelledHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceRemovedHandler(MulticastDelegate):
    """ ResourceRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceRemovedHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceRemovedHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceToBeAddedHandler(MulticastDelegate):
    """ ResourceToBeAddedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceToBeAddedHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceToBeAddedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceToBeAddedHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceToBeModifiedHandler(MulticastDelegate):
    """ ResourceToBeModifiedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceToBeModifiedHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceToBeModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceToBeModifiedHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class ResourceToBeRemovedHandler(MulticastDelegate):
    """ ResourceToBeRemovedHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: ResourceToBeRemovedHandler, sender: object, args: AcMapResourceEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ResourceToBeRemovedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: ResourceToBeRemovedHandler, sender: object, args: AcMapResourceEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


class SchemaEditorOpeningHandler(MulticastDelegate):
    """ SchemaEditorOpeningHandler(object: object, method: IntPtr) """
    def BeginInvoke(self, sender, args, callback, object):
        """ BeginInvoke(self: SchemaEditorOpeningHandler, sender: object, args: SchemaEditorOpeningEventArgs, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SchemaEditorOpeningHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, args):
        """ Invoke(self: SchemaEditorOpeningHandler, sender: object, args: SchemaEditorOpeningEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass


# variables with complex values

