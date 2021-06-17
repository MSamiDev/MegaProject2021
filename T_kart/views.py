from ast import arg
from multiprocessing.sharedctypes import Value
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse, JsonResponse
from T_kart.models import *
from django.core.paginator import Paginator
from django.views import View
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.


class index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        kart = request.session.get('kart')
        if kart:
            quantity = kart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        kart.pop(product)
                    else:
                        kart[product] = quantity-1
                else:
                    kart[product] = quantity+1
            else:
                kart[product] = 1
        else:
            kart = {}
            kart[product] = 1

        request.session['kart'] = kart
        return redirect('/t-kart/')

    def get(self, request):
        kart = request.session.get('kart')
        if not kart:
            request.session['kart'] = {}

        products = Product.objects.all()
        product_pagination = Paginator(products, 9)
        page_number = request.GET.get('page')
        try:
            page_obj = product_pagination.get_page(page_number)
        except PageNotAnInteger:
            # if page_number is not an integer then assign the first page
            page_obj = product_pagination.page(1)
        except EmptyPage:
            # if page is empty then return last page
            page_obj = product_pagination.page(product_pagination.num_pages)
        context = {'page_obj': page_obj}
        return render(request, 'T_kart/Shop.html', context)

class Signup(View):
    def get(self, request):
        return render(request, 'T_kart/SignUp.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('/t-kart/login/')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            print(error_message)
            return render(request, 'T_kart/SignUp.html', data)

    def validateCustomer(self, customer):
        error_message = None
        if (not customer.first_name):
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = 'First Name must be 4 char long or more'
        elif not customer.last_name:
            error_message = 'Last Name Required'
        elif len(customer.last_name) < 4:
            error_message = 'Last Name must be 4 char long or more'
        elif not customer.phone:
            error_message = 'Phone Number required'
        elif len(customer.phone) < 10:
            error_message = 'Phone Number must be 10 char Long'
        elif len(customer.password) < 6:
            error_message = 'Password must be 6 char long'
        elif len(customer.email) < 5:
            error_message = 'Email must be 5 char long'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'
        # saving

        return error_message

""" 
class signUp(View):
    def get(self,request):
        return render(request, 'T_kart/SignUp.html')


    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        email = postData.get('email')
        phone = postData.get('phone')
        password = postData.get('password')
        #validation
        
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        } 

        
        

        
        print(first_name, last_name, email, phone, password)

        customer = Customer(first_name=first_name, last_name=last_name, email=email, phone=phone, password=password)
        customer.register()

        return redirect('/t-kart/') 


        else:
            context = {'values': value }
            return render(request, 'T_kart/SignUp.html', context) 


 """

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'T_kart/Login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('T_kart:myAccount')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        print(email, password)
        return render(request, 'T_kart/Login.html', {'error': error_message})

def logout(request):
    request.session.clear()
    return redirect('/t-kart/login/')

def myAccount(request):
    customer_session = request.session.get('customer')
    orders = Order.get_orders_by_customer(customer_session)
    id = request.session.get('customer')
    customer = Customer.get_customer_by_id(id)
    if customer:
        context = {'customer': customer, 'orders': orders}
        return render(request, 'T_kart/My-Account.html', context)
    else:
        return redirect('/t-kart/login/')

class productView(View):

    def post(self, request, slug):
        products = Product.objects.filter(product_slug=slug)
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        kart = request.session.get('kart')
        if kart:
            quantity = kart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        kart.pop(product)
                    else:
                        kart[product] = quantity-1
                else:
                    kart[product] = quantity+1
            else:
                kart[product] = 1
        else:
            kart = {}
            kart[product] = 1

        request.session['kart'] = kart
        return render(request, 'T_kart/ProductView.html', {'product': products[0]})
        #return redirect(reverse('T_kart:product-view', {'product': products[0]}))

    def get(self, request, slug):
        product = Product.objects.filter(product_slug=slug)
        return render(request, 'T_kart/ProductView.html', {'product': product[0]})

class kart(View):
    
    def post(self, request):
        product = request.POST.get('product')
        removeKart = request.POST.get('removeKart')
        remove = request.POST.get('remove')
        kart = request.session.get('kart')

        if kart:
            if removeKart:
                kart.pop(product)
            quantity = kart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        kart.pop(product)
                    else:
                        kart[product] = quantity-1
                else:
                    kart[product] = quantity+1
            else:
                kart[product] = 1
        else:
            kart = {}
            kart[product] = 1

        request.session['kart'] = kart
        return redirect('/t-kart/kart/')
   

    def get(self, request):
        ids = list(request.session.get('kart').keys())
        products = Product.get_products_by_id(ids)
        context = {'products': products}
        return render(request, 'T_kart/Kart.html', context)

class checkout(View):

    def get(self, request):
        ids = list(request.session.get('kart').keys())
        products = Product.get_products_by_id(ids)
        context = {'products': products, 'STRIPE_PUBLIC_KEY' : settings.STRIPE_PUBLIC_KEY }
        return render(request, 'T_kart/Checkout.html', context)
    
    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        company_name = request.POST.get('companyname')
        country = request.POST.get('country')
        address_line_1 = request.POST.get('addressline1')
        address_line_2 = request.POST.get('addressline2')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        TandC_agree = request.POST.get('checkbox')
        create_account = request.POST.get('createaccount')
        customer = request.session.get('customer')
        kart = request.session.get('kart')
        products = Product.get_products_by_id(list(kart.keys()))
        print(first_name, last_name, company_name, country, address_line_1, address_line_2, city, state, pincode, phone, email, TandC_agree, create_account, products)
        #return render(request, 'T_kart/Shop.html')

        for product in products:
            print(kart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          country=country,
                          city=city,
                          state=state,
                          address_line_1=address_line_1,
                          address_line_2=address_line_2,
                          pincode=pincode,
                          company_name=company_name,
                          phone=phone,
                          quantity=kart.get(str(product.id)),
                          total_price=product.price*kart.get(str(product.id))
                          )
            order.placeOrder()
        request.session['kart'] = {}




        return redirect('/t-kart/')

def wishlist(request):
    return render(request, 'T_kart/Wishlist.html')


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "https://127.0.0.1:8000"
        pl = {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                }
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card',],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': 2000,
                        'product_data': {
                            'name': 'Stubborn Attachments',
                            'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/t-kart/success/',
            cancel_url=YOUR_DOMAIN + '/t-kart/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id
        })

            