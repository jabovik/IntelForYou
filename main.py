import DB.IntelDB
import Parser.feed_parse

db = DB.IntelDB.DB("IFY.db")
db.delete_all()
with open("rss.txt", "r") as f:
    rss_links = f.readlines()
    for link in rss_links:
        parser = Parser.feed_parse.FeedParser(link)
        articles = parser.feed_parse()
        for article in articles:
            db.add_article(article)
articles = db.show_articles()
for i in articles:
    print(i)
