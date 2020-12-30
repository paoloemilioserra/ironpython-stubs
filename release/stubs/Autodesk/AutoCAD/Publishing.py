# encoding: utf-8
# module Autodesk.AutoCAD.Publishing calls itself Publishing
# from accoremgd, Version=23.1.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AboutToBeginBackgroundPublishingEventArgs(EventArgs):
    # no doc
    def ReadPrivateSection(self, sectionName):
        """ ReadPrivateSection(self: AboutToBeginBackgroundPublishingEventArgs, sectionName: str) -> IDictionaryEnumerator """
        pass

    def WritePrivateSection(self, sectionName, data):
        """ WritePrivateSection(self: AboutToBeginBackgroundPublishingEventArgs, sectionName: str, data: IDictionaryEnumerator) """
        pass

    DsdData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DsdData(self: AboutToBeginBackgroundPublishingEventArgs) -> DsdData

"""

    JobWillPublishInBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobWillPublishInBackground(self: AboutToBeginBackgroundPublishingEventArgs) -> bool

"""



class AboutToBeginBackgroundPublishingEventHandler(MulticastDelegate):
    """ AboutToBeginBackgroundPublishingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: AboutToBeginBackgroundPublishingEventHandler, sender: object, e: AboutToBeginBackgroundPublishingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AboutToBeginBackgroundPublishingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AboutToBeginBackgroundPublishingEventHandler, sender: object, e: AboutToBeginBackgroundPublishingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class AboutToBeginPublishingEventArgs(EventArgs):
    # no doc
    def ReadPrivateSection(self, sectionName):
        """ ReadPrivateSection(self: AboutToBeginPublishingEventArgs, sectionName: str) -> IDictionaryEnumerator """
        pass

    def WritePrivateSection(self, sectionName, data):
        """ WritePrivateSection(self: AboutToBeginPublishingEventArgs, sectionName: str, data: IDictionaryEnumerator) """
        pass

    DsdData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DsdData(self: AboutToBeginPublishingEventArgs) -> DsdData

"""

    JobWillPublishInBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobWillPublishInBackground(self: AboutToBeginPublishingEventArgs) -> bool

"""

    PlotLogger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLogger(self: AboutToBeginPublishingEventArgs) -> PlotLogger

"""



class AboutToBeginPublishingEventHandler(MulticastDelegate):
    """ AboutToBeginPublishingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: AboutToBeginPublishingEventHandler, sender: object, e: AboutToBeginPublishingEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AboutToBeginPublishingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AboutToBeginPublishingEventHandler, sender: object, e: AboutToBeginPublishingEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class AboutToEndPublishingEventHandler(MulticastDelegate):
    """ AboutToEndPublishingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: AboutToEndPublishingEventHandler, sender: object, e: PublishEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AboutToEndPublishingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AboutToEndPublishingEventHandler, sender: object, e: PublishEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class AboutToMoveFileEventHandler(MulticastDelegate):
    """ AboutToMoveFileEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: AboutToMoveFileEventHandler, sender: object, e: PublishEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: AboutToMoveFileEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: AboutToMoveFileEventHandler, sender: object, e: PublishEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginAggregationEventArgs(EventArgs):
    # no doc
    def AddGlobalPropertyRange(self, properties):
        """ AddGlobalPropertyRange(self: BeginAggregationEventArgs, properties: Array[EPlotProperty]) """
        pass

    def AddGlobalResourceRange(self, resources):
        """ AddGlobalResourceRange(self: BeginAggregationEventArgs, resources: Array[EPlotResource]) """
        pass

    DwfFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwfFileName(self: BeginAggregationEventArgs) -> str

"""

    DwfPassword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwfPassword(self: BeginAggregationEventArgs) -> str

"""

    PlotLogger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLogger(self: BeginAggregationEventArgs) -> PlotLogger

"""



