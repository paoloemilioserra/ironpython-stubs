# encoding: utf-8
# module Autodesk.AutoCAD.DynamoApp.Services calls itself Services
# from AcDynamoServices, Version=13.3.860.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DisposeLogic(object):
    """ DisposeLogic() """
    DisableDispose = False
    IsClosingHomeworkspace = False
    IsDestroyingDocument = False
    IsShuttingDown = False


class DocumentContext(object):
    """
    DocumentContext(db: Database)
    DocumentContext(db: Database, tearDownOnDispose: bool)
    DocumentContext(doc: Document)
    DocumentContext(doc: Document, tearDownOnDispose: bool)
    """
    def Dispose(self):
        """ Dispose(self: DocumentContext) """
        pass

    @staticmethod
    def GetObjectId(*__args):
        """
        GetObjectId(self: DocumentContext, handle: str) -> ObjectId
        GetObjectId(db: Database, handle: str) -> ObjectId
        """
        pass

    def GetTransaction(self, doc):
        """ GetTransaction(self: DocumentContext, doc: Document) -> Transaction """
        pass

    @staticmethod
    def OnModelRefreshCompleted():
        """ OnModelRefreshCompleted() """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, db: Database)
        __new__(cls: type, db: Database, tearDownOnDispose: bool)
        __new__(cls: type, doc: Document)
        __new__(cls: type, doc: Document, tearDownOnDispose: bool)
        """
        pass

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: DocumentContext) -> Database

"""

    Document = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Document(self: DocumentContext) -> Document

"""

    Transaction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Transaction(self: DocumentContext) -> Transaction

"""


    EvaluationInProgress = False
    MdiActiveDocument = None
    StartupDocument = None


class DrawingReactors(object):
    # no doc
    def Dispose(self):
        """ Dispose(self: DrawingReactors) """
        pass

    def setupDocumentReactors(self, doc):
        """ setupDocumentReactors(self: DrawingReactors, doc: Document) """
        pass

    def teardownDocumentReactors(self, doc):
        """ teardownDocumentReactors(self: DrawingReactors, doc: Document) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    CommandEnded = None
    DocumentActivated = None
    DocumentToBeDestroyed = None
    Instance = None
    ModelessOperationEnded = None
    ObjectUpdated = None


class DynamicUpdateLogic(object):
    """ DynamicUpdateLogic() """
    def CheckAndRun(self, model):
        """ CheckAndRun(self: DynamicUpdateLogic, model: DynamoModel) """
        pass

    def MarkNodeAsModified(self, node):
        """ MarkNodeAsModified(self: DynamicUpdateLogic, node: NodeModel) """
        pass

    Available = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Available(self: DynamicUpdateLogic) -> bool

"""

    ForceDisabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ForceDisabled(self: DynamicUpdateLogic) -> bool

Set: ForceDisabled(self: DynamicUpdateLogic) = value
"""

    HasModifiedNodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasModifiedNodes(self: DynamicUpdateLogic) -> bool

"""


    Instance = None


class ElementBinder(object):
    """ ElementBinder() """
    @staticmethod
    def CleanupAndSetElementForTrace(handle):
        """ CleanupAndSetElementForTrace(handle: str) """
        pass

    @staticmethod
    def ClearInvalidHandlesBeforeFirstRun():
        """ ClearInvalidHandlesBeforeFirstRun() """
        pass

    @staticmethod
    def CollectInvalidHandlesBeforeFirstRun(db, hws, engine):
        """ CollectInvalidHandlesBeforeFirstRun(db: Database, hws: HomeWorkspaceModel, engine: EngineController) """
        pass

    @staticmethod
    def GetHandleFromTrace():
        """ GetHandleFromTrace() -> str """
        pass

    @staticmethod
    def GetNodesFromDBObject(handle, workspace, engine):
        """ GetNodesFromDBObject(handle: str, workspace: WorkspaceModel, engine: EngineController) -> IEnumerable[NodeModel] """
        pass

    @staticmethod
    def GetObjectIdFromTrace(db):
        """ GetObjectIdFromTrace(db: Database) -> ObjectId """
        pass

    @staticmethod
    def SetElementForTrace(handle):
        """ SetElementForTrace(handle: str) """
        pass

    @staticmethod
    def SetObjectIdForTrace(id):
        """ SetObjectIdForTrace(id: ObjectId) """
        pass

    IsEnabled = True


