from django.shortcuts import render

def home_page_view(request):
    return render(request, 'home3.html')

def contact_page_view(request):
    return render(request, 'pages/contact.html')

def n404_page_view(request):
    return render(request, 'pages/404.html')

def about_us_page_view(request):
    return render(request, 'pages/about-us.html')

def user_wishlist_page_view(request):
    return render(request, 'pages/user-wishlist.html')