class BeginAggregationEventHandler(MulticastDelegate):
    """ BeginAggregationEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginAggregationEventHandler, sender: object, e: BeginAggregationEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginAggregationEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginAggregationEventHandler, sender: object, e: BeginAggregationEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginEntityEventHandler(MulticastDelegate):
    """ BeginEntityEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginEntityEventHandler, sender: object, e: PublishEntityEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginEntityEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginEntityEventHandler, sender: object, e: PublishEntityEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginPublishingSheetEventArgs(EventArgs):
    # no doc
    DsdEntry = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DsdEntry(self: BeginPublishingSheetEventArgs) -> DsdEntry

"""

    PlotLogger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLogger(self: BeginPublishingSheetEventArgs) -> PlotLogger

"""

    UniqueId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueId(self: BeginPublishingSheetEventArgs) -> str

"""



class BeginPublishingSheetEventHandler(MulticastDelegate):
    """ BeginPublishingSheetEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginPublishingSheetEventHandler, sender: object, e: BeginPublishingSheetEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginPublishingSheetEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginPublishingSheetEventHandler, sender: object, e: BeginPublishingSheetEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class BeginSheetEventHandler(MulticastDelegate):
    """ BeginSheetEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: BeginSheetEventHandler, sender: object, e: PublishSheetEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: BeginSheetEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: BeginSheetEventHandler, sender: object, e: PublishSheetEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class CancelledOrFailedPublishingEventHandler(MulticastDelegate):
    """ CancelledOrFailedPublishingEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: CancelledOrFailedPublishingEventHandler, sender: object, e: PublishEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: CancelledOrFailedPublishingEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: CancelledOrFailedPublishingEventHandler, sender: object, e: PublishEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class Dwf3dNavigationTreeNode(RXObject):
    """
    Dwf3dNavigationTreeNode(displayName: str, isGroup: bool, isBlock: bool)
    Dwf3dNavigationTreeNode()
    """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetKeys(self):
        """ GetKeys(self: Dwf3dNavigationTreeNode) -> Array[int] """
        pass

    def SetKeys(self, keys):
        """ SetKeys(self: Dwf3dNavigationTreeNode, keys: Array[int]) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, displayName=None, isGroup=None, isBlock=None):
        """
        __new__(cls: type, displayName: str, isGroup: bool, isBlock: bool)
        __new__(cls: type)
        """
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Children(self: Dwf3dNavigationTreeNode) -> Dwf3dNavigationTreeNodeCollection

"""

    DisplayName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayName(self: Dwf3dNavigationTreeNode) -> str

Set: DisplayName(self: Dwf3dNavigationTreeNode) = value
"""

    IsBlock = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsBlock(self: Dwf3dNavigationTreeNode) -> bool

Set: IsBlock(self: Dwf3dNavigationTreeNode) = value
"""

    IsGroup = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsGroup(self: Dwf3dNavigationTreeNode) -> bool

Set: IsGroup(self: Dwf3dNavigationTreeNode) = value
"""



class Dwf3dNavigationTreeNodeCollection(object):
    # no doc
    def Add(self, node):
        """ Add(self: Dwf3dNavigationTreeNodeCollection, node: Dwf3dNavigationTreeNode) """
        pass

    def Remove(self, node):
        """ Remove(self: Dwf3dNavigationTreeNodeCollection, node: Dwf3dNavigationTreeNode) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: Dwf3dNavigationTreeNodeCollection) -> int

"""



class DwfNode(object):
    """
    DwfNode(nodeId: int, nodeName: str)
    DwfNode()
    """
    @staticmethod # known case of __new__
    def __new__(self, nodeId=None, nodeName=None):
        """
        __new__(cls: type, nodeId: int, nodeName: str)
        __new__(cls: type)
        """
        pass

    NodeId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeId(self: DwfNode) -> int

Set: NodeId(self: DwfNode) = value
"""

    NodeName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NodeName(self: DwfNode) -> str

