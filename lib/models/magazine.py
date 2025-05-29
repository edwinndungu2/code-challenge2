from lib.db.connection import get_connection

class Magazine:
    def __init__(self, name, category, id=None):
        self.id = id
        self.name = name
        self.category = category

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", (self.name, self.category, self.id))
        else:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        return cls(name=row["name"], category=row["category"], id=row["id"]) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        return cls(name=row["name"], category=row["category"], id=row["id"]) if row else None

    @classmethod
    def find_by_category(cls, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        rows = cursor.fetchall()
        conn.close()
        return [cls(name=row["name"], category=row["category"], id=row["id"]) for row in rows]

    def articles(self):
        from lib.models.article import Article
        return Article.find_by_magazine_id(self.id)

    def contributing_authors(self):
        from lib.models.author import Author
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT a.author_id, COUNT(*) as article_count
            FROM articles a
            WHERE a.magazine_id = ?
            GROUP BY a.author_id
            HAVING article_count > 2
        """, (self.id,))
        rows = cursor.fetchall()
        authors = []
        for row in rows:
            author = Author.find_by_id(row["author_id"])
            if author:
                authors.append(author)
        conn.close()
        return authors