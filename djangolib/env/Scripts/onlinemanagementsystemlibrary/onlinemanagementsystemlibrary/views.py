 
from django.forms import models
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .Models import Book

# Create your views here.
 

def add_book(request):
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
       
        books =Book.objects.create( name=name, author=author, isbn=isbn, category=category)
        books.save()
        alert = True
        return render(request, "add_book.html", {'alert':alert})
    return render(request, "add_book.html")

def view_books(request):
    books =Book.objects.all()
    books_dict ={
        'books':books
    }
    return render(request, "view_books.html",  books_dict)
 
def edit_book(request,bookId):
    book =Book.objects.get(id=bookId)
    book_dict={
            'book':book
        }
    if request.method == "POST":
        name = request.POST['name']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
 
        book.name= name
        book.author = author
        book.isbn = isbn
        book.category = category
        book.save()
        
        alert = True
        
        return render(request, "edit_book.html")
    return render(request, "edit_book.html",book_dict)
 

     
def index(request):
    return render(request, "index.html")