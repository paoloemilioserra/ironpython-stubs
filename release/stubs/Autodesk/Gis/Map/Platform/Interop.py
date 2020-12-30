# encoding: utf-8
# module Autodesk.Gis.Map.Platform.Interop calls itself Interop
# from Autodesk.Map.Platform, Version=24.0.30.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AcMapDisplayManagementService(MgService):
    """ AcMapDisplayManagementService(cPtr: IntPtr, cMemoryOwn: bool) """
    @staticmethod
    def DisableGroupsViewDrawOrder():
        """ DisableGroupsViewDrawOrder() """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapDisplayManagementService) """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapDisplayManagementService) -> IntPtr """
        pass

    @staticmethod
    def GetDMElementFromLayer(*__args):
        """
        GetDMElementFromLayer(map: MgMapBase, layerName: str) -> ObjectId
        GetDMElementFromLayer(layerName: str) -> ObjectId
        GetDMElementFromLayer(layer: MgLayerBase) -> ObjectId
        """
        pass

    @staticmethod
    def GetDMGroupFromGroup(*__args):
        """
        GetDMGroupFromGroup(map: MgMapBase, groupName: str) -> ObjectId
        GetDMGroupFromGroup(groupName: str) -> ObjectId
        GetDMGroupFromGroup(group: MgLayerGroup) -> ObjectId
        """
        pass

    @staticmethod
    def GetDMMapFromMap(map):
        """ GetDMMapFromMap(map: MgMapBase) -> ObjectId """
        pass

    @staticmethod
    def GetGroupFromDMGroup(groupId):
        """ GetGroupFromDMGroup(groupId: ObjectId) -> MgLayerGroup """
        pass

    @staticmethod
    def GetLayerFromDMElement(elementId):
        """ GetLayerFromDMElement(elementId: ObjectId) -> MgLayerBase """
        pass

    @staticmethod
    def GetMapFromDMMap(mapId):
        """ GetMapFromDMMap(mapId: ObjectId) -> MgMapBase """
        pass

    @staticmethod
    def IsEnhancedMode():
        """ IsEnhancedMode() -> bool """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


class AcMapFeatureEntityService(MgService):
    """ AcMapFeatureEntityService(cPtr: IntPtr, cMemoryOwn: bool) """
    @staticmethod
    def AddFeaturesToSelectionSet(acadSel, selectionBase):
        """ AddFeaturesToSelectionSet(acadSel: SelectionSet, selectionBase: MgSelectionBase) -> SelectionSet """
        pass

    def Dispose(self):
        """ Dispose(self: AcMapFeatureEntityService) """
        pass

    @staticmethod
    def GetBulkEntity(layer):
        """ GetBulkEntity(layer: AcMapLayer) -> ObjectId """
        pass

    @staticmethod
    def getCPtr(obj):
        """ getCPtr(obj: AcMapFeatureEntityService) -> IntPtr """
        pass

    @staticmethod
    def GetEntityType(entityId):
        """ GetEntityType(entityId: ObjectId) -> int """
        pass

    @staticmethod
    def GetFeatures(*__args):
        """
        GetFeatures(paths: Array[FullSubentityPath]) -> MgSelectionBase
        GetFeatures(subObjects: Array[SelectedSubObject]) -> MgSelectionBase
        GetFeatures(entities: ObjectIdCollection) -> MgSelectionBase
        """
        pass

    @staticmethod
    def GetFilteredSelection(acadSel, options):
        """ GetFilteredSelection(acadSel: SelectionSet, options: MgFeatureQueryOptions) -> MgSelectionBase """
        pass

    @staticmethod
    def GetLayer(entityId):
        """ GetLayer(entityId: ObjectId) -> AcMapLayer """
        pass

    @staticmethod
    def GetSelection(acadSel):
        """ GetSelection(acadSel: SelectionSet) -> MgSelectionBase """
        pass

    @staticmethod
    def HighlightFeatures(selection):
        """ HighlightFeatures(selection: MgSelectionBase) """
        pass

    @staticmethod
    def UnhighlightFeatures(selection):
        """ UnhighlightFeatures(selection: MgSelectionBase) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, cPtr, cMemoryOwn):
        """
        __new__(cls: type, cPtr: IntPtr, cMemoryOwn: bool)
        __new__(cls: type)
        """
        pass

    swigCMemOwn = None


