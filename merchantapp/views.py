from django.shortcuts import render,HttpResponse
from fmiapp.models import MerchantInfo,FarmerInfo
from farmerapp.models import FarmerSellProduct
from .models import orderDetail

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

    detail = orderDetail(email= email,customer=customer, address = address, panno=panno, gstno=gstno, product=product, qty=qty, price=price,city=city,state=state,zip=zip,merchantName=merchantName,merchantId=merchantId,farmerName=farmerName,farmerId=farmerId)
    detail.save()
    soldProduct.delete()
    return redirect(reverse('merchantapp'))

def purchasedprod(request):
    if request.session['merchant']:
        merchantobj = MerchantInfo.objects.get(userid=request.session['merchant'])
        merchantId = merchantobj.aadharno

        # orderObj = orderDetail.objects.all().merchantId[0]
        orderObj = orderDetail.objects.filter(merchantId = merchantId)
        print("************")
        print(orderObj[0].email)
        print("************")
        context = {'orderObj':orderObj}
        return render(request,"purchasedprod.html",context)