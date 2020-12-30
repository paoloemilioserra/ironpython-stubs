# encoding: utf-8
# module Autodesk.AutoCAD.Internal.Render.RapidRT calls itself RapidRT
# from Acmgd, Version=24.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class PairedImage(object):
    """ PairedImage() """
    def Dispose(self):
        """ Dispose(self: PairedImage) """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    ManagedBitMap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ManagedBitMap(self: PairedImage) -> Bitmap

Set: ManagedBitMap(self: PairedImage) = value
"""

    UnmanagedBitmap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UnmanagedBitmap(self: PairedImage) -> Image*

Set: UnmanagedBitmap(self: PairedImage) = value
"""



class RenderUtil(object):
    """ RenderUtil() """
    @staticmethod
    def CreateCustomPreset(presetName, presetDescription, basePresetName):
        """ CreateCustomPreset(presetName: str, presetDescription: str, basePresetName: str) -> ErrorStatus """
        pass

    @staticmethod
    def DeleteCustomPreset(presetName):
        """ DeleteCustomPreset(presetName: str) -> ErrorStatus """
        pass

    @staticmethod
    def DoModalRenderSaveFileDlg(pStrPath, filterExtName, filterExt, caption, invalidFileName):
        """ DoModalRenderSaveFileDlg(pStrPath: str, filterExtName: StringCollection, filterExt: StringCollection, caption: str, invalidFileName: str) -> (bool, str) """
        pass

    @staticmethod
    def GetSceneResString(id):
        """ GetSceneResString(id: int) -> str """
        pass

    @staticmethod
    def GetSceneResXMLBlob(id):
        """ GetSceneResXMLBlob(id: int) -> Array[Byte] """
        pass

    @staticmethod
    def GetViewportImage():
        """ GetViewportImage() -> PairedImage """
        pass

    @staticmethod
    def RenameCustomPreset(presetName, newPresetName):
        """ RenameCustomPreset(presetName: str, newPresetName: str) -> ErrorStatus """
        pass

    @staticmethod
    def SaveImage(fileName, strFormat, imagePair):
        """ SaveImage(fileName: str, strFormat: str, imagePair: PairedImage) -> bool """
        pass

    @staticmethod
    def SaveRenderJobImage(fileName, strFormat, jobIndex, pDoc):
        """ SaveRenderJobImage(fileName: str, strFormat: str, jobIndex: int, pDoc: Document) -> bool """
        pass


