from django.shortcuts import render,redirect
from. models import *
# Create your views here.
def index (request):
    return render(request,'mybooks/index.html')
def aboutus (request):
    return render(request,'mybooks/aboutus.html')
def masterpage (request):
    return render(request,'mybooks/masterpage.html')
def login (request):
    if request.method=='POST':
        email=request.POST["email"]
        password=request.POST["password"]
        if Customer.objects.filter(email=email,password=password).exists():
            return redirect("mybooks:seeallbooks")
        else:
            return render(request,'mybooks/login.html',{"msg":"invalid email or password"})
    return render(request,'mybooks/login.html')
def register (request):
    if request.method=='POST':
        email=request.POST["email"]
        password=request.POST["pswd1"]
        cust=Customer(email=email,password=password)
        cust.save()
        return redirect("mybooks:login")
    return render(request,'mybooks/register.html')
def seeallbooks (request):
    books=Books.objects.all()
    return render(request, 'mybooks/seeallbooks.html',{"books":books})
def addbooks (request):
    if request.method=='POST':
       text=request.POST["text1"]
       review=request.POST["text2"] 
       file=request.FILES["file1"]       
       book=Books(name=text,review=review,image=file)
       book.save()
       return redirect("mybooks:seeallbooks")
    return render(request,'mybooks/addbooks.html')
def reviews (request,bid):
    books=Books.objects.get(id=bid)
    return render(request,'mybooks/reviews.html',{"books":books})

def like (request):
    books=liked.objects.all()
    return render(request,'mybooks/like.html',{"books":books})
def add_to_liked (request,bid):
    if request.method=='POST':
        books=Books.objects.get(id=bid)
        book,created=liked.objects.get_or_create(book=books)
        if not created:
            book.save()
    return redirect("mybooks:seeallbooks")
def remove (request,bid):
    liked.objects.get(id=bid).delete()
    return redirect('mybooks:like')

    
