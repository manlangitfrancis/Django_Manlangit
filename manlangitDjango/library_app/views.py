from django.shortcuts import render

def index(request):
    return render(request, 'library/index.html')

def available_books(request):
    return render(request, 'library/available_books.html')

def borrow_book(request):
    return render(request, 'library/borrow_book.html')
