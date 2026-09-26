from .constant import INSTALLATION_DIR as INSTALLATION_DIR, IS_TERMINAL as IS_TERMINAL, PLAYWRIGHT_BROWSERS_PATH as PLAYWRIGHT_BROWSERS_PATH, SHELL as SHELL, log as log, write_marker as write_marker
from _typeshed import Incomplete

has_pty: bool
ANSI_ESCAPE: Incomplete
PROGRESS_MATCHER: Incomplete
PROGRESS_SIZE: int

def log_install_dir(error_msg: bool = True) -> None: ...
def format_progress_bar(message: str) -> tuple[str, str]: ...
def rfbrowser_init(skip_browser_install: bool, silent_mode: bool, with_deps: bool, browser: list): ...
