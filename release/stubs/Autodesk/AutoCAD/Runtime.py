# encoding: utf-8
# module Autodesk.AutoCAD.Runtime calls itself Runtime
# from Acdbmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DisposableWrapper(MarshalByRefObject):
    # no doc
    @staticmethod
    def Create(type, unmanagedPointer, autoDelete):
        """ Create(type: Type, unmanagedPointer: IntPtr, autoDelete: bool) -> DisposableWrapper """
        pass

    def DeleteUnmanagedObject(self, *args): #cannot find CLR method
        """ DeleteUnmanagedObject(self: DisposableWrapper) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper) """
        pass

    def Equals(self, obj):
        """ Equals(self: DisposableWrapper, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: DisposableWrapper) -> int """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """
        __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool)
        __new__(cls: type)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    AutoDelete = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AutoDelete(self: DisposableWrapper) -> bool

"""

    IsDisposed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDisposed(self: DisposableWrapper) -> bool

"""

    UnmanagedObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnmanagedObject(self: DisposableWrapper) -> IntPtr

"""



class RXObject(DisposableWrapper):
    # no doc
    def Clone(self):
        """ Clone(self: RXObject) -> object """
        pass

    def CompareTo(self, obj):
        """ CompareTo(self: RXObject, obj: object) -> int """
        pass

    def CopyFrom(self, source):
        """ CopyFrom(self: RXObject, source: RXObject) """
        pass

    @staticmethod
    def Create(unmanagedPointer, autoDelete):
        """ Create(unmanagedPointer: IntPtr, autoDelete: bool) -> RXObject """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def GetClass(type):
        """ GetClass(type: Type) -> RXClass """
        pass

    def GetRXClass(self):
        """ GetRXClass(self: RXObject) -> RXClass """
        pass

    def QueryX(self, protocolClass):
        """ QueryX(self: RXObject, protocolClass: RXClass) -> IntPtr """
        pass

    def X(self, protocolClass):
        """ X(self: RXObject, protocolClass: RXClass) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass


class Dictionary(RXObject):
    # no doc
    def At(self, *__args):
        """
        At(self: Dictionary, key: str) -> RXObject
        At(self: Dictionary, id: int) -> RXObject
        """
        pass

    def AtKeyAndIdPut(self, newKey, id, value):
        """ AtKeyAndIdPut(self: Dictionary, newKey: str, id: int, value: RXObject) """
        pass

    def AtPut(self, *__args):
        """
        AtPut(self: Dictionary, key: str, value: RXObject) -> RXObject
        AtPut(self: Dictionary, key: str, value: RXObject) -> (RXObject, int)
        AtPut(self: Dictionary, id: int, value: RXObject) -> RXObject
        """
        pass

    def Contains(self, *__args):
        """
        Contains(self: Dictionary, key: str) -> bool
        Contains(self: Dictionary, id: int) -> bool
        """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: Dictionary, array: Array[DictionaryEntry], index: int) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Dictionary) -> IDictionaryEnumerator """
        pass

    def ICollection.CopyTo(self, *args): #cannot find CLR method
        """ ICollection.CopyTo(self: Dictionary, array: Array, index: int) """
        pass

    def IdAt(self, key):
        """ IdAt(self: Dictionary, key: str) -> int """
        pass

    def IDictionary.Add(self, *args): #cannot find CLR method
        """ IDictionary.Add(self: Dictionary, key: object, value: object) """
        pass

    def IDictionary.Clear(self, *args): #cannot find CLR method
        """ IDictionary.Clear(self: Dictionary) """
        pass

    def IDictionary.Contains(self, *args): #cannot find CLR method
        """ IDictionary.Contains(self: Dictionary, key: object) -> bool """
        pass

    def IDictionary.get_IsFixedSize(self, *args): #cannot find CLR method
        """ IDictionary.get_IsFixedSize(self: Dictionary) -> bool """
        pass

    def IDictionary.get_IsReadOnly(self, *args): #cannot find CLR method
        """ IDictionary.get_IsReadOnly(self: Dictionary) -> bool """
        pass

    def IDictionary.get_IsSynchronized(self, *args): #cannot find CLR method
        """ IDictionary.get_IsSynchronized(self: Dictionary) -> bool """
        pass

    def IDictionary.get_Item(self, *args): #cannot find CLR method
        """ IDictionary.get_Item(self: Dictionary, key: object) -> object """
        pass

    def IDictionary.get_Keys(self, *args): #cannot find CLR method
        """ IDictionary.get_Keys(self: Dictionary) -> ICollection """
        pass

    def IDictionary.get_SyncRoot(self, *args): #cannot find CLR method
        """ IDictionary.get_SyncRoot(self: Dictionary) -> object """
        pass

    def IDictionary.get_Values(self, *args): #cannot find CLR method
        """ IDictionary.get_Values(self: Dictionary) -> ICollection """
        pass

    def IDictionary.Remove(self, *args): #cannot find CLR method
        """ IDictionary.Remove(self: Dictionary, key: object) """
        pass

    def IDictionary.set_Item(self, *args): #cannot find CLR method
        """ IDictionary.set_Item(self: Dictionary, key: object, value: object) """
        pass

    def IEnumerable.GetEnumerator(self, *args): #cannot find CLR method
        """ IEnumerable.GetEnumerator(self: Dictionary) -> IEnumerator """
        pass

    def KeyAt(self, id):
        """ KeyAt(self: Dictionary, id: int) -> str """
        pass

    def Remove(self, *__args):
        """
        Remove(self: Dictionary, key: str) -> RXObject
        Remove(self: Dictionary, id: int) -> RXObject
        """
        pass

    def ResetKey(self, *__args):
        """ ResetKey(self: Dictionary, oldKey: str, newKey: str)ResetKey(self: Dictionary, id: int, newKey: str) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: IDictionary, key: object) -> bool """
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
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Dictionary) -> int

"""

    DeletesObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeletesObjects(self: Dictionary) -> bool

"""

    IsCaseSensitive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCaseSensitive(self: Dictionary) -> bool

"""

    IsFixedSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    IsSorted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSorted(self: Dictionary) -> bool

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DynamicLinker(RXObject):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetLoadedModules(self):
        """ GetLoadedModules(self: DynamicLinker) -> StringCollection """
        pass

    def IsAppBusy(self, moduleName):
        """ IsAppBusy(self: DynamicLinker, moduleName: str) -> bool """
        pass

    def IsApplicationLocked(self, moduleName):
        """ IsApplicationLocked(self: DynamicLinker, moduleName: str) -> bool """
        pass

    def IsAppMdiAware(self, moduleName):
        """ IsAppMdiAware(self: DynamicLinker, moduleName: str) -> bool """
        pass

    def IsModuleLoaded(self, fileName):
        """ IsModuleLoaded(self: DynamicLinker, fileName: str) -> bool """
        pass

    def LoadApp(self, appName, printIt, asCmd):
        """ LoadApp(self: DynamicLinker, appName: str, printIt: bool, asCmd: bool) """
        pass

    def LoadModule(self, fileName, printIt, asCmd):
        """ LoadModule(self: DynamicLinker, fileName: str, printIt: bool, asCmd: bool) """
        pass

    def SetAppBusy(self, moduleName, busyFlag):
        """ SetAppBusy(self: DynamicLinker, moduleName: str, busyFlag: bool) """
        pass

    def UnloadApp(self, appName, asCmd):
        """ UnloadApp(self: DynamicLinker, appName: str, asCmd: bool) """
        pass

    def UnloadModule(self, fileName, asCmd):
        """ UnloadModule(self: DynamicLinker, fileName: str, asCmd: bool) """
        pass

    ProductLcid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProductLcid(self: DynamicLinker) -> int

"""


    ModuleLoadAborted = None
    ModuleLoaded = None
    ModuleLoading = None
    ModuleUnloadAborted = None
    ModuleUnloaded = None
    ModuleUnloading = None


