# encoding: utf-8
# module Autodesk.Gis.Map.Platform.Utils.Globalization calls itself Globalization
# from Autodesk.Map.Platform.Utils, Version=24.0.30.14, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class EnumTypeConverter(EnumConverter):
    """ EnumTypeConverter(type: Type, resourceManager: ResourceManager) """
    def ConvertFrom(self, *__args):
        """ ConvertFrom(self: EnumTypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object) -> object """
        pass

    def ConvertTo(self, *__args):
        """ ConvertTo(self: EnumTypeConverter, context: ITypeDescriptorContext, culture: CultureInfo, value: object, destinationType: Type) -> object """
        pass

    @staticmethod
    def ConvertToString(*__args):
        """ ConvertToString(value: Enum) -> str """
        pass

    @staticmethod
    def GetValues(enumType, culture):
        """ GetValues(enumType: Type, culture: CultureInfo) -> Dictionary[Enum, str] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, type, resourceManager):
        """ __new__(cls: type, type: Type, resourceManager: ResourceManager) """
        pass

    Comparer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    EnumType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    Values = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



