from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    """Allow JWTs supplied in an HttpOnly cookie named 'token'.

    This tries the normal Authorization header first. If absent, it will look
    for a cookie named 'token' and inject it into the request's
    HTTP_AUTHORIZATION header as a Bearer token so SimpleJWT can validate it.
    """

    def authenticate(self, request):
        # Try header-based authentication first
        user_auth = super().authenticate(request)
        if user_auth is not None:
            return user_auth

        token = None
        try:
            token = request.COOKIES.get('token')
        except Exception:
            token = None

        if not token:
            return None

        # Inject Authorization header and try again
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
        return super().authenticate(request)