Set: NodeName(self: DwfNode) = value
"""



class EndEntityEventHandler(MulticastDelegate):
    """ EndEntityEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: EndEntityEventHandler, sender: object, e: PublishEntityEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EndEntityEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: EndEntityEventHandler, sender: object, e: PublishEntityEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class EndPublishEventHandler(MulticastDelegate):
    """ EndPublishEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: EndPublishEventHandler, sender: object, e: PublishEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EndPublishEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: EndPublishEventHandler, sender: object, e: PublishEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class EndSheetEventHandler(MulticastDelegate):
    """ EndSheetEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: EndSheetEventHandler, sender: object, e: PublishSheetEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: EndSheetEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: EndSheetEventHandler, sender: object, e: PublishSheetEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class EPlotAttribute(object):
    """
    EPlotAttribute(ns: str, nsUrl: str, name: str, value: str)
    EPlotAttribute()
    """
    @staticmethod # known case of __new__
    def __new__(self, ns=None, nsUrl=None, name=None, value=None):
        """
        __new__(cls: type, ns: str, nsUrl: str, name: str, value: str)
        __new__(cls: type)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EPlotAttribute) -> str

Set: Name(self: EPlotAttribute) = value
"""

    Ns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ns(self: EPlotAttribute) -> str

Set: Ns(self: EPlotAttribute) = value
"""

    NsUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NsUrl(self: EPlotAttribute) -> str

Set: NsUrl(self: EPlotAttribute) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: EPlotAttribute) -> str

Set: Value(self: EPlotAttribute) = value
"""



class EPlotAttributeCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: EPlotAttributeCollection, value: EPlotAttribute) """
        pass

    def Clear(self):
        """ Clear(self: EPlotAttributeCollection) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: EPlotAttributeCollection, array: Array, index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: EPlotAttributeCollection) -> IEnumerator """
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
    """Get: Count(self: EPlotAttributeCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: EPlotAttributeCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: EPlotAttributeCollection) -> object

"""



class EPlotProperty(object):
    """
    EPlotProperty(name: str, val: str)
    EPlotProperty()
    """
    def AddEPlotAttribute(self, ns, nsUrl, attName, attValue):
        """ AddEPlotAttribute(self: EPlotProperty, ns: str, nsUrl: str, attName: str, attValue: str) """
        pass

    def AddEplotAttribute(self, att):
        """ AddEplotAttribute(self: EPlotProperty, att: EPlotAttribute) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, name=None, val=None):
        """
        __new__(cls: type, name: str, val: str)
        __new__(cls: type)
        """
        pass

    Attributes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Attributes(self: EPlotProperty) -> EPlotAttributeCollection

"""

    Category = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Category(self: EPlotProperty) -> str

Set: Category(self: EPlotProperty) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: EPlotProperty) -> str

Set: Name(self: EPlotProperty) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: EPlotProperty) -> str

Set: Type(self: EPlotProperty) = value
"""

    Units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Units(self: EPlotProperty) -> str

Set: Units(self: EPlotProperty) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: EPlotProperty) -> str

Set: Value(self: EPlotProperty) = value
"""



class EPlotPropertyBag(object):
    """
    EPlotPropertyBag(id: str, namespaceUrl: str, namespaceLocation: str)
    EPlotPropertyBag()
    """
    @staticmethod # known case of __new__
    def __new__(self, id=None, namespaceUrl=None, namespaceLocation=None):
        """
        __new__(cls: type, id: str, namespaceUrl: str, namespaceLocation: str)
        __new__(cls: type)
        """
        pass

    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Id(self: EPlotPropertyBag) -> str

Set: Id(self: EPlotPropertyBag) = value
"""

    NamespaceLocation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamespaceLocation(self: EPlotPropertyBag) -> str

Set: NamespaceLocation(self: EPlotPropertyBag) = value
"""

    NamespaceUrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NamespaceUrl(self: EPlotPropertyBag) -> str

Set: NamespaceUrl(self: EPlotPropertyBag) = value
"""

    Properties = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Properties(self: EPlotPropertyBag) -> EPlotPropertyCollection

