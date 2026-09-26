from _typeshed import Incomplete
from pathlib import Path

KEYWORD_NAME: str
DOC_CHANGED: str
NO_LIB_KEYWORD: str
MISSING_TRANSLATION: str
MISSING_CHECKSUM: str
MAX_REASON_LEN: Incomplete

def get_library_translation(plugings: str | None = None, jsextension: str | None = None) -> dict: ...
def compare_translation(filename: Path, library_translation: dict): ...
