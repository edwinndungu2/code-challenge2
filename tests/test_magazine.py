import os
os.environ["TESTING"] = "1"

from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def test_magazine_save_and_find():
    mag = Magazine("Code Monthly", "Tech")
    mag.save()
    found = Magazine.find_by_id(mag.id)
    assert found.name == "Code Monthly"

def test_magazine_find_by_name_and_category():
    mag = Magazine("Writers Digest", "Writing")
    mag.save()
    by_name = Magazine.find_by_name("Writers Digest")
    by_cat = Magazine.find_by_category("Writing")
    assert by_name.id == mag.id
    assert by_cat[0].name == "Writers Digest"

def test_magazine_articles_and_contributors():
    mag = Magazine("Art Today", "Visual Arts")
    mag.save()
    a1 = Author("Banksy")
    a2 = Author("Frida Kahlo")
    a1.save()
    a2.save()

    a1.add_article(mag, "Graffiti Revolution")
    a2.add_article(mag, "Self-Portrait of Power")

    articles = mag.articles()
    assert len(articles) == 2
    assert mag.contributors()[0].name in ["Banksy", "Frida Kahlo"]

def test_magazine_article_titles():
    mag = Magazine("Design Weekly", "Design")
    mag.save()
    author = Author("Zaha Hadid")
    author.save()
    author.add_article(mag, "Architecture of the Future")
    author.add_article(mag, "Beyond Curves")

    titles = mag.article_titles()
    assert titles == ["Architecture of the Future", "Beyond Curves"]

def test_contributing_authors_more_than_two_articles():
    mag = Magazine("Tech Quarterly", "Tech")
    mag.save()
    a1 = Author("Alan Turing")
    a2 = Author("Ada Lovelace")
    a1.save()
    a2.save()

    # 3 articles by Turing
    a1.add_article(mag, "Computing 101")
    a1.add_article(mag, "AI Foundations")
    a1.add_article(mag, "Turing Test")

    # 1 article by Ada
    a2.add_article(mag, "Analytical Engine")

    contributing = mag.contributing_authors()
    assert len(contributing) == 1
    assert contributing[0].name == "Alan Turing"
