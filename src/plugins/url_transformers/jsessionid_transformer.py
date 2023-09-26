from plugins.url_transform_plugin import URLTransformPlugin


class JSessionIDRemover(URLTransformPlugin):
    def transform(self, url: str) -> str:
        return url.split(";jsessionid=")[0]