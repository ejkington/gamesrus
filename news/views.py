from django.views import generic
from .models import News

class NewsList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'

class NewsDetail(generic.DetailView):
    model = News
    template_name = 'News_detail.html'