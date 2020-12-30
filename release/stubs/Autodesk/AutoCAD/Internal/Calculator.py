# encoding: utf-8
# module Autodesk.AutoCAD.Internal.Calculator calls itself Calculator
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AngleUnitsEnum(Enum):
    """ enum AngleUnitsEnum, values: Degree (0), DegreeMinSec (1), Grad (2), None (-1), Radian (3), Surveyor (4) """
    Degree = None
    DegreeMinSec = None
    Grad = None
    None = None
    Radian = None
    Surveyor = None
    value__ = None


class CalcContext(DisposableWrapper):
    """ CalcContext() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    AngleUnits = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AngleUnits(self: CalcContext) -> AngleUnitsEnum

Set: AngleUnits(self: CalcContext) = value
"""

    HostServices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HostServices(self: CalcContext) -> CalcHostServices

"""



class CalcEngine(DisposableWrapper):
    # no doc
    def AddGlobalVariable(self, variableName, variableValue):
        """ AddGlobalVariable(self: CalcEngine, variableName: str, variableValue: CalcValueType) -> bool """
        pass

    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def EvaluateExpression(self, expression, context, result):
        """ EvaluateExpression(self: CalcEngine, expression: str, context: CalcContext, result: CalcResult) -> bool """
        pass

    def EvaluateExpressionDisableSnap(self, expression, context, result):
        """ EvaluateExpressionDisableSnap(self: CalcEngine, expression: str, context: CalcContext, result: CalcResult) -> bool """
        pass

    @staticmethod
    def GetEngine():
        """ GetEngine() -> CalcEngine """
        pass

    def RemoveGlobalVariable(self, variableName):
        """ RemoveGlobalVariable(self: CalcEngine, variableName: str) -> bool """
        pass

    GlobalVariableCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalVariableCollection(self: CalcEngine) -> CalcGlobalVariableBag

"""

    GlobalVariableServices = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalVariableServices(self: CalcEngine) -> CalcGlobalVariableServices

Set: GlobalVariableServices(self: CalcEngine) = value
"""



class CalcGlobalVariableBag(DisposableWrapper):
    """ CalcGlobalVariableBag(pvars: AcCalGlobalVarCollection*) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetEnumerator(self):
        """ GetEnumerator(self: CalcGlobalVariableBag) -> IEnumerator """
        pass

    def MoveNext(self):
        """ MoveNext(self: CalcGlobalVariableBag) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: CalcGlobalVariableBag) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, pvars):
        """ __new__(cls: type, pvars: AcCalGlobalVarCollection*) """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: CalcGlobalVariableBag) -> object

"""



class CalcGlobalVariableServices(DisposableWrapper):
    """ CalcGlobalVariableServices() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    GlobalVariableModifiedEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GlobalVariableModifiedEvent(self: CalcGlobalVariableServices) -> OnGlobalVariableModifiedHandler

Set: GlobalVariableModifiedEvent(self: CalcGlobalVariableServices) = value
"""



class CalcHostServices(DisposableWrapper):
    """ CalcHostServices() """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def SetQCState(self, value):
        """ SetQCState(self: CalcHostServices, value: bool) """
        pass

    FuncEpilogEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FuncEpilogEvent(self: CalcHostServices) -> OnInteractiveFunctionEpilogEventHandler

Set: FuncEpilogEvent(self: CalcHostServices) = value
"""

    FuncPrologEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FuncPrologEvent(self: CalcHostServices) -> OnInteractiveFunctionPrologEventHandler

Set: FuncPrologEvent(self: CalcHostServices) = value
"""

    WriteStringEvent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: WriteStringEvent(self: CalcHostServices) -> OnWriteStringEventHandler

Set: WriteStringEvent(self: CalcHostServices) = value
"""



class CalcResult(DisposableWrapper):
    """ CalcResult(Value: CalcValueType) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, Value):
        """ __new__(cls: type, Value: CalcValueType) """
        pass

    DWGResultString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DWGResultString(self: CalcResult) -> str

"""

    Result = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Result(self: CalcResult) -> CalcValueType

Set: Result(self: CalcResult) = value
"""

    ResultString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ResultString(self: CalcResult) -> str

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: CalcResult) -> ValueTypeEnum

Set: Type(self: CalcResult) = value
"""



class CalcValueType(object):
    # no doc
    def Equals(self, obj):
        """ Equals(self: CalcValueType, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: CalcValueType) -> int """
        pass

    @staticmethod
    def Parse(string):
        """ Parse(string: str) -> CalcValueType """
        pass

    def ToString(self, provider=None):
        """
        ToString(self: CalcValueType, provider: IFormatProvider) -> str
        ToString(self: CalcValueType) -> str
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    DistanceUnit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceUnit(self: CalcValueType) -> float