class DynamicLinkerEventArgs(EventArgs):
    """ DynamicLinkerEventArgs(fileName: str) """
    @staticmethod # known case of __new__
    def __new__(self, fileName):
        """ __new__(cls: type, fileName: str) """
        pass

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: DynamicLinkerEventArgs) -> str

"""



class ErrorStatus(Enum):
    """ enum ErrorStatus, values: AlreadyActive (20051), AlreadyInactive (20052), AlreadyInDB (26), AlreadyInGroup (260), AmbiguousInput (4), AmbiguousOutput (5), AnonymousEntry (38), AtMaxReaders (90), BackgroundPlotInProgress (527), BadColor (208), BadColorIndex (202), BadDwgHeader (314), BadDxfFile (368), BadDxfSequence (52), BadLayerName (200), BadLinetypeName (203), BadLinetypeScale (204), BadLineWeightValue (207), BadlyNestedAppData (378), BadPaperspaceView (169), BadPlotStyleName (384), BadPlotStyleNameHandle (387), BadPlotStyleType (386), BadUcs (168), BadVisibilityValue (205), BinaryDataSizeExceeded (391), BlockDefInEntitySection (381), BrokenHandle (12), BufferTooSmall (7), CannotBeErasedByCaller (105), CannotBeResurrected (106), CannotChangeActiveViewport (140), CannotChangeColumnType (441), CannotExplodeEntity (159), CannotNestBlockDefinitions (59), CannotPlotToFile (524), CannotRestoreFromAcisFile (300), CannotScaleNonUniformly (136), CantOpenFile (364), CloseFailObjectDamaged (104), CloseModifyAborted (102), ClosePartialFailure (103), CloseWasNotifying (101), CommandWasInProgress (142), ContainerNotEmpty (18), CopyDoesNotExist (354), CopyFailed (356), CopyInvalidName (357), CopyIsModelSpace (355), CopyNameExists (358), CreateFailed (337), CreateInvalidName (338), CustomSizeNotPossible (514), DatabaseObjectsOpen (322), DataLinkAdapterNotFound (650), DataLinkBadConnectionString (653), DataLinkConnectionFailed (656), DataLinkInvalidAdapterId (651), DataLinkNotFound (652), DataLinkNotUpdatedYet (654), DataLinkOtherError (660), DataLinkSourceIsWriteProtected (658), DataLinkSourceNotFound (655), DegenerateGeometry (153), DelDoesNotExist (342), DeletedEntry (28), DeleteEntity (191), DelIsModelSpace (343), DelLastLayout (344), DelUnableToFind (346), DelUnableToSetCurrent (345), DeviceNotFound (504), DocumentSwitchDisabled (334), DuplicateBlockDefinition (389), DuplicateBlockName (385), DuplicateDxfField (49), DuplicateIndex (25), DuplicateKey (23), DuplicateLayerName (383), DuplicateRecordName (95), DwgCrcDoesNotMatch (65), DwgNeedsAFullSave (69), DwgNeedsRecovery (190), DwgNotRecoverable (61), DwgObjectImproperlyRead (67), DwgRecoveredOK (60), DwgSentinelDoesNotMatch (66), DwgShareDemandLoad (500), DwgShareReadAccess (501), DwgShareWriteAccess (502), DwkLockFileFound (77), DxbPartiallyRead (64), DxbReadAborted (70), DxfPartiallyRead (62), DxfReadAborted (63), EmbeddedIntersections (552), EndOfFile (41), EndOfObject (40), EntityInInactiveLayout (9), ExcessiveItemCount (166), ExplodeBeforeTransform (135), ExternalDataSizeExceeded (125), FileAccessErr (72), FileExists (362), FileInternalErr (74), FileLockedByAutoCAD (71), FileMissingSections (436), FileNotFound (76), FilerError (53), FileSharingViolation (433), FileSystemErr (73), FileTooManyOpen (75), FiniteStateMachineError (193), FixedAllErrors (120), GeneralModelingFailure (150), GraphicsNotGenerated (523), GuidNoAddress (394), HadMultipleReaders (94), HandleExists (10), HandleInUse (14), HatchTooDense (420), IgnoredLinetypeRedefinition (167), IllegalEntityType (21), IllegalReplacement (39), IncompatiblePlotSettings (508), IncompleteBlockDefinition (379), IncompleteComplexObject (380), InProcessOfCommitting (253), InsertAfter (110), InternetBadPath (20003), InternetBase (20000), InternetCreateInternetSessionFailed (20019), InternetDirectoryFull (20007), InternetDiskFull (20010), InternetFileAccessDenied (20005), InternetFileGenericError (20011), InternetFileNotFound (20002), InternetFileOpenFailed (20023), InternetGenericException (20049), InternetHardwareError (20008), InternetHttpAccessDenied (20027), InternetHttpBadGateway (20044), InternetHttpBadMethod (20031), InternetHttpBadRequest (20026), InternetHttpConflict (20035), InternetHttpGatewayTimeout (20046), InternetHttpLengthRequired (20037), InternetHttpNoAcceptableResponse (20032), InternetHttpNotSupported (20043), InternetHttpObjectNotFound (20030), InternetHttpOpenRequestFailed (20024), InternetHttpPaymentRequired (20028), InternetHttpPreconditionFailure (20038), InternetHttpProxyAuthorizationRequired (20033), InternetHttpRequestForbidden (20029), InternetHttpRequestTooLarge (20039), InternetHttpResourceGone (20036), InternetHttpServerError (20042), InternetHttpServiceUnavailable (20045), InternetHttpTimedOut (20034), InternetHttpUnsupportedMedia (20041), InternetHttpUriTooLong (20040), InternetHttpVersionNotSupported (20047), InternetInCache (20001), InternetInternetError (20048), InternetInternetSessionConnectFailed (20020), InternetInternetSessionOpenFailed (20021), InternetInvalidAccessType (20022), InternetInvalidFileHandle (20006), InternetNoInternetSupport (20016), InternetNotAnUrl (20013), InternetNotImplemented (20017), InternetNoWinInternet (20014), InternetOK (20000), InternetOldWinInternet (20015), InternetProtocolNotSupported (20018), InternetSharingViolation (20009), InternetTooManyOpenFiles (20004), InternetUnknownError (20050), InternetUserCancelledTransfer (20025), InternetValidUrl (20012), InvalidAdsName (31), InvalidAxis (154), InvalidBlockName (47), InvalidContext (335), InvalidDimStyle (172), InvalidDwgVersion (37), InvalidDxf2dPoint (375), InvalidDxf3dPoint (376), InvalidDxfCode (50), InvalidDxfSectionName (371), InvalidEngineState (517), InvalidExtents (30), InvalidFaceVertexIndex (55), InvalidFileExtension (360), InvalidFix (192), InvalidIdMap (220), InvalidIndex (24), InvalidInput (3), InvalidInterfaceId (290), InvalidKey (33), InvalidLayer (173), InvalidMeshVertexIndex (56), InvalidNormal (291), InvalidObjectId (600), InvalidOffset (157), InvalidOpenState (8), InvalidOwnerObject (221), InvalidPlotArea (513), InvalidPlotInfo (520), InvalidProfileName (361), InvalidResultBuffer (51), InvalidStyle (292), InvalidSymbolTableName (32), InvalidSymTableFlag (161), InvalidTextStyle (163), InvalidView (511), InvalidWindowArea (512), InvalidXrefObjectId (601), IsAnEntity (139), IsReading (42), IsWriteProtected (91), IsWriting (43), IsXRefObject (92), IteratorDone (129), KeyNotFound (22), LayerGroupCodeMissing (201), LayoutNotCurrent (522), LeftErrorsUnfixed (122), LispActive (332), LoadFailed (503), LockChangeInProgress (323), LockConflict (321), LockViolation (320), LongTransReferenceError (255), MakeMeProxy (301), MakeMeProxyAndResurrect (432), MaxLayouts (408), MissingBlockName (390), MissingDxfField (48), MissingDxfSection (370), MissingSymbolTable (98), MissingSymbolTableRecord (99), MustBe0to2 (395), MustBe0to3 (396), MustBe0to4 (397), MustBe0to5 (398), MustBe0to8 (399), MustBe1to15 (401), MustBe1to6 (405), MustBe1to8 (400), MustBeNonNegative (403), MustBeNonZero (404), MustBePositive (402), MustFirstAddBlockToDB (58), MustOpenThruOwner (88), MustPlotToFile (525), NegativeValueNotAllowed (29), NlsFileNotAvailable (302), NoActiveTransactions (250), NoBlockBegin (382), NoClassId (409), NoCurrentConfig (505), NoDatabase (124), NoDocument (330), NoErrorHandler (519), NoFileName (365), NoInputFiler (68), NoInternalSpace (171), NoIntersections (551), NoLabelBlock (603), NoLayout (507), NoMatchingMedia (510), NonCoplanarGeometry (152), NonePlotDevice (509), NonPlanarEntity (158), NoPlotStyleTranslationTable (406), NotAllowedForThisProxy (303), NotAnEntity (93), NotApplicable (2), NotCurrentDatabase (138), NotDxfHeaderGroupCode (372), NotFromThisDocument (331), NotHandled (431), NoThumbnailBitmap (393), NotImplementedYet (1), NotInBlock (131), NotInDatabase (137), NotInGroup (261), NotInitializedYet (374), NotInPaperspace (141), NotMultiPageCapable (526), NotNewlyCreated (254), NotOpenForRead (44), NotOpenForWrite (45), NotSupportedInDwgApi (310), NotThatKindOfClass (46), NotTopTransaction (251), NoViewAssociation (602), NoWorkSet (256), NullBlockName (17), NullEntityPointer (20), NullExtents (312), NullHandle (11), NullIterator (130), NullObjectId (16), NullObjectPointer (15), NullPtr (506), NumberOfCopiesNotSupported (521), ObjectIsReferenced (392), ObjectToBeDeleted (36), ObsoleteFileFormat (435), OK (0), OnLockedLayer (87), OpenFileCancelled (430), OtherObjectsBusy (57), OutOfDisk (27), OutOfMemory (6), OutOfPagerMemory (211), OutOfRange (151), OwnerNotInDatabase (132), OwnerNotOpenForRead (133), OwnerNotOpenForWrite (134), OwnerNotSet (222), PageCancelled (515), PagerError (210), PagerWriteError (212), PermanentlyErased (81), PlotAlreadyStarted (518), PlotCancelled (516), PlotStyleInColorDependentMode (407), PointNotOnEntity (155), PolyWidthLost (311), ProfileDoesNotExist (359), ProfileIsInUse (363), ProperClassSeparatorExpected (206), RecordNotInTable (128), RegisteredApplicationIdNotFound (126), RegistryAccessError (366), RegistryCreateError (367), RenameDoesNotExist (348), RenameInvalidLayoutName (350), RenameInvalidName (352), RenameIsModelSpace (349), RenameLayoutAlreadyExists (351), RepeatedDwgRead (437), RepeatEntity (127), RowsMustMatchColumns (442), SecErrorCipherNotSupported (1202), SecErrorComputingSignature (1103), SecErrorDecryptingData (1203), SecErrorEncryptingData (1201), SecErrorGeneratingTimestamp (1102), SecErrorReadingFile (1002), SecErrorWritingFile (1003), SecErrorWritingSignature (1104), SecInitializationFailure (1001), SecInvalidDigitalId (1101), SelfReference (97), SetFailed (340), SingularPoint (156), SomeInputDataLeftUnread (170), StringTooLong (160), SubentitiesStillOpen (89), SubSelectionSetEmpty (550), TargetDocNotQuiescent (333), TooFewLineTypeElements (164), TooFewVertices (232), TooManyLineTypeElements (165), TooManyVertices (231), TransactionOpenWhileCommandEnded (252), UnableToGetLabelBlock (607), UnableToGetViewAssociation (605), UnableToRemoveAssociation (608), UnableToSetLabelBlock (606), UnableToSetViewAssociation (604), UnableToSyncModelView (609), UndefinedDxfGroupCode (373), UndefinedLineType (162), UndefineShapeName (388), UndoNoGroupBegin (411), UndoOperationNotAvailable (410), UnknownDxfFileFormat (369), UnknownHandle (13), UnrecoverableErrors (123), UnsupportedFileFormat (434), UserBreak (180), VertexAfterFace (54), Vetoed (325), WasErased (80), WasNotErased (107), WasNotForwarding (213), WasNotifying (85), WasNotOpenForWrite (100), WasOpenForNotify (86), WasOpenForRead (82), WasOpenForUndo (84), WasOpenForWrite (83), WrongCellType (440), WrongDatabase (35), WrongObjectType (34), WrongSubentityType (230), XRefDependent (96) """
    AlreadyActive = None
    AlreadyInactive = None
    AlreadyInDB = None
    AlreadyInGroup = None
    AmbiguousInput = None
    AmbiguousOutput = None
    AnonymousEntry = None
    AtMaxReaders = None
    BackgroundPlotInProgress = None
    BadColor = None
    BadColorIndex = None
    BadDwgHeader = None
    BadDxfFile = None
    BadDxfSequence = None
    BadLayerName = None
    BadLinetypeName = None
    BadLinetypeScale = None
    BadLineWeightValue = None
    BadlyNestedAppData = None
    BadPaperspaceView = None
    BadPlotStyleName = None
    BadPlotStyleNameHandle = None
    BadPlotStyleType = None
    BadUcs = None
    BadVisibilityValue = None
    BinaryDataSizeExceeded = None
    BlockDefInEntitySection = None
    BrokenHandle = None
    BufferTooSmall = None
    CannotBeErasedByCaller = None
    CannotBeResurrected = None
    CannotChangeActiveViewport = None
    CannotChangeColumnType = None
    CannotExplodeEntity = None
    CannotNestBlockDefinitions = None
    CannotPlotToFile = None
    CannotRestoreFromAcisFile = None
    CannotScaleNonUniformly = None
    CantOpenFile = None
    CloseFailObjectDamaged = None
    CloseModifyAborted = None
    ClosePartialFailure = None
    CloseWasNotifying = None
    CommandWasInProgress = None
    ContainerNotEmpty = None
    CopyDoesNotExist = None
    CopyFailed = None
    CopyInvalidName = None
    CopyIsModelSpace = None
    CopyNameExists = None
    CreateFailed = None
    CreateInvalidName = None
    CustomSizeNotPossible = None
    DatabaseObjectsOpen = None
    DataLinkAdapterNotFound = None
    DataLinkBadConnectionString = None
    DataLinkConnectionFailed = None
    DataLinkInvalidAdapterId = None
    DataLinkNotFound = None
    DataLinkNotUpdatedYet = None
    DataLinkOtherError = None
    DataLinkSourceIsWriteProtected = None
    DataLinkSourceNotFound = None
    DegenerateGeometry = None
    DelDoesNotExist = None
    DeletedEntry = None
    DeleteEntity = None
    DelIsModelSpace = None
    DelLastLayout = None
    DelUnableToFind = None
    DelUnableToSetCurrent = None
    DeviceNotFound = None
    DocumentSwitchDisabled = None
    DuplicateBlockDefinition = None
    DuplicateBlockName = None
    DuplicateDxfField = None
    DuplicateIndex = None
    DuplicateKey = None
    DuplicateLayerName = None
    DuplicateRecordName = None
    DwgCrcDoesNotMatch = None
    DwgNeedsAFullSave = None
    DwgNeedsRecovery = None
    DwgNotRecoverable = None
    DwgObjectImproperlyRead = None
    DwgRecoveredOK = None
    DwgSentinelDoesNotMatch = None
    DwgShareDemandLoad = None
    DwgShareReadAccess = None
    DwgShareWriteAccess = None
    DwkLockFileFound = None
    DxbPartiallyRead = None
    DxbReadAborted = None
    DxfPartiallyRead = None
    DxfReadAborted = None
    EmbeddedIntersections = None
    EndOfFile = None
    EndOfObject = None
    EntityInInactiveLayout = None
    ExcessiveItemCount = None
    ExplodeBeforeTransform = None
    ExternalDataSizeExceeded = None
    FileAccessErr = None
    FileExists = None
    FileInternalErr = None
    FileLockedByAutoCAD = None
    FileMissingSections = None
    FileNotFound = None
    FilerError = None
    FileSharingViolation = None
    FileSystemErr = None
    FileTooManyOpen = None
    FiniteStateMachineError = None
    FixedAllErrors = None
    GeneralModelingFailure = None
    GraphicsNotGenerated = None
    GuidNoAddress = None
    HadMultipleReaders = None
    HandleExists = None
    HandleInUse = None
    HatchTooDense = None
    IgnoredLinetypeRedefinition = None
    IllegalEntityType = None
    IllegalReplacement = None
    IncompatiblePlotSettings = None
    IncompleteBlockDefinition = None
    IncompleteComplexObject = None
    InProcessOfCommitting = None
    InsertAfter = None
    InternetBadPath = None
    InternetBase = None
    InternetCreateInternetSessionFailed = None
    InternetDirectoryFull = None
    InternetDiskFull = None
    InternetFileAccessDenied = None
    InternetFileGenericError = None
    InternetFileNotFound = None
    InternetFileOpenFailed = None
    InternetGenericException = None
    InternetHardwareError = None
    InternetHttpAccessDenied = None
    InternetHttpBadGateway = None
    InternetHttpBadMethod = None
    InternetHttpBadRequest = None
    InternetHttpConflict = None
    InternetHttpGatewayTimeout = None
    InternetHttpLengthRequired = None
    InternetHttpNoAcceptableResponse = None
    InternetHttpNotSupported = None
    InternetHttpObjectNotFound = None
    InternetHttpOpenRequestFailed = None
    InternetHttpPaymentRequired = None
    InternetHttpPreconditionFailure = None
    InternetHttpProxyAuthorizationRequired = None
    InternetHttpRequestForbidden = None
    InternetHttpRequestTooLarge = None
    InternetHttpResourceGone = None
    InternetHttpServerError = None
    InternetHttpServiceUnavailable = None
    InternetHttpTimedOut = None
    InternetHttpUnsupportedMedia = None
    InternetHttpUriTooLong = None
    InternetHttpVersionNotSupported = None
    InternetInCache = None
    InternetInternetError = None
    InternetInternetSessionConnectFailed = None
    InternetInternetSessionOpenFailed = None
    InternetInvalidAccessType = None
    InternetInvalidFileHandle = None
    InternetNoInternetSupport = None
    InternetNotAnUrl = None
    InternetNotImplemented = None
    InternetNoWinInternet = None
    InternetOK = None
    InternetOldWinInternet = None
    InternetProtocolNotSupported = None
    InternetSharingViolation = None
    InternetTooManyOpenFiles = None
    InternetUnknownError = None
    InternetUserCancelledTransfer = None
    InternetValidUrl = None
    InvalidAdsName = None
    InvalidAxis = None
    InvalidBlockName = None
    InvalidContext = None
    InvalidDimStyle = None
    InvalidDwgVersion = None
    InvalidDxf2dPoint = None
    InvalidDxf3dPoint = None
    InvalidDxfCode = None
    InvalidDxfSectionName = None
    InvalidEngineState = None
    InvalidExtents = None
    InvalidFaceVertexIndex = None
    InvalidFileExtension = None
    InvalidFix = None
    InvalidIdMap = None
    InvalidIndex = None
    InvalidInput = None
    InvalidInterfaceId = None
    InvalidKey = None
    InvalidLayer = None
    InvalidMeshVertexIndex = None
    InvalidNormal = None
    InvalidObjectId = None
    InvalidOffset = None
    InvalidOpenState = None
    InvalidOwnerObject = None
    InvalidPlotArea = None
    InvalidPlotInfo = None
    InvalidProfileName = None
    InvalidResultBuffer = None
    InvalidStyle = None
    InvalidSymbolTableName = None
    InvalidSymTableFlag = None
    InvalidTextStyle = None
    InvalidView = None
    InvalidWindowArea = None
    InvalidXrefObjectId = None
    IsAnEntity = None
    IsReading = None
    IsWriteProtected = None
    IsWriting = None
    IsXRefObject = None
    IteratorDone = None
    KeyNotFound = None
    LayerGroupCodeMissing = None
    LayoutNotCurrent = None
    LeftErrorsUnfixed = None
    LispActive = None
    LoadFailed = None
    LockChangeInProgress = None
    LockConflict = None
    LockViolation = None
    LongTransReferenceError = None
    MakeMeProxy = None
    MakeMeProxyAndResurrect = None
    MaxLayouts = None
    MissingBlockName = None
    MissingDxfField = None
    MissingDxfSection = None
    MissingSymbolTable = None
    MissingSymbolTableRecord = None
    MustBe0to2 = None
    MustBe0to3 = None
    MustBe0to4 = None
    MustBe0to5 = None
    MustBe0to8 = None
    MustBe1to15 = None
    MustBe1to6 = None
    MustBe1to8 = None
    MustBeNonNegative = None
    MustBeNonZero = None
    MustBePositive = None
    MustFirstAddBlockToDB = None
    MustOpenThruOwner = None
    MustPlotToFile = None
    NegativeValueNotAllowed = None
    NlsFileNotAvailable = None
    NoActiveTransactions = None
    NoBlockBegin = None
    NoClassId = None
    NoCurrentConfig = None
    NoDatabase = None
    NoDocument = None
    NoErrorHandler = None
    NoFileName = None
    NoInputFiler = None
    NoInternalSpace = None
    NoIntersections = None
    NoLabelBlock = None
    NoLayout = None
    NoMatchingMedia = None
    NonCoplanarGeometry = None
    NonePlotDevice = None
    NonPlanarEntity = None
    NoPlotStyleTranslationTable = None
    NotAllowedForThisProxy = None
    NotAnEntity = None
    NotApplicable = None
    NotCurrentDatabase = None
    NotDxfHeaderGroupCode = None
    NotFromThisDocument = None
    NotHandled = None
    NoThumbnailBitmap = None
    NotImplementedYet = None
    NotInBlock = None
    NotInDatabase = None
    NotInGroup = None
    NotInitializedYet = None
    NotInPaperspace = None
    NotMultiPageCapable = None
    NotNewlyCreated = None
    NotOpenForRead = None
    NotOpenForWrite = None
    NotSupportedInDwgApi = None
    NotThatKindOfClass = None
    NotTopTransaction = None
    NoViewAssociation = None
    NoWorkSet = None
    NullBlockName = None
    NullEntityPointer = None
    NullExtents = None
    NullHandle = None
    NullIterator = None
    NullObjectId = None
    NullObjectPointer = None
    NullPtr = None
    NumberOfCopiesNotSupported = None
    ObjectIsReferenced = None
    ObjectToBeDeleted = None
    ObsoleteFileFormat = None
    OK = None
    OnLockedLayer = None
    OpenFileCancelled = None
    OtherObjectsBusy = None
    OutOfDisk = None
    OutOfMemory = None
    OutOfPagerMemory = None
    OutOfRange = None
    OwnerNotInDatabase = None
    OwnerNotOpenForRead = None
    OwnerNotOpenForWrite = None
    OwnerNotSet = None
    PageCancelled = None
    PagerError = None
    PagerWriteError = None
    PermanentlyErased = None
    PlotAlreadyStarted = None
    PlotCancelled = None
    PlotStyleInColorDependentMode = None
    PointNotOnEntity = None
    PolyWidthLost = None
    ProfileDoesNotExist = None
    ProfileIsInUse = None
    ProperClassSeparatorExpected = None
    RecordNotInTable = None
    RegisteredApplicationIdNotFound = None
    RegistryAccessError = None
    RegistryCreateError = None
    RenameDoesNotExist = None
    RenameInvalidLayoutName = None
    RenameInvalidName = None
    RenameIsModelSpace = None
    RenameLayoutAlreadyExists = None
    RepeatedDwgRead = None
    RepeatEntity = None
    RowsMustMatchColumns = None
    SecErrorCipherNotSupported = None
    SecErrorComputingSignature = None
    SecErrorDecryptingData = None
    SecErrorEncryptingData = None
    SecErrorGeneratingTimestamp = None
    SecErrorReadingFile = None
    SecErrorWritingFile = None
    SecErrorWritingSignature = None
    SecInitializationFailure = None
    SecInvalidDigitalId = None
    SelfReference = None
    SetFailed = None
    SingularPoint = None
    SomeInputDataLeftUnread = None
    StringTooLong = None
    SubentitiesStillOpen = None
    SubSelectionSetEmpty = None
    TargetDocNotQuiescent = None
    TooFewLineTypeElements = None
    TooFewVertices = None
    TooManyLineTypeElements = None
    TooManyVertices = None
    TransactionOpenWhileCommandEnded = None
    UnableToGetLabelBlock = None
    UnableToGetViewAssociation = None
    UnableToRemoveAssociation = None
    UnableToSetLabelBlock = None
    UnableToSetViewAssociation = None
    UnableToSyncModelView = None
    UndefinedDxfGroupCode = None
    UndefinedLineType = None
    UndefineShapeName = None
    UndoNoGroupBegin = None
    UndoOperationNotAvailable = None
    UnknownDxfFileFormat = None
    UnknownHandle = None
    UnrecoverableErrors = None
    UnsupportedFileFormat = None
    UserBreak = None
    value__ = None
    VertexAfterFace = None
    Vetoed = None
    WasErased = None
    WasNotErased = None
    WasNotForwarding = None
    WasNotifying = None
    WasNotOpenForWrite = None
    WasOpenForNotify = None
    WasOpenForRead = None
    WasOpenForUndo = None
    WasOpenForWrite = None
    WrongCellType = None
    WrongDatabase = None
    WrongObjectType = None
    WrongSubentityType = None
    XRefDependent = None


class Exception(Exception):
    """
    Exception(es: ErrorStatus, message: str, innerException: Exception)
    Exception(es: ErrorStatus, message: str)
    Exception(es: ErrorStatus)
    Exception()
    """
    def GetObjectData(self, info, context):
        """ GetObjectData(self: Exception, info: SerializationInfo, context: StreamingContext) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, es=None, message=None, innerException=None):
        """
        __new__(cls: type, es: ErrorStatus, message: str, innerException: Exception)
        __new__(cls: type, es: ErrorStatus, message: str)
        __new__(cls: type, es: ErrorStatus)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    ErrorStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ErrorStatus(self: Exception) -> ErrorStatus

Set: ErrorStatus(self: Exception) = value
"""



