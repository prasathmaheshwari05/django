from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string 
from .models import Book
from django.shortcuts import render,get_object_or_404
# Create your views here.
def index(request):
    # return render(request,'author/index.html')
# def feb(request):
#     return HttpResponse('tommorow is holiday')
# def mar(request):
#     return HttpResponse('no is holiday')

# dis={'jan':'totay is holidy','feb':'tomorrow holiday','mar':'no leave'}
    # content={'name':'gobal'}
    # return HttpResponse(render_to_string('author/index.html',content))

    book=Book.objects.all()
    return render(request,'author/index.html',{
        'book_collection':book
    })
def bookdetails(request,id):
    # try:
    #     book=Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    books=get_object_or_404(Book,pk=id)
    return render(request,'author/detail.html',{
        'title':books.title,
        'rating':books.rating
    })