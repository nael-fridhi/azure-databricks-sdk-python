import attr


@attr.s
class PrincipalName:
    """" PrincipalName: Container type for a name that is either a user name or a group name.
    [1]: https://docs.microsoft.com/en-us/azure/databricks/dev-tools/api/latest/groups#principalname
    """
    user_name: str = attr.ib(default=None)
    group_name: str = attr.ib(default=None)