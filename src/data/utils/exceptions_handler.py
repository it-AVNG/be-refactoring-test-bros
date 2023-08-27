#https://www.django-rest-framework.org/api-guide/exceptions/#custom-exception-handling

from rest_framework.views import exception_handler
from rest_framework.exceptions import Throttled

def custom_exceptions_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # check that a Throttled exception instance is raised
    if isinstance(exc, Throttled): 
        # prepare custom response data
        custom_response_data = { 
            #add status code to response
            'status_code': response.status_code,
            'message': 'Get a chill pill B, exceed connecting limit',
            'available_in': '%d seconds'%exc.wait
        }
        # set the custom response data on response object
        response.data = custom_response_data 
    return response