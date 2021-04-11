from django.shortcuts import render

# Create your views here.


def Blog(request):
    posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


def Categorias(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, 'categorias.html', {'categoria': categoria, 'posts': posts})


# def Details(request, slug):
#    post = get_object_or_404(Post, slug=slug)
#    return render('detail.html', {'post': post})

class BlogDetalView(DetailView):
    model = Post
    template_name = 'detail.html'
