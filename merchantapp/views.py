from django.shortcuts import render,HttpResponse
from fmiapp.models import MerchantInfo
from farmerapp.models import FarmerSellProduct
from .models import orderDetail

# Create your views here.
def merchanthome(request):
    if request.session['merchant']:
        merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
        allProduct = FarmerSellProduct.objects.all()
        print(allProduct)
        context = {'merchantName':merchantName,'allProduct':allProduct}
        print('-------')
        print(request.session['merchant'])
        print('-------')
    return render(request,'merchanthome.html',context )

def viewProd(request,id):
    merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
    product = FarmerSellProduct.objects.get(id = id)
    total = int(product.qty) * int(product.price)
    context = {'product':product,'total':total,'merchantName':merchantName}
    return render(request ,'viewprod.html',context)

def placeorder(request,id):
    merchantName = MerchantInfo.objects.get(userid=request.session['merchant'])
    merchantid = merchantName.userid
    print('-----')
    print("29"+merchantid)
    print('-----')
    product = FarmerSellProduct.objects.get(id=id)
    total = int(product.qty) * int(product.price)
    context = {'product': product,'merchantName': merchantName,'total':total}

    return render(request,'placeorder.html',context)

def purchaseCustomerDetail(request):
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
    merchantName = request.POST['merchantName']
    merchantId = request.POST['merchantId']
    print("MERCHANT id-"+merchantId)
    detail = orderDetail(email= email,customer=customer, address = address, panno=panno, gstno=gstno, product=product, qty=qty, price=price,city=city,state=state,zip=zip,merchantName=merchantName,merchantId=merchantId)
    detail.save()
    productid = request.POST['productid']
    print('product: '+productid)
    soldProduct = FarmerSellProduct.objects.filter(id=productid)
    print('sold: '+soldProduct)
    soldProduct.delete()
    return HttpResponse('Congratulation you own that Items')