class IObjectDescriptorsRegister:
    # no doc
    def RegisterDescriptors(self):
        """ RegisterDescriptors(self: IObjectDescriptorsRegister) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LifecycleManager(object):
    # no doc
    def ClearAll(self):
        """ ClearAll(self: LifecycleManager[T]) """
        pass

    def GetDynamoOwnedRegisterCount(self, handle):
        """ GetDynamoOwnedRegisterCount(self: LifecycleManager[T], handle: T) -> int """
        pass

    def GetRegisteredCount(self, handle):
        """ GetRegisteredCount(self: LifecycleManager[T], handle: T) -> int """
        pass

    def IsAutoCADDeleted(self, handle):
        """ IsAutoCADDeleted(self: LifecycleManager[T], handle: T) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: LifecycleManager[T]) -> bool """
        pass

    def NotifyOfDeletion(self, handle):
        """ NotifyOfDeletion(self: LifecycleManager[T], handle: T) """
        pass

    def RegisterAsssociation(self, elementHandle, wrapper, isDynamoOwned):
        """ RegisterAsssociation(self: LifecycleManager[T], elementHandle: T, wrapper: object, isDynamoOwned: bool) """
        pass

    def UnRegisterAssociation(self, elementHandle, wrapper, isDynamoOwned):
        """ UnRegisterAssociation(self: LifecycleManager[T], elementHandle: T, wrapper: object, isDynamoOwned: bool) """
        pass

    def UpdateAllObjectsForEvaluation(self):
        """ UpdateAllObjectsForEvaluation(self: LifecycleManager[T]) """
        pass


class ObjectDescriptor(object):
    """ ObjectDescriptor() """
    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: ObjectDescriptor) -> str

Set: DisplayName(self: ObjectDescriptor) = value
"""

    DynamoCreator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DynamoCreator(self: ObjectDescriptor) -> Func[Entity, bool, object]

Set: DynamoCreator(self: ObjectDescriptor) = value
"""

    RXClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RXClass(self: ObjectDescriptor) -> RXClass

Set: RXClass(self: ObjectDescriptor) = value
"""

    ShowInDropDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ShowInDropDown(self: ObjectDescriptor) -> bool

Set: ShowInDropDown(self: ObjectDescriptor) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ObjectDescriptor) -> Type

Set: Type(self: ObjectDescriptor) = value
"""



class ObjectDescriptors(object):
    # no doc
    @staticmethod
    def AddRegister(typeName):
        """ AddRegister(typeName: str) """
        pass

    @staticmethod
    def GetAllObjectDescriptors():
        """ GetAllObjectDescriptors() -> IEnumerable[KeyValuePair[str, ObjectDescriptor]] """
        pass

    @staticmethod
    def GetDescriptorById(id):
        """ GetDescriptorById(id: ObjectId) -> ObjectDescriptor """
        pass

    @staticmethod
    def GetDescriptorByRXClass(cls):
        """ GetDescriptorByRXClass(cls: RXClass) -> ObjectDescriptor """
        pass

    @staticmethod
    def GetDescriptorByType(objectType):
        """ GetDescriptorByType(objectType: str) -> ObjectDescriptor """
        pass

    @staticmethod
    def RegisterObjectDescriptor(displayName, type, dynamoCreator, showInDropDown):
        """ RegisterObjectDescriptor(displayName: str, type: Type, dynamoCreator: Func[Entity, bool, object], showInDropDown: bool) """
        pass

    __all__ = [
        'AddRegister',
        'GetAllObjectDescriptors',
        'GetDescriptorById',
        'GetDescriptorByRXClass',
        'GetDescriptorByType',
        'RegisterObjectDescriptor',
    ]


class ObjectUpdateType(Enum):
    """ enum ObjectUpdateType, values: Added (0), Erased (2), Modified (1) """
    Added = None
    Erased = None
    Modified = None
    value__ = None


class SerializableHandle(object):
    """
    SerializableHandle()
    SerializableHandle(info: SerializationInfo, context: StreamingContext)
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: SerializableHandle, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, info=None, context=None):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    stringID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: stringID(self: SerializableHandle) -> str

Set: stringID(self: SerializableHandle) = value
"""



class TraceData(object):
    # no doc
    @staticmethod
    def GetFromDocument(document):
        """ GetFromDocument(document: Document) -> IDictionary[ObjectId, Guid] """
        pass

    @staticmethod
    def LoadFromDocument(hws):
        """ LoadFromDocument(hws: HomeWorkspaceModel) """
        pass

    @staticmethod
    def RemoveFromDocument(*__args):
        """ RemoveFromDocument(document: Document, objectId: ObjectId)RemoveFromDocument(document: Document)RemoveFromDocument(hws: HomeWorkspaceModel) """
        pass

    @staticmethod
    def SaveToDocument(hws):
        """ SaveToDocument(hws: HomeWorkspaceModel) """
        pass

    @staticmethod
    def UpdateSaveState():
        """ UpdateSaveState() """
        pass

    SaveState = None
    TraceDataState = None
    __all__ = [
        'GetFromDocument',
        'LoadFromDocument',
        'RemoveFromDocument',
        'SaveToDocument',
        'TraceDataState',
        'UpdateSaveState',
    ]


