# encoding: utf-8
# module Autodesk.Gis.Map.Platform.Internal calls itself Internal
# from Autodesk.Map.Platform, Version=24.0.30.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcMapActionHandledEventArgs(AcMapEventArgs):
    """
    AcMapActionHandledEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapActionHandledEventArgs(geometryType: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: AcMapActionHandledEventArgs) """
        pass

    def GetActionType(self):
        """ GetActionType(self: AcMapActionHandledEventArgs) -> int """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapActionHandledEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapActionHandledEventArgs) -> IntPtr """
        pass

    def GetHandled(self):
        """ GetHandled(self: AcMapActionHandledEventArgs) -> bool """
        pass

    def GetLayer(self):
        """ GetLayer(self: AcMapActionHandledEventArgs) -> AcMapLayer """
        pass

    def SetHandled(self):
        """ SetHandled(self: AcMapActionHandledEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, geometryType: int, pLayer: AcMapLayer)
        """
        pass

    ActionType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActionType(self: AcMapActionHandledEventArgs) -> int

"""

    Layer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layer(self: AcMapActionHandledEventArgs) -> AcMapLayer

"""


    swigCMemOwn = None


class AcMapBulkCommandEventArgs(AcMapEventArgs):
    """
    AcMapBulkCommandEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapBulkCommandEventArgs(name: str, bCommandWasCancelled: bool)
    """
    def Dispose(self):
        """ Dispose(self: AcMapBulkCommandEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapBulkCommandEventArgs) -> int """
        pass

    def GetCommandWasCancelled(self):
        """ GetCommandWasCancelled(self: AcMapBulkCommandEventArgs) -> bool """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapBulkCommandEventArgs) -> IntPtr """
        pass

    def GetGlobalCmdName(self):
        """ GetGlobalCmdName(self: AcMapBulkCommandEventArgs) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, bCommandWasCancelled: bool)
        """
        pass

    CommandWasCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandWasCancelled(self: AcMapBulkCommandEventArgs) -> bool

"""

    GlobalCmdName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalCmdName(self: AcMapBulkCommandEventArgs) -> str

"""


    swigCMemOwn = None


class AcMapBulkFeaturesToBeErasedEventArgs(AcMapEventArgs):
    """
    AcMapBulkFeaturesToBeErasedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapBulkFeaturesToBeErasedEventArgs(featuresToBeErased: AcMapSelection)
    """
    def Dispose(self):
        """ Dispose(self: AcMapBulkFeaturesToBeErasedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapBulkFeaturesToBeErasedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapBulkFeaturesToBeErasedEventArgs) -> IntPtr """
        pass

    def GetDisplayConfirmationDialog(self):
        """ GetDisplayConfirmationDialog(self: AcMapBulkFeaturesToBeErasedEventArgs) -> bool """
        pass

    def GetFeaturesToBeErased(self):
        """ GetFeaturesToBeErased(self: AcMapBulkFeaturesToBeErasedEventArgs) -> AcMapSelection """
        pass

    def GetPreventEraseOfFeatures(self):
        """ GetPreventEraseOfFeatures(self: AcMapBulkFeaturesToBeErasedEventArgs) -> bool """
        pass

    def SetDisplayConfirmationDialog(self, bNewValue):
        """ SetDisplayConfirmationDialog(self: AcMapBulkFeaturesToBeErasedEventArgs, bNewValue: bool) """
        pass

    def SetPreventEraseOfFeatures(self, bNewValue):
        """ SetPreventEraseOfFeatures(self: AcMapBulkFeaturesToBeErasedEventArgs, bNewValue: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, featuresToBeErased: AcMapSelection)
        """
        pass

    DisplayConfirmationDialog = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayConfirmationDialog(self: AcMapBulkFeaturesToBeErasedEventArgs) -> bool

Set: DisplayConfirmationDialog(self: AcMapBulkFeaturesToBeErasedEventArgs) = value
"""

    FeaturesToBeErased = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeaturesToBeErased(self: AcMapBulkFeaturesToBeErasedEventArgs) -> AcMapSelection

"""

    PreventEraseOfFeatures = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PreventEraseOfFeatures(self: AcMapBulkFeaturesToBeErasedEventArgs) -> bool

