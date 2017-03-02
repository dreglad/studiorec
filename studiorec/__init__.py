class ForceDefaultLanguageMiddleware(object):
    """Force default language"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'HTTP_ACCEPT_LANGUAGE' in request.META:
            del request.META['HTTP_ACCEPT_LANGUAGE']
        return self.get_response(request)
