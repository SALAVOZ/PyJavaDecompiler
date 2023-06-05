

class DCCommonState:
    def __init__(self):
        self.rel_class_type_cache = {}
        self.add()

    def add(self) -> None:
        self.rel_class_type_cache['java.lang.AssertionError'] = 'java.lang.AssertionError'
        self.rel_class_type_cache['java.lang.Object'] = 'java.lang.Object'
        self.rel_class_type_cache['java.lang.String'] = 'java.lang.String'
        self.rel_class_type_cache['java.lang.Enum'] = 'java.lang.Enum'

    def get_rel_class_type_cache(self):
        return self.rel_class_type_cache
