from ..base import LibraryComponent as LibraryComponent
from ..utils import keyword as keyword, logger as logger
from ..utils.data_types import DelayedKeyword as DelayedKeyword, Scope as Scope

class RunOnFailureKeywords(LibraryComponent):
    def register_keyword_to_run_on_failure(self, keyword: str | None, *args: str, scope: Scope = ...) -> DelayedKeyword: ...
