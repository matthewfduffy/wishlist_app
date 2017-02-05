from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import *

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.login(email, password)
        if "errors" in user:
            for error in user["errors"]:
                messages.error(request, error)
            return redirect('/')
        else:
            request.session["username"] = user["user"].username
            request.session["id"] = user["user"].id
            return redirect('/main')
    else:
        return redirect(reverse('/'))

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user = User.objects.add_user(username, first_name, last_name, email, password, confirm_password)
        if "errors" in user:
            for error in user["errors"]:
                messages.error(request, error)
            return redirect('/')
        else:
            request.session["username"] = user["user"].username
            request.session["id"] = user["user"].id
            return redirect('/main')
    else:
        return redirect('/')

def logout(request):
    del request.session['id']
    del request.session['username']
    return redirect('/')

def main(request):
    favorite = Saved.objects.filter(user=request.session['id'])
    all_items = WishList.objects.all()
    exclude = {}

    for f in favorite:
        for a in all_items:
            if a.id == f.id:
                exclude[a] = "exclude"

    for a in all_items:
        if a not in exclude:
            print "final list =", a.id

    context = {
        "all_items" : all_items,
        "favorite" : favorite,
        "exclude" : exclude


    }
    return render(request, 'main.html', context)

def delete(request, id):
    Saved.objects.get(id=id).delete()
    return redirect('/main')

def add(request):
    if "id" not in request.session:
        messages.error(request, "You need to be logged in")
        return redirect('/login')
    return render(request, 'add.html')

def add_item(request):
    if request.method == "POST":
        item = request.POST["product"]
        if WishList.objects.filter(item__iexact=item):
            messages.error(request, "Item or Product already exists")
            return redirect('/add')
        WishList.objects.create(item=item, user_id=request.session['id'])
    return redirect('/main')

def save(request, id):
    save = WishList.objects.get(id=id)
    try:
        Saved.objects.create(user_id=request.session['id'], item_id=save.id)
    except:
        messages.error(request, "that item is already in your favorites!")
        return redirect ('/main')

    return redirect('/main')

def remove(request, id):
    Saved.objects.get(id=id).delete()
    return redirect('/main')

def delete(request, id):
    wish_item = WishList.objects.get(id=id)
    wish_item.delete()
    return redirect('/main')

def shared_user(request, id):
    item = Saved.objects.filter(id=id)
    users = Saved.objects.filter(id=item.id)
    context = {
        "item" : item,
        "users" : user
    }
    return render(request, 'item.html', context )
