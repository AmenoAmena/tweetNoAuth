from django.shortcuts import render,redirect
from .forms import TweetForm
from .models import Tweet

# Create your views here.
def index(request,id=0):
    form = TweetForm()
    tweets = Tweet.objects.all()
    return render(request,'tweeting/index.html',{
        'tweets':tweets,
        'form':form
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

def update(request, id):
    tweet = Tweet.objects.get(pk=id)
    form = TweetForm(instance=tweet)
    if request.method == 'POST':
        form = TweetForm(request.POST, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'tweeting/update.html', {'form': form})
