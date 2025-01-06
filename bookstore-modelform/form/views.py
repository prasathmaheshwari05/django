from django.shortcuts import render
from django.http import HttpResponse
from .forms import ReviewForm
# Create your views here.
def review(request):
    # return render(request,'reviews/review.html')
    if request .method=='POST':
        print(form.cleaned_data)
        return HttpResponse('thank you')
    else:
        form=ReviewForm()
        return render(request,'reviews/reviewform.html',{
            'form':form
        })