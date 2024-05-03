from django.shortcuts import render
from app.models import User,Product,Cart,ProductCategory
from userapp import views
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.



def loginFunction(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(email=username, password=password)
        if user is not None:
            login(request, user)
            print("user::::::",user.is_superuser)
            if user.is_superuser == True:
                request.session['username']=user.email
                request.session['user_id']=user.id
                request.session['is_superuser']=True
                return redirect('home:productlist')
            else:
                cart_count = Cart.objects.filter(user_id=User.objects.get(id=user.id),status=True)
                print(cart_count)

                request.session['username']=user.email
                request.session['user_id']=user.id
                request.session['is_superuser']=False
                return redirect('landing')
        else:
            messages.add_message(request, messages.WARNING,
                                 'Please verify credentials you entered!'
                                 )
            return redirect('home:login')
    return render(request,'login.html')

def Reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        password = request.POST.get('password')
        user = User.objects.create(name=name,email=mail,phone_number=phone,city=city,pincode=pincode,address=address,username=mail)
        user.set_password(password)
        user.save()    
        return redirect('home:login')
    return render(request,'register.html')

def Productlist(request):
    product = Product.objects.all()
    print("product",product)
    context = {
            'product':product,
        }
    return render(request,'productlist.html',context)

def logoutView(request):
    logout(request)
    return redirect('home:login')

def addproduct(request):
    product = ProductCategory.objects.all()
    context={'product':product}
    return render(request,'addproduct.html',context)


def addproductcatogery(request):
    return render(request,'addcategory.html')

def Saveproduct(request):
        name = request.POST.get('name')
        starpcolor = request.POST.get('category')
        print("eeeeeeeeeee",starpcolor)
        highlights = request.POST.get('highlights')
        price = request.POST.get('price')
        category_obj = ProductCategory.objects.get(id=starpcolor)

        print("qqqqqqqqqqq",category_obj)
        Product.objects.create(product_category_id=category_obj,name=name,category=category_obj.name,status="ACTIVE",highlights=highlights,price=price)  
        return redirect('home:productlist')

def SaveCategory(request):
        name = request.POST.get('name')
        category = request.POST.get('category')
        ProductCategory.objects.create(name=name,category=category)  
        return redirect('home:categorylist')

@login_required
def Editproduct(request, id):
    product = Product.objects.get(product_id=id)
    context={'product':product}
    if request.method == 'POST':
        name = request.POST.get('name') 
        starpcolor = request.POST.get('starpcolor') 
        highlights = request.POST.get('highlights') 
        price = request.POST.get('price') 
        product.name ,product.starpcolor , product.highlights , product.price = name , starpcolor , highlights , price
        product.save()
        return redirect('home:productlist')
    return render(request,'product_edit.html',context)

def DeleteProduct(request,id):
    product = Product.objects.get(product_id=id)
    product.delete()
    return redirect('home:productlist')

@login_required
def Editcategory(request, id):
    product = ProductCategory.objects.get(id=id)
    context={'product':product}
    if request.method == 'POST':
        name = request.POST.get('name') 
        category = request.POST.get('category') 
        product.name ,product.category = name , category 
        product.save()
        return redirect('home:categorylist')
    return render(request,'category_edit.html',context)

def categorylist(request):
    product = ProductCategory.objects.all()
    print("product",product)
    context = {
            'product':product,
        }
    return render(request,'product_category.html',context)

def DeleteCategory(request,id):
    product = ProductCategory.objects.get(id=id)
    product.delete()
    return redirect('home:categorylist')