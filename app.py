from flask import Flask, redirect, url_for, render_template, request
from newsapi import NewsApiClient
import random
import validators

newsapi = NewsApiClient(api_key='a14f943cff544e4fa138bcd07daf54bc')

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/news')
def news():
    news = newsapi.get_everything(q="environment OR climate OR energy OR conservation", language="en", sort_by="relevancy", page_size=100)
    articles = news["articles"]

    rtn = []

    for i in range(9):
        temp = random.choice(articles)                                                          # stores the random article in a temporary variable
        while temp["urlToImage"] is None or not validators.url(temp["urlToImage"]):             # if there is not a url or if the url is invalid
            articles.remove(temp)
            temp = random.choice(articles)
        rtn.append(temp)                                                                        # adds the random article to the return list
        articles.remove(temp)                                                                   # removes the random article from the list of articles

    for article in rtn:                                                                         # limiting the length of the title
        if len(article["title"]) > 90:
            article["title"] = article["title"][0:article["title"].find(" ", 85)] + "..."       # this will add an ellipsis to the first space it finds starting from the 70th character

    return render_template("news.html", rtn=rtn)

@app.route('/events')
def events():
	return render_template('events.html')

@app.route('/my-events')
def my_events():
	return render_template('my_events.html')

if __name__ == '__main__':
	app.run(debug=True)