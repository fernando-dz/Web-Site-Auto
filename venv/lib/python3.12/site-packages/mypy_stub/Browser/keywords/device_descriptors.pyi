from ..base import LibraryComponent as LibraryComponent
from ..generated.playwright_pb2 import Request as Request
from ..utils import keyword as keyword, logger as logger

class Devices(LibraryComponent):
    def get_devices(self) -> dict: ...
    def get_device(self, name: str) -> dict: ...
