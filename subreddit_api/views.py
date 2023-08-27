from django.shortcuts import render
import praw
from django.http import JsonResponse

# Create your views here.


def get_subreddit_threads(request):
    reddit = praw.Reddit(
        client_id='YZUySt-F_O1juGB6a9kobg',
        client_secret='WkqNw_arno1pIvUxjnnxcy_YjsQeCw',
        user_agent='0xsynapse'
    )
    subreddit = reddit.subreddit('technology')
    threads_url = f"https://www.reddit.com/r/technology//new.json?limit=10"
    print("Reddit API URL:", threads_url)
    
    threads = subreddit.new(limit=10)
    
    data = []
    for thread in threads:
        data.append({
            'title': thread.title,
            'author': thread.author.name,
            'creation_date': thread.created_utc,
            'link': thread.url
        })
    
    #return JsonResponse(data, safe=False)
    return render(request, 'index.html', {'data': data})
