from django.shortcuts import render, HttpResponse, reverse, redirect
from .models import FarmerSellProduct, Profile, Tracker
from fmiapp.models import FarmerInfo
from merchantapp.models import orderDetail
from datetime import datetime
import requests


# Create your views here.
def farmerhome(request):
    try:
        if request.session['farmer']:
            farmerName = FarmerInfo.objects.get(userid=request.session['farmer'])
            ns = "Login Success Full"
            context = {'ns': ns, 'farmerName': farmerName}
            return render(request, 'farmerhome.html', context)
    except Exception as e:
        print(e)
    return render(request, 'login.html')


def uploadProd(request):
    if request.session['farmer']:
        farmer_name = FarmerInfo.objects.get(userid=request.session['farmer'])

        print(farmer_name, request.session['farmer'])
        if request.method == 'POST':
            qty = request.POST['qty']
            price = request.POST['price']
            productName = request.POST['productName']
            print(price, productName, qty)
            products = FarmerSellProduct.objects.create(farmerName=farmer_name, qty=qty, productName=productName,
                                                        price=price)
            print(price, productName, qty)
            print(products)
            ns = "Product Added"
            context = {'ns': ns}
    return render(request, 'farmerhome.html', context)


# Logout
def logout(request):
    request.session['farmer'] = None
    return render(request, 'login.html')


def changepasword(request):
    try:
        if request.session['farmer']:
            farmerName = FarmerInfo.objects.get(userid=request.session['farmer'])
            ns = "Login Success Full"
            context = {'ns': ns, 'farmerName': farmerName}
            return render(request, 'farmerchangepwd.html', context)
    except Exception as e:
        print(e)
    return render(request, 'login.html')
    # return HttpResponse('Change Ps')


def changepwd(request):
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    msg = 'Message ='
    if newpassword != confirmpassword:
        msg = msg + ' New password is not machted with confirm password!'
        return render(request, 'farmerchangepwd.html', {'msg': msg})
    farmer = request.session['farmer']
    print('*********')
    print(farmer)
    print(oldpassword)
    print(newpassword)
    print(confirmpassword)
    print('*********')
    try:
        obj = FarmerInfo.objects.get(userid=farmer, password=oldpassword)
        obj = get_object_or_404(Profile, username=username)
        print(fil)
        print('Try Third')
        return redirect('farmerapp:logout')
    except Exception as e:
        print(e)
        msg = msg + ' Old Password is not match!'
    return render(request, 'farmerchangepwd.html', {'msg': msg})


def prodlist(request):

    farmerName = FarmerInfo.objects.get(userid=request.session['farmer'])
    products = FarmerSellProduct.objects.filter(farmerName=farmerName)
    context = {'products': products, 'farmerName': farmerName}
    for product in products:
        print(product)

    return render(request, 'prodList.html', context)


# Remove Product
def removeprod(request, id):
    product = FarmerSellProduct.objects.filter(id=id)
    print(product)
    product.delete()
    return redirect(reverse('farmerapp:prodlist'))


def sold(request):
    try:
        if request.session['farmer']:
            merchantobj = FarmerInfo.objects.get(userid=request.session['farmer'])
            merchantId = merchantobj.aadharno
            orderObj = orderDetail.objects.filter(farmerId=merchantId)
            print("************")
            print(orderObj[0].qty)
            # print(orderObj)
            print("************")
            context = {'orderObj': orderObj,'farmerName':merchantobj}
            return render(request, "sold.html", context)
    except Exception as e:
        print(e)
    return render(request, 'login.html')


def updateStatus(request):
    if request.method == 'POST':
        orderId = request.POST['orderId']
        status = request.POST['status']
        updateDate = datetime.now()
        orderObj = orderDetail.objects.filter(id=orderId).update(track_update=status)
        order = orderDetail.objects.get(id=orderId)
        trackObj = Tracker(orderId=order, orderStatus=status)
        trackObj.save()
    return redirect(reverse('farmerapp:sold'))


def currentprice(request):
    try:
        if request.session['farmer']:
            farmerName = FarmerInfo.objects.get(userid=request.session['farmer'])
            context = {'farmerName': farmerName}
            return render(request, 'currentprice.html', context)
    except Exception as e:
        print(e)
    return render(request, 'login.html')


def socialpage(request):
    try:
        if request.session['farmer']:
            request.session['smUser'] = request.session['farmer']
            return redirect(reverse('irrigreatapp:bloghome'))
    except Exception as e:
        print(e)
    return redirect(reverse('irrigreatapp:bloghome'))