from django.shortcuts import render,redirect, get_object_or_404
from .forms import CreateBlog
from .models import Blog
 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def mypage(request):
    return render(request, 'mypage.html')

def mypage(request):
    blogs = Blog.objects.all()
    return render(request, 'mypage.html', {'blogs': blogs})

def write(request):
 
    if request.method == 'POST':
        form = CreateBlog(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('mypage')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'write.html', {'form': form})
 

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
 
    return render(request, 'detail.html', {'blog_detail': blog_detail})