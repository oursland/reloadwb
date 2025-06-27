from __future__ import annotations

import FreeCAD as App # type: ignore
from typing import ClassVar

class HotSwapCommand:
    _instances: ClassVar[list[HotSwapCommand]] = []

    def __init__(self, *, resources: dict[str, object], impl: type) -> None:
        self._resources = resources
        self._name = impl.__name__
        self._module = impl.__module__
        self._reload = False
        self._impl = impl()
        HotSwapCommand._instances.append(self)

    def _reload_if_required(self) -> None:
        if self._reload:
            App.Console.PrintWarning(f"Reloading {self._module}.{self._name}")
            import importlib
            mod = importlib.import_module(self._module)
            importlib.reload(mod)
            cls = getattr(mod, self._name)
            self._impl = cls()
            self._reload = False

    def reload(self) -> None:
        self._reload = True

    @classmethod
    def reload_all(cls) -> None:
        for inst in cls._instances:
            inst.reload()

    def GetResources(self) -> dict[str, object]:
        return self._resources

    def Activated(self) -> None:
        self._reload_if_required()
        self._impl.Activated()

    def IsActive(self) -> bool:
        self._reload_if_required()
        return self._impl.IsActive()
