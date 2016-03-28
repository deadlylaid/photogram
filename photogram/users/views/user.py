from django.http import HttpResponse


def user(request):
    return HttpResponse(
        "hello world",
    )
