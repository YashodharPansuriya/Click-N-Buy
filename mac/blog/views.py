from django.shortcuts import render
from .models import Blogpost
from django.http import HttpResponse

# Create your views here.
def index(request):
    allblog = []
    blogid = Blogpost.objects.values('post_id')
    print(blogid)
    for item in blogid:
        print(item['post_id'])
        blogdetails = Blogpost.objects.filter(post_id=item['post_id'])
        print(blogdetails)
        n=len(blogdetails)
        allblog.append(blogdetails)
        print(allblog)
        params = {'allblog':allblog}
    return render(request, 'blog/index.html', params)

def blogpost(request, myid):
    print(myid)
    blogpostdetails = Blogpost.objects.filter(post_id=myid)
    params = {'blogpostdetails': blogpostdetails}
    return render(request, "blog/blogpost.html", params)

