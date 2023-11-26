from urllib.parse import urlunparse, urlparse, urlencode, parse_qsl


def add_query_params_to_url(base_url, query_params):
    url_parts = list(urlparse(base_url))
    query = dict(parse_qsl(url_parts[4]))
    query.update(query_params)
    url_parts[4] = urlencode(query_params)

    return urlunparse(url_parts)