Set: PreventEraseOfFeatures(self: AcMapBulkFeaturesToBeErasedEventArgs) = value
"""


    swigCMemOwn = None


class AcMapCommandInvokedEventArgs(AcMapActionHandledEventArgs):
    """
    AcMapCommandInvokedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapCommandInvokedEventArgs(cmdGeometryType: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: AcMapCommandInvokedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapCommandInvokedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapCommandInvokedEventArgs) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, cmdGeometryType: int, pLayer: AcMapLayer)
        """
        pass

    swigCMemOwn = None


class AcMapContextMenuItemEventArgs(AcMapActionHandledEventArgs):
    """
    AcMapContextMenuItemEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapContextMenuItemEventArgs(menuGeometryType: int, pLayer: AcMapLayer)
    """
    def Dispose(self):
        """ Dispose(self: AcMapContextMenuItemEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapContextMenuItemEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapContextMenuItemEventArgs) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, menuGeometryType: int, pLayer: AcMapLayer)
        """
        pass

    swigCMemOwn = None


class AcMapEditingCloningSupportedEventArgs(AcMapEventArgs):
    """
    AcMapEditingCloningSupportedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapEditingCloningSupportedEventArgs()
    """
    def Dispose(self):
        """ Dispose(self: AcMapEditingCloningSupportedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapEditingCloningSupportedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapEditingCloningSupportedEventArgs) -> IntPtr """
        pass

    def GetEditingCloningSupported(self):
        """ GetEditingCloningSupported(self: AcMapEditingCloningSupportedEventArgs) -> bool """
        pass

    def GetHandled(self):
        """ GetHandled(self: AcMapEditingCloningSupportedEventArgs) -> bool """
        pass

    def SetEditingCloningSupported(self, bNewValue):
        """ SetEditingCloningSupported(self: AcMapEditingCloningSupportedEventArgs, bNewValue: bool) """
        pass

    def SetHandled(self, bNewValue):
        """ SetHandled(self: AcMapEditingCloningSupportedEventArgs, bNewValue: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    EditingCloningSupported = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EditingCloningSupported(self: AcMapEditingCloningSupportedEventArgs) -> bool

Set: EditingCloningSupported(self: AcMapEditingCloningSupportedEventArgs) = value
"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handled(self: AcMapEditingCloningSupportedEventArgs) -> bool

Set: Handled(self: AcMapEditingCloningSupportedEventArgs) = value
"""


    swigCMemOwn = None


class AcMapEditingDigitizeAddPromptArgs(AcMapEventArgs):
    """
    AcMapEditingDigitizeAddPromptArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapEditingDigitizeAddPromptArgs()
    """
    def Dispose(self):
        """ Dispose(self: AcMapEditingDigitizeAddPromptArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapEditingDigitizeAddPromptArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapEditingDigitizeAddPromptArgs) -> IntPtr """
        pass

    def GetInitialPromptFormatString(self):
        """ GetInitialPromptFormatString(self: AcMapEditingDigitizeAddPromptArgs) -> str """
        pass

    def GetKeyWord(self):
        """ GetKeyWord(self: AcMapEditingDigitizeAddPromptArgs) -> str """
        pass

    def GetKeyWordAdded(self):
        """ GetKeyWordAdded(self: AcMapEditingDigitizeAddPromptArgs) -> bool """
        pass

    def GetLocalizedKeyWord(self):
        """ GetLocalizedKeyWord(self: AcMapEditingDigitizeAddPromptArgs) -> str """
        pass

    def GetPromptSeperator(self):
        """ GetPromptSeperator(self: AcMapEditingDigitizeAddPromptArgs) -> str """
        pass

    def SetInitialPromptFormatString(self, Prompt):
        """ SetInitialPromptFormatString(self: AcMapEditingDigitizeAddPromptArgs, Prompt: str) """
        pass

    def SetKeyWord(self, KeyWord):
        """ SetKeyWord(self: AcMapEditingDigitizeAddPromptArgs, KeyWord: str) """
        pass

    def SetKeyWordAdded(self, bNewValue):
        """ SetKeyWordAdded(self: AcMapEditingDigitizeAddPromptArgs, bNewValue: bool) """
        pass

    def SetLocalizedKeyWord(self, LocalizedKeyWord):
        """ SetLocalizedKeyWord(self: AcMapEditingDigitizeAddPromptArgs, LocalizedKeyWord: str) """
        pass

    def SetPromptSeperator(self, Prompt):
        """ SetPromptSeperator(self: AcMapEditingDigitizeAddPromptArgs, Prompt: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    InitialPromptFormatString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialPromptFormatString(self: AcMapEditingDigitizeAddPromptArgs) -> str

Set: InitialPromptFormatString(self: AcMapEditingDigitizeAddPromptArgs) = value
"""

    KeyWord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyWord(self: AcMapEditingDigitizeAddPromptArgs) -> str

Set: KeyWord(self: AcMapEditingDigitizeAddPromptArgs) = value
"""

    KeyWordAdded = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: KeyWordAdded(self: AcMapEditingDigitizeAddPromptArgs) -> bool

Set: KeyWordAdded(self: AcMapEditingDigitizeAddPromptArgs) = value
"""

    LocalizedKeyWord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LocalizedKeyWord(self: AcMapEditingDigitizeAddPromptArgs) -> str

Set: LocalizedKeyWord(self: AcMapEditingDigitizeAddPromptArgs) = value
"""

    PromptSeperator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PromptSeperator(self: AcMapEditingDigitizeAddPromptArgs) -> str

Set: PromptSeperator(self: AcMapEditingDigitizeAddPromptArgs) = value
"""


    swigCMemOwn = None


class AcMapEditingEventArgs(AcMapEventArgs):
    """
    AcMapEditingEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapEditingEventArgs(resource: MgResourceIdentifier, feature: AcMapFeature)
    """
    def Dispose(self):
        """ Dispose(self: AcMapEditingEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapEditingEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapEditingEventArgs) -> IntPtr """
        pass

    def GetFeature(self):
        """ GetFeature(self: AcMapEditingEventArgs) -> AcMapFeature """
        pass

    def GetResourceIdentifier(self):
        """ GetResourceIdentifier(self: AcMapEditingEventArgs) -> MgResourceIdentifier """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: MgResourceIdentifier, feature: AcMapFeature)
        """
        pass

    swigCMemOwn = None


class AcMapEditingKeyWordSelectedArgs(AcMapEventArgs):
    """
    AcMapEditingKeyWordSelectedArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapEditingKeyWordSelectedArgs()
    AcMapEditingKeyWordSelectedArgs(option: str, points: MgPointCollection, bulges: MgDoubleCollection, mvalues: MgDoubleCollection)
    """
    def Dispose(self):
        """ Dispose(self: AcMapEditingKeyWordSelectedArgs) """
        pass

    def GetBulges(self):
        """ GetBulges(self: AcMapEditingKeyWordSelectedArgs) -> MgDoubleCollection """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapEditingKeyWordSelectedArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapEditingKeyWordSelectedArgs) -> IntPtr """
        pass

    def GetHandled(self):
        """ GetHandled(self: AcMapEditingKeyWordSelectedArgs) -> bool """
        pass

    def GetMValues(self):
        """ GetMValues(self: AcMapEditingKeyWordSelectedArgs) -> MgDoubleCollection """
        pass

    def GetPoints(self):
        """ GetPoints(self: AcMapEditingKeyWordSelectedArgs) -> MgPointCollection """
        pass

    def GetSelectedOption(self):
        """ GetSelectedOption(self: AcMapEditingKeyWordSelectedArgs) -> str """
        pass

    def SetBulges(self, bugles):
        """ SetBulges(self: AcMapEditingKeyWordSelectedArgs, bugles: MgDoubleCollection) """
        pass

    def SetHandled(self, bHandled):
        """ SetHandled(self: AcMapEditingKeyWordSelectedArgs, bHandled: bool) """
        pass

    def SetMValues(self, mvalues):
        """ SetMValues(self: AcMapEditingKeyWordSelectedArgs, mvalues: MgDoubleCollection) """
        pass

    def SetPoints(self, points):
        """ SetPoints(self: AcMapEditingKeyWordSelectedArgs, points: MgPointCollection) """
        pass

    def SetSelectedOption(self, option):
        """ SetSelectedOption(self: AcMapEditingKeyWordSelectedArgs, option: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, option: str, points: MgPointCollection, bulges: MgDoubleCollection, mvalues: MgDoubleCollection)
        """
        pass

    Bulges = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bulges(self: AcMapEditingKeyWordSelectedArgs) -> MgDoubleCollection

Set: Bulges(self: AcMapEditingKeyWordSelectedArgs) = value
"""

    Handled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Handled(self: AcMapEditingKeyWordSelectedArgs) -> bool

Set: Handled(self: AcMapEditingKeyWordSelectedArgs) = value
"""

    MValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MValues(self: AcMapEditingKeyWordSelectedArgs) -> MgDoubleCollection

Set: MValues(self: AcMapEditingKeyWordSelectedArgs) = value
"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: AcMapEditingKeyWordSelectedArgs) -> MgPointCollection

Set: Points(self: AcMapEditingKeyWordSelectedArgs) = value
"""

    SelectedOption = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectedOption(self: AcMapEditingKeyWordSelectedArgs) -> str

"""


    swigCMemOwn = None


class AcMapEditingService(MgService):
    """ AcMapEditingService(cPtr: IntPtr, cMemoryOwn: bool) """
    def AcquireLineString(self, pFeatureLayer, properties, prompt, pOptions):
        """ AcquireLineString(self: AcMapEditingService, pFeatureLayer: AcMapLayer, properties: MgPropertyCollection, prompt: str, pOptions: AcMapFeatureAcquisitionOptions) -> int """
        pass

    def AcquirePoint(self, pFeatureLayer, properties, prompt, pOptions):
        """ AcquirePoint(self: AcMapEditingService, pFeatureLayer: AcMapLayer, properties: MgPropertyCollection, prompt: str, pOptions: AcMapFeatureAcquisitionOptions) -> int """
        pass

    def AcquirePolygon(self, pFeatureLayer, properties, prompt, pOptions):
        """ AcquirePolygon(self: AcMapEditingService, pFeatureLayer: AcMapLayer, properties: MgPropertyCollection, prompt: str, pOptions: AcMapFeatureAcquisitionOptions) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapEditingService) """
        pass

    def FireDigitizeNotification(self, resource, classDefinition, propertyCol, identityCol, info):
        """ FireDigitizeNotification(self: AcMapEditingService, resource: MgResourceIdentifier, classDefinition: MgClassDefinition, propertyCol: MgPropertyCollection, identityCol: AcMapIdentityCollection, info: int) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapEditingService) -> IntPtr """
        pass

    @staticmethod
    def GetInstance():
        """ GetInstance() -> AcMapEditingService """
        pass

    def OnAddDigitizePrompt(self, args):
        """ OnAddDigitizePrompt(self: AcMapEditingService, args: AcMapEditingDigitizeAddPromptArgs) """
        pass

    def OnBulkCommandEndedOrCancelled(self, args):
        """ OnBulkCommandEndedOrCancelled(self: AcMapEditingService, args: AcMapBulkCommandEventArgs) """
        pass

    def OnBulkCommandStarted(self, args):
        """ OnBulkCommandStarted(self: AcMapEditingService, args: AcMapBulkCommandEventArgs) """
        pass

    def OnBulkFeaturesToBeErased(self, args):
        """ OnBulkFeaturesToBeErased(self: AcMapEditingService, args: AcMapBulkFeaturesToBeErasedEventArgs) """
        pass

    def OnCreateCommandInvoked(self, args):
        """ OnCreateCommandInvoked(self: AcMapEditingService, args: AcMapCommandInvokedEventArgs) """
        pass

    def OnDigitizeKeyWordSelected(self, args):
        """ OnDigitizeKeyWordSelected(self: AcMapEditingService, args: AcMapEditingKeyWordSelectedArgs) """
        pass

    def OnFeatureDigitizeCanceled(self, args):
        """ OnFeatureDigitizeCanceled(self: AcMapEditingService, args: AcMapEditingEventArgs) """
        pass

    def OnFeatureDigitized(self, args):
        """ OnFeatureDigitized(self: AcMapEditingService, args: AcMapEditingEventArgs) """
        pass

    def OnFeatureDigitizeUpdated(self, args):
        """ OnFeatureDigitizeUpdated(self: AcMapEditingService, args: AcMapEditingEventArgs) """
        pass

    def OnFeaturesCloneCanceled(self, args):
        """ OnFeaturesCloneCanceled(self: AcMapEditingService, args: AcMapCloningEventArgs) """
        pass

    def OnFeaturesCloned(self, args):
        """ OnFeaturesCloned(self: AcMapEditingService, args: AcMapCloningEventArgs) """
        pass

    def OnFeaturesToBeCloned(self, args):
        """ OnFeaturesToBeCloned(self: AcMapEditingService, args: AcMapCloningCancelHandledEventArgs) """
        pass

    def OnFeatureToBeDigitized(self, args):
        """ OnFeatureToBeDigitized(self: AcMapEditingService, args: AcMapEditingEventArgs) """
        pass

    def OnFeatureToBeGripEdited(self, args):
        """ OnFeatureToBeGripEdited(self: AcMapEditingService, args: AcMapGripEditEventArgs) """
        pass

    def OnGripEditBegin(self, args):
        """ OnGripEditBegin(self: AcMapEditingService, args: AcMapGripEditEventArgs) """
        pass

    def OnGripEditDrag(self, args):
        """ OnGripEditDrag(self: AcMapEditingService, args: AcMapGripEditEventArgs) """
        pass

    def OnGripEditEnd(self, args):
        """ OnGripEditEnd(self: AcMapEditingService, args: AcMapGripEditEventArgs) """
        pass

    def OnIsEditingCloningSupported(self, args):
        """ OnIsEditingCloningSupported(self: AcMapEditingService, args: AcMapEditingCloningSupportedEventArgs) """
        pass

    def OnMapAppendContextMenu(self, args):
        """ OnMapAppendContextMenu(self: AcMapEditingService, args: AcMapContextMenuItemEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    AddDigitizePrompt = None
    BulkCommandEndedOrCancelled = None
    BulkCommandStarted = None
    BulkFeaturesToBeErased = None
    CreateCommandInvoked = None
    DigitizeKeyWordSelected = None
    DigitizeReturnCodes = None
    FeatureDigitizeCanceled = None
    FeatureDigitized = None
    FeatureDigitizeUpdated = None
    FeaturesCloneCanceled = None
    FeaturesCloned = None
    FeaturesToBeCloned = None
    FeatureToBeDigitized = None
    FeatureToBeGripEdited = None
    GripEditBegin = None
    GripEditDrag = None
    GripEditEnd = None
    IsEditingCloningSupported = None
    MapActionTypes = None
    MapAppendContextMenu = None
    swigCMemOwn = None


class AcMapFeatureAcquisitionOptions(MgGuardDisposable):
    """
    AcMapFeatureAcquisitionOptions(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapFeatureAcquisitionOptions()
    """
    def Dispose(self):
        """ Dispose(self: AcMapFeatureAcquisitionOptions) """
        pass

    def GetAcquireStylized(self):
        """ GetAcquireStylized(self: AcMapFeatureAcquisitionOptions) -> bool """
        pass

    def GetAllowArcs(self):
        """ GetAllowArcs(self: AcMapFeatureAcquisitionOptions) -> bool """
        pass

    def GetAllowPolygonInnerRings(self):
        """ GetAllowPolygonInnerRings(self: AcMapFeatureAcquisitionOptions) -> bool """
        pass

    def GetAllowTessellatedArcs(self):
        """ GetAllowTessellatedArcs(self: AcMapFeatureAcquisitionOptions) -> bool """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapFeatureAcquisitionOptions) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureAcquisitionOptions) -> IntPtr """
        pass

    def GetGeometryPropertyName(self):
        """ GetGeometryPropertyName(self: AcMapFeatureAcquisitionOptions) -> str """
        pass

    def GetHasM(self):
        """ GetHasM(self: AcMapFeatureAcquisitionOptions) -> bool """
        pass

    def GetHasZ(self):
        """ GetHasZ(self: AcMapFeatureAcquisitionOptions) -> bool """
        pass

    def SetAcquireStylized(self, bAcquireStylized):
        """ SetAcquireStylized(self: AcMapFeatureAcquisitionOptions, bAcquireStylized: bool) """
        pass

    def SetAllowArcs(self, bAllowArcs):
        """ SetAllowArcs(self: AcMapFeatureAcquisitionOptions, bAllowArcs: bool) """
        pass

    def SetAllowPolygonInnerRings(self, bAllowRings):
        """ SetAllowPolygonInnerRings(self: AcMapFeatureAcquisitionOptions, bAllowRings: bool) """
        pass

    def SetAllowTessellatedArcs(self, bAllowTessellatedArcs):
        """ SetAllowTessellatedArcs(self: AcMapFeatureAcquisitionOptions, bAllowTessellatedArcs: bool) """
        pass

    def SetGeometryPropertyName(self, geomName):
        """ SetGeometryPropertyName(self: AcMapFeatureAcquisitionOptions, geomName: str) """
        pass

    def SetHasM(self, bHasM):
        """ SetHasM(self: AcMapFeatureAcquisitionOptions, bHasM: bool) """
        pass

    def SetHasZ(self, bHasZ):
        """ SetHasZ(self: AcMapFeatureAcquisitionOptions, bHasZ: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    AcquireStylized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AcquireStylized(self: AcMapFeatureAcquisitionOptions) -> bool

Set: AcquireStylized(self: AcMapFeatureAcquisitionOptions) = value
"""

    AllowArcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowArcs(self: AcMapFeatureAcquisitionOptions) -> bool

Set: AllowArcs(self: AcMapFeatureAcquisitionOptions) = value
"""

    AllowPolygonInnerRings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowPolygonInnerRings(self: AcMapFeatureAcquisitionOptions) -> bool

Set: AllowPolygonInnerRings(self: AcMapFeatureAcquisitionOptions) = value
"""

    AllowTessellatedArcs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AllowTessellatedArcs(self: AcMapFeatureAcquisitionOptions) -> bool

Set: AllowTessellatedArcs(self: AcMapFeatureAcquisitionOptions) = value
"""

    GeometryPropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryPropertyName(self: AcMapFeatureAcquisitionOptions) -> str

Set: GeometryPropertyName(self: AcMapFeatureAcquisitionOptions) = value
"""

    HasM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasM(self: AcMapFeatureAcquisitionOptions) -> bool

Set: HasM(self: AcMapFeatureAcquisitionOptions) = value
"""

    HasZ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasZ(self: AcMapFeatureAcquisitionOptions) -> bool

Set: HasZ(self: AcMapFeatureAcquisitionOptions) = value
"""


    swigCMemOwn = None


class AcMapGripEditEventArgs(AcMapEditingEventArgs):
    """
    AcMapGripEditEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapGripEditEventArgs(resource: MgResourceIdentifier, feature: AcMapFeature)
    """
    def Dispose(self):
        """ Dispose(self: AcMapGripEditEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapGripEditEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapGripEditEventArgs) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: MgResourceIdentifier, feature: AcMapFeature)
        """
        pass

    swigCMemOwn = None


class AcMapLabelHorizontal(object):
    """ AcMapLabelHorizontal() """
    kCenter = None
    kLeft = None
    kRight = None


class AcMapLabelInfo(MgGuardDisposable):
    """ AcMapLabelInfo(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapLabelInfo) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLabelInfo) -> IntPtr """
        pass

    def GetElementId(self):
        """ GetElementId(self: AcMapLabelInfo) -> Int64 """
        pass

    def GetExpr(self):
        """ GetExpr(self: AcMapLabelInfo) -> str """
        pass

    def GetFeatureId(self):
        """ GetFeatureId(self: AcMapLabelInfo) -> int """
        pass

    def GetHAlign(self):
        """ GetHAlign(self: AcMapLabelInfo) -> Int16 """
        pass

    def GetJustify(self):
        """ GetJustify(self: AcMapLabelInfo) -> Int16 """
        pass

    def GetRotation(self):
        """ GetRotation(self: AcMapLabelInfo) -> float """
        pass

    def GetText(self):
        """ GetText(self: AcMapLabelInfo) -> str """
        pass

    def GetTextHeight(self):
        """ GetTextHeight(self: AcMapLabelInfo) -> float """
        pass

    def GetTextType(self):
        """ GetTextType(self: AcMapLabelInfo) -> Int16 """
        pass

    def GetVAlign(self):
        """ GetVAlign(self: AcMapLabelInfo) -> Int16 """
        pass

    def GetX(self):
        """ GetX(self: AcMapLabelInfo) -> float """
        pass

    def GetY(self):
        """ GetY(self: AcMapLabelInfo) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    ElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementId(self: AcMapLabelInfo) -> Int64

