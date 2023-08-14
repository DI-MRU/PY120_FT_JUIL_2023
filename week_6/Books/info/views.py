from django.shortcuts import render
from .models import Book, BookReview
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    data = [model_to_dict(book) for book in books] 
    return JsonResponse(data, safe=False)

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
        return JsonResponse(model_to_dict(book))
    except Book.DoesNotExist:
        return JsonResponse({'Try Again : Book not found'}, status = 404)

@csrf_exempt   
def create_book(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            new_book =Book.objects.create(**data)
            return JsonResponse({'message': 'Book created Nice GG','Id': new_book.id})
        except json.JSONDecodeError:
            return JsonResponse({'Error': 'Error'}, status = 400)
    return JsonResponse({'error': 'Invalid'})

