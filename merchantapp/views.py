from django.shortcuts import render,HttpResponse,redirect,reverse
from fmiapp.models import MerchantInfo,FarmerInfo
from farmerapp.models import FarmerSellProduct,Tracker
from .models import orderDetail
from django.http import HttpResponseRedirect

# Create your views here.
def merchanthome(request):
    if not request.session['merchant']:
        return render(request, 'login.html')
    if request.session['merchant']:
        merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
        allProduct = FarmerSellProduct.objects.all()
        print(allProduct)
        context = {'merchantName':merchantName,'allProduct':allProduct}
        print('-------')
        print(request.session['merchant'])
        print('-------')
    return render(request,'merchanthome.html',context )

def logout(request):
    request.session['merchant'] = None
    return render(request, 'login.html')


def viewProd(request,id):
    if not request.session['merchant']:
        return render(request, 'login.html')
    merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
    product = FarmerSellProduct.objects.get(id = id)
    sellerobj= FarmerInfo.objects.get(aadharno = product.farmerName)
    print('----viewProd')
    print(sellerobj.name)
    total = int(product.qty) * int(product.price)
    context = {'product':product,'total':total,'merchantName':merchantName,'sellerName':sellerobj.name}
    return render(request ,'viewprod.html',context)

def placeorder(request,id):
    if not request.session['merchant']:
        return render(request, 'login.html')
    merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantid = merchantName.userid
    print('-----')
    print("29 "+merchantid)
    print('-----')
    product = FarmerSellProduct.objects.get(id=id)
    print(product.farmerName)
    total = int(product.qty) * int(product.price)
    context = {'product': product,'merchantName': merchantName,'total':total}

    return render(request,'placeorder.html',context)

def purchaseCustomerDetail(request):
    if not request.session['merchant']:
        return render(request, 'login.html')
    productid = request.POST['productid']
    soldProduct = FarmerSellProduct.objects.get(id=productid)
    sellerobj = FarmerInfo.objects.get(aadharno=soldProduct.farmerName)

    email = request.POST['email']
    customer = request.POST['customer']
    address = request.POST['address']
    panno = request.POST['panno']
    gstno = request.POST['gstno']
    product = request.POST['product']
    qty = request.POST['qty']
    price = request.POST['price']
    city = request.POST['city']
    state = request.POST['state']
    zip = request.POST['zip']
    merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantId = merchantobj
    merchantName = merchantobj.name
    farmerName = sellerobj.name
    farmerId = sellerobj

    detail = orderDetail(email= email,customer=customer, address = address, panno=panno, gstno=gstno,productid=productid, product=product, qty=qty, price=price,city=city,state=state,zip=zip,merchantName=merchantName,merchantId=merchantId,farmerName=farmerName,farmerId=farmerId)
    detail.save()
    soldProduct.delete()
    # merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
    # merchantId = merchantobj.aadharno

    # orderObj = orderDetail.objects.all().merchantId[0]
    orderObj = orderDetail.objects.filter(merchantId=merchantId,productid=productid)
    print("************")
    print(orderObj[0].id)
    # print(merchantId)
    # print(productid)
    updateTrack = Tracker(orderId = orderObj[0].id)
    updateTrack.save()
    # return HttpResponse('purchaseCustomerDetail pass')
    return redirect(reverse('merchantapp:purchasedprod'))

def purchasedprod(request):
    if request.session['merchant']:
        merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
        merchantId = merchantobj.aadharno
        orderObj = orderDetail.objects.filter(merchantId = merchantId)

        context = {'orderObj':orderObj}
        return render(request,"purchasedprod.html",context)

def trackOrder(request):
    merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantId = merchantobj.aadharno
    orderObj = orderDetail.objects.filter(merchantId=merchantId)
    orderId = request.POST['orderId']
    track = Tracker.objects.filter(orderId=orderId)
    notFound = ''
    if  track.count() ==0:
        track={'orderStatus':'Not Found'}
        print('@@@@@@@@@@@@@@@@@@@')
        notFound = "This is not available for to track"
        print('@@@@@@@@@@@@@@@@@@@')
    # print(track)
    context ={'track':track,'orderObj':orderObj,'notFound':notFound}
    # return HttpResponseRedirect(reverse('merchantapp:purchasedprod',args=(context,)))
    return render(request,"purchasedprod.html",context)