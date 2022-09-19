from django.shortcuts import render,HttpResponse
from .models import FarmerSellProduct,Profile
from fmiapp.models import FarmerInfo
from merchantapp.models import orderDetail
# Create your views here.
def farmerhome(request):
    try:
        if request.session['farmer']:
            farmerName = FarmerInfo.objects.get(userid=request.session['farmer'])
            ns = "Login Success Full"
            context = {'ns': ns, 'farmerName': farmerName}
            return render(request, 'farmerhome.html', context)
    except:
        return render(request, 'login.html')


def uploadProd(request):
    if request.session['farmer']:
        ns = "Login Success Full"
        print("Login Success Full")
        farmerName = FarmerInfo.objects.get(userid = request.session['farmer'] )

        print(farmerName,request.session['farmer'])
        if request.method == 'POST':
            qty = request.POST['qty']
            price = request.POST['price']
            productName = request.POST['productName']
            print(price,productName,qty)
            products = FarmerSellProduct.objects.create(farmerName = farmerName,qty= qty,productName = productName, price= price)
            print(price, productName, qty)
            print(products)
    return HttpResponse("Post SUbmit")
# Logout
def logout(request):
    request.session['farmer'] = None
    return render(request, 'login.html')

def prodlist(request):
    farmerName = FarmerInfo.objects.get(userid=request.session['farmer'])
    products = FarmerSellProduct.objects.filter(farmerName=farmerName)
    context = {'products':products,'farmerName':farmerName}
    for product in products:
        print(product)

    return  render(request,'prodList.html',context)


# Remove Product
def removeprod(request,id):
    product = FarmerSellProduct.objects.filter(id=id)
    print(product)
    product.delete()
    return HttpResponse("Delete")


def sold(request):
    if request.session['farmer']:
        merchantobj = FarmerInfo.objects.get(userid=request.session['farmer'])
        merchantId = merchantobj.aadharno

        # orderObj = orderDetail.objects.all()

        orderObj = orderDetail.objects.filter(farmerId = merchantId)
        print("************")
        print(orderObj[0].qty)
        # print(orderObj)
        print("************")
        context = {'orderObj':orderObj}
        return render(request,"sold.html",context)