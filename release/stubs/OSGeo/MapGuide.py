# encoding: utf-8
# module OSGeo.MapGuide calls itself MapGuide
# from Autodesk.Map.Platform, Version=24.0.30.14, Culture=neutral, PublicKeyToken=null, OSGeo.MapGuide.Foundation, Version=3.4.72.0, Culture=neutral, PublicKeyToken=null, OSGeo.MapGuide.Geometry, Version=3.4.72.0, Culture=neutral, PublicKeyToken=null, OSGeo.MapGuide.PlatformBase, Version=3.4.72.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcMapFeatureUpdateInfo(object):
    """ AcMapFeatureUpdateInfo(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapFeatureUpdateInfo) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureUpdateInfo) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AcMapNorthArrowUtils(object):
    """ AcMapNorthArrowUtils(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: AcMapNorthArrowUtils) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapNorthArrowUtils) -> IntPtr """
        pass

    @staticmethod
    def GetNorthArrowIsDefaultNorth():
        """ GetNorthArrowIsDefaultNorth() -> bool """
        pass

    @staticmethod
    def SetNorthArrowIsDefaultNorth(isDefaultNorth):
        """ SetNorthArrowIsDefaultNorth(isDefaultNorth: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class FoundationApi(object):
    """ FoundationApi() """

class GeometryApi(object):
    """ GeometryApi() """

class IAcquisitionService(object):
    """ IAcquisitionService(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: IAcquisitionService) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: IAcquisitionService) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class ManagedEventArgs(EventArgs):
    """ ManagedEventArgs() """
    def Dispose(self):
        """ Dispose(self: ManagedEventArgs) """
        pass

    def GetClassId(self):
        """ GetClassId(self: ManagedEventArgs) -> int """
        pass


class ManagedException(Exception):
    """ ManagedException() """
    def Dispose(self):
        """ Dispose(self: ManagedException) """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: ManagedException, info: SerializationInfo, context: StreamingContext) """
        pass

    def ToString(self):
        """ ToString(self: ManagedException) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    Message = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Message(self: ManagedException) -> str

"""

    StackTrace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StackTrace(self: ManagedException) -> str

"""



class MgObject(object):
    """ MgObject(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgObject) """
        pass

    def GetClassId(self):
        """ GetClassId(self: MgObject) -> int """
        pass

    def GetClassName(self):
        """ GetClassName(self: MgObject) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgObject) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgDisposable(MgObject):
    """ MgDisposable(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgDisposable) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDisposable) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgGuardDisposable(MgDisposable):
    """ MgGuardDisposable(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgGuardDisposable) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGuardDisposable) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgAgfReaderWriter(MgGuardDisposable):
    """
    MgAgfReaderWriter(cPtr: IntPtr, cMemoryOwn: bool)
    MgAgfReaderWriter()
    """
    def Dispose(self):
        """ Dispose(self: MgAgfReaderWriter) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgAgfReaderWriter) -> IntPtr """
        pass

    def Read(self, agf, transform=None):
        """
        Read(self: MgAgfReaderWriter, agf: MgByteReader, transform: MgTransform) -> MgGeometry
        Read(self: MgAgfReaderWriter, agf: MgByteReader) -> MgGeometry
        """
        pass

    def Write(self, geometry, transform=None):
        """
        Write(self: MgAgfReaderWriter, geometry: MgGeometry, transform: MgTransform) -> MgByteReader
        Write(self: MgAgfReaderWriter, geometry: MgGeometry) -> MgByteReader
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgSerializable(MgGuardDisposable):
    """ MgSerializable(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgSerializable) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgSerializable) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgGeometricEntity(MgSerializable):
    """ MgGeometricEntity(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgGeometricEntity) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgGeometricEntity) """
        pass

    def Envelope(self):
        """ Envelope(self: MgGeometricEntity) -> MgEnvelope """
        pass

    def GetArea(self):
        """ GetArea(self: MgGeometricEntity) -> float """
        pass

    def GetCentroid(self):
        """ GetCentroid(self: MgGeometricEntity) -> MgPoint """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometricEntity) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgGeometricEntity) -> int """
        pass

    def GetLength(self):
        """ GetLength(self: MgGeometricEntity) -> float """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgGeometricEntity) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgGeometricEntity) -> bool """
        pass

    def IsSimple(self):
        """ IsSimple(self: MgGeometricEntity) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgGeometricEntity) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgGeometricEntity, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Area = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Area(self: MgGeometricEntity) -> float

"""

    Centroid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Centroid(self: MgGeometricEntity) -> MgPoint

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgGeometricEntity) -> int

"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: MgGeometricEntity) -> float

"""


    swigCMemOwn = None


class MgGeometry(MgGeometricEntity):
    """ MgGeometry(cPtr: IntPtr, cMemoryOwn: bool) """
    def Boundary(self):
        """ Boundary(self: MgGeometry) -> MgGeometry """
        pass

    def Buffer(self, distance, measure):
        """ Buffer(self: MgGeometry, distance: float, measure: MgMeasure) -> MgGeometry """
        pass

    def Contains(self, other):
        """ Contains(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    def ConvexHull(self):
        """ ConvexHull(self: MgGeometry) -> MgGeometry """
        pass

    def Crosses(self, other):
        """ Crosses(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    def Difference(self, other):
        """ Difference(self: MgGeometry, other: MgGeometry) -> MgGeometry """
        pass

    def Disjoint(self, other):
        """ Disjoint(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgGeometry) """
        pass

    def Distance(self, other, measure):
        """ Distance(self: MgGeometry, other: MgGeometry, measure: MgMeasure) -> float """
        pass

    def Equals(self, *__args):
        """ Equals(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometry) -> IntPtr """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgGeometry) -> int """
        pass

    def Intersection(self, other):
        """ Intersection(self: MgGeometry, other: MgGeometry) -> MgGeometry """
        pass

    def Intersects(self, other):
        """ Intersects(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    def Overlaps(self, other):
        """ Overlaps(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    def Prepare(self):
        """ Prepare(self: MgGeometry) -> MgPreparedGeometry """
        pass

    def SymetricDifference(self, other):
        """ SymetricDifference(self: MgGeometry, other: MgGeometry) -> MgGeometry """
        pass

    def Tessellate(self):
        """ Tessellate(self: MgGeometry) -> MgGeometry """
        pass

    def Touches(self, other):
        """ Touches(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    def Union(self, other):
        """ Union(self: MgGeometry, other: MgGeometry) -> MgGeometry """
        pass

    def Within(self, other):
        """ Within(self: MgGeometry, other: MgGeometry) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgGeometry) -> int

"""


    swigCMemOwn = None


class MgAggregateGeometry(MgGeometry):
    """ MgAggregateGeometry(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgAggregateGeometry) """
        pass

    def GetCount(self):
        """ GetCount(self: MgAggregateGeometry) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgAggregateGeometry) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgAggregateGeometry) -> int

"""


    swigCMemOwn = None


class MgException(ManagedException):
    """ MgException(cPtr: IntPtr, cMemoryOwn: bool) """
    def AddStackTraceInfo(self, methodName, *__args):
        """ AddStackTraceInfo(self: MgException, methodName: str, methodParams: str, lineNumber: int, fileName: str)AddStackTraceInfo(self: MgException, methodName: str, lineNumber: int, fileName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: MgException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgException) -> IntPtr """
        pass

    def GetDetails(self, locale=None):
        """
        GetDetails(self: MgException, locale: str) -> str
        GetDetails(self: MgException) -> str
        """
        pass

    def GetExceptionMessage(self, locale=None):
        """
        GetExceptionMessage(self: MgException, locale: str) -> str
        GetExceptionMessage(self: MgException) -> str
        """
        pass

    def GetStackTrace(self, locale=None):
        """
        GetStackTrace(self: MgException, locale: str) -> str
        GetStackTrace(self: MgException) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    swigCMemOwn = None


class MgApplicationException(MgException):
    """ MgApplicationException(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgApplicationException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgApplicationException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    swigCMemOwn = None


class MgGeometryComponent(MgGeometricEntity):
    """ MgGeometryComponent(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgGeometryComponent) """
        pass

    def GetComponentType(self):
        """ GetComponentType(self: MgGeometryComponent) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometryComponent) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: MgGeometryComponent) -> int

"""


    swigCMemOwn = None


class MgCurveSegment(MgGeometryComponent):
    """ MgCurveSegment(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCurveSegment) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurveSegment) -> IntPtr """
        pass

    def GetEndCoordinate(self):
        """ GetEndCoordinate(self: MgCurveSegment) -> MgCoordinate """
        pass

    def GetStartCoordinate(self):
        """ GetStartCoordinate(self: MgCurveSegment) -> MgCoordinate """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    EndCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndCoordinate(self: MgCurveSegment) -> MgCoordinate

"""

    StartCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCoordinate(self: MgCurveSegment) -> MgCoordinate

"""


    swigCMemOwn = None


class MgArcSegment(MgCurveSegment):
    """ MgArcSegment(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgArcSegment) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgArcSegment) """
        pass

    def GetComponentType(self):
        """ GetComponentType(self: MgArcSegment) -> int """
        pass

    def GetControlCoordinate(self):
        """ GetControlCoordinate(self: MgArcSegment) -> MgCoordinate """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgArcSegment) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgArcSegment) -> int """
        pass

    def GetEndCoordinate(self):
        """ GetEndCoordinate(self: MgArcSegment) -> MgCoordinate """
        pass

    def GetStartCoordinate(self):
        """ GetStartCoordinate(self: MgArcSegment) -> MgCoordinate """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgArcSegment) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgArcSegment) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgArcSegment, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: MgArcSegment) -> int

"""

    ControlCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlCoordinate(self: MgArcSegment) -> MgCoordinate

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgArcSegment) -> int

"""

    EndCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndCoordinate(self: MgArcSegment) -> MgCoordinate

"""

    StartCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCoordinate(self: MgArcSegment) -> MgCoordinate

"""


    swigCMemOwn = None


class MgSystemException(MgException):
    """ MgSystemException(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgSystemException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgSystemException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    swigCMemOwn = None


class MgOutOfRangeException(MgSystemException):
    """
    MgOutOfRangeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgOutOfRangeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgOutOfRangeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgOutOfRangeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgArgumentOutOfRangeException(MgOutOfRangeException):
    """
    MgArgumentOutOfRangeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgArgumentOutOfRangeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgArgumentOutOfRangeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgArgumentOutOfRangeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgArrayTypeMismatchException(MgSystemException):
    """
    MgArrayTypeMismatchException(cPtr: IntPtr, cMemoryOwn: bool)
    MgArrayTypeMismatchException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgArrayTypeMismatchException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgArrayTypeMismatchException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgAsyncTask(MgDisposable):
    """ MgAsyncTask(cPtr: IntPtr, cMemoryOwn: bool) """
    def Cancel(self):
        """ Cancel(self: MgAsyncTask) """
        pass

    def Dispose(self):
        """ Dispose(self: MgAsyncTask) """
        pass

    def GetClassId(self):
        """ GetClassId(self: MgAsyncTask) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgAsyncTask) -> IntPtr """
        pass

    def IsInProgress(self):
        """ IsInProgress(self: MgAsyncTask) -> bool """
        pass

    def Wait(self):
        """ Wait(self: MgAsyncTask) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCollection(MgSerializable):
    """ MgCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Clear(self):
        """ Clear(self: MgCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCollection) -> IntPtr """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCollection, index: int) """
        pass

    def ToXml(self):
        """ ToXml(self: MgCollection) -> MgByteReader """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgBatchPropertyCollection(MgCollection):
    """
    MgBatchPropertyCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgBatchPropertyCollection()
    """
    def Add(self, value):
        """ Add(self: MgBatchPropertyCollection, value: MgPropertyCollection) """
        pass

    def Clear(self):
        """ Clear(self: MgBatchPropertyCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgBatchPropertyCollection, coll: MgPropertyCollection) -> bool
        Contains(self: MgBatchPropertyCollection, value: MgPropertyDefinition) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgBatchPropertyCollection, array: Array[MgPropertyCollection], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgBatchPropertyCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgBatchPropertyCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgBatchPropertyCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgBatchPropertyCollection) -> IEnumerator[MgPropertyCollection] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgBatchPropertyCollection, index: int) -> MgPropertyCollection """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgBatchPropertyCollection, coll: MgPropertyCollection) -> int
        IndexOf(self: MgBatchPropertyCollection, value: MgPropertyDefinition) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgBatchPropertyCollection, index: int, value: MgPropertyCollection) """
        pass

    def Remove(self, value):
        """ Remove(self: MgBatchPropertyCollection, value: MgPropertyCollection) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgBatchPropertyCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgBatchPropertyCollection, index: int, value: MgPropertyCollection) """
        pass

    def ToXml(self):
        """ ToXml(self: MgBatchPropertyCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgPropertyCollection], item: MgPropertyCollection) -> bool """
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
    """Get: Count(self: MgBatchPropertyCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgBatchPropertyCollection) -> bool

"""


    MgBatchPropertyCollectionEnumerator = None
    swigCMemOwn = None


class MgNamedSerializable(MgSerializable):
    """ MgNamedSerializable(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgNamedSerializable) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNamedSerializable) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgProperty(MgNamedSerializable):
    """ MgProperty(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgProperty) -> IntPtr """
        pass

    def GetName(self):
        """ GetName(self: MgProperty) -> str """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgProperty) -> Int16 """
        pass

    def SetName(self, name):
        """ SetName(self: MgProperty, name: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgProperty) -> str

Set: Name(self: MgProperty) = value
"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgProperty) -> Int16

"""


    swigCMemOwn = None


class MgNullableProperty(MgProperty):
    """ MgNullableProperty(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgNullableProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNullableProperty) -> IntPtr """
        pass

    def IsNull(self):
        """ IsNull(self: MgNullableProperty) -> bool """
        pass

    def SetNull(self, bIsNull):
        """ SetNull(self: MgNullableProperty, bIsNull: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgBlobProperty(MgNullableProperty):
    """
    MgBlobProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgBlobProperty(name: str, value: MgByteReader)
    """
    def Dispose(self):
        """ Dispose(self: MgBlobProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgBlobProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgBlobProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgBlobProperty) -> MgByteReader """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgBlobProperty, value: MgByteReader) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: MgByteReader)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgBlobProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgBlobProperty) -> MgByteReader

Set: Value(self: MgBlobProperty) = value
"""


    swigCMemOwn = None


class MgBooleanProperty(MgNullableProperty):
    """
    MgBooleanProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgBooleanProperty(name: str, value: bool)
    """
    def Dispose(self):
        """ Dispose(self: MgBooleanProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgBooleanProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgBooleanProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgBooleanProperty) -> bool """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgBooleanProperty, value: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: bool)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgBooleanProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgBooleanProperty) -> bool

Set: Value(self: MgBooleanProperty) = value
"""


    swigCMemOwn = None


class MgByteProperty(MgNullableProperty):
    """
    MgByteProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgByteProperty(name: str, value: Byte)
    """
    def Dispose(self):
        """ Dispose(self: MgByteProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgByteProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgByteProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgByteProperty) -> Byte """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgByteProperty, value: Byte) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: Byte)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgByteProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgByteProperty) -> Byte

Set: Value(self: MgByteProperty) = value
"""


    swigCMemOwn = None


class MgByteReader(MgSerializable):
    """
    MgByteReader(cPtr: IntPtr, cMemoryOwn: bool)
    MgByteReader(fileName: str, mimeType: str, removeFile: bool)
    MgByteReader(contents: str, mimeType: str)
    MgByteReader(contents: Array[Byte], length: int, mimeType: str)
    """
    def Dispose(self):
        """ Dispose(self: MgByteReader) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgByteReader) -> IntPtr """
        pass

    def GetLength(self):
        """ GetLength(self: MgByteReader) -> Int64 """
        pass

    def GetMimeType(self):
        """ GetMimeType(self: MgByteReader) -> str """
        pass

    def IsRewindable(self):
        """ IsRewindable(self: MgByteReader) -> bool """
        pass

    def Read(self, buffer, length):
        """ Read(self: MgByteReader, buffer: Array[Byte], length: int) -> int """
        pass

    def Rewind(self):
        """ Rewind(self: MgByteReader) """
        pass

    def ToFile(self, fileName):
        """ ToFile(self: MgByteReader, fileName: str) """
        pass

    def ToString(self):
        """ ToString(self: MgByteReader) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, fileName: str, mimeType: str, removeFile: bool)
        __new__(cls: type, contents: str, mimeType: str)
        __new__(cls: type, contents: Array[Byte], length: int, mimeType: str)
        """
        pass

    MimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MimeType(self: MgByteReader) -> str

"""


    swigCMemOwn = None


class MgByteSink(MgGuardDisposable):
    """
    MgByteSink(cPtr: IntPtr, cMemoryOwn: bool)
    MgByteSink(reader: MgByteReader)
    """
    def Dispose(self):
        """ Dispose(self: MgByteSink) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgByteSink) -> IntPtr """
        pass

    def ToFile(self, filename):
        """ ToFile(self: MgByteSink, filename: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, reader: MgByteReader)
        """
        pass

    swigCMemOwn = None


class MgByteSource(MgGuardDisposable):
    """
    MgByteSource(cPtr: IntPtr, cMemoryOwn: bool)
    MgByteSource(file: str)
    MgByteSource(buffer: Array[Byte], length: int)
    """
    def Dispose(self):
        """ Dispose(self: MgByteSource) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgByteSource) -> IntPtr """
        pass

    def GetMimeType(self):
        """ GetMimeType(self: MgByteSource) -> str """
        pass

    def GetReader(self):
        """ GetReader(self: MgByteSource) -> MgByteReader """
        pass

    def SetMimeType(self, mimeType):
        """ SetMimeType(self: MgByteSource, mimeType: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, file: str)
        __new__(cls: type, buffer: Array[Byte], length: int)
        """
        pass

    MimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MimeType(self: MgByteSource) -> str

Set: MimeType(self: MgByteSource) = value
"""


    swigCMemOwn = None


class MgClassDefinition(MgNamedSerializable):
    """
    MgClassDefinition(cPtr: IntPtr, cMemoryOwn: bool)
    MgClassDefinition()
    """
    def Delete(self):
        """ Delete(self: MgClassDefinition) """
        pass

    def Dispose(self):
        """ Dispose(self: MgClassDefinition) """
        pass

    def GetBaseClassDefinition(self):
        """ GetBaseClassDefinition(self: MgClassDefinition) -> MgClassDefinition """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgClassDefinition) -> IntPtr """
        pass

    def GetDefaultGeometryPropertyName(self):
        """ GetDefaultGeometryPropertyName(self: MgClassDefinition) -> str """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgClassDefinition) -> str """
        pass

    def GetIdentityProperties(self):
        """ GetIdentityProperties(self: MgClassDefinition) -> MgPropertyDefinitionCollection """
        pass

    def GetName(self):
        """ GetName(self: MgClassDefinition) -> str """
        pass

    def GetProperties(self):
        """ GetProperties(self: MgClassDefinition) -> MgPropertyDefinitionCollection """
        pass

    def IsAbstract(self):
        """ IsAbstract(self: MgClassDefinition) -> bool """
        pass

    def IsComputed(self):
        """ IsComputed(self: MgClassDefinition) -> bool """
        pass

    def SetDefaultGeometryPropertyName(self, name):
        """ SetDefaultGeometryPropertyName(self: MgClassDefinition, name: str) """
        pass

    def SetDescription(self, description):
        """ SetDescription(self: MgClassDefinition, description: str) """
        pass

    def SetName(self, name):
        """ SetName(self: MgClassDefinition, name: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    BaseClassDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BaseClassDefinition(self: MgClassDefinition) -> MgClassDefinition

"""

    DefaultGeometryPropertyName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultGeometryPropertyName(self: MgClassDefinition) -> str

Set: DefaultGeometryPropertyName(self: MgClassDefinition) = value
"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgClassDefinition) -> str

Set: Description(self: MgClassDefinition) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgClassDefinition) -> str

Set: Name(self: MgClassDefinition) = value
"""


    swigCMemOwn = None


class MgClassDefinitionCollection(MgCollection):
    """
    MgClassDefinitionCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgClassDefinitionCollection()
    """
    def Add(self, value):
        """ Add(self: MgClassDefinitionCollection, value: MgClassDefinition) """
        pass

    def Clear(self):
        """ Clear(self: MgClassDefinitionCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgClassDefinitionCollection, value: MgClassDefinition) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgClassDefinitionCollection, array: Array[MgClassDefinition], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgClassDefinitionCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgClassDefinitionCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgClassDefinitionCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgClassDefinitionCollection) -> IEnumerator[MgClassDefinition] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgClassDefinitionCollection, index: int) -> MgClassDefinition """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgClassDefinitionCollection, value: MgClassDefinition) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgClassDefinitionCollection, index: int, value: MgClassDefinition) """
        pass

    def Remove(self, value):
        """ Remove(self: MgClassDefinitionCollection, value: MgClassDefinition) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgClassDefinitionCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgClassDefinitionCollection, index: int, value: MgClassDefinition) """
        pass

    def ToXml(self):
        """ ToXml(self: MgClassDefinitionCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgClassDefinition], item: MgClassDefinition) -> bool """
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
    """Get: Count(self: MgClassDefinitionCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgClassDefinitionCollection) -> bool

"""


    MgClassDefinitionCollectionEnumerator = None
    swigCMemOwn = None


class MgClassNotFoundException(MgSystemException):
    """
    MgClassNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgClassNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgClassNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgClassNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgClobProperty(MgNullableProperty):
    """
    MgClobProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgClobProperty(name: str, value: MgByteReader)
    """
    def Dispose(self):
        """ Dispose(self: MgClobProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgClobProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgClobProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgClobProperty) -> MgByteReader """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgClobProperty, value: MgByteReader) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: MgByteReader)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgClobProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgClobProperty) -> MgByteReader

Set: Value(self: MgClobProperty) = value
"""


    swigCMemOwn = None


class MgColor(MgSerializable):
    """
    MgColor(cPtr: IntPtr, cMemoryOwn: bool)
    MgColor(color: str)
    MgColor(red: Int16, green: Int16, blue: Int16)
    MgColor(red: Int16, green: Int16, blue: Int16, alpha: Int16)
    MgColor(color: Color)
    """
    def Dispose(self):
        """ Dispose(self: MgColor) """
        pass

    def GetAlpha(self):
        """ GetAlpha(self: MgColor) -> Int16 """
        pass

    def GetBlue(self):
        """ GetBlue(self: MgColor) -> Int16 """
        pass

    def GetColor(self):
        """ GetColor(self: MgColor) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgColor) -> IntPtr """
        pass

    def GetGreen(self):
        """ GetGreen(self: MgColor) -> Int16 """
        pass

    def GetRed(self):
        """ GetRed(self: MgColor) -> Int16 """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, color: str)
        __new__(cls: type, red: Int16, green: Int16, blue: Int16)
        __new__(cls: type, red: Int16, green: Int16, blue: Int16, alpha: Int16)
        __new__(cls: type, color: Color)
        """
        pass

    Alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Alpha(self: MgColor) -> Int16

"""

    Blue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Blue(self: MgColor) -> Int16

"""

    Color = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Color(self: MgColor) -> str

"""

    Green = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Green(self: MgColor) -> Int16

"""

    Red = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Red(self: MgColor) -> Int16

"""


    swigCMemOwn = None


class MgConfigurationException(MgApplicationException):
    """
    MgConfigurationException(cPtr: IntPtr, cMemoryOwn: bool)
    MgConfigurationException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgConfigurationException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgConfigurationException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgConfigurationLoadFailedException(MgApplicationException):
    """
    MgConfigurationLoadFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgConfigurationLoadFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgConfigurationLoadFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgConfigurationLoadFailedException) -> IntPtr """
        pass

    def GetExceptionMessage(self, locale=None):
        """ GetExceptionMessage(self: MgConfigurationLoadFailedException, locale: str) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgConfigurationSaveFailedException(MgApplicationException):
    """
    MgConfigurationSaveFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgConfigurationSaveFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgConfigurationSaveFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgConfigurationSaveFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgCoordinate(MgSerializable):
    """ MgCoordinate(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinate) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinate) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCoordinate) -> int """
        pass

    def GetM(self):
        """ GetM(self: MgCoordinate) -> float """
        pass

    def GetX(self):
        """ GetX(self: MgCoordinate) -> float """
        pass

    def GetY(self):
        """ GetY(self: MgCoordinate) -> float """
        pass

    def GetZ(self):
        """ GetZ(self: MgCoordinate) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCoordinate) -> int

"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: MgCoordinate) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: MgCoordinate) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: MgCoordinate) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: MgCoordinate) -> float

"""


    NoM = nan
    NoZ = nan
    swigCMemOwn = None


class MgCoordinateCollection(MgGuardDisposable):
    """
    MgCoordinateCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateCollection()
    """
    def Add(self, value):
        """ Add(self: MgCoordinateCollection, value: MgCoordinate) """
        pass

    def Clear(self):
        """ Clear(self: MgCoordinateCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgCoordinateCollection, value: MgCoordinate) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgCoordinateCollection, array: Array[MgCoordinate], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCoordinateCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgCoordinateCollection) -> IEnumerator[MgCoordinate] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCoordinateCollection, index: int) -> MgCoordinate """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgCoordinateCollection, value: MgCoordinate) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgCoordinateCollection, index: int, value: MgCoordinate) """
        pass

    def Remove(self, value):
        """ Remove(self: MgCoordinateCollection, value: MgCoordinate) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCoordinateCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgCoordinateCollection, index: int, value: MgCoordinate) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgCoordinate], item: MgCoordinate) -> bool """
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
    """Get: Count(self: MgCoordinateCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgCoordinateCollection) -> bool

"""


    MgCoordinateCollectionEnumerator = None
    swigCMemOwn = None


class MgCoordinateDimension(object):
    """ MgCoordinateDimension() """
    M = 2
    XY = 0
    XYZ = 1


class MgCoordinateIterator(MgGuardDisposable):
    """ MgCoordinateIterator(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateIterator) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateIterator) -> IntPtr """
        pass

    def GetCurrent(self):
        """ GetCurrent(self: MgCoordinateIterator) -> MgCoordinate """
        pass

    def MoveNext(self):
        """ MoveNext(self: MgCoordinateIterator) -> bool """
        pass

    def Reset(self):
        """ Reset(self: MgCoordinateIterator) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystem(MgGuardDisposable):
    """ MgCoordinateSystem(cPtr: IntPtr, cMemoryOwn: bool) """
    def CancelLonLatBounds(self):
        """ CancelLonLatBounds(self: MgCoordinateSystem) """
        pass

    def CancelXYBounds(self):
        """ CancelXYBounds(self: MgCoordinateSystem) """
        pass

    def ConvertCoordinateFromLonLat(self, lonLatToCoordinate):
        """ ConvertCoordinateFromLonLat(self: MgCoordinateSystem, lonLatToCoordinate: MgCoordinate) """
        pass

    def ConvertCoordinateSystemUnitsToMeters(self, units):
        """ ConvertCoordinateSystemUnitsToMeters(self: MgCoordinateSystem, units: float) -> float """
        pass

    def ConvertCoordinateToLonLat(self, coordinateToLonLat):
        """ ConvertCoordinateToLonLat(self: MgCoordinateSystem, coordinateToLonLat: MgCoordinate) """
        pass

    def ConvertFromLonLat(self, *__args):
        """
        ConvertFromLonLat(self: MgCoordinateSystem, dLongitude: float, dLatitude: float, dZ: float) -> MgCoordinate
        ConvertFromLonLat(self: MgCoordinateSystem, dLongitude: float, dLatitude: float) -> MgCoordinate
        ConvertFromLonLat(self: MgCoordinateSystem, lonLat: MgCoordinate) -> MgCoordinate
        """
        pass

    def ConvertMetersToCoordinateSystemUnits(self, meters):
        """ ConvertMetersToCoordinateSystemUnits(self: MgCoordinateSystem, meters: float) -> float """
        pass

    def ConvertToLonLat(self, *__args):
        """
        ConvertToLonLat(self: MgCoordinateSystem, dX: float, dY: float, dZ: float) -> MgCoordinate
        ConvertToLonLat(self: MgCoordinateSystem, dX: float, dY: float) -> MgCoordinate
        ConvertToLonLat(self: MgCoordinateSystem, coordinate: MgCoordinate) -> MgCoordinate
        """
        pass

    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystem) -> MgCoordinateSystem """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystem) """
        pass

    def GetAge(self):
        """ GetAge(self: MgCoordinateSystem) -> Int16 """
        pass

    def GetAzimuth(self, *__args):
        """
        GetAzimuth(self: MgCoordinateSystem, x1: float, y1: float, x2: float, y2: float) -> float
        GetAzimuth(self: MgCoordinateSystem, coord1: MgCoordinate, coord2: MgCoordinate) -> float
        """
        pass

    def GetCatalog(self):
        """ GetCatalog(self: MgCoordinateSystem) -> MgCoordinateSystemCatalog """
        pass

    def GetCategories(self):
        """ GetCategories(self: MgCoordinateSystem) -> MgStringCollection """
        pass

    def GetConvergence(self, dLongitude, dLatitude):
        """ GetConvergence(self: MgCoordinateSystem, dLongitude: float, dLatitude: float) -> float """
        pass

    def GetCoordinate(self, *__args):
        """
        GetCoordinate(self: MgCoordinateSystem, xStart: float, yStart: float, azimuth: float, distance: float) -> MgCoordinate
        GetCoordinate(self: MgCoordinateSystem, coord: MgCoordinate, azimuth: float, distance: float) -> MgCoordinate
        """
        pass

    def GetCountryOrState(self):
        """ GetCountryOrState(self: MgCoordinateSystem) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystem) -> IntPtr """
        pass

    def GetCsCode(self):
        """ GetCsCode(self: MgCoordinateSystem) -> str """
        pass

    def GetDatum(self):
        """ GetDatum(self: MgCoordinateSystem) -> str """
        pass

    def GetDatumDefinition(self):
        """ GetDatumDefinition(self: MgCoordinateSystem) -> MgCoordinateSystemDatum """
        pass

    def GetDatumDescription(self):
        """ GetDatumDescription(self: MgCoordinateSystem) -> str """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgCoordinateSystem) -> str """
        pass

    def GetEllipsoid(self):
        """ GetEllipsoid(self: MgCoordinateSystem) -> str """
        pass

    def GetEllipsoidDefinition(self):
        """ GetEllipsoidDefinition(self: MgCoordinateSystem) -> MgCoordinateSystemEllipsoid """
        pass

    def GetEllipsoidDescription(self):
        """ GetEllipsoidDescription(self: MgCoordinateSystem) -> str """
        pass

    def GetEpsgCode(self):
        """ GetEpsgCode(self: MgCoordinateSystem) -> int """
        pass

    def GetEpsgQuadrant(self):
        """ GetEpsgQuadrant(self: MgCoordinateSystem) -> Int16 """
        pass

    def GetErrors(self):
        """ GetErrors(self: MgCoordinateSystem) -> MgCoordinateSystemEnumInteger32 """
        pass

    def GetGroup(self):
        """ GetGroup(self: MgCoordinateSystem) -> str """
        pass

    def GetLatMax(self):
        """ GetLatMax(self: MgCoordinateSystem) -> float """
        pass

    def GetLatMin(self):
        """ GetLatMin(self: MgCoordinateSystem) -> float """
        pass

    def GetLocation(self):
        """ GetLocation(self: MgCoordinateSystem) -> str """
        pass

    def GetLonMax(self):
        """ GetLonMax(self: MgCoordinateSystem) -> float """
        pass

    def GetLonMin(self):
        """ GetLonMin(self: MgCoordinateSystem) -> float """
        pass

    def GetMapScale(self):
        """ GetMapScale(self: MgCoordinateSystem) -> float """
        pass

    def GetMaxX(self):
        """ GetMaxX(self: MgCoordinateSystem) -> float """
        pass

    def GetMaxY(self):
        """ GetMaxY(self: MgCoordinateSystem) -> float """
        pass

    def GetMeasure(self):
        """ GetMeasure(self: MgCoordinateSystem) -> MgCoordinateSystemMeasure """
        pass

    def GetMinX(self):
        """ GetMinX(self: MgCoordinateSystem) -> float """
        pass

    def GetMinY(self):
        """ GetMinY(self: MgCoordinateSystem) -> float """
        pass

    def GetOffsetX(self):
        """ GetOffsetX(self: MgCoordinateSystem) -> float """
        pass

    def GetOffsetY(self):
        """ GetOffsetY(self: MgCoordinateSystem) -> float """
        pass

    def GetOriginLatitude(self):
        """ GetOriginLatitude(self: MgCoordinateSystem) -> float """
        pass

    def GetOriginLongitude(self):
        """ GetOriginLongitude(self: MgCoordinateSystem) -> float """
        pass

    def GetProjection(self):
        """ GetProjection(self: MgCoordinateSystem) -> str """
        pass

    def GetProjectionCode(self):
        """ GetProjectionCode(self: MgCoordinateSystem) -> int """
        pass

    def GetProjectionDescription(self):
        """ GetProjectionDescription(self: MgCoordinateSystem) -> str """
        pass

    def GetProjectionParameter(self, nIndex):
        """ GetProjectionParameter(self: MgCoordinateSystem, nIndex: int) -> float """
        pass

    def GetProjectionParameterCount(self):
        """ GetProjectionParameterCount(self: MgCoordinateSystem) -> int """
        pass

    def GetQuadrant(self):
        """ GetQuadrant(self: MgCoordinateSystem) -> Int16 """
        pass

    def GetScale(self, dLongitude, dLatitude):
        """ GetScale(self: MgCoordinateSystem, dLongitude: float, dLatitude: float) -> float """
        pass

    def GetScaleH(self, dLongitude, dLatitude):
        """ GetScaleH(self: MgCoordinateSystem, dLongitude: float, dLatitude: float) -> float """
        pass

    def GetScaleK(self, dLongitude, dLatitude):
        """ GetScaleK(self: MgCoordinateSystem, dLongitude: float, dLatitude: float) -> float """
        pass

    def GetScaleReduction(self):
        """ GetScaleReduction(self: MgCoordinateSystem) -> float """
        pass

    def GetSource(self):
        """ GetSource(self: MgCoordinateSystem) -> str """
        pass

    def GetSridCode(self):
        """ GetSridCode(self: MgCoordinateSystem) -> int """
        pass

    def GetType(self):
        """ GetType(self: MgCoordinateSystem) -> int """
        pass

    def GetUnitCode(self):
        """ GetUnitCode(self: MgCoordinateSystem) -> int """
        pass

    def GetUnits(self):
        """ GetUnits(self: MgCoordinateSystem) -> str """
        pass

    def GetUnitScale(self):
        """ GetUnitScale(self: MgCoordinateSystem) -> float """
        pass

    def GetZeroX(self):
        """ GetZeroX(self: MgCoordinateSystem) -> float """
        pass

    def GetZeroY(self):
        """ GetZeroY(self: MgCoordinateSystem) -> float """
        pass

    def IsEncrypted(self):
        """ IsEncrypted(self: MgCoordinateSystem) -> bool """
        pass

    def IsGeodetic(self):
        """ IsGeodetic(self: MgCoordinateSystem) -> bool """
        pass

    def IsLegalCountryOrState(self, sCountryOrState):
        """ IsLegalCountryOrState(self: MgCoordinateSystem, sCountryOrState: str) -> bool """
        pass

    def IsLegalCsCode(self, sCode):
        """ IsLegalCsCode(self: MgCoordinateSystem, sCode: str) -> bool """
        pass

    def IsLegalDescription(self, sDesc):
        """ IsLegalDescription(self: MgCoordinateSystem, sDesc: str) -> bool """
        pass

    def IsLegalGroup(self, sGroup):
        """ IsLegalGroup(self: MgCoordinateSystem, sGroup: str) -> bool """
        pass

    def IsLegalLocation(self, sLoc):
        """ IsLegalLocation(self: MgCoordinateSystem, sLoc: str) -> bool """
        pass

    def IsLegalSource(self, sSource):
        """ IsLegalSource(self: MgCoordinateSystem, sSource: str) -> bool """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystem) -> bool """
        pass

    def IsSameAs(self, pDef):
        """ IsSameAs(self: MgCoordinateSystem, pDef: MgGuardDisposable) -> bool """
        pass

    def IsUsable(self, pCatalog):
        """ IsUsable(self: MgCoordinateSystem, pCatalog: MgCoordinateSystemCatalog) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystem) -> bool """
        pass

    def IsValidLonLat(self, dLongitude, dLatitude):
        """ IsValidLonLat(self: MgCoordinateSystem, dLongitude: float, dLatitude: float) -> bool """
        pass

    def IsValidXY(self, dX, dY):
        """ IsValidXY(self: MgCoordinateSystem, dX: float, dY: float) -> bool """
        pass

    def MeasureEuclideanDistance(self, *__args):
        """
        MeasureEuclideanDistance(self: MgCoordinateSystem, x1: float, y1: float, x2: float, y2: float) -> float
        MeasureEuclideanDistance(self: MgCoordinateSystem, coord1: MgCoordinate, coord2: MgCoordinate) -> float
        """
        pass

    def MeasureGreatCircleDistance(self, *__args):
        """
        MeasureGreatCircleDistance(self: MgCoordinateSystem, x1: float, y1: float, x2: float, y2: float) -> float
        MeasureGreatCircleDistance(self: MgCoordinateSystem, coord1: MgCoordinate, coord2: MgCoordinate) -> float
        """
        pass

    def SetCountryOrState(self, sCountryOrState):
        """ SetCountryOrState(self: MgCoordinateSystem, sCountryOrState: str) """
        pass

    def SetCsCode(self, sCode):
        """ SetCsCode(self: MgCoordinateSystem, sCode: str) """
        pass

    def SetDatumDefinition(self, pDatum):
        """ SetDatumDefinition(self: MgCoordinateSystem, pDatum: MgCoordinateSystemDatum) """
        pass

    def SetDescription(self, sDesc):
        """ SetDescription(self: MgCoordinateSystem, sDesc: str) """
        pass

    def SetEllipsoidDefinition(self, pEllipsoid):
        """ SetEllipsoidDefinition(self: MgCoordinateSystem, pEllipsoid: MgCoordinateSystemEllipsoid) """
        pass

    def SetEncryptMode(self, bIsEncrypted):
        """ SetEncryptMode(self: MgCoordinateSystem, bIsEncrypted: bool) """
        pass

    def SetGroup(self, sGroup):
        """ SetGroup(self: MgCoordinateSystem, sGroup: str) """
        pass

    def SetLocation(self, sLoc):
        """ SetLocation(self: MgCoordinateSystem, sLoc: str) """
        pass

    def SetLonLatBounds(self, dLonMin, dLatMin, dLonMax, dLatMax):
        """ SetLonLatBounds(self: MgCoordinateSystem, dLonMin: float, dLatMin: float, dLonMax: float, dLatMax: float) """
        pass

    def SetMapScale(self, dMapScale):
        """ SetMapScale(self: MgCoordinateSystem, dMapScale: float) """
        pass

    def SetOffsets(self, dXOffset, dYOffset):
        """ SetOffsets(self: MgCoordinateSystem, dXOffset: float, dYOffset: float) """
        pass

    def SetOriginLatitude(self, dOrgLat):
        """ SetOriginLatitude(self: MgCoordinateSystem, dOrgLat: float) """
        pass

    def SetOriginLongitude(self, dOrgLng):
        """ SetOriginLongitude(self: MgCoordinateSystem, dOrgLng: float) """
        pass

    def SetProjectionCode(self, prjType):
        """ SetProjectionCode(self: MgCoordinateSystem, prjType: int) """
        pass

    def SetProjectionParameter(self, nIndex, dValue):
        """ SetProjectionParameter(self: MgCoordinateSystem, nIndex: int, dValue: float) """
        pass

    def SetProtectMode(self, bIsProtected):
        """ SetProtectMode(self: MgCoordinateSystem, bIsProtected: bool) """
        pass

    def SetQuadrant(self, sQuad):
        """ SetQuadrant(self: MgCoordinateSystem, sQuad: Int16) """
        pass

    def SetScaleReduction(self, dSclRed):
        """ SetScaleReduction(self: MgCoordinateSystem, dSclRed: float) """
        pass

    def SetSource(self, sSource):
        """ SetSource(self: MgCoordinateSystem, sSource: str) """
        pass

    def SetUnitCode(self, unit):
        """ SetUnitCode(self: MgCoordinateSystem, unit: int) """
        pass

    def SetXYBounds(self, dXMin, dYMin, dXMax, dYMax):
        """ SetXYBounds(self: MgCoordinateSystem, dXMin: float, dYMin: float, dXMax: float, dYMax: float) """
        pass

    def SetZeroes(self, dXZero, dYZero):
        """ SetZeroes(self: MgCoordinateSystem, dXZero: float, dYZero: float) """
        pass

    def ToString(self):
        """ ToString(self: MgCoordinateSystem) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    CsCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CsCode(self: MgCoordinateSystem) -> str

