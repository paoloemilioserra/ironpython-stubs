# encoding: utf-8
# module Autodesk.Civil.ApplicationServices calls itself ApplicationServices
# from AeccDbMgd, Version=13.3.854.0, Culture=neutral, PublicKeyToken=null, AeccPressurePipesMgd, Version=13.3.854.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class CivilApplication(object):
    # no doc
    ActiveDocument = None
    ActiveProduct = None
    SurveyProjects = None


class CivilDocument(DisposableWrapper):
    # no doc
    def Dispose(self):
        """ Dispose(self: DisposableWrapper, A_0: bool) """
        pass

    def GetAlignmentIds(self):
        """ GetAlignmentIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetAlignmentTableIds(self):
        """ GetAlignmentTableIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetAllPointIds(self):
        """ GetAllPointIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    @staticmethod
    def GetCivilDocument(database):
        """ GetCivilDocument(database: Database) -> CivilDocument """
        pass

    def GetGeneralSegmentLabelIds(self):
        """ GetGeneralSegmentLabelIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetIntersectionIds(self):
        """ GetIntersectionIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetLegendTableIds(self):
        """ GetLegendTableIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetNoteLabelIds(self):
        """ GetNoteLabelIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetParcelSegmentTableIds(self):
        """ GetParcelSegmentTableIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetParcelTableIds(self):
        """ GetParcelTableIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetPipeNetworkIds(self):
        """ GetPipeNetworkIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetPointTableIds(self):
        """ GetPointTableIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetSiteIds(self):
        """ GetSiteIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetSitelessAlignmentId(self, name):
        """ GetSitelessAlignmentId(self: CivilDocument, name: str) -> ObjectId """
        pass

    def GetSitelessAlignmentIds(self):
        """ GetSitelessAlignmentIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetSurfaceIds(self):
        """ GetSurfaceIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    def GetViewFrameGroupIds(self):
        """ GetViewFrameGroupIds(self: CivilDocument) -> ObjectIdCollection """
        pass

    AssemblyCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AssemblyCollection(self: CivilDocument) -> AssemblyCollection

"""

    CogoPoints = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CogoPoints(self: CivilDocument) -> CogoPointCollection

"""

    CorridorCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorCollection(self: CivilDocument) -> CorridorCollection

"""

    CorridorState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CorridorState(self: CivilDocument) -> CorridorState

"""

    IsCorridorSectionViewActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsCorridorSectionViewActive(self: CivilDocument) -> bool

"""

    IsDriveActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsDriveActive(self: CivilDocument) -> bool

"""

    IsSectionEditorCorridorReferenceObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSectionEditorCorridorReferenceObject(self: CivilDocument) -> bool

"""

    NetworkState = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NetworkState(self: CivilDocument) -> PipeNetworkState

"""

    PointGroups = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointGroups(self: CivilDocument) -> PointGroupCollection

"""

    PointUDPClassifications = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointUDPClassifications(self: CivilDocument) -> UDPClassificationCollection

"""

    PointUDPs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PointUDPs(self: CivilDocument) -> UDPCollection

"""

    Settings = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Settings(self: CivilDocument) -> SettingsRoot

"""

    Styles = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Styles(self: CivilDocument) -> StylesRoot

"""

    SubassemblyCollection = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: SubassemblyCollection(self: CivilDocument) -> SubassemblyCollection

"""



class CivilDocumentPressurePipesExtension(object):
    # no doc
    @staticmethod
    def GetPressureNetworkIdFromPipeRunPath(document, idPath):
        """ GetPressureNetworkIdFromPipeRunPath(document: CivilDocument, idPath: ObjectId) -> ObjectId """
        pass

    @staticmethod
    def GetPressurePipeNetworkIds(document):
        """ GetPressurePipeNetworkIds(document: CivilDocument) -> ObjectIdCollection """
        pass

    @staticmethod
    def IsPressurePlanLayoutActive(document):
        """ IsPressurePlanLayoutActive(document: CivilDocument) -> bool """
        pass

    @staticmethod
    def IsPressurePlanLayoutByPathActive(document):
        """ IsPressurePlanLayoutByPathActive(document: CivilDocument) -> bool """
        pass

    @staticmethod
    def IsPressureProfileLayoutActive(document):
        """ IsPressureProfileLayoutActive(document: CivilDocument) -> bool """
        pass

    @staticmethod
    def SetPressurePlanLayoutActive(document, bActive):
        """ SetPressurePlanLayoutActive(document: CivilDocument, bActive: bool) """
        pass

    @staticmethod
    def SetPressurePlanLayoutByPathActive(document, bActive):
        """ SetPressurePlanLayoutByPathActive(document: CivilDocument, bActive: bool) """
        pass

    @staticmethod
    def SetPressureProfileLayoutActive(document, bActive):
        """ SetPressureProfileLayoutActive(document: CivilDocument, bActive: bool) """
        pass

    __all__ = [
        'GetPressureNetworkIdFromPipeRunPath',
        'GetPressurePipeNetworkIds',
        'IsPressurePlanLayoutActive',
        'IsPressurePlanLayoutByPathActive',
        'IsPressureProfileLayoutActive',
        'SetPressurePlanLayoutActive',
        'SetPressurePlanLayoutByPathActive',
        'SetPressureProfileLayoutActive',
    ]


class ProductType(Enum):
    """ enum ProductType, values: Civil (3), Civil3D (1), Map (2), Other (0), Unknown (-1) """
    Civil = None
    Civil3D = None
    Map = None
    Other = None
    Unknown = None
    value__ = None


