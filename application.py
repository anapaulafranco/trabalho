Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@anapaulafranco 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


FernandoFBueno
/
trabalhoCloud
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Update application.py

 main
@FernandoFBueno
FernandoFBueno committed 29 minutes ago 
1 parent 374d14f commit b3fe58464359eb30bd0803d2b4ad1dafff065678
Showing  with 11 additions and 6 deletions.
 17  application.py 
@@ -16,23 +16,28 @@
access_token_secret = 'dMwqHfUPFarhLJBbTLavRbpNBqCEA34YTX2dv5F0eJjb6'

g = []


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


@application.route("/")
def hello():
    return "<h1>TRABALHO DE CLOUD 44BDT</h1><h3>AWS CODE PIPELINE - ELASTIC BEANSTALK</h3><p>Esta aplicacao lista os Trending Topics do Twitter a cada clique no botão abaixo</p><p><a href='getTrendingTopics'>Ver Trending Topics</a></p>"


@application.route("/getTrendingTopics")
def gettingTopics():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    BRAZIL_WOE_ID = 23424768
    brazil_trends = api.trends_place(BRAZIL_WOE_ID)
    trends = json.loads(json.dumps(brazil_trends, indent=1))

    tt = []
    for trend in trends[0]["trends"]:
        tt.append("<br>"+trend["name"])

    return "<h1>TRABALHO DE CLOUD 44BDT</h1><h3>AWS CODE PIPELINE - ELASTIC BEANSTALK</h3><p>Esta aplicacao lista os Trending Topics do Twitter a cada reload da pagina</p>"+ '\n'.join(tt)
    return "<h1>TRABALHO DE CLOUD 44BDT</h1><h3>AWS CODE PIPELINE - ELASTIC BEANSTALK</h3><p>Esta aplicacao lista os Trending Topics do Twitter a cada clique no botão abaixo</p><p><a href='getTrendingTopics'>Ver Trending Topics</a></p>"+ '\n'.join(tt)


if __name__ == '__main__':
0 comments on commit b3fe584
@anapaulafranco
 
 
Leave a comment
Nenhum arquivo selecionado
Attach files by dragging & dropping, selecting or pasting them.
 You’re not receiving notifications from this thread.
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
