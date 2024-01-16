from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
from django.core.mail import send_mail
import razorpay
import random
import requests
from django.http import JsonResponse

# from django .http import HttpResponse
# def index (request):
#     return HttpResponse('<h1>Hello good morning</h1>')
def ajax_validation(request):
	email=request.GET['email']
	print(">>>>>>>>>>>>>>>>AJAX DATA : ",email)
	data={'is_taken':User.objects.filter(email__iexact=email).exists()}

	return JsonResponse(data)
def index(request):
    try:
        user=User.objects.get(email=request.session['email'])
        wishlist=Wishlist.objects.filter(user=user)
        request.session['wishlist_count']=len(wishlist)
        cart=Cart.objects.filter(user=user)
        request.session['cart_count']=len(cart)
        return render (request,"index.html")
    except:
        return render (request,"index.html")
def home(request):
    return render (request,"home.html")
def farmer_home(request):
    return render (request,"farmer_home.html")
def about(request):
    return render (request,'about.html')
def contact(request):
    return render (request,'contact.html')


otp=random.randint(100000,900000)

def sign(request):
    if request.method=="POST":
        try:
             user=User.objects.get(email=request.POST['email'])
             print(">>>>>>>>>>>User object : ",user)
             msg="Email Alresdy exists !!!"
             return render(request,'sign up.html',{'error':msg})
        except:
              user= User.objects.create(
                 name=request.POST['name'],
                 email=request.POST['email'],
                 password=request.POST['pswd'],
                 user=request.POST['usertype'],
                 mobile=request.POST['mobile'],
                 address=request.POST['address']
                 )
              msg="Your Registration Done ..."
              print(">>>>>>>>>>",msg)
              url = "https://www.fast2sms.com/dev/bulkV2"
              querystring = {"authorization":"XjLAwfWdnihsI7bGreUQmY32tv8CaTJuZcEMqRKO9HDpgo6V10ZFDfiIJaVBNtWGCPgplscrjEXSkOe4","variables_values":otp,"route":"otp","numbers":user.mobile}

              headers = {
                'cache-control': "no-cache"
               }

              response = requests.request("GET", url, headers=headers, params=querystring)

              print(response.text)
              return render(request,'login.html',{'done':msg})
    else:
        return render(request,'sign up.html')
def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'],password=request.POST['pswd'])
            request.session['email']=user.email
            request.session['name']=user.name
            request.session['pswd']=user.password
            print(">>>>>>>>>session start : ",request.session['email'])
            if user.user=="farmer":
                return render(request,'farmer_home.html')
            else:
                return render(request,'index.html')
        except: 
            msg="Your email or password is not match !!!!"
            return render(request,'login.html',{'error': msg})
    else:
        return render(request,'login.html')

def logout(request):
    del request.session['email']
    del request.session['name']
    del request.session['pswd']
    try:
        del request.session['wishlist_count']
        del request.session['wf']

    except:
        pass
    print(">>>>>>>>>>>>>>>>>>>>>>>>LOGOUT")
    return redirect('login')
def forgot(request):
    if request.method=='POST':
        try:
             user=User.objects.get(email=request.POST['email'])
             subject = 'OTP registration number'
             otp=random.randint(1000,9999)
             message = f'Hi {user.name},your OTP number is :{otp}'
             email_from = settings.EMAIL_HOST_USER
             recipient_list = [user.email, ]
             send_mail( subject, message, email_from, recipient_list )
             return render(request,'verify.html',{'otp':str(otp),'email':user.email})
        except:
            msg="No such email found !!!!!"
            return render(request,'forgot.html',{'error':msg})
    else:
        return render(request,'forgot.html')
def verify(request):
    if request.method=="POST":
        otp=request.POST['otp']
        uotp=request.POST['uotp']
        email=request.POST['email']
        if otp==uotp:
            return render(request,'create_password.html',{'email':email})
        else:
            msg="OTP doesn't Matched!!!!"
            return render(request,'verify.html',{'error':msg})
    else:
        msg="Something went worng please try again !!!"
        return render(request,'verify.html',{'error':msg})
def create_password(request):
    if request.method=="POST":
        email=request.POST['email']
        npswd=request.POST['npswd']
        cnpswd=request.POST['cnpswd']
        if npswd==cnpswd :
            user=User.objects.get(email=email)
            user.password=npswd
            user.save()
            return render(request,'login.html',{'email':email})
        else:
            msg="new password or confirm password are not matched !!"
            return render(request,'create_password.html',{'error':msg})
    else:
        msg="Something went wrong please try again later"
        return render(request,'create_password.html',{'error':msg})
