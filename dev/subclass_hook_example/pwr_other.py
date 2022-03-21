

from parent_with_registry import ParentWithRegistry

class Other(ParentWithRegistry, lookup='other'):
   pass

Other.register_subclasses()