class BuilderBaseClass:
    """Base class for building nested dictionaries."""

    def __init__(self):
        self.result = {}

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
            return self
        if not keys:
            raise ValueError("keys must contain at least one item")

        current = self.result
        for key in keys[:-1]:
            child = current.setdefault(key, {})
            if not isinstance(child, dict):
                raise ValueError(f"Cannot descend through non-dictionary value at {key!r}")
            current = child
        current[keys[-1]] = value
        return self

    def build(self):
        return self.result.copy()
