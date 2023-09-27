# views.py

from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
# def index(request):
#     # DB에서 전체 게시글을 조회 후 받은 전체 게시글 데이터를 변수에 담아
#     articles = Article.objects.all()
#     context = {
#         'articles' : articles
#     }
#     # index 템플릿에서 사용할 수 있도록 전달
#     return render(request, 'index.html',context)
    
def index2(request):
    # 게시글 목록 조회해서 템플릿에 전달
    # 1. 게시글 목록 db에서 조회
    #   ORM을 이용해야 하는데 >> 이 역할을 model class가 수행
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index2.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # 요청에서 데이터 받아와서 db에 저장
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title,content=content)
    article.save()
    # 목록조회해서 템플릿에전달
    # articles = Article.objects.all()

    # context = {
    #     'articles' : articles
    # }
    # return render(request, 'articles/index2.html',context)
    return redirect('articles:index')

def delete(request, pk):
    # db에서 삭제하고 목록조회에서 템플릿에 전달
    # record 단위는 instance로 처리...
    instance = Article.objects.get(pk=pk)
    instance.delete()

    # articles = Article.objects.all()
    # context = {
    #     'articles' : articles
    # }
    # return render(request, 'articles/index2.html',context)
    return redirect('articles:index')

def detail(request, pk):
    # db에서 pk에 해당하는 게시글  조회
    Article.objects.get(pk=pk)
    context = {

    }
    return render(request, 'articles/detail.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/update.html', context)

def update(request, pk):
    # 원래 db에 저장되어있던 데이터 가져옴
    article = Article.objects.get(pk=pk)
    # 내용수정
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index')