"""

    Expr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Expr(self: AcMapLabelInfo) -> str

"""

    FeatureId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureId(self: AcMapLabelInfo) -> int

"""

    HAlign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HAlign(self: AcMapLabelInfo) -> Int16

"""

    Justify = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Justify(self: AcMapLabelInfo) -> Int16

"""

    Rotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Rotation(self: AcMapLabelInfo) -> float

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: AcMapLabelInfo) -> str

"""

    TextHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextHeight(self: AcMapLabelInfo) -> float

"""

    TextType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TextType(self: AcMapLabelInfo) -> Int16

"""

    VAlign = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: VAlign(self: AcMapLabelInfo) -> Int16

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: AcMapLabelInfo) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: AcMapLabelInfo) -> float

"""


    swigCMemOwn = None


class AcMapLabelInfoCollection(MgGuardDisposable):
    """
    AcMapLabelInfoCollection(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapLabelInfoCollection()
    """
    def Add(self, value):
        """ Add(self: AcMapLabelInfoCollection, value: AcMapLabelInfo) """
        pass

    def Clear(self):
        """ Clear(self: AcMapLabelInfoCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: AcMapLabelInfoCollection, value: AcMapLabelInfo) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: AcMapLabelInfoCollection, array: Array[AcMapLabelInfo], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapLabelInfoCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: AcMapLabelInfoCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLabelInfoCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: AcMapLabelInfoCollection) -> IEnumerator[AcMapLabelInfo] """
        pass

    def GetItem(self, index):
        """ GetItem(self: AcMapLabelInfoCollection, index: int) -> AcMapLabelInfo """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: AcMapLabelInfoCollection, value: AcMapLabelInfo) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: AcMapLabelInfoCollection, index: int, value: AcMapLabelInfo) """
        pass

    def Remove(self, value):
        """ Remove(self: AcMapLabelInfoCollection, value: AcMapLabelInfo) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: AcMapLabelInfoCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: AcMapLabelInfoCollection, index: int, value: AcMapLabelInfo) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[AcMapLabelInfo], item: AcMapLabelInfo) -> bool """
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
    """Get: Count(self: AcMapLabelInfoCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: AcMapLabelInfoCollection) -> bool

"""


    AcMapLabelInfoCollectionEnumerator = None
    swigCMemOwn = None


