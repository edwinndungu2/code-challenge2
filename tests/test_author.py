import os
os.environ["TESTING"] = "1"

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_author_save_and_find_by_id():
    author = Author("Chimamanda Ngozi Adichie")
    author.save()
    found = Author.find_by_id(author.id)
    assert found.name == "Chimamanda Ngozi Adichie"

def test_author_find_by_name():
    author = Author("George Orwell")
    author.save()
    found = Author.find_by_name("George Orwell")
    assert found.id == author.id

def test_author_articles_and_magazines():
    author = Author("Octavia Butler")
    author.save()

    mag1 = Magazine("SciFi World", "Science Fiction")
    mag1.save()
    mag2 = Magazine("Futures", "Sci-Fi")
    mag2.save()

    author.add_article(mag1, "Time Travel Myths")
    author.add_article(mag2, "Alien Encounters")

    articles = author.articles()
    assert len(articles) == 2
    assert articles[0].title == "Time Travel Myths"
    assert articles[1].title == "Alien Encounters"

    mags = author.magazines()
    assert {m.name for m in mags} == {"SciFi World", "Futures"}

def test_author_topic_areas():
    author = Author("Ursula Le Guin")
    author.save()
    mag1 = Magazine("Galactic News", "Sci-Fi")
    mag2 = Magazine("Fantasy Weekly", "Fantasy")
    mag1.save()
    mag2.save()
    author.add_article(mag1, "The Left Hand of Darkness")
    author.add_article(mag2, "Earthsea Revisited")

    categories = author.topic_areas()
    assert set(categories) == {"Sci-Fi", "Fantasy"}