"""

    Datum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Datum(self: MgCoordinateSystem) -> str

"""

    DatumDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DatumDescription(self: MgCoordinateSystem) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgCoordinateSystem) -> str

"""

    Ellipsoid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ellipsoid(self: MgCoordinateSystem) -> str

"""

    EllipsoidDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EllipsoidDescription(self: MgCoordinateSystem) -> str

"""

    EpsgCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EpsgCode(self: MgCoordinateSystem) -> int

"""

    EpsgQuadrant = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EpsgQuadrant(self: MgCoordinateSystem) -> Int16

"""

    MaxX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxX(self: MgCoordinateSystem) -> float

"""

    MaxY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaxY(self: MgCoordinateSystem) -> float

"""

    MinX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinX(self: MgCoordinateSystem) -> float

"""

    MinY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinY(self: MgCoordinateSystem) -> float

"""

    Projection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Projection(self: MgCoordinateSystem) -> str

"""

    ProjectionDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProjectionDescription(self: MgCoordinateSystem) -> str

"""

    SridCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SridCode(self: MgCoordinateSystem) -> int

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: MgCoordinateSystem) -> int

"""

    Units = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Units(self: MgCoordinateSystem) -> str

"""

    UnitScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnitScale(self: MgCoordinateSystem) -> float

"""


    swigCMemOwn = None


class MgCoordinateSystemCatalog(MgGuardDisposable):
    """ MgCoordinateSystemCatalog(cPtr: IntPtr, cMemoryOwn: bool) """
    def AreDictionaryFilesWritable(self):
        """ AreDictionaryFilesWritable(self: MgCoordinateSystemCatalog) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemCatalog) """
        pass

    def GetCategoryDictionary(self):
        """ GetCategoryDictionary(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemCategoryDictionary """
        pass

    def GetCoordinateSystemDictionary(self):
        """ GetCoordinateSystemDictionary(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemDictionary """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemCatalog) -> IntPtr """
        pass

    def GetDatumDictionary(self):
        """ GetDatumDictionary(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemDatumDictionary """
        pass

    def GetDefaultDictionaryDir(self):
        """ GetDefaultDictionaryDir(self: MgCoordinateSystemCatalog) -> str """
        pass

    def GetDefaultUserDictionaryDir(self):
        """ GetDefaultUserDictionaryDir(self: MgCoordinateSystemCatalog) -> str """
        pass

    def GetDictionaryDir(self):
        """ GetDictionaryDir(self: MgCoordinateSystemCatalog) -> str """
        pass

    def GetDictionaryUtility(self):
        """ GetDictionaryUtility(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemDictionaryUtility """
        pass

    def GetEllipsoidDictionary(self):
        """ GetEllipsoidDictionary(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemEllipsoidDictionary """
        pass

    def GetFormatConverter(self):
        """ GetFormatConverter(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemFormatConverter """
        pass

    def GetGeodeticPathDictionary(self):
        """ GetGeodeticPathDictionary(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemGeodeticPathDictionary """
        pass

    def GetGeodeticTransformations(self, pSource, pTarget):
        """ GetGeodeticTransformations(self: MgCoordinateSystemCatalog, pSource: MgCoordinateSystemDatum, pTarget: MgCoordinateSystemDatum) -> MgDisposableCollection """
        pass

    def GetGeodeticTransformDefDictionary(self):
        """ GetGeodeticTransformDefDictionary(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemGeodeticTransformDefDictionary """
        pass

    def GetMathComparator(self):
        """ GetMathComparator(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemMathComparator """
        pass

    def GetProjectionInformation(self):
        """ GetProjectionInformation(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemProjectionInformation """
        pass

    def GetProtectionMode(self):
        """ GetProtectionMode(self: MgCoordinateSystemCatalog) -> Int16 """
        pass

    def GetUnitInformation(self):
        """ GetUnitInformation(self: MgCoordinateSystemCatalog) -> MgCoordinateSystemUnitInformation """
        pass

    def GetUserDictionaryDir(self):
        """ GetUserDictionaryDir(self: MgCoordinateSystemCatalog) -> str """
        pass

    def SetDefaultDictionaryDirAndFileNames(self):
        """ SetDefaultDictionaryDirAndFileNames(self: MgCoordinateSystemCatalog) """
        pass

    def SetDictionaryDir(self, sDirPath):
        """ SetDictionaryDir(self: MgCoordinateSystemCatalog, sDirPath: str) """
        pass

    def SetProtectionMode(self, nMode):
        """ SetProtectionMode(self: MgCoordinateSystemCatalog, nMode: Int16) """
        pass

    def SetUserDictionaryDir(self, sDirPath):
        """ SetUserDictionaryDir(self: MgCoordinateSystemCatalog, sDirPath: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemCategory(MgGuardDisposable):
    """ MgCoordinateSystemCategory(cPtr: IntPtr, cMemoryOwn: bool) """
    def AddCoordinateSystem(self, sName):
        """ AddCoordinateSystem(self: MgCoordinateSystemCategory, sName: str) """
        pass

    def Clear(self):
        """ Clear(self: MgCoordinateSystemCategory) """
        pass

    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystemCategory) -> MgCoordinateSystemCategory """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemCategory) """
        pass

    def GetCatalog(self):
        """ GetCatalog(self: MgCoordinateSystemCategory) -> MgCoordinateSystemCatalog """
        pass

    def GetCoordinateSystems(self):
        """ GetCoordinateSystems(self: MgCoordinateSystemCategory) -> MgStringCollection """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemCategory) -> IntPtr """
        pass

    def GetEnum(self):
        """ GetEnum(self: MgCoordinateSystemCategory) -> MgCoordinateSystemEnum """
        pass

    def GetName(self):
        """ GetName(self: MgCoordinateSystemCategory) -> str """
        pass

    def GetSize(self):
        """ GetSize(self: MgCoordinateSystemCategory) -> int """
        pass

    def HasCoordinateSystem(self, sName):
        """ HasCoordinateSystem(self: MgCoordinateSystemCategory, sName: str) -> bool """
        pass

    def IsLegalName(self, sName):
        """ IsLegalName(self: MgCoordinateSystemCategory, sName: str) -> bool """
        pass

    def IsSameAs(self, pDef):
        """ IsSameAs(self: MgCoordinateSystemCategory, pDef: MgGuardDisposable) -> bool """
        pass

    def IsUsable(self, pCatalog):
        """ IsUsable(self: MgCoordinateSystemCategory, pCatalog: MgCoordinateSystemCatalog) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemCategory) -> bool """
        pass

    def RemoveCoordinateSystem(self, sName):
        """ RemoveCoordinateSystem(self: MgCoordinateSystemCategory, sName: str) """
        pass

    def SetName(self, sName):
        """ SetName(self: MgCoordinateSystemCategory, sName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemDictionaryBase(MgGuardDisposable):
    """ MgCoordinateSystemDictionaryBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Add(self, pDefinition):
        """ Add(self: MgCoordinateSystemDictionaryBase, pDefinition: MgGuardDisposable) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemDictionaryBase) """
        pass

    def Get(self, sName):
        """ Get(self: MgCoordinateSystemDictionaryBase, sName: str) -> MgGuardDisposable """
        pass

    def GetCatalog(self):
        """ GetCatalog(self: MgCoordinateSystemDictionaryBase) -> MgCoordinateSystemCatalog """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemDictionaryBase) -> IntPtr """
        pass

    def GetDefaultFileName(self):
        """ GetDefaultFileName(self: MgCoordinateSystemDictionaryBase) -> str """
        pass

    def GetEnum(self):
        """ GetEnum(self: MgCoordinateSystemDictionaryBase) -> MgCoordinateSystemEnum """
        pass

    def GetFileName(self):
        """ GetFileName(self: MgCoordinateSystemDictionaryBase) -> str """
        pass

    def GetPath(self):
        """ GetPath(self: MgCoordinateSystemDictionaryBase) -> str """
        pass

    def GetSize(self):
        """ GetSize(self: MgCoordinateSystemDictionaryBase) -> int """
        pass

    def Has(self, sName):
        """ Has(self: MgCoordinateSystemDictionaryBase, sName: str) -> bool """
        pass

    def Modify(self, pDefinition):
        """ Modify(self: MgCoordinateSystemDictionaryBase, pDefinition: MgGuardDisposable) """
        pass

    def Remove(self, sName):
        """ Remove(self: MgCoordinateSystemDictionaryBase, sName: str) """
        pass

    def SetFileName(self, sFileName):
        """ SetFileName(self: MgCoordinateSystemDictionaryBase, sFileName: str) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemCategoryDictionary(MgCoordinateSystemDictionaryBase):
    """ MgCoordinateSystemCategoryDictionary(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemCategoryDictionary) """
        pass

    def GetCategory(self, sName):
        """ GetCategory(self: MgCoordinateSystemCategoryDictionary, sName: str) -> MgCoordinateSystemCategory """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemCategoryDictionary) -> IntPtr """
        pass

    def NewCategory(self):
        """ NewCategory(self: MgCoordinateSystemCategoryDictionary) -> MgCoordinateSystemCategory """
        pass

    def Rename(self, sOldName, sNewName):
        """ Rename(self: MgCoordinateSystemCategoryDictionary, sOldName: str, sNewName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemCodeFormat(object):
    """ MgCoordinateSystemCodeFormat() """
    Epsg = 1
    Mentor = 0


class MgCoordinateSystemComputationFailedException(MgApplicationException):
    """
    MgCoordinateSystemComputationFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateSystemComputationFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemComputationFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemComputationFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemConversionFailedException(MgApplicationException):
    """
    MgCoordinateSystemConversionFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateSystemConversionFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemConversionFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemConversionFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemDatum(MgGuardDisposable):
    """ MgCoordinateSystemDatum(cPtr: IntPtr, cMemoryOwn: bool) """
    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystemDatum) -> MgCoordinateSystemDatum """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemDatum) """
        pass

    def GetAge(self):
        """ GetAge(self: MgCoordinateSystemDatum) -> Int16 """
        pass

    def GetCatalog(self):
        """ GetCatalog(self: MgCoordinateSystemDatum) -> MgCoordinateSystemCatalog """
        pass

    def GetCountryOrState(self):
        """ GetCountryOrState(self: MgCoordinateSystemDatum) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemDatum) -> IntPtr """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgCoordinateSystemDatum) -> str """
        pass

    def GetDtCode(self):
        """ GetDtCode(self: MgCoordinateSystemDatum) -> str """
        pass

    def GetEllipsoid(self):
        """ GetEllipsoid(self: MgCoordinateSystemDatum) -> str """
        pass

    def GetEllipsoidDefinition(self):
        """ GetEllipsoidDefinition(self: MgCoordinateSystemDatum) -> MgCoordinateSystemEllipsoid """
        pass

    def GetEpsgCode(self):
        """ GetEpsgCode(self: MgCoordinateSystemDatum) -> Int16 """
        pass

    def GetGeodeticTransformations(self, pTarget):
        """ GetGeodeticTransformations(self: MgCoordinateSystemDatum, pTarget: MgCoordinateSystemDatum) -> MgDisposableCollection """
        pass

    def GetGroup(self):
        """ GetGroup(self: MgCoordinateSystemDatum) -> str """
        pass

    def GetLocation(self):
        """ GetLocation(self: MgCoordinateSystemDatum) -> str """
        pass

    def GetSource(self):
        """ GetSource(self: MgCoordinateSystemDatum) -> str """
        pass

    def IsEncrypted(self):
        """ IsEncrypted(self: MgCoordinateSystemDatum) -> bool """
        pass

    def IsLegalCountryOrState(self, sCountryOrState):
        """ IsLegalCountryOrState(self: MgCoordinateSystemDatum, sCountryOrState: str) -> bool """
        pass

    def IsLegalDescription(self, sDesc):
        """ IsLegalDescription(self: MgCoordinateSystemDatum, sDesc: str) -> bool """
        pass

    def IsLegalDtCode(self, sCode):
        """ IsLegalDtCode(self: MgCoordinateSystemDatum, sCode: str) -> bool """
        pass

    def IsLegalGroup(self, sGroup):
        """ IsLegalGroup(self: MgCoordinateSystemDatum, sGroup: str) -> bool """
        pass

    def IsLegalLocation(self, sLoc):
        """ IsLegalLocation(self: MgCoordinateSystemDatum, sLoc: str) -> bool """
        pass

    def IsLegalSource(self, sSource):
        """ IsLegalSource(self: MgCoordinateSystemDatum, sSource: str) -> bool """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystemDatum) -> bool """
        pass

    def IsSameAs(self, pDef):
        """ IsSameAs(self: MgCoordinateSystemDatum, pDef: MgGuardDisposable) -> bool """
        pass

    def IsUsable(self, pCatalog):
        """ IsUsable(self: MgCoordinateSystemDatum, pCatalog: MgCoordinateSystemCatalog) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemDatum) -> bool """
        pass

    def SetCountryOrState(self, sCountryOrState):
        """ SetCountryOrState(self: MgCoordinateSystemDatum, sCountryOrState: str) """
        pass

    def SetDescription(self, sDesc):
        """ SetDescription(self: MgCoordinateSystemDatum, sDesc: str) """
        pass

    def SetDtCode(self, sCode):
        """ SetDtCode(self: MgCoordinateSystemDatum, sCode: str) """
        pass

    def SetEllipsoid(self, sEllipsoid):
        """ SetEllipsoid(self: MgCoordinateSystemDatum, sEllipsoid: str) """
        pass

    def SetEllipsoidDefinition(self, pDef):
        """ SetEllipsoidDefinition(self: MgCoordinateSystemDatum, pDef: MgCoordinateSystemEllipsoid) """
        pass

    def SetEncryptMode(self, bIsEncrypted):
        """ SetEncryptMode(self: MgCoordinateSystemDatum, bIsEncrypted: bool) """
        pass

    def SetEpsgCode(self, epsgCode):
        """ SetEpsgCode(self: MgCoordinateSystemDatum, epsgCode: Int16) """
        pass

    def SetGroup(self, sGroup):
        """ SetGroup(self: MgCoordinateSystemDatum, sGroup: str) """
        pass

    def SetLocation(self, sLoc):
        """ SetLocation(self: MgCoordinateSystemDatum, sLoc: str) """
        pass

    def SetProtectMode(self, bIsProtected):
        """ SetProtectMode(self: MgCoordinateSystemDatum, bIsProtected: bool) """
        pass

    def SetSource(self, sSource):
        """ SetSource(self: MgCoordinateSystemDatum, sSource: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemDatumDictionary(MgCoordinateSystemDictionaryBase):
    """ MgCoordinateSystemDatumDictionary(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemDatumDictionary) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemDatumDictionary) -> IntPtr """
        pass

    def GetDatum(self, sName):
        """ GetDatum(self: MgCoordinateSystemDatumDictionary, sName: str) -> MgCoordinateSystemDatum """
        pass

    def NewDatum(self):
        """ NewDatum(self: MgCoordinateSystemDatumDictionary) -> MgCoordinateSystemDatum """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemDictionary(MgCoordinateSystemDictionaryBase):
    """ MgCoordinateSystemDictionary(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemDictionary) """
        pass

    def GetCoordinateSystem(self, sName):
        """ GetCoordinateSystem(self: MgCoordinateSystemDictionary, sName: str) -> MgCoordinateSystem """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemDictionary) -> IntPtr """
        pass

    def NewCoordinateSystem(self):
        """ NewCoordinateSystem(self: MgCoordinateSystemDictionary) -> MgCoordinateSystem """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemDictionaryUtility(MgGuardDisposable):
    """ MgCoordinateSystemDictionaryUtility(cPtr: IntPtr, cMemoryOwn: bool) """
    def CreateCategoryDictionary(self, sDictPathName):
        """ CreateCategoryDictionary(self: MgCoordinateSystemDictionaryUtility, sDictPathName: str) """
        pass

    def CreateCoordsysDictionary(self, sDictPathName):
        """ CreateCoordsysDictionary(self: MgCoordinateSystemDictionaryUtility, sDictPathName: str) """
        pass

    def CreateDatumDictionary(self, sDictPathName):
        """ CreateDatumDictionary(self: MgCoordinateSystemDictionaryUtility, sDictPathName: str) """
        pass

    def CreateEllipsoidDictionary(self, sDictPathName):
        """ CreateEllipsoidDictionary(self: MgCoordinateSystemDictionaryUtility, sDictPathName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemDictionaryUtility) """
        pass

    def GetCatalog(self):
        """ GetCatalog(self: MgCoordinateSystemDictionaryUtility) -> MgCoordinateSystemCatalog """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemDictionaryUtility) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemEllipsoid(MgGuardDisposable):
    """ MgCoordinateSystemEllipsoid(cPtr: IntPtr, cMemoryOwn: bool) """
    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystemEllipsoid) -> MgCoordinateSystemEllipsoid """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemEllipsoid) """
        pass

    def EccentricityToFlatteningRatio(self, dEccent):
        """ EccentricityToFlatteningRatio(self: MgCoordinateSystemEllipsoid, dEccent: float) -> float """
        pass

    def EquatorialRadiusFromPolarRadiusFlatteningRatio(self, dPolarRadius, dFlatteningRatio):
        """ EquatorialRadiusFromPolarRadiusFlatteningRatio(self: MgCoordinateSystemEllipsoid, dPolarRadius: float, dFlatteningRatio: float) -> float """
        pass

    def FlatteningRatioFromRadii(self, dEquatorialRadius, dPolarRadius):
        """ FlatteningRatioFromRadii(self: MgCoordinateSystemEllipsoid, dEquatorialRadius: float, dPolarRadius: float) -> float """
        pass

    def FlatteningRatioToEccentricity(self, dFlat):
        """ FlatteningRatioToEccentricity(self: MgCoordinateSystemEllipsoid, dFlat: float) -> float """
        pass

    def GetAge(self):
        """ GetAge(self: MgCoordinateSystemEllipsoid) -> Int16 """
        pass

    def GetCatalog(self):
        """ GetCatalog(self: MgCoordinateSystemEllipsoid) -> MgCoordinateSystemCatalog """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemEllipsoid) -> IntPtr """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgCoordinateSystemEllipsoid) -> str """
        pass

    def GetEccentricity(self):
        """ GetEccentricity(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetElCode(self):
        """ GetElCode(self: MgCoordinateSystemEllipsoid) -> str """
        pass

    def GetEpsgCode(self):
        """ GetEpsgCode(self: MgCoordinateSystemEllipsoid) -> Int16 """
        pass

    def GetEquatorialRadius(self):
        """ GetEquatorialRadius(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetFlatteningRatio(self):
        """ GetFlatteningRatio(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetFlatteningRatioMax(self):
        """ GetFlatteningRatioMax(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetFlatteningRatioMin(self):
        """ GetFlatteningRatioMin(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetGreatCircleAzimuth(self, dLongitude1, dLatitude1, dLongitude2, dLatitude2):
        """ GetGreatCircleAzimuth(self: MgCoordinateSystemEllipsoid, dLongitude1: float, dLatitude1: float, dLongitude2: float, dLatitude2: float) -> float """
        pass

    def GetGreatCircleDistance(self, dLongitude1, dLatitude1, dLongitude2, dLatitude2):
        """ GetGreatCircleDistance(self: MgCoordinateSystemEllipsoid, dLongitude1: float, dLatitude1: float, dLongitude2: float, dLatitude2: float) -> float """
        pass

    def GetGroup(self):
        """ GetGroup(self: MgCoordinateSystemEllipsoid) -> str """
        pass

    def GetPolarRadius(self):
        """ GetPolarRadius(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetRadiusMax(self):
        """ GetRadiusMax(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetRadiusMin(self):
        """ GetRadiusMin(self: MgCoordinateSystemEllipsoid) -> float """
        pass

    def GetSource(self):
        """ GetSource(self: MgCoordinateSystemEllipsoid) -> str """
        pass

    def IsEncrypted(self):
        """ IsEncrypted(self: MgCoordinateSystemEllipsoid) -> bool """
        pass

    def IsLegalDescription(self, sDesc):
        """ IsLegalDescription(self: MgCoordinateSystemEllipsoid, sDesc: str) -> bool """
        pass

    def IsLegalElCode(self, sCode):
        """ IsLegalElCode(self: MgCoordinateSystemEllipsoid, sCode: str) -> bool """
        pass

    def IsLegalFlatteningRatio(self, dFlat):
        """ IsLegalFlatteningRatio(self: MgCoordinateSystemEllipsoid, dFlat: float) -> bool """
        pass

    def IsLegalGroup(self, sGroup):
        """ IsLegalGroup(self: MgCoordinateSystemEllipsoid, sGroup: str) -> bool """
        pass

    def IsLegalRadius(self, dRadius):
        """ IsLegalRadius(self: MgCoordinateSystemEllipsoid, dRadius: float) -> bool """
        pass

    def IsLegalSource(self, sSource):
        """ IsLegalSource(self: MgCoordinateSystemEllipsoid, sSource: str) -> bool """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystemEllipsoid) -> bool """
        pass

    def IsSameAs(self, pDef):
        """ IsSameAs(self: MgCoordinateSystemEllipsoid, pDef: MgGuardDisposable) -> bool """
        pass

    def IsUsable(self):
        """ IsUsable(self: MgCoordinateSystemEllipsoid) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemEllipsoid) -> bool """
        pass

    def PolarRadiusFromEquatorialRadiusFlatteningRatio(self, dEquatorialRadius, dFlatteningRatio):
        """ PolarRadiusFromEquatorialRadiusFlatteningRatio(self: MgCoordinateSystemEllipsoid, dEquatorialRadius: float, dFlatteningRatio: float) -> float """
        pass

    def SetDescription(self, sDesc):
        """ SetDescription(self: MgCoordinateSystemEllipsoid, sDesc: str) """
        pass

    def SetElCode(self, sCode):
        """ SetElCode(self: MgCoordinateSystemEllipsoid, sCode: str) """
        pass

    def SetEncryptMode(self, bIsEncrypted):
        """ SetEncryptMode(self: MgCoordinateSystemEllipsoid, bIsEncrypted: bool) """
        pass

    def SetEpsgCode(self, epsgCode):
        """ SetEpsgCode(self: MgCoordinateSystemEllipsoid, epsgCode: Int16) """
        pass

    def SetGroup(self, sGroup):
        """ SetGroup(self: MgCoordinateSystemEllipsoid, sGroup: str) """
        pass

    def SetProtectMode(self, bIsProtected):
        """ SetProtectMode(self: MgCoordinateSystemEllipsoid, bIsProtected: bool) """
        pass

    def SetRadii(self, dEquatorialRadius, dPolarRadius):
        """ SetRadii(self: MgCoordinateSystemEllipsoid, dEquatorialRadius: float, dPolarRadius: float) """
        pass

    def SetSource(self, sSource):
        """ SetSource(self: MgCoordinateSystemEllipsoid, sSource: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgCoordinateSystemEllipsoid) -> str

"""

    ElCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ElCode(self: MgCoordinateSystemEllipsoid) -> str

"""


    swigCMemOwn = None


class MgCoordinateSystemEllipsoidDictionary(MgCoordinateSystemDictionaryBase):
    """ MgCoordinateSystemEllipsoidDictionary(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemEllipsoidDictionary) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemEllipsoidDictionary) -> IntPtr """
        pass

    def GetEllipsoid(self, sName):
        """ GetEllipsoid(self: MgCoordinateSystemEllipsoidDictionary, sName: str) -> MgCoordinateSystemEllipsoid """
        pass

    def NewEllipsoid(self):
        """ NewEllipsoid(self: MgCoordinateSystemEllipsoidDictionary) -> MgCoordinateSystemEllipsoid """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemEnum(MgGuardDisposable):
    """ MgCoordinateSystemEnum(cPtr: IntPtr, cMemoryOwn: bool) """
    def AddFilter(self, pFilter):
        """ AddFilter(self: MgCoordinateSystemEnum, pFilter: MgCoordinateSystemFilter) """
        pass

    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystemEnum) -> MgCoordinateSystemEnum """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemEnum) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemEnum) -> IntPtr """
        pass

    def Next(self, ulCount):
        """ Next(self: MgCoordinateSystemEnum, ulCount: int) -> MgDisposableCollection """
        pass

    def NextDescription(self, ulCount):
        """ NextDescription(self: MgCoordinateSystemEnum, ulCount: int) -> MgStringCollection """
        pass

    def NextName(self, ulCount):
        """ NextName(self: MgCoordinateSystemEnum, ulCount: int) -> MgStringCollection """
        pass

    def Reset(self):
        """ Reset(self: MgCoordinateSystemEnum) """
        pass

    def Skip(self, ulSkipCount):
        """ Skip(self: MgCoordinateSystemEnum, ulSkipCount: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemEnumInteger32(MgGuardDisposable):
    """ MgCoordinateSystemEnumInteger32(cPtr: IntPtr, cMemoryOwn: bool) """
    def AddFilter(self, pFilter):
        """ AddFilter(self: MgCoordinateSystemEnumInteger32, pFilter: MgCoordinateSystemFilterInteger32) """
        pass

    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystemEnumInteger32) -> MgCoordinateSystemEnumInteger32 """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemEnumInteger32) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemEnumInteger32) -> IntPtr """
        pass

    def Next(self, ulCount):
        """ Next(self: MgCoordinateSystemEnumInteger32, ulCount: int) -> MgStringCollection """
        pass

    def Reset(self):
        """ Reset(self: MgCoordinateSystemEnumInteger32) """
        pass

    def Skip(self, ulSkipCount):
        """ Skip(self: MgCoordinateSystemEnumInteger32, ulSkipCount: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemErrorCode(object):
    """ MgCoordinateSystemErrorCode() """
    AFFZERO = 251
    AZM = 201
    AZMTH = 202
    ConversionFailed = 1003
    CRTMM = 242
    DENRGN = 253
    ELEVEL = 254
    GEOMM = 241
    HMISPHR = 247
    InitializationFailed = 1002
    InvalidArgument = 1005
    INVDTM = 236
    INVELP = 237
    INVPRJ = 235
    INVQUAD = 240
    LAT = 203
    LATEQU = 204
    LLRNG = 238
    LNG = 205
    LNGEQU = 206
    MAPSCL = 207
    MAX15 = 249
    MEREQU = 208
    MRCAT = 209
    MSCOEF = 210
    NOREF = 211
    NOTNRTH = 212
    NRDATUM = 252
    NRTHLAT = 213
    NRTHPNT = 214
    NullArgument = 1004
    OBLQPOLE = 250
    Ok = 1000
    ORGLAT = 215
    ORGLNG = 216
    OSTN02 = 255
    OSTN97 = 253
    OutOfMemory = 1001
    PLL90 = 217
    PLLED = 243
    PLLEQU = 218
    PLLLRG = 219
    PLLREV = 220
    PLLZERO = 221
    PLRLAT = 244
    POLDD = 222
    POLDUP = 223
    POLLAT = 224
    POLLNG = 225
    QUAD = 226
    RNGORD = 239
    SCLRED = 227
    SOTHLAT = 228
    STDLAT = 229
    STDLNG = 230
    STDPLL = 231
    STDSOU = 232
    STDWEST = 233
    TMKRG0 = 256
    UNIT = 234
    USEPLR = 245
    USESW = 248
    UTMZON = 246


class MgCoordinateSystemFactory(MgGuardDisposable):
    """
    MgCoordinateSystemFactory(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateSystemFactory()
    """
    def ConvertCoordinateSystemCodeToWkt(self, code):
        """ ConvertCoordinateSystemCodeToWkt(self: MgCoordinateSystemFactory, code: str) -> str """
        pass

    def ConvertEpsgCodeToWkt(self, code):
        """ ConvertEpsgCodeToWkt(self: MgCoordinateSystemFactory, code: int) -> str """
        pass

    def ConvertWktToCoordinateSystemCode(self, wkt):
        """ ConvertWktToCoordinateSystemCode(self: MgCoordinateSystemFactory, wkt: str) -> str """
        pass

    def ConvertWktToEpsgCode(self, wkt):
        """ ConvertWktToEpsgCode(self: MgCoordinateSystemFactory, wkt: str) -> int """
        pass

    def Create(self, wkt):
        """ Create(self: MgCoordinateSystemFactory, wkt: str) -> MgCoordinateSystem """
        pass

    def CreateFromCode(self, code):
        """ CreateFromCode(self: MgCoordinateSystemFactory, code: str) -> MgCoordinateSystem """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemFactory) """
        pass

    def EnumerateCategories(self):
        """ EnumerateCategories(self: MgCoordinateSystemFactory) -> MgStringCollection """
        pass

    def EnumerateCoordinateSystems(self, category):
        """ EnumerateCoordinateSystems(self: MgCoordinateSystemFactory, category: str) -> MgBatchPropertyCollection """
        pass

    def GenericGrid(self, *__args):
        """
        GenericGrid(self: MgCoordinateSystemFactory, pGridCs: MgCoordinateSystem, pFrameCs: MgCoordinateSystem, bSetExceptionsOn: bool) -> MgCoordinateSystemGridBase
        GenericGrid(self: MgCoordinateSystemFactory, sGridCs: str, sFrameCs: str, bSetExceptionsOn: bool) -> MgCoordinateSystemGridBase
        """
        pass

    def GetBaseLibrary(self):
        """ GetBaseLibrary(self: MgCoordinateSystemFactory) -> str """
        pass

    def GetCatalog(self):
        """ GetCatalog(self: MgCoordinateSystemFactory) -> MgCoordinateSystemCatalog """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemFactory) -> IntPtr """
        pass

    def GetMgrs(self, dEquatorialRadius, dEccentricity, nLetteringScheme, bSetExceptionsOn):
        """ GetMgrs(self: MgCoordinateSystemFactory, dEquatorialRadius: float, dEccentricity: float, nLetteringScheme: Int16, bSetExceptionsOn: bool) -> MgCoordinateSystemMgrs """
        pass

    def GetMgrsDatum(self, sDatumCode, nLetteringScheme, bSetExceptionsOn):
        """ GetMgrsDatum(self: MgCoordinateSystemFactory, sDatumCode: str, nLetteringScheme: Int16, bSetExceptionsOn: bool) -> MgCoordinateSystemMgrs """
        pass

    def GetMgrsEllipsoid(self, sEllipsoidCode, nLetteringScheme, bSetExceptionsOn):
        """ GetMgrsEllipsoid(self: MgCoordinateSystemFactory, sEllipsoidCode: str, nLetteringScheme: Int16, bSetExceptionsOn: bool) -> MgCoordinateSystemMgrs """
        pass

    def GetTransform(self, pSource, pTarget):
        """ GetTransform(self: MgCoordinateSystemFactory, pSource: MgCoordinateSystem, pTarget: MgCoordinateSystem) -> MgCoordinateSystemTransform """
        pass

    def GridBoundary(self, *__args):
        """
        GridBoundary(self: MgCoordinateSystemFactory, boundary: MgPolygon) -> MgCoordinateSystemGridBoundary
        GridBoundary(self: MgCoordinateSystemFactory, southwest: MgCoordinate, northeast: MgCoordinate) -> MgCoordinateSystemGridBoundary
        """
        pass

    def GridSpecification(self, *__args):
        """
        GridSpecification(self: MgCoordinateSystemFactory, gridType: int, gridLevel: int) -> MgCoordinateSystemGridSpecification
        GridSpecification(self: MgCoordinateSystemFactory, increment: float, tickIncrement: float, unitCode: int, curvePrecision: float) -> MgCoordinateSystemGridSpecification
        GridSpecification(self: MgCoordinateSystemFactory) -> MgCoordinateSystemGridSpecification
        """
        pass

    def IsValid(self, wkt):
        """ IsValid(self: MgCoordinateSystemFactory, wkt: str) -> bool """
        pass

    def MgrsGrid(self, *__args):
        """
        MgrsGrid(self: MgCoordinateSystemFactory, sFrameCs: str, bUseFrameDatum: bool, nLetteringScheme: Int16, bSetExceptionsOn: bool) -> MgCoordinateSystemGridBase
        MgrsGrid(self: MgCoordinateSystemFactory, pFrameCs: MgCoordinateSystem, bUseFrameDatum: bool, nLetteringScheme: Int16, bSetExceptionsOn: bool) -> MgCoordinateSystemGridBase
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemFilter(MgGuardDisposable):
    """ MgCoordinateSystemFilter(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemFilter) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemFilter) -> IntPtr """
        pass

    def IsFilteredOut(self, pDef):
        """ IsFilteredOut(self: MgCoordinateSystemFilter, pDef: MgGuardDisposable) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemFilterInteger32(MgGuardDisposable):
    """ MgCoordinateSystemFilterInteger32(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemFilterInteger32) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemFilterInteger32) -> IntPtr """
        pass

    def IsFilteredOut(self, nValue):
        """ IsFilteredOut(self: MgCoordinateSystemFilterInteger32, nValue: int) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemFormatConverter(MgGuardDisposable):
    """ MgCoordinateSystemFormatConverter(cPtr: IntPtr, cMemoryOwn: bool) """
    def CodeToCode(self, nFormatSource, sCodeSource, nFormatDestination):
        """ CodeToCode(self: MgCoordinateSystemFormatConverter, nFormatSource: int, sCodeSource: str, nFormatDestination: int) -> str """
        pass

    def CodeToDefinition(self, nFormatSource, sCodeSource):
        """ CodeToDefinition(self: MgCoordinateSystemFormatConverter, nFormatSource: int, sCodeSource: str) -> MgCoordinateSystem """
        pass

    def CodeToWkt(self, nFormatSource, sCodeSource, nWktFlavor):
        """ CodeToWkt(self: MgCoordinateSystemFormatConverter, nFormatSource: int, sCodeSource: str, nWktFlavor: int) -> str """
        pass

    def DefinitionToCode(self, pSource, nFormatDestination):
        """ DefinitionToCode(self: MgCoordinateSystemFormatConverter, pSource: MgCoordinateSystem, nFormatDestination: int) -> str """
        pass

    def DefinitionToWkt(self, pSource, nWktFlavor):
        """ DefinitionToWkt(self: MgCoordinateSystemFormatConverter, pSource: MgCoordinateSystem, nWktFlavor: int) -> str """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemFormatConverter) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemFormatConverter) -> IntPtr """
        pass

    def IsCodeInDictionary(self, nFormat, sCode):
        """ IsCodeInDictionary(self: MgCoordinateSystemFormatConverter, nFormat: int, sCode: str) -> bool """
        pass

    def WktToCode(self, nWktFlavor, sWkt, nFormatDestination):
        """ WktToCode(self: MgCoordinateSystemFormatConverter, nWktFlavor: int, sWkt: str, nFormatDestination: int) -> str """
        pass

    def WktToDefinition(self, nWktFlavor, sWkt):
        """ WktToDefinition(self: MgCoordinateSystemFormatConverter, nWktFlavor: int, sWkt: str) -> MgCoordinateSystem """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticAnalyticalTransformationMethod(object):
    """ MgCoordinateSystemGeodeticAnalyticalTransformationMethod() """
    AbridgedMolodensky = 8195
    Bursa = 8199
    FourParameter = 8197
    Frame = 8200
    Geocentric = 8196
    Molodensky = 8194
    MolodenskyBadekas = 8202
    None = 0
    SevenParameter = 8201
    SixParameter = 8198
    ThreeParameter = 8193


