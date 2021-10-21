from django.shortcuts import render
import requests
from django.template.loader import get_template

# Create your views here.
def index(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=e718c33406ec4c8c91d6c2f5ec8397c6'
    Tech_news = requests.get(url).json()
    a = Tech_news['articles']
    desc =[]
    title =[]
    img =[]

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist = zip(title, desc, img)

    context = {'mylist': mylist}
    return render(request, r'C:\Users\Mihir\Desktop\SEM-7\CGC\Project\NewsApp\MainApp\Template\index.html', context)