from django.http import HttpRequest, HttpResponse

class MethodOverrideMiddleware:
    def __init__(self, get_response: HttpResponse):
        self.get_response = get_response
    
    def __call__(self, request: HttpRequest):
        if request.method == "POST" and '_method' in request.POST:
            method = request.POST['_method'].upper()
            if method in ['PUT', 'PATCH', 'DELETE']:
                request.method = method
                request.META["REQUEST_METHOD"] = method
            
        return self.get_response(request)
        


