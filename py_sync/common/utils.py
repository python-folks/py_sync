import re 
from itertools import zip_longest

SNAKE_CASE_STEP1 = re.compile('(.)_*([A-Z][a-z]+)')
SNAKE_CASE_STEP2 = re.compile('([a-z0-9])_*([A-Z])')

class attrdict(dict):
    def __getattr__(self, attr):
        try:
            return self[attr]
        except KeyError:
            raise AttributeError(attr)
    def __setattr__(self, attr, value): self[attr] = value
    def __iadd__(self, rhs): self.update(rhs); return self
    def __add__(self, rhs): d = attrdict(self); d.update(rhs); return d

def merge_dict(source, overrides):
    merged = source.copy()
    if overrides:
        merged.update(overrides)
    return merged

def quote(path, quote_chars):
    if len(path) == 1:
        return path[0].join(quote_chars)
    return '.'.join([part.join(quote_chars) for part in path])

def ensure_tuple(value):
    if value is not None:
        return value if isinstance(value, (list, tuple)) else (value,)

def make_snake_case(s):
    first = SNAKE_CASE_STEP1.sub(r'\1_\2', s)
    return SNAKE_CASE_STEP2.sub(r'\1_\2', first).lower()

def chunked(it, n):
    marker = object()
    for group in (list(g) for g in zip_longest(*[iter(it)] * n,
                                                fillvalue=marker)):
        if group[-1] is marker:
            del group[group.index(marker):]
        yield group