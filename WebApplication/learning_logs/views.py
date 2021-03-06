from django.shortcuts import render
from learning_logs.models import Topic


# Create your views here.

def index(request):
    # Main page for learning_logs
    return render(request, 'learning_logs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