class AcMapLabelType(object):
    """ AcMapLabelType() """
    kConfigured = None
    kConfiguredSymbol = None
    kEditable = None
    kEditableConfiguredSymbol = None
    kEditableSymbol = None
    kLabel = None
    kSymbol = None


class AcMapLabelVertical(object):
    """ AcMapLabelVertical() """
    kAscent = None
    kBase = None
    kCap = None
    kDescent = None
    kHalf = None


class AcMapLayerOrientationProperties(MgGuardDisposable):
    """
    AcMapLayerOrientationProperties(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapLayerOrientationProperties(orientationPropertyName: str, orientationUnits: int, orientationBaseAngle: float, orientationDirection: int)
    """
    def Dispose(self):
        """ Dispose(self: AcMapLayerOrientationProperties) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapLayerOrientationProperties) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLayerOrientationProperties) -> IntPtr """
        pass

    def GetOrientationBaseAngle(self):
        """ GetOrientationBaseAngle(self: AcMapLayerOrientationProperties) -> float """
        pass

    def GetOrientationDirection(self):
        """ GetOrientationDirection(self: AcMapLayerOrientationProperties) -> int """
        pass

    def GetOrientationPropertyName(self):
        """ GetOrientationPropertyName(self: AcMapLayerOrientationProperties) -> str """
        pass

    def GetOrientationUnits(self):
        """ GetOrientationUnits(self: AcMapLayerOrientationProperties) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, orientationPropertyName: str, orientationUnits: int, orientationBaseAngle: float, orientationDirection: int)
        """
        pass

    swigCMemOwn = None


