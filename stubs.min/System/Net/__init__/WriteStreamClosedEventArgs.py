class WriteStreamClosedEventArgs(EventArgs):
    """ WriteStreamClosedEventArgs() """
    Error = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Error(self: WriteStreamClosedEventArgs) -> Exception

"""