def change_password(request):
    if request.method=="POST":
        opswd=request.POST['opswd']
        npswd=request.POST['npswd']
        cnpswd=request.POST['cnpswd']
        if opswd==request.session['pswd']:
            if npswd==cnpswd:
                user=User.objects.get(email=request.session['email'])
                user.password=npswd
                user.save()
                return redirect('login')
            else:
                msg= "New password or confirm password are not match !!! "
                return render(request,"change_password.html",{'error':msg})
        else:
            msg= "old password is not matched !!! "
            return render(request,"change_password.html",{'error':msg})
    else:
        return render(request,'Change_password.html')
def farmer_change_pas(request):
    if request.method=="POST":
        opswd=request.POST['opswd']
        npswd=request.POST['npswd']
        cnpswd=request.POST['cnpswd']
        if opswd==request.session['pswd']:
            if npswd==cnpswd:
                user=User.objects.get(email=request.session['email'])
                user.password=npswd
                user.save()
                return redirect('farmer_home')
            else:
                msg= "New password or confirm password are not match !!! "
                return render(request,"farmer_change_pas.html",{'error':msg})
        else:
            msg= "old password is not matched !!! "
            return render(request,"farmer_change_pas.html",{'error':msg})
    else:
        return render(request,'farmer_change_pas.html')
def add_product(request):
    category=Category.objects.all()
    for i in category:
        print(type(i))
        print(type(i.category))
    if request.method=="POST":
        farmer=User.objects.get(email=request.session['email'])
        cat=Category.objects.get(category=request.POST['category'])
        Product.objects.create(
            farmer=farmer,
            category=cat,
            pname=request.POST['p_name'],
            price=request.POST['p_price'],
            p_stock=request.POST['p_stock'],
            p_img=request.FILES['p_img'],
            description=request.POST['p_des']
        )
        msg="Product added...."
        return render(request,'add_product.html',{'done':msg , 'cat':category})
    else:
        return render(request,'add_product.html',{'cat':category})
def our_products(request):
    farmer=User.objects.get(email=request.session['email'])
    print("Using get method :- ",farmer)
    product=Product.objects.filter(farmer=farmer)
    print("Using filter method :- ",product)
    return render(request,'our_product.html',{'product':product})
def product_detail(request,pk):
        product=Product.objects.get(pk=pk)
        return render(request,'product_detail.html',{'product':product})
