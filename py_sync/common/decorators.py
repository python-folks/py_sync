

class method_alias:

    def __init__(self, fn):
        self.instance_handle = fn
        self.class_handle = None

    def for_class(self, fn):
        self.class_handle = fn
        return fn

    def __get__(self, instance, klass):
        def dynamic_handle(*args):
            if instance is None:
                return self.class_handle(klass, *args)
            else:
                return self.instance_handle(instance, *args)
        return dynamic_handle