class ExceptionFilter(object):
    # no doc
    def Catcher(self, *args): #cannot find CLR method
        """ Catcher(self: ExceptionFilter, ex: Exception) """
        pass

    def Filter(self, *args): #cannot find CLR method
        """ Filter(self: ExceptionFilter, ex: Exception) -> bool """
        pass

    def Invoke(self):
        """ Invoke(self: ExceptionFilter) """
        pass

    def InvokeWorker(self, *args): #cannot find CLR method
        """ InvokeWorker(self: ExceptionFilter) """
        pass


class ExtensionApplicationAttribute(Attribute):
    """ ExtensionApplicationAttribute(entryPointType: Type) """
    @staticmethod # known case of __new__
    def __new__(self, entryPointType):
        """ __new__(cls: type, entryPointType: Type) """
        pass

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: ExtensionApplicationAttribute) -> Type

"""



class ExtensionLoader(MarshalByRefObject):
    # no doc
    @staticmethod
    def IsLoaded(fileName):
        """ IsLoaded(fileName: str) -> bool """
        pass

    @staticmethod
    def Load(fileName):
        """ Load(fileName: str) -> Assembly """
        pass


class ExtractionType(Enum):
    """ enum ExtractionType, values: AllLine (1), OutLine (0) """
    AllLine = None
    OutLine = None
    value__ = None


class ExtractOption(object):
    """ ExtractOption() """
    ExtractType = None
    FillGap = None
    MiniumSegmentLength = None
    ProcessPoints = None
    SnapAngle = None
    UseLineSegmentOnly = None


class IExtensionApplication:
    # no doc
    def Initialize(self):
        """ Initialize(self: IExtensionApplication) """
        pass

    def Terminate(self):
        """ Terminate(self: IExtensionApplication) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class IMenuItem:
    # no doc
    def OnClicked(self, eventArgs):
        """ OnClicked(self: IMenuItem, eventArgs: EventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Checked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Checked(self: IMenuItem) -> bool

Set: Checked(self: IMenuItem) = value
"""

    Enabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Enabled(self: IMenuItem) -> bool

