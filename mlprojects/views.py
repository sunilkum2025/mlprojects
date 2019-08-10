from django.http import HttpResponse
def homepage(request):
    return HttpResponse("<h1>This is My First Page</h1>")