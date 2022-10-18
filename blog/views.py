from django.shortcuts import render

from blog.models import Post, Categoria
# Create your views here.

def blog(request):
    # Obtenemos todos los posts
    posts = Post.objects.all()
    return render(request,'blog/blog.html', {'posts': posts})

def categoria(request, categoria_id):

    # Filtramos la categoria
    categoria=Categoria.objects.get(id=categoria_id)
    # Y el post por categoria filtrada
    posts = Post.objects.filter(categorias = categoria)
    return render(request, 'blog/categorias.html', {'categoria':categoria, 'posts':posts})