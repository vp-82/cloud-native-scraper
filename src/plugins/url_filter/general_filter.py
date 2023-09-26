from plugins.url_filter_plugin import URLFilterPlugin


class GeneralPurposeFilter(URLFilterPlugin):
    
    def should_collect(self, url: str) -> bool:
        # Omit URLs with "#"
        if "#" in url:
            return False
        return True