"""

    References = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: References(self: EPlotPropertyBag) -> StringCollection

Set: References(self: EPlotPropertyBag) = value
"""



class EPlotPropertyCollection(object):
    # no doc
    def Add(self, value):
        """ Add(self: EPlotPropertyCollection, value: EPlotProperty) """
        pass

    def Clear(self):
        """ Clear(self: EPlotPropertyCollection) """
        pass

    def CopyTo(self, array, index):
        """ CopyTo(self: EPlotPropertyCollection, array: Array, index: int) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: EPlotPropertyCollection) -> IEnumerator """
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
    """Get: Count(self: EPlotPropertyCollection) -> int

"""

    IsSynchronized = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSynchronized(self: EPlotPropertyCollection) -> bool

"""

    SyncRoot = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SyncRoot(self: EPlotPropertyCollection) -> object

"""



class EPlotResource(object):
    """
    EPlotResource(role: str, mime: str, path: str)
    EPlotResource()
    """
    @staticmethod # known case of __new__
    def __new__(self, role=None, mime=None, path=None):
        """
        __new__(cls: type, role: str, mime: str, path: str)
        __new__(cls: type)
        """
        pass

    Mime = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mime(self: EPlotResource) -> str

Set: Mime(self: EPlotResource) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: EPlotResource) -> str

Set: Path(self: EPlotResource) = value
"""

    Role = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Role(self: EPlotResource) -> str

Set: Role(self: EPlotResource) = value
"""



class InitPublishOptionsDialogEventHandler(MulticastDelegate):
    """ InitPublishOptionsDialogEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: InitPublishOptionsDialogEventHandler, sender: object, e: PublishUIEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InitPublishOptionsDialogEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: InitPublishOptionsDialogEventHandler, sender: object, e: PublishUIEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OptionsDialogResult(object):
    # no doc
    DsdData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DsdData(self: OptionsDialogResult) -> DsdData

"""

    PlotConfig = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotConfig(self: OptionsDialogResult) -> PlotConfig

"""

    Status = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Status(self: OptionsDialogResult) -> Nullable[bool]

"""



class PublishEntityEventArgs(EventArgs):
    # no doc
    def Add3DDwfProperty(self, category, name, value):
        """ Add3DDwfProperty(self: PublishEntityEventArgs, category: str, name: str, value: str) -> bool """
        pass

    def AddNodeToMap(self, entityId, objIds, nodeId):
        """ AddNodeToMap(self: PublishEntityEventArgs, entityId: ObjectId, objIds: ObjectIdCollection, nodeId: int) -> bool """
        pass

    def AddPropertiesIds(self, properties, node):
        """ AddPropertiesIds(self: PublishEntityEventArgs, properties: EPlotPropertyBag, node: DwfNode) -> bool """
        pass

    def AddPropertyBag(self, properties):
        """ AddPropertyBag(self: PublishEntityEventArgs, properties: EPlotPropertyBag) -> bool """
        pass

    def Cancel(self):
        """ Cancel(self: PublishEntityEventArgs) """
        pass

    def Flush(self):
        """ Flush(self: PublishEntityEventArgs) """
        pass

    def GetCurrentEntityNode(self, objIds):
        """ GetCurrentEntityNode(self: PublishEntityEventArgs, objIds: ObjectIdCollection) -> DwfNode """
        pass

    def getEntityBlockRefPath(self):
        """ getEntityBlockRefPath(self: PublishEntityEventArgs) -> ObjectIdCollection """
        pass

    def GetEntityNode(self, entityId, objIds):
        """ GetEntityNode(self: PublishEntityEventArgs, entityId: ObjectId, objIds: ObjectIdCollection) -> int """
        pass

    def GetGraphicIDs(self):
        """ GetGraphicIDs(self: PublishEntityEventArgs) -> Array[int] """
        pass

    def GetNextAvailableNode(self):
        """ GetNextAvailableNode(self: PublishEntityEventArgs) -> int """
        pass

    def GetNode(self, nodeId):
        """ GetNode(self: PublishEntityEventArgs, nodeId: int) -> DwfNode """
        pass

    def SetCurrentNode(self, nodeId, objIds):
        """ SetCurrentNode(self: PublishEntityEventArgs, nodeId: int, objIds: ObjectIdCollection) -> bool """
        pass

    def SetNodeName(self, nodeId, nodeName):
        """ SetNodeName(self: PublishEntityEventArgs, nodeId: int, nodeName: str) -> bool """
        pass

    EffectiveBlockLayerId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectiveBlockLayerId(self: PublishEntityEventArgs) -> ObjectId

