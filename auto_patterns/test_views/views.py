from django.http import HttpResponse

def page(request, slug: str):
    return HttpResponse()

def comment(request, page_slug: str, comment_id: int):
    return HttpResponse()