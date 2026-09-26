from robocop.formatter.formatters import Formatter
from robot.parsing.model.statements import KeywordCall

def is_same_keyword(first: str, second: str) -> bool: ...
def get_normalized_keyword(keyword: str) -> str: ...

OLD_KW_NAME: str
OLD_KW_NAME_WITH_LIB: str

class NetworkIdle(Formatter):
    def visit_KeywordCall(self, node: KeywordCall): ...