"""

    Entity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Entity(self: PublishEntityEventArgs) -> Entity

"""

    IsCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCancelled(self: PublishEntityEventArgs) -> bool

"""

    PlotLogger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLogger(self: PublishEntityEventArgs) -> PlotLogger

"""

    UniqueEntityId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueEntityId(self: PublishEntityEventArgs) -> str

"""



class Publisher(MarshalByRefObject):
    # no doc
    def FireAboutToBeginBackgroundPublishing(self, e):
        """ FireAboutToBeginBackgroundPublishing(self: Publisher, e: AboutToBeginBackgroundPublishingEventArgs) """
        pass

    def FireAboutToBeginPublishing(self, e):
        """ FireAboutToBeginPublishing(self: Publisher, e: AboutToBeginPublishingEventArgs) """
        pass

    def FireAboutToEndPublishing(self, e):
        """ FireAboutToEndPublishing(self: Publisher, e: PublishEventArgs) """
        pass

    def FireAboutToMoveFile(self, e):
        """ FireAboutToMoveFile(self: Publisher, e: PublishEventArgs) """
        pass

    def FireBeginAggregation(self, e):
        """ FireBeginAggregation(self: Publisher, e: BeginAggregationEventArgs) """
        pass

    def FireBeginEntity(self, e):
        """ FireBeginEntity(self: Publisher, e: PublishEntityEventArgs) """
        pass

    def FireBeginPublishingSheet(self, e):
        """ FireBeginPublishingSheet(self: Publisher, e: BeginPublishingSheetEventArgs) """
        pass

    def FireBeginSheet(self, e):
        """ FireBeginSheet(self: Publisher, e: PublishSheetEventArgs) """
        pass

    def FireCancelledOrFailedPublishing(self, e):
        """ FireCancelledOrFailedPublishing(self: Publisher, e: PublishEventArgs) """
        pass

    def FireEndEntity(self, e):
        """ FireEndEntity(self: Publisher, e: PublishEntityEventArgs) """
        pass

    def FireEndPublish(self, e):
        """ FireEndPublish(self: Publisher, e: PublishEventArgs) """
        pass

    def FireEndSheet(self, e):
        """ FireEndSheet(self: Publisher, e: PublishSheetEventArgs) """
        pass

    def FireInitPublishOptionsDialog(self, e):
        """ FireInitPublishOptionsDialog(self: Publisher, e: PublishUIEventArgs) """
        pass

    def PublishDsd(self, dsdFile, plotProgressDialog):
        """ PublishDsd(self: Publisher, dsdFile: str, plotProgressDialog: PlotProgressDialog) -> int """
        pass

    def PublishExecute(self, dsdData, plotConfig):
        """ PublishExecute(self: Publisher, dsdData: DsdData, plotConfig: PlotConfig) """
        pass

    def PublishSelectedLayouts(self, bOverride):
        """ PublishSelectedLayouts(self: Publisher, bOverride: bool) """
        pass

    def ShowDwfOptionsDialog(self, dsdData, plotConfig, optionsDialogTitle):
        """ ShowDwfOptionsDialog(self: Publisher, dsdData: DsdData, plotConfig: PlotConfig, optionsDialogTitle: str) -> OptionsDialogResult """
        pass

    def ShowPublishDialog(self, dsdData, plotConfig, namePageSetups, namePageSetupPaths, optionsDialogTitle, optionsButtonText):
        """ ShowPublishDialog(self: Publisher, dsdData: DsdData, plotConfig: PlotConfig, namePageSetups: StringCollection, namePageSetupPaths: StringCollection, optionsDialogTitle: str, optionsButtonText: str) """
        pass

    CurrentPublishedSheetSetPath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPublishedSheetSetPath(self: Publisher) -> str

"""


    AboutToBeginBackgroundPublishing = None
    AboutToBeginPublishing = None
    AboutToEndPublishing = None
    AboutToMoveFile = None
    BeginAggregation = None
    BeginEntity = None
    BeginPublishingSheet = None
    BeginSheet = None
    CancelledOrFailedPublishing = None
    EndEntity = None
    EndPublish = None
    EndSheet = None
    InitPublishOptionsDialog = None