class AcMapLegend(MgLegendBase):
    """ AcMapLegend(cPtr: IntPtr, cMemoryOwn: bool) """
    @staticmethod
    def CreateEntity(viewportId, tableStyleId):
        """ CreateEntity(viewportId: ObjectId, tableStyleId: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def CreateInstance(blockReferenceId):
        """ CreateInstance(blockReferenceId: ObjectId) -> AcMapLegend """
        pass

    def CreateLegendItem(self, elementId, displayName, visible, rowIndex):
        """ CreateLegendItem(self: AcMapLegend, elementId: ObjectId, displayName: str, visible: bool, rowIndex: int) -> AcMapLegendItem """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapLegend) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLegend) -> IntPtr """
        pass

    @staticmethod
    def GetInstance(blockReferenceId):
        """ GetInstance(blockReferenceId: ObjectId) -> AcMapLegend """
        pass

    def GetIsLinkedWithViewport(self):
        """ GetIsLinkedWithViewport(self: AcMapLegend) -> bool """
        pass

    def GetLegendItems(self):
        """ GetLegendItems(self: AcMapLegend) -> MgLegendItemCollection """
        pass

    def GetPrintLayout(self):
        """ GetPrintLayout(self: AcMapLegend) -> AcMapPrintLayout """
        pass

    def GetTableStyle(self):
        """ GetTableStyle(self: AcMapLegend) -> ObjectId """
        pass

    def GetTitle(self):
        """ GetTitle(self: AcMapLegend) -> str """
        pass

    def Highlight(self):
        """ Highlight(self: AcMapLegend) """
        pass

    @staticmethod
    def IsLegend(blockReferenceId):
        """ IsLegend(blockReferenceId: ObjectId) -> bool """
        pass

    def SetLegendItems(self, legendItems):
        """ SetLegendItems(self: AcMapLegend, legendItems: MgLegendItemCollection) """
        pass

    def SetLinkedViewport(self, viewportEntityId):
        """ SetLinkedViewport(self: AcMapLegend, viewportEntityId: ObjectId) """
        pass

    def SetTableStyle(self, tableStyleId):
        """ SetTableStyle(self: AcMapLegend, tableStyleId: ObjectId) """
        pass

    def SetTitle(self, title):
        """ SetTitle(self: AcMapLegend, title: str) """
        pass

    def Unhighlight(self):
        """ Unhighlight(self: AcMapLegend) """
        pass

    def UpdateTableContents(self, keepTableStyle):
        """ UpdateTableContents(self: AcMapLegend, keepTableStyle: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    IsLinkedWithViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLinkedWithViewport(self: AcMapLegend) -> bool

"""

    LegendItems = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendItems(self: AcMapLegend) -> MgLegendItemCollection

Set: LegendItems(self: AcMapLegend) = value
"""

    LinkedEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkedEntity(self: AcMapLegend) -> ObjectId

"""

    LinkedViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkedViewport(self: AcMapLegend) -> ObjectId

Set: LinkedViewport(self: AcMapLegend) = value
"""

    PrintLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintLayout(self: AcMapLegend) -> AcMapPrintLayout

"""

    TableStyle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TableStyle(self: AcMapLegend) -> ObjectId

Set: TableStyle(self: AcMapLegend) = value
"""

    Title = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Title(self: AcMapLegend) -> str

Set: Title(self: AcMapLegend) = value
"""


    swigCMemOwn = None


class AcMapLegendItem(MgLegendItemBase):
    """ AcMapLegendItem(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapLegendItem) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapLegendItem) -> IntPtr """
        pass

    def GetDisplayName(self):
        """ GetDisplayName(self: AcMapLegendItem) -> str """
        pass

    def GetElementId(self):
        """ GetElementId(self: AcMapLegendItem) -> ObjectId """
        pass

    def GetIsVisible(self):
        """ GetIsVisible(self: AcMapLegendItem) -> bool """
        pass

    def GetRowIndex(self):
        """ GetRowIndex(self: AcMapLegendItem) -> int """
        pass

    def SetDisplayName(self, displayName):
        """ SetDisplayName(self: AcMapLegendItem, displayName: str) -> bool """
        pass

    def SetIsVisible(self, visible):
        """ SetIsVisible(self: AcMapLegendItem, visible: bool) -> bool """
        pass

    def SetRowIndex(self, rowIndex):
        """ SetRowIndex(self: AcMapLegendItem, rowIndex: int) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: AcMapLegendItem) -> str

Set: DisplayName(self: AcMapLegendItem) = value
"""

    ElementId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElementId(self: AcMapLegendItem) -> ObjectId

"""

    IsVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsVisible(self: AcMapLegendItem) -> bool

Set: IsVisible(self: AcMapLegendItem) = value
"""

    RowIndex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowIndex(self: AcMapLegendItem) -> int

Set: RowIndex(self: AcMapLegendItem) = value
"""


    swigCMemOwn = None


class AcMapMapViewport(MgMapViewportBase):
    """ AcMapMapViewport(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapMapViewport) """
        pass

    def GetAssociatedMap(self):
        """ GetAssociatedMap(self: AcMapMapViewport) -> MgMapBase """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapMapViewport) -> IntPtr """
        pass

    @staticmethod
    def GetInstance(viewportEntityId):
        """ GetInstance(viewportEntityId: ObjectId) -> AcMapMapViewport """
        pass

    def GetIsAssociated(self):
        """ GetIsAssociated(self: AcMapMapViewport) -> bool """
        pass

    def GetPrintLayout(self):
        """ GetPrintLayout(self: AcMapMapViewport) -> AcMapPrintLayout """
        pass

    def GetScale(self):
        """ GetScale(self: AcMapMapViewport) -> float """
        pass

    def Highlight(self):
        """ Highlight(self: AcMapMapViewport) """
        pass

    @staticmethod
    def InstanceExists(viewportEntityId):
        """ InstanceExists(viewportEntityId: ObjectId) -> bool """
        pass

    @staticmethod
    def RegenViewport(viewportEntityId):
        """ RegenViewport(viewportEntityId: ObjectId) """
        pass

    def SetAssociatedMap(self, map):
        """ SetAssociatedMap(self: AcMapMapViewport, map: MgMapBase) """
        pass

    def SetScale(self, scale):
        """ SetScale(self: AcMapMapViewport, scale: float) """
        pass

    def Unhighlight(self):
        """ Unhighlight(self: AcMapMapViewport) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    AssociatedMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssociatedMap(self: AcMapMapViewport) -> MgMapBase

Set: AssociatedMap(self: AcMapMapViewport) = value
"""

    HiddenLayers = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HiddenLayers(self: AcMapMapViewport) -> List[str]

Set: HiddenLayers(self: AcMapMapViewport) = value
"""

    IsAssociated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAssociated(self: AcMapMapViewport) -> bool

"""

    Legend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Legend(self: AcMapMapViewport) -> AcMapLegend

"""

    LinkedElements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkedElements(self: AcMapMapViewport) -> MgPrintLayoutElementCollection

"""

    NorthArrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NorthArrow(self: AcMapMapViewport) -> AcMapNorthArrow

