from lib.models.author import Author

# Create new author
a = Author("Edcarter")
a.save()

# Find by ID
fetched = Author.find_by_id(a.id)
print(fetched.name)

# List all
all_authors = Author.all()
for auth in all_authors:
    print(auth.name)
