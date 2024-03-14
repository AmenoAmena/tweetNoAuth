from django.shortcuts import render,redirect
from .forms import TweetForm
from .models import Tweet

# Create your views here.
def index(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = TweetForm()
        else:
            tweets = Tweet.objects.get(pk=id)
            form = TweetForm(instance=task)
    tweets = Tweet.objects.all()
    return render(request,'tweeting/index.html',{
        'tweets':tweets,
        })

def add(request):
    form = TweetForm()
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = TweetForm()
        return redirect('index')

    return render(request,'tweeting/add.html',{
        'form':form
    })

def delete(request, id):
    tweet = Tweet.objects.get(pk=id)
    tweet.delete()
    return redirect('index')
