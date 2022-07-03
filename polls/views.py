from django.http import  HttpResponse

def index(request):
    return HttpResponse("hello, you are at the polls index")