Set: Enabled(self: IMenuItem) = value
"""

    Icon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon(self: IMenuItem) -> Icon

Set: Icon(self: IMenuItem) = value
"""

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: IMenuItem) -> IEnumerable[IMenuItem]

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: IMenuItem) -> str

Set: Text(self: IMenuItem) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: IMenuItem) -> bool

Set: Visible(self: IMenuItem) = value
"""


    Click = None


class Interop(object):
    # no doc
    @staticmethod
    def AttachUnmanagedObject(obj, unmanagedPointer, autoDelete):
        """ AttachUnmanagedObject(obj: DisposableWrapper, unmanagedPointer: IntPtr, autoDelete: bool) """
        pass

    @staticmethod
    def Check(returnValue):
        """ Check(returnValue: int) """
        pass

    @staticmethod
    def CheckAds(returnValue):
        """ CheckAds(returnValue: int) """
        pass

    @staticmethod
    def CheckAdsForCancel(returnValue):
        """ CheckAdsForCancel(returnValue: int) -> bool """
        pass

    @staticmethod
    def CheckBool(returnValue):
        """ CheckBool(returnValue: bool) """
        pass

    @staticmethod
    def CheckBoolean(returnValue):
        """ CheckBoolean(returnValue: int) """
        pass

    @staticmethod
    def CheckNull(returnValue):
        """ CheckNull(returnValue: IntPtr) """
        pass

    @staticmethod
    def DetachUnmanagedObject(obj):
        """ DetachUnmanagedObject(obj: DisposableWrapper) """
        pass

    @staticmethod
    def SetAutoDelete(obj, value):
        """ SetAutoDelete(obj: DisposableWrapper, value: bool) """
        pass

    @staticmethod
    def ThrowExceptionForErrorStatus(errorStatus):
        """ ThrowExceptionForErrorStatus(errorStatus: int) """
        pass


class IPointCloudExtractionProgressCallback:
    # no doc
    def Cancel(self):
        """ Cancel(self: IPointCloudExtractionProgressCallback) """
        pass

    def Cancelled(self):
        """ Cancelled(self: IPointCloudExtractionProgressCallback) -> bool """
        pass

    def End(self):
        """ End(self: IPointCloudExtractionProgressCallback) """
        pass

    def UpdateCaption(self, caption):
        """ UpdateCaption(self: IPointCloudExtractionProgressCallback, caption: str) """
        pass

    def UpdateProgress(self, progress):
        """ UpdateProgress(self: IPointCloudExtractionProgressCallback, progress: int) """
        pass

    def UpdateRemainTime(self, remainTime):
        """ UpdateRemainTime(self: IPointCloudExtractionProgressCallback, remainTime: float) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