class MgCoordinateSystemGeodeticTransformDefParams(MgGuardDisposable):
    """ MgCoordinateSystemGeodeticTransformDefParams(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticTransformDefParams) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticTransformDefParams) -> IntPtr """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystemGeodeticTransformDefParams) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemGeodeticTransformDefParams) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticAnalyticalTransformDefParams(MgCoordinateSystemGeodeticTransformDefParams):
    """ MgCoordinateSystemGeodeticAnalyticalTransformDefParams(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> IntPtr """
        pass

    def GetDeltaX(self):
        """ GetDeltaX(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetDeltaY(self):
        """ GetDeltaY(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetDeltaZ(self):
        """ GetDeltaZ(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetRotateX(self):
        """ GetRotateX(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetRotateY(self):
        """ GetRotateY(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetRotateZ(self):
        """ GetRotateZ(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetScale(self):
        """ GetScale(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetTransformationMethod(self):
        """ GetTransformationMethod(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> int """
        pass

    def GetTranslateX(self):
        """ GetTranslateX(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetTranslateY(self):
        """ GetTranslateY(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def GetTranslateZ(self):
        """ GetTranslateZ(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams) -> float """
        pass

    def SetDeltaX(self, deltaX):
        """ SetDeltaX(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, deltaX: float) """
        pass

    def SetDeltaY(self, deltaY):
        """ SetDeltaY(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, deltaY: float) """
        pass

    def SetDeltaZ(self, deltaZ):
        """ SetDeltaZ(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, deltaZ: float) """
        pass

    def SetRotateX(self, rotateX):
        """ SetRotateX(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, rotateX: float) """
        pass

    def SetRotateY(self, rotateY):
        """ SetRotateY(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, rotateY: float) """
        pass

    def SetRotateZ(self, rotateZ):
        """ SetRotateZ(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, rotateZ: float) """
        pass

    def SetScale(self, scale):
        """ SetScale(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, scale: float) """
        pass

    def SetTransformationMethod(self, analyticalMethodCode):
        """ SetTransformationMethod(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, analyticalMethodCode: int) """
        pass

    def SetTranslateX(self, translateX):
        """ SetTranslateX(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, translateX: float) """
        pass

    def SetTranslateY(self, translateY):
        """ SetTranslateY(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, translateY: float) """
        pass

    def SetTranslateZ(self, translateZ):
        """ SetTranslateZ(self: MgCoordinateSystemGeodeticAnalyticalTransformDefParams, translateZ: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticDirection(object):
    """ MgCoordinateSystemGeodeticDirection() """
    GeodeticDirectionError = -1
    GeodeticDirectionForward = 1
    GeodeticDirectionInverse = 2
    GeodeticDirectionNone = 0


class MgCoordinateSystemGeodeticInterpolationTransformDefParams(MgCoordinateSystemGeodeticTransformDefParams):
    """ MgCoordinateSystemGeodeticInterpolationTransformDefParams(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticInterpolationTransformDefParams) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticInterpolationTransformDefParams) -> IntPtr """
        pass

    def GetFallback(self):
        """ GetFallback(self: MgCoordinateSystemGeodeticInterpolationTransformDefParams) -> str """
        pass

    def GetGridFiles(self):
        """ GetGridFiles(self: MgCoordinateSystemGeodeticInterpolationTransformDefParams) -> MgDisposableCollection """
        pass

    def NewGridFile(self):
        """ NewGridFile(self: MgCoordinateSystemGeodeticInterpolationTransformDefParams) -> MgCoordinateSystemGeodeticTransformGridFile """
        pass

    def SetFallback(self, fallbackTransformation):
        """ SetFallback(self: MgCoordinateSystemGeodeticInterpolationTransformDefParams, fallbackTransformation: str) """
        pass

    def SetGridFiles(self, gridFiles):
        """ SetGridFiles(self: MgCoordinateSystemGeodeticInterpolationTransformDefParams, gridFiles: MgDisposableCollection) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticMultipleRegressionTransformationMethod(object):
    """ MgCoordinateSystemGeodeticMultipleRegressionTransformationMethod() """
    GeneralPolynomialEpsg = 20482
    MultipleRegression = 20481
    None = 0


class MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams(MgCoordinateSystemGeodeticTransformDefParams):
    """ MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) """
        pass

    def GetCoefficientHeight(self, index):
        """ GetCoefficientHeight(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, index: int) -> float """
        pass

    def GetCoefficientLambda(self, index):
        """ GetCoefficientLambda(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, index: int) -> float """
        pass

    def GetCoefficientPhi(self, index):
        """ GetCoefficientPhi(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, index: int) -> float """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> IntPtr """
        pass

    def GetDeltaHeight(self):
        """ GetDeltaHeight(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetDeltaLambda(self):
        """ GetDeltaLambda(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetDeltaPhi(self):
        """ GetDeltaPhi(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetLambdaOffset(self):
        """ GetLambdaOffset(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetNormalizationScale(self):
        """ GetNormalizationScale(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetPhiOffset(self):
        """ GetPhiOffset(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetTestLambda(self):
        """ GetTestLambda(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetTestPhi(self):
        """ GetTestPhi(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def GetTransformationMethod(self):
        """ GetTransformationMethod(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> int """
        pass

    def GetValidation(self):
        """ GetValidation(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams) -> float """
        pass

    def SetCoefficientHeight(self, index, value):
        """ SetCoefficientHeight(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, index: int, value: float) """
        pass

    def SetCoefficientLambda(self, index, value):
        """ SetCoefficientLambda(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, index: int, value: float) """
        pass

    def SetCoefficientPhi(self, index, value):
        """ SetCoefficientPhi(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, index: int, value: float) """
        pass

    def SetDeltaHeight(self, deltaHeight):
        """ SetDeltaHeight(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, deltaHeight: float) """
        pass

    def SetDeltaLambda(self, deltaLambda):
        """ SetDeltaLambda(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, deltaLambda: float) """
        pass

    def SetDeltaPhi(self, deltaPhi):
        """ SetDeltaPhi(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, deltaPhi: float) """
        pass

    def SetLambdaOffset(self, lambdaOffset):
        """ SetLambdaOffset(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, lambdaOffset: float) """
        pass

    def SetNormalizationScale(self, NormalizationScale):
        """ SetNormalizationScale(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, NormalizationScale: float) """
        pass

    def SetPhiOffset(self, phiOffset):
        """ SetPhiOffset(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, phiOffset: float) """
        pass

    def SetTestLambda(self, testLambda):
        """ SetTestLambda(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, testLambda: float) """
        pass

    def SetTestPhi(self, testPhi):
        """ SetTestPhi(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, testPhi: float) """
        pass

    def SetTransformationMethod(self, mulRegTransformationMethod):
        """ SetTransformationMethod(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, mulRegTransformationMethod: int) """
        pass

    def SetValidation(self, validation):
        """ SetValidation(self: MgCoordinateSystemGeodeticMultipleRegressionTransformDefParams, validation: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticPath(MgGuardDisposable):
    """ MgCoordinateSystemGeodeticPath(cPtr: IntPtr, cMemoryOwn: bool) """
    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystemGeodeticPath) -> MgCoordinateSystemGeodeticPath """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticPath) """
        pass

    def GetAccuracy(self):
        """ GetAccuracy(self: MgCoordinateSystemGeodeticPath) -> float """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticPath) -> IntPtr """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgCoordinateSystemGeodeticPath) -> str """
        pass

    def GetEpsgCode(self):
        """ GetEpsgCode(self: MgCoordinateSystemGeodeticPath) -> int """
        pass

    def GetEpsgVariant(self):
        """ GetEpsgVariant(self: MgCoordinateSystemGeodeticPath) -> int """
        pass

    def GetGroup(self):
        """ GetGroup(self: MgCoordinateSystemGeodeticPath) -> str """
        pass

    def GetIsReversible(self):
        """ GetIsReversible(self: MgCoordinateSystemGeodeticPath) -> bool """
        pass

    def GetPathElements(self):
        """ GetPathElements(self: MgCoordinateSystemGeodeticPath) -> MgDisposableCollection """
        pass

    def GetPathName(self):
        """ GetPathName(self: MgCoordinateSystemGeodeticPath) -> str """
        pass

    def GetSource(self):
        """ GetSource(self: MgCoordinateSystemGeodeticPath) -> str """
        pass

    def GetSourceDatum(self):
        """ GetSourceDatum(self: MgCoordinateSystemGeodeticPath) -> str """
        pass

    def GetTargetDatum(self):
        """ GetTargetDatum(self: MgCoordinateSystemGeodeticPath) -> str """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystemGeodeticPath) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemGeodeticPath) -> bool """
        pass

    def NewPathElement(self):
        """ NewPathElement(self: MgCoordinateSystemGeodeticPath) -> MgCoordinateSystemGeodeticPathElement """
        pass

    def SetAccuracy(self, accuracy):
        """ SetAccuracy(self: MgCoordinateSystemGeodeticPath, accuracy: float) """
        pass

    def SetDescription(self, sDescription):
        """ SetDescription(self: MgCoordinateSystemGeodeticPath, sDescription: str) """
        pass

    def SetEpsgCode(self, epsgCode):
        """ SetEpsgCode(self: MgCoordinateSystemGeodeticPath, epsgCode: int) """
        pass

    def SetEpsgVariant(self, epsgVariant):
        """ SetEpsgVariant(self: MgCoordinateSystemGeodeticPath, epsgVariant: int) """
        pass

    def SetGroup(self, sGroup):
        """ SetGroup(self: MgCoordinateSystemGeodeticPath, sGroup: str) """
        pass

    def SetIsReversible(self, isReversible):
        """ SetIsReversible(self: MgCoordinateSystemGeodeticPath, isReversible: bool) """
        pass

    def SetPathElements(self, pathElements):
        """ SetPathElements(self: MgCoordinateSystemGeodeticPath, pathElements: MgDisposableCollection) """
        pass

    def SetPathName(self, sName):
        """ SetPathName(self: MgCoordinateSystemGeodeticPath, sName: str) """
        pass

    def SetSource(self, sSource):
        """ SetSource(self: MgCoordinateSystemGeodeticPath, sSource: str) """
        pass

    def SetSourceDatum(self, sSourceDatum):
        """ SetSourceDatum(self: MgCoordinateSystemGeodeticPath, sSourceDatum: str) """
        pass

    def SetTargetDatum(self, sTargetDatum):
        """ SetTargetDatum(self: MgCoordinateSystemGeodeticPath, sTargetDatum: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Accuracy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Accuracy(self: MgCoordinateSystemGeodeticPath) -> float

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgCoordinateSystemGeodeticPath) -> str

"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Group(self: MgCoordinateSystemGeodeticPath) -> str

"""

    Source = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Source(self: MgCoordinateSystemGeodeticPath) -> str

"""

    SourceDatum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SourceDatum(self: MgCoordinateSystemGeodeticPath) -> str

"""

    TargetDatum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TargetDatum(self: MgCoordinateSystemGeodeticPath) -> str

"""


    swigCMemOwn = None


class MgCoordinateSystemGeodeticPathDictionary(MgCoordinateSystemDictionaryBase):
    """ MgCoordinateSystemGeodeticPathDictionary(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticPathDictionary) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticPathDictionary) -> IntPtr """
        pass

    def GetGeodeticPath(self, pathName):
        """ GetGeodeticPath(self: MgCoordinateSystemGeodeticPathDictionary, pathName: str) -> MgCoordinateSystemGeodeticPath """
        pass

    def NewGeodeticPath(self):
        """ NewGeodeticPath(self: MgCoordinateSystemGeodeticPathDictionary) -> MgCoordinateSystemGeodeticPath """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticPathElement(MgGuardDisposable):
    """ MgCoordinateSystemGeodeticPathElement(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticPathElement) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticPathElement) -> IntPtr """
        pass

    def GetIsInversed(self):
        """ GetIsInversed(self: MgCoordinateSystemGeodeticPathElement) -> bool """
        pass

    def GetTransformName(self):
        """ GetTransformName(self: MgCoordinateSystemGeodeticPathElement) -> str """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystemGeodeticPathElement) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemGeodeticPathElement) -> bool """
        pass

    def SetIsInversed(self, bInversed):
        """ SetIsInversed(self: MgCoordinateSystemGeodeticPathElement, bInversed: bool) """
        pass

    def SetTransformName(self, name):
        """ SetTransformName(self: MgCoordinateSystemGeodeticPathElement, name: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticStandaloneTransformationMethod(object):
    """ MgCoordinateSystemGeodeticStandaloneTransformationMethod() """
    None = 0
    NullX = 4097
    Wgs72 = 4098


class MgCoordinateSystemGeodeticStandaloneTransformDefParams(MgCoordinateSystemGeodeticTransformDefParams):
    """ MgCoordinateSystemGeodeticStandaloneTransformDefParams(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticStandaloneTransformDefParams) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticStandaloneTransformDefParams) -> IntPtr """
        pass

    def GetTransformationMethod(self):
        """ GetTransformationMethod(self: MgCoordinateSystemGeodeticStandaloneTransformDefParams) -> int """
        pass

    def SetTransformationMethod(self, builtInTransformationMethod):
        """ SetTransformationMethod(self: MgCoordinateSystemGeodeticStandaloneTransformDefParams, builtInTransformationMethod: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    TransformationMethod = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TransformationMethod(self: MgCoordinateSystemGeodeticStandaloneTransformDefParams) -> int

Set: TransformationMethod(self: MgCoordinateSystemGeodeticStandaloneTransformDefParams) = value
"""


    swigCMemOwn = None


class MgCoordinateSystemGeodeticTransformation(MgGuardDisposable):
    """ MgCoordinateSystemGeodeticTransformation(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticTransformation) """
        pass

    def GetBursaWolfeTransformBwScale(self):
        """ GetBursaWolfeTransformBwScale(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetBursaWolfeTransformRotationX(self):
        """ GetBursaWolfeTransformRotationX(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetBursaWolfeTransformRotationY(self):
        """ GetBursaWolfeTransformRotationY(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetBursaWolfeTransformRotationZ(self):
        """ GetBursaWolfeTransformRotationZ(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetBwScaleMax(self):
        """ GetBwScaleMax(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetBwScaleMin(self):
        """ GetBwScaleMin(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticTransformation) -> IntPtr """
        pass

    def GetGeodeticTransformationMethod(self):
        """ GetGeodeticTransformationMethod(self: MgCoordinateSystemGeodeticTransformation) -> int """
        pass

    def GetMaxOffset(self):
        """ GetMaxOffset(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetMaxRotation(self):
        """ GetMaxRotation(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetOffsetX(self):
        """ GetOffsetX(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetOffsetY(self):
        """ GetOffsetY(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetOffsetZ(self):
        """ GetOffsetZ(self: MgCoordinateSystemGeodeticTransformation) -> float """
        pass

    def GetSource(self):
        """ GetSource(self: MgCoordinateSystemGeodeticTransformation) -> MgCoordinateSystemDatum """
        pass

    def GetTarget(self):
        """ GetTarget(self: MgCoordinateSystemGeodeticTransformation) -> MgCoordinateSystemDatum """
        pass

    def IsLegalBwScale(self, dBwScale):
        """ IsLegalBwScale(self: MgCoordinateSystemGeodeticTransformation, dBwScale: float) -> bool """
        pass

    def IsLegalOffset(self, dOffset):
        """ IsLegalOffset(self: MgCoordinateSystemGeodeticTransformation, dOffset: float) -> bool """
        pass

    def IsLegalRotation(self, dRotation):
        """ IsLegalRotation(self: MgCoordinateSystemGeodeticTransformation, dRotation: float) -> bool """
        pass

    def SetBursaWolfeTransform(self, dRotationX, dRotationY, dRotationZ, dBwScale):
        """ SetBursaWolfeTransform(self: MgCoordinateSystemGeodeticTransformation, dRotationX: float, dRotationY: float, dRotationZ: float, dBwScale: float) """
        pass

    def SetGeodeticTransformationMethod(self, nGeodeticTransformationMethod):
        """ SetGeodeticTransformationMethod(self: MgCoordinateSystemGeodeticTransformation, nGeodeticTransformationMethod: int) """
        pass

    def SetOffset(self, x, y, z):
        """ SetOffset(self: MgCoordinateSystemGeodeticTransformation, x: float, y: float, z: float) """
        pass

    def SetSourceAndTarget(self, pSource, pTarget):
        """ SetSourceAndTarget(self: MgCoordinateSystemGeodeticTransformation, pSource: MgCoordinateSystemDatum, pTarget: MgCoordinateSystemDatum) """
        pass

    def Shift(self, *__args):
        """
        Shift(self: MgCoordinateSystemGeodeticTransformation, dLongitude: float, dLatitude: float, dZ: float) -> MgCoordinate
        Shift(self: MgCoordinateSystemGeodeticTransformation, dLongitude: float, dLatitude: float) -> MgCoordinate
        Shift(self: MgCoordinateSystemGeodeticTransformation, pLonLat: MgCoordinate)
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticTransformationMethod(object):
    """ MgCoordinateSystemGeodeticTransformationMethod() """
    AGD66 = 10
    AGD84 = 14
    ATS77 = 16
    Bursa = 3
    CHENYX = 26
    CSRS = 19
    DHDN = 23
    ED50 = 22
    ETRF89 = 24
    FourParameter = 13
    GDA94 = 17
    Geocentric = 25
    HPGN = 8
    Lclgrf = 99
    Molodensky = 1
    MReg = 2
    NAD27 = 4
    NAD83 = 5
    None = 0
    NZGD2K = 18
    NZGD49 = 15
    RGF93 = 21
    SevenParameter = 9
    SixParameter = 12
    ThreeParameter = 11
    TOKYO = 20
    WGS72 = 7
    WGS84 = 6


class MgCoordinateSystemGeodeticTransformDef(MgGuardDisposable):
    """ MgCoordinateSystemGeodeticTransformDef(cPtr: IntPtr, cMemoryOwn: bool) """
    def CreateClone(self):
        """ CreateClone(self: MgCoordinateSystemGeodeticTransformDef) -> MgCoordinateSystemGeodeticTransformDef """
        pass

    def CreateTransformation(self, createInverse):
        """ CreateTransformation(self: MgCoordinateSystemGeodeticTransformDef, createInverse: bool) -> MgCoordinateSystemGeodeticTransformation """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticTransformDef) """
        pass

    def GetAccuracy(self):
        """ GetAccuracy(self: MgCoordinateSystemGeodeticTransformDef) -> float """
        pass

    def GetConvergenceValue(self):
        """ GetConvergenceValue(self: MgCoordinateSystemGeodeticTransformDef) -> float """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticTransformDef) -> IntPtr """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgCoordinateSystemGeodeticTransformDef) -> str """
        pass

    def GetEpsgCode(self):
        """ GetEpsgCode(self: MgCoordinateSystemGeodeticTransformDef) -> int """
        pass

    def GetEpsgVariation(self):
        """ GetEpsgVariation(self: MgCoordinateSystemGeodeticTransformDef) -> int """
        pass

    def GetErrorValue(self):
        """ GetErrorValue(self: MgCoordinateSystemGeodeticTransformDef) -> float """
        pass

    def GetGroup(self):
        """ GetGroup(self: MgCoordinateSystemGeodeticTransformDef) -> str """
        pass

    def GetInverseSupported(self):
        """ GetInverseSupported(self: MgCoordinateSystemGeodeticTransformDef) -> bool """
        pass

    def GetMaxIterations(self):
        """ GetMaxIterations(self: MgCoordinateSystemGeodeticTransformDef) -> int """
        pass

    def GetParameters(self):
        """ GetParameters(self: MgCoordinateSystemGeodeticTransformDef) -> MgCoordinateSystemGeodeticTransformDefParams """
        pass

    def GetRangeMaxLatitude(self):
        """ GetRangeMaxLatitude(self: MgCoordinateSystemGeodeticTransformDef) -> float """
        pass

    def GetRangeMaxLongitude(self):
        """ GetRangeMaxLongitude(self: MgCoordinateSystemGeodeticTransformDef) -> float """
        pass

    def GetRangeMinLatitude(self):
        """ GetRangeMinLatitude(self: MgCoordinateSystemGeodeticTransformDef) -> float """
        pass

    def GetRangeMinLongitude(self):
        """ GetRangeMinLongitude(self: MgCoordinateSystemGeodeticTransformDef) -> float """
        pass

    def GetSource(self):
        """ GetSource(self: MgCoordinateSystemGeodeticTransformDef) -> str """
        pass

    def GetSourceDatum(self):
        """ GetSourceDatum(self: MgCoordinateSystemGeodeticTransformDef) -> str """
        pass

    def GetTargetDatum(self):
        """ GetTargetDatum(self: MgCoordinateSystemGeodeticTransformDef) -> str """
        pass

    def GetTransformDefType(self):
        """ GetTransformDefType(self: MgCoordinateSystemGeodeticTransformDef) -> int """
        pass

    def GetTransformName(self):
        """ GetTransformName(self: MgCoordinateSystemGeodeticTransformDef) -> str """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystemGeodeticTransformDef) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemGeodeticTransformDef) -> bool """
        pass

    def SetAccuracy(self, accuracy):
        """ SetAccuracy(self: MgCoordinateSystemGeodeticTransformDef, accuracy: float) """
        pass

    def SetConvergenceValue(self, convergenceValue):
        """ SetConvergenceValue(self: MgCoordinateSystemGeodeticTransformDef, convergenceValue: float) """
        pass

    def SetDescription(self, description):
        """ SetDescription(self: MgCoordinateSystemGeodeticTransformDef, description: str) """
        pass

    def SetEpsgCode(self, epsgCode):
        """ SetEpsgCode(self: MgCoordinateSystemGeodeticTransformDef, epsgCode: int) """
        pass

    def SetEpsgVariation(self, epsgVariation):
        """ SetEpsgVariation(self: MgCoordinateSystemGeodeticTransformDef, epsgVariation: int) """
        pass

    def SetErrorValue(self, errorValue):
        """ SetErrorValue(self: MgCoordinateSystemGeodeticTransformDef, errorValue: float) """
        pass

    def SetGroup(self, group):
        """ SetGroup(self: MgCoordinateSystemGeodeticTransformDef, group: str) """
        pass

    def SetInverseSupported(self, inverseSupported):
        """ SetInverseSupported(self: MgCoordinateSystemGeodeticTransformDef, inverseSupported: bool) """
        pass

    def SetMaxIterations(self, maxIterations):
        """ SetMaxIterations(self: MgCoordinateSystemGeodeticTransformDef, maxIterations: int) """
        pass

    def SetParameters(self, parameters):
        """ SetParameters(self: MgCoordinateSystemGeodeticTransformDef, parameters: MgCoordinateSystemGeodeticTransformDefParams) """
        pass

    def SetRangeMaxLatitude(self, maxLat):
        """ SetRangeMaxLatitude(self: MgCoordinateSystemGeodeticTransformDef, maxLat: float) """
        pass

    def SetRangeMaxLongitude(self, maxLong):
        """ SetRangeMaxLongitude(self: MgCoordinateSystemGeodeticTransformDef, maxLong: float) """
        pass

    def SetRangeMinLatitude(self, minLat):
        """ SetRangeMinLatitude(self: MgCoordinateSystemGeodeticTransformDef, minLat: float) """
        pass

    def SetRangeMinLongitude(self, minLong):
        """ SetRangeMinLongitude(self: MgCoordinateSystemGeodeticTransformDef, minLong: float) """
        pass

    def SetSource(self, source):
        """ SetSource(self: MgCoordinateSystemGeodeticTransformDef, source: str) """
        pass

    def SetSourceDatum(self, datumKey):
        """ SetSourceDatum(self: MgCoordinateSystemGeodeticTransformDef, datumKey: str) """
        pass

    def SetTargetDatum(self, datumKey):
        """ SetTargetDatum(self: MgCoordinateSystemGeodeticTransformDef, datumKey: str) """
        pass

    def SetTransformName(self, name):
        """ SetTransformName(self: MgCoordinateSystemGeodeticTransformDef, name: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticTransformDefDictionary(MgCoordinateSystemDictionaryBase):
    """ MgCoordinateSystemGeodeticTransformDefDictionary(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticTransformDefDictionary) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticTransformDefDictionary) -> IntPtr """
        pass

    def GetGeodeticTransformationDef(self, transformationName):
        """ GetGeodeticTransformationDef(self: MgCoordinateSystemGeodeticTransformDefDictionary, transformationName: str) -> MgCoordinateSystemGeodeticTransformDef """
        pass

    def NewGeodeticTransformationDef(self, transformationDefType):
        """ NewGeodeticTransformationDef(self: MgCoordinateSystemGeodeticTransformDefDictionary, transformationDefType: int) -> MgCoordinateSystemGeodeticTransformDef """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticTransformDefType(object):
    """ MgCoordinateSystemGeodeticTransformDefType() """
    Analytical = 2
    Interpolation = 3
    MultipleRegression = 4
    None = 0
    Standalone = 1


class MgCoordinateSystemGeodeticTransformGridFile(MgGuardDisposable):
    """ MgCoordinateSystemGeodeticTransformGridFile(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGeodeticTransformGridFile) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGeodeticTransformGridFile) -> IntPtr """
        pass

    def GetFileFormat(self):
        """ GetFileFormat(self: MgCoordinateSystemGeodeticTransformGridFile) -> int """
        pass

    def GetFileName(self):
        """ GetFileName(self: MgCoordinateSystemGeodeticTransformGridFile) -> str """
        pass

    def GetIsInverseDirection(self):
        """ GetIsInverseDirection(self: MgCoordinateSystemGeodeticTransformGridFile) -> bool """
        pass

    def IsProtected(self):
        """ IsProtected(self: MgCoordinateSystemGeodeticTransformGridFile) -> bool """
        pass

    def IsValid(self):
        """ IsValid(self: MgCoordinateSystemGeodeticTransformGridFile) -> bool """
        pass

    def SetFileFormat(self, gridFileFormat):
        """ SetFileFormat(self: MgCoordinateSystemGeodeticTransformGridFile, gridFileFormat: int) """
        pass

    def SetFileName(self, fileName):
        """ SetFileName(self: MgCoordinateSystemGeodeticTransformGridFile, fileName: str) """
        pass

    def SetIsInverseDirection(self, isInverseDirection):
        """ SetIsInverseDirection(self: MgCoordinateSystemGeodeticTransformGridFile, isInverseDirection: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGeodeticTransformGridFileFormat(object):
    """ MgCoordinateSystemGeodeticTransformGridFileFormat() """
    ATS77 = 6
    GEOCON = 9
    NADCON = 3
    None = 0
    NTv1 = 1
    NTv2 = 2
    PAR = 5
    RGF = 4


class MgCoordinateSystemGridBase(MgGuardDisposable):
    """ MgCoordinateSystemGridBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def ApproxGridLineMemoryUsage(self, specification):
        """ ApproxGridLineMemoryUsage(self: MgCoordinateSystemGridBase, specification: MgCoordinateSystemGridSpecification) -> int """
        pass

    def ApproxGridRegionMemoryUsage(self, specification):
        """ ApproxGridRegionMemoryUsage(self: MgCoordinateSystemGridBase, specification: MgCoordinateSystemGridSpecification) -> int """
        pass

    def ApproxGridTickMemoryUsage(self, specification):
        """ ApproxGridTickMemoryUsage(self: MgCoordinateSystemGridBase, specification: MgCoordinateSystemGridSpecification) -> int """
        pass

    def AreExceptionsOn(self):
        """ AreExceptionsOn(self: MgCoordinateSystemGridBase) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridBase) """
        pass

    def GetBoundary(self):
        """ GetBoundary(self: MgCoordinateSystemGridBase) -> MgCoordinateSystemGridBoundary """
        pass

    def GetConvergenceAngle(self, location):
        """ GetConvergenceAngle(self: MgCoordinateSystemGridBase, location: MgCoordinate) -> float """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridBase) -> IntPtr """
        pass

    def GetGridLines(self, specification):
        """ GetGridLines(self: MgCoordinateSystemGridBase, specification: MgCoordinateSystemGridSpecification) -> MgCoordinateSystemGridLineCollection """
        pass

    def GetGridRegions(self, specification):
        """ GetGridRegions(self: MgCoordinateSystemGridBase, specification: MgCoordinateSystemGridSpecification) -> MgCoordinateSystemGridRegionCollection """
        pass

    def GetGridTicks(self, specification):
        """ GetGridTicks(self: MgCoordinateSystemGridBase, specification: MgCoordinateSystemGridSpecification) -> MgCoordinateSystemGridTickCollection """
        pass

    def GetLastError(self):
        """ GetLastError(self: MgCoordinateSystemGridBase) -> int """
        pass

    def GetProjectiveGridScale(self, location):
        """ GetProjectiveGridScale(self: MgCoordinateSystemGridBase, location: MgCoordinate) -> float """
        pass

    def GetSpecializationType(self):
        """ GetSpecializationType(self: MgCoordinateSystemGridBase) -> int """
        pass

    def ResetLastError(self):
        """ ResetLastError(self: MgCoordinateSystemGridBase) """
        pass

    def SetBoundary(self, pGridBoundary):
        """ SetBoundary(self: MgCoordinateSystemGridBase, pGridBoundary: MgCoordinateSystemGridBoundary) """
        pass

    def SetExceptionsOn(self, bOn):
        """ SetExceptionsOn(self: MgCoordinateSystemGridBase, bOn: bool) """
        pass

    def SetGridLineExceptionLevel(self, memoryUseMax):
        """ SetGridLineExceptionLevel(self: MgCoordinateSystemGridBase, memoryUseMax: int) -> int """
        pass

    def SetGridRegionExceptionLevel(self, memoryUseMax):
        """ SetGridRegionExceptionLevel(self: MgCoordinateSystemGridBase, memoryUseMax: int) -> int """
        pass

    def SetGridTickExceptionLevel(self, memoryUseMax):
        """ SetGridTickExceptionLevel(self: MgCoordinateSystemGridBase, memoryUseMax: int) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridBoundary(MgGuardDisposable):
    """ MgCoordinateSystemGridBoundary(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridBoundary) """
        pass

    def GetBoundary(self):
        """ GetBoundary(self: MgCoordinateSystemGridBoundary) -> MgPolygon """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridBoundary) -> IntPtr """
        pass

    def SetBoundaryExtents(self, *__args):
        """ SetBoundaryExtents(self: MgCoordinateSystemGridBoundary, boundary: MgPolygon)SetBoundaryExtents(self: MgCoordinateSystemGridBoundary, southwest: MgCoordinate, northeast: MgCoordinate) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridLine(MgGuardDisposable):
    """ MgCoordinateSystemGridLine(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridLine) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCoordinateSystemGridLine) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridLine) -> IntPtr """
        pass

    def GetGridOrientation(self):
        """ GetGridOrientation(self: MgCoordinateSystemGridLine) -> int """
        pass

    def GetRealValue(self):
        """ GetRealValue(self: MgCoordinateSystemGridLine) -> float """
        pass

    def GetSegment(self, index):
        """ GetSegment(self: MgCoordinateSystemGridLine, index: int) -> MgLineString """
        pass

    def GetSegmentCollection(self):
        """ GetSegmentCollection(self: MgCoordinateSystemGridLine) -> MgLineStringCollection """
        pass

    def SetSegmentCollection(self, segmentCollection):
        """ SetSegmentCollection(self: MgCoordinateSystemGridLine, segmentCollection: MgLineStringCollection) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridLineCollection(MgGuardDisposable):
    """ MgCoordinateSystemGridLineCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Clear(self):
        """ Clear(self: MgCoordinateSystemGridLineCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridLineCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCoordinateSystemGridLineCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridLineCollection) -> IntPtr """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCoordinateSystemGridLineCollection, index: int) -> MgCoordinateSystemGridLine """
        pass

    def IndexOf(self, gridOrientation, gridValue):
        """ IndexOf(self: MgCoordinateSystemGridLineCollection, gridOrientation: int, gridValue: float) -> int """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCoordinateSystemGridLineCollection, index: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridOrientation(object):
    """ MgCoordinateSystemGridOrientation() """
    EastWest = None
    None = None
    NorthSouth = None
    Unknown = None


class MgCoordinateSystemGridRegion(MgGuardDisposable):
    """ MgCoordinateSystemGridRegion(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridRegion) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridRegion) -> IntPtr """
        pass

    def GetEastLine(self):
        """ GetEastLine(self: MgCoordinateSystemGridRegion) -> MgLineStringCollection """
        pass

    def GetLabel(self):
        """ GetLabel(self: MgCoordinateSystemGridRegion) -> str """
        pass

    def GetNorthLine(self):
        """ GetNorthLine(self: MgCoordinateSystemGridRegion) -> MgLineStringCollection """
        pass

    def GetRegionBoundary(self):
        """ GetRegionBoundary(self: MgCoordinateSystemGridRegion) -> MgPolygon """
        pass

    def GetRegionCenter(self):
        """ GetRegionCenter(self: MgCoordinateSystemGridRegion) -> MgCoordinate """
        pass

    def GetSouthLine(self):
        """ GetSouthLine(self: MgCoordinateSystemGridRegion) -> MgLineStringCollection """
        pass

    def GetWestLine(self):
        """ GetWestLine(self: MgCoordinateSystemGridRegion) -> MgLineStringCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridRegionCollection(MgGuardDisposable):
    """ MgCoordinateSystemGridRegionCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Clear(self):
        """ Clear(self: MgCoordinateSystemGridRegionCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridRegionCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCoordinateSystemGridRegionCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridRegionCollection) -> IntPtr """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCoordinateSystemGridRegionCollection, index: int) -> MgCoordinateSystemGridRegion """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCoordinateSystemGridRegionCollection, index: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridSpecializationType(object):
    """ MgCoordinateSystemGridSpecializationType() """
    Generic = 1
    MGRS = 17
    None = 0
    Unknown = 65366
    USNG = 18


class MgCoordinateSystemGridSpecification(MgGuardDisposable):
    """ MgCoordinateSystemGridSpecification(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridSpecification) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridSpecification) -> IntPtr """
        pass

    def GetCurvePrecision(self):
        """ GetCurvePrecision(self: MgCoordinateSystemGridSpecification) -> float """
        pass

    def GetEastingBase(self):
        """ GetEastingBase(self: MgCoordinateSystemGridSpecification) -> float """
        pass

    def GetEastingIncrement(self):
        """ GetEastingIncrement(self: MgCoordinateSystemGridSpecification) -> float """
        pass

    def GetNorthingBase(self):
        """ GetNorthingBase(self: MgCoordinateSystemGridSpecification) -> float """
        pass

    def GetNorthingIncrement(self):
        """ GetNorthingIncrement(self: MgCoordinateSystemGridSpecification) -> float """
        pass

    def GetTickEastingIncrement(self):
        """ GetTickEastingIncrement(self: MgCoordinateSystemGridSpecification) -> float """
        pass

    def GetTickNorthingIncrement(self):
        """ GetTickNorthingIncrement(self: MgCoordinateSystemGridSpecification) -> float """
        pass

    def GetUnitCode(self):
        """ GetUnitCode(self: MgCoordinateSystemGridSpecification) -> int """
        pass

    def GetUnitType(self):
        """ GetUnitType(self: MgCoordinateSystemGridSpecification) -> int """
        pass

    def IsConsistent(self):
        """ IsConsistent(self: MgCoordinateSystemGridSpecification) -> bool """
        pass

    def IsSameAs(self, specification):
        """ IsSameAs(self: MgCoordinateSystemGridSpecification, specification: MgCoordinateSystemGridSpecification) -> bool """
        pass

    def SetCurvePrecision(self, curvePrecision):
        """ SetCurvePrecision(self: MgCoordinateSystemGridSpecification, curvePrecision: float) """
        pass

    def SetGridBase(self, eastingBase, northingBase):
        """ SetGridBase(self: MgCoordinateSystemGridSpecification, eastingBase: float, northingBase: float) """
        pass

    def SetGridIncrement(self, eastingIncrement, northingIncrement):
        """ SetGridIncrement(self: MgCoordinateSystemGridSpecification, eastingIncrement: float, northingIncrement: float) """
        pass

    def SetMaxCurvePoints(self, maxCurvePoints):
        """ SetMaxCurvePoints(self: MgCoordinateSystemGridSpecification, maxCurvePoints: int) """
        pass

    def SetTickIncrements(self, eastingIncrement, northingIncrement):
        """ SetTickIncrements(self: MgCoordinateSystemGridSpecification, eastingIncrement: float, northingIncrement: float) """
        pass

    def SetUnits(self, unitCode, unitType):
        """ SetUnits(self: MgCoordinateSystemGridSpecification, unitCode: int, unitType: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridTick(MgGuardDisposable):
    """ MgCoordinateSystemGridTick(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridTick) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridTick) -> IntPtr """
        pass

    def GetDirectionVector(self):
        """ GetDirectionVector(self: MgCoordinateSystemGridTick) -> MgCoordinate """
        pass

    def GetIsOnGridLine(self):
        """ GetIsOnGridLine(self: MgCoordinateSystemGridTick) -> bool """
        pass

    def GetPosition(self):
        """ GetPosition(self: MgCoordinateSystemGridTick) -> MgCoordinate """
        pass

    def GetTickOrientation(self):
        """ GetTickOrientation(self: MgCoordinateSystemGridTick) -> int """
        pass

    def GetValue(self):
        """ GetValue(self: MgCoordinateSystemGridTick) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemGridTickCollection(MgGuardDisposable):
    """ MgCoordinateSystemGridTickCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Clear(self):
        """ Clear(self: MgCoordinateSystemGridTickCollection) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemGridTickCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCoordinateSystemGridTickCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemGridTickCollection) -> IntPtr """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCoordinateSystemGridTickCollection, index: int) -> MgCoordinateSystemGridTick """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCoordinateSystemGridTickCollection, index: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemInitializationFailedException(MgApplicationException):
    """
    MgCoordinateSystemInitializationFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateSystemInitializationFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemInitializationFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemInitializationFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemLoadFailedException(MgApplicationException):
    """
    MgCoordinateSystemLoadFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateSystemLoadFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemLoadFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemLoadFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemMathComparator(MgGuardDisposable):
    """ MgCoordinateSystemMathComparator(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemMathComparator) """
        pass

    def GetCompareInternalDatumOldParameters(self):
        """ GetCompareInternalDatumOldParameters(self: MgCoordinateSystemMathComparator) -> bool """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemMathComparator) -> IntPtr """
        pass

    def Same(self, pDefinition1, pDefinition2):
        """ Same(self: MgCoordinateSystemMathComparator, pDefinition1: MgGuardDisposable, pDefinition2: MgGuardDisposable) -> bool """
        pass

    def SameCoordinateSystem(self, pDefinition1, pDefinition2):
        """ SameCoordinateSystem(self: MgCoordinateSystemMathComparator, pDefinition1: MgCoordinateSystem, pDefinition2: MgCoordinateSystem) -> bool """
        pass

    def SameDatum(self, pDefinition1, pDefinition2):
        """ SameDatum(self: MgCoordinateSystemMathComparator, pDefinition1: MgCoordinateSystemDatum, pDefinition2: MgCoordinateSystemDatum) -> bool """
        pass

    def SameEllipsoid(self, pDefinition1, pDefinition2):
        """ SameEllipsoid(self: MgCoordinateSystemMathComparator, pDefinition1: MgCoordinateSystemEllipsoid, pDefinition2: MgCoordinateSystemEllipsoid) -> bool """
        pass

    def SetCompareInternalDatumOldParameters(self, arg0):
        """ SetCompareInternalDatumOldParameters(self: MgCoordinateSystemMathComparator, arg0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgMeasure(MgGuardDisposable):
    """ MgMeasure(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgMeasure) """
        pass

    def GetAzimuth(self, coord1, coord2):
        """ GetAzimuth(self: MgMeasure, coord1: MgCoordinate, coord2: MgCoordinate) -> float """
        pass

    def GetCoordinate(self, coord, azimuth, distance):
        """ GetCoordinate(self: MgMeasure, coord: MgCoordinate, azimuth: float, distance: float) -> MgCoordinate """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMeasure) -> IntPtr """
        pass

    def GetDistance(self, coord1, coord2):
        """ GetDistance(self: MgMeasure, coord1: MgCoordinate, coord2: MgCoordinate) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemMeasure(MgMeasure):
    """ MgCoordinateSystemMeasure(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemMeasure) """
        pass

    def GetAzimuth(self, *__args):
        """
        GetAzimuth(self: MgCoordinateSystemMeasure, x1: float, y1: float, x2: float, y2: float) -> float
        GetAzimuth(self: MgCoordinateSystemMeasure, coord1: MgCoordinate, coord2: MgCoordinate) -> float
        """
        pass

    def GetCoordinate(self, *__args):
        """
        GetCoordinate(self: MgCoordinateSystemMeasure, xStart: float, yStart: float, azimuth: float, distance: float) -> MgCoordinate
        GetCoordinate(self: MgCoordinateSystemMeasure, coord: MgCoordinate, azimuth: float, distance: float) -> MgCoordinate
        """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemMeasure) -> IntPtr """
        pass

    def GetDistance(self, *__args):
        """
        GetDistance(self: MgCoordinateSystemMeasure, x1: float, y1: float, x2: float, y2: float) -> float
        GetDistance(self: MgCoordinateSystemMeasure, coord1: MgCoordinate, coord2: MgCoordinate) -> float
        """
        pass

    def GetEnvelope(self):
        """ GetEnvelope(self: MgCoordinateSystemMeasure) -> MgEnvelope """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Envelope = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Envelope(self: MgCoordinateSystemMeasure) -> MgEnvelope

"""


    swigCMemOwn = None