class PublishEventArgs(EventArgs):
    # no doc
    DwfFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwfFileName(self: PublishEventArgs) -> str

"""

    DwfPassword = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DwfPassword(self: PublishEventArgs) -> str

"""

    IsMultiSheetDwf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsMultiSheetDwf(self: PublishEventArgs) -> bool

"""

    TemporaryDwfFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TemporaryDwfFileName(self: PublishEventArgs) -> str

"""



class PublishSheetEventArgs(EventArgs):
    # no doc
    def AddPagePropertyRange(self, properties):
        """ AddPagePropertyRange(self: PublishSheetEventArgs, properties: Array[EPlotProperty]) """
        pass

    def AddPageResourceRange(self, resources):
        """ AddPageResourceRange(self: PublishSheetEventArgs, resources: Array[EPlotResource]) """
        pass

    AreLinesHidden = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreLinesHidden(self: PublishSheetEventArgs) -> bool

"""

    ArePlottingLineWeights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ArePlottingLineWeights(self: PublishSheetEventArgs) -> bool

"""

    AreScalingLineWeights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AreScalingLineWeights(self: PublishSheetEventArgs) -> bool

"""

    CanonicalMediaName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanonicalMediaName(self: PublishSheetEventArgs) -> str

"""

    Configuration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Configuration(self: PublishSheetEventArgs) -> str

"""

    Database = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Database(self: PublishSheetEventArgs) -> Database

"""

    DisplayMaxX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayMaxX(self: PublishSheetEventArgs) -> float

"""

    DisplayMaxY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayMaxY(self: PublishSheetEventArgs) -> float

"""

    DisplayMinX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayMinX(self: PublishSheetEventArgs) -> float

"""

    DisplayMinY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayMinY(self: PublishSheetEventArgs) -> float

"""

    DrawingScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DrawingScale(self: PublishSheetEventArgs) -> float

"""

    Dwf3dNavigationTreeNode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dwf3dNavigationTreeNode(self: PublishSheetEventArgs) -> Dwf3dNavigationTreeNode

Set: Dwf3dNavigationTreeNode(self: PublishSheetEventArgs) = value
"""

    EffectivePlotOffsetX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectivePlotOffsetX(self: PublishSheetEventArgs) -> float

"""

    EffectivePlotOffsetXDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectivePlotOffsetXDevice(self: PublishSheetEventArgs) -> int

"""

    EffectivePlotOffsetY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectivePlotOffsetY(self: PublishSheetEventArgs) -> float

"""

    EffectivePlotOffsetYDevice = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EffectivePlotOffsetYDevice(self: PublishSheetEventArgs) -> int

"""

    IsModelLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsModelLayout(self: PublishSheetEventArgs) -> bool

"""

    IsPlotJobCancelled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsPlotJobCancelled(self: PublishSheetEventArgs) -> bool

"""

    IsScaleSpecified = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsScaleSpecified(self: PublishSheetEventArgs) -> bool

"""

    LayoutBoundsMaxX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutBoundsMaxX(self: PublishSheetEventArgs) -> float

"""

    LayoutBoundsMaxY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutBoundsMaxY(self: PublishSheetEventArgs) -> float

