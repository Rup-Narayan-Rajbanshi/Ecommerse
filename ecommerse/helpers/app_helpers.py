
def url_builder(obj, request):
    build_url = None
    try:
        from chowk.settings import PROXY_URL, MEDIA_URL
        url = None
        if isinstance(obj, str):
            len_media = len(MEDIA_URL)
            url = obj if obj[:len_media] == MEDIA_URL else MEDIA_URL + obj
        else:
            url = obj.url
        build_url = PROXY_URL + url
    except Exception as e:
        build_url = None
    return build_url
