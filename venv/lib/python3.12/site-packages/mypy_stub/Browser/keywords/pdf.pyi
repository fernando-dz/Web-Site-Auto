from ..base import LibraryComponent as LibraryComponent
from ..generated.playwright_pb2 import Request as Request
from ..utils import keyword as keyword, logger as logger
from ..utils.data_types import ColorScheme as ColorScheme, ForcedColors as ForcedColors, Media as Media, NotSet as NotSet, PdfFormat as PdfFormat, PdfMarging as PdfMarging, ReducedMotion as ReducedMotion
from os import PathLike

PdfMargingDefault: PdfMarging

class Pdf(LibraryComponent):
    def save_page_as_pdf(self, path: PathLike, *, displayHeaderFooter: bool = False, footerTemplate: str = '', format: PdfFormat = ..., headerTemplate: str = '', height: str = '0px', landscape: bool = False, margin: PdfMarging = ..., outline: bool = False, pageRanges: str = '', preferCSSPageSize: bool = False, printBackground: bool = False, scale: float = 1, tagged: bool = False, width: str = '0px') -> str: ...
    def emulate_media(self, colorScheme: ColorScheme | None = None, forcedColors: ForcedColors | NotSet = ..., media: Media | None = None, reducedMotion: ReducedMotion | None = None) -> None: ...
