from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def post_list(request):
    # Получаем все посты
    posts = Post.objects.all()

    # Создаем пагинатор
    paginator = Paginator(posts, 10)  # 10 постов на странице

    # Преобразуем page_number в целое число
    page_number = request.GET.get('page', 1)
    page_posts = None

    try:
        page_number = int(page_number)
        page_posts = paginator.get_page(page_number)
    except ValueError:
        # Если page_number не является числом, возвращаемся на первую страницу
        page_posts = paginator.page(1)

    # Передаем контекст в шаблон
    return render(request, 'post_list.html', {'page_posts': page_posts})