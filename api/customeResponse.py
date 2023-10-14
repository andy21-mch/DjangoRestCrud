from rest_framework.response import Response

class ApiResponse(Response):
    def __init__(self, message=None, data=None, status_code=None, **kwargs):
        response_data = {
            'message': message,
            'data': data
        }

        if status_code is not None:
            kwargs['status'] = status_code

        super().__init__(response_data, **kwargs)