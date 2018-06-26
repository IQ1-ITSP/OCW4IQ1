from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def test_response(request):
    return HttpResponse("OCW4IQ1")

def search_result(request):
    d = {'default_input_value' : '授業名'}
    return render(request,'searchAndResult.html',d)