class LenientResourceManager(ResourceManager):
    """ LenientResourceManager(t: Type) """
    @staticmethod # known case of __new__
    def __new__(self, t):
        """ __new__(cls: type, t: Type) """
        pass

    FallbackLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BaseNameField = None
    MainAssembly = None
    ResourceSets = None


class LispDataType(Enum):
    """ enum LispDataType, values: Angle (5004), DottedPair (5018), Double (5001), Int16 (5003), Int32 (5010), ListBegin (5016), ListEnd (5017), Nil (5019), None (5000), ObjectId (5006), Orientation (5008), Point2d (5002), Point3d (5009), SelectionSet (5007), T_atom (5021), Text (5005), Void (5014) """
    Angle = None
    DottedPair = None
    Double = None
    Int16 = None
    Int32 = None
    ListBegin = None
    ListEnd = None
    Nil = None
    None = None
    ObjectId = None
    Orientation = None
    Point2d = None
    Point3d = None
    SelectionSet = None
    Text = None
    T_atom = None
    value__ = None
    Void = None


class ManagedHost(object):
    """ ManagedHost() """
    def Entry(self):
        """ Entry(self: ManagedHost) """
        pass


class Marshaler(object):
    # no doc
    @staticmethod
    def AcValueToObject(acValueObj):
        """ AcValueToObject(acValueObj: IntPtr) -> object """
        pass

    @staticmethod
    def BitmapInfoToBitmap(bitmapInfo):
        """ BitmapInfoToBitmap(bitmapInfo: IntPtr) -> Bitmap """
        pass

    @staticmethod
    def BitmapToBitmapInfo(bitmap):
        """ BitmapToBitmapInfo(bitmap: Bitmap) -> IntPtr """
        pass

    @staticmethod
    def CopyToManagedFullSubentityPath(path):
        """ CopyToManagedFullSubentityPath(path: IntPtr) -> FullSubentityPath """
        pass

    @staticmethod
    def CopyToUnmanagedFullSubentityPath(path, newPath):
        """ CopyToUnmanagedFullSubentityPath(path: FullSubentityPath, newPath: IntPtr) """
        pass

    @staticmethod
    def GetInternalArray(col):
        """
        GetInternalArray(col: IntegerCollection) -> Array[int]
        GetInternalArray(col: DoubleCollection) -> Array[float]
        GetInternalArray(col: Point2dCollection) -> Array[Point2d]
        GetInternalArray(col: Vector3dCollection) -> Array[Vector3d]
        GetInternalArray(col: Vector2dCollection) -> Array[Vector2d]
        """
        pass

    @staticmethod
    def ObjectsToResbuf(objects):
        """ ObjectsToResbuf(*objects: Array[object]) -> IntPtr """
        pass

    @staticmethod
    def ObjectToAcValue(obj, acValueObj):
        """ ObjectToAcValue(obj: object, acValueObj: IntPtr) """
        pass

    @staticmethod
    def ObjectToResbuf(o, rb=None):
        """ ObjectToResbuf(o: object, rb: IntPtr)ObjectToResbuf(o: object) -> IntPtr """
        pass

    @staticmethod
    def ResbufToObject(rb):
        """ ResbufToObject(rb: IntPtr) -> object """
        pass

    @staticmethod
    def ResbufToTypedValues(resbuf):
        """ ResbufToTypedValues(resbuf: IntPtr) -> Array[TypedValue] """
        pass

    @staticmethod
    def SetInternalArray(col, newArray, count):
        """ SetInternalArray(col: IntegerCollection, newArray: Array[int], count: int)SetInternalArray(col: DoubleCollection, newArray: Array[float], count: int)SetInternalArray(col: Point2dCollection, newArray: Array[Point2d], count: int)SetInternalArray(col: Vector3dCollection, newArray: Array[Vector3d], count: int)SetInternalArray(col: Vector2dCollection, newArray: Array[Vector2d], count: int) """
        pass

    @staticmethod
    def TypedValuesToResbuf(values):
        """ TypedValuesToResbuf(*values: Array[TypedValue]) -> IntPtr """
        pass


