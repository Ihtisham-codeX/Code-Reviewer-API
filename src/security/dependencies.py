from fastapi import Request


# Called whenever a route uses Depends(get_current_user)
# AuthMiddleware already verified the JWT and attached the payload to request.state.user
# So we simply read and return it here , no re-verification needed

def get_current_user(request: Request):
    return request.state.user