"""

    PrintLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintLayout(self: AcMapMapViewport) -> AcMapPrintLayout

"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: AcMapMapViewport) -> float

Set: Scale(self: AcMapMapViewport) = value
"""

    ScaleBars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ScaleBars(self: AcMapMapViewport) -> IEnumerable[AcMapScaleBar]

"""

    ViewportEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewportEntity(self: AcMapMapViewport) -> ObjectId

"""


    swigCMemOwn = None


class AcMapNorthArrow(MgNorthArrowBase):
    """ AcMapNorthArrow(cPtr: IntPtr, cMemoryOwn: bool) """
    @staticmethod
    def CreateInstance(blockReferenceId):
        """ CreateInstance(blockReferenceId: ObjectId) -> AcMapNorthArrow """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapNorthArrow) """
        pass

    def GetAngle(self):
        """ GetAngle(self: AcMapNorthArrow) -> float """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapNorthArrow) -> IntPtr """
        pass

    @staticmethod
    def GetInstance(blockReferenceId):
        """ GetInstance(blockReferenceId: ObjectId) -> AcMapNorthArrow """
        pass

    def GetIsLinkedWithViewport(self):
        """ GetIsLinkedWithViewport(self: AcMapNorthArrow) -> bool """
        pass

    def GetPrintLayout(self):
        """ GetPrintLayout(self: AcMapNorthArrow) -> AcMapPrintLayout """
        pass

    def Highlight(self):
        """ Highlight(self: AcMapNorthArrow) """
        pass

    @staticmethod
    def IsNorthArrow(blockReferenceId):
        """ IsNorthArrow(blockReferenceId: ObjectId) -> bool """
        pass

    def ResetNorth(self):
        """ ResetNorth(self: AcMapNorthArrow) """
        pass

    def SetAngle(self, angle):
        """ SetAngle(self: AcMapNorthArrow, angle: float) """
        pass

    def SetLinkedViewport(self, viewportEntityId):
        """ SetLinkedViewport(self: AcMapNorthArrow, viewportEntityId: ObjectId) """
        pass

    def Unhighlight(self):
        """ Unhighlight(self: AcMapNorthArrow) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Angle = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Angle(self: AcMapNorthArrow) -> float

Set: Angle(self: AcMapNorthArrow) = value
"""

    IsLinkedWithViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLinkedWithViewport(self: AcMapNorthArrow) -> bool

"""

    LinkedEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkedEntity(self: AcMapNorthArrow) -> ObjectId

"""

    LinkedViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkedViewport(self: AcMapNorthArrow) -> ObjectId

Set: LinkedViewport(self: AcMapNorthArrow) = value
"""

    PrintLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintLayout(self: AcMapNorthArrow) -> AcMapPrintLayout

"""


    swigCMemOwn = None


class AcMapPrintLayout(MgPrintLayoutBase):
    """ AcMapPrintLayout(cPtr: IntPtr, cMemoryOwn: bool) """
    @staticmethod
    def AssociateViewportWithMap(viewportEntityId, map):
        """ AssociateViewportWithMap(viewportEntityId: ObjectId, map: MgMapBase) """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapPrintLayout) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapPrintLayout) -> IntPtr """
        pass

    def GetElements(self):
        """ GetElements(self: AcMapPrintLayout) -> MgPrintLayoutElementCollection """
        pass

    def GetLinkedMapViewport(self, blockId):
        """ GetLinkedMapViewport(self: AcMapPrintLayout, blockId: ObjectId) -> AcMapMapViewport """
        pass

    def GetLinkedPrintLayoutElements(self, viewportId):
        """ GetLinkedPrintLayoutElements(self: AcMapPrintLayout, viewportId: ObjectId) -> MgPrintLayoutElementCollection """
        pass

    @staticmethod
    def HighlightLinkedElements(viewportId):
        """ HighlightLinkedElements(viewportId: ObjectId) """
        pass

    @staticmethod
    def HighlightLinkedViewport(blockId):
        """ HighlightLinkedViewport(blockId: ObjectId) """
        pass

    @staticmethod
    def UnhighlightLinkedElements(viewportId):
        """ UnhighlightLinkedElements(viewportId: ObjectId) """
        pass

    @staticmethod
    def UnhighlightLinkedViewport(blockId):
        """ UnhighlightLinkedViewport(blockId: ObjectId) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: AcMapPrintLayout) -> Database

"""

    Elements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Elements(self: AcMapPrintLayout) -> MgPrintLayoutElementCollection

"""

    LayoutId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutId(self: AcMapPrintLayout) -> ObjectId

"""


    swigCMemOwn = None


class AcMapPrintLayoutElementEventArgs(AcMapEventArgs):
    """
    AcMapPrintLayoutElementEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapPrintLayoutElementEventArgs(pElement: MgPrintLayoutElementBase, pLayout: AcMapPrintLayout)
    """
    def Dispose(self):
        """ Dispose(self: AcMapPrintLayoutElementEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapPrintLayoutElementEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapPrintLayoutElementEventArgs) -> IntPtr """
        pass

    def GetElement(self):
        """ GetElement(self: AcMapPrintLayoutElementEventArgs) -> MgPrintLayoutElementBase """
        pass

    def GetLayout(self):
        """ GetLayout(self: AcMapPrintLayoutElementEventArgs) -> AcMapPrintLayout """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, pElement: MgPrintLayoutElementBase, pLayout: AcMapPrintLayout)
        """
        pass

    Element = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Element(self: AcMapPrintLayoutElementEventArgs) -> MgPrintLayoutElementBase

"""

    Layout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layout(self: AcMapPrintLayoutElementEventArgs) -> AcMapPrintLayout

"""


    swigCMemOwn = None


class AcMapPrintLayoutElementModifiedEventArgs(AcMapPrintLayoutElementEventArgs):
    """
    AcMapPrintLayoutElementModifiedEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    AcMapPrintLayoutElementModifiedEventArgs(pElement: MgPrintLayoutElementBase, pLayout: AcMapPrintLayout, modification: int)
    """
    def Dispose(self):
        """ Dispose(self: AcMapPrintLayoutElementModifiedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: AcMapPrintLayoutElementModifiedEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapPrintLayoutElementModifiedEventArgs) -> IntPtr """
        pass

    def GetModification(self):
        """ GetModification(self: AcMapPrintLayoutElementModifiedEventArgs) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, pElement: MgPrintLayoutElementBase, pLayout: AcMapPrintLayout, modification: int)
        """
        pass

    Modification = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Modification(self: AcMapPrintLayoutElementModifiedEventArgs) -> int

