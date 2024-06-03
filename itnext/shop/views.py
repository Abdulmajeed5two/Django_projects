from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from itnext import settings
from .models import Order, OrderItem, Product, Cart, CartItem
from .forms import AddToCartForm, ReviewForm, UpdateCartItemForm

def home_view(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'range': range(1, 6)
    }
    return render(request, 'home/home.html', context)

def header_view(request):
    return render(request, 'header/header.html')

def footer_view(request):
    return render(request, 'footer/footer.html')

def section_why(request):
    return render(request, 'sections/section_why.html')

def product_view(request):
    return render(request, 'sections/product_view.html')

def about_view(request):
    return render(request, 'about/about.html')

def contact_view(request):
    return render(request, 'contact/contact.html')

def services_view(request):
    return render(request, 'services/service.html')

def services_list(request):
    return render(request, 'services/services_list.html')

def services(request):
    return render(request, 'sections/services.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'sections/our_products.html', {'products': products, 'range': range(1, 6)})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = AddToCartForm()
    description = product.description  
    return render(request, 'sections/product_view.html', {'product': product, 'form': form, 'description': description})

@login_required(login_url='/login/')
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        cart = Cart.objects.create(user=request.user)

    if request.method == 'POST':
        if 'update_quantity' in request.POST:
            form = UpdateCartItemForm(request.POST)
            if form.is_valid():
                cart_item_id = form.cleaned_data['cart_item_id']
                quantity = form.cleaned_data['quantity']
                cart_item = get_object_or_404(CartItem, id=cart_item_id)
                cart_item.quantity = quantity
                cart_item.save()
        elif 'remove_item' in request.POST:
            cart_item_id = request.POST.get('cart_item_id')
            cart_item = get_object_or_404(CartItem, id=cart_item_id)
            cart_item.delete()
        return redirect('cart_detail')

    return render(request, 'sections/cart_detail.html', {'cart': cart})

@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')


@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        order = Order.objects.create(
            user=request.user,
            first_name=request.POST['fn'],
            last_name=request.POST['ln'],
            country=request.POST['cn'],
            address=request.POST['ad'],
            city=request.POST['tc'],
            state=request.POST['sc'],
            postal_code=request.POST['pz'],
            phone=request.POST['ph'],
            email=request.POST['em'],
            total=cart.get_total_price() + Decimal('5.00')  
        )
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                price=item.product.new_price,
                quantity=item.quantity
            )
        cart.items.all().delete()  # Clear the cart
        return redirect('order_success')

    return render(request, 'sections/checkout.html', {
        'cart': cart,
        'subtotal': cart.get_total_price(),
        'shipping': Decimal('5.00'),
        'total': cart.get_total_price() + Decimal('5.00')
    })

@login_required
def order_success(request):
    return render(request, 'sections/order_success.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'sections/all_products.html', {'products': products})


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {'form': form, 'product': product})