Set: DistanceUnit(self: CalcValueType) = value
"""

    DistanceUnitType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DistanceUnitType(self: CalcValueType) -> DistanceBaseUnitType

"""

    R = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: R(self: CalcValueType) -> float

Set: R(self: CalcValueType) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: CalcValueType) -> ValueTypeEnum

Set: Type(self: CalcValueType) = value
"""

    V = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: V(self: CalcValueType) -> XYZPoint

Set: V(self: CalcValueType) = value
"""



class FuncPrologEpilogEventArgs(EventArgs):
    """ FuncPrologEpilogEventArgs(FuncName: str, Result: CalcResult) """
    @staticmethod # known case of __new__
    def __new__(self, FuncName, Result):
        """ __new__(cls: type, FuncName: str, Result: CalcResult) """
        pass

    FuncName = None
    Result = None


class GlobalVariable(DisposableWrapper):
    """ GlobalVariable(umgd: AcCalGlobalVar*) """
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, umgd):
        """ __new__(cls: type, umgd: AcCalGlobalVar*) """
        pass

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GlobalVariable) -> str

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GlobalVariable) -> CalcValueType

"""



class GlobalVariableEventArgs(EventArgs):
    """ GlobalVariableEventArgs(VariableName: str, VariableValue: CalcValueType, IsNewVariable: bool) """
    @staticmethod # known case of __new__
    def __new__(self, VariableName, VariableValue, IsNewVariable):
        """ __new__(cls: type, VariableName: str, VariableValue: CalcValueType, IsNewVariable: bool) """
        pass

    IsNewVariable = None
    VariableName = None
    VariableValue = None


class IOStringEventArgs(EventArgs):
    """ IOStringEventArgs(IOString: str) """
    @staticmethod # known case of __new__
    def __new__(self, IOString):
        """ __new__(cls: type, IOString: str) """
        pass

    IOString = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IOString(self: IOStringEventArgs) -> str

Set: IOString(self: IOStringEventArgs) = value
"""



class OnGlobalVariableModifiedHandler(MulticastDelegate):
    """ OnGlobalVariableModifiedHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, e, callback, obj):
        """ BeginInvoke(self: OnGlobalVariableModifiedHandler, e: GlobalVariableEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnGlobalVariableModifiedHandler, result: IAsyncResult) """
        pass

    def Invoke(self, e):
        """ Invoke(self: OnGlobalVariableModifiedHandler, e: GlobalVariableEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OnInteractiveFunctionEpilogEventHandler(MulticastDelegate):
    """ OnInteractiveFunctionEpilogEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, e, callback, obj):
        """ BeginInvoke(self: OnInteractiveFunctionEpilogEventHandler, e: FuncPrologEpilogEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnInteractiveFunctionEpilogEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, e):
        """ Invoke(self: OnInteractiveFunctionEpilogEventHandler, e: FuncPrologEpilogEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OnInteractiveFunctionPrologEventHandler(MulticastDelegate):
    """ OnInteractiveFunctionPrologEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, e, callback, obj):
        """ BeginInvoke(self: OnInteractiveFunctionPrologEventHandler, e: FuncPrologEpilogEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnInteractiveFunctionPrologEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, e):
        """ Invoke(self: OnInteractiveFunctionPrologEventHandler, e: FuncPrologEpilogEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class OnWriteStringEventHandler(MulticastDelegate):
    """ OnWriteStringEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, e, callback, obj):
        """ BeginInvoke(self: OnWriteStringEventHandler, e: IOStringEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: OnWriteStringEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, e):
        """ Invoke(self: OnWriteStringEventHandler, e: IOStringEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class Unit(object):
    """ Unit() """
    m_Distance = None
    m_DistanceUnitType = None


class ValueTypeEnum(Enum):
    """ enum ValueTypeEnum, values: IntType (2), NoType (3), RealType (1), VectorType (0) """
    IntType = None
    NoType = None
    RealType = None
    value__ = None
    VectorType = None


class XYZPoint(object):
    """ XYZPoint(X: float, Y: float, Z: float) """
    def Equals(self, obj):
        """ Equals(self: XYZPoint, obj: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: XYZPoint) -> int """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, X, Y, Z):
        """
        __new__[XYZPoint]() -> XYZPoint
        
        __new__(cls: type, X: float, Y: float, Z: float)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: XYZPoint) -> float

Set: X(self: XYZPoint) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: XYZPoint) -> float

Set: Y(self: XYZPoint) = value
"""

    Z = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Z(self: XYZPoint) -> float

Set: Z(self: XYZPoint) = value
"""