"""


    swigCMemOwn = None


class AcMapPrintLayoutService(MgPrintLayoutServiceBase):
    """ AcMapPrintLayoutService(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapPrintLayoutService) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapPrintLayoutService) -> IntPtr """
        pass

    @staticmethod
    def GetEnableVisualCueForViewports():
        """ GetEnableVisualCueForViewports() -> bool """
        pass

    @staticmethod
    def GetInstance(db):
        """ GetInstance(db: Database) -> AcMapPrintLayoutService """
        pass

    def GetLayouts(self):
        """ GetLayouts(self: AcMapPrintLayoutService) -> MgPrintLayoutCollection """
        pass

    @staticmethod
    def GetPrintLayoutForEntity(entityId):
        """ GetPrintLayoutForEntity(entityId: ObjectId) -> AcMapPrintLayout """
        pass

    @staticmethod
    def GetPrintLayoutForLayout(layoutId):
        """ GetPrintLayoutForLayout(layoutId: ObjectId) -> AcMapPrintLayout """
        pass

    def OnPrintLayoutElementAdded(self, pArgs):
        """ OnPrintLayoutElementAdded(self: AcMapPrintLayoutService, pArgs: AcMapPrintLayoutElementEventArgs) """
        pass

    def OnPrintLayoutElementModified(self, pArgs):
        """ OnPrintLayoutElementModified(self: AcMapPrintLayoutService, pArgs: AcMapPrintLayoutElementModifiedEventArgs) """
        pass

    def OnPrintLayoutElementRemoved(self, pArgs):
        """ OnPrintLayoutElementRemoved(self: AcMapPrintLayoutService, pArgs: AcMapPrintLayoutElementEventArgs) """
        pass

    @staticmethod
    def SetEnableVisualCueForViewports(Enable):
        """ SetEnableVisualCueForViewports(Enable: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: AcMapPrintLayoutService) -> Database

"""

    EnableVisualCueForViewports = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EnableVisualCueForViewports(self: AcMapPrintLayoutService) -> bool

Set: EnableVisualCueForViewports(self: AcMapPrintLayoutService) = value
"""

    Layouts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Layouts(self: AcMapPrintLayoutService) -> MgPrintLayoutCollection

"""


    PrintLayoutElementAdded = None
    PrintLayoutElementModified = None
    PrintLayoutElementRemoved = None
    swigCMemOwn = None


class AcMapScaleBar(MgScaleBarBase):
    """ AcMapScaleBar(cPtr: IntPtr, cMemoryOwn: bool) """
    @staticmethod
    def CreateInstance(blockReferenceId):
        """ CreateInstance(blockReferenceId: ObjectId) -> AcMapScaleBar """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapScaleBar) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapScaleBar) -> IntPtr """
        pass

    @staticmethod
    def GetInstance(blockReferenceId):
        """ GetInstance(blockReferenceId: ObjectId) -> AcMapScaleBar """
        pass

    def GetInteractiveMode(self):
        """ GetInteractiveMode(self: AcMapScaleBar) -> ScaleBarInteractiveMode """
        pass

    def GetIsLinkedWithViewport(self):
        """ GetIsLinkedWithViewport(self: AcMapScaleBar) -> bool """
        pass

    def GetPrecision(self):
        """ GetPrecision(self: AcMapScaleBar) -> int """
        pass

    def GetPrintLayout(self):
        """ GetPrintLayout(self: AcMapScaleBar) -> AcMapPrintLayout """
        pass

    def GetScale(self):
        """ GetScale(self: AcMapScaleBar) -> float """
        pass

    def Highlight(self):
        """ Highlight(self: AcMapScaleBar) """
        pass

    @staticmethod
    def IsScaleBar(blockReferenceId):
        """ IsScaleBar(blockReferenceId: ObjectId) -> bool """
        pass

    def SetInteractiveMode(self, interactiveMode):
        """ SetInteractiveMode(self: AcMapScaleBar, interactiveMode: ScaleBarInteractiveMode) """
        pass

    def SetLinkedViewport(self, viewportEntityId):
        """ SetLinkedViewport(self: AcMapScaleBar, viewportEntityId: ObjectId) """
        pass

    def SetPrecision(self, precision):
        """ SetPrecision(self: AcMapScaleBar, precision: int) """
        pass

    def SetProperties(self, scaleRatio, *__args):
        """ SetProperties(self: AcMapScaleBar, scaleRatio: float, dispUnits: UnitsValue, unitsLabel: str, divisionLengthInPaper: float)SetProperties(self: AcMapScaleBar, scaleRatio: float, divisionValue: float, dispUnits: UnitsValue, unitsLabel: str) """
        pass

    def SetScale(self, scale):
        """ SetScale(self: AcMapScaleBar, scale: float) """
        pass

    def Unhighlight(self):
        """ Unhighlight(self: AcMapScaleBar) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    DisplayUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayUnits(self: AcMapScaleBar) -> UnitsValue

Set: DisplayUnits(self: AcMapScaleBar) = value
"""

    DisplayUnitsLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayUnitsLabel(self: AcMapScaleBar) -> str

Set: DisplayUnitsLabel(self: AcMapScaleBar) = value
"""

    DivisionValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DivisionValue(self: AcMapScaleBar) -> float

Set: DivisionValue(self: AcMapScaleBar) = value
"""

    InteractiveMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InteractiveMode(self: AcMapScaleBar) -> ScaleBarInteractiveMode

Set: InteractiveMode(self: AcMapScaleBar) = value
"""

    IsLinkedWithViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsLinkedWithViewport(self: AcMapScaleBar) -> bool

"""

    LinkedEntity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkedEntity(self: AcMapScaleBar) -> ObjectId

"""

    LinkedViewport = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkedViewport(self: AcMapScaleBar) -> ObjectId

Set: LinkedViewport(self: AcMapScaleBar) = value
"""

    Precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Precision(self: AcMapScaleBar) -> int

Set: Precision(self: AcMapScaleBar) = value
"""

    PrintLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintLayout(self: AcMapScaleBar) -> AcMapPrintLayout

"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: AcMapScaleBar) -> float

Set: Scale(self: AcMapScaleBar) = value
"""


    ScaleBarInteractiveMode = None
    swigCMemOwn = None


class FeatureServiceExtensions(object):
    # no doc
    @staticmethod
    def CreateDataStoreAndApplySchema(featureService, fileName, resId, coordSysWKT, featureSchema):
        """ CreateDataStoreAndApplySchema(featureService: MgFeatureService, fileName: str, resId: MgResourceIdentifier, coordSysWKT: str, featureSchema: MgFeatureSchema) """
        pass

    @staticmethod
    def GetConnectionName(featureService, resourceService, resourceId):
        """ GetConnectionName(featureService: MgFeatureService, resourceService: MgResourceService, resourceId: MgResourceIdentifier) -> str """
        pass

    @staticmethod
    def GetFileName(featureService, resourceService, resourceId):
        """ GetFileName(featureService: MgFeatureService, resourceService: MgResourceService, resourceId: str) -> str """
        pass

    @staticmethod
    def GetProviderName(featureService, resourceService, resourceId):
        """ GetProviderName(featureService: MgFeatureService, resourceService: MgResourceService, resourceId: str) -> str """
        pass

    @staticmethod
    def IsConnected(featureService, resourceId):
        """ IsConnected(featureService: MgFeatureService, resourceId: MgResourceIdentifier) -> bool """
        pass

    @staticmethod
    def IsFileBasedConnectionReadOnly(featureService, resourceService, resourceId):
        """ IsFileBasedConnectionReadOnly(featureService: MgFeatureService, resourceService: MgResourceService, resourceId: str) -> bool """
        pass

    PostgreSQLProvider = 'PostgreSQL'
    SDFExtension = '.sdf'
    SDFProvider = 'OSGeo.SDF'
    SHPExtension = '.shp'
    SHPProvider = 'OSGeo.SHP'
    SqliteExtension = '.sqlite'
    SqliteProvider = 'OSGeo.SQLite'
    __all__ = [
        'CreateDataStoreAndApplySchema',
        'GetConnectionName',
        'GetFileName',
        'GetProviderName',
        'IsConnected',
        'IsFileBasedConnectionReadOnly',
        'PostgreSQLProvider',
        'SDFExtension',
        'SDFProvider',
        'SHPExtension',
        'SHPProvider',
        'SqliteExtension',
        'SqliteProvider',
    ]