def update(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
        farmer=User.objects.get(email=request.session['email'])
        product.farmer=farmer
        product.pname=request.POST['p_name']
        product.price=request.POST['p_price']
        product.p_stock=request.POST['p_stock']
        try:
            product.p_img=request.FILES['p_img']
        except:
            pass
        product.description=request.POST['p_des']
        product.save()
        return redirect('our_products')
    else:
        return render(request,'update.html',{'product':product})    
def delete(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('our_products')
def create_blog(request):
    if request.method=="POST":
        user=User.objects.get(email=request.session['email'])
        Blog.objects.create(
            user=user,
            blog_title=request.POST['btitle'],
            blog_img=request.FILES['bimg'],
            desc=request.POST['bdesc']
            )
        return render(request,'create_blog.html')

    else:
        return render(request,'create_blog.html')
def my_blog(request):
    farmer=User.objects.get(email=request.session['email'])
    blogs=Blog.objects.filter(user=farmer)
    return render(request,'my_blog.html',{'blogs':blogs})
def shop(request):
    shops=Product.objects.all()
    return render(request,'shop.html',{'shop':shops})
def shop_detail(request,pk):
    prods=Product.objects.get(pk=pk)
    return render(request,'shop_detail.html',{'prods':prods})
    

def add_to_wishlist(request,pk):
    user=User.objects.get(email=request.session['email'])
    prod=Product.objects.get(pk=pk)
    try:
        w1=Wishlist.objects.get(user=user,product=prod)
        return redirect('wishlist')
    except:
        w2=Wishlist.objects.create(user=user,product=prod)
        return redirect('wishlist')

def wishlist(request):
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.filter(user=user)
    request.session['wishlist_count']=len(wishlist)
    return render(request,'wishlist.html',{'wishlist':wishlist})

def remove_wishlist(request,pk):
    user=User.objects.get(email=request.session['email'])
    product=Product.objects.get(pk=pk)  
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    request.session['wf']=True
    return redirect ('wishlist')

def add_to_cart(request,pk):
    request.session['cart_flag']=True
    user=User.objects.get(email=request.session['email'])
    prod=Product.objects.get(pk=pk)
    try:
        Cart.objects.get(user=user,product=prod)
        return redirect('cart')
    except:
        Cart.objects.create(
            user=user,
            product=prod,
            qty=1,
            availability=True,
            total=prod.price,
            )
        return redirect('cart')

def cart(request):
    request.session['cart_flag']=True
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.filter(user=user,payment_status=False)
    net_price=0
    for i in cart:
        net_price+=i.total
    request.session['cart_count']=len(cart)

    try:
        client = razorpay.Client(auth=(settings.KEY_ID,settings.KEY_SECRET))
        payment=client.order.create({ "amount":(net_price)*100, "currency": "INR", "receipt": "order_rcptid_11" })
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",payment)
        global payment_id   
        payment_id=payment['id']
        cart.razorpay_order_id=payment['id']
        # cart.save()
        for i in cart:
            i.save()
        return render(request,'cart.html',{'cart':cart,'net_price':net_price,'payment':payment,'total':(net_price-1)*100})
    except:
        return render(request,'cart.html',{'cart':cart,'net_price':net_price-1,'total':(net_price-1)*100})

   

def success(request):
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.filter(user=user,payment_status=False)
    net_price=0
    for i in cart:
        net_price+=i.total
        i.payment_status=True
        i.save()
        i.delete()

    transaction=Transaction.objects.create(
        user=user,
        grand_amount=net_price,
        trans_id=payment_id,
    )
    return render(request,'success.html')

def remove_cart(request,pk):
    request.session['cart_flag']=False
    user=User.objects.get(email=request.session['email'])
    product=Product.objects.get(pk=pk)  
    cart=Cart.objects.get(user=user,product=product)
    cart.delete()
    request.session['wf']=True
    return redirect ('cart')

def change_qty(request,pk):
    prod=Product.objects.get(pk=pk)
    cart=Cart.objects.get(product=prod)
    cart.qty=request.POST['qty']
    cart.total=(prod.price)*int(cart.qty)
    cart.save()
    return redirect('cart')

def customer_show_blog(request):
    blog=Blog.objects.all()
    return render(request,'customer_show_blog.html',{'blog':blog})
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Customer Dashboard >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def c_dashboard(request):
    user=User.objects.get(email=request.session['email'])
    return render(request,'c_dashboard.html',{'user':user})
def farmer_c_dashboard(request):
    user=User.objects.get(email=request.session['email'])
    return render(request,'farmer_c_dashboard.html',{'user':user})
def dash_header(request):
    user=User.objects.get(email=request.session['email'])
    return render(request,'dash_header.html',{'user':user})
def farmer_dash_header(request):
    user=User.objects.get(email=request.session['email'])
    return render(request,'farmer_dash_header.html',{'user':user})

def c_dash_profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=='POST':
        user.name=request.POST['name']
        try:
            user.image=request.FILES['image']
        except:
            pass
        user.email=request.POST['Email']
        user.password=request.POST['password']
        user.mobile=request.POST['contact']
        user.user=request.POST['utype']
        user.address=request.POST['address']
        user.save()
        return redirect('c_dashboard')
    else:
        return render(request,'c_dash_profile.html',{'user':user})
def farmer_c_dash_profile(request):
        user=User.objects.get(email=request.session['email'])
        if request.method=='POST':
            user.name=request.POST['name']
            try:
                user.image=request.FILES['image']
            except:
                pass
            user.email=request.POST['Email']
            user.password=request.POST['password']
            user.mobile=request.POST['contact']
            user.user=request.POST['utype']
            user.address=request.POST['address']
            user.save()
            return redirect('farmer_dash_header')
        else:
            return render(request,'farmer_c_dash_profile.html',{'user':user})
def d_cart(request):
    request.session['cart_flag']=True
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.filter(user=user)
    return render(request,'d_cart.html',{'cart':cart,'user':user})
def rd_cart(request,pk):
     user=User.objects.get(email=request.session['email'])
     product=Product.objects.get(pk=pk)  
     cart=Cart.objects.get(user=user,product=product)
     cart.delete()
     request.session['wf']=True
     return redirect ('d_cart')
def d_wish(request):
     user=User.objects.get(email=request.session['email'])
     wishlist=Wishlist.objects.filter(user=user)
     return render (request,'d_wish.html',{'wishlist':wishlist,'user':user})
def rd_wish(request,pk):
    user=User.objects.get(email=request.session['email'])
    product=Product.objects.get(pk=pk)  
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    request.session['wf']=True
    return redirect ('d_wish')
def d_order(request):
    user=User.objects.get(email=request.session['email'])
    cart=Cart.objects.filter(user=user)
    transaction=Transaction.objects.filter(user=user)
    return render(request,'d_order.html',{'cart':cart,'user':user,'trans':transaction})
def farmer_c_my_blog(request):
    user=User.objects.get(email=request.session['email'])
    farmer=User.objects.get(email=request.session['email'])
    blogs=Blog.objects.filter(user=farmer)
    return render(request,'farmer_c_my_blog.html',{'blogs':blogs,'user':user})
def farmer_c_my_product(request):
    user=User.objects.get(email=request.session['email'])
    farmer=User.objects.get(email=request.session['email'])
    product=Product.objects.filter(farmer=farmer)
    return render(request,'farmer_c_my_product.html',{'product':product,'user':user})
