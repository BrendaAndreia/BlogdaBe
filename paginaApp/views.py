from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

def home(request):
    recent_posts = Post.objects.order_by('-data_postagem')[:4]
    context = {'recent_posts': recent_posts}
    return render(request, 'pagina/home.html', context)

def contatos(request):
    return render(request, 'pagina/contatos.html')

def sobre(request):
    return render(request, 'pagina/sobre.html')

def posts(request):
    posts = Post.objects.all().order_by('-data_postagem')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'pagina/posts.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'pagina/post_detail.html', {'post': post})

def post_list_by_tag(request, tag):
    posts = Post.objects.filter(tags__name__in=[tag]).order_by('-data_postagem')
    return render(request, 'pagina/posts.html', {'posts': posts, 'tag': tag})

