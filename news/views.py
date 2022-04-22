from django.views import generic
from .models import News

class NewsList(generic.ListView):
    queryset = News.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'

class NewsDetail(generic.DetailView):
    model = News
    template_name = 'news_detail.html'