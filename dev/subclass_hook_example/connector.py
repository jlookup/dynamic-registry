

from parent_with_registry import ParentWithRegistry

class Connector(ParentWithRegistry, lookup=None):
    """Abstract Connector class"""
    pass

Connector.register_subclasses()