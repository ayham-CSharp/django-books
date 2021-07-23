from django.shortcuts import render, get_object_or_404,redirect
from .models import book
from django.urls import reverse
from .forms import add_book_form
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.
@login_required
def newBook(request):
  if request.method=='POST':
    add_form = add_book_form(request.POST,request.FILES)
    if add_form.is_valid():
      myform = add_form.save(commit=False)
      myform.publisher = request.user
      myform.save()
  else:
    add_form = add_book_form()
  template='add_book.html'
  data={'keyform':add_form}
  return render(request,template,data)

def allBooks(request):
  all_books = book.objects.all()
  data = {
      'books': all_books,
  }
  return render(request,'book_list.html',data)
def singleBook(request,slug):
  one_book = get_object_or_404(book,slug=slug)
  intTo =int(one_book.bookLike.count())-1
  data = {
      'title':'hey',
      'book': one_book,
      'tota':intTo,
  }
  return render(request,'book_detail.html',data)

def like_dislike(request,slug):
    bookall = book.objects.get(slug=slug)
    is_like=False
    if request.method=='POST':
      if request.user in bookall.bookLike.all():
        bookall.bookLike.remove(request.user)
        is_like=False
      else:
        bookall.bookLike.add(request.user)
        is_like=True
      total =bookall.bookLike.count()
      alldata={'is_like':is_like,'tx':total}
      return JsonResponse(alldata,safe=False)
    return redirect(reverse('books:singlebook',kwargs=slug))
    




