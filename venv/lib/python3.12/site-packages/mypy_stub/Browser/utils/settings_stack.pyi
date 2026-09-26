from ..browser import Browser as Browser
from .data_types import Scope as Scope
from _typeshed import Incomplete
from collections.abc import Callable as Callable
from dataclasses import dataclass
from typing import Any

@dataclass
class ScopedSetting:
    typ: Scope
    setting: Any

class SettingsStack:
    library: Incomplete
    setter_function: Incomplete
    def __init__(self, global_setting: Any, ctx: Browser, setter_function: Callable | None = None) -> None: ...
    def start(self, identifier: str, typ: Scope): ...
    def end(self, identifier: str): ...
    def set(self, setting: Any, scope: Scope | None = ...): ...
    def get(self): ...
