from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def post_list(request):
    posts = Post.objects.all()

    posts_per_page = request.GET.get('posts_per_page', 10)

    paginator = Paginator(posts, posts_per_page)

    page_number = request.GET.get('page', 1)
    page_posts = None

    try:
        page_number = int(page_number)
        page_posts = paginator.get_page(page_number)
    except ValueError:
        page_posts = paginator.page(1)

    return render(request, 'post_list.html', {'page_posts': page_posts, 'posts_per_page': posts_per_page})
