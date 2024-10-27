from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post


def index(request):
    posts = Post.objects.all()
    items_per_page = request.GET.get('items_per_page', 5)
    paginator = Paginator(posts, items_per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})