class ModuleLoadAbortedEventHandler(MulticastDelegate):
    """ ModuleLoadAbortedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ModuleLoadAbortedEventHandler, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleLoadAbortedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleLoadAbortedEventHandler, sender: object, e: DynamicLinkerEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ModuleLoadedEventHandler(MulticastDelegate):
    """ ModuleLoadedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ModuleLoadedEventHandler, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleLoadedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleLoadedEventHandler, sender: object, e: DynamicLinkerEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ModuleLoadingEventHandler(MulticastDelegate):
    """ ModuleLoadingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ModuleLoadingEventHandler, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleLoadingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleLoadingEventHandler, sender: object, e: DynamicLinkerEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ModuleUnloadAbortedEventHandler(MulticastDelegate):
    """ ModuleUnloadAbortedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ModuleUnloadAbortedEventHandler, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleUnloadAbortedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleUnloadAbortedEventHandler, sender: object, e: DynamicLinkerEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ModuleUnloadedEventHandler(MulticastDelegate):
    """ ModuleUnloadedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ModuleUnloadedEventHandler, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleUnloadedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleUnloadedEventHandler, sender: object, e: DynamicLinkerEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class ModuleUnloadingEventHandler(MulticastDelegate):
    """ ModuleUnloadingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: ModuleUnloadingEventHandler, sender: object, e: DynamicLinkerEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: ModuleUnloadingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: ModuleUnloadingEventHandler, sender: object, e: DynamicLinkerEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class Overrule(RXObject):
    # no doc
    @staticmethod
    def AddOverrule(targetClass, overrule, bAtLast):
        """ AddOverrule(targetClass: RXClass, overrule: Overrule, bAtLast: bool) """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def HasOverrule(overruledSubject, targetClass):
        """ HasOverrule(overruledSubject: RXObject, targetClass: RXClass) -> bool """
        pass

    def IsApplicable(self, overruledSubject):
        """ IsApplicable(self: Overrule, overruledSubject: RXObject) -> bool """
        pass

    @staticmethod
    def RemoveOverrule(targetClass, overrule):
        """ RemoveOverrule(targetClass: RXClass, overrule: Overrule) """
        pass

    def SetCustomFilter(self):
        """ SetCustomFilter(self: Overrule) """
        pass

    def SetExtensionDictionaryEntryFilter(self, entryName):
        """ SetExtensionDictionaryEntryFilter(self: Overrule, entryName: str) """
        pass

    def SetIdFilter(self, ids):
        """ SetIdFilter(self: Overrule, ids: Array[ObjectId]) """
        pass

    def SetNoFilter(self):
        """ SetNoFilter(self: Overrule) """
        pass

    def SetXDataFilter(self, registeredApplicationName):
        """ SetXDataFilter(self: Overrule, registeredApplicationName: str) """
        pass

    Overruling = True