"""

    LayoutBoundsMinX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutBoundsMinX(self: PublishSheetEventArgs) -> float

"""

    LayoutBoundsMinY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutBoundsMinY(self: PublishSheetEventArgs) -> float

"""

    LayoutMarginMaxX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutMarginMaxX(self: PublishSheetEventArgs) -> float

"""

    LayoutMarginMaxY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutMarginMaxY(self: PublishSheetEventArgs) -> float

"""

    LayoutMarginMinX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutMarginMinX(self: PublishSheetEventArgs) -> float

"""

    LayoutMarginMinY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayoutMarginMinY(self: PublishSheetEventArgs) -> float

"""

    MaxBoundsX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxBoundsX(self: PublishSheetEventArgs) -> float

"""

    MaxBoundsY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxBoundsY(self: PublishSheetEventArgs) -> float

"""

    OriginX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginX(self: PublishSheetEventArgs) -> float

"""

    OriginY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginY(self: PublishSheetEventArgs) -> float

"""

    PaperScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PaperScale(self: PublishSheetEventArgs) -> float

"""

    PlotBoundsMaxX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotBoundsMaxX(self: PublishSheetEventArgs) -> float

"""

    PlotBoundsMaxY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotBoundsMaxY(self: PublishSheetEventArgs) -> float

"""

    PlotBoundsMinX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotBoundsMinX(self: PublishSheetEventArgs) -> float

"""

    PlotBoundsMinY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotBoundsMinY(self: PublishSheetEventArgs) -> float

"""

    PlotLayoutId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLayoutId(self: PublishSheetEventArgs) -> ObjectId

"""

    PlotLogger = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotLogger(self: PublishSheetEventArgs) -> PlotLogger

"""

    PlotPaperUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotPaperUnit(self: PublishSheetEventArgs) -> PlotPaperUnit

"""

    PlotRotation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotRotation(self: PublishSheetEventArgs) -> PlotRotation

"""

    PlotToFileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotToFileName(self: PublishSheetEventArgs) -> str

"""

    PlotToFilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotToFilePath(self: PublishSheetEventArgs) -> str

"""

    PlotType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotType(self: PublishSheetEventArgs) -> PlotType

"""

    PlotWindowMaxX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWindowMaxX(self: PublishSheetEventArgs) -> float

"""

    PlotWindowMaxY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWindowMaxY(self: PublishSheetEventArgs) -> float

"""

    PlotWindowMinX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWindowMinX(self: PublishSheetEventArgs) -> float

"""

    PlotWindowMinY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PlotWindowMinY(self: PublishSheetEventArgs) -> float

"""

    PrintableBoundsX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintableBoundsX(self: PublishSheetEventArgs) -> float

"""

    PrintableBoundsY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PrintableBoundsY(self: PublishSheetEventArgs) -> float

"""

    PublishingTo3DDwf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PublishingTo3DDwf(self: PublishSheetEventArgs) -> bool

"""

    StepsPerInch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StepsPerInch(self: PublishSheetEventArgs) -> float

"""

    UniqueLayoutId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UniqueLayoutId(self: PublishSheetEventArgs) -> str

"""

    ViewPlotted = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewPlotted(self: PublishSheetEventArgs) -> str

"""



class PublishUIEventArgs(EventArgs):
    # no doc
    def ReadPrivateSection(self, sectionName):
        """ ReadPrivateSection(self: PublishUIEventArgs, sectionName: str) -> IDictionaryEnumerator """
        pass

    def WritePrivateSection(self, sectionName, data):
        """ WritePrivateSection(self: PublishUIEventArgs, sectionName: str, data: IDictionaryEnumerator) """
        pass

    DsdData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DsdData(self: PublishUIEventArgs) -> DsdData

"""

    IUnknown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IUnknown(self: PublishUIEventArgs) -> IUnknown**

"""

    JobWillPublishInBackground = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: JobWillPublishInBackground(self: PublishUIEventArgs) -> bool

"""



