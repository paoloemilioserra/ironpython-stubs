class AddingNewItemEventArgs(EventArgs):
    """ AddingNewItemEventArgs() """
    NewItem = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: NewItem(self: AddingNewItemEventArgs) -> object

Set: NewItem(self: AddingNewItemEventArgs) = value
"""


