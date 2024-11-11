from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def fun2(request):
    return HttpResponse("HII")
def fun3(request):
    return render(request,'new.html',{'name': 'vismaya'})
def fun4(request):
    context={
        'fruits':["apple","orange","grape"]
    }
    return render(request,'fruit.html',context)
def fun5(request):
    item=[
        {'name':'laptop','price':2000,'quantity':2},
        {'name':'mobile','price':1000,'quantity':3},
        {'name':'tv','price':4000,'quantity':5}
    ]
    return render(request,'item.html',{'items':item})
def fun6(request):
    item=[
        {'name':'laptop','price':2000,'available':'instock'},
        {'name':'mobile','price':1000,'available':'outstock'},
        {'name':'tv','price':4000,'available':'instock'},
        {'name':'haedphone','price':2500,'available':'instock'},
    ]
    return render(request,'product.html',{'items':item})
def fun7(request):
    data=usermodel.objects.all()
    return render(request,"all.html",{'data1':data})
def fun8(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        date=request.POST.get('date')
        user_obj=usermodel()
        user_obj.user_id=id
        user_obj.user_name=name
        user_obj.user_age=age
        user_obj.date=date
        user_obj.save()
    return render(request,"form.html")
def fun9(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        title=request.POST.get('title')
        author=request.POST.get('author')
        date=request.POST.get('date')
        isbn=request.POST.get('isbn')
        b=Book()
        b.book_id=id
        b.title=title
        b.author=author
        b.published_date=date
        b.isbn=isbn
        b.save()
    return render(request,'addbook.html')
def fun10(request):
    data=Book.objects.all()
    return render(request,'displaybook.html',{'display':data})
def fun11(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        a=employee()
        a.employee_id=id
        a.name=name
        a.age=age
        a.save()
        return redirect('v')    
    return render(request,'add_employee.html')
def fun12(request):
    data=employee.objects.all()
    return render(request,'display_emp_details.html',{'display':data})
def fundelete_user(request,id):
    user=employee.objects.get(employee_id=id)
    user.delete()
    return redirect('v')
def update_user(request,id):
    user=employee.objects.filter(employee_id=id)
    if request.method == 'POST':
        ID=request.POST.get('id')
        name=request.POST.get('name')
        age=request.POST.get('age')
        user_obj=employee()
        user_obj.employee_id=ID
        user_obj.name=name
        user_obj.age=age
        user_obj.save()
        return redirect('v')
    return render(request,"update_employee.html",{'user1':user})


def fun13(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        description=request.POST.get('des')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        pro=Product()
        pro.name=name
        pro.description=description
        pro.price=price
        pro.quantity=quantity
        pro.save()
        return redirect('product_table')
    return render(request,'add_product.html')
def fun14(request):
    value=Product.objects.all()
    return render(request,'product_view.html',{'product':value})
def cus_add(request):
    if request.method == 'POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date=request.POST.get('dob')
        cus=Customer()
        cus.first_name=f_name
        cus.last_name=l_name
        cus.email=email
        cus.phone_number=phone
        cus.address=address
        cus.date_of_birth=date
        cus.save()
        return redirect('display_customer')
    return render(request,'add_customer.html')
def cus_display(request):
    value=Customer.objects.all()
    return render(request,'display_customer.html',{'customer':value})
def cus_update(request,id):
    update=Customer.objects.get(id=id)
    if request.method == 'POST':
        f_name=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        date=request.POST.get('dob')
        update.first_name=f_name
        update.last_name=l_name
        update.email=email
        update.phone_number=phone
        update.address=address
        update.date_of_birth=date
        update.save()  
        return redirect('display_customer')
    return render(request,'update_customer.html',{'update':update})
def cus_delete(request,id):
    value=Customer.objects.get(id=id)
    value.delete()
    return redirect('display_customer')

def blogcreate(request):
    if request.method == "POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        author=request.POST.get('author')
        created_at=request.POST.get('created_at')
        updated_at=request.POST.get('updated_at')
        blog=blogmodel()
        blog.title=title
        blog.content=content
        blog.author=author
        blog.created_at=created_at
        blog.updated_at=updated_at
        blog.save()
        return redirect('blog')
    return render(request,"blog_model.html")
def blog(request):
    blogs=blogmodel.objects.all()
    return render(request,"blogmodel_table.html",{'blog1':blogs})
def get_user(request):
    data=product_use.objects.all()
    return render(request,"product_view.html"),{'data1':data}


def add_organizer(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        obj=Organizer()
        obj.name=name
        obj.email=email
        obj.phone_number=number
        obj.save()
        return redirect('display_organizer')
    return render(request,'em_add_organizer.html')
def add_event(request):
    org_names=Organizer.objects.all()
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        obj=Event()
        obj.title=title
        obj.date=date
        obj.location=location
        obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('display_event')
    return render(request,'em_add_event.html',{'org_list':org_names})
def display_organizer(request):
    org=Organizer.objects.all()
    return render(request,'em_display_organizer.html',{'org':org})
def display_event(request):
    eve=Event.objects.all()
    return render(request,'em_display_event.html',{'event':eve})
def update_organizer(request,id):
    obj=Organizer.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('phone')
        obj.name=name
        obj.email=email
        obj.phone_number=number
        obj.save()
        return redirect('display_organizer')
    return render(request,'em_update_organizer.html',{'obj':obj})
def update_event(request,id):
    orgg=Organizer.objects.all()
    obj=Event.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        date=request.POST.get('date')
        location=request.POST.get('location')
        obj.title=title
        obj.date=date
        obj.location=location
        obj.organizer=Organizer.objects.get(id=request.POST.get('org'))
        obj.save()
        return redirect('display_event')
    return render(request,'em_update_event.html',{'obj':obj,'organize':orgg})
def delete_organizer(request,id):
    dlt=Organizer.objects.get(id=id)
    dlt.delete()
    return redirect('display_organizer')
def delete_event(request,id):
    dlt=Event.objects.get(id=id)
    dlt.delete()
    return redirect('display_event')






def add_product_cate(request):
    data=Category.objects.all()
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        obj=Product_cate()
        obj.name=name
        obj.price=price
        obj.stock_quantity=quantity
        obj.category=Category.objects.get(id=request.POST.get('categ'))
        obj.save()
        return redirect('display_product_cate')
    return render(request,'c_add_product.html',{'dataa':data})
def display_product_cate(request):
    data=Product_cate.objects.all()
    return render(request,'c_display_product.html',{'dataa':data})
def update_product_cate(request,id):
    data=Category.objects.all()
    obj=Product_cate.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('name')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        obj.name=name
        obj.price=price
        obj.stock_quantity=quantity
        obj.category=Category.objects.get(id=request.POST.get('categ'))
        obj.save()
        return redirect('display_product_cate')
    return render(request,'c_update_product.html',{'dataa':data,'obj':obj})
def delete_product_cate(request,id):
    data=Product_cate.objects.get(id=id)
    data.delete()
    return redirect('display_product_cate')

def hotel_display(request):
    val=Hotel.objects.all()
    return render(request,'hotel_view.html',{'value':val})
def booking_display(request,id):
    htl=Hotel.objects.get(id=id)
    val=Booking.objects.filter(hotel=htl)
    return render(request,'hotel_booking_view.html',{'values':val,'htl':htl})
def update_booking(rq,id):
    val=Booking.objects.get(id=id)
    if rq.method == 'POST':
        nm=rq.POST.get('name')
        val.guest_name=nm
        val.save()
        return redirect('bookings')
    return render(rq,'hotel_bkn_update.html',{'x':val})
def delete_booking(rq,id):
    val=Booking.objects.get(id=id)
    val.delete()
    return redirect('bookings')
def rating_3(req):
    rate=Hotel.objects.filter(Q(rating__gte=5))
    return render(req,'hotel_view.html',{'value':rate})


def user1(request):
    if request.method=='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=userform()
    return render(request,"users.html",{'form':form})

def u_profile(request):
    if request.method == 'POST':
        form=profile(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profileView')
    else:
        form=profile()
    return render(request,'users.html',{'form':form})
def profile_view(request):
    data=userProfile.objects.all()
    return render(request,'user_profile_view.html',{'dataa':data})
def profile_delete(request,id):
    data=userProfile.objects.get(id=id)
    data.delete()
    return redirect('profileView')

def hm(request):
    return render(request,'login.html')

def post_form(request):
    if request.method == 'POST':
        form=postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('postview')
    else:
        form=postform()
    return render(request,'post_form.html',{'form':form})
def post_view(request):
    data=Post1.objects.all()
    return render(request,'view_post.html',{'dataa':data})
def post_update(request,id):
    data=Post1.objects.get(id=id)
    if request.method=='POST':
        title=request.POST.get('title')
        content=request.POST.get('content')
        data.title=title
        data.content=content
        data.save()
        return redirect('postview')
    return render(request,'update_form.html',{'dataa':data})
def post_delete(request,id):
    data=Post1.objects.get(id=id)
    data.delete()
    return redirect('postview')

def add_userRegistration(request):
    if request.method == 'POST':
        data=UserRegistrationForm(request.POST)
        if data.is_valid():
            data.save()
    else:
        data=UserRegistrationForm()
    return render(request,'users.html',{'form':data})

def add_image(request):
    if request.method == 'POST':
        title=request.POST.get('title')
        image=request.POST.get('img')
        obj=Image()
        obj.title=title
        obj.image=image
        obj.save()
    return render(request,'image_form.html')
def view_image(request):
    data=Image.objects.all()
    return render(request,'image_view.html',{'dataa':data})

def product_base(request):
    return render(request,'base1.html')
def product_product(request):
    return render(request,'product1.html')