class LayerExtensions(object):
    # no doc
    @staticmethod
    def CreateDataStoreAndApplySchema(featureLayer, fileName, resId, featureSchema):
        """ CreateDataStoreAndApplySchema(featureLayer: AcMapLayer, fileName: str, resId: MgResourceIdentifier, featureSchema: MgFeatureSchema) """
        pass

    @staticmethod
    def CreateMTextForLabels(layer, *__args):
        """ CreateMTextForLabels(layer: AcMapLayer, acadLayerName: str, doLabelsWithinView: bool)CreateMTextForLabels(layer: AcMapLayer, acadLayerId: ObjectId, doLabelsWithinView: bool) """
        pass

    @staticmethod
    def GetLayerDefinitionXML(featureLayer):
        """ GetLayerDefinitionXML(featureLayer: AcMapLayer) -> str """
        pass

    @staticmethod
    def GetOrientationProperties(featureLayer):
        """ GetOrientationProperties(featureLayer: AcMapLayer) -> AcMapLayerOrientationProperties """
        pass

    @staticmethod
    def IsVisibleIn3d(featureLayer):
        """ IsVisibleIn3d(featureLayer: AcMapLayer) -> bool """
        pass

    @staticmethod
    def SetMTextLabel(featureLayer, mtextId, featureId):
        """ SetMTextLabel(featureLayer: AcMapLayer, mtextId: ObjectId, featureId: int) """
        pass

    @staticmethod
    def SetOrientationProperties(featureLayer, props):
        """ SetOrientationProperties(featureLayer: AcMapLayer, props: AcMapLayerOrientationProperties) """
        pass

    @staticmethod
    def SetVisibleIn3d(featureLayer, bVisibleIn3d):
        """ SetVisibleIn3d(featureLayer: AcMapLayer, bVisibleIn3d: bool) """
        pass

    OrientationDirection = None
    OrientationUnitType = None
    __all__ = [
        'CreateDataStoreAndApplySchema',
        'CreateMTextForLabels',
        'GetLayerDefinitionXML',
        'GetOrientationProperties',
        'IsVisibleIn3d',
        'OrientationDirection',
        'OrientationUnitType',
        'SetMTextLabel',
        'SetOrientationProperties',
        'SetVisibleIn3d',
    ]


class LayerGroupExtensions(object):
    # no doc
    __all__ = []


class MapExtensions(object):
    # no doc
    @staticmethod
    def CreateTextLayer(map, featureSourceId, featureSchema, featureClass):
        """ CreateTextLayer(map: AcMapMap, featureSourceId: str, featureSchema: str, featureClass: str) -> ObjectId """
        pass

    @staticmethod
    def GetMetersPerWorldUnit(db):
        """ GetMetersPerWorldUnit(db: Database) -> float """
        pass

    @staticmethod
    def GetTextInfoFromLocation(screenX, screenY):
        """ GetTextInfoFromLocation(screenX: int, screenY: int) -> AcMapLabelInfoCollection """
        pass

    @staticmethod
    def IsDrawOrderHatchOnBottom(map):
        """ IsDrawOrderHatchOnBottom(map: AcMapMap) -> bool """
        pass

    @staticmethod
    def IsDrawOrderTextOnTop(map):
        """ IsDrawOrderTextOnTop(map: AcMapMap) -> bool """
        pass

    @staticmethod
    def SetBackgroundColor(map, backgroundColor):
        """ SetBackgroundColor(map: AcMapMap, backgroundColor: str) """
        pass

    @staticmethod
    def SetDrawOrderHatchOnBottom(map, flag):
        """ SetDrawOrderHatchOnBottom(map: AcMapMap, flag: bool) """
        pass

    @staticmethod
    def SetDrawOrderTextOnTop(map, flag):
        """ SetDrawOrderTextOnTop(map: AcMapMap, flag: bool) """
        pass

    __all__ = [
        'CreateTextLayer',
        'GetMetersPerWorldUnit',
        'GetTextInfoFromLocation',
        'IsDrawOrderHatchOnBottom',
        'IsDrawOrderTextOnTop',
        'SetBackgroundColor',
        'SetDrawOrderHatchOnBottom',
        'SetDrawOrderTextOnTop',
    ]


class PrintLayoutExtensions(object):
    # no doc
    @staticmethod
    def GetDatabase(printLayout):
        """ GetDatabase(printLayout: MgPrintLayoutBase) -> Database """
        pass

    @staticmethod
    def GetLayout(printLayout):
        """ GetLayout(printLayout: MgPrintLayoutBase) -> ObjectId """
        pass

    @staticmethod
    def IsAssociatedWithAMap(viewportId):
        """ IsAssociatedWithAMap(viewportId: ObjectId) -> bool """
        pass

    @staticmethod
    def IsLinkedWithViewport(ple):
        """ IsLinkedWithViewport(ple: MgPrintLayoutElementBase) -> bool """
        pass

    __all__ = [
        'GetDatabase',
        'GetLayout',
        'IsAssociatedWithAMap',
        'IsLinkedWithViewport',
    ]


class ResourceServiceExtensions(object):
    # no doc
    @staticmethod
    def GetAllResources(resourceService, resourceType):
        """ GetAllResources(resourceService: MgResourceService, resourceType: str) -> Dictionary[str, str] """
        pass

    __all__ = [
        'GetAllResources',
    ]


class SchemaEditorOpeningEventArgs(AcMapEventArgs):
    """
    SchemaEditorOpeningEventArgs(cPtr: IntPtr, cMemoryOwn: bool)
    SchemaEditorOpeningEventArgs(featureSourceID: MgResourceIdentifier)
    """
    def Canceled(self):
        """ Canceled(self: SchemaEditorOpeningEventArgs) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: SchemaEditorOpeningEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: SchemaEditorOpeningEventArgs) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: SchemaEditorOpeningEventArgs) -> IntPtr """
        pass

    def GetFeatureSourceId(self):
        """ GetFeatureSourceId(self: SchemaEditorOpeningEventArgs) -> MgResourceIdentifier """
        pass

    def Handled(self):
        """ Handled(self: SchemaEditorOpeningEventArgs) -> bool """
        pass

    def Message(self):
        """ Message(self: SchemaEditorOpeningEventArgs) -> str """
        pass

    def SetCanceled(self, message):
        """ SetCanceled(self: SchemaEditorOpeningEventArgs, message: str) """
        pass

    def SetHandled(self):
        """ SetHandled(self: SchemaEditorOpeningEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, featureSourceID: MgResourceIdentifier)
        """
        pass

    swigCMemOwn = None


class UtilityExtensions(object):
    # no doc
    @staticmethod
    def ConvertMTextToAnnotation(*__args):
        """
        ConvertMTextToAnnotation(idCol: Array[ObjectId]) -> MgBatchPropertyCollection
        ConvertMTextToAnnotation(selSet: SelectionSet) -> MgBatchPropertyCollection
        """
        pass

    FieldNames = None
    __all__ = [
        'ConvertMTextToAnnotation',
        'FieldNames',
    ]