class PointCloudExtractor(DisposableWrapper):
    """ PointCloudExtractor() """
    @staticmethod
    def AppendLineProfile(profile, spaceId, layer, color):
        """ AppendLineProfile(profile: PointCloudExtractResult, spaceId: ObjectId, layer: str, color: Color) -> ObjectIdCollection """
        pass

    @staticmethod
    def AppendPolylineProfile(profile, spaceId, layer, color, polylineWidth):
        """ AppendPolylineProfile(profile: PointCloudExtractResult, spaceId: ObjectId, layer: str, color: Color, polylineWidth: float) -> ObjectIdCollection """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod
    def Extract(pointCloud, planZDirection, planXDirection, pointOnPlan, extractOption, progress):
        """ Extract(pointCloud: PointCloudEx, planZDirection: Vector3d, planXDirection: Vector3d, pointOnPlan: Point3d, extractOption: ExtractOption, progress: IPointCloudExtractionProgressCallback) -> PointCloudExtractResult """
        pass


class PointCloudExtractResult(object):
    """ PointCloudExtractResult() """
    Curves = None
    transform = None


class ProfileCurve2d(DisposableWrapper):
    """
    ProfileCurve2d(arc: CircularArc2d)
    ProfileCurve2d(seg: LineSegment2d)
    ProfileCurve2d()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, arc: CircularArc2d)
        __new__(cls: type, seg: LineSegment2d)
        __new__(cls: type)
        __new__(cls: type, unmanagedObjPtr: IntPtr, autoDelete: bool)
        """
        pass

    Arc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Arc(self: ProfileCurve2d) -> CircularArc2d

Set: Arc(self: ProfileCurve2d) = value
"""

    IsArc = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsArc(self: ProfileCurve2d) -> bool

"""

    IsSegment = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSegment(self: ProfileCurve2d) -> bool

"""

    LineSeg = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LineSeg(self: ProfileCurve2d) -> LineSegment2d

Set: LineSeg(self: ProfileCurve2d) = value
"""



class ProfileCurveType(Enum):
    """ enum ProfileCurveType, values: Arc (1), LineSeg (0) """
    Arc = None
    LineSeg = None
    value__ = None


