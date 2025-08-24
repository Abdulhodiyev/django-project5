from django.shortcuts import render

def products_page_view(request):
    return render(request, 'product/product-cart.html')

def product_checkout_page_view(request):
    return render(request, 'product/product-checkout.html')

def product_detail_page_view(request):
    return render(request, 'product/product-detail.html')

def product_grid_page_view(request):
    return render(request, 'product/product-grid-sidebar-left.html')