class MgCoordinateSystemMeasureFailedException(MgApplicationException):
    """
    MgCoordinateSystemMeasureFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateSystemMeasureFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemMeasureFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemMeasureFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemMgrs(MgCoordinateSystemGridBase):
    """ MgCoordinateSystemMgrs(cPtr: IntPtr, cMemoryOwn: bool) """
    def ConvertFromLonLat(self, *__args):
        """
        ConvertFromLonLat(self: MgCoordinateSystemMgrs, pLonLat: MgCoordinate, nPrecision: int) -> str
        ConvertFromLonLat(self: MgCoordinateSystemMgrs, dLongitude: float, dLatitude: float, nPrecision: int) -> str
        """
        pass

    def ConvertToLonLat(self, sMgrs, grdSqrPosition=None):
        """
        ConvertToLonLat(self: MgCoordinateSystemMgrs, sMgrs: str, grdSqrPosition: int) -> MgCoordinate
        ConvertToLonLat(self: MgCoordinateSystemMgrs, sMgrs: str) -> MgCoordinate
        """
        pass

    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemMgrs) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemMgrs) -> IntPtr """
        pass

    def GetLetteringScheme(self):
        """ GetLetteringScheme(self: MgCoordinateSystemMgrs) -> Int16 """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemMgrsGridLevel(object):
    """ MgCoordinateSystemMgrsGridLevel() """
    Mgrs100Km = 3
    Mgrs100m = 6
    Mgrs10Km = 4
    Mgrs10m = 7
    Mgrs1Km = 5
    Mgrs1m = 8
    MgrsNone = 0
    MgrsUnknown = 99
    MgrsUps = 2
    MgrsUtm = 1


class MgCoordinateSystemMgrsGridSquarePosition(object):
    """ MgCoordinateSystemMgrsGridSquarePosition() """
    Center = 1
    East = 7
    None = 0
    North = 5
    NorthEast = 6
    NorthWest = 4
    South = 9
    SouthEast = 8
    SouthWest = 2
    Unknown = 10
    West = 3


class MgCoordinateSystemMgrsLetteringScheme(object):
    """ MgCoordinateSystemMgrsLetteringScheme() """
    Alternative = None
    Normal = None


class MgCoordinateSystemProjectionCode(object):
    """ MgCoordinateSystemProjectionCode() """
    Alber = 4
    Azede = 59
    Azmea = 11
    Azmed = 7
    Bipolar = 31
    Bonne = 24
    Cassini = 22
    Eckert4 = 25
    Eckert6 = 26
    Edcnc = 12
    Edcyl = 20
    EdcylE = 67
    GaussK = 46
    Gnomonic = 19
    Goode = 28
    Hom1uv = 1281
    Hom1xy = 1282
    Hom2uv = 1283
    Hom2xy = 1284
    Krovak = 47
    Krvk95 = 51
    LL = 1
    Lm1sp = 36
    Lm2sp = 37
    Lmblg = 38
    Lmbrtaf = 65
    LmMich = 70
    Lmtan = 8
    Miller = 13
    Mndotl = 41
    Mndott = 42
    Modpc = 10
    Mollweid = 27
    Mrcat = 6
    MrcatK = 49
    Mstero = 15
    Neacyl = 29
    Nerth = 55
    Nrthsrt = 64
    Nzealand = 16
    OblqM = 5
    Obqcyl = 56
    Ortho = 18
    Ostn02 = 60
    Ostn97 = 58
    Ostro = 34
    PlateCarree = 68
    Plycn = 9
    Pstro = 33
    Pstrosl = 53
    PvMercator = 69
    Robinson = 23
    Rskew = 1285
    Rskewc = 1286
    Rskewo = 1287
    Sinus = 17
    Sotrm = 43
    Sstro = 35
    Swiss = 32
    Sys34 = 57
    Sys34_01 = 66
    Sys34_99 = 61
    Teacyl = 30
    Tm = 3
    Trmeraf = 54
    Trmrkrg = 62
    Trmrs = 45
    Unknown = 0
    Utm = 44
    Vdgrntn = 21
    Wccsl = 39
    Wccst = 40
    Winkl = 63


class MgCoordinateSystemProjectionFormatType(object):
    """ MgCoordinateSystemProjectionFormatType() """
    Angd = 32933
    Coef = 13
    Lat = 41157
    Lng = 57509
    None = 0
    Rot = 4
    Scl = 7
    Xxx = 4099
    Yyy = 4099


class MgCoordinateSystemProjectionInformation(MgGuardDisposable):
    """ MgCoordinateSystemProjectionInformation(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemProjectionInformation) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemProjectionInformation) -> IntPtr """
        pass

    def GetEnumProjections(self):
        """ GetEnumProjections(self: MgCoordinateSystemProjectionInformation) -> MgCoordinateSystemEnumInteger32 """
        pass

    def GetParameterCount(self, nProjectionCode):
        """ GetParameterCount(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> int """
        pass

    def GetParameterDefault(self, nProjectionCode, ulIndex):
        """ GetParameterDefault(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int, ulIndex: int) -> float """
        pass

    def GetParameterFormatType(self, nProjectionCode, ulIndex):
        """ GetParameterFormatType(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int, ulIndex: int) -> int """
        pass

    def GetParameterLogicalType(self, nProjectionCode, ulIndex):
        """ GetParameterLogicalType(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int, ulIndex: int) -> int """
        pass

    def GetParameterMax(self, nProjectionCode, ulIndex):
        """ GetParameterMax(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int, ulIndex: int) -> float """
        pass

    def GetParameterMin(self, nProjectionCode, ulIndex):
        """ GetParameterMin(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int, ulIndex: int) -> float """
        pass

    def GetParameterType(self, nProjectionCode, ulIndex):
        """ GetParameterType(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int, ulIndex: int) -> int """
        pass

    def GetTagString(self, nProjectionCode):
        """ GetTagString(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> str """
        pass

    def GetUnitType(self, nProjectionCode):
        """ GetUnitType(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> int """
        pass

    def IsUsingOffset(self, nProjectionCode):
        """ IsUsingOffset(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> bool """
        pass

    def IsUsingOriginLatitude(self, nProjectionCode):
        """ IsUsingOriginLatitude(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> bool """
        pass

    def IsUsingOriginLongitude(self, nProjectionCode):
        """ IsUsingOriginLongitude(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> bool """
        pass

    def IsUsingParameter(self, nProjectionCode, ulIndex):
        """ IsUsingParameter(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int, ulIndex: int) -> bool """
        pass

    def IsUsingQuadrant(self, nProjectionCode):
        """ IsUsingQuadrant(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> bool """
        pass

    def IsUsingScaleReduction(self, nProjectionCode):
        """ IsUsingScaleReduction(self: MgCoordinateSystemProjectionInformation, nProjectionCode: int) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemProjectionLogicalType(object):
    """ MgCoordinateSystemProjectionLogicalType() """
    AffineCoefficient = 10
    AngularDistance = 4
    Azimuth = 3
    ComplexCoefficient = 5
    Elevation = 9
    GeoidHeight = 8
    HemisphereSelection = 7
    Latitude = 2
    Longitude = 1
    None = 0
    Scale = 12
    UTMZoneNumber = 6
    XYCoordinate = 11


class MgCoordinateSystemProjectionParameterType(object):
    """ MgCoordinateSystemProjectionParameterType() """
    Adp1p2 = 20
    Adsp1 = 21
    Adsp2 = 22
    Aelev = 30
    Afa0 = 35
    Afa1 = 37
    Afa2 = 38
    Afb0 = 36
    Afb1 = 39
    Afb2 = 40
    Cmplxan = 23
    Cmplxbn = 24
    Cntmer = 1
    Denrgn = 42
    Eastll = 26
    EllipsoidScale = 48
    Estdmer = 13
    Gcazm = 11
    Gcp1lat = 6
    Gcp1lng = 5
    Gcp2lat = 8
    Gcp2lng = 7
    Gcplat = 10
    Gcplng = 9
    Ghgt = 29
    Hsns = 28
    NotUsed = 0
    Nparall = 14
    Nrmlpll = 41
    Nrthrot = 47
    Nrthscl = 46
    Nstdpll = 2
    Ostdpll = 33
    P1lat = 17
    P1lng = 16
    P2lat = 19
    P2lng = 18
    Polelat = 32
    Polelng = 31
    Sclrotorgx = 44
    Sclrotorgy = 45
    Skwazm = 43
    Sparall = 15
    Sstdpll = 3
    Stdcir = 34
    Stdpll = 4
    Utmzn = 27
    Westll = 25
    Yaxisaz = 12


class MgTransform(MgGuardDisposable):
    """ MgTransform(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgTransform) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgTransform) -> IntPtr """
        pass

    def Transform(self, *__args):
        """
        Transform(self: MgTransform, coordinate: MgCoordinate) -> MgCoordinate
        Transform(self: MgTransform, envelope: MgEnvelope) -> MgEnvelope
        Transform(self: MgTransform, x: float, y: float) -> MgCoordinate
        Transform(self: MgTransform, x: float, y: float, z: float) -> MgCoordinate
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemTransform(MgTransform):
    """ MgCoordinateSystemTransform(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemTransform) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemTransform) -> IntPtr """
        pass

    def GetdatumWarningCount(self):
        """ GetdatumWarningCount(self: MgCoordinateSystemTransform) -> int """
        pass

    def GetExplicitGeodeticPath(self):
        """ GetExplicitGeodeticPath(self: MgCoordinateSystemTransform) -> MgCoordinateSystemGeodeticPath """
        pass

    def GetGeodeticTransformation(self, index):
        """ GetGeodeticTransformation(self: MgCoordinateSystemTransform, index: int) -> MgCoordinateSystemGeodeticTransformDef """
        pass

    def GetGeodeticTransformationCount(self):
        """ GetGeodeticTransformationCount(self: MgCoordinateSystemTransform) -> int """
        pass

    def GetGeodeticTransformationDirection(self, index):
        """ GetGeodeticTransformationDirection(self: MgCoordinateSystemTransform, index: int) -> int """
        pass

    def GetLastTransformStatus(self):
        """ GetLastTransformStatus(self: MgCoordinateSystemTransform) -> int """
        pass

    def GetSource(self):
        """ GetSource(self: MgCoordinateSystemTransform) -> MgCoordinateSystem """
        pass

    def GetSourceWarningCount(self):
        """ GetSourceWarningCount(self: MgCoordinateSystemTransform) -> int """
        pass

    def GetTarget(self):
        """ GetTarget(self: MgCoordinateSystemTransform) -> MgCoordinateSystem """
        pass

    def GetTargetWarningCount(self):
        """ GetTargetWarningCount(self: MgCoordinateSystemTransform) -> int """
        pass

    def GridLine(self, fromPnt, toPnt, curvePrecision, maxPoints):
        """ GridLine(self: MgCoordinateSystemTransform, fromPnt: MgCoordinate, toPnt: MgCoordinate, curvePrecision: float, maxPoints: int) -> MgLineString """
        pass

    def IgnoreDatumShiftWarning(self, bIgnoreDatumShiftWarning):
        """ IgnoreDatumShiftWarning(self: MgCoordinateSystemTransform, bIgnoreDatumShiftWarning: bool) """
        pass

    def IgnoreOutsideDomainWarning(self, bIgnoreOutsideDomainWarning):
        """ IgnoreOutsideDomainWarning(self: MgCoordinateSystemTransform, bIgnoreOutsideDomainWarning: bool) """
        pass

    def IsIgnoreDatumShiftWarning(self):
        """ IsIgnoreDatumShiftWarning(self: MgCoordinateSystemTransform) -> bool """
        pass

    def IsIgnoreOutsideDomainWarning(self):
        """ IsIgnoreOutsideDomainWarning(self: MgCoordinateSystemTransform) -> bool """
        pass

    def IsValidSourcePoint(self, x, y, z=None):
        """
        IsValidSourcePoint(self: MgCoordinateSystemTransform, x: float, y: float, z: float) -> bool
        IsValidSourcePoint(self: MgCoordinateSystemTransform, x: float, y: float) -> bool
        """
        pass

    def IsValidTargetPoint(self, x, y, z=None):
        """
        IsValidTargetPoint(self: MgCoordinateSystemTransform, x: float, y: float, z: float) -> bool
        IsValidTargetPoint(self: MgCoordinateSystemTransform, x: float, y: float) -> bool
        """
        pass

    def ResetLastTransformStatus(self):
        """ ResetLastTransformStatus(self: MgCoordinateSystemTransform) """
        pass

    def SetSourceAndTarget(self, pSource, pTarget):
        """ SetSourceAndTarget(self: MgCoordinateSystemTransform, pSource: MgCoordinateSystem, pTarget: MgCoordinateSystem) """
        pass

    def Transform(self, *__args):
        """
        Transform(self: MgCoordinateSystemTransform, coordinate: MgCoordinate) -> MgCoordinate
        Transform(self: MgCoordinateSystemTransform, envelope: MgEnvelope) -> MgEnvelope
        Transform(self: MgCoordinateSystemTransform, x: float, y: float) -> MgCoordinate
        Transform(self: MgCoordinateSystemTransform, x: float, y: float, z: float) -> MgCoordinate
        """
        pass

    def TransformCoordinate(self, coordinate):
        """ TransformCoordinate(self: MgCoordinateSystemTransform, coordinate: MgCoordinate) """
        pass

    def TransformM(self, x, y, *__args):
        """
        TransformM(self: MgCoordinateSystemTransform, x: float, y: float, z: float, m: float) -> MgCoordinate
        TransformM(self: MgCoordinateSystemTransform, x: float, y: float, m: float) -> MgCoordinate
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemTransformFailedException(MgApplicationException):
    """
    MgCoordinateSystemTransformFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgCoordinateSystemTransformFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemTransformFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemTransformFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemType(object):
    """ MgCoordinateSystemType() """
    Arbitrary = 1
    Geographic = 2
    Projected = 3
    Unknown = 0


class MgCoordinateSystemUnitCode(object):
    """ MgCoordinateSystemUnitCode() """
    BenoitChain = 26
    BenoitLink = 30
    BrChainTrunc = 52
    Brealey = 38
    BrFootTrunc = 51
    BrLinkTrunc = 53
    CaGrid = 23
    CapeFoot = 37
    Centimeter = 7
    Centisec = 1010
    ClarkeChain = 24
    ClarkeFoot = 5
    ClarkeLink = 28
    Decameter = 48
    Decimeter = 18
    Decisec = 1009
    Degree = 1001
    Dekameter = 20
    Foot = 2
    Furlong = 35
    GermanMeter = 22
    GoldCoastFoot = 40
    Grad = 1002
    Grade = 1003
    GunterChain = 25
    GunterLink = 29
    Hectometer = 21
    IFoot = 4
    IInch = 6
    IMile = 13
    Inch = 3
    IndianFoot = 43
    IndianFt37 = 44
    IndianFt62 = 45
    IndianFt75 = 46
    IndianYard = 42
    IndianYd37 = 47
    InternationalChain = 49
    InternationalLink = 50
    IYard = 12
    Kilometer = 8
    Knot = 14
    Lat66 = 16
    Lat83 = 17
    MapInfo = 1004
    Meter = 1
    MicroInch = 41
    Mil = 1005
    Mile = 11
    Millimeter = 19
    Millisec = 1011
    Minute = 1006
    NautM = 15
    Perch = 33
    Pole = 34
    Radian = 1007
    Rod = 32
    Rood = 36
    SearsChain = 27
    SearsFoot = 39
    SearsLink = 31
    SearsYard = 10
    Second = 1008
    Unknown = 0
    Yard = 9


class MgCoordinateSystemUnitInformation(MgGuardDisposable):
    """ MgCoordinateSystemUnitInformation(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateSystemUnitInformation) """
        pass

    def GetAbbreviation(self, nUnitCode):
        """ GetAbbreviation(self: MgCoordinateSystemUnitInformation, nUnitCode: int) -> str """
        pass

    def GetAngularUnitScale(self, nUnitCode):
        """ GetAngularUnitScale(self: MgCoordinateSystemUnitInformation, nUnitCode: int) -> float """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateSystemUnitInformation) -> IntPtr """
        pass

    def GetEnumAngularUnits(self):
        """ GetEnumAngularUnits(self: MgCoordinateSystemUnitInformation) -> MgCoordinateSystemEnumInteger32 """
        pass

    def GetEnumLinearUnits(self):
        """ GetEnumLinearUnits(self: MgCoordinateSystemUnitInformation) -> MgCoordinateSystemEnumInteger32 """
        pass

    def GetLinearUnitScale(self, nUnitCode):
        """ GetLinearUnitScale(self: MgCoordinateSystemUnitInformation, nUnitCode: int) -> float """
        pass

    def GetTagString(self, nUnitCode):
        """ GetTagString(self: MgCoordinateSystemUnitInformation, nUnitCode: int) -> str """
        pass

    def GetUnitType(self, nUnitCode):
        """ GetUnitType(self: MgCoordinateSystemUnitInformation, nUnitCode: int) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgCoordinateSystemUnitType(object):
    """ MgCoordinateSystemUnitType() """
    Angular = 2
    Linear = 1
    Unknown = 0


class MgCoordinateSystemWktFlavor(object):
    """ MgCoordinateSystemWktFlavor() """
    Epsg = 3
    Esri = 2
    Geotiff = 4
    Geotools = 5
    Ogc = 0
    Oracle = 1
    Unknown = -1


class MgCoordinateXY(MgCoordinate):
    """ MgCoordinateXY(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateXY) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateXY) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCoordinateXY) -> int """
        pass

    def GetM(self):
        """ GetM(self: MgCoordinateXY) -> float """
        pass

    def GetX(self):
        """ GetX(self: MgCoordinateXY) -> float """
        pass

    def GetY(self):
        """ GetY(self: MgCoordinateXY) -> float """
        pass

    def GetZ(self):
        """ GetZ(self: MgCoordinateXY) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCoordinateXY) -> int

"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: MgCoordinateXY) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: MgCoordinateXY) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: MgCoordinateXY) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: MgCoordinateXY) -> float

"""


    swigCMemOwn = None


class MgCoordinateXYM(MgCoordinate):
    """ MgCoordinateXYM(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateXYM) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateXYM) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCoordinateXYM) -> int """
        pass

    def GetM(self):
        """ GetM(self: MgCoordinateXYM) -> float """
        pass

    def GetX(self):
        """ GetX(self: MgCoordinateXYM) -> float """
        pass

    def GetY(self):
        """ GetY(self: MgCoordinateXYM) -> float """
        pass

    def GetZ(self):
        """ GetZ(self: MgCoordinateXYM) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCoordinateXYM) -> int

"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: MgCoordinateXYM) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: MgCoordinateXYM) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: MgCoordinateXYM) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: MgCoordinateXYM) -> float

"""


    swigCMemOwn = None


class MgCoordinateXYZ(MgCoordinate):
    """ MgCoordinateXYZ(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateXYZ) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateXYZ) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCoordinateXYZ) -> int """
        pass

    def GetM(self):
        """ GetM(self: MgCoordinateXYZ) -> float """
        pass

    def GetX(self):
        """ GetX(self: MgCoordinateXYZ) -> float """
        pass

    def GetY(self):
        """ GetY(self: MgCoordinateXYZ) -> float """
        pass

    def GetZ(self):
        """ GetZ(self: MgCoordinateXYZ) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCoordinateXYZ) -> int

"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: MgCoordinateXYZ) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: MgCoordinateXYZ) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: MgCoordinateXYZ) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: MgCoordinateXYZ) -> float

"""


    swigCMemOwn = None


class MgCoordinateXYZM(MgCoordinate):
    """ MgCoordinateXYZM(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCoordinateXYZM) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCoordinateXYZM) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCoordinateXYZM) -> int """
        pass

    def GetM(self):
        """ GetM(self: MgCoordinateXYZM) -> float """
        pass

    def GetX(self):
        """ GetX(self: MgCoordinateXYZM) -> float """
        pass

    def GetY(self):
        """ GetY(self: MgCoordinateXYZM) -> float """
        pass

    def GetZ(self):
        """ GetZ(self: MgCoordinateXYZM) -> float """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCoordinateXYZM) -> int

"""

    M = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: M(self: MgCoordinateXYZM) -> float

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: MgCoordinateXYZM) -> float

"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: MgCoordinateXYZM) -> float

"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: MgCoordinateXYZM) -> float

"""


    swigCMemOwn = None


class MgCurve(MgGeometry):
    """ MgCurve(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgCurve) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurve) -> IntPtr """
        pass

    def GetEndCoordinate(self):
        """ GetEndCoordinate(self: MgCurve) -> MgCoordinate """
        pass

    def GetStartCoordinate(self):
        """ GetStartCoordinate(self: MgCurve) -> MgCoordinate """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    EndCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndCoordinate(self: MgCurve) -> MgCoordinate

"""

    StartCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCoordinate(self: MgCurve) -> MgCoordinate

"""


    swigCMemOwn = None


class MgRegion(MgGeometry):
    """ MgRegion(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgRegion) """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgRegion) -> MgCoordinateIterator """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgRegion) -> IntPtr """
        pass

    def GetPointInRegion(self):
        """ GetPointInRegion(self: MgRegion) -> MgPoint """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Coordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coordinates(self: MgRegion) -> MgCoordinateIterator

"""

    PointInRegion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointInRegion(self: MgRegion) -> MgPoint

"""


    swigCMemOwn = None


class MgCurvePolygon(MgRegion):
    """ MgCurvePolygon(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgCurvePolygon) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgCurvePolygon) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurvePolygon) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCurvePolygon) -> int """
        pass

    def GetExteriorRing(self):
        """ GetExteriorRing(self: MgCurvePolygon) -> MgCurveRing """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgCurvePolygon) -> int """
        pass

    def GetInteriorRing(self, index):
        """ GetInteriorRing(self: MgCurvePolygon, index: int) -> MgCurveRing """
        pass

    def GetInteriorRingCount(self):
        """ GetInteriorRingCount(self: MgCurvePolygon) -> int """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgCurvePolygon) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgCurvePolygon) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgCurvePolygon, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCurvePolygon) -> int

"""

    ExteriorRing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExteriorRing(self: MgCurvePolygon) -> MgCurveRing

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgCurvePolygon) -> int

"""

    InteriorRingCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InteriorRingCount(self: MgCurvePolygon) -> int

"""


    swigCMemOwn = None


class MgCurvePolygonCollection(MgGuardDisposable):
    """
    MgCurvePolygonCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgCurvePolygonCollection()
    """
    def Add(self, value):
        """ Add(self: MgCurvePolygonCollection, value: MgCurvePolygon) """
        pass

    def Clear(self):
        """ Clear(self: MgCurvePolygonCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgCurvePolygonCollection, value: MgCurvePolygon) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgCurvePolygonCollection, array: Array[MgCurvePolygon], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCurvePolygonCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCurvePolygonCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurvePolygonCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgCurvePolygonCollection) -> IEnumerator[MgCurvePolygon] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCurvePolygonCollection, index: int) -> MgCurvePolygon """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgCurvePolygonCollection, value: MgCurvePolygon) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgCurvePolygonCollection, index: int, value: MgCurvePolygon) """
        pass

    def Remove(self, value):
        """ Remove(self: MgCurvePolygonCollection, value: MgCurvePolygon) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCurvePolygonCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgCurvePolygonCollection, index: int, value: MgCurvePolygon) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgCurvePolygon], item: MgCurvePolygon) -> bool """
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
    """Get: Count(self: MgCurvePolygonCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgCurvePolygonCollection) -> bool

"""


    MgCurvePolygonCollectionEnumerator = None
    swigCMemOwn = None


class MgRing(MgGeometryComponent):
    """ MgRing(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgRing) """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgRing) -> MgCoordinateIterator """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgRing) -> IntPtr """
        pass

    def GetPointInRing(self):
        """ GetPointInRing(self: MgRing) -> MgPoint """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Coordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coordinates(self: MgRing) -> MgCoordinateIterator

"""

    PointInRing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointInRing(self: MgRing) -> MgPoint

"""


    swigCMemOwn = None


class MgCurveRing(MgRing):
    """ MgCurveRing(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgCurveRing) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgCurveRing) """
        pass

    def GetComponentType(self):
        """ GetComponentType(self: MgCurveRing) -> int """
        pass

    def GetCount(self):
        """ GetCount(self: MgCurveRing) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurveRing) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCurveRing) -> int """
        pass

    def GetSegment(self, index):
        """ GetSegment(self: MgCurveRing, index: int) -> MgCurveSegment """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgCurveRing) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgCurveRing) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgCurveRing, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: MgCurveRing) -> int

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgCurveRing) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCurveRing) -> int

"""


    swigCMemOwn = None


class MgCurveRingCollection(MgGuardDisposable):
    """
    MgCurveRingCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgCurveRingCollection()
    """
    def Add(self, value):
        """ Add(self: MgCurveRingCollection, value: MgCurveRing) """
        pass

    def Clear(self):
        """ Clear(self: MgCurveRingCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgCurveRingCollection, value: MgCurveRing) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgCurveRingCollection, array: Array[MgCurveRing], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCurveRingCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCurveRingCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurveRingCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgCurveRingCollection) -> IEnumerator[MgCurveRing] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCurveRingCollection, index: int) -> MgCurveRing """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgCurveRingCollection, value: MgCurveRing) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgCurveRingCollection, index: int, value: MgCurveRing) """
        pass

    def Remove(self, value):
        """ Remove(self: MgCurveRingCollection, value: MgCurveRing) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCurveRingCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgCurveRingCollection, index: int, value: MgCurveRing) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgCurveRing], item: MgCurveRing) -> bool """
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
    """Get: Count(self: MgCurveRingCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgCurveRingCollection) -> bool

"""


    MgCurveRingCollectionEnumerator = None
    swigCMemOwn = None


class MgCurveSegmentCollection(MgGuardDisposable):
    """
    MgCurveSegmentCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgCurveSegmentCollection()
    """
    def Add(self, value):
        """ Add(self: MgCurveSegmentCollection, value: MgCurveSegment) """
        pass

    def Clear(self):
        """ Clear(self: MgCurveSegmentCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgCurveSegmentCollection, value: MgCurveSegment) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgCurveSegmentCollection, array: Array[MgCurveSegment], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCurveSegmentCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCurveSegmentCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurveSegmentCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgCurveSegmentCollection) -> IEnumerator[MgCurveSegment] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCurveSegmentCollection, index: int) -> MgCurveSegment """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgCurveSegmentCollection, value: MgCurveSegment) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgCurveSegmentCollection, index: int, value: MgCurveSegment) """
        pass

    def Remove(self, value):
        """ Remove(self: MgCurveSegmentCollection, value: MgCurveSegment) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCurveSegmentCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgCurveSegmentCollection, index: int, value: MgCurveSegment) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgCurveSegment], item: MgCurveSegment) -> bool """
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
    """Get: Count(self: MgCurveSegmentCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgCurveSegmentCollection) -> bool

"""


    MgCurveSegmentCollectionEnumerator = None
    swigCMemOwn = None


class MgCurveString(MgCurve):
    """ MgCurveString(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgCurveString) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgCurveString) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCurveString) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurveString) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgCurveString) -> int """
        pass

    def GetEndCoordinate(self):
        """ GetEndCoordinate(self: MgCurveString) -> MgCoordinate """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgCurveString) -> int """
        pass

    def GetSegment(self, index):
        """ GetSegment(self: MgCurveString, index: int) -> MgCurveSegment """
        pass

    def GetStartCoordinate(self):
        """ GetStartCoordinate(self: MgCurveString) -> MgCoordinate """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgCurveString) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgCurveString) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgCurveString, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgCurveString) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgCurveString) -> int

"""

    EndCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndCoordinate(self: MgCurveString) -> MgCoordinate

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgCurveString) -> int

"""

    StartCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCoordinate(self: MgCurveString) -> MgCoordinate

"""


    swigCMemOwn = None


class MgCurveStringCollection(MgGuardDisposable):
    """
    MgCurveStringCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgCurveStringCollection()
    """
    def Add(self, value):
        """ Add(self: MgCurveStringCollection, value: MgCurveString) """
        pass

    def Clear(self):
        """ Clear(self: MgCurveStringCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgCurveStringCollection, value: MgCurveString) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgCurveStringCollection, array: Array[MgCurveString], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgCurveStringCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgCurveStringCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgCurveStringCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgCurveStringCollection) -> IEnumerator[MgCurveString] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgCurveStringCollection, index: int) -> MgCurveString """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgCurveStringCollection, value: MgCurveString) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgCurveStringCollection, index: int, value: MgCurveString) """
        pass

    def Remove(self, value):
        """ Remove(self: MgCurveStringCollection, value: MgCurveString) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgCurveStringCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgCurveStringCollection, index: int, value: MgCurveString) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgCurveString], item: MgCurveString) -> bool """
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
    """Get: Count(self: MgCurveStringCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgCurveStringCollection) -> bool

"""


    MgCurveStringCollectionEnumerator = None
    swigCMemOwn = None


class MgPropertyDefinition(MgProperty):
    """
    MgPropertyDefinition(cPtr: IntPtr, cMemoryOwn: bool)
    MgPropertyDefinition(name: str, type: Int16)
    """
    def Delete(self):
        """ Delete(self: MgPropertyDefinition) """
        pass

    def Dispose(self):
        """ Dispose(self: MgPropertyDefinition) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPropertyDefinition) -> IntPtr """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgPropertyDefinition) -> str """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgPropertyDefinition) -> Int16 """
        pass

    def GetQualifiedName(self):
        """ GetQualifiedName(self: MgPropertyDefinition) -> str """
        pass

    def SetDescription(self, description):
        """ SetDescription(self: MgPropertyDefinition, description: str) """
        pass

    def SetQualifiedName(self, qualifiedName):
        """ SetQualifiedName(self: MgPropertyDefinition, qualifiedName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, type: Int16)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgPropertyDefinition) -> str

