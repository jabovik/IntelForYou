import sqlite3
import datetime


class DB:
    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.con.autocommit = True
        self._create_tables()

    def __del__(self):
        self.con.close()

    def _create_tables(self):
        # Table of articles fetched from RSS
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS articles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT NOT NULL,
                title TEXT,
                description TEXT,
                link TEXT NOT NULL,
                type TEXT NOT NULL,
                published TEXT,
                inserted TEXT NOT NULL,
                embedding TEXT
            )
            
        """
        )
        # Table of enclosures
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS media(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                article_id INTEGER NOT NULL,
                type TEXT NOT NULL,
                link TEXT NOT NULL
            )
        """
        )
        print("tables created!")

    def _add_feed_article(self, article):
        self.cur.execute(
            """
            INSERT INTO articles(title, description,link,type,embedding, source,published, inserted)
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                article.title,
                article.summary,
                article.link,
                article.type,
                article.embedding,
                article.source,
                article.published,  # Those datetime formats are different
                str(datetime.datetime.now()),  # Needs to be fixed
            ),
        )
        id = self.cur.lastrowid
        for enclosure in article.enclosures:
            self.cur.execute(
                """
                INSERT INTO media(article_id,type,link)
                VALUES(?,?,?)
                """,
                (id, enclosure.type, enclosure.link),
            )

    def _add_telegram_article(self, article):
        pass

    def add_article(self, article):
        method_name = f"_add_{str(article.type)}_article"  # method is called the same as the type of an article
        method = getattr(self, method_name)
        method(article)

    def show_articles(self):
        self.cur.execute("SELECT * FROM articles")
        return self.cur.fetchall()

    def delete_all(self):
        self.cur.execute("DELETE FROM articles")
        self.cur.execute("DELETE FROM media")
