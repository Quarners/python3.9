def print_content_list(authors: list[str]):
    for author in authors:
        print(author)

def print_content_dict(author: dict):
    for key_author in author.keys():
        print(author[key_author])

print("Author List")
authors = ["José Saramago", "Lord Byron", "Carlos Fuentes"]
print_content_list(authors=authors)

"""
Salida:

Author List
José Saramago
Lord Byron
Carlos Fuentes
"""

print("\nAuthor Dict")
author_dict = {"name": "José Saramago", "country": "Portugal", "is_Nobel": True}
print_content_dict(author=author_dict)

"""
Salida:

Author Dict
José Saramago
Portugal
True
"""