Set: Description(self: MgPropertyDefinition) = value
"""

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgPropertyDefinition) -> Int16

"""

    QualifiedName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: QualifiedName(self: MgPropertyDefinition) -> str

Set: QualifiedName(self: MgPropertyDefinition) = value
"""


    swigCMemOwn = None


class MgDataPropertyDefinition(MgPropertyDefinition):
    """
    MgDataPropertyDefinition(cPtr: IntPtr, cMemoryOwn: bool)
    MgDataPropertyDefinition(name: str)
    """
    def Dispose(self):
        """ Dispose(self: MgDataPropertyDefinition) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDataPropertyDefinition) -> IntPtr """
        pass

    def GetDataType(self):
        """ GetDataType(self: MgDataPropertyDefinition) -> int """
        pass

    def GetDefaultValue(self):
        """ GetDefaultValue(self: MgDataPropertyDefinition) -> str """
        pass

    def GetLength(self):
        """ GetLength(self: MgDataPropertyDefinition) -> int """
        pass

    def GetNullable(self):
        """ GetNullable(self: MgDataPropertyDefinition) -> bool """
        pass

    def GetPrecision(self):
        """ GetPrecision(self: MgDataPropertyDefinition) -> int """
        pass

    def GetReadOnly(self):
        """ GetReadOnly(self: MgDataPropertyDefinition) -> bool """
        pass

    def GetScale(self):
        """ GetScale(self: MgDataPropertyDefinition) -> int """
        pass

    def IsAutoGenerated(self):
        """ IsAutoGenerated(self: MgDataPropertyDefinition) -> bool """
        pass

    def SetAutoGeneration(self, value):
        """ SetAutoGeneration(self: MgDataPropertyDefinition, value: bool) """
        pass

    def SetDataType(self, type):
        """ SetDataType(self: MgDataPropertyDefinition, type: int) """
        pass

    def SetDefaultValue(self, value):
        """ SetDefaultValue(self: MgDataPropertyDefinition, value: str) """
        pass

    def SetLength(self, len):
        """ SetLength(self: MgDataPropertyDefinition, len: int) """
        pass

    def SetNullable(self, value):
        """ SetNullable(self: MgDataPropertyDefinition, value: bool) """
        pass

    def SetPrecision(self, precision):
        """ SetPrecision(self: MgDataPropertyDefinition, precision: int) """
        pass

    def SetReadOnly(self, value):
        """ SetReadOnly(self: MgDataPropertyDefinition, value: bool) """
        pass

    def SetScale(self, scale):
        """ SetScale(self: MgDataPropertyDefinition, scale: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    DataType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataType(self: MgDataPropertyDefinition) -> int

Set: DataType(self: MgDataPropertyDefinition) = value
"""

    DefaultValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultValue(self: MgDataPropertyDefinition) -> str

Set: DefaultValue(self: MgDataPropertyDefinition) = value
"""

    Length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Length(self: MgDataPropertyDefinition) -> int

Set: Length(self: MgDataPropertyDefinition) = value
"""

    Nullable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nullable(self: MgDataPropertyDefinition) -> bool

Set: Nullable(self: MgDataPropertyDefinition) = value
"""

    Precision = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Precision(self: MgDataPropertyDefinition) -> int

Set: Precision(self: MgDataPropertyDefinition) = value
"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: MgDataPropertyDefinition) -> bool

Set: ReadOnly(self: MgDataPropertyDefinition) = value
"""

    Scale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Scale(self: MgDataPropertyDefinition) -> int

Set: Scale(self: MgDataPropertyDefinition) = value
"""


    swigCMemOwn = None


class MgReader(MgSerializable):
    """ MgReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Close(self):
        """ Close(self: MgReader) """
        pass

    def Dispose(self):
        """ Dispose(self: MgReader) """
        pass

    def GetBLOB(self, *__args):
        """
        GetBLOB(self: MgReader, index: int) -> MgByteReader
        GetBLOB(self: MgReader, propertyName: str) -> MgByteReader
        """
        pass

    def GetBoolean(self, *__args):
        """
        GetBoolean(self: MgReader, index: int) -> bool
        GetBoolean(self: MgReader, propertyName: str) -> bool
        """
        pass

    def GetByte(self, *__args):
        """
        GetByte(self: MgReader, index: int) -> Byte
        GetByte(self: MgReader, propertyName: str) -> Byte
        """
        pass

    def GetCLOB(self, *__args):
        """
        GetCLOB(self: MgReader, index: int) -> MgByteReader
        GetCLOB(self: MgReader, propertyName: str) -> MgByteReader
        """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgReader) -> IntPtr """
        pass

    def GetDateTime(self, *__args):
        """
        GetDateTime(self: MgReader, index: int) -> MgDateTime
        GetDateTime(self: MgReader, propertyName: str) -> MgDateTime
        """
        pass

    def GetDouble(self, *__args):
        """
        GetDouble(self: MgReader, index: int) -> float
        GetDouble(self: MgReader, propertyName: str) -> float
        """
        pass

    def GetGeometry(self, *__args):
        """
        GetGeometry(self: MgReader, index: int) -> MgByteReader
        GetGeometry(self: MgReader, propertyName: str) -> MgByteReader
        """
        pass

    def GetInt16(self, *__args):
        """
        GetInt16(self: MgReader, index: int) -> Int16
        GetInt16(self: MgReader, propertyName: str) -> Int16
        """
        pass

    def GetInt32(self, *__args):
        """
        GetInt32(self: MgReader, index: int) -> int
        GetInt32(self: MgReader, propertyName: str) -> int
        """
        pass

    def GetInt64(self, *__args):
        """
        GetInt64(self: MgReader, index: int) -> Int64
        GetInt64(self: MgReader, propertyName: str) -> Int64
        """
        pass

    def GetPropertyCount(self):
        """ GetPropertyCount(self: MgReader) -> int """
        pass

    def GetPropertyIndex(self, propertyName):
        """ GetPropertyIndex(self: MgReader, propertyName: str) -> int """
        pass

    def GetPropertyName(self, index):
        """ GetPropertyName(self: MgReader, index: int) -> str """
        pass

    def GetPropertyType(self, *__args):
        """
        GetPropertyType(self: MgReader, index: int) -> int
        GetPropertyType(self: MgReader, propertyName: str) -> int
        """
        pass

    def GetRaster(self, *__args):
        """
        GetRaster(self: MgReader, index: int) -> MgRaster
        GetRaster(self: MgReader, propertyName: str) -> MgRaster
        """
        pass

    def GetReaderType(self):
        """ GetReaderType(self: MgReader) -> int """
        pass

    def GetSingle(self, *__args):
        """
        GetSingle(self: MgReader, index: int) -> Single
        GetSingle(self: MgReader, propertyName: str) -> Single
        """
        pass

    def GetString(self, *__args):
        """
        GetString(self: MgReader, index: int) -> str
        GetString(self: MgReader, propertyName: str) -> str
        """
        pass

    def IsNull(self, *__args):
        """
        IsNull(self: MgReader, index: int) -> bool
        IsNull(self: MgReader, propertyName: str) -> bool
        """
        pass

    def ReadNext(self):
        """ ReadNext(self: MgReader) -> bool """
        pass

    def ToXml(self):
        """ ToXml(self: MgReader) -> MgByteReader """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgDataReader(MgReader):
    """ MgDataReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgDataReader) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDataReader) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgDateTime(MgSerializable):
    """
    MgDateTime(cPtr: IntPtr, cMemoryOwn: bool)
    MgDateTime()
    MgDateTime(year: Int16, month: Int16, day: Int16)
    MgDateTime(hour: Int16, minute: Int16, second: Int16, microsecond: int)
    MgDateTime(year: Int16, month: Int16, day: Int16, hour: Int16, minute: Int16, second: Int16, microsecond: int)
    """
    def Dispose(self):
        """ Dispose(self: MgDateTime) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDateTime) -> IntPtr """
        pass

    def GetDay(self):
        """ GetDay(self: MgDateTime) -> Int16 """
        pass

    def GetHour(self):
        """ GetHour(self: MgDateTime) -> Int16 """
        pass

    def GetMicrosecond(self):
        """ GetMicrosecond(self: MgDateTime) -> int """
        pass

    def GetMinute(self):
        """ GetMinute(self: MgDateTime) -> Int16 """
        pass

    def GetMonth(self):
        """ GetMonth(self: MgDateTime) -> Int16 """
        pass

    def GetSecond(self):
        """ GetSecond(self: MgDateTime) -> Int16 """
        pass

    def GetYear(self):
        """ GetYear(self: MgDateTime) -> Int16 """
        pass

    def IsDate(self):
        """ IsDate(self: MgDateTime) -> bool """
        pass

    def IsDateTime(self):
        """ IsDateTime(self: MgDateTime) -> bool """
        pass

    def IsTime(self):
        """ IsTime(self: MgDateTime) -> bool """
        pass

    def SetDay(self, day):
        """ SetDay(self: MgDateTime, day: Int16) """
        pass

    def SetHour(self, hour):
        """ SetHour(self: MgDateTime, hour: Int16) """
        pass

    def SetMicrosecond(self, microsecond):
        """ SetMicrosecond(self: MgDateTime, microsecond: int) """
        pass

    def SetMinute(self, minute):
        """ SetMinute(self: MgDateTime, minute: Int16) """
        pass

    def SetMonth(self, month):
        """ SetMonth(self: MgDateTime, month: Int16) """
        pass

    def SetSecond(self, second):
        """ SetSecond(self: MgDateTime, second: Int16) """
        pass

    def SetYear(self, year):
        """ SetYear(self: MgDateTime, year: Int16) """
        pass

    def ToString(self):
        """ ToString(self: MgDateTime) -> str """
        pass

    def Validate(self):
        """ Validate(self: MgDateTime) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, year: Int16, month: Int16, day: Int16)
        __new__(cls: type, hour: Int16, minute: Int16, second: Int16, microsecond: int)
        __new__(cls: type, year: Int16, month: Int16, day: Int16, hour: Int16, minute: Int16, second: Int16, microsecond: int)
        """
        pass

    Day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Day(self: MgDateTime) -> Int16

Set: Day(self: MgDateTime) = value
"""

    Hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Hour(self: MgDateTime) -> Int16

Set: Hour(self: MgDateTime) = value
"""

    Microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Microsecond(self: MgDateTime) -> int

Set: Microsecond(self: MgDateTime) = value
"""

    Minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Minute(self: MgDateTime) -> Int16

Set: Minute(self: MgDateTime) = value
"""

    Month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Month(self: MgDateTime) -> Int16

Set: Month(self: MgDateTime) = value
"""

    Second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Second(self: MgDateTime) -> Int16

Set: Second(self: MgDateTime) = value
"""

    Year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Year(self: MgDateTime) -> Int16

Set: Year(self: MgDateTime) = value
"""


    swigCMemOwn = None


class MgDateTimeException(MgApplicationException):
    """
    MgDateTimeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDateTimeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDateTimeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDateTimeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDateTimeProperty(MgNullableProperty):
    """
    MgDateTimeProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgDateTimeProperty(name: str, value: MgDateTime)
    """
    def Dispose(self):
        """ Dispose(self: MgDateTimeProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDateTimeProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgDateTimeProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgDateTimeProperty) -> MgDateTime """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgDateTimeProperty, value: MgDateTime) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: MgDateTime)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgDateTimeProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgDateTimeProperty) -> MgDateTime

Set: Value(self: MgDateTimeProperty) = value
"""


    swigCMemOwn = None


class MgDecryptionException(MgApplicationException):
    """
    MgDecryptionException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDecryptionException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDecryptionException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDecryptionException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgFeatureCommand(MgSerializable):
    """ MgFeatureCommand(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgFeatureCommand) """
        pass

    def GetCommandType(self):
        """ GetCommandType(self: MgFeatureCommand) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureCommand) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgDeleteFeatures(MgFeatureCommand):
    """
    MgDeleteFeatures(cPtr: IntPtr, cMemoryOwn: bool)
    MgDeleteFeatures(className: str, filterText: str)
    """
    def Dispose(self):
        """ Dispose(self: MgDeleteFeatures) """
        pass

    def GetCommandType(self):
        """ GetCommandType(self: MgDeleteFeatures) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDeleteFeatures) -> IntPtr """
        pass

    def GetFeatureClassName(self):
        """ GetFeatureClassName(self: MgDeleteFeatures) -> str """
        pass

    def GetFilterText(self):
        """ GetFilterText(self: MgDeleteFeatures) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, className: str, filterText: str)
        """
        pass

    CommandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandType(self: MgDeleteFeatures) -> int

"""

    FeatureClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureClassName(self: MgDeleteFeatures) -> str

"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterText(self: MgDeleteFeatures) -> str

"""


    swigCMemOwn = None


class MgIoException(MgSystemException):
    """
    MgIoException(cPtr: IntPtr, cMemoryOwn: bool)
    MgIoException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgIoException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgIoException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgFileIoException(MgIoException):
    """
    MgFileIoException(cPtr: IntPtr, cMemoryOwn: bool)
    MgFileIoException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgFileIoException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFileIoException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDirectoryNotFoundException(MgFileIoException):
    """
    MgDirectoryNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDirectoryNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDirectoryNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDirectoryNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDisposableCollection(MgCollection):
    """
    MgDisposableCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgDisposableCollection()
    """
    def Add(self, value):
        """ Add(self: MgDisposableCollection, value: MgDisposable) """
        pass

    def Clear(self):
        """ Clear(self: MgDisposableCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgDisposableCollection, value: MgDisposable) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgDisposableCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgDisposableCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDisposableCollection) -> IntPtr """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgDisposableCollection, index: int) -> MgDisposable """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgDisposableCollection, value: MgDisposable) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgDisposableCollection, index: int, value: MgDisposable) """
        pass

    def Remove(self, value):
        """ Remove(self: MgDisposableCollection, value: MgDisposable) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgDisposableCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgDisposableCollection, index: int, value: MgDisposable) """
        pass

    def ToXml(self):
        """ ToXml(self: MgDisposableCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    swigCMemOwn = None


class MgDivideByZeroException(MgSystemException):
    """
    MgDivideByZeroException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDivideByZeroException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDivideByZeroException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDivideByZeroException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDomainException(MgSystemException):
    """
    MgDomainException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDomainException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDomainException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDomainException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDoubleCollection(MgCollection):
    """
    MgDoubleCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgDoubleCollection()
    """
    def Add(self, value):
        """ Add(self: MgDoubleCollection, value: float) """
        pass

    def Clear(self):
        """ Clear(self: MgDoubleCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgDoubleCollection, value: float) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgDoubleCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgDoubleCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDoubleCollection) -> IntPtr """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgDoubleCollection, index: int) -> float """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgDoubleCollection, value: float) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgDoubleCollection, index: int, value: float) """
        pass

    def Remove(self, value):
        """ Remove(self: MgDoubleCollection, value: float) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgDoubleCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgDoubleCollection, index: int, value: float) """
        pass

    def ToXml(self):
        """ ToXml(self: MgDoubleCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    swigCMemOwn = None


class MgDoubleProperty(MgNullableProperty):
    """
    MgDoubleProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgDoubleProperty(name: str, value: float)
    """
    def Dispose(self):
        """ Dispose(self: MgDoubleProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDoubleProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgDoubleProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgDoubleProperty) -> float """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgDoubleProperty, value: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: float)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgDoubleProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgDoubleProperty) -> float

Set: Value(self: MgDoubleProperty) = value
"""


    swigCMemOwn = None


class MgDuplicateDirectoryException(MgApplicationException):
    """
    MgDuplicateDirectoryException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDuplicateDirectoryException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDuplicateDirectoryException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDuplicateDirectoryException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDuplicateFileException(MgApplicationException):
    """
    MgDuplicateFileException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDuplicateFileException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDuplicateFileException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDuplicateFileException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDuplicateObjectException(MgSystemException):
    """
    MgDuplicateObjectException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDuplicateObjectException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDuplicateObjectException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDuplicateObjectException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDuplicateResourceDataException(MgApplicationException):
    """
    MgDuplicateResourceDataException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDuplicateResourceDataException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDuplicateResourceDataException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDuplicateResourceDataException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgDuplicateResourceException(MgApplicationException):
    """
    MgDuplicateResourceException(cPtr: IntPtr, cMemoryOwn: bool)
    MgDuplicateResourceException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgDuplicateResourceException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgDuplicateResourceException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgEmptyFeatureSetException(MgSystemException):
    """
    MgEmptyFeatureSetException(cPtr: IntPtr, cMemoryOwn: bool)
    MgEmptyFeatureSetException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgEmptyFeatureSetException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgEmptyFeatureSetException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgEncryptionException(MgApplicationException):
    """
    MgEncryptionException(cPtr: IntPtr, cMemoryOwn: bool)
    MgEncryptionException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgEncryptionException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgEncryptionException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgEnvelope(MgSerializable):
    """
    MgEnvelope(cPtr: IntPtr, cMemoryOwn: bool)
    MgEnvelope()
    MgEnvelope(coord: MgCoordinate)
    MgEnvelope(coord1: MgCoordinate, coord2: MgCoordinate)
    MgEnvelope(xMin: float, yMin: float, xMax: float, yMax: float)
    MgEnvelope(envelope: MgEnvelope)
    """
    def Contains(self, *__args):
        """
        Contains(self: MgEnvelope, envelope: MgEnvelope) -> bool
        Contains(self: MgEnvelope, coordinate: MgCoordinate) -> bool
        """
        pass

    def Dispose(self):
        """ Dispose(self: MgEnvelope) """
        pass

    def ExpandToInclude(self, *__args):
        """ ExpandToInclude(self: MgEnvelope, envelope: MgEnvelope)ExpandToInclude(self: MgEnvelope, coordinate: MgCoordinate) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgEnvelope) -> IntPtr """
        pass

    def GetDepth(self):
        """ GetDepth(self: MgEnvelope) -> float """
        pass

    def GetHeight(self):
        """ GetHeight(self: MgEnvelope) -> float """
        pass

    def GetLowerLeftCoordinate(self):
        """ GetLowerLeftCoordinate(self: MgEnvelope) -> MgCoordinate """
        pass

    def GetUpperRightCoordinate(self):
        """ GetUpperRightCoordinate(self: MgEnvelope) -> MgCoordinate """
        pass

    def GetWidth(self):
        """ GetWidth(self: MgEnvelope) -> float """
        pass

    def Intersects(self, envelope):
        """ Intersects(self: MgEnvelope, envelope: MgEnvelope) -> bool """
        pass

    def IsNull(self):
        """ IsNull(self: MgEnvelope) -> bool """
        pass

    def MakeNull(self):
        """ MakeNull(self: MgEnvelope) """
        pass

    def Transform(self, transform):
        """ Transform(self: MgEnvelope, transform: MgTransform) -> MgEnvelope """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, coord: MgCoordinate)
        __new__(cls: type, coord1: MgCoordinate, coord2: MgCoordinate)
        __new__(cls: type, xMin: float, yMin: float, xMax: float, yMax: float)
        __new__(cls: type, envelope: MgEnvelope)
        """
        pass

    Depth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Depth(self: MgEnvelope) -> float

"""

    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Height(self: MgEnvelope) -> float

"""

    LowerLeftCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LowerLeftCoordinate(self: MgEnvelope) -> MgCoordinate

"""

    UpperRightCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpperRightCoordinate(self: MgEnvelope) -> MgCoordinate

"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Width(self: MgEnvelope) -> float

"""


    swigCMemOwn = None


class MgThirdPartyException(MgException):
    """ MgThirdPartyException(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgThirdPartyException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgThirdPartyException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    swigCMemOwn = None


class MgFdoException(MgThirdPartyException):
    """
    MgFdoException(cPtr: IntPtr, cMemoryOwn: bool)
    MgFdoException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    MgFdoException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection, nativeErrorCode: Int64)
    """
    def Dispose(self):
        """ Dispose(self: MgFdoException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFdoException) -> IntPtr """
        pass

    def GetNativeErrorCode(self):
        """ GetNativeErrorCode(self: MgFdoException) -> Int64 """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection, nativeErrorCode: Int64)
        """
        pass

    swigCMemOwn = None


class MgFeatureQueryOptions(MgSerializable):
    """
    MgFeatureQueryOptions(cPtr: IntPtr, cMemoryOwn: bool)
    MgFeatureQueryOptions()
    """
    def AddComputedProperty(self, aliasName, expression):
        """ AddComputedProperty(self: MgFeatureQueryOptions, aliasName: str, expression: str) -> int """
        pass

    def AddFeatureProperty(self, propertyName):
        """ AddFeatureProperty(self: MgFeatureQueryOptions, propertyName: str) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: MgFeatureQueryOptions) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureQueryOptions) -> IntPtr """
        pass

    def RemoveComputedProperty(self, aliasName):
        """ RemoveComputedProperty(self: MgFeatureQueryOptions, aliasName: str) """
        pass

    def RemoveFeatureProperty(self, propertyName):
        """ RemoveFeatureProperty(self: MgFeatureQueryOptions, propertyName: str) """
        pass

    def SetBinaryOperator(self, andOr):
        """ SetBinaryOperator(self: MgFeatureQueryOptions, andOr: bool) """
        pass

    def SetFetchSize(self, fetchSize):
        """ SetFetchSize(self: MgFeatureQueryOptions, fetchSize: int) """
        pass

    def SetFilter(self, filterText):
        """ SetFilter(self: MgFeatureQueryOptions, filterText: str) """
        pass

    def SetOrderingFilter(self, orderByProperties, orderOption):
        """ SetOrderingFilter(self: MgFeatureQueryOptions, orderByProperties: MgStringCollection, orderOption: int) """
        pass

    def SetSpatialFilter(self, geometryProperty, geometry, spatialOperation):
        """ SetSpatialFilter(self: MgFeatureQueryOptions, geometryProperty: str, geometry: MgGeometry, spatialOperation: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgFeatureAggregateOptions(MgFeatureQueryOptions):
    """
    MgFeatureAggregateOptions(cPtr: IntPtr, cMemoryOwn: bool)
    MgFeatureAggregateOptions()
    """
    def Dispose(self):
        """ Dispose(self: MgFeatureAggregateOptions) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureAggregateOptions) -> IntPtr """
        pass

    def SelectDistinct(self, yes):
        """ SelectDistinct(self: MgFeatureAggregateOptions, yes: bool) """
        pass

    def SetGroupingFilter(self, groupByProperties, groupFilter):
        """ SetGroupingFilter(self: MgFeatureAggregateOptions, groupByProperties: MgStringCollection, groupFilter: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgFeatureCommandCollection(MgSerializable):
    """
    MgFeatureCommandCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgFeatureCommandCollection()
    """
    def Add(self, command):
        """ Add(self: MgFeatureCommandCollection, command: MgFeatureCommand) """
        pass

    def Clear(self):
        """ Clear(self: MgFeatureCommandCollection) """
        pass

    def Contains(self, command):
        """ Contains(self: MgFeatureCommandCollection, command: MgFeatureCommand) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgFeatureCommandCollection, array: Array[MgFeatureCommand], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgFeatureCommandCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgFeatureCommandCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureCommandCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgFeatureCommandCollection) -> IEnumerator[MgFeatureCommand] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgFeatureCommandCollection, index: int) -> MgFeatureCommand """
        pass

    def IndexOf(self, command):
        """ IndexOf(self: MgFeatureCommandCollection, command: MgFeatureCommand) -> int """
        pass

    def Insert(self, index, command):
        """ Insert(self: MgFeatureCommandCollection, index: int, command: MgFeatureCommand) """
        pass

    def Remove(self, command):
        """ Remove(self: MgFeatureCommandCollection, command: MgFeatureCommand) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgFeatureCommandCollection, index: int) """
        pass

    def SetItem(self, index, command):
        """ SetItem(self: MgFeatureCommandCollection, index: int, command: MgFeatureCommand) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgFeatureCommand], item: MgFeatureCommand) -> bool """
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
    """Get: Count(self: MgFeatureCommandCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgFeatureCommandCollection) -> bool

"""


    MgFeatureCommandCollectionEnumerator = None
    swigCMemOwn = None


class MgFeatureCommandType(object):
    """ MgFeatureCommandType() """
    DeleteFeatures = 2
    InsertFeatures = 0
    LockFeatures = 3
    UnlockFeatures = 4
    UpdateFeatures = 1


class MgFeatureGeometricType(object):
    """ MgFeatureGeometricType() """
    Curve = 2
    Point = 1
    Solid = 8
    Surface = 4


class MgFeatureProperty(MgNullableProperty):
    """
    MgFeatureProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgFeatureProperty(name: str, value: MgFeatureReader)
    """
    def Dispose(self):
        """ Dispose(self: MgFeatureProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgFeatureProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgFeatureProperty) -> MgFeatureReader """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgFeatureProperty, value: MgFeatureReader) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: MgFeatureReader)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgFeatureProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgFeatureProperty) -> MgFeatureReader

Set: Value(self: MgFeatureProperty) = value
"""


    swigCMemOwn = None


class MgFeaturePropertyType(object):
    """ MgFeaturePropertyType() """
    AssociationProperty = 103
    DataProperty = 100
    GeometricProperty = 102
    ObjectProperty = 101
    RasterProperty = 104


class MgFeatureReader(MgReader):
    """ MgFeatureReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgFeatureReader) """
        pass

    def GetClassDefinition(self):
        """ GetClassDefinition(self: MgFeatureReader) -> MgClassDefinition """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureReader) -> IntPtr """
        pass

    def GetFeatureObject(self, *__args):
        """
        GetFeatureObject(self: MgFeatureReader, index: int) -> MgFeatureReader
        GetFeatureObject(self: MgFeatureReader, propertyName: str) -> MgFeatureReader
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgFeatureSchema(MgNamedSerializable):
    """
    MgFeatureSchema(cPtr: IntPtr, cMemoryOwn: bool)
    MgFeatureSchema()
    MgFeatureSchema(name: str, description: str)
    """
    def Delete(self):
        """ Delete(self: MgFeatureSchema) """
        pass

    def Dispose(self):
        """ Dispose(self: MgFeatureSchema) """
        pass

    def GetClasses(self):
        """ GetClasses(self: MgFeatureSchema) -> MgClassDefinitionCollection """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureSchema) -> IntPtr """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgFeatureSchema) -> str """
        pass

    def GetName(self):
        """ GetName(self: MgFeatureSchema) -> str """
        pass

    def SetDescription(self, description):
        """ SetDescription(self: MgFeatureSchema, description: str) """
        pass

    def SetName(self, name):
        """ SetName(self: MgFeatureSchema, name: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, description: str)
        """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgFeatureSchema) -> str

Set: Description(self: MgFeatureSchema) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgFeatureSchema) -> str

Set: Name(self: MgFeatureSchema) = value
"""


    swigCMemOwn = None


class MgFeatureSchemaCollection(MgCollection):
    """
    MgFeatureSchemaCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgFeatureSchemaCollection()
    """
    def Add(self, value):
        """ Add(self: MgFeatureSchemaCollection, value: MgFeatureSchema) """
        pass

    def Clear(self):
        """ Clear(self: MgFeatureSchemaCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgFeatureSchemaCollection, value: MgFeatureSchema) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgFeatureSchemaCollection, array: Array[MgFeatureSchema], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgFeatureSchemaCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgFeatureSchemaCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureSchemaCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgFeatureSchemaCollection) -> IEnumerator[MgFeatureSchema] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgFeatureSchemaCollection, index: int) -> MgFeatureSchema """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgFeatureSchemaCollection, value: MgFeatureSchema) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgFeatureSchemaCollection, index: int, value: MgFeatureSchema) """
        pass

    def Remove(self, value):
        """ Remove(self: MgFeatureSchemaCollection, value: MgFeatureSchema) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgFeatureSchemaCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgFeatureSchemaCollection, index: int, value: MgFeatureSchema) """
        pass

    def ToXml(self):
        """ ToXml(self: MgFeatureSchemaCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgFeatureSchema], item: MgFeatureSchema) -> bool """
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
    """Get: Count(self: MgFeatureSchemaCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgFeatureSchemaCollection) -> bool

"""


    MgFeatureSchemaCollectionEnumerator = None
    swigCMemOwn = None


class MgService(MgGuardDisposable):
    """ MgService(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgService) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgService) -> IntPtr """
        pass

    def GetWarningsObject(self):
        """ GetWarningsObject(self: MgService) -> MgWarnings """
        pass

    def HasWarnings(self):
        """ HasWarnings(self: MgService) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgFeatureService(MgService):
    """ MgFeatureService(cPtr: IntPtr, cMemoryOwn: bool) """
    def ApplySchema(self, resource, schema):
        """ ApplySchema(self: MgFeatureService, resource: MgResourceIdentifier, schema: MgFeatureSchema) """
        pass

    def BeginTransaction(self, resource):
        """ BeginTransaction(self: MgFeatureService, resource: MgResourceIdentifier) -> MgTransaction """
        pass

    def CreateFeatureSource(self, resource, sourceParams):
        """ CreateFeatureSource(self: MgFeatureService, resource: MgResourceIdentifier, sourceParams: MgFeatureSourceParams) """
        pass

    def DeleteFeatures(self, resource, className, filter, trans=None):
        """
        DeleteFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, filter: str, trans: MgTransaction) -> int
        DeleteFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, filter: str) -> int
        """
        pass

    def DescribeSchema(self, resource, schemaName, classNames=None):
        """
        DescribeSchema(self: MgFeatureService, resource: MgResourceIdentifier, schemaName: str) -> MgFeatureSchemaCollection
        DescribeSchema(self: MgFeatureService, resource: MgResourceIdentifier, schemaName: str, classNames: MgStringCollection) -> MgFeatureSchemaCollection
        """
        pass

    def DescribeSchemaAsXml(self, resource, schemaName, classNames=None):
        """
        DescribeSchemaAsXml(self: MgFeatureService, resource: MgResourceIdentifier, schemaName: str) -> str
        DescribeSchemaAsXml(self: MgFeatureService, resource: MgResourceIdentifier, schemaName: str, classNames: MgStringCollection) -> str
        """
        pass

    def DescribeWfsFeatureType(self, featureSourceId, featureClasses, namespacePrefix=None, namespaceUrl=None):
        """
        DescribeWfsFeatureType(self: MgFeatureService, featureSourceId: MgResourceIdentifier, featureClasses: MgStringCollection, namespacePrefix: str, namespaceUrl: str) -> MgByteReader
        DescribeWfsFeatureType(self: MgFeatureService, featureSourceId: MgResourceIdentifier, featureClasses: MgStringCollection) -> MgByteReader
        """
        pass

    def Dispose(self):
        """ Dispose(self: MgFeatureService) """
        pass

    def EnumerateDataStores(self, providerName, partialConnString):
        """ EnumerateDataStores(self: MgFeatureService, providerName: str, partialConnString: str) -> MgByteReader """
        pass

    def ExecuteSqlNonQuery(self, resource, sqlNonSelectStatement, parameters=None, transaction=None):
        """
        ExecuteSqlNonQuery(self: MgFeatureService, resource: MgResourceIdentifier, sqlNonSelectStatement: str, parameters: MgParameterCollection, transaction: MgTransaction) -> int
        ExecuteSqlNonQuery(self: MgFeatureService, resource: MgResourceIdentifier, sqlNonSelectStatement: str) -> int
        """
        pass

    def ExecuteSqlQuery(self, resource, sqlStatement, parameters=None, transaction=None):
        """
        ExecuteSqlQuery(self: MgFeatureService, resource: MgResourceIdentifier, sqlStatement: str, parameters: MgParameterCollection, transaction: MgTransaction) -> MgSqlDataReader
        ExecuteSqlQuery(self: MgFeatureService, resource: MgResourceIdentifier, sqlStatement: str) -> MgSqlDataReader
        """
        pass

    def GetCapabilities(self, providerName, connectionString=None):
        """
        GetCapabilities(self: MgFeatureService, providerName: str, connectionString: str) -> MgByteReader
        GetCapabilities(self: MgFeatureService, providerName: str) -> MgByteReader
        """
        pass

    def GetClassDefinition(self, resource, schemaName, className):
        """ GetClassDefinition(self: MgFeatureService, resource: MgResourceIdentifier, schemaName: str, className: str) -> MgClassDefinition """
        pass

    def GetClasses(self, resource, schemaName):
        """ GetClasses(self: MgFeatureService, resource: MgResourceIdentifier, schemaName: str) -> MgStringCollection """
        pass

    def GetConnectionPropertyValues(self, providerName, propertyName, partialConnString):
        """ GetConnectionPropertyValues(self: MgFeatureService, providerName: str, propertyName: str, partialConnString: str) -> MgStringCollection """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureService) -> IntPtr """
        pass

    def GetFeatureProviders(self):
        """ GetFeatureProviders(self: MgFeatureService) -> MgByteReader """
        pass

    def GetLockedFeatures(self, resource, className, options):
        """ GetLockedFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, options: MgFeatureQueryOptions) -> MgFeatureReader """
        pass

    def GetLongTransactions(self, resource, bActiveOnly):
        """ GetLongTransactions(self: MgFeatureService, resource: MgResourceIdentifier, bActiveOnly: bool) -> MgLongTransactionReader """
        pass

    def GetSchemaMapping(self, providerName, partialConnString):
        """ GetSchemaMapping(self: MgFeatureService, providerName: str, partialConnString: str) -> MgByteReader """
        pass

    def GetSchemas(self, resource):
        """ GetSchemas(self: MgFeatureService, resource: MgResourceIdentifier) -> MgStringCollection """
        pass

    def GetSpatialContexts(self, resource, bActiveOnly):
        """ GetSpatialContexts(self: MgFeatureService, resource: MgResourceIdentifier, bActiveOnly: bool) -> MgSpatialContextReader """
        pass

    def GetWfsFeature(self, featureSourceId, featureClass, requiredProperties, srs, filter, maxFeatures, wfsVersion=None, outputFormat=None, sortCriteria=None, namespacePrefix=None, namespaceUrl=None):
        """
        GetWfsFeature(self: MgFeatureService, featureSourceId: MgResourceIdentifier, featureClass: str, requiredProperties: MgStringCollection, srs: str, filter: str, maxFeatures: int, wfsVersion: str, outputFormat: str, sortCriteria: str, namespacePrefix: str, namespaceUrl: str) -> MgByteReader
        GetWfsFeature(self: MgFeatureService, featureSourceId: MgResourceIdentifier, featureClass: str, requiredProperties: MgStringCollection, srs: str, filter: str, maxFeatures: int) -> MgByteReader
        """
        pass

    def InsertFeatures(self, resource, className, *__args):
        """
        InsertFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, batchPropertyValues: MgBatchPropertyCollection) -> MgFeatureReader
        InsertFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, batchPropertyValues: MgBatchPropertyCollection, trans: MgTransaction) -> MgFeatureReader
        InsertFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, propertyValues: MgPropertyCollection) -> MgFeatureReader
        InsertFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, propertyValues: MgPropertyCollection, trans: MgTransaction) -> MgFeatureReader
        """
        pass

    def SchemaToXml(self, schema):
        """ SchemaToXml(self: MgFeatureService, schema: MgFeatureSchemaCollection) -> str """
        pass

    def SelectAggregate(self, resource, className, options):
        """ SelectAggregate(self: MgFeatureService, resource: MgResourceIdentifier, className: str, options: MgFeatureAggregateOptions) -> MgDataReader """
        pass

    def SelectFeatures(self, resource, className, options, coordinateSystem=None):
        """
        SelectFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, options: MgFeatureQueryOptions, coordinateSystem: str) -> MgFeatureReader
        SelectFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, options: MgFeatureQueryOptions) -> MgFeatureReader
        """
        pass

    def SetLongTransaction(self, featureSourceId, longTransactionName):
        """ SetLongTransaction(self: MgFeatureService, featureSourceId: MgResourceIdentifier, longTransactionName: str) -> bool """
        pass

    def TestConnection(self, *__args):
        """
        TestConnection(self: MgFeatureService, resource: MgResourceIdentifier) -> bool
        TestConnection(self: MgFeatureService, providerName: str, connectionString: str) -> bool
        """
        pass

    def UpdateFeatures(self, resource, commands, *__args):
        """
        UpdateFeatures(self: MgFeatureService, resource: MgResourceIdentifier, commands: MgFeatureCommandCollection, transaction: MgTransaction) -> MgPropertyCollection
        UpdateFeatures(self: MgFeatureService, resource: MgResourceIdentifier, commands: MgFeatureCommandCollection, useTransaction: bool) -> MgPropertyCollection
        """
        pass

    def UpdateMatchingFeatures(self, resource, className, properties, filter, trans=None):
        """
        UpdateMatchingFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, properties: MgPropertyCollection, filter: str, trans: MgTransaction) -> int
        UpdateMatchingFeatures(self: MgFeatureService, resource: MgResourceIdentifier, className: str, properties: MgPropertyCollection, filter: str) -> int
        """
        pass

    def XmlToSchema(self, xml):
        """ XmlToSchema(self: MgFeatureService, xml: str) -> MgFeatureSchemaCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgFeatureServiceException(MgApplicationException):
    """
    MgFeatureServiceException(cPtr: IntPtr, cMemoryOwn: bool)
    MgFeatureServiceException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgFeatureServiceException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureServiceException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgFeatureSourceParams(MgSerializable):
    """ MgFeatureSourceParams(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgFeatureSourceParams) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFeatureSourceParams) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgFeatureSpatialOperations(object):
    """ MgFeatureSpatialOperations() """
    Contains = 0
    CoveredBy = 8
    Crosses = 1
    Disjoint = 2
    EnvelopeIntersects = 10
    Equals = 3
    Inside = 9
    Intersects = 4
    Overlaps = 5
    Touches = 6
    Within = 7


