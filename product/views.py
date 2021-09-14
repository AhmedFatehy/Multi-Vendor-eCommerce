from cart.cart import Cart
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AddToCartForm
from .models import Product


def product_detail(request, category_slug, product_slug):
    '''	Product detail & add to cart view '''
    cart = Cart(request)
    products = get_object_or_404(
        Product, category__slug=category_slug, slug=product_slug)

    if request.method == 'POST':
        form = AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            print(f"Product qty: {quantity}")
            cart.add(product_id=products.id, quantity=quantity, update_quantity=False)
            messages.success(request, 'Product added to cart!')
            return redirect('cart:cart_list')
    else:
        form = AddToCartForm()

    return render(request, 'product/single_product.html', {'products': products, 'form': form})
