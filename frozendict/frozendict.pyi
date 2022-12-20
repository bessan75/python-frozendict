from collections.abc import Hashable
from typing import Any, Generic, NoReturn, TypeVar, overload

try:
    from typing import Mapping, Sequence, Iterable, Iterator
except ImportError:
    from collections.abc import Mapping, Sequence, Iterable, Iterator

_K = TypeVar("_K", Hashable)
_V = TypeVar("_V")
_KV = TypeVar("_V", _K, _V)

def frozendict_or(
    self: Mapping[_K, _V], other: Mapping[_K, _V]
) -> "frozendict[_K, _V]": ...

class frozendict(Mapping[_K, _V], Generic[_K, _V]):
    # Fake __init__ to describe what __new__ does:
    @overload
    def __init__(self, **kwargs: _V) -> None: ...
    @overload
    def __init__(self, mapping: Mapping[_K, _V]) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[Sequence[_KV]]) -> None: ...

    # Magic Methods:
    def __getitem__(self, __key: _K) -> _V: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[_K]: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...
    def copy(self) -> "frozendict[_K, _V]": ...
    def __copy__(self) -> "frozendict[_K, _V]": ...
    def __deepcopy__(self) -> "frozendict[_K, _V]": ...
    # Omit __reduce__, its used for Pickle and we don't need the annotation in code.
    def set(self, key: _K, value: _V) -> "frozendict[_K, _V]": ...
    def setdefault(self, key: _K, default: _V) -> "frozendict[_K, _V]": ...
    def delete(self, key: _K) -> "frozendict[_K, _V]": ...
    def key(self, index: int) -> _K: ...
    def value(self, index: int) -> _V: ...
    def item(self, index: int) -> Sequence[_KV]: ...
    def __or__(self: Mapping[_K, _V], other: Mapping[_K, _V]) -> "frozendict[_K, _V]": ...
    def __reversed__(self) -> Iterator[_K]: ...

    # Blacklisted methods:
    def __setattr__(self, *a, **kw) -> NoReturn: ...
    def __delattr__(self, *a, **kw) -> NoReturn: ...


FrozenOrderedDict = frozendict
