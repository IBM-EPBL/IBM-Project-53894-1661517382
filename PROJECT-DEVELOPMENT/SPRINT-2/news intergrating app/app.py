from flask import Flask,render_template
from newsapi import NewsApiClient

app = Flask(__name__)


@app.route('/')
def index():
    newsapi = NewsApiClient(api_key = "faeeea5c0d764c4faa9a2bcbd4af3ca3")
    topheadlinesindia= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=in")
    articles =topheadlinesindia['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist1=zip(news,desc,img)
    topheadlinessouthkorea = newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=kr")
    articles = topheadlinessouthkorea['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist2=zip(news,desc,img)


    topheadlinesthailand= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=th")
    articles = topheadlinesthailand['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist3 =zip(news,desc,img)


    topheadlinesuk= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=gb")
    articles =topheadlinesuk['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist4 =zip(news,desc,img)
    

    topheadlinesukrane= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=ua")
    articles =topheadlinesukrane['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist5 =zip(news,desc,img)
    

    topheadlinesrussia= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=ru")
    articles =topheadlinesrussia['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist6 =zip(news,desc,img)


    topheadlinestiwan= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=tw")
    articles =topheadlinestiwan['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist7 =zip(news,desc,img)
   

    topheadlinesfrance= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=fr")
    articles =topheadlinesfrance['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist8 =zip(news,desc,img)
   

    topheadlinesgermany= newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=de")
    articles =topheadlinesgermany['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist9 =zip(news,desc,img)
    

    topheadlineschina = newsapi.get_top_headlines(sources = "https://newsapi.org/v2/top-headlines?country=cn")
    articles = topheadlineschina['articles']

    desc = []
    news = []
    img = []
    for i in range(len(articles)):
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist10 =zip(news,desc,img)
    mylist = zip(mylist1,mylist2,mylist3,mylist4,mylist5,mylist6,mylist7,mylist8,mylist9,mylist10)
    return render_template (index.html, context = mylist)

if __name__ == "__main__":
    app.run(debug = True)