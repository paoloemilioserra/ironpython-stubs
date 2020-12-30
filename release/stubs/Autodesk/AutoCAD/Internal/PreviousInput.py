# encoding: utf-8
# module Autodesk.AutoCAD.Internal.PreviousInput calls itself PreviousInput
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcPiMonitorReactorImpl(object):
    # no doc
    ReactorFlags = None


class CommandLineMonitor(object):
    # no doc
    def EnableSsGetFilter(self, on):
        """ EnableSsGetFilter(self: CommandLineMonitor, on: bool) """
        pass

    CurrentCommandName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentCommandName(self: CommandLineMonitor) -> str

"""

    CurrentDoubleOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDoubleOut(self: CommandLineMonitor) -> float

"""

    CurrentInitgetFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentInitgetFlags(self: CommandLineMonitor) -> int

"""

    CurrentInitgetKeywords = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentInitgetKeywords(self: CommandLineMonitor) -> str

"""

    CurrentInputControlFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentInputControlFlags(self: CommandLineMonitor) -> InputControlFlags

"""

    CurrentIntOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentIntOut(self: CommandLineMonitor) -> Int64

"""

    CurrentKeywordsIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentKeywordsIn(self: CommandLineMonitor) -> str

"""

    CurrentMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentMode(self: CommandLineMonitor) -> InputModes

"""

    CurrentModes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentModes(self: CommandLineMonitor) -> InputModes

"""

    CurrentNestingCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentNestingCount(self: CommandLineMonitor) -> int

"""

    CurrentPointIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPointIn(self: CommandLineMonitor) -> ValueType

"""

    CurrentPointInFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPointInFlag(self: CommandLineMonitor) -> bool

"""

    CurrentPointOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPointOut(self: CommandLineMonitor) -> ValueType

"""

    CurrentPointOut2d = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPointOut2d(self: CommandLineMonitor) -> ValueType

"""

    CurrentPointOut2dFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPointOut2dFlag(self: CommandLineMonitor) -> bool

"""

    CurrentPointOutFlag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPointOutFlag(self: CommandLineMonitor) -> bool

"""

    CurrentPrompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentPrompt(self: CommandLineMonitor) -> str

"""

    CurrentReturnStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentReturnStatus(self: CommandLineMonitor) -> PromptStatus

"""

    CurrentSSControlsIn = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSSControlsIn(self: CommandLineMonitor) -> str

"""

    CurrentSSGetConsumedPickfirst = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSSGetConsumedPickfirst(self: CommandLineMonitor) -> bool

"""

    CurrentSSGetCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSSGetCount(self: CommandLineMonitor) -> int

"""

    CurrentSSGetIsManual = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSSGetIsManual(self: CommandLineMonitor) -> bool

"""

    CurrentSSGetKeywordsUsed = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentSSGetKeywordsUsed(self: CommandLineMonitor) -> ArrayList

"""

    CurrentStringOut = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentStringOut(self: CommandLineMonitor) -> str

"""

    LastCommandName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastCommandName(self: CommandLineMonitor) -> str

"""

    LastNotifiedSSGetCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LastNotifiedSSGetCount(self: CommandLineMonitor) -> int

"""


    BeginSSGetCustomKeywordCallback = None
    CommandEnded = None
    CommandWillStart = None
    EndSSGetCustomKeywordCallback = None
    GetAngleEnded = None
    GetAngleWillStart = None
    GetDistanceEnded = None
    GetDistanceWillStart = None
    GetInput = None
    PickfirstEnded = None
    PickfirstWillStart = None
    SelectEnded = None
    SelectOperation = None
    SelectWillStart = None
    UnknownCmd = None


class CommandLineMonitorServices(object):
    # no doc
    def ActiveCommandFlags(self):
        """ ActiveCommandFlags(self: CommandLineMonitorServices) -> CommandFlags """
        pass

    def CommandActiveBits(self):
        """ CommandActiveBits(self: CommandLineMonitorServices) -> int """
        pass

    def CommandNestedDepth(self):
        """ CommandNestedDepth(self: CommandLineMonitorServices) -> int """
        pass

    def GetCommandLineMonitor(self, doc):
        """ GetCommandLineMonitor(self: CommandLineMonitorServices, doc: Document) -> CommandLineMonitor """
        pass

    def GetLocalCommandName(self, globalCmdName):
        """ GetLocalCommandName(self: CommandLineMonitorServices, globalCmdName: str) -> str """
        pass

    @staticmethod
    def Instance():
        """ Instance() -> CommandLineMonitorServices """
        pass

    def IsCurrentCommandTransparent(self):
        """ IsCurrentCommandTransparent(self: CommandLineMonitorServices) -> bool """
        pass


class GetAngleEventHandler(MulticastDelegate):
    """ GetAngleEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: GetAngleEventHandler, sender: object, e: GetInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GetAngleEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: GetAngleEventHandler, sender: object, e: GetInputEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class GetDistanceEventHandler(MulticastDelegate):
    """ GetDistanceEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: GetDistanceEventHandler, sender: object, e: GetInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GetDistanceEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: GetDistanceEventHandler, sender: object, e: GetInputEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class GetInputEventArgs(EventArgs):
    # no doc
    Mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Mode(self: GetInputEventArgs) -> InputModes

