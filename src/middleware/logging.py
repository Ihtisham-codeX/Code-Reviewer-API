# middleware designed to return the details of each endpoint called

import time
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request

# Request Object : 
# URL
# Method
# Headers
# Cookies
# Body
# Client IP


class LoggingMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        start_time = time.time()

        # Process the request
        response = await call_next(request)

        # Calculate time taken
        process_time = round(time.time() - start_time, 4)

        # Log request details where request.client.host -> User's IP 
        print(
            f"{request.method} {request.url.path} "
            f"| Status: {response.status_code} "
            f"| Time: {process_time}s "
            f"| IP: {request.client.host}"
        )

        # final response that the user will get
        return response
