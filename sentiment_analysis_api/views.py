from django.http import JsonResponse


def home(request):
    if request.method == "GET":
        return JsonResponse({"message": "Welcome to the Sentiment Analysis API."})


def test(request):
    if request.method == "GET":
        return JsonResponse({"message": "success"})
