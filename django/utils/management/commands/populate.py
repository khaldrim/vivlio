
import random
import string
from faker import Faker
import json
# Base command
from django.core.management.base import BaseCommand, CommandError
# Models
from users.models import User
from library.models import Library
from books.models import Book
from books.models import BookLibrary
from tags.models import Tag


class Command(BaseCommand):


    def handle(self, *args, **options):

        print("Creando usuarios...")
        self.populate_users()
        print("Creando librerías...")
        self.populate_library()
        print("Creando géneros...")
        self.populate_tags()
        print("Creando libros...") # 8334
        self.populate_books()
        print("Asignando géneros a los libros...")
        self.assign_tags()
        print("Asignando libros a librerías...")
        self.assign_library()
        print("Base de datos poblada correctamente!")
    def random_char(self, y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))


    def populate_users(self):
        # Create 50 users
        fake = Faker()
        for i in range(0, 50):
            name = fake.name()
            rand_first_name = name.split(" ")[0]
            rand_last_name = name.split(" ")[1]
            rand_email = name.replace(" ","")+'@gmail.com'
            rand_password = self.random_char(random.randint(6,10))
            user = User(
                first_name = rand_first_name,
                last_name = rand_last_name,
                email = rand_email,
                password = rand_password
            )
            user.save()
    def populate_library(self):
        fake = Faker()
        for i in range(0,5):
            rand_name = fake.name().split(" ")[1]
            rand_address = fake.address()
            library = Library(
                name = rand_name,
                address = rand_address
            )
            library.save()
    def populate_tags(self):
        tag_list = ['Drama', 'Comedia', 'Terror', 'Aventura',
         'Ciencia Ficción', 'Fantasía', 'Amor']

        for tag in tag_list:
            tag_instance = Tag(
                tag_name = tag
            )
            tag_instance.save()
    def populate_books(self):
        f = open("./django/books_db.json", "r")
        languages = ['es', 'eng']
        file_string = ""
        for line in f:
            file_string = file_string + line
        f.close()
        file_json = json.loads(file_string)
        for book in file_json:
            if book['author']:
                author = book['author'].capitalize()
            else:
                author = "---"
            book = Book(
                    authors = author,
                    title = book['name'].capitalize(),
                    language_code = languages[random.randint(0,1)],
                    image_url = book['img'],
                    summary = book['sinopsis']
                )
            book.save()

    def assign_tags(self):
        tags = Tag.objects.all()
        books = Book.objects.all()
        for book in books:
            tags_aux = tags
            tag_number = random.randint(1,3)
            tags_for_book = random.sample(list(tags), tag_number)
            for tag in tags_for_book:
                book.tag.add(tag)

    def assign_library(self):
        library_objs = Library.objects.all()
        books = Book.objects.all()
        for book in books:
            library_number = random.randint(1,library_objs.count())
            library_for_book = random.sample(list(library_objs), library_number)
            for library in library_for_book:
                random_price = random.randint(10000, 50000)
                book_library = BookLibrary(
                    book = book,
                    library = library,
                    price = random_price
                )
                book_library.save()