class MgFileFeatureSourceParams(MgFeatureSourceParams):
    """
    MgFileFeatureSourceParams(cPtr: IntPtr, cMemoryOwn: bool)
    MgFileFeatureSourceParams()
    MgFileFeatureSourceParams(providerName: str)
    MgFileFeatureSourceParams(providerName: str, spatialContextName: str, srsWkt: str, featureSchema: MgFeatureSchema)
    """
    def Dispose(self):
        """ Dispose(self: MgFileFeatureSourceParams) """
        pass

    def GetCoordinateSystemWkt(self):
        """ GetCoordinateSystemWkt(self: MgFileFeatureSourceParams) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFileFeatureSourceParams) -> IntPtr """
        pass

    def GetFeatureSchema(self):
        """ GetFeatureSchema(self: MgFileFeatureSourceParams) -> MgFeatureSchema """
        pass

    def GetFileName(self):
        """ GetFileName(self: MgFileFeatureSourceParams) -> str """
        pass

    def GetProviderName(self):
        """ GetProviderName(self: MgFileFeatureSourceParams) -> str """
        pass

    def GetSpatialContextDescription(self):
        """ GetSpatialContextDescription(self: MgFileFeatureSourceParams) -> str """
        pass

    def GetSpatialContextName(self):
        """ GetSpatialContextName(self: MgFileFeatureSourceParams) -> str """
        pass

    def GetXYTolerance(self):
        """ GetXYTolerance(self: MgFileFeatureSourceParams) -> float """
        pass

    def GetZTolerance(self):
        """ GetZTolerance(self: MgFileFeatureSourceParams) -> float """
        pass

    def SetCoordinateSystemWkt(self, srsWkt):
        """ SetCoordinateSystemWkt(self: MgFileFeatureSourceParams, srsWkt: str) """
        pass

    def SetFeatureSchema(self, featureSchema):
        """ SetFeatureSchema(self: MgFileFeatureSourceParams, featureSchema: MgFeatureSchema) """
        pass

    def SetFileName(self, name):
        """ SetFileName(self: MgFileFeatureSourceParams, name: str) """
        pass

    def SetProviderName(self, name):
        """ SetProviderName(self: MgFileFeatureSourceParams, name: str) """
        pass

    def SetSpatialContextDescription(self, description):
        """ SetSpatialContextDescription(self: MgFileFeatureSourceParams, description: str) """
        pass

    def SetSpatialContextName(self, name):
        """ SetSpatialContextName(self: MgFileFeatureSourceParams, name: str) """
        pass

    def SetXYTolerance(self, tolerance):
        """ SetXYTolerance(self: MgFileFeatureSourceParams, tolerance: float) """
        pass

    def SetZTolerance(self, tolerance):
        """ SetZTolerance(self: MgFileFeatureSourceParams, tolerance: float) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, providerName: str)
        __new__(cls: type, providerName: str, spatialContextName: str, srsWkt: str, featureSchema: MgFeatureSchema)
        """
        pass

    CoordinateSystemWkt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystemWkt(self: MgFileFeatureSourceParams) -> str

Set: CoordinateSystemWkt(self: MgFileFeatureSourceParams) = value
"""

    FeatureSchema = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureSchema(self: MgFileFeatureSourceParams) -> MgFeatureSchema

Set: FeatureSchema(self: MgFileFeatureSourceParams) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FileName(self: MgFileFeatureSourceParams) -> str

Set: FileName(self: MgFileFeatureSourceParams) = value
"""

    ProviderName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ProviderName(self: MgFileFeatureSourceParams) -> str

Set: ProviderName(self: MgFileFeatureSourceParams) = value
"""

    SpatialContextDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialContextDescription(self: MgFileFeatureSourceParams) -> str

Set: SpatialContextDescription(self: MgFileFeatureSourceParams) = value
"""

    SpatialContextName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialContextName(self: MgFileFeatureSourceParams) -> str

Set: SpatialContextName(self: MgFileFeatureSourceParams) = value
"""

    XYTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XYTolerance(self: MgFileFeatureSourceParams) -> float

Set: XYTolerance(self: MgFileFeatureSourceParams) = value
"""

    ZTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZTolerance(self: MgFileFeatureSourceParams) -> float

Set: ZTolerance(self: MgFileFeatureSourceParams) = value
"""


    swigCMemOwn = None


class MgFileNotFoundException(MgFileIoException):
    """
    MgFileNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgFileNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgFileNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgFileNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgGeoJsonWriter(MgGuardDisposable):
    """
    MgGeoJsonWriter(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeoJsonWriter()
    """
    def Dispose(self):
        """ Dispose(self: MgGeoJsonWriter) """
        pass

    def FeatureToGeoJson(self, *__args):
        """
        FeatureToGeoJson(self: MgGeoJsonWriter, reader: MgReader, transform: MgTransform, idPropertyName: str, geomPropName: str) -> str
        FeatureToGeoJson(self: MgGeoJsonWriter, featureReader: MgFeatureReader, transform: MgTransform) -> str
        """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeoJsonWriter) -> IntPtr """
        pass

    def GetPrecision(self):
        """ GetPrecision(self: MgGeoJsonWriter) -> int """
        pass

    def IsPrecisionEnabled(self):
        """ IsPrecisionEnabled(self: MgGeoJsonWriter) -> bool """
        pass

    def SetPrecision(self, precision):
        """ SetPrecision(self: MgGeoJsonWriter, precision: int) """
        pass

    def SetPrecisionEnabled(self, enabled):
        """ SetPrecisionEnabled(self: MgGeoJsonWriter, enabled: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgGeometricPathInstructionType(object):
    """ MgGeometricPathInstructionType() """
    Close = 4
    LineTo = 1
    MoveTo = 0
    QuadTo = 2


class MgGeometricPropertyDefinition(MgPropertyDefinition):
    """
    MgGeometricPropertyDefinition(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeometricPropertyDefinition(name: str)
    """
    def Dispose(self):
        """ Dispose(self: MgGeometricPropertyDefinition) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometricPropertyDefinition) -> IntPtr """
        pass

    def GetGeometryTypes(self):
        """ GetGeometryTypes(self: MgGeometricPropertyDefinition) -> int """
        pass

    def GetHasElevation(self):
        """ GetHasElevation(self: MgGeometricPropertyDefinition) -> bool """
        pass

    def GetHasMeasure(self):
        """ GetHasMeasure(self: MgGeometricPropertyDefinition) -> bool """
        pass

    def GetReadOnly(self):
        """ GetReadOnly(self: MgGeometricPropertyDefinition) -> bool """
        pass

    def GetSpatialContextAssociation(self):
        """ GetSpatialContextAssociation(self: MgGeometricPropertyDefinition) -> str """
        pass

    def GetSpecificGeometryTypes(self):
        """ GetSpecificGeometryTypes(self: MgGeometricPropertyDefinition) -> MgGeometryTypeInfo """
        pass

    def SetGeometryTypes(self, types):
        """ SetGeometryTypes(self: MgGeometricPropertyDefinition, types: int) """
        pass

    def SetHasElevation(self, hasElevation):
        """ SetHasElevation(self: MgGeometricPropertyDefinition, hasElevation: bool) """
        pass

    def SetHasMeasure(self, hasMeasure):
        """ SetHasMeasure(self: MgGeometricPropertyDefinition, hasMeasure: bool) """
        pass

    def SetReadOnly(self, value):
        """ SetReadOnly(self: MgGeometricPropertyDefinition, value: bool) """
        pass

    def SetSpatialContextAssociation(self, spatialContextName):
        """ SetSpatialContextAssociation(self: MgGeometricPropertyDefinition, spatialContextName: str) """
        pass

    def SetSpecificGeometryTypes(self, typeInfo):
        """ SetSpecificGeometryTypes(self: MgGeometricPropertyDefinition, typeInfo: MgGeometryTypeInfo) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    GeometryTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryTypes(self: MgGeometricPropertyDefinition) -> int

Set: GeometryTypes(self: MgGeometricPropertyDefinition) = value
"""

    HasElevation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasElevation(self: MgGeometricPropertyDefinition) -> bool

Set: HasElevation(self: MgGeometricPropertyDefinition) = value
"""

    HasMeasure = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasMeasure(self: MgGeometricPropertyDefinition) -> bool

Set: HasMeasure(self: MgGeometricPropertyDefinition) = value
"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: MgGeometricPropertyDefinition) -> bool

Set: ReadOnly(self: MgGeometricPropertyDefinition) = value
"""

    SpatialContextAssociation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialContextAssociation(self: MgGeometricPropertyDefinition) -> str

Set: SpatialContextAssociation(self: MgGeometricPropertyDefinition) = value
"""

    SpecificGeometryTypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpecificGeometryTypes(self: MgGeometricPropertyDefinition) -> MgGeometryTypeInfo

Set: SpecificGeometryTypes(self: MgGeometricPropertyDefinition) = value
"""


    swigCMemOwn = None


class MgGeometryCollection(MgGuardDisposable):
    """
    MgGeometryCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeometryCollection()
    """
    def Add(self, value):
        """ Add(self: MgGeometryCollection, value: MgGeometry) """
        pass

    def Clear(self):
        """ Clear(self: MgGeometryCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgGeometryCollection, value: MgGeometry) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgGeometryCollection, array: Array[MgGeometry], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgGeometryCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgGeometryCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometryCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgGeometryCollection) -> IEnumerator[MgGeometry] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgGeometryCollection, index: int) -> MgGeometry """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgGeometryCollection, value: MgGeometry) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgGeometryCollection, index: int, value: MgGeometry) """
        pass

    def Remove(self, value):
        """ Remove(self: MgGeometryCollection, value: MgGeometry) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgGeometryCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgGeometryCollection, index: int, value: MgGeometry) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgGeometry], item: MgGeometry) -> bool """
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
    """Get: Count(self: MgGeometryCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgGeometryCollection) -> bool

"""


    MgGeometryCollectionEnumerator = None
    swigCMemOwn = None


class MgGeometryComponentType(object):
    """ MgGeometryComponentType() """
    ArcSegment = 130
    CurveRing = 132
    LinearRing = 129
    LinearSegment = 131


class MgGeometryEntityType(object):
    """ MgGeometryEntityType() """
    Geometry = 1
    GeometryComponent = 0


class MgGeometryException(MgThirdPartyException):
    """
    MgGeometryException(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeometryException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgGeometryException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometryException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgGeometryFactory(MgGuardDisposable):
    """
    MgGeometryFactory(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeometryFactory()
    """
    def CreateArcSegment(self, start, end, control):
        """ CreateArcSegment(self: MgGeometryFactory, start: MgCoordinate, end: MgCoordinate, control: MgCoordinate) -> MgArcSegment """
        pass

    def CreateCoordinateXY(self, x, y):
        """ CreateCoordinateXY(self: MgGeometryFactory, x: float, y: float) -> MgCoordinate """
        pass

    def CreateCoordinateXYM(self, x, y, m):
        """ CreateCoordinateXYM(self: MgGeometryFactory, x: float, y: float, m: float) -> MgCoordinate """
        pass

    def CreateCoordinateXYZ(self, x, y, z):
        """ CreateCoordinateXYZ(self: MgGeometryFactory, x: float, y: float, z: float) -> MgCoordinate """
        pass

    def CreateCoordinateXYZM(self, x, y, z, m):
        """ CreateCoordinateXYZM(self: MgGeometryFactory, x: float, y: float, z: float, m: float) -> MgCoordinate """
        pass

    def CreateCurvePolygon(self, outerRing, innerRings):
        """ CreateCurvePolygon(self: MgGeometryFactory, outerRing: MgCurveRing, innerRings: MgCurveRingCollection) -> MgCurvePolygon """
        pass

    def CreateCurveRing(self, curveSegments):
        """ CreateCurveRing(self: MgGeometryFactory, curveSegments: MgCurveSegmentCollection) -> MgCurveRing """
        pass

    def CreateCurveString(self, curveSegments):
        """ CreateCurveString(self: MgGeometryFactory, curveSegments: MgCurveSegmentCollection) -> MgCurveString """
        pass

    def CreateLinearRing(self, coordinates):
        """ CreateLinearRing(self: MgGeometryFactory, coordinates: MgCoordinateCollection) -> MgLinearRing """
        pass

    def CreateLinearSegment(self, coordinates):
        """ CreateLinearSegment(self: MgGeometryFactory, coordinates: MgCoordinateCollection) -> MgLinearSegment """
        pass

    def CreateLineString(self, coordinates):
        """ CreateLineString(self: MgGeometryFactory, coordinates: MgCoordinateCollection) -> MgLineString """
        pass

    def CreateMultiCurvePolygon(self, polygons):
        """ CreateMultiCurvePolygon(self: MgGeometryFactory, polygons: MgCurvePolygonCollection) -> MgMultiCurvePolygon """
        pass

    def CreateMultiCurveString(self, curveStrings):
        """ CreateMultiCurveString(self: MgGeometryFactory, curveStrings: MgCurveStringCollection) -> MgMultiCurveString """
        pass

    def CreateMultiGeometry(self, geometries):
        """ CreateMultiGeometry(self: MgGeometryFactory, geometries: MgGeometryCollection) -> MgMultiGeometry """
        pass

    def CreateMultiLineString(self, lineStrings):
        """ CreateMultiLineString(self: MgGeometryFactory, lineStrings: MgLineStringCollection) -> MgMultiLineString """
        pass

    def CreateMultiPoint(self, points):
        """ CreateMultiPoint(self: MgGeometryFactory, points: MgPointCollection) -> MgMultiPoint """
        pass

    def CreateMultiPolygon(self, polygons):
        """ CreateMultiPolygon(self: MgGeometryFactory, polygons: MgPolygonCollection) -> MgMultiPolygon """
        pass

    def CreatePoint(self, coordinate):
        """ CreatePoint(self: MgGeometryFactory, coordinate: MgCoordinate) -> MgPoint """
        pass

    def CreatePolygon(self, outerRing, innerRings):
        """ CreatePolygon(self: MgGeometryFactory, outerRing: MgLinearRing, innerRings: MgLinearRingCollection) -> MgPolygon """
        pass

    def Dispose(self):
        """ Dispose(self: MgGeometryFactory) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometryFactory) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgGeometryProperty(MgNullableProperty):
    """
    MgGeometryProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeometryProperty(name: str, value: MgByteReader)
    """
    def Dispose(self):
        """ Dispose(self: MgGeometryProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometryProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgGeometryProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgGeometryProperty) -> MgByteReader """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgGeometryProperty, value: MgByteReader) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: MgByteReader)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgGeometryProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgGeometryProperty) -> MgByteReader

Set: Value(self: MgGeometryProperty) = value
"""


    swigCMemOwn = None


class MgGeometrySimplificationAlgorithmType(object):
    """ MgGeometrySimplificationAlgorithmType() """
    DouglasPeucker = 0
    TopologyPreserving = 1


class MgGeometrySimplifier(MgGuardDisposable):
    """
    MgGeometrySimplifier(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeometrySimplifier()
    """
    def Dispose(self):
        """ Dispose(self: MgGeometrySimplifier) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometrySimplifier) -> IntPtr """
        pass

    def Simplify(self, geom, tolerance, algorithm):
        """ Simplify(self: MgGeometrySimplifier, geom: MgGeometry, tolerance: float, algorithm: int) -> MgGeometry """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgGeometryType(object):
    """ MgGeometryType() """
    CurvePolygon = 11
    CurveString = 10
    LineString = 2
    MultiCurvePolygon = 13
    MultiCurveString = 12
    MultiGeometry = 7
    MultiLineString = 5
    MultiPoint = 4
    MultiPolygon = 6
    Point = 1
    Polygon = 3


class MgGeometryTypeInfo(MgSerializable):
    """
    MgGeometryTypeInfo(cPtr: IntPtr, cMemoryOwn: bool)
    MgGeometryTypeInfo()
    """
    def Dispose(self):
        """ Dispose(self: MgGeometryTypeInfo) """
        pass

    def GetCount(self):
        """ GetCount(self: MgGeometryTypeInfo) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGeometryTypeInfo) -> IntPtr """
        pass

    def GetType(self, index=None):
        """ GetType(self: MgGeometryTypeInfo, index: int) -> int """
        pass

    def SetTypes(self, types):
        """ SetTypes(self: MgGeometryTypeInfo, types: MgIntCollection) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgGroup(object):
    """ MgGroup() """
    Everyone = 'Everyone'


class MgGwsFeatureReader(MgFeatureReader):
    """ MgGwsFeatureReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgGwsFeatureReader) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgGwsFeatureReader) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgIndexOutOfRangeException(MgOutOfRangeException):
    """
    MgIndexOutOfRangeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgIndexOutOfRangeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgIndexOutOfRangeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgIndexOutOfRangeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInsertFeatures(MgFeatureCommand):
    """
    MgInsertFeatures(cPtr: IntPtr, cMemoryOwn: bool)
    MgInsertFeatures(className: str, propertyValues: MgPropertyCollection)
    MgInsertFeatures(className: str, propertyValueCollection: MgBatchPropertyCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInsertFeatures) """
        pass

    def GetCommandType(self):
        """ GetCommandType(self: MgInsertFeatures) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInsertFeatures) -> IntPtr """
        pass

    def GetFeatureClassName(self):
        """ GetFeatureClassName(self: MgInsertFeatures) -> str """
        pass

    def GetPropertyValues(self):
        """ GetPropertyValues(self: MgInsertFeatures) -> MgPropertyCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, className: str, propertyValues: MgPropertyCollection)
        __new__(cls: type, className: str, propertyValueCollection: MgBatchPropertyCollection)
        """
        pass

    CommandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandType(self: MgInsertFeatures) -> int

"""

    FeatureClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureClassName(self: MgInsertFeatures) -> str

"""

    PropertyValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyValues(self: MgInsertFeatures) -> MgPropertyCollection

"""


    swigCMemOwn = None


class MgInt16Property(MgNullableProperty):
    """
    MgInt16Property(cPtr: IntPtr, cMemoryOwn: bool)
    MgInt16Property(name: str, value: Int16)
    """
    def Dispose(self):
        """ Dispose(self: MgInt16Property) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInt16Property) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgInt16Property) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgInt16Property) -> Int16 """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgInt16Property, value: Int16) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: Int16)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgInt16Property) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgInt16Property) -> Int16

Set: Value(self: MgInt16Property) = value
"""


    swigCMemOwn = None


class MgInt32Property(MgNullableProperty):
    """
    MgInt32Property(cPtr: IntPtr, cMemoryOwn: bool)
    MgInt32Property(name: str, value: int)
    """
    def Dispose(self):
        """ Dispose(self: MgInt32Property) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInt32Property) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgInt32Property) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgInt32Property) -> int """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgInt32Property, value: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: int)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgInt32Property) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgInt32Property) -> int

Set: Value(self: MgInt32Property) = value
"""


    swigCMemOwn = None


class MgInt64Property(MgNullableProperty):
    """
    MgInt64Property(cPtr: IntPtr, cMemoryOwn: bool)
    MgInt64Property(name: str, value: Int64)
    """
    def Dispose(self):
        """ Dispose(self: MgInt64Property) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInt64Property) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgInt64Property) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgInt64Property) -> Int64 """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgInt64Property, value: Int64) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: Int64)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgInt64Property) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgInt64Property) -> Int64

Set: Value(self: MgInt64Property) = value
"""


    swigCMemOwn = None


class MgIntCollection(MgCollection):
    """
    MgIntCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgIntCollection()
    """
    def Add(self, value):
        """ Add(self: MgIntCollection, value: int) """
        pass

    def Clear(self):
        """ Clear(self: MgIntCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgIntCollection, value: int) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgIntCollection, array: Array[int], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgIntCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgIntCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgIntCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgIntCollection) -> IEnumerator[int] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgIntCollection, index: int) -> int """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgIntCollection, value: int) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgIntCollection, index: int, value: int) """
        pass

    def Remove(self, value):
        """ Remove(self: MgIntCollection, value: int) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgIntCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgIntCollection, index: int, value: int) """
        pass

    def ToXml(self):
        """ ToXml(self: MgIntCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[int], item: int) -> bool """
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
    """Get: Count(self: MgIntCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgIntCollection) -> bool

"""


    MgIntCollectionEnumerator = None
    swigCMemOwn = None


class MgInvalidArgumentException(MgSystemException):
    """
    MgInvalidArgumentException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidArgumentException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidArgumentException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidArgumentException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidCastException(MgSystemException):
    """
    MgInvalidCastException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidCastException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidCastException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidCastException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidCoordinateSystemException(MgApplicationException):
    """
    MgInvalidCoordinateSystemException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidCoordinateSystemException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidCoordinateSystemException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidCoordinateSystemException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidCoordinateSystemTypeException(MgApplicationException):
    """
    MgInvalidCoordinateSystemTypeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidCoordinateSystemTypeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidCoordinateSystemTypeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidCoordinateSystemTypeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidCoordinateSystemUnitsException(MgApplicationException):
    """
    MgInvalidCoordinateSystemUnitsException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidCoordinateSystemUnitsException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidCoordinateSystemUnitsException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidCoordinateSystemUnitsException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidMapDefinitionException(MgApplicationException):
    """
    MgInvalidMapDefinitionException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidMapDefinitionException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidMapDefinitionException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidMapDefinitionException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidOperationException(MgSystemException):
    """
    MgInvalidOperationException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidOperationException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidOperationException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidOperationException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidPropertyTypeException(MgSystemException):
    """
    MgInvalidPropertyTypeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidPropertyTypeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidPropertyTypeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidPropertyTypeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidRepositoryNameException(MgApplicationException):
    """
    MgInvalidRepositoryNameException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidRepositoryNameException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidRepositoryNameException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidRepositoryNameException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidRepositoryTypeException(MgApplicationException):
    """
    MgInvalidRepositoryTypeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidRepositoryTypeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidRepositoryTypeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidRepositoryTypeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidResourceDataNameException(MgApplicationException):
    """
    MgInvalidResourceDataNameException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidResourceDataNameException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidResourceDataNameException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidResourceDataNameException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidResourceDataTypeException(MgApplicationException):
    """
    MgInvalidResourceDataTypeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidResourceDataTypeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidResourceDataTypeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidResourceDataTypeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidResourceNameException(MgApplicationException):
    """
    MgInvalidResourceNameException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidResourceNameException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidResourceNameException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidResourceNameException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidResourcePathException(MgApplicationException):
    """
    MgInvalidResourcePathException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidResourcePathException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidResourcePathException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidResourcePathException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidResourcePreProcessingTypeException(MgApplicationException):
    """
    MgInvalidResourcePreProcessingTypeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidResourcePreProcessingTypeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidResourcePreProcessingTypeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidResourcePreProcessingTypeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidResourceTypeException(MgApplicationException):
    """
    MgInvalidResourceTypeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidResourceTypeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidResourceTypeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidResourceTypeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgStreamIoException(MgIoException):
    """
    MgStreamIoException(cPtr: IntPtr, cMemoryOwn: bool)
    MgStreamIoException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgStreamIoException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgStreamIoException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgInvalidStreamHeaderException(MgStreamIoException):
    """
    MgInvalidStreamHeaderException(cPtr: IntPtr, cMemoryOwn: bool)
    MgInvalidStreamHeaderException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgInvalidStreamHeaderException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgInvalidStreamHeaderException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgLayerBase(MgNamedSerializable):
    """
    MgLayerBase(cPtr: IntPtr, cMemoryOwn: bool)
    MgLayerBase(layerDefinition: MgResourceIdentifier, resourceService: MgResourceService)
    """
    def BeginTransaction(self):
        """ BeginTransaction(self: MgLayerBase) -> MgTransaction """
        pass

    def DeleteFeatures(self, filter, transaction):
        """ DeleteFeatures(self: MgLayerBase, filter: str, transaction: MgTransaction) -> int """
        pass

    def Dispose(self):
        """ Dispose(self: MgLayerBase) """
        pass

    def ForceRefresh(self):
        """ ForceRefresh(self: MgLayerBase) """
        pass

    def GetClassDefinition(self):
        """ GetClassDefinition(self: MgLayerBase) -> MgClassDefinition """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLayerBase) -> IntPtr """
        pass

    def GetDisplayInLegend(self):
        """ GetDisplayInLegend(self: MgLayerBase) -> bool """
        pass

    def GetExpandInLegend(self):
        """ GetExpandInLegend(self: MgLayerBase) -> bool """
        pass

    def GetFeatureClassName(self):
        """ GetFeatureClassName(self: MgLayerBase) -> str """
        pass

    def GetFeatureGeometryName(self):
        """ GetFeatureGeometryName(self: MgLayerBase) -> str """
        pass

    def GetFeatureSourceId(self):
        """ GetFeatureSourceId(self: MgLayerBase) -> str """
        pass

    def GetFilter(self):
        """ GetFilter(self: MgLayerBase) -> str """
        pass

    def GetGroup(self):
        """ GetGroup(self: MgLayerBase) -> MgLayerGroup """
        pass

    def GetLayerDefinition(self):
        """ GetLayerDefinition(self: MgLayerBase) -> MgResourceIdentifier """
        pass

    def GetLayerType(self):
        """ GetLayerType(self: MgLayerBase) -> int """
        pass

    def GetLegendLabel(self):
        """ GetLegendLabel(self: MgLayerBase) -> str """
        pass

    def GetName(self):
        """ GetName(self: MgLayerBase) -> str """
        pass

    def GetObjectId(self):
        """ GetObjectId(self: MgLayerBase) -> str """
        pass

    def GetSelectable(self):
        """ GetSelectable(self: MgLayerBase) -> bool """
        pass

    def GetSpatialContexts(self, bActiveOnly):
        """ GetSpatialContexts(self: MgLayerBase, bActiveOnly: bool) -> MgSpatialContextReader """
        pass

    def GetVisible(self):
        """ GetVisible(self: MgLayerBase) -> bool """
        pass

    def InsertFeatures(self, properties, transaction):
        """
        InsertFeatures(self: MgLayerBase, properties: MgBatchPropertyCollection, transaction: MgTransaction) -> MgFeatureReader
        InsertFeatures(self: MgLayerBase, properties: MgPropertyCollection, transaction: MgTransaction) -> MgFeatureReader
        """
        pass

    def IsVisible(self):
        """ IsVisible(self: MgLayerBase) -> bool """
        pass

    def NeedsRefresh(self):
        """ NeedsRefresh(self: MgLayerBase) -> bool """
        pass

    def SelectAggregate(self, options):
        """ SelectAggregate(self: MgLayerBase, options: MgFeatureAggregateOptions) -> MgDataReader """
        pass

    def SelectFeatures(self, options, coordinateSystem=None):
        """
        SelectFeatures(self: MgLayerBase, options: MgFeatureQueryOptions, coordinateSystem: str) -> MgFeatureReader
        SelectFeatures(self: MgLayerBase, options: MgFeatureQueryOptions) -> MgFeatureReader
        """
        pass

    def SetDisplayInLegend(self, displayInLegend):
        """ SetDisplayInLegend(self: MgLayerBase, displayInLegend: bool) """
        pass

    def SetGroup(self, group):
        """ SetGroup(self: MgLayerBase, group: MgLayerGroup) """
        pass

    def SetLayerDefinition(self, layerDefinition, resourceService):
        """ SetLayerDefinition(self: MgLayerBase, layerDefinition: MgResourceIdentifier, resourceService: MgResourceService) """
        pass

    def SetLegendLabel(self, legendLabel):
        """ SetLegendLabel(self: MgLayerBase, legendLabel: str) """
        pass

    def SetName(self, name):
        """ SetName(self: MgLayerBase, name: str) """
        pass

    def SetSelectable(self, selectable):
        """ SetSelectable(self: MgLayerBase, selectable: bool) """
        pass

    def SetVisible(self, visible):
        """ SetVisible(self: MgLayerBase, visible: bool) """
        pass

    def UpdateFeatures(self, commands, transaction=None):
        """
        UpdateFeatures(self: MgLayerBase, commands: MgFeatureCommandCollection, transaction: MgTransaction) -> MgPropertyCollection
        UpdateFeatures(self: MgLayerBase, commands: MgFeatureCommandCollection) -> MgPropertyCollection
        """
        pass

    def UpdateMatchingFeatures(self, properties, filter, transaction):
        """ UpdateMatchingFeatures(self: MgLayerBase, properties: MgPropertyCollection, filter: str, transaction: MgTransaction) -> int """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, layerDefinition: MgResourceIdentifier, resourceService: MgResourceService)
        """
        pass

    DisplayInLegend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayInLegend(self: MgLayerBase) -> bool

Set: DisplayInLegend(self: MgLayerBase) = value
"""

    ExpandInLegend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpandInLegend(self: MgLayerBase) -> bool

"""

    FeatureClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureClassName(self: MgLayerBase) -> str

"""

    FeatureGeometryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureGeometryName(self: MgLayerBase) -> str

"""

    FeatureSourceId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureSourceId(self: MgLayerBase) -> str

"""

    Filter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filter(self: MgLayerBase) -> str

"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Group(self: MgLayerBase) -> MgLayerGroup

Set: Group(self: MgLayerBase) = value
"""

    LayerDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerDefinition(self: MgLayerBase) -> MgResourceIdentifier

"""

    LayerType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerType(self: MgLayerBase) -> int

"""

    LegendLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendLabel(self: MgLayerBase) -> str

Set: LegendLabel(self: MgLayerBase) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgLayerBase) -> str

Set: Name(self: MgLayerBase) = value
"""

    Selectable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Selectable(self: MgLayerBase) -> bool

Set: Selectable(self: MgLayerBase) = value
"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: MgLayerBase) -> bool

Set: Visible(self: MgLayerBase) = value
"""


    swigCMemOwn = None


class MgLayerCollection(MgGuardDisposable):
    """ MgLayerCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Add(self, value):
        """ Add(self: MgLayerCollection, value: MgLayerBase) """
        pass

    def Clear(self):
        """ Clear(self: MgLayerCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgLayerCollection, value: MgLayerBase) -> bool
        Contains(self: MgLayerCollection, name: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgLayerCollection, array: Array[MgLayerBase], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgLayerCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgLayerCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLayerCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgLayerCollection) -> IEnumerator[MgLayerBase] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: MgLayerCollection, name: str) -> MgLayerBase
        GetItem(self: MgLayerCollection, index: int) -> MgLayerBase
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgLayerCollection, value: MgLayerBase) -> int
        IndexOf(self: MgLayerCollection, name: str) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgLayerCollection, index: int, value: MgLayerBase) """
        pass

    def Remove(self, value):
        """ Remove(self: MgLayerCollection, value: MgLayerBase) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgLayerCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgLayerCollection, index: int, value: MgLayerBase) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgLayerBase], item: MgLayerBase) -> bool """
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
    """Get: Count(self: MgLayerCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgLayerCollection) -> bool

"""


    MgLayerCollectionEnumerator = None
    swigCMemOwn = None


class MgLayerGroup(MgNamedSerializable):
    """
    MgLayerGroup(cPtr: IntPtr, cMemoryOwn: bool)
    MgLayerGroup(name: str)
    """
    def Dispose(self):
        """ Dispose(self: MgLayerGroup) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLayerGroup) -> IntPtr """
        pass

    def GetDisplayInLegend(self):
        """ GetDisplayInLegend(self: MgLayerGroup) -> bool """
        pass

    def GetExpandInLegend(self):
        """ GetExpandInLegend(self: MgLayerGroup) -> bool """
        pass

    def GetGroup(self):
        """ GetGroup(self: MgLayerGroup) -> MgLayerGroup """
        pass

    def GetLayerGroupType(self):
        """ GetLayerGroupType(self: MgLayerGroup) -> int """
        pass

    def GetLegendLabel(self):
        """ GetLegendLabel(self: MgLayerGroup) -> str """
        pass

    def GetName(self):
        """ GetName(self: MgLayerGroup) -> str """
        pass

    def GetObjectId(self):
        """ GetObjectId(self: MgLayerGroup) -> str """
        pass

    def GetVisible(self):
        """ GetVisible(self: MgLayerGroup) -> bool """
        pass

    def IsVisible(self):
        """ IsVisible(self: MgLayerGroup) -> bool """
        pass

    def SetDisplayInLegend(self, displayInLegend):
        """ SetDisplayInLegend(self: MgLayerGroup, displayInLegend: bool) """
        pass

    def SetExpandInLegend(self, expandInLegend):
        """ SetExpandInLegend(self: MgLayerGroup, expandInLegend: bool) """
        pass

    def SetGroup(self, group):
        """ SetGroup(self: MgLayerGroup, group: MgLayerGroup) """
        pass

    def SetLegendLabel(self, legendLabel):
        """ SetLegendLabel(self: MgLayerGroup, legendLabel: str) """
        pass

    def SetVisible(self, visible):
        """ SetVisible(self: MgLayerGroup, visible: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    DisplayInLegend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayInLegend(self: MgLayerGroup) -> bool

Set: DisplayInLegend(self: MgLayerGroup) = value
"""

    ExpandInLegend = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpandInLegend(self: MgLayerGroup) -> bool

"""

    Group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Group(self: MgLayerGroup) -> MgLayerGroup

Set: Group(self: MgLayerGroup) = value
"""

    LayerGroupType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LayerGroupType(self: MgLayerGroup) -> int

"""

    LegendLabel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LegendLabel(self: MgLayerGroup) -> str

Set: LegendLabel(self: MgLayerGroup) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgLayerGroup) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: MgLayerGroup) -> bool

Set: Visible(self: MgLayerGroup) = value
"""


    swigCMemOwn = None


class MgLayerGroupCollection(MgGuardDisposable):
    """ MgLayerGroupCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Add(self, value):
        """ Add(self: MgLayerGroupCollection, value: MgLayerGroup) """
        pass

    def Clear(self):
        """ Clear(self: MgLayerGroupCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgLayerGroupCollection, value: MgLayerGroup) -> bool
        Contains(self: MgLayerGroupCollection, name: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgLayerGroupCollection, array: Array[MgLayerGroup], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgLayerGroupCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgLayerGroupCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLayerGroupCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgLayerGroupCollection) -> IEnumerator[MgLayerGroup] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: MgLayerGroupCollection, name: str) -> MgLayerGroup
        GetItem(self: MgLayerGroupCollection, index: int) -> MgLayerGroup
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgLayerGroupCollection, value: MgLayerGroup) -> int
        IndexOf(self: MgLayerGroupCollection, name: str) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgLayerGroupCollection, index: int, value: MgLayerGroup) """
        pass

    def Remove(self, value):
        """ Remove(self: MgLayerGroupCollection, value: MgLayerGroup) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgLayerGroupCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgLayerGroupCollection, index: int, value: MgLayerGroup) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgLayerGroup], item: MgLayerGroup) -> bool """
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
    """Get: Count(self: MgLayerGroupCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgLayerGroupCollection) -> bool

"""


    MgLayerGroupCollectionEnumerator = None
    swigCMemOwn = None


class MgLayerGroupType(object):
    """ MgLayerGroupType() """
    BaseMap = 2
    BaseMapFromTileSet = 3
    Normal = 1


class MgLayerNotFoundException(MgApplicationException):
    """
    MgLayerNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgLayerNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgLayerNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLayerNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgLayerType(object):
    """ MgLayerType() """
    BaseMap = 2
    Dynamic = 1


class MgPrintLayoutElementBase(MgNamedSerializable):
    """ MgPrintLayoutElementBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgPrintLayoutElementBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPrintLayoutElementBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgLegendBase(MgPrintLayoutElementBase):
    """ MgLegendBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgLegendBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLegendBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgLegendItemBase(MgNamedSerializable):
    """ MgLegendItemBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgLegendItemBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLegendItemBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgLegendItemCollection(MgGuardDisposable):
    """ MgLegendItemCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Add(self, value):
        """ Add(self: MgLegendItemCollection, value: MgLegendItemBase) """
        pass

    def Clear(self):
        """ Clear(self: MgLegendItemCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgLegendItemCollection, value: MgLegendItemBase) -> bool
        Contains(self: MgLegendItemCollection, name: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgLegendItemCollection, array: Array[MgLegendItemBase], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgLegendItemCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgLegendItemCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLegendItemCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgLegendItemCollection) -> IEnumerator[MgLegendItemBase] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgLegendItemCollection, index: int) -> MgLegendItemBase """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgLegendItemCollection, value: MgLegendItemBase) -> int
        IndexOf(self: MgLegendItemCollection, name: str) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgLegendItemCollection, index: int, value: MgLegendItemBase) """
        pass

    def Remove(self, value):
        """ Remove(self: MgLegendItemCollection, value: MgLegendItemBase) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgLegendItemCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgLegendItemCollection, index: int, value: MgLegendItemBase) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MgLegendItemBase](enumerable: IEnumerable[MgLegendItemBase], value: MgLegendItemBase) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
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
    """Get: Count(self: MgLegendItemCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgLegendItemCollection) -> bool

