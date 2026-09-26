from ..utils import logger as logger
from Browser.base import LibraryComponent as LibraryComponent

class Crawling(LibraryComponent):
    def crawl_site(self, url: str | None = None, page_crawl_keyword: str = 'take_screenshot', max_number_of_page_to_crawl: int = 1000, max_depth_to_crawl: int = 50): ...
