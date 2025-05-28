import os
os.environ["TESTING"] = "1"

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_article_save_and_find():
    author = Author("Mary Shelley")
    mag = Magazine("Horror Weekly", "Horror")
    author.save()
    mag.save()

    article = Article("Frankenstein Lives", author.id, mag.id)
    article.save()

    found = Article.find_by_id(article.id)
    assert found.title == "Frankenstein Lives"

def test_article_find_by_title():
    author = Author("Stephen King")
    mag = Magazine("Dark Tales", "Horror")
    author.save()
    mag.save()

    article = Article("The Shining Explained", author.id, mag.id)
    article.save()

    found = Article.find_by_title("The Shining Explained")
    assert found.id == article.id

def test_article_author_and_magazine_properties():
    author = Author("Neil Gaiman")
    mag = Magazine("Mythos Monthly", "Fantasy")
    author.save()
    mag.save()

    article = Article("American Gods Deep Dive", author.id, mag.id)
    article.save()

    found = Article.find_by_id(article.id)
    assert found.author().name == "Neil Gaiman"
    assert found.magazine().name == "Mythos Monthly"