"""


    MgLegendItemCollectionEnumerator = None
    swigCMemOwn = None


class MgLengthException(MgSystemException):
    """
    MgLengthException(cPtr: IntPtr, cMemoryOwn: bool)
    MgLengthException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgLengthException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLengthException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgLinearRing(MgRing):
    """ MgLinearRing(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgLinearRing) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgLinearRing) """
        pass

    def GetComponentType(self):
        """ GetComponentType(self: MgLinearRing) -> int """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgLinearRing) -> MgCoordinateIterator """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLinearRing) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgLinearRing) -> int """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgLinearRing) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgLinearRing) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgLinearRing, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: MgLinearRing) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgLinearRing) -> int

"""


    swigCMemOwn = None


class MgLinearRingCollection(MgGuardDisposable):
    """
    MgLinearRingCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgLinearRingCollection()
    """
    def Add(self, value):
        """ Add(self: MgLinearRingCollection, value: MgLinearRing) """
        pass

    def Clear(self):
        """ Clear(self: MgLinearRingCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgLinearRingCollection, value: MgLinearRing) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgLinearRingCollection, array: Array[MgLinearRing], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgLinearRingCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgLinearRingCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLinearRingCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgLinearRingCollection) -> IEnumerator[MgLinearRing] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgLinearRingCollection, index: int) -> MgLinearRing """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgLinearRingCollection, value: MgLinearRing) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgLinearRingCollection, index: int, value: MgLinearRing) """
        pass

    def Remove(self, value):
        """ Remove(self: MgLinearRingCollection, value: MgLinearRing) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgLinearRingCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgLinearRingCollection, index: int, value: MgLinearRing) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgLinearRing], item: MgLinearRing) -> bool """
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
    """Get: Count(self: MgLinearRingCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgLinearRingCollection) -> bool

"""


    MgLinearRingCollectionEnumerator = None
    swigCMemOwn = None


class MgLinearSegment(MgCurveSegment):
    """ MgLinearSegment(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgLinearSegment) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgLinearSegment) """
        pass

    def GetComponentType(self):
        """ GetComponentType(self: MgLinearSegment) -> int """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgLinearSegment) -> MgCoordinateIterator """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLinearSegment) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgLinearSegment) -> int """
        pass

    def GetEndCoordinate(self):
        """ GetEndCoordinate(self: MgLinearSegment) -> MgCoordinate """
        pass

    def GetStartCoordinate(self):
        """ GetStartCoordinate(self: MgLinearSegment) -> MgCoordinate """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgLinearSegment) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgLinearSegment) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgLinearSegment, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    ComponentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ComponentType(self: MgLinearSegment) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgLinearSegment) -> int

"""

    EndCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndCoordinate(self: MgLinearSegment) -> MgCoordinate

"""

    StartCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCoordinate(self: MgLinearSegment) -> MgCoordinate

"""


    swigCMemOwn = None


class MgLineString(MgCurve):
    """ MgLineString(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgLineString) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgLineString) """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgLineString) -> MgCoordinateIterator """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLineString) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgLineString) -> int """
        pass

    def GetEndCoordinate(self):
        """ GetEndCoordinate(self: MgLineString) -> MgCoordinate """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgLineString) -> int """
        pass

    def GetStartCoordinate(self):
        """ GetStartCoordinate(self: MgLineString) -> MgCoordinate """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgLineString) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgLineString) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgLineString, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgLineString) -> int

"""

    EndCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndCoordinate(self: MgLineString) -> MgCoordinate

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgLineString) -> int

"""

    StartCoordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartCoordinate(self: MgLineString) -> MgCoordinate

"""


    swigCMemOwn = None


class MgLineStringCollection(MgGuardDisposable):
    """
    MgLineStringCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgLineStringCollection()
    """
    def Add(self, value):
        """ Add(self: MgLineStringCollection, value: MgLineString) """
        pass

    def Clear(self):
        """ Clear(self: MgLineStringCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgLineStringCollection, value: MgLineString) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgLineStringCollection, array: Array[MgLineString], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgLineStringCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgLineStringCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLineStringCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgLineStringCollection) -> IEnumerator[MgLineString] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgLineStringCollection, index: int) -> MgLineString """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgLineStringCollection, value: MgLineString) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgLineStringCollection, index: int, value: MgLineString) """
        pass

    def Remove(self, value):
        """ Remove(self: MgLineStringCollection, value: MgLineString) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgLineStringCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgLineStringCollection, index: int, value: MgLineString) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgLineString], item: MgLineString) -> bool """
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
    """Get: Count(self: MgLineStringCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgLineStringCollection) -> bool

"""


    MgLineStringCollectionEnumerator = None
    swigCMemOwn = None


class MgLockFeatures(MgFeatureCommand):
    """
    MgLockFeatures(cPtr: IntPtr, cMemoryOwn: bool)
    MgLockFeatures(className: str, filterText: str)
    """
    def Dispose(self):
        """ Dispose(self: MgLockFeatures) """
        pass

    def GetCommandType(self):
        """ GetCommandType(self: MgLockFeatures) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLockFeatures) -> IntPtr """
        pass

    def GetFeatureClassName(self):
        """ GetFeatureClassName(self: MgLockFeatures) -> str """
        pass

    def GetFilterText(self):
        """ GetFilterText(self: MgLockFeatures) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, className: str, filterText: str)
        """
        pass

    CommandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandType(self: MgLockFeatures) -> int

"""

    FeatureClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureClassName(self: MgLockFeatures) -> str

"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterText(self: MgLockFeatures) -> str

"""


    swigCMemOwn = None


class MgLogicException(MgSystemException):
    """
    MgLogicException(cPtr: IntPtr, cMemoryOwn: bool)
    MgLogicException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgLogicException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLogicException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgLongTransactionReader(MgSerializable):
    """ MgLongTransactionReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Close(self):
        """ Close(self: MgLongTransactionReader) """
        pass

    def Dispose(self):
        """ Dispose(self: MgLongTransactionReader) """
        pass

    def GetChildren(self):
        """ GetChildren(self: MgLongTransactionReader) -> MgLongTransactionReader """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgLongTransactionReader) -> IntPtr """
        pass

    def GetCreationDate(self):
        """ GetCreationDate(self: MgLongTransactionReader) -> MgDateTime """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgLongTransactionReader) -> str """
        pass

    def GetName(self):
        """ GetName(self: MgLongTransactionReader) -> str """
        pass

    def GetOwner(self):
        """ GetOwner(self: MgLongTransactionReader) -> str """
        pass

    def GetParents(self):
        """ GetParents(self: MgLongTransactionReader) -> MgLongTransactionReader """
        pass

    def IsActive(self):
        """ IsActive(self: MgLongTransactionReader) -> bool """
        pass

    def IsFrozen(self):
        """ IsFrozen(self: MgLongTransactionReader) -> bool """
        pass

    def ReadNext(self):
        """ ReadNext(self: MgLongTransactionReader) -> bool """
        pass

    def ToXml(self):
        """ ToXml(self: MgLongTransactionReader) -> MgByteReader """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Children = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Children(self: MgLongTransactionReader) -> MgLongTransactionReader

"""

    CreationDate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CreationDate(self: MgLongTransactionReader) -> MgDateTime

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgLongTransactionReader) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgLongTransactionReader) -> str

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: MgLongTransactionReader) -> str

"""

    Parents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parents(self: MgLongTransactionReader) -> MgLongTransactionReader

"""


    swigCMemOwn = None


class MgResource(MgNamedSerializable):
    """ MgResource(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgResource) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResource) -> IntPtr """
        pass

    def GetResourceId(self):
        """ GetResourceId(self: MgResource) -> MgResourceIdentifier """
        pass

    def Open(self, resourceService, resourceId):
        """ Open(self: MgResource, resourceService: MgResourceService, resourceId: MgResourceIdentifier) """
        pass

    def Save(self, resourceService, resourceId=None):
        """ Save(self: MgResource, resourceService: MgResourceService, resourceId: MgResourceIdentifier)Save(self: MgResource, resourceService: MgResourceService) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgMapBase(MgResource):
    """
    MgMapBase(cPtr: IntPtr, cMemoryOwn: bool)
    MgMapBase()
    """
    def Create(self, *__args):
        """ Create(self: MgMapBase, mapSRS: str, mapExtent: MgEnvelope, mapName: str)Create(self: MgMapBase, resourceService: MgResourceService, mapDefinition: MgResourceIdentifier, mapName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: MgMapBase) """
        pass

    def GetBackgroundColor(self):
        """ GetBackgroundColor(self: MgMapBase) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMapBase) -> IntPtr """
        pass

    def GetDataExtent(self):
        """ GetDataExtent(self: MgMapBase) -> MgEnvelope """
        pass

    def GetDisplayDpi(self):
        """ GetDisplayDpi(self: MgMapBase) -> int """
        pass

    def GetDisplayHeight(self):
        """ GetDisplayHeight(self: MgMapBase) -> int """
        pass

    def GetDisplayWidth(self):
        """ GetDisplayWidth(self: MgMapBase) -> int """
        pass

    def GetFiniteDisplayScaleAt(self, index):
        """ GetFiniteDisplayScaleAt(self: MgMapBase, index: int) -> float """
        pass

    def GetFiniteDisplayScaleCount(self):
        """ GetFiniteDisplayScaleCount(self: MgMapBase) -> int """
        pass

    def GetLayerGroups(self):
        """ GetLayerGroups(self: MgMapBase) -> MgLayerGroupCollection """
        pass

    def GetLayers(self):
        """ GetLayers(self: MgMapBase) -> MgLayerCollection """
        pass

    def GetMapDefinition(self):
        """ GetMapDefinition(self: MgMapBase) -> MgResourceIdentifier """
        pass

    def GetMapExtent(self):
        """ GetMapExtent(self: MgMapBase) -> MgEnvelope """
        pass

    def GetMapSRS(self):
        """ GetMapSRS(self: MgMapBase) -> str """
        pass

    def GetName(self):
        """ GetName(self: MgMapBase) -> str """
        pass

    def GetObjectId(self):
        """ GetObjectId(self: MgMapBase) -> str """
        pass

    def GetSessionId(self):
        """ GetSessionId(self: MgMapBase) -> str """
        pass

    def GetViewCenter(self):
        """ GetViewCenter(self: MgMapBase) -> MgPoint """
        pass

    def GetViewScale(self):
        """ GetViewScale(self: MgMapBase) -> float """
        pass

    def Open(self, resourceService, *__args):
        """ Open(self: MgMapBase, resourceService: MgResourceService, mapName: str) """
        pass

    def SetDisplayDpi(self, dpi):
        """ SetDisplayDpi(self: MgMapBase, dpi: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    DataExtent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataExtent(self: MgMapBase) -> MgEnvelope

"""

    DisplayDpi = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayDpi(self: MgMapBase) -> int

Set: DisplayDpi(self: MgMapBase) = value
"""

    DisplayHeight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayHeight(self: MgMapBase) -> int

"""

    DisplayWidth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DisplayWidth(self: MgMapBase) -> int

"""

    FiniteDisplayScaleCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FiniteDisplayScaleCount(self: MgMapBase) -> int

"""

    MapDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MapDefinition(self: MgMapBase) -> MgResourceIdentifier

"""

    MapExtent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MapExtent(self: MgMapBase) -> MgEnvelope

"""

    MapSRS = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MapSRS(self: MgMapBase) -> str

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgMapBase) -> str

"""

    SessionId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SessionId(self: MgMapBase) -> str

"""

    ViewCenter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewCenter(self: MgMapBase) -> MgPoint

"""

    ViewScale = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ViewScale(self: MgMapBase) -> float

"""


    swigCMemOwn = None


class MgMapCollection(MgGuardDisposable):
    """
    MgMapCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgMapCollection()
    """
    def Add(self, value):
        """ Add(self: MgMapCollection, value: MgMapBase) """
        pass

    def Clear(self):
        """ Clear(self: MgMapCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgMapCollection, value: MgMapBase) -> bool
        Contains(self: MgMapCollection, name: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgMapCollection, array: Array[MgMapBase], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgMapCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgMapCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMapCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgMapCollection) -> IEnumerator[MgMapBase] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: MgMapCollection, name: str) -> MgMapBase
        GetItem(self: MgMapCollection, index: int) -> MgMapBase
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgMapCollection, value: MgMapBase) -> int
        IndexOf(self: MgMapCollection, name: str) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgMapCollection, index: int, value: MgMapBase) """
        pass

    def Remove(self, value):
        """ Remove(self: MgMapCollection, value: MgMapBase) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgMapCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgMapCollection, index: int, value: MgMapBase) """
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
    """Get: Count(self: MgMapCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgMapCollection) -> bool

"""


    MgMapCollectionEnumerator = None
    swigCMemOwn = None


class MgMapView(MgSerializable):
    """ MgMapView(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgMapView) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMapView) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgMapViewportBase(MgPrintLayoutElementBase):
    """ MgMapViewportBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgMapViewportBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMapViewportBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgMimeType(object):
    """ MgMimeType() """
    Agf = 'application/agf'
    Binary = 'application/octet-stream'
    Dwf = 'model/vnd.dwf'
    Gif = 'image/gif'
    Html = 'text/html'
    Jpeg = 'image/jpeg'
    Json = 'application/json'
    Kml = 'application/vnd.google-earth.kml+xml'
    Kmz = 'application/vnd.google-earth.kmz'
    Png = 'image/png'
    Text = 'text/plain'
    Tiff = 'image/tiff'
    Xml = 'text/xml'


class MgMultiCurvePolygon(MgAggregateGeometry):
    """ MgMultiCurvePolygon(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgMultiCurvePolygon) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgMultiCurvePolygon) """
        pass

    def GetCount(self):
        """ GetCount(self: MgMultiCurvePolygon) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMultiCurvePolygon) -> IntPtr """
        pass

    def GetCurvePolygon(self, index):
        """ GetCurvePolygon(self: MgMultiCurvePolygon, index: int) -> MgCurvePolygon """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgMultiCurvePolygon) -> int """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgMultiCurvePolygon) -> int """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgMultiCurvePolygon) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgMultiCurvePolygon) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgMultiCurvePolygon, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgMultiCurvePolygon) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgMultiCurvePolygon) -> int

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgMultiCurvePolygon) -> int

"""


    swigCMemOwn = None


class MgMultiCurveString(MgAggregateGeometry):
    """ MgMultiCurveString(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgMultiCurveString) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgMultiCurveString) """
        pass

    def GetCount(self):
        """ GetCount(self: MgMultiCurveString) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMultiCurveString) -> IntPtr """
        pass

    def GetCurveString(self, index):
        """ GetCurveString(self: MgMultiCurveString, index: int) -> MgCurveString """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgMultiCurveString) -> int """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgMultiCurveString) -> int """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgMultiCurveString) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgMultiCurveString) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgMultiCurveString, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgMultiCurveString) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgMultiCurveString) -> int

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgMultiCurveString) -> int

"""


    swigCMemOwn = None


class MgMultiGeometry(MgAggregateGeometry):
    """ MgMultiGeometry(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgMultiGeometry) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgMultiGeometry) """
        pass

    def GetCount(self):
        """ GetCount(self: MgMultiGeometry) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMultiGeometry) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgMultiGeometry) -> int """
        pass

    def GetGeometry(self, index):
        """ GetGeometry(self: MgMultiGeometry, index: int) -> MgGeometry """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgMultiGeometry) -> int """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgMultiGeometry) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgMultiGeometry) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgMultiGeometry, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgMultiGeometry) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgMultiGeometry) -> int

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgMultiGeometry) -> int

"""


    swigCMemOwn = None


class MgMultiLineString(MgAggregateGeometry):
    """ MgMultiLineString(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgMultiLineString) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgMultiLineString) """
        pass

    def GetCount(self):
        """ GetCount(self: MgMultiLineString) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMultiLineString) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgMultiLineString) -> int """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgMultiLineString) -> int """
        pass

    def GetLineString(self, index):
        """ GetLineString(self: MgMultiLineString, index: int) -> MgLineString """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgMultiLineString) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgMultiLineString) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgMultiLineString, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgMultiLineString) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgMultiLineString) -> int

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgMultiLineString) -> int

"""


    swigCMemOwn = None


class MgMultiPoint(MgAggregateGeometry):
    """ MgMultiPoint(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgMultiPoint) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgMultiPoint) """
        pass

    def GetCount(self):
        """ GetCount(self: MgMultiPoint) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMultiPoint) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgMultiPoint) -> int """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgMultiPoint) -> int """
        pass

    def GetPoint(self, index):
        """ GetPoint(self: MgMultiPoint, index: int) -> MgPoint """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgMultiPoint) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgMultiPoint) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgMultiPoint, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgMultiPoint) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgMultiPoint) -> int

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgMultiPoint) -> int

"""


    swigCMemOwn = None


class MgMultiPolygon(MgAggregateGeometry):
    """ MgMultiPolygon(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgMultiPolygon) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgMultiPolygon) """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgMultiPolygon) -> MgCoordinateIterator """
        pass

    def GetCount(self):
        """ GetCount(self: MgMultiPolygon) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgMultiPolygon) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgMultiPolygon) -> int """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgMultiPolygon) -> int """
        pass

    def GetPolygon(self, index):
        """ GetPolygon(self: MgMultiPolygon, index: int) -> MgPolygon """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgMultiPolygon) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgMultiPolygon) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgMultiPolygon, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Coordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coordinates(self: MgMultiPolygon) -> MgCoordinateIterator

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgMultiPolygon) -> int

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgMultiPolygon) -> int

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgMultiPolygon) -> int

"""


    swigCMemOwn = None


class MgNorthArrowBase(MgPrintLayoutElementBase):
    """ MgNorthArrowBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgNorthArrowBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNorthArrowBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgNotFiniteNumberException(MgSystemException):
    """
    MgNotFiniteNumberException(cPtr: IntPtr, cMemoryOwn: bool)
    MgNotFiniteNumberException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgNotFiniteNumberException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNotFiniteNumberException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgNotImplementedException(MgSystemException):
    """
    MgNotImplementedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgNotImplementedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgNotImplementedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNotImplementedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgNullArgumentException(MgSystemException):
    """
    MgNullArgumentException(cPtr: IntPtr, cMemoryOwn: bool)
    MgNullArgumentException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgNullArgumentException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNullArgumentException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgNullPropertyValueException(MgApplicationException):
    """
    MgNullPropertyValueException(cPtr: IntPtr, cMemoryOwn: bool)
    MgNullPropertyValueException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgNullPropertyValueException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNullPropertyValueException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgNullReferenceException(MgSystemException):
    """
    MgNullReferenceException(cPtr: IntPtr, cMemoryOwn: bool)
    MgNullReferenceException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgNullReferenceException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgNullReferenceException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgObjectNotFoundException(MgSystemException):
    """
    MgObjectNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgObjectNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgObjectNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgObjectNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgObjectPropertyDefinition(MgPropertyDefinition):
    """
    MgObjectPropertyDefinition(cPtr: IntPtr, cMemoryOwn: bool)
    MgObjectPropertyDefinition(name: str)
    """
    def Dispose(self):
        """ Dispose(self: MgObjectPropertyDefinition) """
        pass

    def GetClassDefinition(self):
        """ GetClassDefinition(self: MgObjectPropertyDefinition) -> MgClassDefinition """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgObjectPropertyDefinition) -> IntPtr """
        pass

    def GetIdentityProperty(self):
        """ GetIdentityProperty(self: MgObjectPropertyDefinition) -> MgDataPropertyDefinition """
        pass

    def GetObjectType(self):
        """ GetObjectType(self: MgObjectPropertyDefinition) -> int """
        pass

    def GetOrderType(self):
        """ GetOrderType(self: MgObjectPropertyDefinition) -> int """
        pass

    def SetClassDefinition(self, classDef):
        """ SetClassDefinition(self: MgObjectPropertyDefinition, classDef: MgClassDefinition) """
        pass

    def SetIdentityProperty(self, propDef):
        """ SetIdentityProperty(self: MgObjectPropertyDefinition, propDef: MgDataPropertyDefinition) """
        pass

    def SetObjectType(self, objType):
        """ SetObjectType(self: MgObjectPropertyDefinition, objType: int) """
        pass

    def SetOrderType(self, orderType):
        """ SetOrderType(self: MgObjectPropertyDefinition, orderType: int) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    ClassDefinition = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ClassDefinition(self: MgObjectPropertyDefinition) -> MgClassDefinition

Set: ClassDefinition(self: MgObjectPropertyDefinition) = value
"""

    IdentityProperty = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IdentityProperty(self: MgObjectPropertyDefinition) -> MgDataPropertyDefinition

Set: IdentityProperty(self: MgObjectPropertyDefinition) = value
"""

    ObjectType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ObjectType(self: MgObjectPropertyDefinition) -> int

Set: ObjectType(self: MgObjectPropertyDefinition) = value
"""

    OrderType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OrderType(self: MgObjectPropertyDefinition) -> int

Set: OrderType(self: MgObjectPropertyDefinition) = value
"""


    swigCMemOwn = None


class MgObjectPropertyType(object):
    """ MgObjectPropertyType() """
    Collection = 1
    OrderedCollection = 2
    Value = 0


class MgOrderingOption(object):
    """ MgOrderingOption() """
    Ascending = 0
    Descending = 1


class MgOutOfMemoryException(MgSystemException):
    """
    MgOutOfMemoryException(cPtr: IntPtr, cMemoryOwn: bool)
    MgOutOfMemoryException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgOutOfMemoryException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgOutOfMemoryException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgOverflowException(MgSystemException):
    """
    MgOverflowException(cPtr: IntPtr, cMemoryOwn: bool)
    MgOverflowException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgOverflowException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgOverflowException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgParameter(MgNamedSerializable):
    """
    MgParameter(cPtr: IntPtr, cMemoryOwn: bool)
    MgParameter(prop: MgNullableProperty)
    MgParameter(prop: MgNullableProperty, direction: int)
    """
    def Dispose(self):
        """ Dispose(self: MgParameter) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgParameter) -> IntPtr """
        pass

    def GetDirection(self):
        """ GetDirection(self: MgParameter) -> int """
        pass

    def GetName(self):
        """ GetName(self: MgParameter) -> str """
        pass

    def GetProperty(self):
        """ GetProperty(self: MgParameter) -> MgNullableProperty """
        pass

    def SetDirection(self, value):
        """ SetDirection(self: MgParameter, value: int) """
        pass

    def SetName(self, name):
        """ SetName(self: MgParameter, name: str) """
        pass

    def SetProperty(self, prop):
        """ SetProperty(self: MgParameter, prop: MgNullableProperty) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, prop: MgNullableProperty)
        __new__(cls: type, prop: MgNullableProperty, direction: int)
        """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgParameter) -> str

Set: Name(self: MgParameter) = value
"""


    swigCMemOwn = None


class MgParameterCollection(MgCollection):
    """
    MgParameterCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgParameterCollection()
    """
    def Add(self, value):
        """ Add(self: MgParameterCollection, value: MgParameter) """
        pass

    def Clear(self):
        """ Clear(self: MgParameterCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgParameterCollection, value: MgParameter) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgParameterCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgParameterCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgParameterCollection) -> IntPtr """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgParameterCollection, index: int) -> MgParameter """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgParameterCollection, value: MgParameter) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgParameterCollection, index: int, value: MgParameter) """
        pass

    def Remove(self, value):
        """ Remove(self: MgParameterCollection, value: MgParameter) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgParameterCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgParameterCollection, index: int, value: MgParameter) """
        pass

    def ToXml(self):
        """ ToXml(self: MgParameterCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
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

    swigCMemOwn = None


class MgParameterDirection(object):
    """ MgParameterDirection() """
    Input = 0
    InputOutput = 2
    Output = 1
    Ret = 3


class MgPlatformNotSupportedException(MgSystemException):
    """
    MgPlatformNotSupportedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgPlatformNotSupportedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgPlatformNotSupportedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPlatformNotSupportedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgPoint(MgGeometry):
    """ MgPoint(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgPoint) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgPoint) """
        pass

    def GetCoordinate(self):
        """ GetCoordinate(self: MgPoint) -> MgCoordinate """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgPoint) -> MgCoordinateIterator """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPoint) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgPoint) -> int """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgPoint) -> int """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgPoint) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgPoint) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgPoint, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Coordinate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coordinate(self: MgPoint) -> MgCoordinate

"""

    Coordinates = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Coordinates(self: MgPoint) -> MgCoordinateIterator

"""

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgPoint) -> int

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgPoint) -> int

"""


    swigCMemOwn = None


class MgPointCollection(MgGuardDisposable):
    """
    MgPointCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgPointCollection()
    """
    def Add(self, value):
        """ Add(self: MgPointCollection, value: MgPoint) """
        pass

    def Clear(self):
        """ Clear(self: MgPointCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgPointCollection, value: MgPoint) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgPointCollection, array: Array[MgPoint], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgPointCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgPointCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPointCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgPointCollection) -> IEnumerator[MgPoint] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgPointCollection, index: int) -> MgPoint """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgPointCollection, value: MgPoint) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgPointCollection, index: int, value: MgPoint) """
        pass

    def Remove(self, value):
        """ Remove(self: MgPointCollection, value: MgPoint) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgPointCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgPointCollection, index: int, value: MgPoint) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgPoint], item: MgPoint) -> bool """
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
    """Get: Count(self: MgPointCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgPointCollection) -> bool

"""


    MgPointCollectionEnumerator = None
    swigCMemOwn = None


class MgPolygon(MgRegion):
    """ MgPolygon(cPtr: IntPtr, cMemoryOwn: bool) """
    def Copy(self):
        """ Copy(self: MgPolygon) -> MgGeometricEntity """
        pass

    def Dispose(self):
        """ Dispose(self: MgPolygon) """
        pass

    def GetCoordinates(self):
        """ GetCoordinates(self: MgPolygon) -> MgCoordinateIterator """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPolygon) -> IntPtr """
        pass

    def GetDimension(self):
        """ GetDimension(self: MgPolygon) -> int """
        pass

    def GetExteriorRing(self):
        """ GetExteriorRing(self: MgPolygon) -> MgLinearRing """
        pass

    def GetGeometryType(self):
        """ GetGeometryType(self: MgPolygon) -> int """
        pass

    def GetInteriorRing(self, index):
        """ GetInteriorRing(self: MgPolygon, index: int) -> MgLinearRing """
        pass

    def GetInteriorRingCount(self):
        """ GetInteriorRingCount(self: MgPolygon) -> int """
        pass

    def IsClosed(self):
        """ IsClosed(self: MgPolygon) -> bool """
        pass

    def IsEmpty(self):
        """ IsEmpty(self: MgPolygon) -> bool """
        pass

    def Transform(self, transform):
        """ Transform(self: MgPolygon, transform: MgTransform) -> MgGeometricEntity """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Dimension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Dimension(self: MgPolygon) -> int

"""

    ExteriorRing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExteriorRing(self: MgPolygon) -> MgLinearRing

"""

    GeometryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GeometryType(self: MgPolygon) -> int

"""

    InteriorRingCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InteriorRingCount(self: MgPolygon) -> int

"""


    swigCMemOwn = None


class MgPolygonCollection(MgGuardDisposable):
    """
    MgPolygonCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgPolygonCollection()
    """
    def Add(self, value):
        """ Add(self: MgPolygonCollection, value: MgPolygon) """
        pass

    def Clear(self):
        """ Clear(self: MgPolygonCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgPolygonCollection, value: MgPolygon) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgPolygonCollection, array: Array[MgPolygon], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgPolygonCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgPolygonCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPolygonCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgPolygonCollection) -> IEnumerator[MgPolygon] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgPolygonCollection, index: int) -> MgPolygon """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgPolygonCollection, value: MgPolygon) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgPolygonCollection, index: int, value: MgPolygon) """
        pass

    def Remove(self, value):
        """ Remove(self: MgPolygonCollection, value: MgPolygon) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgPolygonCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgPolygonCollection, index: int, value: MgPolygon) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgPolygon], item: MgPolygon) -> bool """
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
    """Get: Count(self: MgPolygonCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgPolygonCollection) -> bool

"""


    MgPolygonCollectionEnumerator = None
    swigCMemOwn = None


class MgPreparedGeometry(MgGuardDisposable):
    """ MgPreparedGeometry(cPtr: IntPtr, cMemoryOwn: bool) """
    def Contains(self, other):
        """ Contains(self: MgPreparedGeometry, other: MgGeometry) -> bool """
        pass

    def Crosses(self, other):
        """ Crosses(self: MgPreparedGeometry, other: MgGeometry) -> bool """
        pass

    def Disjoint(self, other):
        """ Disjoint(self: MgPreparedGeometry, other: MgGeometry) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgPreparedGeometry) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPreparedGeometry) -> IntPtr """
        pass

    def Intersects(self, other):
        """ Intersects(self: MgPreparedGeometry, other: MgGeometry) -> bool """
        pass

    def Overlaps(self, other):
        """ Overlaps(self: MgPreparedGeometry, other: MgGeometry) -> bool """
        pass

    def Touches(self, other):
        """ Touches(self: MgPreparedGeometry, other: MgGeometry) -> bool """
        pass

    def Within(self, other):
        """ Within(self: MgPreparedGeometry, other: MgGeometry) -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgPrintLayoutBase(MgResource):
    """ MgPrintLayoutBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgPrintLayoutBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPrintLayoutBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgPrintLayoutCollection(MgGuardDisposable):
    """ MgPrintLayoutCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Contains(self, *__args):
        """
        Contains(self: MgPrintLayoutCollection, value: MgPrintLayoutBase) -> bool
        Contains(self: MgPrintLayoutCollection, name: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgPrintLayoutCollection, array: Array[MgPrintLayoutBase], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgPrintLayoutCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgPrintLayoutCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPrintLayoutCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgPrintLayoutCollection) -> IEnumerator[MgPrintLayoutBase] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: MgPrintLayoutCollection, name: str) -> MgPrintLayoutBase
        GetItem(self: MgPrintLayoutCollection, index: int) -> MgPrintLayoutBase
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgPrintLayoutCollection, value: MgPrintLayoutBase) -> int
        IndexOf(self: MgPrintLayoutCollection, name: str) -> int
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MgPrintLayoutBase](enumerable: IEnumerable[MgPrintLayoutBase], value: MgPrintLayoutBase) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgPrintLayoutCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgPrintLayoutCollection) -> bool

"""


    MgPrintLayoutCollectionEnumerator = None
    swigCMemOwn = None


class MgPrintLayoutElementCollection(MgCollection):
    """ MgPrintLayoutElementCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Add(self, value):
        """ Add(self: MgPrintLayoutElementCollection, value: MgPrintLayoutElementBase) """
        pass

    def Clear(self):
        """ Clear(self: MgPrintLayoutElementCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgPrintLayoutElementCollection, value: MgPrintLayoutElementBase) -> bool
        Contains(self: MgPrintLayoutElementCollection, name: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgPrintLayoutElementCollection, array: Array[MgPrintLayoutElementBase], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgPrintLayoutElementCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgPrintLayoutElementCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPrintLayoutElementCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgPrintLayoutElementCollection) -> IEnumerator[MgPrintLayoutElementBase] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: MgPrintLayoutElementCollection, name: str) -> MgPrintLayoutElementBase
        GetItem(self: MgPrintLayoutElementCollection, index: int) -> MgPrintLayoutElementBase
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgPrintLayoutElementCollection, value: MgPrintLayoutElementBase) -> int
        IndexOf(self: MgPrintLayoutElementCollection, name: str) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgPrintLayoutElementCollection, index: int, value: MgPrintLayoutElementBase) """
        pass

    def Remove(self, value):
        """ Remove(self: MgPrintLayoutElementCollection, value: MgPrintLayoutElementBase) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgPrintLayoutElementCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgPrintLayoutElementCollection, index: int, value: MgPrintLayoutElementBase) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[MgPrintLayoutElementBase](enumerable: IEnumerable[MgPrintLayoutElementBase], value: MgPrintLayoutElementBase) -> bool """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
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
    """Get: Count(self: MgPrintLayoutElementCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgPrintLayoutElementCollection) -> bool

"""


    MgPrintLayoutElementCollectionEnumerator = None
    swigCMemOwn = None


class MgPrintLayoutElementFactoryBase(MgDisposable):
    """ MgPrintLayoutElementFactoryBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgPrintLayoutElementFactoryBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPrintLayoutElementFactoryBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgPrintLayoutServiceBase(MgService):
    """ MgPrintLayoutServiceBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgPrintLayoutServiceBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPrintLayoutServiceBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgPropertyCollection(MgCollection):
    """
    MgPropertyCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgPropertyCollection()
    """
    def Add(self, value):
        """ Add(self: MgPropertyCollection, value: MgProperty) """
        pass

    def Clear(self):
        """ Clear(self: MgPropertyCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgPropertyCollection, name: str) -> bool
        Contains(self: MgPropertyCollection, value: MgProperty) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgPropertyCollection, array: Array[MgProperty], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgPropertyCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgPropertyCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPropertyCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgPropertyCollection) -> IEnumerator[MgProperty] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: MgPropertyCollection, name: str) -> MgProperty
        GetItem(self: MgPropertyCollection, index: int) -> MgProperty
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgPropertyCollection, name: str) -> int
        IndexOf(self: MgPropertyCollection, value: MgProperty) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgPropertyCollection, index: int, value: MgProperty) """
        pass

    def Remove(self, value):
        """ Remove(self: MgPropertyCollection, value: MgProperty) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgPropertyCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgPropertyCollection, index: int, value: MgProperty) """
        pass

    def ToXml(self):
        """ ToXml(self: MgPropertyCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgProperty], item: MgProperty) -> bool """
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
    """Get: Count(self: MgPropertyCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgPropertyCollection) -> bool

"""


    MgPropertyCollectionEnumerator = None
    swigCMemOwn = None


class MgPropertyDefinitionCollection(MgCollection):
    """
    MgPropertyDefinitionCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgPropertyDefinitionCollection()
    """
    def Add(self, value):
        """ Add(self: MgPropertyDefinitionCollection, value: MgPropertyDefinition) """
        pass

    def Clear(self):
        """ Clear(self: MgPropertyDefinitionCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgPropertyDefinitionCollection, name: str) -> bool
        Contains(self: MgPropertyDefinitionCollection, value: MgPropertyDefinition) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgPropertyDefinitionCollection, array: Array[MgPropertyDefinition], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgPropertyDefinitionCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgPropertyDefinitionCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPropertyDefinitionCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgPropertyDefinitionCollection) -> IEnumerator[MgPropertyDefinition] """
        pass

    def GetItem(self, *__args):
        """
        GetItem(self: MgPropertyDefinitionCollection, name: str) -> MgPropertyDefinition
        GetItem(self: MgPropertyDefinitionCollection, index: int) -> MgPropertyDefinition
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgPropertyDefinitionCollection, name: str) -> int
        IndexOf(self: MgPropertyDefinitionCollection, value: MgPropertyDefinition) -> int
        """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgPropertyDefinitionCollection, index: int, value: MgPropertyDefinition) """
        pass

    def Remove(self, value):
        """ Remove(self: MgPropertyDefinitionCollection, value: MgPropertyDefinition) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgPropertyDefinitionCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgPropertyDefinitionCollection, index: int, value: MgPropertyDefinition) """
        pass

    def ToXml(self):
        """ ToXml(self: MgPropertyDefinitionCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgPropertyDefinition], item: MgPropertyDefinition) -> bool """
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
    """Get: Count(self: MgPropertyDefinitionCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgPropertyDefinitionCollection) -> bool

