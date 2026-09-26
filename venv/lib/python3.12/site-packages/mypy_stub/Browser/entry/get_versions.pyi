from .constant import INSTALLATION_DIR as INSTALLATION_DIR, ROOT_FOLDER as ROOT_FOLDER, log as log, write_marker as write_marker
from dataclasses import dataclass

@dataclass
class Version:
    version: str
    from_cmd: bool

def get_rf_version(): ...
def get_pw_version() -> Version: ...
def print_version(ctx, param, value) -> None: ...
