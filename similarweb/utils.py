import tldextract
from similarweb.exceptions import InvalidURLException


def domain_from_url(url):
    """
    Get root domain from url.
    Will prune away query strings, url paths, protocol prefix and sub-domains
    Exceptions will be raised on invalid urls
    """
    ext = tldextract.extract(url)
    if not ext.suffix:
        raise InvalidURLException()
    new_url = ext.domain + "." + ext.suffix
    return new_url