"""

    ReturnStatus = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ReturnStatus(self: GetInputEventArgs) -> PromptStatus

"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: GetInputEventArgs) -> object

"""



class GetInputEventHandler(MulticastDelegate):
    """ GetInputEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: GetInputEventHandler, sender: object, e: GetInputEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: GetInputEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: GetInputEventHandler, sender: object, e: GetInputEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class InputControlFlags(Enum):
    """ enum (flags) InputControlFlags, values: ud2DDIST (4194304), udANYBLANK (33554432), udBASE (1), udBKSL (1073741824), udCURSOR (64), udDISPLPT (524288), udDRAG (16), udENTITY (8192), udFIRSTBLANK (67108864), udFLATCUR (262144), udGETZ (16384), udIGNOREETX (134217728), udKWORD (8), udLABELOK (536870912), udMSG (128), udMSGNUM (1048576), udNOLAST (256), udNOLIM (512), udNONE (0), udNONEG (4096), udNOOSNAP (131072), udNOPFILT (65536), udNORANGEMSG (32768), udNOSMODE (2097152), udNOZERO (2048), udNULLOK (4), udORTHO (2), udOTHER (1024), udPOINTOK (268435456), udPOINTUP (16777216), udRESCAN (8388608), udSILENTETX (32), udWNOSORT (2), udXCTL (-2147483648) """
    ud2DDIST = None
    udANYBLANK = None
    udBASE = None
    udBKSL = None
    udCURSOR = None
    udDISPLPT = None
    udDRAG = None
    udENTITY = None
    udFIRSTBLANK = None
    udFLATCUR = None
    udGETZ = None
    udIGNOREETX = None
    udKWORD = None
    udLABELOK = None
    udMSG = None
    udMSGNUM = None
    udNOLAST = None
    udNOLIM = None
    udNONE = None
    udNONEG = None
    udNOOSNAP = None
    udNOPFILT = None
    udNORANGEMSG = None
    udNOSMODE = None
    udNOZERO = None
    udNULLOK = None
    udORTHO = None
    udOTHER = None
    udPOINTOK = None
    udPOINTUP = None
    udRESCAN = None
    udSILENTETX = None
    udWNOSORT = None
    udXCTL = None
    value__ = None


class InputModes(Enum):
    """ enum (flags) InputModes, values: AllGetInput (16284671), Angle (2), Cmd (65536), Color (512), Corner (16), Distance (4), Drag (32768), DynDimGetPoint (1048576), EntSel (4096), Integer (256), kword (128), Nentsel (8192), None (0), Orientation (8), Point (1), RawAngle (8388608), Real (2048), ScaleFactor (32), ScaleFactor2 (524288), SSGet (16384), String (64), UnknownCmd (131072), Vector (262144) """
    AllGetInput = None
    Angle = None
    Cmd = None
    Color = None
    Corner = None
    Distance = None
    Drag = None
    DynDimGetPoint = None
    EntSel = None
    Integer = None
    kword = None
    Nentsel = None
    None = None
    Orientation = None
    Point = None
    RawAngle = None
    Real = None
    ScaleFactor = None
    ScaleFactor2 = None
    SSGet = None
    String = None
    UnknownCmd = None
    value__ = None
    Vector = None


class InputStringEventArgs(EventArgs):
    # no doc
    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Value(self: InputStringEventArgs) -> str

"""



class InputStringEventHandler(MulticastDelegate):
    """ InputStringEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: InputStringEventHandler, sender: object, e: InputStringEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: InputStringEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: InputStringEventHandler, sender: object, e: InputStringEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SelectEventHandler(MulticastDelegate):
    """ SelectEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: SelectEventHandler, sender: object, e: EventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SelectEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SelectEventHandler, sender: object, e: EventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


class SelectOperationEventArgs(EventArgs):
    # no doc
    GroupName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GroupName(self: SelectOperationEventArgs) -> str

"""

    IsAdding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAdding(self: SelectOperationEventArgs) -> bool

"""

    IsCancel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCancel(self: SelectOperationEventArgs) -> bool

"""

    IsCrossingBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCrossingBox(self: SelectOperationEventArgs) -> bool

"""

    IsSubSelection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSubSelection(self: SelectOperationEventArgs) -> bool

"""

    Points = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Points(self: SelectOperationEventArgs) -> Point3dCollection

"""

    SelectionFlags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionFlags(self: SelectOperationEventArgs) -> int

"""

    SelectionMode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SelectionMode(self: SelectOperationEventArgs) -> SelectionMode

"""



class SelectOperationEventHandler(MulticastDelegate):
    """ SelectOperationEventHandler(A_0: object, A_1: IntPtr) """
    def BeginInvoke(self, sender, e, callback, obj):
        """ BeginInvoke(self: SelectOperationEventHandler, sender: object, e: SelectOperationEventArgs, callback: AsyncCallback, obj: object) -> IAsyncResult """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: SelectOperationEventHandler, result: IAsyncResult) """
        pass

    def Invoke(self, sender, e):
        """ Invoke(self: SelectOperationEventHandler, sender: object, e: SelectOperationEventArgs) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, A_0, A_1):
        """ __new__(cls: type, A_0: object, A_1: IntPtr) """
        pass


