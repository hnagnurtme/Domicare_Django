import threading

_thread_locals = threading.local()

def set_current_user(user):
    _thread_locals.user = user

def get_current_user():
    return getattr(_thread_locals, 'user', None)

def clear_current_user():
    if hasattr(_thread_locals, 'user'):
        del _thread_locals.user

class CurrentUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if hasattr(request, 'user'):
            set_current_user(request.user)

        response = self.get_response(request)

        clear_current_user()
        return response