"""


    MgPropertyDefinitionCollectionEnumerator = None
    swigCMemOwn = None


class MgPropertyMapping(MgSerializable):
    """ MgPropertyMapping(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgPropertyMapping) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPropertyMapping) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgPropertyMappingCollection(MgCollection):
    """ MgPropertyMappingCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgPropertyMappingCollection) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgPropertyMappingCollection) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgPropertyType(object):
    """ MgPropertyType() """
    Blob = 10
    Boolean = 1
    Byte = 2
    Clob = 11
    DateTime = 3
    Decimal = 15
    Double = 5
    Feature = 12
    Geometry = 13
    Int16 = 6
    Int32 = 7
    Int64 = 8
    Null = 0
    Raster = 14
    Single = 4
    String = 9


class MgRaster(MgSerializable):
    """ MgRaster(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgRaster) """
        pass

    def GetBitsPerPixel(self):
        """ GetBitsPerPixel(self: MgRaster) -> int """
        pass

    def GetBounds(self):
        """ GetBounds(self: MgRaster) -> MgEnvelope """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgRaster) -> IntPtr """
        pass

    def GetCurrentBand(self):
        """ GetCurrentBand(self: MgRaster) -> int """
        pass

    def GetDataModelType(self):
        """ GetDataModelType(self: MgRaster) -> int """
        pass

    def GetDataType(self):
        """ GetDataType(self: MgRaster) -> Int16 """
        pass

    def GetImageXSize(self):
        """ GetImageXSize(self: MgRaster) -> int """
        pass

    def GetImageYSize(self):
        """ GetImageYSize(self: MgRaster) -> int """
        pass

    def GetNullValue(self):
        """ GetNullValue(self: MgRaster) -> Int64 """
        pass

    def GetNullValueType(self):
        """ GetNullValueType(self: MgRaster) -> int """
        pass

    def GetNumberOfBands(self):
        """ GetNumberOfBands(self: MgRaster) -> int """
        pass

    def GetStream(self):
        """ GetStream(self: MgRaster) -> MgByteReader """
        pass

    def GetVerticalUnits(self):
        """ GetVerticalUnits(self: MgRaster) -> str """
        pass

    def IsNull(self):
        """ IsNull(self: MgRaster) -> bool """
        pass

    def SetImageXSize(self, size):
        """ SetImageXSize(self: MgRaster, size: int) """
        pass

    def SetImageYSize(self, size):
        """ SetImageYSize(self: MgRaster, size: int) """
        pass

    def SetNull(self):
        """ SetNull(self: MgRaster) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    BitsPerPixel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: BitsPerPixel(self: MgRaster) -> int

"""

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Bounds(self: MgRaster) -> MgEnvelope

"""

    DataModelType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DataModelType(self: MgRaster) -> int

"""

    ImageXSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageXSize(self: MgRaster) -> int

Set: ImageXSize(self: MgRaster) = value
"""

    ImageYSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ImageYSize(self: MgRaster) -> int

Set: ImageYSize(self: MgRaster) = value
"""


    swigCMemOwn = None


class MgRasterDataModelType(object):
    """ MgRasterDataModelType() """
    Bitonal = 2
    Data = 1
    Gray = 3
    Palette = 6
    RGB = 4
    RGBA = 5
    Unknown = 0


class MgRasterProperty(MgNullableProperty):
    """
    MgRasterProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgRasterProperty(name: str, value: MgRaster)
    """
    def Dispose(self):
        """ Dispose(self: MgRasterProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgRasterProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgRasterProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgRasterProperty) -> MgRaster """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgRasterProperty, value: MgRaster) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: MgRaster)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgRasterProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgRasterProperty) -> MgRaster

Set: Value(self: MgRasterProperty) = value
"""


    swigCMemOwn = None


class MgRasterPropertyDefinition(MgPropertyDefinition):
    """
    MgRasterPropertyDefinition(cPtr: IntPtr, cMemoryOwn: bool)
    MgRasterPropertyDefinition(name: str)
    """
    def Dispose(self):
        """ Dispose(self: MgRasterPropertyDefinition) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgRasterPropertyDefinition) -> IntPtr """
        pass

    def GetDefaultImageXSize(self):
        """ GetDefaultImageXSize(self: MgRasterPropertyDefinition) -> int """
        pass

    def GetDefaultImageYSize(self):
        """ GetDefaultImageYSize(self: MgRasterPropertyDefinition) -> int """
        pass

    def GetNullable(self):
        """ GetNullable(self: MgRasterPropertyDefinition) -> bool """
        pass

    def GetReadOnly(self):
        """ GetReadOnly(self: MgRasterPropertyDefinition) -> bool """
        pass

    def GetSpatialContextAssociation(self):
        """ GetSpatialContextAssociation(self: MgRasterPropertyDefinition) -> str """
        pass

    def SetDefaultImageXSize(self, size):
        """ SetDefaultImageXSize(self: MgRasterPropertyDefinition, size: int) """
        pass

    def SetDefaultImageYSize(self, size):
        """ SetDefaultImageYSize(self: MgRasterPropertyDefinition, size: int) """
        pass

    def SetNullable(self, value):
        """ SetNullable(self: MgRasterPropertyDefinition, value: bool) """
        pass

    def SetReadOnly(self, value):
        """ SetReadOnly(self: MgRasterPropertyDefinition, value: bool) """
        pass

    def SetSpatialContextAssociation(self, spatialContextName):
        """ SetSpatialContextAssociation(self: MgRasterPropertyDefinition, spatialContextName: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str)
        """
        pass

    DefaultImageXSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultImageXSize(self: MgRasterPropertyDefinition) -> int

Set: DefaultImageXSize(self: MgRasterPropertyDefinition) = value
"""

    DefaultImageYSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DefaultImageYSize(self: MgRasterPropertyDefinition) -> int

Set: DefaultImageYSize(self: MgRasterPropertyDefinition) = value
"""

    Nullable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Nullable(self: MgRasterPropertyDefinition) -> bool

Set: Nullable(self: MgRasterPropertyDefinition) = value
"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReadOnly(self: MgRasterPropertyDefinition) -> bool

Set: ReadOnly(self: MgRasterPropertyDefinition) = value
"""

    SpatialContextAssociation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SpatialContextAssociation(self: MgRasterPropertyDefinition) -> str

Set: SpatialContextAssociation(self: MgRasterPropertyDefinition) = value
"""


    swigCMemOwn = None


class MgReaderType(object):
    """ MgReaderType() """
    DataReader = 1
    FeatureReader = 0
    SqlDataReader = 2


class MgReadOnlyLayerCollection(MgGuardDisposable):
    """ MgReadOnlyLayerCollection(cPtr: IntPtr, cMemoryOwn: bool) """
    def Add(self, value):
        """ Add(self: MgReadOnlyLayerCollection, value: MgLayerBase) """
        pass

    def Clear(self):
        """ Clear(self: MgReadOnlyLayerCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgReadOnlyLayerCollection, value: MgLayerBase) -> bool """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgReadOnlyLayerCollection, array: Array[MgLayerBase], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgReadOnlyLayerCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgReadOnlyLayerCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgReadOnlyLayerCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgReadOnlyLayerCollection) -> IEnumerator[MgLayerBase] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgReadOnlyLayerCollection, index: int) -> MgLayerBase """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgReadOnlyLayerCollection, value: MgLayerBase) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgReadOnlyLayerCollection, index: int, value: MgLayerBase) """
        pass

    def Remove(self, value):
        """ Remove(self: MgReadOnlyLayerCollection, value: MgLayerBase) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgReadOnlyLayerCollection, index: int) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgLayerBase], item: MgLayerBase) -> bool """
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
    """Get: Count(self: MgReadOnlyLayerCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgReadOnlyLayerCollection) -> bool

"""


    MgReadOnlyLayerCollectionEnumerator = None
    swigCMemOwn = None


class MgRepositoryType(object):
    """ MgRepositoryType() """
    Library = 'Library'
    Session = 'Session'


class MgResourceBusyException(MgApplicationException):
    """
    MgResourceBusyException(cPtr: IntPtr, cMemoryOwn: bool)
    MgResourceBusyException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgResourceBusyException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourceBusyException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgResourceDataName(object):
    """ MgResourceDataName() """
    ProxyCredentials = 'MG_PROXY_CREDENTIALS'
    ProxyServerName = 'MG_PROXY_SERVER'
    ProxyServerPort = 'MG_PROXY_PORT'
    UserCredentials = 'MG_USER_CREDENTIALS'


class MgResourceDataNotFoundException(MgApplicationException):
    """
    MgResourceDataNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgResourceDataNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgResourceDataNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourceDataNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgResourceDataType(object):
    """ MgResourceDataType() """
    File = 'File'
    Stream = 'Stream'
    String = 'String'


class MgResourceHeaderProperties(object):
    """ MgResourceHeaderProperties() """
    General = 1
    Metadata = 4
    Security = 2


class MgResourceIdentifier(MgSerializable):
    """
    MgResourceIdentifier(cPtr: IntPtr, cMemoryOwn: bool)
    MgResourceIdentifier(resource: str)
    """
    def Dispose(self):
        """ Dispose(self: MgResourceIdentifier) """
        pass

    def Equals(self, obj):
        """ Equals(self: MgResourceIdentifier, obj: object) -> bool """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourceIdentifier) -> IntPtr """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MgResourceIdentifier) -> int """
        pass

    def GetName(self):
        """ GetName(self: MgResourceIdentifier) -> str """
        pass

    def GetPath(self):
        """ GetPath(self: MgResourceIdentifier) -> str """
        pass

    def GetRepositoryName(self):
        """ GetRepositoryName(self: MgResourceIdentifier) -> str """
        pass

    def GetRepositoryType(self):
        """ GetRepositoryType(self: MgResourceIdentifier) -> str """
        pass

    def GetResourceType(self):
        """ GetResourceType(self: MgResourceIdentifier) -> str """
        pass

    def SetName(self, name):
        """ SetName(self: MgResourceIdentifier, name: str) """
        pass

    def SetPath(self, path):
        """ SetPath(self: MgResourceIdentifier, path: str) """
        pass

    def SetRepositoryName(self, name):
        """ SetRepositoryName(self: MgResourceIdentifier, name: str) """
        pass

    def SetRepositoryType(self, type):
        """ SetRepositoryType(self: MgResourceIdentifier, type: str) """
        pass

    def SetResourceType(self, type):
        """ SetResourceType(self: MgResourceIdentifier, type: str) """
        pass

    def ToString(self):
        """ ToString(self: MgResourceIdentifier) -> str """
        pass

    def Validate(self):
        """ Validate(self: MgResourceIdentifier) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, resource: str)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgResourceIdentifier) -> str

Set: Name(self: MgResourceIdentifier) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: MgResourceIdentifier) -> str

Set: Path(self: MgResourceIdentifier) = value
"""

    RepositoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RepositoryName(self: MgResourceIdentifier) -> str

Set: RepositoryName(self: MgResourceIdentifier) = value
"""

    RepositoryType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RepositoryType(self: MgResourceIdentifier) -> str

Set: RepositoryType(self: MgResourceIdentifier) = value
"""

    ResourceType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResourceType(self: MgResourceIdentifier) -> str

Set: ResourceType(self: MgResourceIdentifier) = value
"""


    swigCMemOwn = None


class MgResourceNotFoundException(MgApplicationException):
    """
    MgResourceNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgResourceNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgResourceNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourceNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgResourcePermission(object):
    """ MgResourcePermission() """
    NoAccess = 'n'
    ReadOnly = 'r'
    ReadWrite = 'r,w'


class MgResourceService(MgService):
    """ MgResourceService(cPtr: IntPtr, cMemoryOwn: bool) """
    def ApplyResourcePackage(self, resourcePackage):
        """ ApplyResourcePackage(self: MgResourceService, resourcePackage: MgByteReader) """
        pass

    def ChangeResourceOwner(self, resource, owner, includeDescendants):
        """ ChangeResourceOwner(self: MgResourceService, resource: MgResourceIdentifier, owner: str, includeDescendants: bool) """
        pass

    def CopyResource(self, sourceResource, destResource, overwrite):
        """ CopyResource(self: MgResourceService, sourceResource: MgResourceIdentifier, destResource: MgResourceIdentifier, overwrite: bool) """
        pass

    def DeleteResource(self, resource):
        """ DeleteResource(self: MgResourceService, resource: MgResourceIdentifier) """
        pass

    def DeleteResourceData(self, resource, dataName):
        """ DeleteResourceData(self: MgResourceService, resource: MgResourceIdentifier, dataName: str) """
        pass

    def Dispose(self):
        """ Dispose(self: MgResourceService) """
        pass

    def EnumerateReferences(self, resource):
        """ EnumerateReferences(self: MgResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def EnumerateResourceData(self, resource):
        """ EnumerateResourceData(self: MgResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def EnumerateResourceDocuments(self, resources, type, properties):
        """ EnumerateResourceDocuments(self: MgResourceService, resources: MgStringCollection, type: str, properties: int) -> str """
        pass

    def EnumerateResources(self, resource, depth, type, computeChildren=None):
        """
        EnumerateResources(self: MgResourceService, resource: MgResourceIdentifier, depth: int, type: str, computeChildren: bool) -> MgByteReader
        EnumerateResources(self: MgResourceService, resource: MgResourceIdentifier, depth: int, type: str) -> MgByteReader
        """
        pass

    def EnumerateUnmanagedData(self, path, recursive, type, filter):
        """ EnumerateUnmanagedData(self: MgResourceService, path: str, recursive: bool, type: str, filter: str) -> MgByteReader """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourceService) -> IntPtr """
        pass

    def GetRepositoryContent(self, resource):
        """ GetRepositoryContent(self: MgResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetRepositoryHeader(self, resource):
        """ GetRepositoryHeader(self: MgResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetResourceContent(self, resource):
        """ GetResourceContent(self: MgResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetResourceContents(self, resources, preProcessTags):
        """ GetResourceContents(self: MgResourceService, resources: MgStringCollection, preProcessTags: MgStringCollection) -> MgStringCollection """
        pass

    def GetResourceData(self, resource, dataName):
        """ GetResourceData(self: MgResourceService, resource: MgResourceIdentifier, dataName: str) -> MgByteReader """
        pass

    def GetResourceHeader(self, resource):
        """ GetResourceHeader(self: MgResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetResourceMetadata(self, resource):
        """ GetResourceMetadata(self: MgResourceService, resource: MgResourceIdentifier) -> MgByteReader """
        pass

    def GetResourceModifiedDate(self, resource):
        """ GetResourceModifiedDate(self: MgResourceService, resource: MgResourceIdentifier) -> MgDateTime """
        pass

    def InheritPermissionsFrom(self, resource):
        """ InheritPermissionsFrom(self: MgResourceService, resource: MgResourceIdentifier) """
        pass

    def MoveResource(self, sourceResource, destResource, overwrite, cascade=None):
        """ MoveResource(self: MgResourceService, sourceResource: MgResourceIdentifier, destResource: MgResourceIdentifier, overwrite: bool, cascade: bool)MoveResource(self: MgResourceService, sourceResource: MgResourceIdentifier, destResource: MgResourceIdentifier, overwrite: bool) """
        pass

    def RenameResourceData(self, resource, oldDataName, newDataName, overwrite):
        """ RenameResourceData(self: MgResourceService, resource: MgResourceIdentifier, oldDataName: str, newDataName: str, overwrite: bool) """
        pass

    def ResourceExists(self, resource):
        """ ResourceExists(self: MgResourceService, resource: MgResourceIdentifier) -> bool """
        pass

    def SetResource(self, resource, content, header):
        """ SetResource(self: MgResourceService, resource: MgResourceIdentifier, content: MgByteReader, header: MgByteReader) """
        pass

    def SetResourceData(self, resource, dataName, dataType, data):
        """ SetResourceData(self: MgResourceService, resource: MgResourceIdentifier, dataName: str, dataType: str, data: MgByteReader) """
        pass

    def SetResourceMetadata(self, resource, content):
        """ SetResourceMetadata(self: MgResourceService, resource: MgResourceIdentifier, content: MgByteReader) """
        pass

    def UpdateRepository(self, resource, content, header):
        """ UpdateRepository(self: MgResourceService, resource: MgResourceIdentifier, content: MgByteReader, header: MgByteReader) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgResourcesException(MgApplicationException):
    """
    MgResourcesException(cPtr: IntPtr, cMemoryOwn: bool)
    MgResourcesException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgResourcesException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourcesException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgResourcesLoadFailedException(MgApplicationException):
    """
    MgResourcesLoadFailedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgResourcesLoadFailedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgResourcesLoadFailedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourcesLoadFailedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgResourceTag(object):
    """ MgResourceTag() """
    DataFilePath = '%MG_DATA_FILE_PATH%'
    DataPathAliasBegin = '%MG_DATA_PATH_ALIAS['
    DataPathAliasEnd = ']%'
    LoginPassword = '%MG_LOGIN_PASSWORD%'
    LoginUsername = '%MG_LOGIN_USERNAME%'
    Password = '%MG_PASSWORD%'
    ProxyPassword = '%MG_PROXY_PASSWORD%'
    ProxyPort = '%MG_PROXY_PORT%'
    ProxyServer = '%MG_PROXY_SERVER%'
    ProxyUsername = '%MG_PROXY_USERNAME%'
    TileCachePath = '%MG_TILE_CACHE_PATH%'
    Username = '%MG_USERNAME%'


class MgResourceTagNotFoundException(MgApplicationException):
    """
    MgResourceTagNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgResourceTagNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgResourceTagNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgResourceTagNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgResourceType(object):
    """ MgResourceType() """
    ApplicationDefinition = 'ApplicationDefinition'
    DrawingSource = 'DrawingSource'
    FeatureSource = 'FeatureSource'
    Folder = 'Folder'
    LayerDefinition = 'LayerDefinition'
    LoadProcedure = 'LoadProcedure'
    Map = 'Map'
    MapDefinition = 'MapDefinition'
    PrintLayout = 'PrintLayout'
    Selection = 'Selection'
    SymbolDefinition = 'SymbolDefinition'
    SymbolLibrary = 'SymbolLibrary'
    TileSetDefinition = 'TileSetDefinition'
    WatermarkDefinition = 'WatermarkDefinition'
    WebLayout = 'WebLayout'


class MgRole(object):
    """ MgRole() """
    Administrator = 'Administrator'
    Author = 'Author'
    Viewer = 'Viewer'


class MgRuntimeException(MgSystemException):
    """
    MgRuntimeException(cPtr: IntPtr, cMemoryOwn: bool)
    MgRuntimeException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgRuntimeException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgRuntimeException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgScaleBarBase(MgPrintLayoutElementBase):
    """ MgScaleBarBase(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgScaleBarBase) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgScaleBarBase) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgSelectionBase(MgResource):
    """
    MgSelectionBase(cPtr: IntPtr, cMemoryOwn: bool)
    MgSelectionBase(map: MgMapBase)
    MgSelectionBase(map: MgMapBase, xmlSelectionString: str)
    """
    def Add(self, layer, className, id):
        """ Add(self: MgSelectionBase, layer: str, className: str, id: str) """
        pass

    def AddFeatureIdDouble(self, layer, className, identifier):
        """ AddFeatureIdDouble(self: MgSelectionBase, layer: MgLayerBase, className: str, identifier: float) """
        pass

    def AddFeatureIdInt16(self, layer, className, identifier):
        """ AddFeatureIdInt16(self: MgSelectionBase, layer: MgLayerBase, className: str, identifier: Int16) """
        pass

    def AddFeatureIdInt32(self, layer, className, identifier):
        """ AddFeatureIdInt32(self: MgSelectionBase, layer: MgLayerBase, className: str, identifier: int) """
        pass

    def AddFeatureIdInt64(self, layer, className, identifier):
        """ AddFeatureIdInt64(self: MgSelectionBase, layer: MgLayerBase, className: str, identifier: Int64) """
        pass

    def AddFeatureIds(self, layer, className, identityProperties):
        """ AddFeatureIds(self: MgSelectionBase, layer: MgLayerBase, className: str, identityProperties: MgPropertyCollection) """
        pass

    def AddFeatureIdString(self, layer, className, identifier):
        """ AddFeatureIdString(self: MgSelectionBase, layer: MgLayerBase, className: str, identifier: str) """
        pass

    def AddFeatures(self, layer, features, nFeatures):
        """ AddFeatures(self: MgSelectionBase, layer: MgLayerBase, features: MgFeatureReader, nFeatures: int) """
        pass

    def Contains(self, layer, className):
        """ Contains(self: MgSelectionBase, layer: MgLayerBase, className: str) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgSelectionBase) """
        pass

    def FromXml(self, xmlSelectionString):
        """ FromXml(self: MgSelectionBase, xmlSelectionString: str) """
        pass

    def GenerateFilter(self, layer, className):
        """ GenerateFilter(self: MgSelectionBase, layer: MgLayerBase, className: str) -> str """
        pass

    def GenerateFilters(self, layer, className, selectionSize):
        """ GenerateFilters(self: MgSelectionBase, layer: MgLayerBase, className: str, selectionSize: int) -> MgStringCollection """
        pass

    def GetClass(self, layer):
        """ GetClass(self: MgSelectionBase, layer: str) -> str """
        pass

    def GetClasses(self, layer):
        """ GetClasses(self: MgSelectionBase, layer: str) -> MgStringCollection """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgSelectionBase) -> IntPtr """
        pass

    def GetExtents(self, featureService):
        """ GetExtents(self: MgSelectionBase, featureService: MgFeatureService) -> MgEnvelope """
        pass

    def GetLayers(self):
        """ GetLayers(self: MgSelectionBase) -> MgReadOnlyLayerCollection """
        pass

    def GetResourceName(self, sessionId, mapName):
        """ GetResourceName(self: MgSelectionBase, sessionId: str, mapName: str) -> str """
        pass

    def GetSelectedFeatures(self, layer, className, *__args):
        """
        GetSelectedFeatures(self: MgSelectionBase, layer: MgLayerBase, className: str, propertyNames: MgStringCollection) -> MgFeatureReader
        GetSelectedFeatures(self: MgSelectionBase, layer: MgLayerBase, className: str, mappedOnly: bool) -> MgFeatureReader
        """
        pass

    def GetSelectedFeaturesCount(self, layer, className):
        """ GetSelectedFeaturesCount(self: MgSelectionBase, layer: MgLayerBase, className: str) -> int """
        pass

    def Open(self, resourceService, *__args):
        """ Open(self: MgSelectionBase, resourceService: MgResourceService, mapName: str) """
        pass

    def Save(self, resourceService, *__args):
        """ Save(self: MgSelectionBase, resourceService: MgResourceService, mapName: str) """
        pass

    def SetMap(self, map):
        """ SetMap(self: MgSelectionBase, map: MgMapBase) """
        pass

    def ToXml(self):
        """ ToXml(self: MgSelectionBase) -> str """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, map: MgMapBase)
        __new__(cls: type, map: MgMapBase, xmlSelectionString: str)
        """
        pass

    swigCMemOwn = None


class MgServiceNotAvailableException(MgApplicationException):
    """
    MgServiceNotAvailableException(cPtr: IntPtr, cMemoryOwn: bool)
    MgServiceNotAvailableException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgServiceNotAvailableException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgServiceNotAvailableException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgServiceNotSupportedException(MgApplicationException):
    """
    MgServiceNotSupportedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgServiceNotSupportedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgServiceNotSupportedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgServiceNotSupportedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgServiceType(object):
    """ MgServiceType() """
    DrawingService = None
    FeatureService = None
    KmlService = None
    MappingService = None
    ProfilingService = None
    RenderingService = None
    ResourceService = None
    TileService = None


class MgSingleProperty(MgNullableProperty):
    """
    MgSingleProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgSingleProperty(name: str, value: Single)
    """
    def Dispose(self):
        """ Dispose(self: MgSingleProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgSingleProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgSingleProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgSingleProperty) -> Single """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgSingleProperty, value: Single) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: Single)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgSingleProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgSingleProperty) -> Single

Set: Value(self: MgSingleProperty) = value
"""


    swigCMemOwn = None


class MgSpatialContextExtentType(object):
    """ MgSpatialContextExtentType() """
    scDynamic = 1
    scStatic = 0


class MgSpatialContextReader(MgSerializable):
    """ MgSpatialContextReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Close(self):
        """ Close(self: MgSpatialContextReader) """
        pass

    def Dispose(self):
        """ Dispose(self: MgSpatialContextReader) """
        pass

    def GetCoordinateSystem(self):
        """ GetCoordinateSystem(self: MgSpatialContextReader) -> str """
        pass

    def GetCoordinateSystemWkt(self):
        """ GetCoordinateSystemWkt(self: MgSpatialContextReader) -> str """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgSpatialContextReader) -> IntPtr """
        pass

    def GetDescription(self):
        """ GetDescription(self: MgSpatialContextReader) -> str """
        pass

    def GetExtent(self):
        """ GetExtent(self: MgSpatialContextReader) -> MgByteReader """
        pass

    def GetExtentType(self):
        """ GetExtentType(self: MgSpatialContextReader) -> int """
        pass

    def GetName(self):
        """ GetName(self: MgSpatialContextReader) -> str """
        pass

    def GetXYTolerance(self):
        """ GetXYTolerance(self: MgSpatialContextReader) -> float """
        pass

    def GetZTolerance(self):
        """ GetZTolerance(self: MgSpatialContextReader) -> float """
        pass

    def IsActive(self):
        """ IsActive(self: MgSpatialContextReader) -> bool """
        pass

    def ReadNext(self):
        """ ReadNext(self: MgSpatialContextReader) -> bool """
        pass

    def Reset(self):
        """ Reset(self: MgSpatialContextReader) """
        pass

    def ToXml(self):
        """ ToXml(self: MgSpatialContextReader) -> MgByteReader """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    CoordinateSystem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystem(self: MgSpatialContextReader) -> str

"""

    CoordinateSystemWkt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CoordinateSystemWkt(self: MgSpatialContextReader) -> str

"""

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: MgSpatialContextReader) -> str

"""

    Extent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Extent(self: MgSpatialContextReader) -> MgByteReader

"""

    ExtentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExtentType(self: MgSpatialContextReader) -> int

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: MgSpatialContextReader) -> str

"""

    XYTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: XYTolerance(self: MgSpatialContextReader) -> float

"""

    ZTolerance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ZTolerance(self: MgSpatialContextReader) -> float

"""


    swigCMemOwn = None


class MgSqlDataReader(MgReader):
    """ MgSqlDataReader(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgSqlDataReader) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgSqlDataReader) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgStringCollection(MgCollection):
    """
    MgStringCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgStringCollection()
    MgStringCollection(collection: StringCollection)
    """
    def Add(self, value):
        """ Add(self: MgStringCollection, value: str) """
        pass

    def Clear(self):
        """ Clear(self: MgStringCollection) """
        pass

    def Contains(self, value):
        """ Contains(self: MgStringCollection, value: str) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: MgStringCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgStringCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgStringCollection) -> IntPtr """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgStringCollection, index: int) -> str """
        pass

    def IndexOf(self, value):
        """ IndexOf(self: MgStringCollection, value: str) -> int """
        pass

    def Insert(self, index, value):
        """ Insert(self: MgStringCollection, index: int, value: str) """
        pass

    def Remove(self, value):
        """ Remove(self: MgStringCollection, value: str) -> bool """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgStringCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgStringCollection, index: int, value: str) """
        pass

    def ToXml(self):
        """ ToXml(self: MgStringCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, collection: StringCollection)
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    swigCMemOwn = None


class MgStringProperty(MgNullableProperty):
    """
    MgStringProperty(cPtr: IntPtr, cMemoryOwn: bool)
    MgStringProperty(name: str, value: str)
    """
    def Dispose(self):
        """ Dispose(self: MgStringProperty) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgStringProperty) -> IntPtr """
        pass

    def GetPropertyType(self):
        """ GetPropertyType(self: MgStringProperty) -> Int16 """
        pass

    def GetValue(self):
        """ GetValue(self: MgStringProperty) -> str """
        pass

    def SetValue(self, value):
        """ SetValue(self: MgStringProperty, value: str) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, name: str, value: str)
        """
        pass

    PropertyType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyType(self: MgStringProperty) -> Int16

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: MgStringProperty) -> str

"""


    swigCMemOwn = None


class MgStringPropertyCollection(MgCollection):
    """
    MgStringPropertyCollection(cPtr: IntPtr, cMemoryOwn: bool)
    MgStringPropertyCollection()
    """
    def Add(self, *__args):
        """ Add(self: MgStringPropertyCollection, value: MgStringProperty)Add(self: MgStringPropertyCollection, keyname: str, value: str) """
        pass

    def Clear(self):
        """ Clear(self: MgStringPropertyCollection) """
        pass

    def Contains(self, *__args):
        """
        Contains(self: MgStringPropertyCollection, value: MgStringProperty) -> bool
        Contains(self: MgStringPropertyCollection, keyname: str) -> bool
        """
        pass

    def CopyTo(self, array, arrayIndex):
        """ CopyTo(self: MgStringPropertyCollection, array: Array[MgStringProperty], arrayIndex: int) """
        pass

    def Dispose(self):
        """ Dispose(self: MgStringPropertyCollection) """
        pass

    def GetCount(self):
        """ GetCount(self: MgStringPropertyCollection) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgStringPropertyCollection) -> IntPtr """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: MgStringPropertyCollection) -> IEnumerator[MgStringProperty] """
        pass

    def GetItem(self, index):
        """ GetItem(self: MgStringPropertyCollection, index: int) -> MgStringProperty """
        pass

    def GetName(self, index):
        """ GetName(self: MgStringPropertyCollection, index: int) -> str """
        pass

    def GetValue(self, *__args):
        """
        GetValue(self: MgStringPropertyCollection, keyname: str) -> str
        GetValue(self: MgStringPropertyCollection, index: int) -> str
        """
        pass

    def IndexOf(self, *__args):
        """
        IndexOf(self: MgStringPropertyCollection, value: MgStringProperty) -> int
        IndexOf(self: MgStringPropertyCollection, keyname: str) -> int
        """
        pass

    def Insert(self, index, *__args):
        """ Insert(self: MgStringPropertyCollection, index: int, value: MgStringProperty)Insert(self: MgStringPropertyCollection, index: int, keyname: str, value: str) """
        pass

    def Remove(self, *__args):
        """
        Remove(self: MgStringPropertyCollection, value: MgStringProperty) -> bool
        Remove(self: MgStringPropertyCollection, keyname: str) -> bool
        """
        pass

    def RemoveAt(self, index):
        """ RemoveAt(self: MgStringPropertyCollection, index: int) """
        pass

    def SetItem(self, index, value):
        """ SetItem(self: MgStringPropertyCollection, index: int, value: MgStringProperty) """
        pass

    def SetValue(self, keyname, value):
        """ SetValue(self: MgStringPropertyCollection, keyname: str, value: str) """
        pass

    def ToXml(self):
        """ ToXml(self: MgStringPropertyCollection) -> MgByteReader """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__(self: ICollection[MgStringProperty], item: MgStringProperty) -> bool """
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
    """Get: Count(self: MgStringPropertyCollection) -> int

"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsReadOnly(self: MgStringPropertyCollection) -> bool

"""


    MgStringPropertyCollectionEnumerator = None
    swigCMemOwn = None


class MgTemporaryFileNotAvailableException(MgApplicationException):
    """
    MgTemporaryFileNotAvailableException(cPtr: IntPtr, cMemoryOwn: bool)
    MgTemporaryFileNotAvailableException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgTemporaryFileNotAvailableException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgTemporaryFileNotAvailableException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgTransaction(MgSerializable):
    """ MgTransaction(cPtr: IntPtr, cMemoryOwn: bool) """
    def AddSavePoint(self, suggestName):
        """ AddSavePoint(self: MgTransaction, suggestName: str) -> str """
        pass

    def Commit(self):
        """ Commit(self: MgTransaction) """
        pass

    def Dispose(self):
        """ Dispose(self: MgTransaction) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgTransaction) -> IntPtr """
        pass

    def GetFeatureSource(self):
        """ GetFeatureSource(self: MgTransaction) -> MgResourceIdentifier """
        pass

    def ReleaseSavePoint(self, savePointName):
        """ ReleaseSavePoint(self: MgTransaction, savePointName: str) """
        pass

    def Rollback(self, savePointName=None):
        """ Rollback(self: MgTransaction, savePointName: str)Rollback(self: MgTransaction) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgUnclassifiedException(MgSystemException):
    """
    MgUnclassifiedException(cPtr: IntPtr, cMemoryOwn: bool)
    MgUnclassifiedException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgUnclassifiedException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgUnclassifiedException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgUnderflowException(MgSystemException):
    """
    MgUnderflowException(cPtr: IntPtr, cMemoryOwn: bool)
    MgUnderflowException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgUnderflowException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgUnderflowException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgUnlockFeatures(MgFeatureCommand):
    """
    MgUnlockFeatures(cPtr: IntPtr, cMemoryOwn: bool)
    MgUnlockFeatures(className: str, filterText: str)
    """
    def Dispose(self):
        """ Dispose(self: MgUnlockFeatures) """
        pass

    def GetCommandType(self):
        """ GetCommandType(self: MgUnlockFeatures) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgUnlockFeatures) -> IntPtr """
        pass

    def GetFeatureClassName(self):
        """ GetFeatureClassName(self: MgUnlockFeatures) -> str """
        pass

    def GetFilterText(self):
        """ GetFilterText(self: MgUnlockFeatures) -> str """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, className: str, filterText: str)
        """
        pass

    CommandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandType(self: MgUnlockFeatures) -> int

"""

    FeatureClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureClassName(self: MgUnlockFeatures) -> str

"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterText(self: MgUnlockFeatures) -> str

"""


    swigCMemOwn = None


class MgUpdateFeatures(MgFeatureCommand):
    """
    MgUpdateFeatures(cPtr: IntPtr, cMemoryOwn: bool)
    MgUpdateFeatures(className: str, propertyValues: MgPropertyCollection, filterText: str)
    """
    def Dispose(self):
        """ Dispose(self: MgUpdateFeatures) """
        pass

    def GetCommandType(self):
        """ GetCommandType(self: MgUpdateFeatures) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgUpdateFeatures) -> IntPtr """
        pass

    def GetFeatureClassName(self):
        """ GetFeatureClassName(self: MgUpdateFeatures) -> str """
        pass

    def GetFilterText(self):
        """ GetFilterText(self: MgUpdateFeatures) -> str """
        pass

    def GetPropertyValues(self):
        """ GetPropertyValues(self: MgUpdateFeatures) -> MgPropertyCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, className: str, propertyValues: MgPropertyCollection, filterText: str)
        """
        pass

    CommandType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CommandType(self: MgUpdateFeatures) -> int

"""

    FeatureClassName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FeatureClassName(self: MgUpdateFeatures) -> str

"""

    FilterText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilterText(self: MgUpdateFeatures) -> str

"""

    PropertyValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PropertyValues(self: MgUpdateFeatures) -> MgPropertyCollection

"""


    swigCMemOwn = None


class MgUser(object):
    """ MgUser() """
    Administrator = 'Administrator'
    Anonymous = 'Anonymous'
    Author = 'Author'
    WfsUser = 'WfsUser'
    WmsUser = 'WmsUser'


class MgUserNotFoundException(MgApplicationException):
    """
    MgUserNotFoundException(cPtr: IntPtr, cMemoryOwn: bool)
    MgUserNotFoundException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgUserNotFoundException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgUserNotFoundException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgWarnings(MgSerializable):
    """ MgWarnings(cPtr: IntPtr, cMemoryOwn: bool) """
    def Dispose(self):
        """ Dispose(self: MgWarnings) """
        pass

    def GetCount(self):
        """ GetCount(self: MgWarnings) -> int """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgWarnings) -> IntPtr """
        pass

    def GetMessages(self):
        """ GetMessages(self: MgWarnings) -> MgStringCollection """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: MgWarnings) -> int

"""


    swigCMemOwn = None


class MgWktReaderWriter(MgGuardDisposable):
    """
    MgWktReaderWriter(cPtr: IntPtr, cMemoryOwn: bool)
    MgWktReaderWriter()
    """
    def Dispose(self):
        """ Dispose(self: MgWktReaderWriter) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgWktReaderWriter) -> IntPtr """
        pass

    def Read(self, wkt, transform=None):
        """
        Read(self: MgWktReaderWriter, wkt: str, transform: MgTransform) -> MgGeometry
        Read(self: MgWktReaderWriter, wkt: str) -> MgGeometry
        """
        pass

    def Write(self, geometry, transform=None):
        """
        Write(self: MgWktReaderWriter, geometry: MgGeometry, transform: MgTransform) -> str
        Write(self: MgWktReaderWriter, geometry: MgGeometry) -> str
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr=None, cMemoryOwn=None):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class MgXmlException(MgThirdPartyException):
    """
    MgXmlException(cPtr: IntPtr, cMemoryOwn: bool)
    MgXmlException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgXmlException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgXmlException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class MgXmlParserException(MgThirdPartyException):
    """
    MgXmlParserException(cPtr: IntPtr, cMemoryOwn: bool)
    MgXmlParserException(methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
    """
    def Dispose(self):
        """ Dispose(self: MgXmlParserException) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: MgXmlParserException) -> IntPtr """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        __new__(cls: type, methodName: str, lineNumber: int, fileName: str, whatArguments: MgStringCollection, whyMessageId: str, whyArguments: MgStringCollection)
        """
        pass

    swigCMemOwn = None


class PlatformBaseApi(object):
    """ PlatformBaseApi() """