class ProgressMeter(DisposableWrapper):
    """ ProgressMeter() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def MeterProgress(self):
        """ MeterProgress(self: ProgressMeter) """
        pass

    def SetLimit(self, max):
        """ SetLimit(self: ProgressMeter, max: int) """
        pass

    def Start(self, displayString=None):
        """ Start(self: ProgressMeter, displayString: str)Start(self: ProgressMeter) """
        pass

    def Stop(self):
        """ Stop(self: ProgressMeter) """
        pass


class Registry(object):
    # no doc
    ClassesRoot = None
    CurrentConfig = None
    CurrentUser = None
    LocalMachine = None


class RegistryKey(object):
    """ RegistryKey(hKey: RegistryKey) """
    def Close(self):
        """ Close(self: RegistryKey) """
        pass

    def CreateSubKey(self, subkey, permissionCheck=None, *__args):
        """
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, options: RegistryOptions) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registryOptions: RegistryOptions, registrySecurity: RegistrySecurity) -> RegistryKey
        CreateSubKey(self: RegistryKey, subkey: str, permissionCheck: RegistryKeyPermissionCheck, registrySecurity: RegistrySecurity) -> RegistryKey
        """
        pass

    def DeleteSubKey(self, subkey):
        """ DeleteSubKey(self: RegistryKey, subkey: str) """
        pass

    def DeleteSubKeyTree(self, subkey):
        """ DeleteSubKeyTree(self: RegistryKey, subkey: str) """
        pass

    def DeleteValue(self, name):
        """ DeleteValue(self: RegistryKey, name: str) """
        pass

    def Dispose(self):
        """ Dispose(self: RegistryKey) """
        pass

    @staticmethod
    def GetBaseKey(hKey):
        """ GetBaseKey(hKey: RegistryHive) -> RegistryKey """
        pass

    def GetSubKeyNames(self):
        """ GetSubKeyNames(self: RegistryKey) -> Array[str] """
        pass

    def GetValue(self, name, defaultValue=None, options=None):
        """
        GetValue(self: RegistryKey, name: str) -> object
        GetValue(self: RegistryKey, name: str, defaultValue: object) -> object
        GetValue(self: RegistryKey, name: str, defaultValue: object, options: RegistryValueOptions) -> object
        """
        pass

    def GetValueKind(self, name):
        """ GetValueKind(self: RegistryKey, name: str) -> RegistryValueKind """
        pass

    def GetValueNames(self):
        """ GetValueNames(self: RegistryKey) -> Array[str] """
        pass

    @staticmethod
    def OpenBaseKey(hKey, view):
        """ OpenBaseKey(hKey: RegistryHive, view: RegistryView) -> RegistryKey """
        pass

    def OpenSubKey(self, name, *__args):
        """
        OpenSubKey(self: RegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str, permissionCheck: RegistryKeyPermissionCheck, rights: RegistryRights) -> RegistryKey
        OpenSubKey(self: RegistryKey, name: str, writable: bool) -> RegistryKey
        """
        pass

    def SetValue(self, name, value, kind=None):
        """ SetValue(self: RegistryKey, name: str, value: object)SetValue(self: RegistryKey, name: str, value: object, kind: RegistryValueKind) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, hKey):
        """ __new__(cls: type, hKey: RegistryKey) """
        pass

    SubKeyCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubKeyCount(self: RegistryKey) -> int

"""

    ValueCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueCount(self: RegistryKey) -> int

"""



class RuntimeSystem(object):
    # no doc
    @staticmethod
    def Initialize(hostServices, localId):
        """ Initialize(hostServices: HostApplicationServices, localId: int) """
        pass

    @staticmethod
    def Main(pwzArgument):
        """ Main(pwzArgument: str) -> int """
        pass

    @staticmethod
    def Terminate():
        """ Terminate() """
        pass


class SecuredApplicationAttribute(Attribute):
    """ SecuredApplicationAttribute(license: str, ourSignature: str, clientSignature: str, clientPublicKey: str) """
    @staticmethod # known case of __new__
    def __new__(self, license, ourSignature, clientSignature, clientPublicKey):
        """ __new__(cls: type, license: str, ourSignature: str, clientSignature: str, clientPublicKey: str) """
        pass

    ClientPublicKey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClientPublicKey(self: SecuredApplicationAttribute) -> str

"""

    ClientSignature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClientSignature(self: SecuredApplicationAttribute) -> str

"""

    License = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: License(self: SecuredApplicationAttribute) -> str

"""

    OurSignature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OurSignature(self: SecuredApplicationAttribute) -> str

"""



class SystemObjects(object):
    # no doc
    ClassDictionary = None
    DynamicLinker = None
    ServiceDictionary = None
    Variables = None


class Utilities(object):
    """ Utilities() """
    @staticmethod
    def GetErrorStatus(eStatus):
        """ GetErrorStatus(eStatus: ErrorStatus) -> str """
        pass

    @staticmethod
    def GetRedirectedRegistryValue(subPath, propertyName):
        """ GetRedirectedRegistryValue(subPath: str, propertyName: str) -> str """
        pass

    @staticmethod
    def GetRedirectedRegistryValueMap(subPath):
        """ GetRedirectedRegistryValueMap(subPath: str) -> IDictionary[str, str] """
        pass

    @staticmethod
    def GetReservedString(reservedType, bGetLocalized):
        """ GetReservedString(reservedType: ReservedStringEnumType, bGetLocalized: bool) -> str """
        pass

    @staticmethod
    def TranslateReservedString(pGlobalName):
        """ TranslateReservedString(pGlobalName: str) -> str """
        pass


class Variable(DisposableWrapper):
    """ Variable(pImp: IntPtr, autoDelete: bool) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def Reset(self):
        """ Reset(self: Variable) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pImp, autoDelete):
        """ __new__(cls: type, pImp: IntPtr, autoDelete: bool) """
        pass

    IsLocked = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLocked(self: Variable) -> bool

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: Variable) -> bool

Set: IsReadOnly(self: Variable) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: Variable) -> str

"""

    PrimaryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrimaryType(self: Variable) -> Int16

"""

    Range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Range(self: Variable) -> RangeInfo

"""

    SecondaryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SecondaryType(self: Variable) -> SecondaryTypeInfo

"""

    Storage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Storage(self: Variable) -> StorageType

"""

    TypeFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TypeFlags(self: Variable) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: Variable) -> object

Set: Value(self: Variable) = value
"""


    Changed = None
    Changing = None
    RangeInfo = None
    SecondaryTypeInfo = None
    StorageType = None
    TypeFlagsInfo = None


class VariableChangedEventArgs(EventArgs):
    # no doc
    def Dispose(self):
        """ Dispose(self: VariableChangedEventArgs) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewValue(self: VariableChangedEventArgs) -> object

"""

    OldValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldValue(self: VariableChangedEventArgs) -> object

"""



class VariableChangedEventHandler(MulticastDelegate):
    """ VariableChangedEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: VariableChangedEventHandler, sender: object, e: VariableChangedEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: VariableChangedEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: VariableChangedEventHandler, sender: object, e: VariableChangedEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class VariableChangingEventArgs(EventArgs):
    # no doc
    def Dispose(self):
        """ Dispose(self: VariableChangingEventArgs) """
        pass

    def Veto(self, reason):
        """ Veto(self: VariableChangingEventArgs, reason: str) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    IsResetting = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsResetting(self: VariableChangingEventArgs) -> bool

"""

    NewValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewValue(self: VariableChangingEventArgs) -> object

Set: NewValue(self: VariableChangingEventArgs) = value
"""

    OldValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OldValue(self: VariableChangingEventArgs) -> object

"""



class VariableChangingEventHandler(MulticastDelegate):
    """ VariableChangingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: VariableChangingEventHandler, sender: object, e: VariableChangingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: VariableChangingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: VariableChangingEventHandler, sender: object, e: VariableChangingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class Variables(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetAllNames(self):
        """ GetAllNames(self: Variables) -> Array[str] """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: Variables) -> IEnumerator[Variable] """
        pass

    def Reset(self, filter):
        """ Reset(self: Variables, filter: StorageType) """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Variable](enumerable: IEnumerable[Variable], value: Variable) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Changed = None
    Changing = None


class WrapperAttribute(Attribute):
    """ WrapperAttribute(wrappedClass: str) """
    @staticmethod # known case of __new__
    def __new__(self, wrappedClass):
        """ __new__(cls: type, wrappedClass: str) """
        pass

    WrappedClass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WrappedClass(self: WrapperAttribute) -> str

"""



