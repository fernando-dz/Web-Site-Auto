from ..base import LibraryComponent as LibraryComponent
from ..utils import Scope as Scope, keyword as keyword, logger as logger

class StrictMode(LibraryComponent):
    def set_strict_mode(self, mode: bool, scope: Scope = ...): ...
