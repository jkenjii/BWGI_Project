
def computed_property(*dependencias):
    def decorator(func):
        nome_cache = "_cache_" + func.__name__
        nome_deps = "_deps_" + func.__name__
        def getter(self):
            valores = tuple(getattr(self, d, None) for d in dependencias)
            antigo = getattr(self, nome_deps, None)
            if valores != antigo:
                setattr(self, nome_deps, valores)
                setattr(self, nome_cache, func(self))
            return getattr(self, nome_cache)
        def setter(self, value):
            setattr(self, nome_cache, value)
        def deleter(self):
            if hasattr(self, nome_cache):
                delattr(self, nome_cache)
        prop = property(getter, setter, deleter)
        prop.__doc__ = func.__doc__
        return prop
    return decorator
