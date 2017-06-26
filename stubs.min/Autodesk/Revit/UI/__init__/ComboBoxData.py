class ComboBoxData(RibbonItemData):
    """
    This class contains information necessary to construct a combo box in the Ribbon.
    
    ComboBoxData(name: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, name):
        """ __new__(cls: type, name: str) """
        pass

    Image = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The image shown on the ComboBox.

Get: Image(self: ComboBoxData) -> ImageSource

Set: Image(self: ComboBoxData) = value
"""


