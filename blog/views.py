from django.shortcuts import render, redirect
from .models import Category, Article

# Create your views here.
def new_view(request):
    if request.method == 'POST':
        title = request.POST.get('title',None)
        content = request.POST.get('content',None)
        category = request.POST.get('category',None)
        # html에서 입력받은 값이므로 category가 string형식

        # category object 형식으로 저장
        category = Category.objects.get(name=category)
        article = Article.objects.create(title=title, content=content, category=category)

        # 자동으로 pk 라는 필드를 만들어준다.
        # 첫번째 글을 썼다 -> pk = 1
        return redirect('detail', article.pk)
    elif request.method == 'GET':
        # 페이지 받아오면서 현 Category 모델에 존재하는 것만 사용자가 선택해야해서, 전체 불러온다.
        categories = Category.objects.all()
        return render(request, 'new.html',{'categories':categories})


def category_view(request):
    categories = Category.objects.all()
    infos = {}
    for category in categories:
        infos[category.name] = Article.objects.filter(category=category).count()
    return render(request, 'category.html', {'infos':infos})


# '127.0.0.1/movie' -> name = 'movie'
def article_view(request, name):
    category = Category.objects.get(name=name)
    articles = Article.objects.filter(category=category)
    return render(request, 'article.html', {'articles':articles})


# '127.0.0.1/detail/1' -> pk = 1
def detail_view(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'detail.html', {'article':article})
