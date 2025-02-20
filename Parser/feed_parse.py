import feedparser
class Enclosures:
    def __init__(self, enclosures):
        self.enclosures =enclosures
        self.url = []
        self.type = []
        for i in enclosures:
            self.url.append(i.url)
            self.type.append(i.type)
        
class FeedArticle:
    def __init__(self, link, pubDate, title, description, enclosures):
        self.link = link
        self.pubDate = pubDate
        self.title = title
        self.description = description
        self.enclosures = enclosures
        
def feed_parse(url):
    """_summary_

    Args:
        url (string): feed url to parse

    Returns:
        FeedArticle[]: list of articles
    """
    articles = []
    rss = feedparser.parse(url)
    for entry in rss.entries:
        articles.append(FeedArticle(
            entry.link,
            entry.published_parsed,
            entry.title,
            entry.description,
            Enclosures(entry.enclosures)
        ))
    return articles
    