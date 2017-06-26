class MutexAuditRule(AuditRule):
    """
    Represents a set of access rights to be audited for a user or group. This class cannot be inherited.
    
    MutexAuditRule(identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags)
    """
    @staticmethod # known case of __new__
    def __new__(self, identity, eventRights, flags):
        """ __new__(cls: type, identity: IdentityReference, eventRights: MutexRights, flags: AuditFlags) """
        pass

    AccessMask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access mask for this rule.

"""

    MutexRights = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the access rights affected by the audit rule.

Get: MutexRights(self: MutexAuditRule) -> MutexRights

"""


