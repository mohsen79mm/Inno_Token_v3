from django.shortcuts import render , get_object_or_404 
from django.views import generic
from .models import Post
from taggit.models import Tag 
from django.http import HttpResponseNotFound



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_list.html'
    # paginate_by = 12

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'
#     queryset = Post.objects.filter()

def postDetail(request, url):
    if request.method == 'GET':
        try:
            product_object = Post.objects.get(url=url)
            product_object_dict = {'object': product_object}
        except:
            return HttpResponseNotFound('not found')

        return render(request, 'post_detail.html', context=product_object_dict)


def tagged(request,tag) : 
    gag = get_object_or_404(Tag , slug = tag) 
    posts = Post.objects.filter(tag = gag)
    context = {
        'tag' : gag , 
        'posts' : posts ,
    }
    return render(request , 'tag_list.html' , context)

def about(request):
    return HttpResponse('about page')

def snippet_detail(request, slug):
    snippet = get_object_or_404(post_detail, url=str)
    return HttpResponse(f'the detailview for slug of {slug}')    