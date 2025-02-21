import feedparser
class Enclosure:
    def __init__(self, enclosure):
        self.link = enclosure.url
        self.type = enclosure.type
        
class FeedArticle:
    def __init__(self, link, published, title, summary, enclosures, source):
        self.link = link
        self.published = published # tuple(YEAR, MONTH, DAY, HOUR, MINUTE, SECOND, WEEK DAY(0-6), YEAR DAY, DST flag)
        self.title = title
        self.summary = summary
        self.enclosures = enclosures
        self.type = "feed"
        self.source = source
        self.embedding = None

class FeedParser:
    def __init__(self,url):
        self.url =url
        
    def feed_parse(self) -> list[FeedArticle]:
        articles = []
        rss = feedparser.parse(self.url)
        for entry in rss.entries:
            articles.append(FeedArticle(
                link= entry.link,
                published = str(entry.published_parsed),
                title= entry.title,
                summary= entry.summary,
                enclosures = [Enclosure(i) for i in entry.enclosures],
                source = rss.feed.title
            ))
        return articles