from authentication.models import UserToken


def is_authenticated(request) -> bool:

    if "authorization" in request.headers:
        token_str = request.headers.get("authorization")

        # Get the first user_token instance if available
        user_token = UserToken.objects.filter(token=token_str).first()
        if user_token:
            # If token exists, set request.user=user and return True
            request.user = user_token.user
            return True